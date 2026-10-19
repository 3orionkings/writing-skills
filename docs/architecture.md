# Architecture

This page explains how the skills, the checkers and the packaging fit together, and why they are built the way they are.

## Two layers of skills

The humanizer holds the rules for prose that reads as written by its author: the vocabulary to avoid, the sentence shapes to avoid, the structure of an email or a letter, what must survive word for word, and the rule against adding facts. On its own it rewrites drafts and writes short pieces.

Each of the eleven forms holds the structure of one kind of piece: what it is for, what to gather before writing, the shape and its variants, the moves, the language, the figures, the ways an imitation goes wrong, a workflow and a skeleton. A form's first step is to load the humanizer, so the rules apply to every form without being repeated in full. Where the humanizer is not installed, each form carries `references/human-writing-rules.md`, a condensed copy of the same rules, so it still holds on its own.

Formatting is the one place where the layers could conflict, since the humanizer bans headings and bullets in prose and several forms need them. The humanizer's "Formatted content" section settles it: a loaded form's template governs structure, and so do the departures the form names. The no-markdown rule applies to emails, letters, messages and running prose.

## The checkers

Every skill's workflow ends by running two scripts on the draft and fixing what they report.

`lint.py` works sentence by sentence. Hard findings are patterns the rules exclude outright: dashes used as punctuation, tell vocabulary and phrases, markdown in prose, chatbot framing, negative parallelism, emoji and decorative symbols, connective openers, significance framing. Soft findings need judgement: groups of three, participial tails, hedges, uniform sentence length, repeated openings, self-answered questions, fragments, aphorism formulas, copula avoidance, gap-filling speculation, and words that are tells only in a figurative sense. The linter is the only place the vocabulary is defined; `lint.py --list` prints it.

`style_check.py` reads a form's `style.json` and checks the draft's shape: length, headings, bullets, numbered outlines, where the bold thesis sits, the first and last sentence, whether a method paragraph or an objection is present, links, numbers, figures and captions, a references section, the first-person rate. It finds where the body ends (at the first footnote, a references or notes heading, or a dated footer) and reads the close from the body, not from the footnotes. A form with several formats declares them as variants in `style.json`, and the workflow passes the one it chose with `--variant`.

Both checkers are heuristics. Passing them means the draft has none of the patterns they know and the shape the form asks for. It does not mean the draft is good, which is why each skill also tells the model what a good piece does.

## Why each skill carries its own copy of the scripts

A skill is installed and loaded on its own, by a harness that may not have the other eleven. So each skill folder holds the scripts it runs and the rules file it falls back on. To keep twelve copies from drifting, they are never edited in place: `shared/` holds the one source, `tools/sync_shared.py` copies it out, and the tests fail if any copy differs.

## Packaging for each harness

The repository is one plugin in a subfolder, `plugins/writing-skills/`, with a marketplace for each harness at the root. Keeping the plugin out of the repository root keeps development files (tests, tools, docs) out of what users install, and it follows the layout both harnesses document for marketplaces.

| Harness | Marketplace file | Plugin manifest it reads | How skills are found |
|---|---|---|---|
| Claude Code | `.claude-plugin/marketplace.json` | `plugins/writing-skills/.claude-plugin/plugin.json` | the plugin's `skills/` folder |
| Codex and ChatGPT | `.agents/plugins/marketplace.json` | `plugins/writing-skills/plugin.json`, with `.codex-plugin/plugin.json` as the overlay | `skills/`, declared in the overlay as `./skills/` |
| Any skills folder | none | none | copy `skills/<name>/` into the folder |

Codex reads two manifests. The root `plugin.json` follows the portable Agent Plugins format and holds the plugin's identity. The overlay in `.codex-plugin/plugin.json` repeats that identity, for Codex versions that read only the overlay, and adds the OpenAI-specific `interface` block (display name, descriptions, category, default prompts). Current Codex versions take the overlay's interface only when the root manifest has no `extensions` block, so the root manifest deliberately has none. `tools/validate.py` checks that all three manifests agree.

Each skill also has `agents/openai.yaml`, which gives Codex and ChatGPT a display name, a one-line description and a starter prompt. Claude Code ignores it.

## Tests

`tests/run_tests.py` runs four suites against the skills:

- **lint**: sentences that must and must not be flagged, and every word from the research catalogue.
- **style**: drafts in `tests/cases/` that must pass or fail each form's checks, for the base form and each variant. `tests/build_cases.py` generates them.
- **docs**: wording that must be present in, or absent from, the skills and references, so a rule cannot be edited out by accident.
- **shared**: every copy of the shared files matches `shared/`.

`tools/validate.py` covers the packaging: manifests, versions, marketplaces, skill names and descriptions, and the README. CI runs both on Linux and macOS for every push and pull request.
