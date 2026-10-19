# AGENTS.md

Guidance for coding agents (Claude Code, Codex and others) working in this repository. [CONTRIBUTING.md](CONTRIBUTING.md) says the same for people, at more length.

## What this repository is

One plugin, `writing-skills`, holding twelve agent skills: a humanizer and eleven writing forms that stack on it. The product is the text of each `SKILL.md` and its `references/`. The Python scripts are the checkers those skills run on their own drafts. The plugin installs in Claude Code, Codex and the ChatGPT desktop app, and each skill folder also works on its own.

## Layout

```text
plugins/writing-skills/
  plugin.json                  portable Agent Plugins manifest (identity only, no extensions block)
  .codex-plugin/plugin.json    Codex overlay: identity, "skills": "./skills/" and the interface block
  .claude-plugin/plugin.json   Claude Code manifest
  skills/<name>/
    SKILL.md                   the skill
    agents/openai.yaml         Codex and ChatGPT display metadata
    scripts/lint.py            copy of shared/lint.py (all twelve)
    scripts/style_check.py     copy of shared/style_check.py (the eleven forms)
    references/                human-writing-rules.md (copy, forms) or ai-tells.md (humanizer)
    style.json                 the form's structural spec and variants (forms only)
shared/                        the only place to edit lint.py, style_check.py, human-writing-rules.md
tools/sync_shared.py           copies shared/ into the skills; --check verifies
tools/validate.py              manifests, versions, skills and README agree
tools/package.py               builds dist/*.skill and dist/writing-skills.zip
tests/                         run_tests.py, build_cases.py, the JSON case files and tests/cases/
.claude-plugin/marketplace.json     Claude Code marketplace, points at ./plugins/writing-skills
.agents/plugins/marketplace.json    Codex marketplace, points at ./plugins/writing-skills
docs/                          architecture.md and release notes
```

## Invariants

The tests and `tools/validate.py` enforce all of these. Do not work around a failing check; fix the cause.

1. **One source for shared files.** Edit `shared/lint.py`, `shared/style_check.py` and `shared/human-writing-rules.md`, then run `python3 tools/sync_shared.py`. Never edit the copies under `plugins/writing-skills/skills/`. Each skill carries its own copy because a skill is installed and loaded on its own and must work without the others.
2. **One version.** The version appears in `plugin.json`, `.codex-plugin/plugin.json`, `.claude-plugin/plugin.json`, both the `metadata` and the plugin entry of `.claude-plugin/marketplace.json`, and the newest `## [x.y.z]` heading of `CHANGELOG.md`. Change them together.
3. **One identity.** `name`, `description`, `license`, `homepage`, `repository` and `author` are identical in the three plugin manifests.
4. **Codex overlay rules.** `.codex-plugin/` holds `plugin.json` and nothing else. The root `plugin.json` has no `extensions` block, because Codex ignores the overlay's `interface` when one is present.
5. **Skill identity.** A skill's folder name equals its frontmatter `name`: lowercase words joined by hyphens, 64 characters at most. The description is 1,024 characters at most, and each form's description ends with a "Not for:" line naming the sibling to use instead. Every skill has `agents/openai.yaml` with a `display_name` and a `short_description` of 64 characters at most.
6. **README lists every skill** by its backticked name.
7. **No names of people.** No file names the writers whose published work informed the forms, or the authors of the studies the catalogue cites. Cite a study by its title and venue. `tools/validate.py` fails on any name from its hashed list; never add the names themselves to a file to test this.

## Rules for the skill text

- **Neutral voice.** A skill carries no author profile and no profession's defaults. Voice comes from the user's draft and the conversation.
- **No invented facts.** Every number, name, date and quoted remark in an output comes from the user's material; otherwise the skill leaves a bracketed placeholder or asks. Examples inside a skill use placeholders such as `[date]`, never real-looking specifics a model could reuse.
- **Moves, not sentences.** The forms were derived from published writers. They encode structure and moves only. Do not add text, coined terms or anecdotes from those writers.
- **Harness-neutral wording.** Refer to "the assistant" or address the model directly. Name a vendor only to state a fact about that vendor, as the watermark notes do.
- **Front-load descriptions.** Codex shortens skill descriptions when the list passes its budget, so the first sentence must say what the skill writes.
- **The skills follow their own rules.** After editing a `SKILL.md` or a reference file, lint it with `--allow-markdown`. Hard findings are acceptable only inside quoted examples of a tell.

## Before you finish a change

```bash
python3 tools/sync_shared.py
python3 -I -B tests/run_tests.py
python3 tools/validate.py
claude plugin validate . --strict
claude plugin validate plugins/writing-skills --strict
```

The last two need the Claude Code CLI; CI runs everything else. Codex has no validation command, so `tools/validate.py` checks the Codex manifests against the published format.

## Tests

- `tests/lint_cases.json` and `tests/vocab_catalogue.json` hold the linter cases. Every linter change gets a case that must flag and a case that must not.
- `tests/style_cases.json` lists the structure-checker cases; the drafts in `tests/cases/<skill>/` are generated by `tests/build_cases.py`. Edit `build_cases.py`, run it, and commit the regenerated drafts.
- `tests/doc_checks.json` holds wording that must be present in, or absent from, the skills and references.
- Write the failing test first, then the fix.

## Adding a skill

1. Create `plugins/writing-skills/skills/<name>/` with `SKILL.md`, `agents/openai.yaml` and, for a form, `style.json`.
2. Add the name to `STYLE_SKILLS` (forms) in both `tools/sync_shared.py` and `tests/run_tests.py`, then run `python3 tools/sync_shared.py` to copy the shared files in.
3. Add style cases in `tests/build_cases.py` and doc checks for any rule the skill must keep.
4. Add the skill to the README table and to "Choosing a form", and give its nearest siblings a "Not for:" pointer to it.
5. Add a `CHANGELOG.md` entry and bump the minor version.

## Releasing

Versions follow semantic versioning. A patch fixes wording or a checker without changing what passes. A minor version adds a rule, check, variant or skill. A major version removes or renames a skill, a variant or a script option. To release: bump the version in the places listed under Invariants, write the `CHANGELOG.md` entry, run the checks, tag `vX.Y.Z`, and attach the output of `python3 tools/package.py` to a GitHub release.

## Do not

- Commit `dist/`, `__pycache__/` or test output.
- Add third-party dependencies to the scripts. They are standard library only and must run on Python 3.8.
- Install the plugin or copy skills into `~/.claude`, `~/.agents` or `~/.codex` while working here.
