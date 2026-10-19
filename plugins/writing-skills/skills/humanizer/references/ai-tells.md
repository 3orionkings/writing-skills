# The catalogue of AI-writing tells

Compiled October 2026 from Pangram's corpus analysis, Pew Research Center's web study, the WikiProject AI Cleanup field guide, an ACL 2025 study of human detectors, a vocabulary study of PubMed abstracts, a study of the focal words behind the shift, the Binoculars detection paper, and Anthropic's help-centre note on watermarking. Each item says what the pattern is and, where known, how much more often it appears in AI text than in human text.

Contents
1. How detectors work, and why that matters for rewriting
2. Vocabulary
3. Phrases
4. Punctuation and formatting
5. Rhetoric and structure
6. Chat artefacts
7. Content tells
8. Watermarks (what style editing cannot touch)
9. What human writing has that AI writing lacks
10. Sources

## 1. How detectors work, and why that matters for rewriting

Automated detectors measure two things above all. Perplexity: how predictable each next word is to a language model. AI text picks the likely word every time, so it scores low. Burstiness: how much sentence length and structure vary. AI text sits in a narrow band (often 15 to 25 words per sentence, subject-verb-object); human text spikes and drops. Newer detectors are trained classifiers (fine-tuned transformer models on millions of paired samples) that read the whole document and weigh thousands of signals at once, which is why swapping one tell-word for a synonym rarely moves a score. Zero-shot methods such as Binoculars contrast two related models and catch over 90% of ChatGPT output at a 0.01% false-positive rate without any training on it.

Two consequences for rewriting. First, uniform rhythm is itself a tell, independent of word choice: vary sentence length and sentence openings deliberately. Second, polished, formal, heavily edited and non-native prose trips detectors most, because editing passes smooth out the unevenness that reads as human. Independent 2026 benchmarks put commercial detectors at 63 to 91% true-positive rates with 1 to 8% false positives, so no score is proof either way.

The best human detectors (people who use LLMs for writing every day) rely on vocabulary first but also on formality, originality and clarity-without-specificity, which detectors cannot easily measure. A majority vote of five such readers misclassified one article in 300, beating every automated detector tested, including on paraphrased and "humanised" text. Non-users performed at chance. Write for those five readers.

## 2. Vocabulary

A study of 14 million PubMed abstracts found an abrupt rise in certain style words after ChatGPT's release, implying at least 10% of 2024 abstracts were LLM-processed. The shift was in style words, not content words. Pew's web study (490,000 pages) found AI-favoured vocabulary more than doubled on the web between 2023 and 2026.

Pangram counts "AI phrases" at 12 times the human rate (30 vs 3 per 10,000 words). Different model families have different favourites.

The working list is `scripts/lint.py`, the single source for the humanizer and every style skill built on it; `python3 scripts/lint.py --list` prints it by severity. This section explains the tiers and names examples; when the two disagree, the linter is right and this file is out of date.

Hard in any use (replace with the plain word, or cut): delve; tapestry; realm; testament; underscore; pivotal; crucial; intricate; meticulous; multifaceted; nuanced; vibrant; showcase; garner; bolster; interplay; seamless; notably; additionally; moreover; furthermore; ever-evolving; fast-paced; game-changer; cutting-edge; state-of-the-art; holistic; streamline; empower; transformative; groundbreaking; invaluable; paramount; utilize; embark; beacon; unlock; unleash; resonate; thrive; synergy; align with; boasts.

Hard only when figurative or beside other tells: navigate, landscape, robust, dynamic, leverage, enhance, elevate, foster, harness, comprehensive, facilitate. Each has an ordinary literal or trade sense, so the linter reports it as soft unless the use is the brochure one ("navigate the complexities of", "the AI landscape", "leverage our data", "foster a culture of") or another tell sits in the same sentence. Fixed collocations are never flagged: foster care, enhanced due diligence, leverage ratio, elevated blood pressure, test harness, dynamic programming, dynamic range, robust standard errors, landscape architect, navigate to. A literal or trade use the allowlist misses is cleared by leaving it.

