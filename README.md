# Prospero

**Status:** activated 2026-11-09; first increment being defined with Zach.
This repository holds only a foundation (licence, purpose records, tests, CI). It has no features yet.

## What it is for

In the words recorded in the project's lane seed, summarising Zach's stated purpose (decision DEC-128):

> - a creative-collaboration tool to help him write and publish articles and books with an agent network that keeps his decisions and preferences;
> - "cognitive augmentation for artists", without replacing the artist;
> - later versions remixed by professional artists (bonsai pruning, classroom, tutor, exercise generator);
> - the vehicle for his papers that define Cognitive Augmentation, which he then edits into shape.
> - *Ariel* is reserved for the agent layer, if that layer is ever named separately.

These lines summarise intake notes; they are not a verbatim transcript. Zach's own statement of purpose will
replace them, and will become the purpose record `P0` in `.aec/records.jsonl` (still a stub).

## Name

PlayWrite → Prospero (DEC-128, 2026-11-05). The repository is still called `PlayWrite`; renaming it is Zach's call.

## Working here

- Read [AGENTS.md](AGENTS.md) before changing anything, whether you are a person or an agent.
- Tests: `python3 -m unittest discover -s tests -v` (standard library only, Python 3.10+).
- Purpose records: `.aec/` ([Telosmith](https://github.com/eraevous/Telosmith)). CI runs `aec check` on every push.

## Licence and contributions

MIT, see [LICENSE](LICENSE). Contributions are accepted under the [Contributor License Agreement](CLA.md).
