---
name: humanizer
description: Rewrite or draft prose so it reads as written by a specific real person, with none of the patterns that AI detectors and experienced readers use to spot machine writing. Use this skill when the user asks to humanize, de-AI, "make it sound like me", "make it natural", strip AI tells, or rewrite in their voice; when they paste a draft (email, letter, advice, submission, post, message, bio, article) and ask for it to be edited, tightened, polished or cleaned up; and when the assistant drafts something the user will send or publish under their own name. Trigger even when the word "humanize" never appears. The assistant's replies that are such drafts follow these rules; ordinary conversational replies do not. Not for: code, commands, commit messages or data.
---

# Humanizer

## What this is for

The user sends prose and gets back the same prose in their own voice, with the machine patterns gone and nothing else changed. The standard is not "clean" but "written by this person". The readers who detect AI best (frequent LLM users, in an ACL 2025 study) go by formality, originality and specificity as much as by vocabulary, so a rewrite that only swaps out tell-words still reads as AI. What makes text read as human is the specific detail, the stated opinion, the aside, the sentence only this writer would write. Keep those. Add nothing generic.

## Workflow

1. Read the draft. Note the register (email, letter, memo, formal document, post, message), who will read it, and what the author wants from the reader. Note whether it already has structure (headings, lists, links); if it does, read Formatted content below before changing anything.
2. Mark what survives verbatim: citations, section and reference numbers, dates, figures, names of people, organisations and products, defined terms, quoted material, the salutation and sign-off, hashtags the author chose, and phrases that are conventional in the author's profession or trade (a lawyer's formal submission phrasing, a clinician's "unremarkable", an engineer's "ship" are register, not tells). If a citation looks wrong, keep it as written and flag it in one line above the text (step 5).
3. Decide how much to change. Run the linter (step 4) on the draft as it stands. If it has no hard findings and reads as specific (names, numbers, a stated stake, sentences only this writer would write), take the minimal edit path: fix what the soft findings point at where they are real, and return the rest as written. A clean, specific draft rewritten for the sake of it loses the author's voice. Otherwise rewrite the prose around the fixed points. Keep every fact and claim; invent none. Apply the rules below. Expect the result to be shorter than the draft, because the padding is what goes; never pad to match the original length.
4. Save the text to a scratch file and run the linter on it: `python3 <this skill's folder>/scripts/lint.py draft.txt` (or pipe text in with `-`). Add `--allow-markdown` for formatted content, and `--author-sample mine.txt` when the user has supplied writing of their own that uses dashes (see Punctuation). There is no need to read the linter's source; run it and read its report. Fix every hard finding and look at each soft one. A hard finding on a literal or trade term that the linter's allowlist misses (a social worker's foster care, an engineer's test harness, a landscape architect's landscape) is cleared by leaving the term as it is: the rule targets the tell, not the word. Never clear a flag by substituting another tell, an odd synonym, or an unusual character; the linter catches those too. The linter is a net, not the judge. A text with zero flags can still read as machine-written if it is generic.
5. Return the rewritten text only, in the same medium as the input. No preamble, no "here's the revised version", no list of changes, no closing offer. The one permitted note is the citation flag from step 2: a single line above the text, then a blank line, then the text. Nothing goes after the text. If the user asked a question rather than sending a draft, answer it under the same rules.

## Rules

### Punctuation
No em dashes or en dashes by default, and no spaced hyphen doing a dash's job ("the hearing - which was adjourned - "). Use a comma, a full stop or brackets instead. The exception is the author's own habit: when the user supplies writing of their own that uses dashes (an earlier email, a published post), keep dashes at the author's rate and no higher. Run the linter with `--author-sample` on that writing and it treats each dash as soft until the draft goes past the author's own rate. A dash between two numbers (2019–2021, pages 12–15) is a range, not a dash. Hyphens only inside compound words. A colon is fine before a list or a quotation, not as a rhetorical hinge ("The problem: nobody read it."). Semicolons sparingly. Exclamation marks only where the author uses them. Oxford commas and curly quotes: follow the draft.

### Vocabulary
Replace tell-words with the plain word a person would say. The full list lives in `scripts/lint.py`, the single source for this skill and for every style skill built on it; `python3 scripts/lint.py --list` prints it by severity. The commonest: delve, tapestry, realm, testament, underscore, pivotal, crucial, intricate, multifaceted, nuanced, vibrant, showcase, seamless, holistic, transformative, utilize, moreover, furthermore, additionally. Some words have an ordinary literal or trade sense (navigate, robust, dynamic, leverage, enhance, elevate, foster, harness, landscape, comprehensive, facilitate) and are tells only in their brochure sense: "navigate the complexities", "leverage our data", "the AI landscape". Foster care, a test harness and dynamic programming are just words, and the linter leaves them alone. Cut filler: very, really, truly, actually, basically, essentially, ultimately, genuinely, honestly, simply, just (as an intensifier), in order to, it is important to note, it is worth noting. The research behind the list is in references/ai-tells.md. Prefer the concrete noun and the plain verb.

### Sentence shape
Vary length on purpose. Let one sentence carry a subordinate clause and the next stop at five words. Start consecutive sentences on different words and different subjects. Drop the set-piece rhythms: groups of three ("fair, fast and proportionate"); "not just X but Y" and "it's not about X, it's about Y", including the version split over two sentences ("You're not sending more email. You're sending email that's harder to ignore."); "not because X, but because Y"; a fragment used for punch ("Not anymore."); a question the writer answers ("The result? ..."); a participial tail hung on a sentence (", highlighting the importance of ..."); "while X, Y" symmetry where the author meant one side; "everything from X to Y"; a formula that makes one noun the "language", "currency" or "architecture" of another; "serves as" or "stands as" where "is" will do.

### Structure
No headings, bullet points, numbered lists, bold or other markdown inside running prose; text that already has structure keeps it (see Formatted content). Where a paragraph of prose lists things, write them into a sentence. No opener announcing the topic's importance ("In today's fast-paced business landscape"), no signposting ("This note will first ..."), no closing summary, no line about the future. End on the last substantive point, or in an email on the specific ask. In a request email or letter, the ask goes in the first or second sentence, followed by one reason; then stop. Other emails and letters (an update, a reply, a thank-you) open on whatever the reader most needs to know. Nothing goes below the sign-off. Paragraphs break where the thought turns, not at a fixed length, and never open on a connective (Moreover, Furthermore, Additionally, Consequently, Overall, In conclusion, In summary). Fold transitions into the syntax with and, but, so, which, because, or drop them.

### Tone
Match the author, not a neutral professional register. Keep first person where the author uses it, opinions stated as opinions, humour if present. A first-person stake (what the writer has seen, done, wants) is the strongest human signal there is. Where the author's own experience is known from the draft, the conversation or memory, use it; never invent one, and never add a fact the author has not supplied. Do not fill a gap in what is known with speculation ("is believed to", "likely grew up in", "keeps a low profile"); say what is known and stop. No cheerful-assistant framing ("I hope this email finds you well", "Please do not hesitate", "I'd be happy to", "Great question"). No stacked hedges ("may potentially", "could arguably"); state the position, then the qualification if there is one. No significance framing ("plays a vital role", "cannot be overstated", "a testament to").

### Characters
No emoji, no ✅ ⚠ ─ or similar symbols, no decorative Unicode of any kind. Arrows and mathematical signs (→ ≈ ≤) are notation, not decoration: they belong in formulas and technical content linted with `--allow-markdown`, never in running prose.

## Formatted content

The no-markdown rule is for emails, letters, messages and running prose. Two kinds of text keep their structure.

When a style skill is loaded (field-guide, patterns-survey and the others that build on this one), its template governs headings, lists, bold, figures, footnotes and callouts, and so do any departures from these rules it names in its own "Departures from the humanizer" section (fragments, rhetorical questions, dashes). Follow the template, apply these rules to the sentences inside it, and lint with `--allow-markdown`.

When the input already has structure (a README, documentation, a web page, slides, a PR description, release notes), keep its headings, lists, links, tables, code blocks and call to action, and edit the prose inside them. Do not flatten a list into prose, and do not add structure the input did not have. Lint with `--allow-markdown`: markdown findings become soft and every sentence-level check stays as it is.

## Examples

Email, before: "I hope this email finds you well. I am writing to follow up regarding the proposed timeline — specifically, the 14 November deadline — which, in light of recent developments, we believe should be extended to allow for the comprehensive preparation of the deliverables."

Email, after: "We would like a short extension of the 14 November deadline for the deliverables. Our side's position has changed and the work needs more time. Can your team agree to 28 November?"

Note what the first rewrite does not do: it adds no reason the draft did not give. "Recent developments" stays as vague as the author left it.

Analysis, before: "It is important to note that the committee's discretion is broad and should be exercised only in clear cases. Moreover, the factual disputes are multifaceted and cannot be resolved on the papers alone. Consequently, an application at this stage would be unlikely to succeed."

Analysis, after: "The committee's discretion is broad and reserved for clear cases. This is not one. The facts are disputed on almost every point and cannot be settled on the papers, so an application now would fail."

Note what the second rewrite keeps: "clear cases", because it is the test the author is applying, and the author's conclusion, stated flatly because that is how this author writes.

## Author defaults

This skill ships neutral. Voice comes from the user's own draft and from any instructions they give in the conversation: their usual length, their sign-off, "I" or "we", the phrases they repeat, whether they use dashes. Where the draft shows a habit, keep it. A user who wants a standing description of their voice can add it here; until then, nothing about the author is assumed.

## What this skill does not do

It changes how text reads, not where it came from. Text generated by some current models, Claude models released since August 2026 among them, carries a statistical watermark that style edits do not remove (references/ai-tells.md, section 8). Do not claim or imply that a humanized draft is undetectable.

## Files

- `scripts/lint.py`: flags hard and soft tells, prints line numbers, reports sentence-length variation. Exit code 1 when hard findings remain, so it can gate delivery. Options: `--allow-markdown` for formatted content, `--author-sample FILE` or `--max-dashes-per-1000 N` to hold dashes to the author's rate, `--list` to print the vocabulary, `--json` for a machine-readable report. The same file ships in every style skill; edit it only through `tools/sync_shared.py` in the source tree.
- `references/ai-tells.md`: the catalogue, with the research behind each item and the sources. Read section 9 (what human writing has) before any rewrite longer than a paragraph; read the rest when a linter flag needs context.
