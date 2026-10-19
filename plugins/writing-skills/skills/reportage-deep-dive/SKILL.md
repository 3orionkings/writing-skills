---
name: reportage-deep-dive
description: Write long reportage on how engineering and product work inside named companies: a blockquoted reader question or a paragraph of hard numbers, a bolded scope sentence and a numbered outline; how the material was gathered and from how many people; the author's own experience set against two or three named companies; one bold thesis sentence per section; charts captioned with a full sentence and a linked source; the caveat stated right after the data; a close of advice and related reading. Use it for deep dives, newsletter issues, industry analyses, "how X company does Y", cross-company comparisons, explainers that bridge engineering and product, and the short news-commentary variant; trigger on a deep dive, a newsletter issue, a reader survey, interviews with engineers, or "what I've seen at" companies. Not for: a literature deep dive on research papers (use taxonomy-explainer). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# Reportage deep dive

## What this form is for

Senior engineers, engineering managers and the product leaders who work with them read it because the method is on the page: how many people were interviewed, how long they were there, which survey the chart comes from. The author's own time at named companies is set against what others report, the comparison produces a model or a chart, and advice arrives last, framed as personal practice. A skimmer gets the argument from the captions alone.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies the form; the voice comes from the user's own draft or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather: the reader's question (or the paragraph of hard numbers that opens the piece); the scope in one bolded sentence; the numbered outline; the method with counts (how many people, how long they were there, which survey, how many responses, who did not reply); the author's first-hand experience at named companies; the two or three companies to compare; the chart or box diagram with its full-sentence caption and source; the caveat for each piece of data; the advice list written as direct suggestions; the related reading; and, only if the user supplies them, the teaser for the next part, the paywall point and the names of reviewers to thank. If you don't have interviews, survey data or first-hand experience from the user, write the evergreen guide instead or say how thin the sourcing is in the method paragraph; never invent interviewees, counts or quotes.

## The shape

Three registers. The evergreen guide of 1,000 to 2,000 words: a definition, then nine traits or twelve questions as headings, then tips, few images, sourcing limited to experience plus one quoted practitioner. The newsletter deep dive of 3,000 to 5,000 words with a methodology paragraph, survey data, named interviewees, numbered headings, a paywall point after section two or three if the user's publication has one, and a Part 1 and Part 2 split when the length needs it. The news commentary of 650 to 2,300 words: an italic series blurb, a line saying what the issue covers, four numbered topics with bold lead-ins, then the lead story told as a timeline reconstructed from a thread, a status page and a postmortem, image-heavy, short on caveats, closing on one dry line.

Opening. A reader's question in a blockquote, or one paragraph of hard numbers (growth since release; a reorg email and the headcount it moved). Then the bolded scope sentence, then the numbered outline with a pointer to the next part if the piece is split.

Body. Numbered headings march through the outline. The method paragraph sits by the second or third section: [how many current and former staff, and how long they were there]; anonymised survey answers linked as a spreadsheet; a request to the company that went unanswered. The narrative compares what the author saw (a first-person anecdote from a named company) with what interviewees and surveys report, across two or three named companies, then produces a model or a chart. Advice arrives last.

Close. An advice list written as direct suggestions, related reading, and thanks to reviewers and a teaser for the next issue only if the user supplies them. Every post carries a footer with the original date and the last update. Short pieces close on one dry line.

## The moves

Tell the reader how the material was gathered before using it. State the caveat in plain words right after the data (the survey is not representative; pull requests per engineer is an imperfect metric; one bad interview may be luck), then conclude anyway. Label deductions as deductions. Drop a mid-piece update when a postmortem lands. Attribute company-supplied figures to the company. Generalise from thin samples only with the thinness stated.

## Language

Sentences of 15 to 25 words with short fragments for punch; paragraphs of one to four sentences. Professional and conversational, with insider abbreviations (TPM, IC, SEV, Staff+) explained on first use and plain idioms. First person carries the evidence: the author joined a company, took the opposite approach as a manager, strongly believes. Bold marks one thesis sentence per section and the lead-in of every bullet. In the commentary register, opinion comes through understatement and rhetorical questions rather than "I think". Humour is light and aimed at institutions. Typos survive to publication.

## Figures

Deep dives carry two or three: survey bar charts and plain box diagrams of team structures, each with a full-sentence italic caption stating the finding. Commentary pieces are image-heavy (fifteen to twenty), mostly screenshots and memes placed as evidence at points on the timeline, with bold-italic captions ending in a linked source. Nothing hand-drawn; default charts and boxes. The caption is a sentence of the argument and the picture is its exhibit. If the chart does not exist yet, write the image line with its full-sentence caption and a placeholder file name, so the caption carries the argument now and the chart can be made from the user's data later.

## Departures from the humanizer

Two of this form's moves are on the humanizer's list. Short fragments for punch: the deep dive allows one after a run of data (a five-word verdict on the chart), never as a reveal or a hinge. Rhetorical questions: the commentary register carries opinion through understatement and the odd rhetorical question rather than "I think". Keep both rare; the linter reports them as soft findings, and those can stay where the form puts them. Everything else in the humanizer applies, including the dash rule.

## What makes an imitation fail

Being too polished (no typos, no admitted thin samples) or too jokey (mistaking dry understatement for comedy). Skipping the method paragraph and the numbered outline, which are the most recognisable parts. Decorative hand-drawn diagrams. Forgetting the mechanics (the published and updated footer, and the two-part split when the piece is long enough to need one). Generic management advice instead of every claim anchored to a named company and a year.

## Workflow

1. Write the opening (reader question or hard numbers), the bolded scope sentence and the numbered outline before any research is written up.
2. Open every source before citing it: each survey, postmortem, status page, filing and interview note. Record the exact figure and where it appears, attribute company-supplied figures to the company, and mark anything you could not open or confirm as [unverified]; it stays out of the finished piece until the user confirms it.
3. Write the method paragraph with counts. If the counts are not known, ask for them or say so in the paragraph.
4. Draft the sections in outline order: first-hand anecdote, what others report, comparison, model or chart with a full-sentence caption and source, caveat, conclusion.
5. Write the advice list as direct suggestions, then related reading, and thanks and a teaser if the user supplied them.
6. Save to a file and run `python3 scripts/style_check.py draft.md` for the deep dive, or add `--variant evergreen-guide` or `--variant commentary` for those registers (length, numbered outline near the top, method sentence with counts, bold thesis per section, full-sentence captions, no summarising close), and `python3 scripts/lint.py draft.md --allow-markdown`. Fix every failure and every hard lint finding.
7. Return the piece only.

## Skeleton

```
# [Title]

> [Reader's question.]   or   [One paragraph of hard numbers.]

**[Scope sentence: who this is for and what it covers.]**

1. [Section]
2. [Section]
3. [Section] (Part 2 covers 4 to 6)

## 1. [Section]
[First-hand anecdote at a named company. **The thesis sentence of the section.**]

## 2. [Section]
[Method: how many people, how long, which survey, who did not reply.]
![The chart's finding stated as a full sentence. Source: linked.](chart.png)
[The caveat. The conclusion anyway.]

## 3. [Section]
[Comparison across two or three named companies. Model or diagram with a full-sentence caption.]

## Advice
**[Direct suggestion.]** [One or two sentences.]
**[Direct suggestion.]** ...

[Related reading. Thanks and a teaser, if the user supplied them.]
[Published DATE. Updated DATE.]
```
