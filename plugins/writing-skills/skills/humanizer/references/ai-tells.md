# The catalogue of AI-writing tells

Compiled October 2026 and revised November 2026 from Wikipedia's "Signs of AI writing" field guide (maintained by WikiProject AI Cleanup), Pangram's corpus analysis, Pew Research Center's web study, an ACL 2025 study of human detectors, a vocabulary study of PubMed abstracts, a study of the focal words behind that shift, the Binoculars detection paper, and Anthropic's help-centre note on watermarking. Each entry says what the pattern is, how strong a sign it is now, and, where known, how much more often it appears in machine text than in human text. The wording here is this skill's own; the Wikipedia guide is the place to read the original observations and their examples.

Contents
1. Where the patterns come from
2. How detectors and readers work
3. How to weigh a tell
4. Emphasis instead of content
5. Mechanical rhythm
6. Inflated importance
7. Vocabulary
8. Formatting
9. Chat and draft residue
10. Context the reader already has
11. Citations and invented detail
12. What human writing has
13. Signs that no longer work
14. Watermarks (what style editing cannot touch)
15. Sources

## 1. Where the patterns come from

A language model writes the most likely next word, and a second round of training then tunes it towards prose that the widest range of readers will accept. The result regresses to the mean: specific, unusual facts (statistically rare) give way to generic, positive description (statistically common). The Wikipedia guide's image for this is a portrait that fades from a sharp photograph into a blurry sketch while a caption insists ever louder that the subject is important. The subject becomes less specific and more exaggerated at the same time.

The patterns below are that pull towards the average, showing up in different places. A person writes for one reader about one subject, and their choices come out uneven and particular. A model writes for everyone, so it reaches for moves that fit anywhere: a contrast that adds weight, a group of three that sounds complete, a closing line that tells the reader what to feel. Vocabulary turns over with each new model; the structural moves stay, so this catalogue starts with them.

## 2. How detectors and readers work

Automated detectors measure two things above all. Perplexity: how predictable each next word is to a language model. Machine text picks the likely word every time, so it scores low. Burstiness: how much sentence length and structure vary. Newer detectors are trained classifiers that read the whole document and weigh thousands of signals at once, which is why swapping one tell-word for a synonym rarely moves a score. Zero-shot methods such as Binoculars contrast two related models and catch over 90% of ChatGPT output at a 0.01% false-positive rate. Independent 2026 benchmarks put commercial detectors at 63 to 91% true-positive rates with 1 to 8% false positives, and paraphrasing, markup and spacing changes all degrade them, so no score is proof either way.

People who use LLMs for writing every day are the best detectors. A majority vote of five such readers misclassified one article in 300, beating every automated detector tested, including on paraphrased and "humanised" text. They go by vocabulary first, then by formality, originality and clarity without specificity. People who rarely use LLMs perform at chance. Write for the first group.

Human writing is also absorbing machine habits: studies through 2024 and 2025 found LLM vocabulary spreading into speech and podcasts. The reverse is not happening. So a single tell in a single document proves little: rely on clusters of tells, not one.

## 3. How to weigh a tell

The rarer a choice is among careful writers, the stronger a tell it is. The emphasis patterns in section 4, chatbot framing and the artefacts in section 9 warrant an edit the first time they appear. Most others are weak alone: a dash, one group of three, a passive sentence, a single "however". A weak tell counts only when others share the passage.

The linter mirrors this. Hard findings are tells a careful writer almost never produces; fix every one. Soft findings need a look: keep the sentence when the author meant it, rewrite it when the tell is doing the work a fact should do.

Some patterns now belong to the past (section 13). Text written before 30 November 2022, when ChatGPT reached the public, was not written by a chatbot whatever it looks like. A phrase that is quoted, part of a title or name, or being talked about rather than used is never a tell.

## 4. Emphasis instead of content

Current models produce these more than any other tell, and they give the text away fastest. The sentence claims weight it has not earned with a fact.

