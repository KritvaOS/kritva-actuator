#!/usr/bin/env python3
"""
Kritva Actuator - mechanical sizing calculations (canonical script).

Proprietary and confidential. Copyright (c) 2026 Kritvaos. All rights reserved.

Produces the numbers used in:
    mechanical/calculations/LOAD_CASES.md
    mechanical/calculations/TORQUE_AND_SPEED.md
    mechanical/calculations/SHAFT_STRENGTH.md
    mechanical/calculations/BEARING_SELECTION.md
    mechanical/calculations/GEARBOX_SELECTION.md

Usage:
    python3 mechanical/calculations/actuator_sizing.py            # all sections
    python3 mechanical/calculations/actuator_sizing.py --section shaft
    python3 mechanical/calculations/actuator_sizing.py --json

All inputs are in INPUTS. Every value is a PROPOSED baseline (ACT-DEC-008/009)
or an explicit ASSUMPTION; replace with CAD / datasheet values as they become
available and re-run. Geometry values marked ASSUMED are placeholders until the
CAD exists (ACT-02-004). Catalogue bearing ratings are typical published values
for the generic size and MUST be checked against the chosen manufacturer.

Standard library only (Python 3.8+).
"""
import argparse
import json
import math

G = 9.81

INPUTS = {
    # --- Load model (SYS-REQ-010/011) ---
    "m_arm_kg": 1.5,            # forearm + hand
    "r_arm_m": 0.180,           # CoM from elbow - PROVISIONAL assumption
    "m_pay_kg": 1.0,            # payload
    "r_pay_m": 0.350,           # payload centre from elbow
    # --- Targets (ACT-DEC-008, proposed) ---
    "T_cont_Nm": 10.0,
    "T_peak_min_Nm": 20.0,
    "T_peak_stretch_Nm": 25.0,
    "n_out_rpm": 45.0,
    "eta_gb": 0.85,             # preliminary gearbox efficiency
    "ratios": [15, 20, 25],
    "v_bus": 24.0,
    "v_usable_frac": 0.90,      # SVPWM usable fraction (approx.)
    "speed_margin": 0.70,       # loaded / no-load speed at the operating point
    # --- Illustrative angular accelerations (NOT approved; SYS-REQ-013 open) ---
    "alpha_examples": [5.0, 10.0, 20.0],   # rad/s^2
    # --- Shaft (ACT-DEC-009) ---
    "d_shaft_mm": 12.0,
    "shaft_free_len_mm": 30.0,  # ASSUMED torsional length gearbox coupling -> flange
    "Kt_keyway": 2.0,           # ASSUMED stress concentration (keyway / flat); refine per detail
    "Kt_shoulder": 1.7,         # ASSUMED shoulder fillet r/d ~ 0.05
    "G_steel_GPa": 80.0,
    "E_steel_GPa": 205.0,
    # --- Bearing geometry (ASSUMED until CAD) ---
    "overhang_a_mm": 20.0,      # load line (flange) to near bearing centre
    "span_L_mm": 25.0,          # bearing centre distance
    "stop_radius_mm": 25.0,     # hard-stop contact radius
    "bumper_stroke_mm": 2.0,    # example compliant stroke
    "s0_required": 2.0,         # static safety factor on C0 (robotics practice, TBC)
    "life_hours_target": 2000.0,  # bearing L10h design target (TBC)
    "mean_speed_rpm": 10.0,     # equivalent mean output speed for life (TBC: duty)
}

# Material data: indicative minimum values for the stated condition; VERIFY against
# the governing standard (e.g. IS 1570 / EN 10083) and the mill certificate.
MATERIALS = {
    "EN8 / C45 normalised":            {"Sy": 280.0, "Su": 550.0},
    "EN8 / C45 hardened & tempered":   {"Sy": 430.0, "Su": 700.0},
    "EN19 / 42CrMo4 Q&T (T condition)": {"Sy": 650.0, "Su": 850.0},
    "SS304 annealed":                  {"Sy": 205.0, "Su": 515.0},
    "Al 6061-T6 (not for shaft)":      {"Sy": 275.0, "Su": 310.0},
}

