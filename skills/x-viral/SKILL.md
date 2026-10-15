---
name: x-viral
description: >-
  Find what is actually working in the user's niche on X (Twitter) and rank it
  by how far each post beat its own account's median, then name the formula.
  Use for "what's working right now", "find viral posts in my niche", "why did
  this blow up", competitor research, or a swipe file.
---

# x-viral

Big accounts win every ranking by size. That tells you nothing, because you are not them. What you
want is the post that beat its OWN account's median — the format that worked on a normal account.
That is the one you can copy.

This skill reads public listings. It never logs in as the user and never touches their credentials.

## Before you write

1. Read `~/.claude/x/voice.md` if it exists. If it does not, ask for **five of their own posts that
   did well** and write it.
2. Never invent a number, a result or a source. If the user cannot give you the numbers, work from
   what is visible and say so.

## How to rank

1. Collect a set of recent posts from a handful of accounts in the niche (public listings only).
2. For each account, work out its own median engagement. The user may have to supply a number for
   their own account; ask rather than guess.
3. Rank every post by its **multiple over its own account's median**, not by raw likes. A post at 6x
   its account's median on a small account is a better lesson than a big account's average day.
4. Name the formula each outlier used, against [`../x-post/hooks.json`](../x-post/hooks.json). The
   classification is about the words you can see, not a claim about why it got its views.

## What to hand back

- the ranked outliers, each with its multiple over its own median
- the formula the top three share, named, with the exact first lines
- one format the user can run this week, adapted to their voice — not copied verbatim

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
