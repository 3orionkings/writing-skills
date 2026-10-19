---
name: strategy-pattern-essay
description: Write a strategy or organisational-mechanics essay that opens on a one-sentence law about companies or a concrete anomaly, reaches a named framework within three paragraphs, coins a two-word label for the mechanism and uses it as a heading, isolates one variable between two similar companies, converts the story into cost or incentive terms, puts the concession and the rival explanation in their own paragraphs, and ends the body on one aphoristic line. Use it for "why X wins" pieces, company and market analyses, essays on loops, network effects, bundling, pricing or org design, investor memos, and competitive briefs written as argument; trigger on strategy, moats, loops, incentives, a company case, or "how X made its market". Not for: a policy or position argument built on objections (use mechanism-essay) or an engineering essay proved by measurements (use technical-principles-essay). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# Strategy pattern essay

## What this form is for

Founders, operators and investors who already know what a network effect is and want a tool they can carry to the next company. The essay names a mechanism with a two-word label, traces the loop on one case, isolates the variable that explains the outcome, and keeps the jokes in the captions so six thousand words of strategy stay readable. Confidence sits in the claims; doubt sits in its own paragraphs.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies the form; the voice comes from the user's own draft or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather: the law or the anomaly that opens the piece; the two-word label for the mechanism; the redefinition of the market that is larger than the incumbent's; the loop traced step by step; the two companies that differ in one variable; the story converted into economic structure (fixed cost to variable cost, bundle to abstraction, acquihire to licence); the concession; the simplest rival explanation; what cannot be known from outside; the implications stated separately for founders, employees and investors if they differ; the one-line close; the jokes that go in captions, bracketed notes and endnotes; promised future essays and thanks only if the user supplies them.

## The shape

Three formats. The long essay of 5,000 to 6,000 words with up to twenty images, appendices and acknowledgements. The memo piece of 2,500 to 4,500 words that says up front it is an edited private memo, with an italic preface, a bold thesis sentence, loop diagrams and repeated admissions of what internal data would be needed. The late essay of 1,900 to 3,300 words: thesis in the first paragraph, one to four images, two-word headings, numbered endnotes.

Opening. Either a one-sentence law about companies, or a concrete anomaly (an under-rated founder, a strange deal), then the framework within three paragraphs. Two italic lines may preview the claims; a disclaimer follows if the author has a position.

Body. Subsection headings are reusable concept labels rather than topics. The argument moves from a redefinition ([the activity] is the whole process, so the tool is for [the larger group]) to the loop that creates value, to the sales motion, to platform choices. The framework is tested on three or four companies and then extended. One two-axis chart may do analytic work. When a term is coined, the name is defended on three grounds and the implications are stated separately for each kind of reader.

Close. One aphoristic line on tech history or on what the product really is, then jokes, and thanks if the user supplied them, in italics or endnotes. A method paragraph may precede it: compressing a company to a few primitives is lossy and often post hoc, the author's own included, which is why founders should do it themselves.

## The moves

Reason by isolating one variable between similar companies; by converting a story into cost or incentive structure and then asking who else the conversion applies to; by historical parallel; and above all by naming the pattern so it carries. Take the common complaint seriously (the tool is distracting) and relocate the cause (immature process). Concede diminishing returns. Offer the rival explanation in its own paragraph (timing as the simplest alternative). Say what cannot be known without internal data. Close by granting luck or saying the test is still ahead.

## Language

The constant unit: a short declarative sentence that names a mechanism, two or three longer sentences that run it forward in time, then a one-line paragraph that lands it. Paragraphs of two to five sentences in the long form, one to three in the late form. First person thin: what the author uses, teaches, where they worked. Italics stress single words; bold marks the one thesis sentence. No rhetorical questions and no dashes in the late form. Humour stays out of the body and lives in captions, headings, bracketed italic notes and footnotes.

## Figures

Loops and two-axis charts, mnemonic rather than evidential, with joke captions in the long essays. A struck-through disclosure where the author holds a position.

## Departures from the humanizer

The early long essays and memos in this form use dashes and the late form does not. This skill follows the humanizer: no dashes, unless the user's own writing uses them, and then at the author's rate (lint with `--author-sample`). The form also prescribes threes: a coined name defended on three grounds, and implications stated for founders, employees and investors. Those are three real things, so the linter's soft triad finding on them can stay; do not add a third item anywhere else for rhythm. Everything else in the humanizer applies.

## What makes an imitation fail

Keeping the vocabulary of loops and compounding while dropping the mechanism, so the loop is asserted rather than traced. Jokes in the body. Explaining basics. Hedging inside the claim rather than in a separate paragraph, which drains the declarative rhythm. Piling up examples that prove the same point instead of one comparison that isolates a variable. Skipping the self-critical method paragraph. Ending on a summary.

## Workflow

1. Write the law or the anomaly and the two-word label. If the label cannot be a heading, it is not yet a concept.
2. Trace the loop in numbered steps in your notes; then write it as prose.
3. Pick the two companies that differ in one variable and write that comparison before any other example.
4. Write the concession paragraph and the rival explanation paragraph as separate paragraphs.
5. Draft the body, then the one-line close, then move every joke and aside into captions, notes or endnotes.
6. Save to a file and run `python3 scripts/style_check.py draft.md` (length, short concept headings, bold thesis, an objection or rival explanation present, no summarising close; one spec covers all three formats) and `python3 scripts/lint.py draft.md --allow-markdown`. Fix every failure and every hard lint finding.
7. Return the essay only.

## Skeleton

```
# [Title that names the company or the mechanism]

*[Two italic lines previewing the claims. Disclaimer if any.]*

[Para 1: the law, or the anomaly.]
[Para 2 to 3: the framework. **The thesis sentence in bold.**]

## [Two-word concept label]
[Mechanism sentence. Two or three sentences running it forward. One-line landing.]

## [Two-word concept label]
[The comparison: two companies, one variable.]

## [Two-word concept label]
[The conversion into cost or incentive terms. Who else it applies to.]

[Concession, its own paragraph.]
[Rival explanation, its own paragraph. What cannot be known from outside.]

[Implications for founders. For employees. For investors.]

[One aphoristic line.]

*[A joke. Thanks and promised essays, if the user supplied them.]*
[Endnotes.]
```
