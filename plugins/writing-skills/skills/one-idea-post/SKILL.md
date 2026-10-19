---
name: one-idea-post
description: Write a very short post that carries one idea under an imperative title, uses the author's own experience as the evidence, reverses a common belief on a single hinge word, states the rule and qualifies it once, and closes under twelve words on a call to act. Use this skill for leadership and management posts, career advice, team notes, internal memos that set a norm, LinkedIn or blog posts under 750 words, "a quick post on X", "a short piece on how I think about Y", and any time the user wants to say one thing plainly to people who manage or build; the longer list essay (eight to fifteen numbered items) and the 150-word miniature are variants inside it. Trigger even when the user does not say post. Not for: a calm reflective note on craft or a belief (use thesis-first-note) or an opinion column that reframes a trend (use principle-column). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# One-idea post

## What this form is for

A manager, an engineer thinking about leadership, or someone early in a career reads it in two minutes and leaves with one rule and the story that earned it. The author has run the teams, made the mistake, and now tells the reader the shortcut. Everything that is not the one idea is cut.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies the form; the voice comes from the user's own draft or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather: the one idea, phrased as an imperative title of two to five words; the common belief or measure it reverses; the author's own story in four sentences or fewer (one named product or practice, one person at most, the rest compressed to a clause); the rule as an instruction to the reader; the one qualification; the closing line under twelve words. If you don't have the author's story, ask for it; if they have none to give, write the miniature, which needs no first person, rather than inventing one.

## The shape

Three modes, chosen by length and period.

The confessional post, 350 to 750 words: opens on a scene or an admission ([a mistake the author made]; [feedback the author got too late]) and lets the lesson arrive once the scene is complete. Six to eight paragraphs of one to four sentences. No headings, no lists, no images.

The list essay, 1,100 words or more: four paragraphs of argument, then eight to fifteen numbered items styled as a label of two or three words followed by a sentence or two, then a one-line close. The only form in which a numbered list belongs.

The miniature, 130 to 250 words: no first person, no hedge, one aphorism with one example, sentences averaging nine words. For a norm the author wants the whole organisation to repeat.

Opening. One plain sentence: a confession, or a claim about how people behave. No scene-setting beyond that sentence. The turn sits at the head of a paragraph on a single hinge word (still, but, though) and usually reverses received wisdom inside the first third: [people are measured by X], so measure them by [what X misses].

Body. The lesson, the story that proves it, the sharper restatement. The anecdote is usually compressed to a clause ([several times in my career]; [N years ago I launched a product]); when it is told in full it stays under four sentences. Numbers appear only as protocol ([a meeting's length and how it is split]). Hypotheticals get placeholder names or a type (the rising star).

Close. A declarative under twelve words that restates the title as a rule, tells the reader what to do, or admits the author is still working on it. No summary, no return to the opening image, no reflective coda.

## The moves

Experience is the evidence and it is stated as such in those words. Then the contrast with the common belief. Then the rule, stated and qualified in the next sentence (follow skill, but skill alone is not enough). Then a reframe of ownership where it applies: withheld feedback is your problem, not theirs. One engineering concept may be mapped onto people and left unexplained (leaky abstractions, a cold start, a personal API). Outside authority is one borrowed figure at most. A change of mind is reported as finished (over time, I realised), never performed on the page. Hedges number two per post at most, and the miniature has none.

## Language

Sentences average 15 to 19 words in the mid-length posts and about nine in the miniature, with a four or five word verdict after a long sentence. Plain management English with one formal word per post. First person carries the anecdote, "you" carries the advice, "we" means the company and sometimes everyone. Imperatives live in the title and the list labels, seldom in the body. Humour is one dry line at the author's own expense. Italics on a word or two; one to three links to the author's own earlier posts, only if the user supplies them; otherwise an unbroken column.

## What makes an imitation fail

Adding headings, bullets or images. Piling up anecdotes with names, dates and figures where one person and one product will do. Hedging in every sentence. Explaining the metaphor. Making the humour jokey. Writing a summarising closer. Writing a 2015-style confessional at miniature length, or a miniature full of first person. Quoting outside authority to shore up a rule the author's experience already supports.

## Workflow

1. Write the title first. If it is not an imperative or a thesis of five words or fewer, the idea is not yet one idea.
2. Write the closing line next, under twelve words. The post exists to deliver it.
3. Draft the opening sentence, then the hinge paragraph, then the story in four sentences, then the rule and its one qualification.
4. Cut anything that serves a second idea.
5. Save to a file and run `python3 scripts/style_check.py draft.md --variant confessional`, `--variant list-essay` or `--variant miniature`, matching the mode you chose (length by mode, no headings, imperative title, short close, paragraph length; without --variant only the checks the three modes share apply), and `python3 scripts/lint.py draft.md --allow-markdown`. Fix every failure and every hard lint finding.
6. Return the post only.

## Skeleton

```
# [Imperative title, two to five words]

[One sentence: the confession or the claim about how people behave.]

[The hinge paragraph. Still, ... / But ... The common measure reversed.]

[The story, four sentences or fewer. One product or practice named. One person at most.]

[The rule as an instruction to the reader. The one qualification in the next sentence.]

[Close under twelve words.]
```