# Typical published deep-groove bearing ratings (generic size). VERIFY with vendor.
BEARINGS = {
    "6001 (12x28x8)":  {"d": 12, "D": 28, "B": 8,  "C_kN": 5.4,  "C0_kN": 2.36},
    "6201 (12x32x10)": {"d": 12, "D": 32, "B": 10, "C_kN": 7.28, "C0_kN": 3.10},
    "6002 (15x32x9)":  {"d": 15, "D": 32, "B": 9,  "C_kN": 5.85, "C0_kN": 2.85},
    "6202 (15x35x11)": {"d": 15, "D": 35, "B": 11, "C_kN": 8.06, "C0_kN": 3.75},
}

# Illustrative motor classes for the motor/ratio trade study (RISK-001). Values are
# TYPICAL ORDERS OF MAGNITUDE for the class, not data for any specific product.
MOTOR_CLASSES = {
    "A: 57 mm inrunner BLDC, 24 V, ~100 W, 3000 RPM rated": {"T_cont": 0.32, "T_peak": 0.95, "n_rated": 3000},
    "B: 60-70 mm low-Kv outrunner/pancake, 24 V":           {"T_cont": 0.45, "T_peak": 1.30, "n_rated": 1500},
    "C: 80-90 mm low-Kv pancake (8108-class), 24 V":        {"T_cont": 0.80, "T_peak": 2.20, "n_rated": 900},
}


def rpm_to_rad(n):
    return n * 2.0 * math.pi / 60.0


# ---------------------------------------------------------------- effective inertia
def effective_inertia(p=INPUTS):
    """Rod-plus-point arm inertia plus reflected rotor inertia J_rotor*N^2 (EXT-AUD-003/019).

    Rotor values are illustrative; the selected motor's datasheet value replaces them.
    Returns {(J_rotor, N): {"J": kg*m^2, "E": J, "rotor_share": fraction}}.
    """
    lc = load_cases(p)
    w = lc["omega"]
    out = {}
    for jr in (2e-5, 5e-5, 1e-4):
        for n in (15, 20, 25):
            j = lc["J_rod"] + jr * n ** 2
            out[(jr, n)] = {"J": j, "E": 0.5 * j * w ** 2, "rotor_share": jr * n ** 2 / j}
    return out


# ---------------------------------------------------------------- load cases
def load_cases(p=INPUTS):
    Tg_arm = p["m_arm_kg"] * G * p["r_arm_m"]
    Tg_pay = p["m_pay_kg"] * G * p["r_pay_m"]
    Tg = Tg_arm + Tg_pay
    J = p["m_arm_kg"] * p["r_arm_m"] ** 2 + p["m_pay_kg"] * p["r_pay_m"] ** 2
    # uniform-rod alternative for the forearm: rod length 2*r_arm, mass m_arm
    L_rod = 2 * p["r_arm_m"]
    J_rod = p["m_arm_kg"] * L_rod ** 2 / 3.0 + p["m_pay_kg"] * p["r_pay_m"] ** 2
    w = rpm_to_rad(p["n_out_rpm"])
    E = 0.5 * J * w ** 2
    W = (p["m_arm_kg"] + p["m_pay_kg"]) * G
    # centripetal force at 45 RPM on the combined CoM
    r_cm = (p["m_arm_kg"] * p["r_arm_m"] + p["m_pay_kg"] * p["r_pay_m"]) / (p["m_arm_kg"] + p["m_pay_kg"])
    F_cent = (p["m_arm_kg"] + p["m_pay_kg"]) * r_cm * w ** 2
    sens = []
    for r in (0.150, 0.180, 0.210):
        row = []
        for m in (0.5, 1.0, 2.0):
            row.append(p["m_arm_kg"] * G * r + m * G * p["r_pay_m"])
        sens.append((r, row))
    dyn = [(a, Tg + J * a, Tg + J_rod * a) for a in p["alpha_examples"]]
    return {
        "Tg_arm": Tg_arm, "Tg_pay": Tg_pay, "Tg": Tg, "J_point": J, "J_rod": J_rod,
        "omega": w, "E_stop": E, "E_stop_rod": 0.5 * J_rod * w ** 2,
        "W_link_N": W, "r_cm_m": r_cm, "F_cent_N": F_cent,
        "margin_cont": p["T_cont_Nm"] / Tg, "sensitivity": sens, "dynamic": dyn,
    }


