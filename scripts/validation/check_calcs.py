#!/usr/bin/env python3
"""Check that the mechanical calculation documents match the canonical script.

Copyright (c) 2026 Kritvaos. Licensed under the Apache License, Version 2.0 (see LICENSE).

Addresses external-audit finding EXT-AUD-011 (calculation CI was a smoke run only).

What it does
------------
1. Imports ``mechanical/common-sizing/actuator_sizing.py`` and evaluates it with its
   committed ``INPUTS``.
2. **Regression check:** compares key results against the approved reference values
   in ``mechanical/common-sizing/expected_results.json`` (relative tolerance per entry).
   A change to INPUTS or formulas that moves a result fails until the reference file
   (and the documents) are deliberately updated in the same pull request.
3. **Document consistency check:** for each key result, verifies that the formatted
   value appears in the calculation document that reports it. This catches documents
   that were not updated after the script changed.

It does NOT validate the engineering assumptions or load paths - that remains the
independent reviewer's job (audit/mechanical/MECHANICAL_DESIGN_AUDIT.md).

Exit status: 0 = consistent, 1 = mismatch, 2 = script or reference missing.
Standard library only. Python 3.8+.
"""
import argparse
import importlib.util
import json
import sys
from pathlib import Path


def default_root() -> Path:
    return Path(__file__).resolve().parents[2]


def load_module(path: Path):
    spec = importlib.util.spec_from_file_location("actuator_sizing", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def compute(mod, p=None) -> dict:
    p = dict(mod.INPUTS) if p is None else p
    load = mod.load_cases(p)
    ts = {r["N"]: r for r in mod.torque_speed(p)["rows"]}
    sh = {c["case"]: c for c in mod.shaft(p)["cases"]}
    br = mod.bearings(p)
    checks = {c["bearing"].split(" ")[0]: c for c in br["checks"]}
    st = mod.stops(p)
    eff = mod.effective_inertia(p)
    lo, mid, hi = eff[(2e-5, 15)], eff[(5e-5, 20)], eff[(1e-4, 25)]
    return {
        "J_rod": load["J_rod"],
        "E_stop_rod_45": load["E_stop_rod"],
        "eff_J_low": lo["J"], "eff_E_low": lo["E"],
        "eff_J_mid": mid["J"], "eff_E_mid": mid["E"],
        "eff_J_high": hi["J"], "eff_E_high": hi["E"],
        "rotor_share_low_pct": 100 * lo["rotor_share"], "rotor_share_high_pct": 100 * hi["rotor_share"],
        "T_g": load["Tg"],
        "J_point": load["J_point"],
        "E_stop_45": load["E_stop"],
        "P_out": mod.torque_speed(p)["P_out"],
        "Tm_cont_20": ts[20]["Tm_cont"],
        "Tm_peak25_20": ts[20]["Tm_peak25"],
        "Kv_min_20": ts[20]["Kv_min"],
        "vm_kt_LC05": sh["LC-05 stall into single stop 25"]["vm_kt"],
        "vm_kt_LC03_25": sh["LC-03 peak 25"]["vm_kt"],
        "R_near_LC05": br["governing"]["R_near"],
        "s0_6001": checks["6001"]["s0_gov"],
        "s0_6202": checks["6202"]["s0_gov"],
        "T_stop_45": st["rows"][0]["T_stop_2mm_25mm"],
        "n_allow_20": st["n_allow_20Nm_rpm"],
    }


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description="Check calculation documents against actuator_sizing.py.")
    ap.add_argument("--root", type=Path, default=default_root())
    ap.add_argument("--write-reference", action="store_true",
                    help="overwrite expected_results.json values with the current results "
                         "(only after a reviewed change; keeps doc patterns)")
    a = ap.parse_args(argv)
    calc_dir = a.root / "mechanical" / "common-sizing"
    if not (calc_dir / "actuator_sizing.py").is_file():          # before migration Stage 4 (M)
        calc_dir = a.root / "mechanical" / "calculations"
    script = calc_dir / "actuator_sizing.py"
    ref_path = calc_dir / "expected_results.json"
    if not script.is_file() or not ref_path.is_file():
        print(f"check_calcs: missing {script if not script.is_file() else ref_path}")
        return 2
    results = compute(load_module(script))
    ref = json.loads(ref_path.read_text(encoding="utf-8"))
    errors = 0
    if a.write_reference:
        for key, entry in ref["results"].items():
            entry["value"] = round(results[key], 6)
        ref_path.write_text(json.dumps(ref, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print("check_calcs: reference values updated - update the documents and get review")
    for key, entry in ref["results"].items():
        if key not in results:
            print(f"ERROR   {key}: not produced by actuator_sizing.py")
            errors += 1
            continue
        got, exp, tol = results[key], entry["value"], entry.get("rel_tol", 1e-3)
        if abs(got - exp) > tol * max(abs(exp), 1e-12):
            print(f"ERROR   {key}: script gives {got:.6g}, reference is {exp:.6g} "
                  f"(update expected_results.json and the documents together)")
            errors += 1
        for doc, pattern in entry.get("documents", {}).items():
            path = a.root / doc
            if not path.is_file():
                print(f"ERROR   {key}: document {doc} not found")
                errors += 1
                continue
            text = path.read_text(encoding="utf-8").replace(" ", " ")
            needle = pattern.format(v=got)
            variants = {needle, needle.replace(",", " "), needle.replace(",", "")}
            if not any(v in text for v in variants):
                print(f"ERROR   {key}: '{needle}' not found in {doc} (document out of date?)")
                errors += 1
    mod = load_module(script)
    # Per-variant evaluation (external audit 2026-10-16, finding 4): run the shared engine with each
    # checked-out variant's own sizing/inputs.json. Variant results are compared with the variant's
    # own sizing/expected_results.json when it exists (same format as the reference file); otherwise
    # they are only computed (proves the inputs are usable) and reported. Skipped if not checked out.
    for var in ("s", "m", "l"):
        vdir = a.root / "mechanical" / f"actuator-{var}" / "sizing"
        vin = vdir / "inputs.json"
        if not vin.is_file():
            continue
        try:
            vp = dict(mod.INPUTS)
            vp.update(json.loads(vin.read_text(encoding="utf-8")))
            vres = compute(mod, vp)
        except Exception as exc:  # noqa: BLE001 - any failure means unusable inputs
            print(f"ERROR   actuator-{var} sizing/inputs.json cannot be evaluated by the engine: {exc!r}")
            errors += 1
            continue
        diff = [k for k, v in json.loads(vin.read_text(encoding="utf-8")).items()
                if k in mod.INPUTS and mod.INPUTS[k] != v]
        vref = vdir / "expected_results.json"
        if vref.is_file():
            for key, entry in json.loads(vref.read_text(encoding="utf-8")).get("results", {}).items():
                got, exp, tol = vres.get(key), entry["value"], entry.get("rel_tol", 1e-3)
                if got is None or abs(got - exp) > tol * max(abs(exp), 1e-12):
                    print(f"ERROR   actuator-{var} {key}: engine gives {got}, variant reference is {exp}")
                    errors += 1
            print(f"check_calcs: actuator-{var} evaluated and compared with its own reference.")
        else:
            print(f"WARNING actuator-{var}: inputs evaluate ({len(diff)} field(s) differ from the A0 baseline) "
                  f"but no sizing/expected_results.json exists - variant is NOT regression-protected; "
                  f"keep the variant at Concept until inputs are reviewed and a reference is committed.")
    print(f"check_calcs: {len(ref['results'])} key result(s) checked; {errors} error(s).")
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main())
