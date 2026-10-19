---
name: thesis-first-note
description: Write a short reflective note that states a personal belief in its first sentence, concedes the other side in paragraph two, carries the argument on one craft analogy from outside software, cites the author's own company once as evidence, and closes by restating the title as a maxim or on an unfinished personal line. Use it for founder and product notes, design and craft essays, reflections on AI tools and how work is changing, posts first drafted as a thread, and 400 to 1,300 word pieces from a personal point of view for people in software; the headed advice essay is a variant. Trigger on "a note on", "my thoughts on", "a short essay on", "a reflection on", or a post in a calm first-person voice. Not for: a management rule earned by one story under an imperative title (use one-idea-post), a column reframing a trend (use principle-column) or a long argument (use mechanism-essay). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# Thesis-first note

## What this form is for

Founders, designers, product leads and people building with AI read it for a point of view they can test against their own. The note gives them the belief in the first sentence, the honest concession right after, one analogy that makes the belief feel earned, and one fact from the author's own company. It is calm, single-threaded, and unpolished enough to read as a person thinking rather than a team editing.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies the form; the voice comes from the user's own draft or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather: the belief in under twelve words; the common view it stands against, as the industry would phrase it; the concession; one craft analogy from outside software (a cook, an architect, a cabinetmaker, a musician); one fact from the author's own company with a date or a number; the three or four plain nouns the note will lean on (quality, craft, intent, taste, or whatever the author's are); where the author could be wrong; the closing maxim or the unfinished line. If you don't have a fact from the user's own company, use one from their own work or team that they have supplied, or leave [company fact] and ask; never invent one.

## The shape

Two registers. When the user asks for something short, the note can run under 300 words; the form's usual range is below. The headless note, 370 to 900 words: no headings, no lists, often no first person at all in the shortest ones, a thesis and a turn and a close. The headed essay, 950 to 1,300 words: three to six sentence-case headings, numbers, bullets for a short list of practices, constant "you", and often an imperative heading per point; the talk write-up and the company announcement are louder variants of this one.

Opening. The thesis, or the belief about to be overturned, in sentence one, under twelve words, with "I think" allowed as the position marker. No scene-setting, unless the note is personal, in which case one sentence of scene ([a time and place from the author's own past]) then the question it raised.

Paragraph two concedes the other side, in a sentence as short as an admission that there is some truth to that.

Body. The turn ([what the common view misses, in one clause]). The analogy from outside software, carried for a paragraph or two. The author's company once, as evidence. Where the author could be wrong, once, in specific terms ([the setting where it holds]; [how old the evidence is]).

Close. Restate the title as a maxim and stop, or end on an unfinished personal line. In the headed essay, end on a personal admission, or on a hiring line only if the user supplies one. Never a summary paragraph.

## The moves

Evidence is first-hand and small: what the company did, a team size, a release cadence, a revenue-per-employee figure. The contrast partner is the industry, not a named rival. Trade-offs are named and a side is taken; sometimes the false choice (growth against craft) is rejected outright. Hedging is specific and placed: "I think" marks position, "might", "often" and "usually" limit scope, and one sentence admits where the author could be wrong. Rhetorical questions are a per-piece choice, many or none, never a few sprinkled in.

## Language

Sentences of eight to eighteen words broken by three-to-five-word ones and the occasional verbless fragment. Paragraphs of one to four sentences, with paragraph breaks doing the pacing. Plain vocabulary with the note's three or four nouns repeated rather than varied. Commas and full stops; almost no dashes, colons or parentheses in the note register. No adjectives of enthusiasm. Small imperfections of grammar are left alone; they are part of the register. The aphoristic closer may contrast two things, but it does not take the "not X but Y" template, which is a machine tell.

## Figures

Rare. One header image if the site uses them; a single product screenshot or a small diagram only in a how-to piece. Most notes are text only.

## Departures from the humanizer

Three of this form's habits touch the humanizer's rules. Fragments: the note allows the occasional verbless fragment between plain sentences; keep it rare and never use it as a reveal. Rhetorical questions: a per-piece choice, many or none; when the note uses them they carry the argument, so the linter's soft findings on them can stay. Dashes: the source notes use almost none, and this skill uses none, because the humanizer's dash rule holds; when the user's own writing uses dashes, keep them at the author's rate (lint with `--author-sample`). Everything else in the humanizer applies.

## What makes an imitation fail

Over-polishing: fixing every article, adding dashes and semicolons, varying the nouns. Piling on company anecdotes where one will do. Adding headings and bullets to a note that should run headless, or stripping them from an advice piece that needs them. Naming enemies and current products. Explaining what an agent or an issue tracker is. Adding enthusiasm and adjectives. Ending with a summary.

## Workflow

1. Write the first sentence. If it needs twelve words or more, the belief is not yet clear.
2. Write the concession as a single short sentence.
3. Choose the register (note or essay) by the ask and the audience, and draft straight through.
4. Add the one company fact and the one admission of doubt. Remove any second company fact.
5. Save to a file and run `python3 scripts/style_check.py draft.md` for the headless note, or add `--variant headed-essay` for the headed essay (length, first-sentence length, headings, paragraph length, no summarising close), and `python3 scripts/lint.py draft.md --allow-markdown`. Fix every failure and every hard lint finding.
6. Return the note only.

## Skeleton

```
[Sentence one: the belief, under twelve words. "I think" allowed.]

[Paragraph two: the other side, conceded in a sentence.]

[The turn: what the common view misses. The mechanism in plain terms.]

[The analogy from outside software, one or two paragraphs.]

[The company, once, with a number or a date.]

[Where this could be wrong, in one specific sentence.]

[The maxim, or the unfinished line.]
```
