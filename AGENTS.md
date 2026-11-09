# AGENTS.md: rules for agents (and people) working in this repository

## Who decides

- **Product direction, scope and purpose come from Zach.** Agents build what has been agreed with him and
  recorded in a handoff or a decision. Anything else an agent suggests is a **proposal, not direction**:
  write it up (pull request description, issue, or a proposed decision) and let Zach decide.
- The purpose record `P0` in `.aec/records.jsonl` is a stub until Zach states the purpose in his own words.
  Do not fill it in for him.
- Never merge, never force-push. Open draft pull requests.

## How code is written

- **Standard library first.** Do not add a third-party dependency without a recorded decision.
- **Parsimony and modularity.** Small modules with one job each; no new subsystem without a dissent review
  (what purpose it might violate, the evidence for and against, what follows, what to test).
- **Commented for human readers.** Explain why, not only what. A reader who is not a programmer should be able
  to follow what each module is for.
- Every change keeps `python3 -m unittest discover -s tests` passing and `aec check` clean.

## What never enters this repository

- **Nothing personal or employer-related**: no personal details, no private conversations, no work material.
- **No personal writing corpora**: drafts, manuscripts, notes and source material for the writing Prospero
  helps with live outside the repository. Tests and examples use synthetic or public-domain text only.
- No secrets, tokens or credentials.

## Purpose records (Telosmith)

`.aec/records.jsonl` is append-only: add a new version of a record instead of editing a line. Before you finish
a change:

```bash
python3 -m aec edges . -o .aec/edges.jsonl
python3 -m aec check .aec/records.jsonl --edges .aec/edges.jsonl
```

`.claude/settings.json` runs the same check after every edit made by Claude Code; CI runs it on every push.
