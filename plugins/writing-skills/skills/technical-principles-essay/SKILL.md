---
name: technical-principles-essay
description: Write a technical product essay that declares one lens, states its principles as headings that assert a claim, restates each principle in a two-sentence box, proves it with measured numbers that carry units and linked sources, runs a demo, and closes in two or three lines on the medium itself. Use it for engineering and product essays with graphs, benchmarks, latency figures or recorded demos; "N principles of X" pieces; the technical case for a product decision; developer-facing announcements that argue rather than announce; and any piece that proves a claim with a number or a screenshot rather than asserting it. Trigger on principles, benchmarks, latency, performance, a demo, a technical essay, or a product thesis for engineers. Not for: a policy or position argument (use mechanism-essay), company strategy (use strategy-pattern-essay) or a short reflective note (use thesis-first-note). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# Technical principles essay

## What this form is for

Engineers who ship, and the founders and product leaders who used to, read it because every claim comes with a measurement and every measurement comes with a source. The essay declares one lens up front (user-perceived latency, say) and judges everything through it. The visuals prove; they never decorate. The reader is assumed to know the stack, so nothing basic is explained.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies the form; the voice comes from the user's own draft or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather: the one lens; the principles (three to seven), each phrased as a claim; for each principle a number with a unit and a linked primary source (a packet capture, a benchmark, a published threshold, a physical limit); the demo the author can run on their own product, blog or pull request; the primary sources worth quoting at length (a mailing-list post, an engineering book, a talk); the exception to each principle; the historical precedent the argument reaches for; the borrowed quotation or the one line about the medium that will close it. If you don't have a product, blog or pull request of the user's to demo on, run the walkthrough on something public they can point to (an open-source project, a public site), credit it, and never imply it is theirs; if there is nothing to show, describe the measurement in words.

## The shape

Four formats. The long argumentative essay of 2,000 to 5,000 words with numbered principles. The mid-length single-thesis essay of 1,200 to 1,500 words that ends in a demo or a product. The announcement written as a vision statement (a founding frustration, traction numbers, a historical analogy, three shifts as headings, a mapping table). The short note of 150 to 700 words made of one-sentence paragraphs with no headings or images.

Opening. One paragraph that places the piece in time and in the author's own work: a talk given, an earlier tweet, a player rebuilt, a founding frustration. Then the open questions the field argues about, and the promise to answer them from one lens only.

Body. Each principle gets a heading that asserts (pre-rendered pages are not optional), a two-sentence restatement in a quote box, and then the argument. Within the argument: the physical or numeric evidence first (speed-of-light arithmetic, a first-window size, a response-time threshold), then the recorded demo or the walkthrough, then the exception the author names before the reader can (optimistic updates are wrong for payments and logout). The single-thesis essay states the thesis in bold, removes objections in three headed sections each answered with a named tool or paper, and spends its last third on a screenshot walkthrough in which the author breaks their own thing on camera.

Close. Two or three lines on the medium itself, often someone else's sentence or an aphorism. No summary.

Footnotes carry the side arguments. The year-in-review variant is twenty-odd fragments whose headings are claims, each followed by a few paragraphs, an embedded quotation and a footnote.

## The moves

Reasoning from physics, measured numbers and observed user behaviour, with web or systems history as precedent (an early mailing-list post quoted to show an idea predates its fashionable form). Primary sources are quoted at length rather than summarised. Numbers are odd, sourced and linked, never round. Confidence is plain and unhedged, and each claim is fenced in the same section by one concrete exception. What the author got wrong ([a component that needed more states than planned]) is shown and turned into a distinction. Tables and charts replace comparison paragraphs. Code can be the argument: a function that renders a player from state, a JSON file enumerating states, the counterexample in the old style.

## Language

First person throughout. Median sentence of 15 to 18 words; paragraphs of one or two sentences make up more than half of every piece. One bold claim per section, italics on the key term, a link on nearly every noun that has a source. Later-period pieces grow more declarative, with fragments. Nothing is defined for a beginner.

## Figures

Recorded GIFs or screenshots of real products doing the thing, each captioned with the finding as a full sentence. A six-screenshot walkthrough for a demo. A two-column table mapping old primitives to new ones. A live chart where the data is public. Fifteen images in a long essay is normal; a decorative one is not.

## Departures from the humanizer

Later pieces in this form are more declarative and use fragments, and the short note is built from one-sentence paragraphs. Keep a fragment only where it lands a measured claim the sentence before it set up; never use one as a reveal or a hinge. The linter reports fragments as soft findings, and those can stay. Everything else in the humanizer applies, including the dash rule.

## What makes an imitation fail

Long paragraphs. Headings that name topics instead of asserting claims. Visuals that illustrate rather than prove. Hedging, where the form states the claim plainly and fences it with one exception. Round numbers. Explaining fundamentals. Dropping the personal anchor (the talk, the rebuild) that the authority comes from. A summarising conclusion.

## Workflow

1. Write the lens sentence and the list of principles as claims. Any principle that cannot be stated as a claim is not yet a principle.
2. Open every source before citing it. For each principle, record the number, its unit, the conditions it was measured under and where it appears in the source; mark anything you could not open or confirm as [unverified] and keep it out of the finished essay until the user confirms it. Collect all of this before drafting a word of argument.
3. Plan the demo (on the author's own product or blog, or a credited public one), and the exception to each principle.
4. Draft in order: opening anchor, questions, lens, principles with boxed restatements, demo, close.
5. Save to a file and run `python3 scripts/style_check.py draft.md` for the long essay, or add `--variant single-thesis`, `--variant announcement`, `--variant short-note` or `--variant year-in-review` for those formats (asserting headings, boxed restatements, numbers, links, full-sentence captions, no summarising close), and `python3 scripts/lint.py draft.md --allow-markdown`. Fix every failure and every hard lint finding.
6. Return the essay only.

## Skeleton

```
# [Title]

[Para 1: where this comes from (the talk, the tweet, the rebuild). The open questions. The one lens.]

## 1. [Heading that asserts a claim]
> [Two-sentence restatement of the principle.]
[The number with unit and linked source. The precedent. The demo or GIF, captioned with the finding. The exception.]

## 2. [Next asserting heading] ... same sequence

[Walkthrough: screenshots of the author running the demo on their own thing.]

[Two or three lines on the medium. A borrowed sentence or an aphorism.]

[Footnotes.]
```
