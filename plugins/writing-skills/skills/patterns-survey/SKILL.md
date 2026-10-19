---
name: patterns-survey
description: Write a long technical survey or a practice essay that engineers, product managers and scientists can all read: definition first, why before how, headings of the form thing colon purpose with question sub-headings beneath, bold lead-in sentences explained in two or three plain lines, a named paper and a counted experience behind every claim, the trade-off in the same sentence as the recommendation, and a close of questions, references and a citation block. Use it for "patterns for X", "fundamentals of X", "lessons from building X", applied-ML and LLM-product write-ups, evaluation and prompting guides, and shorter practice essays for technical individual contributors, even when the user says "blog post" or "guide". Not for: a how-to built on one client and its artefacts (use field-guide) or a map of a research literature (use taxonomy-explainer). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# Patterns survey

## What this form is for

A survey that a product manager can follow and an engineer can act on, because every section opens with a definition, why comes before how, jargon gets an aside, and each claim carries a paper and a number from the author's own production work. The reader can skim by the template and trust what they skip.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies the form; the voice comes from the user's own draft or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather: the problem in one paragraph; the items (patterns, techniques, lessons) with a four-word purpose each; for each item a named paper or industry write-up (bolded, linked, followed by a verb), a production example, a number (latency, cost, sample size, a before-and-after percentage), and the trade-off in a clause; the author's counted experience ([N] samples, [N] requests, [N] past conversations); the aside that tells the reader what to do first (build an evaluation set of [N] labelled examples); reader contributions and dated updates, only if the user supplies them; the two questions, references and citation block for the end. If you don't have counted experience from the user, say the piece surveys published work, drop the production opinions, and never supply a count.

## The shape

Two registers, one voice. The technical survey of 4,000 to 17,000 words, and the practice or career essay of 800 to 4,000.

Survey opening, under 100 words: a borrowed blockquote or a definition, one sentence announcing the items, and a linked list of sections giving each a four-word purpose. Each item is a heading of the form thing, colon, purpose, with three question sub-headings beneath it: why it, more about it, how to apply it. The why part surveys papers in rough date order, each name bolded and linked and followed by a verb. The how part is a run of bold lead-in sentences, each explained in two or three plain sentences with a production opinion. Figures are the papers' own: link to each or describe its finding in a sourced caption, and reproduce the image only if the user has the rights to it. No tables, code or footnotes in the survey; code blocks live in the how-to pieces (prompts, config files, pseudocode).

Essay opening: a claim in one sentence, or a scene (a planning meeting where the simpler proposal lost; rejected papers and denied promotions), then a blockquote from someone worth borrowing. Headings are questions or imperatives; each section is a claim, the mechanism, an example or a code block, and a soft caveat. Benefits or reasons run as bold lead-ins starting First, Second.

Close. Eight short sentences at most: a two-by-two placing the items, two questions, then references and a citation block. Reader quotes and dated update blocks are appended unanswered, only if the user supplies them. Never a summarising conclusion.

## The moves

Reasoning moves from paper to industry example to the author's own production experience, with a number whenever one exists and the trade-off in the same sentence as the recommendation (a little accuracy for a large speed-up). Arithmetic is done in the open ([N] samples at [an X percent] defect rate is inconclusive; [2N] clears the bar). The hedge goes in a heading ("what doesn't seem to matter") or in an aside, not in every sentence. The chain of thought is candour rather than narrated revision: say what was unwieldy, disclaim what the author is not, admit a first draft overfits, and link the earlier post (where the user supplies one) rather than explaining how the view changed.

## Language

Sentences of 15 to 30 words with short declaratives for emphasis; paragraphs of two to five sentences; contractions throughout; "we" for the reader's actions and "I" for opinion. Heavy bold, rare italics, bullets over numbered lists. Jargon is used and then defined in parentheses or an aside. Humour is dry and parenthetical. Titles are descriptive and often carry a colon.

## Figures

About one figure per item in the survey, each linked or described in a caption that states the finding and credits the source; reproduce the image only if the user has the rights to it. A single illustrative figure in the essays. A two-by-two or a simple diagram when the items need placing against each other.

## What makes an imitation fail

Topic nouns where the form uses question headings. Losing the why-before-how order. Citing with years and et al. where the form bolds names. Hedging every sentence where the form hedges once in a heading. Inventing experience where the form counts it. Broad humour. A summarising conclusion. Omitting the references and citation block, which are where a post stops reading like a generic blog.

## Workflow

1. Write the one-paragraph problem and the linked list of items with four-word purposes. If an item has no paper or no number, it is not ready.
2. Open every source before citing it. For each paper or write-up, record the exact figure and where it appears (section, table or figure number). Mark anything you could not open or confirm as [unverified] and keep it out of the finished piece until the user confirms it.
3. Draft each item through the same three questions in the same order.
4. Write the bold lead-ins of the how parts before their explanations, so each is a complete instruction on its own.
5. Draft the close: two-by-two, two questions, references, citation block.
6. Save to a file and run `python3 scripts/style_check.py draft.md` for the survey, or add `--variant essay` for the practice essay (length, question headings, bold lead-ins, numbers, links, references section, no summarising close), and `python3 scripts/lint.py draft.md --allow-markdown`. Fix every failure and every hard lint finding.
7. Return the piece only.

## Skeleton

```
# [Descriptive title: what it covers]

> [Borrowed blockquote.]
[One sentence announcing N items.]
- [Item 1: four-word purpose](#item-1)
- [Item 2: four-word purpose](#item-2)

## [Item 1]: [purpose]
### Why [item 1]?
[The problem it solves.]
### More about [item 1]
[**Paper name** (linked) shows ... **Paper name** finds ... in date order, each with a sourced figure.]
### How to apply [item 1]
**[Lead-in instruction.]** [Two or three plain sentences with a production opinion and a number. Trade-off in the same sentence.]

## [Item 2]: [purpose] ... same sequence

## Conclusion
[Eight sentences at most. The two-by-two. Two questions.]

## References
[Numbered list.]

## Citation
[Citation block.]
```
