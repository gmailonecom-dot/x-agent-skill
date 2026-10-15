---
name: x-post
description: >-
  Write an X (Twitter) post from a raw idea - five hooks off 21 formulas,
  scored, then the post with its first line doing the work. Use whenever the
  user wants a post, a tweet, an opening line, "what should I say", or is
  about to post and does not have the first line yet.
---

# x-post

One idea into a post somebody stops for.

On X the first line is the whole job. It is the only line the timeline shows before the fold, and it
is the only thing most people will ever read. Two tools live in this folder and both actually run.
Use them. Do not eyeball the hook.

```bash
python3 hookscore.py hooks.txt              # rank your hook options
python3 hookscore.py --hook "one line"      # score a single one
```

## Before you write

1. Read `~/.claude/x/voice.md` if it exists. That is the user's voice profile: who they talk to, the
   words they never use, what they will not claim. If it does not exist, ask for **five of their own
   posts that did well**, read them, infer the voice, and write the file. A post in the wrong voice
   is worse than no post.
2. Never invent a number, a result or a source. If a figure would strengthen it and you do not have
   one, ask for it or write the line without it.

## The shape

**The first line is the whole job.** It does three things or the post is scrolled past: it earns the
fold (the reader taps "show more"), it opens a question they cannot close, and it proves a payoff
exists.

1. **Hook.** Write FIVE against [the 21 formulas](hooks.json), run them through `hookscore.py`, keep
   the top two, and show the user both with their scores. Never hand over one hook.
2. **The turn** (lines 2-3). Say what the post is going to do, in one sentence, and start doing it.
   No throat-clearing — "Let me explain", "Here's the thing", "Unpopular opinion:" are the single
   most common cause of a post dying at the fold.
3. **The body.** One idea. Short lines. A line break every sentence or two, because the timeline is
   a narrow column and a paragraph is a wall.
4. **The payoff.** Deliver the thing the hook promised, explicitly: "here is the prompt", "here are
   the three". Say that you are delivering it.
5. **The close.** One ask, or none. A post that asks for a follow, a repost and a reply is asking
   for nothing.

## What to hand back

- the two best hooks with their scored panels
- the post, inside 280 characters, with the character count
- the first line quoted separately, because that is the part that decides everything
- one line naming which formula the winning hook used and why it fits this idea

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
