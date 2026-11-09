# Prospero

**Status:** activated 2026-11-09; first increment being defined with Zach.
This repository holds only a foundation (licence, purpose records, tests, CI). It has no features yet.

## What it is for

Zach has not yet stated the purpose in his own words. When he does, it becomes the purpose record `P0` in
`.aec/records.jsonl` (a stub until then). Until then, only these facts are adopted:

- Prospero is the name of the creative-collaboration tool formerly called PlayWrite (decision DEC-128, 2026-11-05).
  *Ariel* is reserved for its agent layer, if that layer is ever named separately (same decision).
- Development was activated on 2026-11-09 (DEC-182).
- This repository holds the mechanics (code, docs, tests) and no content: no works and no corpora (DEC-183).

### Ideas on record, not requirements

Recorded in intake notes (paraphrased, not verbatim) while the idea was being explored. They are context for
discussion with Zach, not product requirements, and nothing here should be built from them alone:

- Zach: a tool to write and publish articles and books with an agent network that keeps his decisions and preferences.
- Zach: later versions remixed by professional artists (bonsai pruning, a classroom, a tutor, an exercise generator).
- Zach: the papers that define Cognitive Augmentation are to be written with it.
- Kate (an assistant in the project, not Zach): "cognitive augmentation for artists", not replacement.

## Name

PlayWrite → Prospero (DEC-128). Zach authorized renaming the repository to Prospero (DEC-183); until that is
done the repository is still called `PlayWrite`.

## Working here

- Read [AGENTS.md](AGENTS.md) before changing anything, whether you are a person or an agent.
- Tests: `python3 -m unittest discover -s tests -v` (standard library only, Python 3.10+).
- Purpose records: `.aec/` ([Telosmith](https://github.com/eraevous/Telosmith)). CI runs `aec check` on every push.

## Licence and contributions

MIT, see [LICENSE](LICENSE). Contributions are accepted under the [Contributor License Agreement](CLA.md).