# ---------------------------------------------------------- torque and speed
def torque_speed(p=INPUTS):
    w_out = rpm_to_rad(p["n_out_rpm"])
    P_out = p["T_cont_Nm"] * w_out
    rows = []
    for N in p["ratios"]:
        n_m = p["n_out_rpm"] * N
        Tm_c = p["T_cont_Nm"] / (N * p["eta_gb"])
        Tm_p20 = p["T_peak_min_Nm"] / (N * p["eta_gb"])
        Tm_p25 = p["T_peak_stretch_Nm"] / (N * p["eta_gb"])
        Tm_g = load_cases(p)["Tg"] / (N * p["eta_gb"])
        P_m = Tm_c * rpm_to_rad(n_m)
        kv_min = n_m / (p["v_bus"] * p["v_usable_frac"] * p["speed_margin"])
        rows.append({"N": N, "n_motor": n_m, "Tm_cont": Tm_c, "Tm_peak20": Tm_p20,
                     "Tm_peak25": Tm_p25, "Tm_hold": Tm_g, "P_motor": P_m,
                     "Kv_min": kv_min, "Kt_at_Kvmin": 8.27 / kv_min, "N2": N * N})
    return {"w_out": w_out, "P_out": P_out, "rows": rows}


def motor_class_trade(p=INPUTS):
    out = []
    for name, m in MOTOR_CLASSES.items():
        N_cont = p["T_cont_Nm"] / (p["eta_gb"] * m["T_cont"])
        N_peak = p["T_peak_stretch_Nm"] / (p["eta_gb"] * m["T_peak"])
        N_req = max(N_cont, N_peak)
        N_speed_max = m["n_rated"] / p["n_out_rpm"]
        out.append({"class": name, "N_req_cont": N_cont, "N_req_peak25": N_peak,
                    "N_required": N_req, "N_max_for_45rpm": N_speed_max,
                    "feasible": N_req <= N_speed_max})
    return out


