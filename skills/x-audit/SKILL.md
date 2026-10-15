---
name: x-audit
description: >-
  Audit an X (Twitter) account end to end - the profile, the last posts as a
  set, the first lines, the rhythm, the replies - and end in ONE fix. Use for
  "audit my account", "why isn't my account growing", "review my posts", or a
  pasted profile or handle.
---

# x-audit

An audit that lists twenty problems is a way of avoiding the one that matters. This ends in ONE fix.

## Before you write

1. Read `~/.claude/x/voice.md` if it exists. If it does not, ask for **five of their own posts that
   did well** and write it.
2. Never invent a number, a result or a source. Ask for it or write the line without it.

## What to look at, in this order

1. **The profile, as a stranger sees it.** Run `/x-profile`. If a visitor cannot tell what the
   account is for in five seconds, that is the fix and nothing else matters yet.
2. **The last ten first lines, as a set.** Read them as a column, the way the timeline shows them.
   Do they promise different things? Run them through [`../x-hook/lint.py`](../x-hook/lint.py). An
   account where every first line is the same shape has a format problem, not a hook problem.
3. **The first lines of the three most recent posts**, scored with
   [`../x-post/hookscore.py`](../x-post/hookscore.py). This is where most accounts lose.
4. **Rhythm.** Not frequency — consistency. Nine posts in one week and then nothing for a month is
   worse than one a day forever.
5. **The reply habit.** Half of growth is `/x-engage`. If the account never replies to anyone, say
   so; it is usually the real answer.

## What to hand back

- the single biggest fix, named, with what to do this week
- three things that are already working, so they do not break them. Be specific; "your tone is good"
  is not an observation.
- what NOT to do yet, and why

Never open an audit with praise you do not mean, and never end one with a list of twenty things.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
