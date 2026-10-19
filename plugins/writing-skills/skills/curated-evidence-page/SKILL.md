---
name: curated-evidence-page
description: Build a curated knowledge page where the list is the argument, with one framing sentence, then dated and sourced entries with the number computed for the reader, one counterexample left unexplained, a note of what is excluded, and a request for additions. Use this skill for evidence lists (examples of X happening fast, studies with effect sizes), lists of open questions, reading lists and canons, "best examples of", "a page collecting", "a running list of", research notebooks kept in public, and any page meant to be returned to and extended rather than read once; the dated first-person dispatch is a variant inside it. Trigger even when the user says "post" or "doc" rather than "page". Not for: a survey that explains patterns from papers (use patterns-survey) or reporting built on interviews (use reportage-deep-dive). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# Curated evidence page

## What this form is for

Founders, researchers and policy people who want the primary source, not the summary. The page states in one sentence what the list is and why it exists, and then gets out of the way: entries carry a name, a number, a date and a link, and the selection does the arguing. The reader supplies the conclusion. A page like this is kept rather than published once, so it marks its own incompleteness and asks for more.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies the form; the voice comes from the user's own draft or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather: the frame in one or two sentences (what the list is, why it exists); the entries, each with a name, a one-to-three-sentence fact, a number computed for the reader (elapsed days, effect size, cost per unit), a date, and a link to a primary or near-primary source (an oral history, an institutional history, a paper, a contemporary account); one counterexample; the conventional explanation the list quietly rebuts; what the page excludes; the works that offer hypotheses, none endorsed; a line asking for additions, with the author's email only if the user supplies it.

## The shape

Four shapes. The evidence list: a framing line, then twenty to forty entries, each a bold name, one to three sentences of fact, and an italic source line, ordered loosely by time or theme and never sorted too neatly. The question list: twenty-odd questions, each a plain headline (why is X so constant) and a body giving the evidence that makes it hard, several disposing of the obvious answer in a sentence. The reading list: titles with a one-line description and a link, marked nascent or first cut, naming what it leaves out. The dispatch: a dated first-person post of 300 to 2,000 words, linked to where it was first posted, with heavy specific hedging and firm judgements, ending on a question or an invitation.

Opening. One or two plain sentences. No thesis paragraph.

Entries. Forty to eighty words each. A bold project or study name, then the facts: start, finish, elapsed time or effect size, who was responsible, then the italic source line. The few adjectives sit inside quotations. Compute the number the reader would otherwise have to compute ([N] days from start to finish; [N] times the cost per unit).

The counterexample. One paragraph that sets a slow or failed case against the fast ones, with its own numbers, and does not say what the contrast means.

Close. A request for more entries, with sources, and a line of works offering hypotheses. For a question list, the last entry admits what its chart overstates. For a reading list, a line marking it in progress. Never a conclusion.

## The moves

Reasoning is enumeration, implied rebuttal of a received belief, and the question as a thesis in disguise. Name the conventional explanation and dispose of it with a single fact (that country is not simply rich, since its income per head trails). Uncertainty is stated exactly where it exists and nowhere else: nascent, first cut, in progress, "as far as I can tell". Reader contributions and responses appear only if the user supplies them: contributions appended with credit, responses noted in italics beside the question.

In the dispatch variant, state the lack of expertise in the first line, make the judgement anyway, and close by asking for arguments from people who know.

## Language

Plain and short, often no verb beyond the fact. No adjectives in the entries; evaluative words (definitive, best) only in reading-list descriptions. Precision in days, dollar figures, dates and the names of the people responsible. First person confined to the frame and the close, except in dispatches, where it carries the piece. No humour, no flourish. The link and the date are the devices.

## What makes an imitation fail

An adjective on every entry, so the examples stop speaking for themselves. A paragraph that explains what the list proves. Round numbers where the source gives an exact figure. Dropped source lines, or links to summaries instead of the oral history. Hedging throughout instead of one precise caveat. Alphabetical sorting that loses the notebook feel. Answering the questions. Padding with weak examples; the selection is the argument. A closing lesson.

## Workflow

1. Write the frame sentence. If it needs a second paragraph, the list is not yet one list.
2. Open every source before citing it. For each entry, record the exact figure and date and where in the source they appear (page, section, table or timestamp). Mark anything you could not open or confirm as [unverified] and keep it out of the finished page until the user confirms it.
3. Draft the entries from those notes, computing the number for each. Cut any entry without a source or without a number.
4. Order loosely by time or theme. Add the one counterexample.
5. Add the exclusions line, the request for additions and the hypotheses line.
6. Save to a file and run `python3 scripts/style_check.py draft.md` for the evidence list, or add `--variant question-list`, `--variant reading-list` or `--variant dispatch` for the other shapes (frame length, every entry with a link and a number, no summarising close, a close that asks for more; adjectives are checked by eye), and `python3 scripts/lint.py draft.md --allow-markdown`. Fix every failure and every hard lint finding.
7. Return the page only.

## Skeleton

```
# [Page title, one to three words]

[One or two sentences: what this is and why it exists.]

**[Entry name].** [What was built or found, who led it, start and finish, elapsed days or effect size.]
*[Source: title of the primary account, linked.]*

**[Entry name].** ...

[The counterexample, with its numbers. No comment on what it means.]

[What this page leaves out. Works offering hypotheses, none endorsed.]

[Request for additions, with sources. Email link.]
```
