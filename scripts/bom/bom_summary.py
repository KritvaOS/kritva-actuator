#!/usr/bin/env python3
"""Summarise the Kritva Actuator BOM costs by milestone and category.

Copyright (c) 2026 Kritvaos. Licensed under the Apache License, Version 2.0 (see LICENSE).

Reads the same files as ``check_bom.py`` (``mechanical/bom/MECHANICAL_BOM.csv``
and ``hardware/bom/ELECTRICAL_BOM.csv`` by default), using its parser and
validation, and prints:

1. totals by milestone, split into *committed* items (status SELECTED,
   ORDERED or RECEIVED) and *candidate* items (status CANDIDATE);
2. totals by category, with the same split;
3. totals by cost_status (ESTIMATE / QUOTED / PURCHASED), plus the number of
   TBD items that carry no cost and are therefore NOT in any total;
4. cumulative committed cost against the provisional budget bands from the
   project baseline (A0 INR 10,000-15,000; A1 cumulative INR 20,000-30,000;
   provisional, not supplier-verified, laboratory equipment excluded).

REJECTED rows are excluded from all totals. Candidate totals can include
mutually exclusive alternatives (for example three gearbox ratios), so they
are an upper bound for comparison, not a forecast.

The summary is printed even when check_bom reports problems; rows that fail
numeric validation are left out of the totals and counted as "unpriced".
Exit status is 0 unless ``--fail-on-errors`` is given and the BOMs have
validation errors (exit 1).

Standard library only. Python 3.8+.
"""

from __future__ import annotations

import argparse
import sys
from collections import OrderedDict
from decimal import Decimal
from pathlib import Path
from typing import Dict, List, Optional, Tuple

sys.path.insert(0, str(Path(__file__).resolve().parent))
from check_bom import (  # noqa: E402  (local module next to this script)
    MILESTONES,
    BomRow,
    check_files,
    default_root,
    resolve_files,
)

COMMITTED = {"SELECTED", "ORDERED", "RECEIVED"}
CANDIDATE = {"CANDIDATE"}
# Provisional budget bands (baseline brief section 4 / SYS-REQ-100). Cumulative.
BUDGET_BANDS: Dict[str, Tuple[int, int]] = {
    "A0": (10000, 15000),
    "A1": (20000, 30000),
}


def row_cost(row: BomRow) -> Optional[Decimal]:
    if row.extended is not None:
        return row.extended
    if row.quantity is not None and row.unit_cost is not None:
        return row.quantity * row.unit_cost
    return None


def inr(value: Decimal) -> str:
    return f"{value:,.2f}"


class Bucket:
    __slots__ = ("committed", "candidate", "unpriced", "items")

    def __init__(self) -> None:
        self.committed = Decimal(0)
        self.candidate = Decimal(0)
        self.unpriced = 0
        self.items = 0


def summarise(rows: List[BomRow]):
    by_ms: "OrderedDict[str, Bucket]" = OrderedDict((m, Bucket()) for m in MILESTONES)
    by_cat: Dict[str, Bucket] = {}
    by_cost_status: Dict[str, Decimal] = {"ESTIMATE": Decimal(0), "QUOTED": Decimal(0),
                                          "PURCHASED": Decimal(0)}
    tbd_items = 0
    rejected = 0
    for row in rows:
        d = row.data
        if d["status"] == "REJECTED":
            rejected += 1
            continue
        cost = row_cost(row)
        ms = by_ms.setdefault(d["milestone"] or "(none)", Bucket())
        cat = by_cat.setdefault(d["category"] or "(none)", Bucket())
        for b in (ms, cat):
            b.items += 1
            if cost is None:
                b.unpriced += 1
            elif d["status"] in COMMITTED:
                b.committed += cost
            elif d["status"] in CANDIDATE:
                b.candidate += cost
        if d["cost_status"] == "TBD" or cost is None:
            tbd_items += 1
        elif d["cost_status"] in by_cost_status:
            by_cost_status[d["cost_status"]] += cost
    return by_ms, by_cat, by_cost_status, tbd_items, rejected


