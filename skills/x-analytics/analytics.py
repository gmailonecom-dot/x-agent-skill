#!/usr/bin/env python3
"""analytics.py - read an X analytics export: rate, outliers, the fold.

No dependencies.

    python3 analytics.py posts.csv
    python3 analytics.py posts.csv --sort rate
"""
import argparse
import csv
import re
import sys
from statistics import median

ALIASES = {
    "impressions": ["impressions", "impression", "views", "view_count"],
    "engagements": ["engagements", "engagement", "engagements_total", "total_engagements"],
    "likes": ["likes", "like_count", "favorites"],
    "reposts": ["reposts", "retweets", "repost_count", "retweet_count"],
    "replies": ["replies", "reply_count"],
    "link_clicks": ["link_clicks", "url_clicks", "clicks", "link_click"],
    "follows": ["follows", "new_follows", "followers_gained"],
    "text": ["text", "post", "tweet", "content", "body"],
    "date": ["date", "time", "created_at", "posted_at", "day"],
}


def pick(fieldnames, key):
    lower = {f.lower().strip(): f for f in fieldnames}
    for a in ALIASES[key]:
        if a in lower:
            return lower[a]
    return None


def to_int(v):
    if v is None:
        return None
    s = re.sub(r"[^0-9.]", "", str(v))
    if s == "":
        return None
    try:
        return float(s)
    except ValueError:
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("csv")
    ap.add_argument("--sort", choices=["rate", "mult", "date"], default="mult")
    args = ap.parse_args()

    with open(args.csv, newline="") as f:
        rows = list(csv.DictReader(f))
    if not rows:
        print("empty file")
        sys.exit(1)

    fn = rows[0].keys()
    cols = {k: pick(fn, k) for k in ALIASES}
    if not cols["impressions"]:
        print("no impressions column found. Expected one of: " + ", ".join(ALIASES["impressions"]))
        sys.exit(1)

    posts = []
    for r in rows:
        imp = to_int(r.get(cols["impressions"]))
        if not imp:
            continue
        eng = to_int(r.get(cols["engagements"])) if cols["engagements"] else None
        if eng is None:
            parts = [to_int(r.get(cols[k])) or 0 for k in ("likes", "reposts", "replies") if cols[k]]
            eng = sum(parts) if parts else None
        clicks = to_int(r.get(cols["link_clicks"])) if cols["link_clicks"] else None
        follows = to_int(r.get(cols["follows"])) if cols["follows"] else None
        text = (r.get(cols["text"]) or "").strip().replace("\n", " ")
        date = (r.get(cols["date"]) or "").strip()
        posts.append({"imp": imp, "eng": eng, "clicks": clicks, "follows": follows,
                      "text": text, "date": date})

    if not posts:
        print("no rows with a usable impression count")
        sys.exit(1)

    med = median([p["imp"] for p in posts])
    print(f"{len(posts)} posts. median impressions {med:g}.\n")

    for p in posts:
        p["rate"] = (p["eng"] / p["imp"] * 100) if p["eng"] is not None else None
        p["mult"] = p["imp"] / med if med else 0

    key = {"rate": lambda p: (p["rate"] or 0), "mult": lambda p: p["mult"],
           "date": lambda p: p["date"]}.get(args.sort)
    for p in sorted(posts, key=key, reverse=(args.sort != "date")):
        rate = f"{p['rate']:.1f}%" if p["rate"] is not None else "  -  "
        extra = []
        if p["clicks"] is not None:
            extra.append(f"{p['clicks']:g} clicks")
        if p["follows"] is not None:
            extra.append(f"{p['follows']:g} follows")
        tail = ("  " + ", ".join(extra)) if extra else ""
        line = (p["text"][:70] + "...") if len(p["text"]) > 70 else p["text"]
        print(f"{p['mult']:>4.1f}x  {rate:>6}  {p['imp']:>8g} imp  {line}{tail}")

    print("\nThe outliers are the lesson, not the average. Read the top three's first lines "
          "and the bottom three's first lines with ../x-hook/lint.py.")


if __name__ == "__main__":
    main()
