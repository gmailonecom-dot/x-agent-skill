#!/usr/bin/env python3
"""lint.py - lint the first line and the media of an X post as one pairing.

No dependencies.

    python3 lint.py --line "one line" --media "TEXT ON IMAGE"
    python3 lint.py posts.txt            # one post per line, ranked
"""
import argparse
import re
import sys

FOLD = 120  # roughly where a first line is truncated on a phone timeline
MAX = 280
VAGUE = re.compile(
    r"\b(game[- ]?changer|unlock|massive|insane|crazy|amazing|huge|secret|"
    r"dive in|leverage|synergy|revolutionary|10x|ninja|guru)\b",
    re.I,
)
THROAT = re.compile(
    r"^(let me|here'?s the thing|unpopular opinion|hot take|in this (post|thread)|"
    r"i want to|just a reminder|thread\s*[:\-])",
    re.I,
)
LINK = re.compile(r"https?://|www\.", re.I)


def words(s):
    return [w for w in re.split(r"[^A-Za-z0-9]+", s) if w]


def lint(line, media=""):
    issues = []
    score = 10
    n = len(line)
    if n > MAX:
        issues.append(f"first line is {n} chars; a single post caps at {MAX}.")
        score -= 3
    if n > FOLD:
        issues.append(f"first line is {n} chars; it will truncate near the fold ({FOLD}). Front-load the promise.")
        score -= 1
    if THROAT.search(line.strip()):
        issues.append("opens with throat-clearing. Cut it; the promise has to be in the first six words.")
        score -= 2
    v = VAGUE.findall(line)
    if v:
        issues.append(f"vague words: {', '.join(sorted(set(v)))}. Replace with a number, a name or a date.")
        score -= 1 * len(set(v))
    tags = re.findall(r"#\w+", line)
    if len(tags) > 2:
        issues.append(f"{len(tags)} hashtags. Two is the ceiling; zero is usually right.")
        score -= 1
    if LINK.search(line):
        issues.append("link in the body. Put it in the first reply so the post is not throttled.")
        score -= 1
    if media:
        mw = words(media)
        if len(mw) > 4:
            issues.append(f"image text is {len(mw)} words. Four is the maximum that survives timeline size.")
            score -= 1
        shared = {w.lower() for w in words(line)} & {w.lower() for w in mw}
        if shared:
            issues.append(f"image repeats the line: {', '.join(sorted(shared))}. Different words, same promise.")
            score -= 1
    return max(0, min(10, score)), issues


def report(line, media=""):
    sc, issues = lint(line, media)
    print(f'line: "{line}"  ({len(line)} chars)')
    if media:
        print(f'media: "{media}"')
    print(f"score {sc}/10")
    for i in issues:
        print(f"  - {i}")
    if not issues:
        print("  - clean. The line works alone and the image adds, rather than repeats.")
    return sc


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?")
    ap.add_argument("--line")
    ap.add_argument("--media", default="")
    args = ap.parse_args()
    if args.line:
        report(args.line, args.media)
        return
    if args.file:
        with open(args.file) as f:
            lines = [ln.strip() for ln in f if ln.strip()]
        for ln in lines:
            report(ln)
            print()
        return
    ap.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