def table(title: str, headers: List[str], rows: List[List[str]], markdown: bool) -> str:
    out: List[str] = []
    if markdown:
        out.append(f"### {title}\n")
        out.append("| " + " | ".join(headers) + " |")
        out.append("|" + "|".join("---" for _ in headers) + "|")
        for r in rows:
            out.append("| " + " | ".join(r) + " |")
    else:
        widths = [max(len(h), *(len(r[i]) for r in rows)) if rows else len(h)
                  for i, h in enumerate(headers)]
        out.append(title)
        out.append("-" * len(title))
        out.append("  ".join(h.ljust(w) if i == 0 else h.rjust(w)
                             for i, (h, w) in enumerate(zip(headers, widths))))
        for r in rows:
            out.append("  ".join(c.ljust(w) if i == 0 else c.rjust(w)
                                 for i, (c, w) in enumerate(zip(r, widths))))
    out.append("")
    return "\n".join(out)


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Summarise BOM costs by milestone and category.")
    parser.add_argument("--root", type=Path, default=default_root(),
                        help="repository root (default: two levels above this script)")
    parser.add_argument("files", nargs="*",
                        help="BOM CSV paths relative to the root (default: both project BOMs)")
    parser.add_argument("--markdown", action="store_true", help="print Markdown tables")
    parser.add_argument("--fail-on-errors", action="store_true",
                        help="exit 1 if the BOMs have validation errors")
    args = parser.parse_args(argv)

    root = args.root.resolve()
    if not root.is_dir():
        print(f"ERROR   repository root '{root}' does not exist")
        return 2

    result = check_files(root, resolve_files(args.files))
    for line in result.warnings:
        if "not present yet" in line:
            print(line)
    if result.errors:
        print(f"NOTE    {len(result.errors)} BOM validation error(s); run 'make check-bom' for "
              "details. Invalid numeric rows are counted as unpriced.")
    if not result.rows:
        print("bom_summary: no BOM rows to summarise yet.")
        return 1 if (args.fail_on_errors and result.errors) else 0

    by_ms, by_cat, by_cs, tbd_items, rejected = summarise(result.rows)
    print(f"BOM summary (INR) from: {', '.join(result.files_read)}\n")

    ms_rows = [[m, str(b.items), inr(b.committed), inr(b.candidate), str(b.unpriced)]
               for m, b in by_ms.items()]
    print(table("Totals by milestone", ["Milestone", "Items", "Committed", "Candidates",
                                        "Unpriced"], ms_rows, args.markdown))

    cat_rows = [[c, str(b.items), inr(b.committed), inr(b.candidate), str(b.unpriced)]
                for c, b in sorted(by_cat.items())]
    print(table("Totals by category", ["Category", "Items", "Committed", "Candidates",
                                       "Unpriced"], cat_rows, args.markdown))

    cs_rows = [[k, inr(v)] for k, v in by_cs.items()]
    cs_rows.append(["TBD / unpriced items (not in totals)", str(tbd_items)])
    cs_rows.append(["REJECTED items (excluded)", str(rejected)])
    print(table("Totals by cost status (committed + candidates)", ["Cost status", "Value"],
                cs_rows, args.markdown))

    cumulative = Decimal(0)
    cum_rows = []
    for m, b in by_ms.items():
        cumulative += b.committed
        band = BUDGET_BANDS.get(m)
        if band:
            lo, hi = band
            if cumulative > hi:
                verdict = "ABOVE band"
            elif cumulative >= lo:
                verdict = "within band"
            else:
                verdict = "below band"
            band_text = f"{lo:,}-{hi:,}"
        else:
            band_text, verdict = "not defined", "-"
        cum_rows.append([m, inr(cumulative), band_text, verdict])
    print(table("Cumulative committed cost against provisional budget bands",
                ["Up to", "Cumulative", "Band (INR)", "Position"], cum_rows, args.markdown))
    print("Budget bands are provisional and not supplier-verified (SYS-REQ-100); laboratory "
          "equipment is excluded. Candidate totals may include mutually exclusive alternatives.")
    return 1 if (args.fail_on_errors and result.errors) else 0


if __name__ == "__main__":
    sys.exit(main())
