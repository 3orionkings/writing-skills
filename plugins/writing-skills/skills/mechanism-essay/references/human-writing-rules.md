# Human-writing rules (the humanizer, condensed)

This style skill sits on top of the humanizer skill. If the humanizer is listed in the session, load it first and follow its rules and its linter. The rules below are the same rules in condensed form, so the style skill still holds when the humanizer is not available. The style skill adds a structure and a set of moves; it relaxes these rules only where its own "Departures from the humanizer" section says so, and only in the ways that section names.

## What the rules protect

Readers who spot machine writing go by vocabulary first, then by formality without a stake, clarity without specificity, and rhythm without variation. Every rule here removes one of those signals. A text that keeps the author's specifics, opinions and odd sentences reads as a person; a text that only swaps out tell-words does not.

## Punctuation

No em dashes or en dashes by default, and no spaced hyphen doing a dash's job. Use a comma, a full stop or brackets. When the user supplies writing of their own that uses dashes, keep them at the author's rate and no higher: lint with `--author-sample FILE` pointing at that writing. A dash between two numbers (2019–2021) is a range, not a dash. Hyphens only inside compound words. A colon before a list or a quotation is fine; a colon as a rhetorical hinge is not. Semicolons sparingly. Exclamation marks only where the author uses them.

## Vocabulary

Replace tell-words with the plain word a person would say. The full list is in `scripts/lint.py`, the single source for every skill in this set; `python3 scripts/lint.py --list` prints it by severity. The commonest: delve, tapestry, realm, testament, underscore, pivotal, crucial, intricate, multifaceted, nuanced, vibrant, showcase, seamless, holistic, transformative, utilize, moreover, furthermore, additionally. Words with a literal or trade sense (navigate, robust, dynamic, leverage, enhance, elevate, foster, harness, landscape, comprehensive, facilitate) are tells only in their brochure sense ("navigate the complexities", "the AI landscape"); foster care, a test harness and dynamic programming are just words. Cut filler where it pads (very, really, truly, actually, basically, essentially, ultimately, genuinely, honestly, simply, just as an intensifier, in order to) and keep it where it is how the author talks: a text scrubbed of every qualifier reads as more machine-like, not less. Cut "it is important to note" and "it is worth noting" outright.

## Sentence shape

Vary length on purpose: a sentence with a subordinate clause, then one of five words. Start consecutive sentences on different words and subjects. No groups of three for rhythm's sake. No "not just X but Y", no "it's not about X, it's about Y", and no two-sentence version of it ("You're not X. You're Y."). No "not because X, but because Y". No fragment for punch, no question the writer answers at once, no participial tail (", highlighting the importance of"), no "while X, Y" balance where the author means one side, no "everything from X to Y". No formula that makes one noun the "currency" or "language" of another; "is" instead of "serves as".

## Emphasis instead of content

Current models lean on these more than on any other tell; fix them the first time they appear. No pause-for-effect closer that repeats the paragraph or tells the reader to stop and absorb it ("Let that sink in.", "That's the whole point.", "That matters."), and no line that names what an example just showed ("It was a lesson in patience."). No throat-clearing opener ("Here's the thing", "Real talk:", "Honestly? It depends."). No faux-profound saying ("The real question is", "What really matters is"). No rebutting an objection nobody made, or ruling out an option nobody proposed ("I'm not saying", "Don't get me wrong", "A tempting approach would be"). No split or clipped contrast ("This does not mean X. It means Y.", "no X, no Y, just Z", ", no guessing."). No corrective hedge that recasts a source ("should be read as X rather than Y"). No notability padding (lists of outlets, "an active social media presence"), no "associated with" where the relationship is known, no stock "challenges and future outlook" close, and no sentence about how the text was made or what it replaced.

## Structure inside prose

Paragraphs break where the thought turns, never open on a connective (Moreover, Furthermore, Additionally, Consequently, Overall, In conclusion, In summary). Fold transitions into the syntax with and, but, so, which, because, or drop them. No opener announcing the topic's importance, no signposting of the "this piece will first" kind, no closing summary, no line about the future, and no heading followed by a line that says the heading again. End on the last substantive point or on the ask.

The style skill's own template governs headings, numbered sections, lists, callouts, footnotes and figures. Where the template calls for a heading or a list, use it; where it does not, write prose. A list is for parallel items the reader will scan, never a substitute for an argument.

## Tone

Match the author, not a neutral professional register. Keep first person where the author uses it, opinions stated as opinions, humour if present. A first-person stake is the strongest human signal there is; use only what the user has supplied about their experience and never invent a fact. Never reuse an example's specifics: the examples in a style skill show a move, not content, so every number, name, event, analogy and quotation in the piece comes from the user's material. Do not fill a gap with speculation ("is believed to", "likely grew up"). No cheerful-assistant framing ("I hope this finds you well", "I'd be happy to", "Great question"). No stacked hedges ("may potentially"); state the position, then the one qualification. No significance framing ("plays a vital role", "cannot be overstated", "a testament to").

## Characters

No emoji, no symbols such as ticks or warning signs, no decorative Unicode. Arrows and mathematical signs belong only in formulas and technical notation. Typographic quotes are fine if the draft uses them.

## Delivery

Return the piece only, in the medium asked for. No preamble, no "here's the draft", no list of changes, no closing offer. The one permitted note is a citation or source that looks wrong: one line above the piece, never after it. Run the linter on the finished text with `python3 scripts/lint.py draft.md --allow-markdown` (the flag makes the form's own headings, bold and lists soft and leaves mathematical notation alone; every sentence-level check stays as it is), adding `--author-sample FILE` when the user's own writing uses dashes. Before linting, compare the piece with the user's material for any name, number, date, quotation or claim that was lost or altered. Fix every hard finding, look at each soft one, and never clear a flag by swapping in another tell or an odd synonym. A hard finding on a literal or trade term is cleared by leaving the term as it is. Then run `python3 scripts/style_check.py draft.md` for the form's structure, with `--variant NAME` when the skill's workflow names a format other than its default.

## What none of this does

Style editing changes how text reads, not where it came from. Text generated by some current models, Claude models released since August 2026 among them, carries a statistical watermark that these rules do not remove. Never claim or imply a draft is undetectable.
