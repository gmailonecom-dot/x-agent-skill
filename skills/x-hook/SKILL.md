---
name: x-hook
description: >-
  Write and lint the first line and the media for an X (Twitter) post as one
  pairing, checking the fold, duplication, vagueness and hashtag noise before
  you post. Use for "check my post", "will this get read", "my reach is bad",
  "first line", or any request to lint or rewrite a post's opening.
---

# x-hook

The first line and the image are ONE unit. On X they sit on the same click surface: the timeline
shows your line and your picture together, and writing them apart is why half of a post says the
same thing twice.

```bash
python3 lint.py --line "..." --media "AI RAN IT"
python3 lint.py posts.txt                 # one post per line, ranked
```

## Before you write

1. Read `~/.claude/x/voice.md` if it exists. If it does not, ask for **five of their own posts that
   did well** and write it.
2. Never invent a number, a result or a source. Ask for it or write the line without it.

## Rules the tool enforces, and why

- **The fold.** X shows roughly the first line before "show more". The line has to earn the tap on
  its own; a line that only makes sense with the second line loses the reader who never saw it.
- **The image must not repeat the first line.** Different words, same promise.
- **Four words maximum on the image.** At timeline size a fifth word is a grey smear.
- **Hashtags: two is the ceiling, and usually zero is right.** They are not a discovery mechanism
  the way people think, and a line of them reads as a bot.
- **A number, a name or a date** beats every adjective available to you.
- **No link in the post body if reach matters.** Put it in the first reply and say so.

## Write ten, keep two

Generate ten first lines, run them all through `lint.py`, show the user the top three with their
scores and the specific issue on each. For the winner, write the media brief: the image or the
screenshot, the three or four words on it, and what has to hold contrast at timeline size.

## The gate

Nothing here publishes. This skill writes and you publish. Every output ends in a block the user
copies, and the last line of every run is the question: **ship it, or change it?**