# -------------------------------------------------------------------- shaft
def shaft(p=INPUTS):
    d = p["d_shaft_mm"]
    Jp = math.pi * d ** 4 / 32.0
    Zb = math.pi * d ** 3 / 32.0
    Zt = math.pi * d ** 3 / 16.0
    lc = load_cases(p)
    cases = []
    stop_F = p["T_peak_stretch_Nm"] * 1000 / p["stop_radius_mm"]
    defs = [
        ("LC-01 hold", lc["Tg"], lc["W_link_N"]),
        ("LC-02 continuous", p["T_cont_Nm"], lc["W_link_N"] + lc["F_cent_N"]),
        ("LC-03 peak 20", p["T_peak_min_Nm"], 2 * lc["W_link_N"]),
        ("LC-03 peak 25", p["T_peak_stretch_Nm"], 2 * lc["W_link_N"]),
        ("LC-05 stall into single stop 25", p["T_peak_stretch_Nm"], stop_F),
    ]
    for name, T, F in defs:
        tau = T * 1000 / Zt
        M = F * p["overhang_a_mm"]
        sig = M / Zb
        vm = math.sqrt(sig ** 2 + 3 * tau ** 2)
        vm_kt = math.sqrt((p["Kt_shoulder"] * sig) ** 2 + 3 * (p["Kt_keyway"] * tau) ** 2)
        twist = math.degrees(T * 1000 * p["shaft_free_len_mm"] / (p["G_steel_GPa"] * 1e3 * Jp))
        cases.append({"case": name, "T": T, "F": F, "M_Nmm": M, "tau": tau, "sigma_b": sig,
                      "vm": vm, "vm_kt": vm_kt, "twist_deg": twist})
    sf = []
    gov = max(cases, key=lambda c: c["vm_kt"])
    for mat, v in MATERIALS.items():
        sf.append({"material": mat, "Sy": v["Sy"], "SF_yield_gov": v["Sy"] / gov["vm_kt"]})
    # minimum diameter for SF 2.0 on yield, EN19, governing case (solve numerically)
    def vm_at(dd, c):
        zb = math.pi * dd ** 3 / 32.0
        zt = math.pi * dd ** 3 / 16.0
        return math.sqrt((p["Kt_shoulder"] * c["M_Nmm"] / zb) ** 2 + 3 * (p["Kt_keyway"] * c["T"] * 1000 / zt) ** 2)
    dmin = {}
    for mat in ("EN8 / C45 normalised", "EN19 / 42CrMo4 Q&T (T condition)"):
        dd = 6.0
        while vm_at(dd, gov) * 2.0 > MATERIALS[mat]["Sy"] and dd < 40:
            dd += 0.1
        dmin[mat] = dd
    # fatigue (Modified Goodman, fully reversed bending + steady torsion) at LC-02
    c2 = cases[1]
    Se_prime = {}
    for mat in ("EN8 / C45 normalised", "EN19 / 42CrMo4 Q&T (T condition)"):
        Su = MATERIALS[mat]["Su"]
        Se = 0.5 * Su * 0.8 * 0.9 * 0.9  # surface (machined), size, reliability ~ indicative
        sa = p["Kt_shoulder"] * c2["sigma_b"]
        tm = p["Kt_keyway"] * c2["tau"]
        sm_eq = math.sqrt(3) * tm
        n_f = 1.0 / (sa / Se + sm_eq / Su)
        Se_prime[mat] = {"Se": Se, "sigma_a": sa, "sigma_m_eq": sm_eq, "n_goodman": n_f}
    return {"d": d, "Jp": Jp, "Zb": Zb, "Zt": Zt, "cases": cases, "governing": gov["case"],
            "sf": sf, "dmin_sf2": dmin, "fatigue_LC02": Se_prime}


# ----------------------------------------------------------------- bearings
def bearings(p=INPUTS):
    lc = load_cases(p)
    a, L = p["overhang_a_mm"], p["span_L_mm"]
    stop_F = p["T_peak_stretch_Nm"] * 1000 / p["stop_radius_mm"]
    loads = [
        ("LC-01 link weight", lc["W_link_N"]),
        ("LC-02 weight + centripetal", lc["W_link_N"] + lc["F_cent_N"]),
        ("LC-03 2x weight (dynamic allowance)", 2 * lc["W_link_N"]),
        ("LC-05 single stop @25 N*m", stop_F),
    ]
    reac = []
    for name, F in loads:
        reac.append({"case": name, "F": F, "R_near": F * (1 + a / L), "R_far": F * a / L})
    gov = max(reac, key=lambda r: r["R_near"])
    # dynamic equivalent for life: LC-02 radial at mean speed
    P_life = reac[1]["R_near"]
    checks = []
    for name, b in BEARINGS.items():
        s0 = b["C0_kN"] * 1000 / gov["R_near"]
        L10 = (b["C_kN"] * 1000 / P_life) ** 3  # million revs
        L10h = L10 * 1e6 / (60 * p["mean_speed_rpm"])
        checks.append({"bearing": name, "s0_gov": s0, "s0_ok": s0 >= p["s0_required"],
                       "L10h_LC02": L10h})
    # span sensitivity for governing load
    span = []
    for LL in (15, 20, 25, 30, 40):
        span.append((LL, gov["F"] * (1 + a / LL), gov["F"] * a / LL))
    return {"a": a, "L": L, "reactions": reac, "governing": gov, "checks": checks, "span": span,
            "balanced_stop_note": "A two-sided (balanced) stop reacts the stop torque as a couple and removes the radial stop force from the bearings."}


