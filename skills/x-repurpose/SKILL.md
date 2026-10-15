---
name: x-repurpose
description: >-
  Turn an existing piece - a video, a blog, a newsletter, a talk - into X
  (Twitter) posts and a thread, in the user's voice. Use for "repurpose this",
  "turn this into posts", "make a thread from this", or a pasted transcript or
  article.
---

# x-repurpose

You already made the thing. The job is not to shorten it, it is to find the parts of it that stand
alone as posts, and the spine that makes one thread.

## Before you write

1. Read `~/.claude/x/voice.md` if it exists. If it does not, ask for **five of their own posts that
   did well** and write it.
2. Never invent a number, a result or a source. Everything comes from the piece. If a figure is not
   in it, do not add one.

## How to mine the piece

1. **Find the standalone moments.** A 40-minute video is maybe five posts, not one thread. Each is a
   moment that means something on its own with no context.
2. **Find the spine.** Separately, look for the one argument that runs through the whole piece. That
   is the thread — its first post is the argument's sharpest sentence, rewritten as a hook and scored
   with [`../x-post/hookscore.py`](../x-post/hookscore.py).
3. **Rewrite, do not paste.** A transcript sentence is spoken; a post is read. Cut the filler, lead
   with the point, break the lines.

## What to hand back

- five standalone posts, each under 280 characters, each with its own first line
- one thread, using `/x-thread`'s shape, with the payoff marked
- a note on which single post is the strongest, and why

Do not hand back the whole piece reformatted. If nothing in it stands alone, say so plainly — that is
a useful answer.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