Pause-for-effect closers. A short paragraph or sentence that repeats the one before it, or tells the reader to stop and absorb it: "Let that sink in.", "Read that again.", "That's the whole point.", "That matters." A closer repeated section after section is a stronger sign. So is a line after an example spelling out the lesson it already made ("It was a lesson in patience.", "The message was clear.", "This shows the importance of testing early."). Delete the repeat; a short sentence stays if it brings in something new, a fact or a consequence the example left out.

Dramatic fragments. A run of fragments ("No preference for symmetry. No nostalgia. No rules.") or emphasis by full stops between words ("every. single. day."). Fold them into one sentence that says something specific.

Throat-clearing openers and staged candour. "Let's dive in", "Here's what you need to know", "Here's the thing", "The thing is,", "Real talk:", "Quick note:", "Now let's look at", and a one-word question before an ordinary answer ("Honestly? It depends."). Delete the opener itself; softening its tone is not enough. People say "honestly" mid-sentence all the time; what marks the machine is the word standing alone as a lead-in.

Faux-profound sayings. "The real question is", "What really matters is", "At its core", "The heart of the matter", "The deeper issue", and aphorism formulas that make one noun the "language", "currency", "architecture", "operating system" or "lifeblood" of another, or say that something "becomes a trap" or "is a mirror". A plain point gets dressed up as a revelation. Say the specific thing the saying gestures at.

Rebutting objections nobody made. The text answers a view or rules out an option that appears nowhere else: "Don't get me wrong", "Some might argue", "To be clear", "You might think", "I'm not saying X", "It would be easy to just", "This isn't about X", "One might be tempted to". Typically residue from a prompt or an earlier version. Drop the rebuttal and keep any real claim inside it. Keep an objection when the text says who raised it and answers it, and an option a reader would genuinely consider.

Negative parallelism. "Not just X but Y", "not only X but also Y", "It's not X, it's Y", "This isn't X; it's Y". The same move split across sentences on one subject ("You're not sending more email. You're sending email that's harder to ignore.", "This does not mean X. It means Y."), hung on a cause ("not because X, but because Y"), reversed ("Y rather than X"), listed ("No meetings, no slides, just code."), or clipped into a tail (", no guessing."). The denied half is a claim nobody made, set up so the real point looks bigger by contrast. Pangram counts the "not just X but Y" template at 3 times the human rate, Pew found negative parallelism nearly tripled on the web between 2023 and 2026, and frequent LLM users name "it's not X, it's Y" as the single most recognisable tell. A contrast earns its place only if readers really do believe the negated half, or if both halves say something.

Corrective framing. Since mid-2026 models often recast a source or claim as a hedge: something "should be read as a personal recollection rather than a verified record", the evidence "does not establish" a firm conclusion, a topic "should not be confused with" another. Wikipedia's editors found this almost unheard of before July 2026. State what the source says and stop.

## 5. Mechanical rhythm

Groups of three. 4 times the human rate (19 vs 5 per 10,000 words). "Speed, scale and simplicity"; three parallel examples followed by a lesson; three short facts and a moral. Human writers list three things when there are three things; models list three things by default, often to make a thin analysis look complete. The sign is stronger where nobody bothers with flourishes, such as a change note.

Repeated openings. Several sentences in a row that start on the same word or subject. Combine them, or open on the verb. Deliberate repetition for rhythm is human; three in a row without purpose is not.

Uniform sentence length. Older output sat at 15 to 25 words per sentence, subject then verb then object. Output from mid-2026 on keeps to a tighter band of roughly 8 to 20 words, with more full stops and commas and fewer of any other mark. Either way the rhythm is flat. A long sentence that earns its length followed by a short one is human; ten sentences of the same length are not.

Self-answered questions. "The result? Fewer errors." "Why? Because ..." The question exists to set up its own answer.

Participial tails. A sentence that ends on a comma and an -ing phrase commenting on itself: ", highlighting the importance of collaboration", ", ensuring a seamless experience", ", reflecting broader trends". The tail asserts significance without adding a fact. Newer tools attach these to named sources whether or not the source says anything close. The tail stays only if a source backs what it asserts.

