# The X agent skill

Eleven agent skills that run an X (Twitter) account. Free, MIT, no signup, no API key, nothing to
connect.

One of them writes your post off 21 hook formulas and scores the hook before you post it. One lints
the first line and the media as a single pairing, because the fold and the image are one click
surface and writing them apart is why half of it says the same thing twice. One reads your analytics
export and names the exact post where people stopped. One turns a video, a blog or a newsletter into
a thread. One finds what is working in your niche and ranks it by how far each post beat its own
account, not by how big the account is. One goes and finds the accounts in your field worth replying
to, and drafts the reply that earns a follow.

**Nothing gets posted until you do it.** These skills write. You post.

## Install

Paste this into your agent:

```
https://github.com/gmailonecom-dot/x-agent-skill

Install this skill, then confirm /x-post works.
```

Or do it yourself:

```bash
git clone https://github.com/gmailonecom-dot/x-agent-skill.git
cp -r x-agent-skill/skills/x-* ~/.claude/skills/
```

Project-local instead of global: copy the same folders into your repo's `.claude/skills/`. No Claude
Code at all? Paste any single `SKILL.md` at the top of a chat and it runs as a mode. You lose the
three Python tools, which is most of the point of `/x-post`, `/x-hook` and `/x-analytics`, but the
rest works.

Then spend ten minutes on [`templates/voice.md`](templates/voice.md). Copy it to `~/.claude/x/voice.md`
and fill it in. Every skill reads that file.

## The eleven

| command | what it does |
| --- | --- |
| `/x-post` | One idea into a post. Five hooks off [21 formulas](skills/x-post/hooks.json), scored, then the post with its first line doing the work. |
| `/x-thread` | One idea into a numbered thread, with the turn, the payoff and the ask marked. |
| `/x-hook` | The first line and the media linted as one pairing: the fold, duplication and vagueness. |
| `/x-reply` | Your replies and mentions triaged into four piles, then drafted in your voice. Says which one to pin. |
| `/x-engage` | The accounts in your field worth replying to, ranked, and the reply that earns a follow. |
| `/x-plan` | A week that fits the hours you actually have. One anchor, a couple of cheap ones, a thread. |
| `/x-viral` | What is working in your niche, ranked by multiple over each account's own median. |
| `/x-analytics` | Your export read properly: the fold, the drop, the outliers, and what to change. |
| `/x-repurpose` | A video, blog or newsletter into posts and a thread. |
| `/x-profile` | Bio, handle, pinned post and header as one unit, scored. |
| `/x-audit` | The whole account, ending in ONE fix rather than twenty. |

## The three tools

Dependency-free Python 3. They are the reason the skills are not just prompts.

```bash
python3 skills/x-post/hookscore.py --hook "one line"      # 5-property hook panel
python3 skills/x-hook/lint.py --line "..." --media "..."  # first line + media linter
python3 skills/x-analytics/analytics.py posts.csv         # outliers by own-account multiple
```

## The fine print

**It does not post.** The X API would allow it with your own keys, and this pack deliberately does
not use them. Every skill ends in a block you copy and a question — ship it, or change it? Anything
that claims to run your account unattended should be read with that distinction in mind.

**`hookscore.py` is a heuristic, not a predictor.** It separates deliberately bad first lines from
real ones well. It separates a given creator's hits from their own misses barely at all. A low score
is a reason to look again; a high score is not a promise.

**`/x-viral` and `/x-engage` read, they do not scrape.** Public listings only. They never log in as
you and never touch your credentials.

**Hashtags barely matter** and this pack says so instead of selling you a hashtag generator.

**Nothing invents a number.** If a skill wants a figure it does not have, it asks you for it or
writes the line without it.

## Licence

MIT. Use it, change it, ship it.
