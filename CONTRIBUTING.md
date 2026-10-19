# Contributing

Thanks for helping. Most useful changes fall into three kinds: a tell the linter misses or flags wrongly, a form that produces the wrong shape, and a skill instruction a model misreads. Each is easiest to act on with an example.

## Reporting a problem

Open an issue with:

- the skill, and the variant if you passed one;
- the input you gave and the output you got, or the sentence the linter flagged or missed;
- what you expected, and why. For a missed tell, say where it comes from (a study, a style guide, a pattern you see often in machine text). For a wrong flag, say what the word means in your field.

Leave out anything confidential. A short invented example that shows the same problem is enough.

## Changing a skill or a checker

1. Read [AGENTS.md](AGENTS.md). Its invariants apply to people too.
2. Write the test first. Linter cases go in `tests/lint_cases.json`, with one sentence that must flag and one that must not. Structure cases go in `tests/build_cases.py`; run `python3 tests/build_cases.py` to regenerate the drafts. Wording that a skill must keep goes in `tests/doc_checks.json`.
3. Make the change. Shared scripts and the shared rules file are edited in `shared/` only, then copied out with `python3 tools/sync_shared.py`.
4. Run the checks:

```bash
python3 -I -B tests/run_tests.py
```

```bash
python3 tools/validate.py
```

If you have the Claude Code CLI, also run `claude plugin validate . --strict` and `claude plugin validate plugins/writing-skills --strict`.

5. Add a line under `[Unreleased]` in `CHANGELOG.md`.

## How the skills are written

The skills hold to their own rules, so a change to a `SKILL.md` should read as plain, specific prose: no tell vocabulary, no stacked hedges, no closing summary. Lint it with `--allow-markdown` before you open a pull request.

Three rules matter more than the rest. A skill never tells the model to invent a fact, a source or an anecdote; where a form needs a detail the user has not supplied, it asks for it or leaves a placeholder. A skill carries no author profile; the voice comes from the user. And the forms encode moves, not sentences: do not paste in text from the pieces a form was derived from, or from anyone else, and do not name the people behind them. Cite studies by title and venue rather than by author; the validator fails if a listed name appears anywhere in the repository.

## Pull requests

Keep a pull request to one change. Say what it fixes, show the before and after on the example from the issue, and confirm the checks pass. CI runs the test suite and the validator on every pull request.

## Licence

By contributing you agree that your contribution is licensed under the [MIT License](LICENSE).