Hedged symmetry and stacked hedges. "While X is true, Y" where the author holds one view; "on the one hand ... on the other"; "may potentially", "could arguably", "to some extent". State the position, then the qualification if there is one. One qualifier like "perhaps" or "tends to" is how people write (section 12).

Dashes. See section 13 for how this sign has changed. The skill's default is no em dashes, no en dashes and no spaced hyphen used as a dash; when the user supplies writing of their own that uses dashes, keep them at the author's own rate. `lint.py --author-sample FILE` measures that rate and only flags the draft when it goes past it. A dash between two numbers (2019–2021) is a range and is never flagged.

## 6. Inflated importance

There is usually a real fact underneath; keep it and strip what is piled on top.

Significance framing. "Plays a vital role", "stands as a testament to", "marks a pivotal moment", "part of a broader movement", "cannot be overstated", "more important than ever", "enduring legacy", "setting the stage for", "a new era". Models attach these to the most mundane facts (an etymology, a population figure), sometimes after admitting the subject is minor. On living things they belabour ecosystems and conservation status. Keep the fact; cut the claim that it matters.

Influence framing. A subject is placed amid broader "debates" or "public discussions": the ruling "sparked broader discussions about privacy". Say what changed, or cut it.

Notability padding. Coverage named instead of what the coverage said: "has been featured in The New York Times, the BBC and the Financial Times", "received independent coverage in trade publications", a primary source "identifies" the subject, "maintains an active social media presence", "over 500,000 followers". The first two are more common in output from 2025 on, and the emphasis on identification by primary sources became common in 2026. Give one source and what it actually said, or cut the list.

Vague attribution and overgeneralisation. "Experts believe", "critics argue", "industry observers note", "is widely regarded as". Models also inflate the number of sources: one reviewer becomes "reviewers", one example becomes "among others". Name who, or cut the claim. An unsourced claim is not a sign by itself; most writing cites nothing.

Vague association. "Associated with", "connected to", "linked to", "in connection with" where the text could say how. "Associated with the leadership of the company" leaves the reader guessing at the actual role. If the real relationship is known, state it; if not, the vague phrase is safer than a guess.

Avoiding plain is and has. "Serves as", "stands as", "functions as", "marks", "represents"; "boasts", "features", "offers" for "has"; "began his career as" or "ventured into politics as" for "was". One study found an over 10% fall in "is" and "are" in academic writing in 2023, and the same fall appears when a model is asked to revise a sentence. A model writing about a topic will also define it with "refers to", as if the article were about the term. Use is, are and has.

Sales language. "Nestled", "in the heart of", "breathtaking", "renowned", "diverse array", "rich cultural heritage", "must-visit". Common in output from 2023 to 2025 and much rarer since (section 13), but still a tell where it appears. Say plainly what it is.

Stock sections. A "Challenges" section that opens "Despite its strengths, X faces challenges" and closes on a vaguely hopeful note; a "Future Outlook" or "Future Prospects" section; an "Awards and recognition" section; a closing "Conclusion". The sign is the rigid formula, not the mention of a challenge. Stop at the last concrete fact, and mention plans only when the source gives real ones.

## 7. Vocabulary

A study of 14 million PubMed abstracts found an abrupt rise in certain style words after ChatGPT's release, implying at least 10% of 2024 abstracts were LLM-processed. The shift was in style words, not content words. Pew's web study (490,000 pages) found AI-favoured vocabulary more than doubled on the web between 2023 and 2026. Pangram counts "AI phrases" at 12 times the human rate (30 vs 3 per 10,000 words). The words cluster: where there is one there are usually others, and one or two in a long text may be coincidence.

The favourites change with each model generation. Wikipedia's editors track rough eras:

- 2023 to mid-2024: additionally, boasts, bolstered, crucial, delve, emphasizing, enduring, garner, intricate, interplay, key, landscape, meticulously, pivotal, underscore, tapestry, testament, valuable, vibrant.
- Mid-2024 to mid-2025: align with, bolstered, crucial, emphasizing, enhance, enduring, fostering, highlighting, pivotal, showcasing, underscore, vibrant.
- Mid-2025 to mid-2026: emphasizing, enhance, highlighting, showcasing, plus the notability language in section 6.
- Mid-2026 on: challenge, clearer, dependable, echoed, foster, leverage, matters, multifaceted, practical, prioritize, quietly, steady, universally, with shorter sentences and more full stops and commas.