# ----------------------------------------------------------------- gearbox / stops
def stops(p=INPUTS):
    lc = load_cases(p)
    out = []
    for n in (45, 30, 20, 15, 10):
        E = 0.5 * lc["J_point"] * rpm_to_rad(n) ** 2
        th = p["bumper_stroke_mm"] / p["stop_radius_mm"]
        Tpk = 2 * E / th
        out.append({"rpm": n, "E": E, "T_stop_2mm_25mm": Tpk,
                    "theta_for_20": math.degrees(2 * E / 20.0),
                    "theta_for_25": math.degrees(2 * E / 25.0)})
    # max approach speed so that T_stop <= 20 N*m with the example bumper
    th = p["bumper_stroke_mm"] / p["stop_radius_mm"]
    E_allow = 20.0 * th / 2
    n_allow = math.sqrt(2 * E_allow / lc["J_point"]) * 60 / (2 * math.pi)
    return {"rows": out, "n_allow_20Nm_rpm": n_allow}


def gearbox_requirements(p=INPUTS):
    ts = torque_speed(p)
    rows = []
    for r in ts["rows"]:
        rows.append({"N": r["N"], "out_cont_req": p["T_cont_Nm"], "out_peak_req": p["T_peak_stretch_Nm"],
                     "input_speed_rpm": r["n_motor"], "input_torque_cont": r["Tm_cont"]})
    return rows


# ------------------------------------------------------------------ printing
def pr_load(r):
    print("## LOAD CASES")
    print(f"T_g arm = {r['Tg_arm']:.3f} N*m, payload = {r['Tg_pay']:.3f} N*m, total T_g = {r['Tg']:.3f} N*m")
    print(f"Continuous target / T_g = {r['margin_cont']:.2f}")
    print(f"J point-mass = {r['J_point']:.4f} kg*m^2 ; J rod+point = {r['J_rod']:.4f} kg*m^2")
    print(f"omega(45 RPM) = {r['omega']:.3f} rad/s ; E_stop = {r['E_stop']:.3f} J (rod model {r['E_stop_rod']:.3f} J)")
    print(f"Link weight = {r['W_link_N']:.2f} N ; combined CoM = {r['r_cm_m']*1000:.1f} mm ; centripetal @45 RPM = {r['F_cent_N']:.2f} N")
    print("Sensitivity T_g [N*m]: rows CoM 150/180/210 mm, cols payload 0.5/1.0/2.0 kg")
    for rr, row in r["sensitivity"]:
        print(f"  {rr*1000:.0f} mm: " + "  ".join(f"{v:.2f}" for v in row))
    print("Dynamic (T_g + J*alpha), illustrative alphas:")
    for a, t1, t2 in r["dynamic"]:
        print(f"  alpha={a:.0f} rad/s^2 : point {t1:.2f} N*m ; rod {t2:.2f} N*m")


def pr_ts(r, mc):
    print("## TORQUE AND SPEED")
    print(f"omega_out = {r['w_out']:.3f} rad/s ; P_out(10 N*m) = {r['P_out']:.1f} W")
    print("N  n_motor  Tm_hold Tm_cont Tm_pk20 Tm_pk25  P_motor  Kv_min  Kt@Kvmin  N^2")
    for x in r["rows"]:
        print(f"{x['N']:<3}{x['n_motor']:>7.0f}{x['Tm_hold']:>8.3f}{x['Tm_cont']:>8.3f}{x['Tm_peak20']:>8.3f}"
              f"{x['Tm_peak25']:>8.3f}{x['P_motor']:>8.1f}{x['Kv_min']:>8.1f}{x['Kt_at_Kvmin']:>9.3f}{x['N2']:>6}")
    print("Motor class trade (illustrative class values):")
    for m in mc:
        print(f"  {m['class']}: N_req cont {m['N_req_cont']:.1f}, peak25 {m['N_req_peak25']:.1f} -> N_req {m['N_required']:.1f};"
              f" N_max for 45 RPM {m['N_max_for_45rpm']:.1f}; feasible={m['feasible']}")


