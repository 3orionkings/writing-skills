# Changelog

All notable changes to this project are recorded here. The format follows [Keep a Changelog](https://keepachangelog.com/en/1.1.0/), and versions follow [semantic versioning](https://semver.org/).

## [Unreleased]

## [1.0.0] - 2026-10-19

The first release.

### Added

- Twelve skills: `humanizer`, and the forms `one-idea-post`, `thesis-first-note`, `principle-column`, `mechanism-essay`, `strategy-pattern-essay`, `technical-principles-essay`, `field-guide`, `patterns-survey`, `reportage-deep-dive`, `taxonomy-explainer` and `curated-evidence-page`.
- A plugin for Claude Code (`.claude-plugin/plugin.json`) and for Codex and the ChatGPT desktop app (a portable `plugin.json` with a `.codex-plugin/plugin.json` overlay), with a marketplace for each at the repository root.
- Codex and ChatGPT display metadata (`agents/openai.yaml`) for every skill.
- `tools/validate.py`, which checks that manifests, versions, skills and the README agree, and that no file names a person on its hashed list.
- Continuous integration on GitHub Actions: the test suite, the shared-file check and the validator on Linux and macOS.

### Changed

- The skills moved to `plugins/writing-skills/skills/`; the tools and tests now look there by default.
- `tools/package.py` builds one `.skill` file per skill and a `writing-skills.zip` holding only `skills/`, ready to unzip into a skills folder.
- The humanizer and the shared rules refer to "the assistant" instead of a particular model, so the skills read correctly in any harness. The watermark notes still name the vendors they describe.

### Fixed

- 24 defects found in a pre-release audit of the linter, the structure checker, the humanizer and the forms, from context-blind vocabulary flags to close checks that read a footnote instead of the closing paragraph. The audit's test suite went from 32 of 128 passing to 128 of 128. Each fix is described in [docs/release-notes/1.0.0.md](docs/release-notes/1.0.0.md).

### Known issues

- A sentence that uses two words which are tells in their figurative sense but literal there (an insurance clause, for example) gets two hard findings, because the linter treats two such words in one sentence as a cluster.
- The twelve skill descriptions total about 11,000 characters, over Codex's default skill-list budget of 8,000, so Codex shortens them.
- `reportage-deep-dive` and `field-guide` list "no typos" among the ways an imitation fails. The intent is to leave the author's typos alone, but the line could be read as an instruction to add some.

[Unreleased]: https://github.com/3orionkings/writing-skills/compare/v1.0.0...HEAD
[1.0.0]: https://github.com/3orionkings/writing-skills/releases/tag/v1.0.0
