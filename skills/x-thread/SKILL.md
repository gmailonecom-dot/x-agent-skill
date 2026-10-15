---
name: x-thread
description: >-
  Turn one idea into a numbered X (Twitter) thread - the first post that earns
  the tap, the beats in order, the payoff and the ask marked. Use for "write a
  thread", "turn this into a thread", "how do I structure this", or a long idea
  that will not fit in one post.
---

# x-thread

A thread is a post with a spine. If the first post does not work alone, the other nine are never
read.

## Before you write

1. Read `~/.claude/x/voice.md` if it exists. That is the user's voice profile. If it does not exist,
   ask for **five of their own posts that did well**, read them, infer the voice, and write the file.
2. Never invent a number, a result or a source. Ask for it or write the line without it.

## The shape

1. **Post 1 is a post, not an intro.** It uses `/x-post`'s rules: a scored hook off
   [`../x-post/hooks.json`](../x-post/hooks.json), run through
   [`../x-post/hookscore.py`](../x-post/hookscore.py). No "a thread 🧵" as the whole first line — the
   🧵 can sit at the end, but the line has to promise something on its own.
2. **One beat per post.** Each numbered post makes exactly one point and can stand alone. If a post
   needs the previous two to make sense, it is a paragraph, not a beat.
3. **The turn** (post 2). Say what the thread will do, in one sentence, and start doing it.
4. **The body** (posts 3 to n-2). The steps, the list, the teardown — whatever the hook promised.
   Mark the payoff beat so the user knows where the thing they clicked for actually lands.
5. **The payoff** (second to last). Deliver it explicitly and say so: "that is the prompt, it is in
   the last post".
6. **The close** (last post). One ask. Not three. If it is a follow, say why, in one clause.

## What to hand back

- the scored first post, and the runner-up hook beside it
- the full thread, numbered, one beat per post, each under 280 characters with its count
- a one-line note on where the payoff lands and why there
- which beat is the one most likely to be quoted, so the user can make it the strongest

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