def pr_shaft(r):
    print("## SHAFT")
    print(f"d = {r['d']} mm ; Jp = {r['Jp']:.0f} mm^4 ; Zb = {r['Zb']:.1f} mm^3 ; Zt = {r['Zt']:.1f} mm^3")
    print("case  T  F  M  tau  sigma_b  vm  vm_Kt  twist")
    for c in r["cases"]:
        print(f"  {c['case']}: T={c['T']:.2f} F={c['F']:.1f}N M={c['M_Nmm']:.0f}Nmm tau={c['tau']:.1f} sb={c['sigma_b']:.1f} "
              f"vm={c['vm']:.1f} vmKt={c['vm_kt']:.1f} MPa twist={c['twist_deg']:.3f} deg")
    print(f"Governing: {r['governing']}")
    for s in r["sf"]:
        print(f"  {s['material']}: Sy={s['Sy']:.0f} SF={s['SF_yield_gov']:.2f}")
    for m, d in r["dmin_sf2"].items():
        print(f"  d_min for SF 2.0 (governing, with Kt) {m}: {d:.1f} mm")
    for m, f in r["fatigue_LC02"].items():
        print(f"  Fatigue LC-02 {m}: Se={f['Se']:.0f} sa={f['sigma_a']:.1f} sm_eq={f['sigma_m_eq']:.1f} n_Goodman={f['n_goodman']:.1f}")


def pr_bear(r):
    print("## BEARINGS")
    print(f"a = {r['a']} mm, L = {r['L']} mm")
    for x in r["reactions"]:
        print(f"  {x['case']}: F={x['F']:.1f} N R_near={x['R_near']:.1f} R_far={x['R_far']:.1f}")
    print(f"Governing: {r['governing']['case']}")
    for c in r["checks"]:
        print(f"  {c['bearing']}: s0={c['s0_gov']:.2f} ok={c['s0_ok']} L10h(LC-02 @mean speed)={c['L10h_LC02']:.3g} h")
    print("Span sensitivity (governing F):")
    for LL, rn, rf in r["span"]:
        print(f"  L={LL} mm: R_near={rn:.0f} N, R_far={rf:.0f} N")


def pr_stops(r):
    print("## HARD STOPS")
    for x in r["rows"]:
        print(f"  {x['rpm']} RPM: E={x['E']:.3f} J ; T_stop(2 mm @25 mm)={x['T_stop_2mm_25mm']:.1f} N*m ;"
              f" theta for 20 N*m={x['theta_for_20']:.1f} deg ; for 25 N*m={x['theta_for_25']:.1f} deg")
    print(f"  Max approach speed for T_stop <= 20 N*m with 2 mm @ 25 mm bumper: {r['n_allow_20Nm_rpm']:.1f} RPM")


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--section", choices=["load", "torque", "shaft", "bearing", "stops", "all"], default="all")
    ap.add_argument("--json", action="store_true")
    ap.add_argument("--inputs", metavar="FILE.json",
                    help="variant inputs (e.g. mechanical/actuator-m/sizing/inputs.json); values override INPUTS")
    a = ap.parse_args()
    p = dict(INPUTS)
    if a.inputs:
        with open(a.inputs, encoding="utf-8") as fh:
            p.update(json.load(fh))
    res = {"inputs": p, "load": load_cases(p), "torque": torque_speed(p), "motor_classes": motor_class_trade(p),
           "shaft": shaft(p), "bearing": bearings(p), "stops": stops(p), "gearbox": gearbox_requirements(p)}
    if a.json:
        print(json.dumps(res, indent=2, default=str))
        return
    if a.section in ("load", "all"):
        pr_load(res["load"])
    if a.section in ("torque", "all"):
        pr_ts(res["torque"], res["motor_classes"])
    if a.section in ("shaft", "all"):
        pr_shaft(res["shaft"])
    if a.section in ("bearing", "all"):
        pr_bear(res["bearing"])
    if a.section in ("stops", "all"):
        pr_stops(res["stops"])


if __name__ == "__main__":
    main()
