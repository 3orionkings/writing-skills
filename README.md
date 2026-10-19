# Writing Skills

Twelve agent skills for writing that reads as if a person wrote it. The humanizer removes the patterns that readers and detectors use to spot machine prose, and keeps your facts, citations and voice exactly as you gave them. Eleven forms give a piece the structure of a kind of writing that works: a one-idea post, a principle column, a mechanism essay, a field guide, a research explainer and six more. Every skill ships a linter and every form ships a structure checker, so the agent checks its own draft before you see it.

The skills install as a plugin in Claude Code, Codex and the ChatGPT desktop app, or as plain skill folders anywhere that reads `SKILL.md`.

## How the skills fit together

The humanizer is the base layer. It rewrites or drafts prose in the author's own voice: plain words in place of the vocabulary models overuse, varied sentence length, none of the set-piece rhythms (the reflexive group of three, the negative parallelism, the fragment for punch), no opener announcing the topic's importance and no closing summary. It marks what must survive word for word (citations, figures, names, defined terms, the sign-off, the phrasing of the author's trade) and never adds a fact the author did not supply.

Each form stacks on top. A form loads the humanizer first, then adds a template, the moves that make that kind of piece work, an evidence policy and a checker for its structure. Where a form needs something the humanizer bans, such as a fragment in reportage or rhetorical questions in a reflective note, it says so in a short "Departures from the humanizer" section and the linter's finding on it can stay.

Two scripts do the checking, and the agent runs both before it hands a draft back:

- `scripts/lint.py` flags machine-writing tells at sentence level. Hard findings must be fixed; soft ones get a second look. It exits with status 1 while any hard finding remains.
- `scripts/style_check.py` checks a draft against its form: length, headings, where the thesis sits, whether a method paragraph or an objection exists, whether figures carry full-sentence captions, whether the close summarises. Each form has variants for its different formats.

Both are single Python files with no dependencies.

## The skills

| Skill | What it writes | Length (words) | Variants |
|---|---|---|---|
| `humanizer` | Rewrites a draft, or drafts from notes, so it reads as written by its author | any | |
| `one-idea-post` | One rule under an imperative title, earned by one story, closed on a call to act | 100 to 1,400 | `confessional`, `list-essay`, `miniature` |
| `thesis-first-note` | A belief in sentence one, the other side conceded in paragraph two, one analogy from outside the field | 180 to 1,500 | `headed-essay` |
| `principle-column` | An unbroken column that grants a trend, flips it in one sentence and names the principle underneath | 600 to 1,700 | `confessional-list`, `coaching` |
| `mechanism-essay` | A long position piece that defines its terms, builds the mechanism before the conclusion and answers the strongest objection | 1,800 to 16,000 | |
| `strategy-pattern-essay` | A strategy essay that names a mechanism with a two-word label and isolates one variable between two companies | 1,500 to 7,000 | |
| `technical-principles-essay` | An engineering essay that declares one lens and proves each principle with a measured, sourced number | 900 to 6,000 | `single-thesis`, `announcement`, `short-note`, `year-in-review` |
| `field-guide` | A practitioner's guide carried by one real case, with the artefact shown before it is explained | 1,200 to 13,000 | `faq`, `teardown`, `notes-page` |
| `patterns-survey` | A technical survey that engineers, product managers and scientists can all read, with a paper and a counted experience behind each claim | 700 to 18,000 | `essay` |
| `reportage-deep-dive` | Reportage on how work happens inside named companies, with the method on the page | 600 to 7,000 | `evergreen-guide`, `commentary` |
| `taxonomy-explainer` | Research notes that define a term, build a taxonomy and place each paper in one cell of it | 1,500 to 12,000 | |
| `curated-evidence-page` | A page where the list is the argument: dated, sourced entries with the number computed for the reader | 150 to 6,000 | `question-list`, `reading-list`, `dispatch` |

### Choosing a form

You can name a skill, or describe the piece and let the agent choose. Each description ends with a "Not for" line that points to the right sibling, which keeps the close calls apart:

- A short first-person piece: `one-idea-post` when it gives the reader a rule, `thesis-first-note` when it argues a belief calmly, `principle-column` when it reframes a trend for people who run teams.
- A long argument: `mechanism-essay` for a contested question of policy or technology, `strategy-pattern-essay` for why a company or market works the way it does, `technical-principles-essay` when the proof is a measurement or a demo.
- Practical writing: `field-guide` when one case and its artefacts carry the advice, `patterns-survey` when the items are techniques backed by papers, `reportage-deep-dive` when the material comes from interviews and named companies.
- Reference: `taxonomy-explainer` for a literature, `curated-evidence-page` for a list you will keep adding to.

## Install

The repository is a marketplace for both Claude Code and Codex. While the repository is private, installing needs git access to it, for example through `gh auth login`.

### Claude Code

Add the marketplace, then install the plugin:

```bash
claude plugin marketplace add 3orionkings/writing-skills
```

```bash
claude plugin install writing-skills@writing-skills
```

Inside a session the same steps are `/plugin marketplace add 3orionkings/writing-skills` and `/plugin install writing-skills@writing-skills`. The skills then appear as `/writing-skills:humanizer`, `/writing-skills:field-guide` and so on, and they also load on their own when a request matches a description. Run `claude plugin marketplace update writing-skills` to pick up a new release.

### Codex and the ChatGPT desktop app

Add the marketplace:

```bash
codex plugin marketplace add 3orionkings/writing-skills
```

Then install the plugin:

```bash
codex plugin add writing-skills@writing-skills
```

You can also install it from the plugin browser instead: type `/plugins` in Codex, or open the Plugins tab in the ChatGPT or Codex desktop app and select the plus button on Writing Skills. Start a new session or chat afterwards; the desktop apps pick up a new marketplace after a restart. Type `@` to call a skill by name, or describe the piece and let the model choose. Skills that arrive in a plugin are also available in ChatGPT's Chat and Work modes. Run `codex plugin marketplace upgrade writing-skills` to pick up a new release. To switch the plugin off for one project, add this to that project's `.codex/config.toml`:

```toml
[plugins."writing-skills@writing-skills"]
enabled = false
```

Codex lists every installed skill's description in a budget of about 8,000 characters by default. These twelve descriptions come to about 11,000, so Codex shortens them. If routing between forms gets worse, raise `skills.max_context_tokens` in your Codex config or disable the forms you do not use.

### As plain skill folders

Any tool that reads `SKILL.md` folders can use the skills without the plugin. Clone the repository:

```bash
git clone https://github.com/3orionkings/writing-skills.git
```

For Claude Code, copy the skills into your personal skills folder:

```bash
cp -R writing-skills/plugins/writing-skills/skills/. ~/.claude/skills/
```

For Codex, copy them into your agent skills folder:

```bash
mkdir -p ~/.agents/skills && cp -R writing-skills/plugins/writing-skills/skills/. ~/.agents/skills/
```

For claude.ai or another tool that takes uploaded skills, build one zip per skill with `python3 tools/package.py` and upload the files from `dist/`.

The checkers need Python 3.8 or later. Where the agent cannot run code, the skills still apply their rules and skip the checks.

## Using them

Give the agent your material and say what you want: "Humanize this email to our supplier about the late delivery", "Turn these notes into a field guide on evaluating our support bot", "Write a one-idea post about why I read plans before stand-ups; here's what happened". Paste the draft, the notes, the numbers and the story. The forms never invent a fact, a source or an anecdote. Where a form wants a detail you did not give, it leaves a placeholder such as `[date]` or asks for it.

You get the piece back on its own, with no preamble and no list of changes. Where a citation looks wrong, the humanizer keeps it exactly as written and says so in one line above the text.

You can run the checkers on any draft yourself:

```bash
python3 plugins/writing-skills/skills/humanizer/scripts/lint.py draft.md
```

```bash
python3 plugins/writing-skills/skills/field-guide/scripts/style_check.py draft.md --variant faq
```

`lint.py --list` prints every word and phrase the linter knows, by severity. `--allow-markdown` treats headings, bold and lists as soft for forms that use them. `--author-sample MINE.txt` lets dashes through at the rate your own writing uses them. `style_check.py --list-variants` shows a form's formats.

## Where the rules come from

The humanizer's catalogue (`references/ai-tells.md`) is built from published measurements: Pangram's corpus counts of AI-favoured words, phrases and punctuation, Pew Research Center's study of 490,000 web pages, the WikiProject AI Cleanup field guide, an ACL 2025 study finding that frequent LLM users spot machine text better than automated detectors, and a vocabulary study of 14 million PubMed abstracts. Each entry gives the pattern, how much more often it appears in machine text where that is known, and the source.

Each form comes from a close reading of four to seven published pieces of its kind, read in full across their formats and put through the same seven questions (how the prose sounds, how a piece is built, how the narrative moves, how the reasoning works, what thinking shows on the page, what the sentences do, who it is for). The skills encode the moves that came out of that reading, such as where the hedge goes, what counts as evidence and how the piece closes. They do not encode the sentences or phrasing of the pieces they were drawn from, because pastiche reads as machine-made to readers who know the original.

## Limits

- The skills change how text reads, not where it came from. Some current models, Claude models released since August 2026 among them, watermark their output statistically, and style edits do not remove that. Never present a humanized draft as undetectable.
- The checkers are heuristics. A draft that passes both can still read as generic, and some sentences will be flagged that should not be. One known case: when a single sentence uses two words that are tells in their figurative sense but literal there, as an insurance clause can, both get hard findings, because the linter reads two such words in one sentence as a cluster.
- The tests run on Linux and macOS. The scripts should work on Windows, where the command may be `python` instead of `python3`, but that is untested.
- The rules and examples are written in British English.

## Development

```text
plugins/writing-skills/        the plugin: manifests for each harness, and skills/
  skills/<name>/               SKILL.md, scripts/, references/, style.json, agents/openai.yaml
shared/                        the one source for lint.py, style_check.py and human-writing-rules.md
tools/                         sync_shared.py, validate.py, package.py
tests/                         run_tests.py, build_cases.py and the test cases
.claude-plugin/marketplace.json     Claude Code marketplace
.agents/plugins/marketplace.json    Codex and ChatGPT marketplace
```

Edit the shared scripts in `shared/`, never the copies inside a skill, then copy them out and run the checks:

```bash
python3 tools/sync_shared.py
```

```bash
python3 -I -B tests/run_tests.py
```

```bash
python3 tools/validate.py
```

[CONTRIBUTING.md](CONTRIBUTING.md) covers changes to skills and the release steps. [AGENTS.md](AGENTS.md) is the same material for coding agents working in this repository. [docs/architecture.md](docs/architecture.md) explains how the pieces fit, and [CHANGELOG.md](CHANGELOG.md) lists the releases.

## License

[MIT](LICENSE). Copyright 2026 Emmanuel Benami.
