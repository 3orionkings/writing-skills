---
name: principle-column
description: Write a short opinion column that names a trend the reader has already noticed, grants it, flips it in one short sentence, defines a principle in two plain sentences, concedes that many reject it, and closes on an assertion plus one hedge. Use this skill for product-management and leadership columns, newsletter opinion pieces, "my take on X" posts, principle explainers, and any 600 to 1,700 word piece for executives and practitioners deciding how to organise; also when the user asks for "a column", "a short opinion piece", "a hot take that still holds up", or "explain the principle behind X". Trigger even when the word column never appears. Not for: a one-rule post under an imperative title (use one-idea-post) or a reflective note built on a craft analogy (use thesis-first-note). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# Principle column

## What this form is for

A reader who runs a team or a company has noticed a trend and half-believes the lazy reading of it. This form grants that the trend is real, then reframes it in one sentence, names the principle underneath, and tells the reader what to do about it, all in an unbroken column they can read in four minutes. Authority comes from decades of observation stated plainly, not from data.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies the column's shape; the voice comes from the user's own draft or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather: the trend as the reader would phrase it; the short sentence that flips it; the principle, in two plain sentences, with a source if it is borrowed; the reason many organisations reject the principle; the author's own history with the idea (what they used to think, when they changed their mind); one outside voice worth one line; two to six of the author's own earlier pieces to link; the assertion the column ends on and the hedge that follows it. If you don't have earlier pieces from the user, leave the links out: the column stands on the author's stated experience and the one borrowed source.

## The shape

Length 600 to 1,700 words. No subheadings, no numbered points, no images, no bullets. Nineteen to thirty paragraphs, most of them a single long sentence of 30 to 60 words, with a six to nine word verdict paragraph every four or five paragraphs. Italics on the one or two terms the argument turns on ([one term] against [its opposite]). The column is one unbroken column; a heading breaks it at once.

Opening. Either the trend everyone has seen, granted as real in the first sentence and called temporary in a short paragraph under fifteen words, or a personal anchor: how the author was first taught the idea, a question they cannot shake, a hedged guess.

Movement. Reframe-driven. The surface symptom is dismissed and the real cause named (usually a model of working, not a person). The principle is defined in two sentences and at once followed by the concession that many organisations reject it, with the reason. One outside voice is quoted in a single line and mapped onto the column's own vocabulary. The column then turns: what follows once the cause is named, what the opposing camp will say (put in a subordinate clause and answered in the main clause), and what the reader should do.

Close. Assert the view in one sentence, then hedge it once as a prediction the author is willing to risk, or restate the stakes. Never summarise.

The one exception to the no-headings rule: a confessional list of the author's own mistakes may run as ten numbered bold headings, because each confession is its own item. Use it only for that.

## The moves

A principle stated, justified by observation over years, contrasted with the common corporate mistake. Objections get one clause and are answered in the next. Concessions are explicit and short. The chain of thought shows as biography: what the author used to think, when they changed their mind, what their earlier work underestimated. Evidence is experience plus links to the author's own earlier pieces (two to six of them, where the user supplies them); no case studies, no numbers, no named companies in the body beyond the one linked source. The borrowed quotation is one line and attributed by name.

## Language

First person, plain, mildly impatient, with understated dry humour (an image rather than a joke). Second person sparing and conditional. The vocabulary is the author's own set of terms used consistently; define a term once with italics and then use it without apology. Sentences stack clauses in a spoken rhythm; the verdicts break it.

## The coaching variant

A related form for the reader who is alone with a problem rather than organising a team: sectioned and scannable, 1,000 to 3,000 words, numbered headings, an analogy from outside the field (a musician's instrument, an athlete's gear), a quoted outsider, a photo or a comic, coaching questions the reader answers for themselves, overt self-deprecating humour, warm constant second person, and two-word closing sentences. Choose it only when the user asks for a coaching piece; blending it with the column produces something that reads as neither.

## What makes an imitation fail

Adding subheadings and bullets. Chopping the long sentences into tidy medium ones, which loses the spoken rhythm and the contrast with the verdicts. Hedging in every sentence instead of once at the close. Inventing data or case studies. Naming companies and people in the body. Making the humour jokey. Ending with a summary.

## Workflow

1. Write the trend sentence and the flip sentence first; if the flip takes more than fifteen words, the reframe is not sharp enough yet.
2. Write the principle in two sentences and the concession in one. Then the biography paragraph.
3. Draft the column straight through, one idea per paragraph, and insert a verdict paragraph wherever four long paragraphs have run.
4. Add the one outside voice and the links to earlier pieces.
5. Save to a file and run `python3 scripts/style_check.py draft.md` for the column, or add `--variant confessional-list` or `--variant coaching` for those forms (length, no headings, no bullets, paragraph count, no summarising close), and `python3 scripts/lint.py draft.md --allow-markdown`. Fix every failure and every hard lint finding.
6. Return the column only.

## Skeleton

```
[Para 1: the trend as the reader has noticed it, granted as real.]
[Para 2: under fifteen words. The flip.]
[Para 3 to 5: the principle, defined in two sentences, with its linked source; the concession that many reject it, and why.]
[Para 6 to 10: the author's history with the idea. What they thought, what changed. One verdict paragraph.]
[Para 11 to 16: the turn. What follows once the cause is named. The opposing camp in a subordinate clause, answered in the main clause. One outside voice, one line.]
[Para 17 to 19: the assertion. The hedge, as a prediction the author will risk.]
```