Soft in every use (look, then keep or cut): journey (figurative); emphasizing; essential; highlight (as a verb for "show"); key (as an adjective: a key factor, a key insight); perfectly; significant(ly) (when it means "large"; statistically significant is not flagged); valuable.

Filler (cut outright; the linter reports it as soft because some uses carry meaning): very, really, truly, actually, basically, essentially, ultimately, genuinely, honestly, incredibly, extremely, highly, simply, just (as an intensifier), in order to, in terms of, a wide range of, a variety of, when it comes to, the fact that.

Replacement principle: the word a person would say aloud. "Use" for utilize. "Help" for facilitate. "Show" for showcase, highlight, underscore. "Big" or "large" for significant. "Important" is usually a sign the sentence should say why it matters instead.

## 3. Phrases

Openers: "In today's fast-paced world" (35 times the human rate), "In an increasingly...", "In the digital age", "In the ever-evolving landscape of", "In a world where", "As we navigate", "It's no secret that", "Whether you're a ... or a ...".

Editorial commentary: "It is important to note that", "It is worth noting", "crucial to note that" (22 times), "Notably,", "Importantly,", "Interestingly,", "It goes without saying", "Needless to say".

Significance framing: "plays a vital/crucial/key/significant/pivotal role", "stands as a testament to", "a testament to", "serves as a reminder", "marks a significant milestone", "cannot be overstated", "more important than ever", "now more than ever", "in an era of", "a new era", "rich cultural heritage", "enduring legacy", "a pivotal moment", "part of a broader movement", "highlights the importance of", "underscores the need for".

Summaries and closers: "In conclusion", "In summary", "To sum up", "Overall,", "Ultimately,", "At the end of the day", "The bottom line", "Key takeaways", "Moving forward", "As we look to the future".

Hinges and reveals: "Here's the thing", "Here's the truth", "Here's what you need to know" (11 times), "The result?", "The catch?", "Let's dive in", "Let's break it down", "Let's take a closer look", "Without further ado". "Deep dive" and "step-by-step" are soft: tells in most prose, but the ordinary name of a format or a set of instructions.

Email and assistant register: "I hope this email finds you well", "I am writing to provide/inform/follow up", "Please do not hesitate to", "Feel free to", "I'd be happy to" (5 times), "Great question", "You're touching on", "I hope this helps", "Let me know if you'd like", "Thank you for reaching out".

## 4. Punctuation and formatting

Em dashes: 10 times the human rate overall (humans about 2 to 5 per 10,000 words; OpenAI models about 45, Anthropic models about 32, Gemini 3 Pro about 3). Pew found em dashes on the web roughly doubled between 2023 and 2026. The spaced hyphen or en dash used as a dash is the same tell in disguise. The default is no dashes at all. Some people do write with them, so when the user supplies their own writing that uses dashes, keep dashes at the author's own rate: `lint.py --author-sample FILE` measures that rate and only flags the draft when it goes past it. An en dash between two numbers (2019–2021) is a range and is never flagged.

Markdown in plain-text contexts: 12 times the human rate (90 vs 8 per 10,000 words). Bold is 43 times, headers 23 times, inline code 5 times, italics 2 times. Humans typing into email clients, forum boxes and documents rarely mark up.

Bullet lists: 9 times the human rate (28 vs 3 per 10,000 words), often where prose would read more naturally. Where a person writes "apples, oranges and bananas", a model reaches for a line break and a dash.

Oxford commas: Pew found a 63% rise on the web since 2023; models use them more than people. Follow the author's own habit.

