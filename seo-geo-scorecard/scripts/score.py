#!/usr/bin/env python3
"""Score SEO/GEO Scorecard results.

Usage:
    python scripts/score.py results.json
    cat results.json | python scripts/score.py -

Input JSON maps each site name to its 12 check scores:
    {"client.com": {"title_tag": 2, "meta_description": 1, ..., "structured_data": null}}
Each score is 0, 1, 2, or null/"unassessed". Unassessed checks are excluded from both
the points and the maximum (never counted as failures).

Output: per site, points, max, percent of assessed maximum, band, and unassessed checks.
"""
import json
import sys

CHECKS = [
    "title_tag", "meta_description", "canonical_tag", "heading_structure",
    "ai_crawler_accessibility", "llms_txt", "ai_access_legal_posture",
    "image_alt_text", "url_structure", "structured_data",
    "content_extractability", "internal_linking",
]
# Bands are percentages of the assessed maximum: 19/24 = 79% and 12/24 = 50%,
# the original absolute cutoffs, so results are comparable when checks are unassessed.
STRONG_PCT = 79
ADEQUATE_PCT = 50


def band(pct):
    if pct >= STRONG_PCT:
        return "Strong"
    if pct >= ADEQUATE_PCT:
        return "Adequate, real gaps"
    return "At Risk"


def score_site(name, results):
    unknown = set(results) - set(CHECKS)
    if unknown:
        sys.exit(f"{name}: unknown check(s): {sorted(unknown)}")
    points = maximum = 0
    unassessed = []
    for check in CHECKS:
        value = results.get(check)
        if value is None or value == "unassessed":
            unassessed.append(check)
            continue
        if value not in (0, 1, 2):
            sys.exit(f"{name}: {check} must be 0, 1, 2, or null, got {value!r}")
        points += value
        maximum += 2
    if maximum == 0:
        sys.exit(f"{name}: no assessed checks")
    pct = round(100 * points / maximum, 1)
    return {"site": name, "points": points, "max": maximum, "percent": pct,
            "band": band(pct), "unassessed": unassessed}


def main():
    if len(sys.argv) != 2:
        sys.exit(__doc__)
    src = sys.stdin if sys.argv[1] == "-" else open(sys.argv[1])
    data = json.load(src)
    print(json.dumps([score_site(n, r) for n, r in data.items()], indent=2))


if __name__ == "__main__":
    main()