Take each word literally. A word being overused does not make its synonyms tells, and "underscore" can still mean an underline.

The working list is `scripts/lint.py`, the single source for the humanizer and every style skill built on it; `python3 scripts/lint.py --list` prints it by severity. This section explains the tiers; when the two disagree, the linter is right and this file is out of date.

Hard in any use: delve, tapestry, realm, testament, underscore, pivotal, crucial, intricate, meticulous, multifaceted, nuanced, vibrant, showcase, garner, bolster, interplay, seamless, notably, additionally, moreover, furthermore, ever-evolving, fast-paced, game-changer, cutting-edge, state-of-the-art, holistic, streamline, empower, transformative, groundbreaking, invaluable, paramount, utilize, embark, beacon, unlock, unleash, resonate, thrive, synergy, align with, boasts.

Hard only when figurative or beside other tells: navigate, landscape, robust, dynamic, leverage, enhance, elevate, foster, harness, comprehensive, facilitate. Each has an ordinary literal or trade sense, so the linter reports it as soft unless the use is the brochure one ("navigate the complexities of", "the AI landscape", "leverage our data", "foster a culture of") or another tell sits in the same sentence. Fixed collocations are never flagged: foster care, enhanced due diligence, leverage ratio, elevated blood pressure, test harness, dynamic programming, dynamic range, robust standard errors, landscape architect, navigate to. A literal or trade use the allowlist misses is cleared by leaving it.

Soft in every use: journey (figurative), emphasizing, essential, highlight (as a verb for "show"), key (as an adjective), perfectly, significant(ly) (when it means "large"), valuable, quietly, echoed, enduring, dependable, universally.

Filler (soft; cut where it pads, keep where it is how the author talks): very, really, truly, actually, basically, essentially, ultimately, genuinely, honestly, incredibly, extremely, highly, simply, just (as an intensifier), in order to, in terms of, a wide range of, a variety of, when it comes to, the fact that.

Replacement principle: the word a person would say aloud. "Use" for utilize. "Help" for facilitate. "Show" for showcase, highlight, underscore. "Big" for significant. "Important" is usually a sign the sentence should say why it matters instead.

## 8. Formatting

Markdown in plain-text contexts: 12 times the human rate (90 vs 8 per 10,000 words). Bold is 43 times, headers 23 times, inline code 5 times. Humans typing into email clients, forum boxes and documents rarely mark up. Asterisks and hash signs left raw in a medium that does not render them, and text wrapped in a code block for no reason, are among the most certain signs there are.

Bullet lists: 9 times the human rate (28 vs 3 per 10,000 words), often where prose would read better. Lists where every item opens on a bold label and a colon are a specific tell: rewrite them as prose if the labels say nothing the sentences do not.

Headings: title case where the medium uses sentence case, a top-level heading that repeats the document's title, several top-level headings, a heading on every two paragraphs, a heading chosen for drama instead of describing the section, a rule between every section, and a first line that says the heading again.

Emoji and symbols: emoji volume is only 2 times human, but the type differs. ✅ is 167 times, keycap digits 61 to 129 times, 🚀 26 times. Emotional emoji (😊, ❤️) skew human; functional ones (ticks, warnings, numbers) and emoji at the start of headings or list items read as machine. Unusual Unicode runs 3 times the human rate: box-drawing ─ (940 times), ≈ (241 times), ⚠ (57 times), → (48 times). In technical writing with formulas, arrows and mathematical signs are notation; `--allow-markdown` leaves them alone.

Quotation marks and commas: curly quotes pasted into contexts where people type straight ones are a weak sign, since most editors curl automatically. Oxford commas rose 63% on the web since 2023. Follow the author's habit for both.

## 9. Chat and draft residue