Unusual Unicode: 3 times the human rate (71 vs 28 per 10,000 words). Box-drawing ─ (940 times), ≈ (241 times), ⚠ (57 times), → (48 times). Such characters in otherwise ordinary prose can also signal a humanisation attempt. In technical writing with formulas, arrows and mathematical signs are notation; `--allow-markdown` leaves them alone.

Emoji: volume is only 2 times human, but the type differs. ✅ 167 times, keycap digits 61 to 129 times, 🚀 26 times, ❌ 24 times. 😊 and ❤️ skew human. Functional emoji (ticks, warnings, numbers) read as machine; emotional emoji read as a person.

Other formatting tells from the Wikipedia guide: title case in headings, bold-headed bullet points ("**Key point:** ..."), curly quotes pasted into contexts where people type straight ones, heavy headers on short pieces.

## 5. Rhetoric and structure

Triads (rule of three): 4 times the human rate (19 vs 5 per 10,000 words). "Innovative, transformative and groundbreaking"; "past, present and future"; "love, loss and identity". Human writers list three things when there are three things; models list three things by default.

Negative parallelism: "not just X but Y", "it's not about X, it's about Y", "this isn't X; it's Y", and the same move split over two sentences on one subject ("You're not sending more email. You're sending email that's harder to ignore."; "We don't sell software. We sell outcomes."), or hung on a cause ("not because X, but because Y"). Pangram counts the "not just X but Y" template at 3 times the human rate; Pew found negative parallelism nearly tripled on the web since 2023. Frequent LLM users name "it's not x, it's y" as the single most recognisable tell.

Aphorism formulas: one noun made the "language", "currency", "architecture", "operating system" or "lifeblood" of another ("Trust is the currency of remote teams"). Copula avoidance: "serves as", "stands as", "acts as" where "is" would do. Both read as a model reaching for weight.

Participial tails: a sentence that ends on a comma and an -ing phrase that comments on itself (", highlighting the importance of collaboration", ", ensuring a seamless experience", ", reflecting broader trends"). The Wikipedia guide calls this superficial analysis: the tail asserts significance without adding a fact.

Vague attribution: "experts believe", "critics argue", "industry observers note", "has been described as", "is widely regarded as". Human writers name who.

False ranges: "everything from X to Y", "ranging from X to Y" where the ends are not on a scale.

Hedged symmetry: "While X is true, Y", "On the one hand ... on the other hand", balanced both-sides sentences where the author holds one view. Stacked hedges: "may potentially", "could arguably", "to some extent".

Stock openers and summarising closers (section 3). A piece that opens by announcing the topic's importance and closes by restating itself was written by a model or by someone imitating one.

Over-signposting: "This note will first ... then ...", "In this article we explore", headers for every two paragraphs, "Key takeaways" boxes, and a heading followed by a line that says the heading again.

Connectives at paragraph and sentence openings: Moreover, Furthermore, Additionally, Consequently, Overall, In conclusion. The Wikipedia guide notes these give a formal, essay-like tone that does not match how people write for readers they know.

Uniform sentence shape: every sentence 15 to 25 words, subject then verb then object, each paragraph the same length. Fragment-for-punch ("Not anymore.") and self-answered questions ("The result? Fewer errors.") are the stylised exceptions models use to fake variation.

Equidistant voice: no first-person stake, no opinion stated as an opinion, no aside, no specific anecdote. Everything true in general and nothing true in particular. Description of what happened without why.

Too clean: no typos, no digressions, no sentence that goes nowhere. (Do not add errors to fix this. Add specifics instead.)

## 6. Chat artefacts

"Certainly! Here's" appeared 0 times in human text and 94 times in AI text per 10,000 words in Pangram's corpus. "Sure! Here's a" 18 times. "I'd be happy to help" 5 times. Also: knowledge-cutoff disclaimers ("As of my last update"), refusals ("As an AI language model"), placeholders in brackets ("[insert name]"), "I hope this helps", "Let me know if you need anything else", and a list of changes appended to a rewrite nobody asked to be annotated.

## 7. Content tells

