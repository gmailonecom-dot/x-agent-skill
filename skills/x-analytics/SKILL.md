---
name: x-analytics
description: >-
  Read an X (Twitter) analytics export and find where posts actually won or
  lost - the fold, the drop, the outliers by own-account multiple - then say
  what to change. Use for "why do my posts flop", "read my analytics", a pasted
  export or CSV, or "fix my reach".
---

# x-analytics

The export has the answer and almost nobody reads it. This reads it properly: engagement rate per
post, the outliers against your own median, and the fold.

```bash
python3 analytics.py posts.csv
python3 analytics.py posts.csv --sort rate
```

## Before you write

1. Read `~/.claude/x/voice.md` if it exists. If it does not, ask for **five of their own posts that
   did well** and write it.
2. Never invent a number. Every figure in the output comes from the export or the user. If a number
   is missing, say it is missing rather than filling it in.

## What the tool wants

A CSV with one row per post. It looks for columns like `impressions`, `engagements` (or
`likes`+`reposts`+`replies`), `link_clicks`, `follows`, and the post `text` or `date`. Column names
are matched loosely; if it cannot find one it says so.

## What to look at, in this order

1. **Engagement rate** (engagements ÷ impressions), per post. This is the only number that compares
   across a big post and a small one.
2. **The outliers**, by multiple over your own median. Two things to learn: what the best three have
   in common, and what the worst three have in common. The worst are usually the same mistake.
3. **The fold.** For the low performers, look at the first line. `../x-hook/lint.py` will name the
   problem. Most flops are a first line that only made sense with the second.
4. **The link tax.** If link posts underperform, that is why the pack says put the link in a reply.

## What to hand back

- the single biggest fix, named, with what to do this week
- three things already working, so they are not broken. Be specific.
- what NOT to change yet, and why

Never open with praise you do not mean, and never end with a list of twenty things.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
