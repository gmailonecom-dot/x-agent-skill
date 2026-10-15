#!/usr/bin/env python3
"""hookscore.py - a 5-property panel for an X (Twitter) first line.

No dependencies. Heuristic, not a predictor.

    python3 hookscore.py --hook "one line"
    python3 hookscore.py hooks.txt            # one per line, ranked
"""
import argparse
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
HOOKS = os.path.join(HERE, "hooks.json")

THROAT = re.compile(
    r"^(let me|here'?s the thing|unpopular opinion|hot take|in this (post|thread)|"
    r"i want to|i'?m going to talk|thread\s*[:\-]|a thread\s*[:\-]|just a reminder)",
    re.I,
)
VAGUE = re.compile(
    r"\b(game[- ]?changer|unlock|massive|insane|crazy|amazing|huge|secret|"
    r"dive in|leverage|synergy|revolutionary|10x|ninja|guru)\b",
    re.I,
)
NUMBER = re.compile(r"\b\d+([.,]\d+)?\s?(%|k|m|x|followers|posts|days|weeks|months|years|₹|\$)?\b", re.I)
STAKE = re.compile(
    r"\b(don'?t|do not|before you|stop|cost|spent|wasted|lost|risk|mistake|"
    r"for \d+ (days|weeks|months)|quit|failed|paid)\b",
    re.I,
)
CURIOSITY = re.compile(
    r"\b(why|how|what|nobody|everyone|almost nobody|hidden|buried|secret|"
    r"wrong|never|nobody tells|real reason)\b|\?",
    re.I,
)
PROOF = re.compile(
    r"\b(here (is|are)|on screen|screenshot|receipts?|proof|exact|"
    r"the prompt|i (mapped|pulled|broke)|breakdown|template|list)\b",
    re.I,
)
SECOND_PERSON = re.compile(r"\byou(r)?\b", re.I)


def clamp(n, lo=0, hi=5):
    return max(lo, min(hi, n))


def classify(text, hooks):
    hits = []
    for h in hooks:
        for pat in h.get("match", []):
            try:
                if re.search(pat, text, re.I):
                    hits.append(h["name"])
                    break
            except re.error:
                continue
    return hits


def score(text, hooks):
    words = text.split()
    n = len(words)
    s = {}

    # specificity: numbers, named things, concrete nouns; penalise vague buzzwords
    spec = 0
    if NUMBER.search(text):
        spec += 3
    if any(w[0].isupper() for w in words[1:]):
        spec += 1
    if 8 <= n <= 30:
        spec += 1
    spec -= 2 * len(VAGUE.findall(text))
    s["specificity"] = clamp(spec)

    # curiosity: opens a question the reader cannot close
    cur = 1 + len(CURIOSITY.findall(text))
    if text.strip().endswith("?"):
        cur += 1
    s["curiosity"] = clamp(cur)

    # stakes: something to lose or gain
    st = len(STAKE.findall(text))
    s["stakes"] = clamp(st)

    # directness: no throat-clearing, speaks to "you", not too long
    d = 4
    if THROAT.search(text):
        d -= 3
    if SECOND_PERSON.search(text):
        d += 1
    if n > 40:
        d -= 1
    if n > 60:
        d -= 1
    s["directness"] = clamp(d)

    # proof: promises an artifact you can actually deliver
    pr = len(PROOF.findall(text))
    s["proof"] = clamp(pr)

    overall = round(sum(s.values()) / (5 * 5) * 10, 1)
    return s, overall


def panel(text, hooks):
    s, overall = score(text, hooks)
    forms = classify(text, hooks)
    print(f'hook: "{text}"')
    print(f"formula: {', '.join(forms) if forms else 'none recognised'}")
    for k in ("specificity", "curiosity", "stakes", "directness", "proof"):
        bar = "#" * s[k] + "." * (5 - s[k])
        print(f"  {k:<12} {bar} {s[k]}/5")
    print(f"overall {overall}/10  - a low score is a reason to look again, not a verdict.")
    return overall


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("file", nargs="?", help="file with one hook per line")
    ap.add_argument("--hook", help="score a single hook")
    args = ap.parse_args()

    with open(HOOKS) as f:
        hooks = json.load(f)["hooks"]

    if args.hook:
        panel(args.hook, hooks)
        return

    if args.file:
        with open(args.file) as f:
            lines = [ln.strip() for ln in f if ln.strip()]
        ranked = sorted(((panel(ln, hooks), ln) for ln in lines), reverse=True)
        print("\n--- ranked ---")
        for sc, ln in ranked:
            print(f"{sc:>4}  {ln}")
        return

    ap.print_help()
    sys.exit(1)


if __name__ == "__main__":
    main()
