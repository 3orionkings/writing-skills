---
name: field-guide
description: Write a practical guide for people building AI or software products that opens with a credential and a diagnosis (or a consulting scene), states the common mistake as a flat fact, lets one client or case carry the piece, puts the real artefact on the page (a spreadsheet, a trace, a dashboard, a full prompt) before explaining it, numbers the method as steps or levels with a bold rule ending each, and closes with a numbered recap and a sentence that undercuts the method. Use it for how-to guides, field guides, evaluation and debugging write-ups, "what most teams get wrong about X", verdict-first FAQs, tool teardowns, and posts where screenshots and spreadsheets are the evidence; trigger on evals, a client, a worked example, a field guide, or "show the actual data". Not for: a survey of papers and patterns across a field (use patterns-survey). Stacks on the humanizer skill, which is loaded first whenever it is listed.
---

# Field guide

## What this form is for

Engineers and product people building something that misbehaves read it because the advice is attached to a real case and the artefact is on the page. The author has watched many teams make the same mistake and says so bluntly, then shows the fix on one client with a spreadsheet, a trace and a prompt, and names the tool that makes it repeatable. The bluntness reads as earned because the piece ends by admitting what the method does not do.

## Before writing

Load the humanizer skill if it is listed; otherwise read `references/human-writing-rules.md`. This skill supplies the form; the voice comes from the user's own draft or instructions in the conversation, never from a stored profile. Every number, name, date and quoted remark comes from the user's material or their instructions in the conversation; where the form wants a detail the user has not supplied, leave a bracketed placeholder such as [date] or [name], or ask, and never fill it with a plausible invention. A placeholder is a smaller defect than a false specific in a piece that carries the user's name. The examples in this file show a move, not content: never reuse an example's specifics (its numbers, names, events, analogies or phrasing) in the user's piece.

Gather: the credential in one clause (what the author built or led); the diagnosis (the one root cause behind failed products of this kind); the common mistake, stated as a fact; the one client or case that will carry the piece, named, or described by role if it cannot be named; the artefacts (a screenshot of a trace, a spreadsheet of critiques beside the model's output, a dashboard, the full prompt, a before-and-after interface); the method as steps or levels, ordered by cost; the counts (traces reviewed, agreement rate between a judge and a human, samples labelled); the tool used at each step; what the author relies on judgement for and where they failed; the numbered recap and the sentence that undercuts it. If you don't have a client or case from the user, use their own project or a public case they can point to, say which it is, and never invent a client, a count or an artefact.

## The shape

Four formats. The long guide of 3,000 to 5,000 words with screenshots. The FAQ of dozens of questions, each answered verdict first (No. Generally no. Yes.) then three to five sentences with bold lead-ins and dense cross-links, opening with a persona table and a warning that these are sharp opinions. The shorter polemic or teardown of 2,000 to 3,500 words, which opens on the claim and runs it through examples with no table of contents. And the notes page: annotated slides, each with a paraphrase and a short Q&A.

Opening. Two sentences: the credential and the diagnosis. Or a scripted consulting scene in the present tense with speaker labels. Then, in the long guide, a table of contents.

Body. Each section runs the same arc: name the mistake (as a flat fact), show it in an artefact introduced by a sentence ending in a colon, explain why it fails, show the fix in a second artefact, show the tooling, end on a bold one-line rule. The method is sorted into levels by cost (the cheapest check first) or numbered as steps one to seven on the one client, with the judge prompt or the spreadsheet reproduced whole. Callout boxes (tip, warning, note) carry one-paragraph asides.

Close. A numbered recap of the principles, then a sentence that undercuts or qualifies the method (the judge was not what created the value; you may not need any of this), then a pointer to a course or resource only if the user supplies one.

## The moves

Evidence is the author's caseload ([how many teams, clients or people the author has worked with]) plus the real object on the page; a claim is backed by a pivot table, not a paper. Reasoning is cost-ordered: cheapest check first, agreement tracked across iterations, before and after. The author prefers simple tools (spreadsheets, notebooks, a minimal custom interface) and argues against complex platforms by showing the simple version working. Disagreements with vendors and common practice are stated early and bluntly. The author says what they rely on judgement for, what they got wrong, and when an answer is a matter of taste. The FAQ shows a changed mind as a crossed-out old answer. Dated additions mark updates.

## Language

Direct and blunt. Sentences average 17 to 20 words with a fifth under ten. Heavy "I" and "you", "we" for team work. Bold for rules and list lead-ins. Dry interjections of a word or two. Profanity, if the author uses it, appears once, in a title or a closing line, never in the body. Jargon is left undefined because the reader is a practitioner. Typos and informalities are left as the author wrote them. The essay variant drops the bold and the callouts; the FAQ shifts to "we".

## Figures

About one image per 400 words in the guides: screenshots of real traces, dashboards and tool interfaces; a spreadsheet of a colleague's critiques beside the model's; an agreement chart; a before-and-after interface; a flowchart of the loop; a flashcard; a mockup. Captions in under ten words, or the image introduced by a colon sentence. A video of the client explaining their own process if one exists. The images are evidence of real work, never illustration.

## Departures from the humanizer

The FAQ answers verdict first in a word or two (No. Generally no. Yes.), and the guides allow a dry interjection of a word or two. The humanizer treats short fragments as a tell; here they are the form, so keep them where the form puts them (the verdict that opens an answer, the rare interjection) and nowhere else. The linter reports them as soft findings, and those can stay. Everything else in the humanizer applies, including the dash rule.

## What makes an imitation fail

Writing the method without the client, so the advice floats. Describing the spreadsheet instead of showing it. Hedging every verdict where the form states it once and caveats in a footnote. Adding citations the form never uses. Swearing in the body. Polishing away the typos and interjections. Dropping the self-undercut at the end, which is what makes the bluntness read as earned.

## Workflow

1. Write the credential and the diagnosis in two sentences. Write the common mistake as a flat statement.
2. Choose the one client or case. Collect the artefacts before drafting; if an artefact cannot be shown, say so and describe its exact shape.
3. Order the method by cost or as numbered steps on that client. Write the bold rule for each section first.
4. Draft the sections through the arc: mistake, artefact, why it fails, fix, tooling, rule. Add callouts for asides.
5. Write the numbered recap and the undercut sentence.
6. Save to a file and run `python3 scripts/style_check.py draft.md` for the long guide, or add `--variant faq`, `--variant teardown` or `--variant notes-page` for the other formats (length, numbered steps or levels, bold rules, a short caption or a colon introduction for every figure, no summarising close), and `python3 scripts/lint.py draft.md --allow-markdown`. Fix every failure and every hard lint finding.
7. Return the guide only.

## Skeleton

```
# [Title]

[Credential clause. The diagnosis: the one root cause.]  or  [Consulting scene, present tense, speaker labels.]

[Table of contents.]

## 1. [Mistake named as a fact]
[Here is what the trace looked like:]
![Caption under ten words.](trace.png)
[Why it fails. The fix:]
![Caption.](spreadsheet.png)
[The tool. **The one-line rule.**]

> Note: [one-paragraph aside]

## 2. ... same arc

## Recap
1. [Principle]
2. [Principle]
[The undercut: what this method is not, or whether you need it at all.]
```
