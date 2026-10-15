---
name: x-profile
description: >-
  Write and score an X (Twitter) profile - bio, handle, pinned post and header
  as one unit - so a stranger knows what you do and why to follow in five
  seconds. Use for "review my profile", "rewrite my bio", "my profile is bad",
  "profile audit", or a pasted profile.
---

# x-profile

A profile has one job: a stranger lands on it from a post and decides in five seconds whether to
follow. Everything on it serves that decision or it is noise.

## Before you write

1. Read `~/.claude/x/voice.md` if it exists. If it does not, ask for **five of their own posts that
   did well** and write it.
2. Never invent a credential, a number or a result. If the user cannot back a claim, it does not go
   in the bio.

## Score it as one unit, not four parts

Read the four together, the way a visitor does:

1. **Handle.** A real name, not a keyword salad. If the handle is `AI_Growth_Ninja_42`, say so.
2. **Bio.** Three lines maximum. Line one: what you do and for whom. Line two: the proof — a number,
   a name, a role. Line three: the person, or a reason to stay. No "passionate about", no emoji
   walls, no link dump.
3. **Pinned post.** The pinned post is the real bio. It should be the single best post you have —
   the one that shows the thing you want to be known for. If there is no good candidate, that is the
   finding.
4. **Header and avatar.** Readable at small size, consistent with what the bio promises.

## What to hand back

- the score, with the one change that moves it most
- three rewritten bios at different angles, and the one you would ship
- a recommendation for the pinned post, or the note that none exists yet

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