Chatbot framing. "Certainly! Here's" appeared 0 times in human text and 94 times in AI text per 10,000 words in Pangram's corpus. Also "Sure! Here's a", "Great question", "You're absolutely right", "I hope this helps", "Let me know if you'd like", "Would you like me to", "Should I continue?", and a list of changes appended to a rewrite nobody asked to be annotated. Nothing is a surer sign, and it hides easily when real content sits inside it.

Collaborative and customer-service register. Text meant as advice to the user, pasted as if it were the content; or comments that sound like a clerk: claims to have "carefully reviewed" the work, apologies for any inconvenience "that may have been caused", invitations to point out "specific issues" so they can be resolved.

Disclaimers about sources. Older output warned that a topic was "important to note" or varied by place. Output from 2024 and 2025 with web search often claims information is "not publicly available" or "not widely documented" and then guesses what it "likely" is; for people, that they "maintain a low profile" or "keep personal details private". Both the claim and the guess are speculation. State what is known and stop.

Placeholders and artefacts. Fill-in-the-blank templates left unfilled ("[insert name]", "[Your Company]"); dates such as "2026-xx-xx"; strings such as INSERT_SOURCE_URL; links to subpages of example.com; tracking parameters such as utm_source=chatgpt.com or utm_source=openai; citation residue such as "oaicite" or "contentReference"; the ↩ character beside footnotes. A tracking parameter shows a chatbot found the source, not that it wrote the text, but it is a reason to read closely.

Text that describes itself instead of its subject. Notes on what the text supersedes ("this page replaces the old setup guide"), on how it was put together ("pulled together from public filings", "where a figure could not be confirmed we say so instead of estimating"), on a layout already visible ("the table below compares"), and the procedural voice of a machine edit summary: "revised to ensure neutrality and improve clarity while preserving the original meaning". People rarely mention what they did not change. A source the reader can check stays, and so does any warning that alters what the reader will do; the story of how the text was made goes.

## 10. Context the reader already has

A model assumes a reader with no background, the safest guess across all readers. Someone answering in a thread is writing to a person who was there. A short reply that retells the problem, works through the cause and defends the plan before it gets to the decision leaves the answer in the last line. Put the decision first and keep only what could change the reader's mind, typically the single fact they are missing and whatever link lets them act. Because every sentence may be fine in isolation, sentence-by-sentence editing misses it. Apply it only when you can see the thread, or the text is obviously a response.

The same habit shows in standalone writing as explaining what every reader already knows. A person leaves that out.

## 11. Citations and invented detail

Fabricated or mis-assigned citations: references to papers that do not exist, DOIs that resolve to unrelated articles, invalid ISBN checksums, book citations without page numbers on general topics, several dead links in a new document that no web archive has seen. Retraction Watch reported a roughly twelve-fold rise in fabricated references in PubMed-indexed literature over two years. Never alter a citation while humanizing. Keep it as written and flag any that looks wrong, in one line above the text.

Generic claims where specifics belong, padding a subject's importance with minor mentions, and both-sides balance on a question the author has decided are content tells. Fix them with specifics the author supplies, never with specifics the model supplies.

## 12. What human writing has

Specificity: the date, the amount, the name, the version number, the thing that actually happened on Tuesday. One concrete detail does more than any amount of vocabulary scrubbing.

A stake: the writer wants something from the reader and says so. Emails end on the ask. Advice ends on the recommendation. Posts end on the point, not on "exciting times ahead".

Opinion as opinion: "I think the plan fails" rather than "it could be argued that the plan may face challenges".

Plain syntax. Over 25 years of Wikipedia writing, these turn up more in human text than in machine text: simple "there is" and "it has" constructions; plain verbs (wrote, not authored; moved, not relocated; used, not utilized; tried, not attempted; died, not passed away); definitive statements (is the only, was the first, one of the best); single qualifiers and intensifiers (very, perhaps, tends to); and small wordy constructions (as a result of, in order to, all of the, the fact that). So the fix for machine prose is not to strip every qualifier and filler word: a text scrubbed of all of them reads as more machine-like, not less. Cut filler where it pads; keep it where it is the author's voice.

Repetition. Older models were tuned to avoid repeating words, which produced elegant variation: the subject called by three different names in three sentences. People repeat the plain word.