Fabricated or mis-assigned citations: wrong case names, invented paragraph numbers, DOIs that resolve elsewhere, "retrieved" dates on sources that were never visited. Retraction Watch reported a roughly twelve-fold rise in fabricated references in PubMed-indexed literature over two years. Wherever sources get checked, this is the tell that ends careers; never alter a citation while humanising, and flag any that looks wrong.

Generic claims where specifics belong. Padding a subject's importance with minor mentions. Explaining what the reader already knows. Both-sides balance on a question the author has decided. Gap-filling speculation, which the Wikipedia guide singles out in biographies: "maintains a low profile", "keeps personal details private", "it is believed that", "likely grew up in". Say what is known and stop.

## 8. Watermarks (what style editing cannot touch)

Anthropic's help centre (August 2026) states that Claude models launched on or after 2 August 2026 weave an imperceptible statistical watermark into generated text; it lives in word choice, not hidden characters, travels with copy and paste, and may persist through some editing. Fable 5.1, Opus 5.5, Sonnet 5.5 and Haiku 5.5 are among the listed models. Detection is in private preview for regulators, law enforcement, media, fact-checkers, researchers, educational organisations and compliance-obligated enterprises, with wider access planned. Anthropic's own stated limits: a detected mark only means the text may have been processed by Claude (proofreading counts), not that Claude authored it; and text that has been heavily edited, paraphrased, translated or mixed into other writing, or that is very short, may carry no detectable mark. Google's SynthID-Text and OpenAI's planned marking work on the same principle.

This skill makes prose read as the author's. It does not and cannot remove a watermark from a draft generated by a model that marks its output, and it should never be described as doing so.

## 9. What human writing has that AI writing lacks

Specificity: the date, the amount, the name, the clause number, the thing that actually happened on Tuesday. One concrete detail does more than any amount of vocabulary scrubbing.

A stake: the writer wants something from the reader and says so. Emails end on the ask. Advice ends on the recommendation. Posts end on the point, not on "exciting times ahead".

Opinion as opinion: "I think the application fails" rather than "it could be argued that the application may face challenges".

Uneven rhythm: a long sentence that earns its length, then a short one. Sentences that start with "And" or "But" when that is how the thought arrived. A parenthesis where the writer would have lowered their voice.

Register that belongs to a trade: a lawyer's formal submission phrasing, a doctor's "unremarkable", a product manager's "ship". These are how the profession writes and are not tells. Keep them. Strip only the generic layer on top.

Omission: a person leaves out what the reader knows. A model explains everything to everyone.

The writer's own habits: the sign-off they always use, the word they overuse (if it is their word and not the model's), the one-line paragraph before the ask. Keep whatever the draft shows.

## 10. Sources

- Pangram, 9 Signs of AI Writing, Backed by Data: https://www.pangram.com/signs-of-ai-writing
- Pew Research Center, How Much of the Internet Is Written With AI? (20 Aug 2026): https://www.pewresearch.org/data-labs/2026/08/20/how-much-of-the-internet-is-written-with-ai/
- Wikipedia: Signs of AI writing (WikiProject AI Cleanup): https://en.wikipedia.org/wiki/Wikipedia:Signs_of_AI_writing
- People who frequently use ChatGPT for writing tasks are accurate and robust detectors of AI-generated text (ACL 2025): https://arxiv.org/abs/2501.15654
- Delving into ChatGPT usage in academic writing through excess vocabulary: https://arxiv.org/abs/2406.07016
- Why Does ChatGPT "Delve" So Much?: https://arxiv.org/abs/2412.11385
- Spotting LLMs With Binoculars: https://arxiv.org/abs/2401.12070
- Anthropic, How Claude marks AI-generated content: https://support.claude.com/en/articles/16266773-how-claude-marks-ai-generated-content
- CASRAI, How AI detection actually works: https://casrai.org/guides/how-ai-detection-actually-works
