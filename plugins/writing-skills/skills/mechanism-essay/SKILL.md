---
name: mechanism-essay
description: Write a long-form position piece that defines its terms, teaches the mechanism before stating the conclusion, examines the strongest objection on purpose, and says what follows if the premise holds. Use this skill whenever the user asks for an essay, a position piece, a policy post, a long argument, a manifesto, a "why I think X" piece, a letter to policymakers or regulators, a thought-leadership piece, or anything over 2,000 words meant to persuade a serious reader; also when they ask to "make the case for", "lay out my thinking on", or "write up my view on" a contested question. Trigger even when the word essay never appears. Not for: company or market strategy (use strategy-pattern-essay), an engineering argument proved by measurements (use technical-principles-essay), or a short personal note (use thesis-first-note). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# Mechanism essay

## What this form is for

A serious reader (a policymaker, a researcher, a technology leader, an educated generalist) will give you ten to twenty thousand words if you earn them in the first three paragraphs. This form earns them by saying exactly what it is about and what it is not, defining its terms before using them, and building the mechanism that produces the conclusion so the reader arrives at it themselves. The conclusion is a consequence, never an announcement.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies structure and moves, not a personality; the voice comes from the user's own drafts or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather, before any drafting: the precise claim; the two extreme positions it sits between; the key terms and their definitions; the limiting factors or assumptions the argument rests on; the mechanism, taught first as a labelled hypothetical in round numbers; the live case the mechanism applies to; the author's own experiments, cases or data (these are the evidence of choice); the strongest objection; the bet the author is willing to state (a range, a year, a probability); and the obligation the analysis converts into. If any of these is missing, ask for it or mark the gap in one line rather than inventing it. If you don't have experiments, cases or data from the user, argue from the mechanism and from published evidence the user can point to, say plainly that the piece rests on reasoning rather than first-hand results, and never imply first-hand evidence.

## The shape

Choose the tier. The post runs 2,000 to 5,500 words, sectioned and footnoted. The essay runs 10,000 to 15,000 words with numbered sections, 25 to 40 footnotes, and acknowledgements only if the user supplies them. The programme variant (a piece that proposes a course of action) opens on a story and closes on a duty, carries few footnotes, and moves its sourcing to inline links.

Opening (two to three paragraphs). State the thesis in bold. Say in the same breath what the piece will not argue, why it is being written now, and that parts of it may be wrong. If the author has been misread, correct the reading first. Then a framework section: define the key term (quote the author's own earlier definition if one exists) and list the limiting factors before any claim is made.

Map. Give a numbered plan of the sections and follow it exactly. In the essay tier, each domain or risk gets its own numbered section with the same inner sequence: the state of the field, the bottleneck, the sceptic's objection, the mechanism applied, an estimate with its limit, what becomes possible, what it does not solve. Treating every section with the same question order is what lets a reader skip and still trust the piece.

Body moves, in order within a section. Teach the mechanism with a hypothetical before applying it to the real case, and label it as one in the sentence that introduces it ("suppose a budget of [X] buys this share of the work, and ten times [X] buys that share"). Its round numbers are illustrations, not findings: never carry them into a claim about the real case, and never present them as data. Name the two extreme positions on the question, reject both, and place the author between them with a stated bet. Use the author's own experiments or cases as evidence. Run a second-person thought experiment where the reader holds the decision (suppose you were the official who had to decide). Then list objections as First, Second, Third and answer each, conceding where the answer is thin; flag the strongest objection yourself, even if nobody has raised it.

Close. Return to the stakes set out at the opening and convert the analysis into an obligation in one short sentence, often bolded. Never summarise the sections. The essay tier may end on an image or a line borrowed from literature; the programme tier ends on a duty.

Footnotes carry the caveats, the corrections of the author's past statements, the technical qualifications, the brainstorm that did not fit, and the one joke per essay. The body keeps a straight face.

## The moves

Reasoning is first principles from mechanism, with explicit probability language and conditionals. Uncertainty is given as a range, a bet or an if-then, never as hedging adverbs sprinkled through sentences. Concede once, in a sentence that begins "To be clear" or in a footnote, and then argue with confidence. Separate what the author knows from inside their own work from what they are inferring, and say which is which. Where a rival's figure is suspect, take it at face value and show the argument survives anyway. If the author's own past statement was wrong, correct it in a footnote rather than hiding it.

Research findings enter at the point where the argument needs them, placed exactly there, never gathered into a literature section. A finding that does no work in the argument is cut.

## Language

Long, carefully subordinated sentences with a short declarative landing each move. Singular "I" carries judgement; "we" carries the organisation or humanity. Italics stress one word in a paragraph; bold marks the thesis and the lead-in of a forecast list. Rhetorical questions may open a section. Exclamation marks never appear. Technical terms are defined at first use. Plain words beat slogans; "for example" beats "e.g."

## Figures

None. The argument lives in prose, numbers in sentences, and footnotes. A table or chart in this form signals a different genre.

## Departures from the humanizer

A section may open on a rhetorical question that the section then answers at length. The humanizer rules out a short question the writer answers at once ("The result? ..."); a section opener answered over several paragraphs is this form's move, and the linter's soft finding on it can stay. Use one per section at most, and never as a one-line hinge. Everything else in the humanizer applies, including the dash rule.

## What makes an imitation fail

Copying the urgency and skipping the framework section, so claims float with no stated limiting factors. Asserting the middle position without naming the extremes it sits between. Citing other people's research where the author should cite their own cases. Hedging inside every sentence instead of conceding once. Letting the joke into the body. Forgetting the bet. Shortening the sentences until the voice is gone. Ending on a summary rather than a duty.

## Workflow

1. Collect the inputs listed under Before writing. Write the map before any section.
2. Draft the opening and the framework section first and read them as a sceptic would: is the claim precise, are the terms defined, is the exclusion stated?
3. Draft the sections in map order, each through the same question sequence. Write the objection list last within each section.
4. Draft the close from the opening, not from the sections.
5. Save to a file and run `python3 scripts/style_check.py draft.md` (length, bold thesis early, numbered map, an objection present, no summarising close, no figures or tables; one spec covers all three tiers, so no --variant is needed) and `python3 scripts/lint.py draft.md --allow-markdown` (machine-writing tells). Fix every failure and every hard lint finding.
6. Return the piece only. No preamble, no change log.

## Skeleton

```
# [Title that states the claim]

[Para 1: thesis in bold; what this piece will not argue; why now.]
[Para 2: what may be wrong here; how the author has been misread, if relevant.]

## 1. Framework
[Definition of the key term. The limiting factors, numbered or listed in prose.]

## 2. [First domain or risk]
[State of play. The bottleneck. The sceptic's objection. The mechanism as a labelled hypothetical in round numbers. The estimate and its limit. What becomes possible. What it does not solve.]

## 3. [Second domain or risk] ... same sequence

## N. Objections
[First, ... Second, ... Third, ... each answered or conceded. The strongest one named as such.]

## N+1. What follows
[The bet. The obligation, in one short bolded sentence.]

[Footnotes: caveats, corrections, qualifications, the joke.]
```