Uneven rhythm: a long sentence that earns its length, then a short one. Sentences that start with "And" or "But" when that is how the thought arrived. A parenthesis where the writer would have lowered their voice.

Register that belongs to a trade or community: a clinician's "unremarkable", an engineer's "ship", an accountant's "reconcile", a teacher's "scaffold", the fixed phrases of a profession's formal documents. These are how the profession writes and are not tells. Keep them. Strip only the generic layer on top.

Omission: a person leaves out what the reader knows.

The writer's own habits: the sign-off they always use, the word they overuse (if it is their word and not the model's), the one-line paragraph before the ask, mixed feelings left unresolved, a dated reference, an aside or a self-correction. Keep whatever the draft shows.

## 13. Signs that no longer work

Some signs people rely on do not distinguish machine from human text, and some have faded as models changed. Treating them as tells produces false accusations and pointless edits.

Ineffective as signs: perfect grammar (many people write well); a mix of casual and formal registers (common in technical fields, in young writers, and in text with several authors); prose that merely feels bland or robotic; formal or academic prose in general (only specific words are overused, not formality itself); transition words in isolation (only a few, such as additionally and notably, are overused, and essay writers have always used them); and a lack of citations.

Historical, still worth catching but rarer in new output:

- Em dashes (roughly 2022 to September 2026). Models used them about 10 times as often as people (humans 2 to 5 per 10,000 words; OpenAI models about 45, Anthropic models about 32, Gemini 3 Pro about 3), often spaced and in sales-like emphasis. Pew found them roughly doubled on the web between 2023 and 2026. A July 2026 study found only Claude still above professional writers. Since September 2026 the newest models increasingly avoid dashes altogether and fall back on full stops and commas more than people do, which is its own sign. So removing dashes does not make text read as human. Replace a dash with whatever mark the sentence needs (a comma, brackets, a colon before a list, a full stop) and vary them.
- Promotional, travel-guide language (2023 to 2025).
- Knowledge-cutoff statements ("As of my last update") (2022 to 2023), and outright refusals ("As an AI language model").
- Section summaries and closing "In conclusion" paragraphs, now much less common but still produced by older models.
- Elegant variation from repetition penalties.
- Text that stops mid-sentence where an older chatbot ran out of tokens.

## 14. Watermarks (what style editing cannot touch)

Anthropic's help centre (August 2026) states that Claude models launched on or after 2 August 2026 weave an imperceptible statistical watermark into generated text; it lives in word choice, not hidden characters, travels with copy and paste, and may persist through some editing. Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5 are among the listed models. Detection is in private preview for regulators, law enforcement, media, fact-checkers, researchers, educational organisations and compliance-obligated enterprises, with wider access planned. Anthropic's own stated limits: a detected mark only means the text may have been processed by Claude (proofreading counts), not that Claude authored it; and text that has been heavily edited, paraphrased, translated or mixed into other writing, or that is very short, may carry no detectable mark. Google's SynthID-Text and OpenAI's planned marking work on the same principle.

This skill makes prose read as the author's. It does not and cannot remove a watermark from a draft generated by a model that marks its output, and it should never be described as doing so.

## 15. Sources

- Wikipedia: Signs of AI writing (WikiProject AI Cleanup), revision of 18 November 2026: https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing (text available under CC BY-SA 4.0; this catalogue paraphrases it and quotes only short example phrases)
- Pangram, 9 Signs of AI Writing, Backed by Data: https://www.pangram.com/signs-of-ai-writing
- Pew Research Center, How Much of the Internet Is Written With AI? (20 Aug 2026): https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/
- People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text (ACL 2025): https://arxiv.org/abs/2501.15654
- Delving into ChatGPT usage in academic writing through excess vocabulary: https://arxiv.org/abs/2406.07016
- Why Does ChatGPT "Delve" So Much?: https://arxiv.org/abs/2412.11385
- Spotting LLMs With Binoculars: https://arxiv.org/abs/2401.12070
- Anthropic, How Claude marks AI-generated content: https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
- CASRAI, How AI detection actually works: https://casrai.org/guides/how-ai-detection-actually-works
