---
name: taxonomy-explainer
description: Write a research explainer in the form of learning notes: the term defined in the first sentence, the scope narrowed in the first paragraph with what is left out, a taxonomy used as the heading tree, and each method written as a bold name, a linked author-year citation, the mechanism in the author's own notation, one number, one caveat and the paper's figure linked or described with its credit; it closes on open questions, a citation block and references. Use it for technical explainers of a research area (machine learning, AI safety, systems, any literature with papers), literature-driven deep dives, "what is X and how does it work" pieces, survey notes and derivation walkthroughs; trigger on papers, a literature, a taxonomy, a survey, or citing by author and year. Not for: reporting on how companies work (use reportage-deep-dive) or a practitioner's patterns guide (use patterns-survey). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# Taxonomy explainer

## What this form is for

Researchers, engineers and technical product people who want the map of a research area and the papers placed on it. The notes define the term, choose a framework to sort the literature, and put each paper in one cell with its mechanism restated, its number, its caveat and its own figure. Opinion lives in a few marked spots; the exposition is in "we". Nothing basic is defined, which is why capable readers from other fields also read it: they are given the map and trusted with it.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies the form; the voice comes from the user's own draft or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather: the one-sentence definition; the scope and what it excludes, with the reason (a full survey would be too long; a neighbouring topic is left for later); the taxonomy (two to four levels) that will become the heading tree; for each method a bold name, an author-year citation linked to the paper, the mechanism in the author's own notation, one quantitative result, one caveat about what the result does not show, and the paper's figure, linked or described with its credit (reproduced only if the user has the rights to it); the symbol table if there are derivations; the pairs of disagreeing papers and the conditions that produce the gap; the open questions; the one or two marked opinions; the citation block and references.

## The shape

Two styles. The survey, 5,000 to 9,000 words, wide and taxonomic, many figures, little derivation. The single-idea post, which goes deep on one line of work, defines every symbol, derives, and allows more opinion.

Opening. Sentence one is the definition. Paragraph one narrows the scope and says what is excluded and why, or names the gap the post fills (past work has been theoretical; mitigation is under-studied). When the idea has a history ([an early paper], [a later essay]), tell it right after the definition. Then a linked table of contents.

Body. The heading tree is the taxonomy (causes, detection, mitigation; three numbered components, case studies, challenges). Methods are ordered by idea, not date, and each section opens with one sentence saying what it covers. The method paragraph runs: bold name, linked citation, mechanism in own notation, one number, one caveat, one figure linked or described with its credit. A symbol table sits up front where there are equations; pipeline stages are numbered. Derivations step through with one connective sentence between equations. Comparisons are made in prose, not tables; disagreeing papers sit side by side with the conditions that produce the gap, and a side is taken only when the evidence allows.

Close. Open problems where warranted, a citation block, then a numbered reference list that is never cited by number in the text. Revised posts carry bracketed, dated update notes at the top. Never a summary.

## The moves

Evidence is the papers' own equations and figures: equations restated in the author's notation, figures linked or described with a credit, and reproduced only when the user has the rights to them. The author says what a result does not show ([what the result does not establish]; [a limit of the study's setup]). Framing choices are stated with reasons. Hedges are short and specific (it is unclear why these laws take exactly this form; the direction is interesting but the evidence provisional). Opinion appears in a few marked spots per post: a bracketed personal take, a call for a kind of research, a two-step prediction. Thanks to collaborators go in the body, only if the user supplies them.

## Language

Sentences of 20 to 30 words with parenthetical citations and qualifiers, broken by short declaratives. Paragraphs of two to four sentences. Textbook prose with the odd plain word (a cool concept; a demo is fun). "I" appears a handful of times per post, only for scoping, opinion or thanks; "we" and "let's" carry the exposition. Key terms bold at first mention. Inline and display math wherever a method has a formula. Typos and the one informal word per section are left; they mark the text as notes rather than a paper.

## Figures

Many per survey, nearly all from the cited papers: link to each figure or describe its finding in an italic full-sentence caption with a source credit, and reproduce the image only when the user has the rights to it. One or two per post are the author's own framework diagrams. An interactive toy simulation where a law can be played with.

## What makes an imitation fail

Opening on why the topic is exciting instead of a definition. Summarising at the end instead of listing questions. Comparing in tables instead of prose. Drawing its own diagrams instead of linking or describing the paper's figure with its credit. Hedging everything softly instead of once and specifically. Citing by bracketed number instead of linked author and year. Writing "I" throughout instead of "we". Polishing away the typos and the informal word that mark the notes as notes.

## Workflow

1. Write the definition sentence and the scope paragraph, including the exclusion and its reason.
2. Build the taxonomy and lay it out as the heading tree before reading for the body.
3. Open every source before citing it. For each paper, record the exact number, the conditions it holds under, and where it appears (section, table or figure number). Mark anything you could not open or confirm as [unverified] and keep it out of the finished notes until the user confirms it.
4. For each method, fill the fixed paragraph (name, citation, mechanism, number, caveat, figure). A method with no number or no caveat is not finished.
5. Place disagreeing papers side by side and write the conditions that explain the gap.
6. Write the open questions, the citation block and the references.
7. Save to a file and run `python3 scripts/style_check.py draft.md` (length, heading count, first-sentence definition, full-sentence captions on any figures, references section, open-questions close, first-person rate; one spec covers both styles) and `python3 scripts/lint.py draft.md --allow-markdown`. Fix every failure and every hard lint finding.
8. Return the notes only.

## Skeleton

```
# [Topic]

[Updated on DATE: bracketed note, if revised.]

[Sentence one: the definition. The scope, what is left out and why. The gap this fills.]

[Table of contents.]

## [Top-level taxonomy branch]
[One sentence saying what this section covers.]
### [Sub-branch]
**[Method name]** ([Author et al. YEAR], linked) [mechanism in own notation]. [One number.] [One caveat.]
![Fig. N. Full-sentence caption stating the finding. (Image source: Author et al. YEAR)](figure.png)
[Without rights to the image: a link to the figure and one sentence stating its finding.]

## Open problems
[Questions, as a list.]

## Citation
[Citation block.]

## References
[Numbered list, never cited by number in the text.]
```
