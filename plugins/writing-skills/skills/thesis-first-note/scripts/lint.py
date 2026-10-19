#!/usr/bin/env python3
"""Flag the patterns that AI detectors and experienced readers use to spot machine-written prose.

Usage:
    python3 lint.py FILE            human-readable report
    python3 lint.py FILE --json     machine-readable report
    cat draft.txt | python3 lint.py -
    python3 lint.py FILE --allow-markdown   treat headings, bold, lists and quotes as soft, and leave
                                            maths and arrow symbols (<= ~ ->) alone (for forms that use them)
    python3 lint.py FILE --author-sample MINE.txt   dashes become soft while the draft stays at or under
                                                    the dash rate of the author's own writing in MINE.txt
    python3 lint.py FILE --max-dashes-per-1000 N    the same, with the author's rate given directly
    python3 lint.py --list          print every word and phrase the linter knows, by severity

Exit status: 0 when there are no hard findings, 1 when there are, 2 on a usage error.

Hard findings are patterns the author has ruled out entirely: dashes used as punctuation,
tell vocabulary and phrases, markdown and bullets, chatbot framing, negative parallelism,
emoji and symbols, connective openers, significance framing.
Soft findings need a human look: triads, participial tails, hedges, uniform sentence
length, repeated sentence openings, self-answered questions, fragments for punch,
context-dependent words, aphorism formulas, copula avoidance, gap-filling speculation,
a heading restated in the line below it.

Words with a literal or trade sense (navigate, robust, dynamic, leverage, enhance, elevate,
foster, harness, landscape, comprehensive, facilitate) are soft unless the use is figurative
or the sentence carries other tells. Fixed collocations (foster care, test harness, dynamic
programming and the rest of ALLOWLIST) are never flagged. A hard finding on a literal or
trade term that the list misses is cleared by leaving the term as it is.

This file is the single source of the tell vocabulary. The skills' prose names examples;
run --list for the full set.

Standard library only. Python 3.8 or later.
"""

import json
import re
import statistics
import sys

HARD = "hard"
SOFT = "soft"

# ---------------------------------------------------------------------------
# Word and phrase lists. Patterns are regular expressions, matched case-insensitively.
# ---------------------------------------------------------------------------

# Hard in every use.
TELL_WORDS = [
    r"delv(?:e|es|ed|ing)", r"tapestr(?:y|ies)", r"realms?", r"testament",
    r"underscor(?:e|es|ed|ing)", r"pivotal", r"crucial(?:ly)?", r"intricate(?:ly)?",
    r"meticulous(?:ly)?", r"multifaceted", r"nuanced", r"vibrant", r"showcas(?:e|es|ed|ing)",
    r"garner(?:s|ed|ing)?", r"bolster(?:s|ed|ing)?", r"interplay", r"seamless(?:ly)?",
    r"notably", r"additionally", r"moreover", r"furthermore",
    r"ever-evolving", r"fast-paced", r"game-?chang(?:er|ers|ing)", r"cutting-edge",
    r"state-of-the-art", r"holistic(?:ally)?", r"streamlin(?:e|es|ed|ing)", r"empower(?:s|ed|ing|ment)?",
    r"transformative", r"groundbreaking", r"invaluable", r"paramount",
    r"utiliz(?:e|es|ed|ing|ation)", r"embark(?:s|ed|ing)?",
    r"beacons?", r"unlock(?:s|ed|ing)?", r"unleash(?:es|ed|ing)?", r"resonat(?:e|es|ed|ing)",
    r"synerg(?:y|ies|istic)", r"thrive", r"thriving", r"boasts?", r"aligns? with",
]

# Words with a literal or trade sense. Soft by default; hard when the use is figurative
# (the pattern after or before the word matches) or when another tell sits in the same sentence.
_DET = r"(?:(?:the|a|an|our|your|their|its|this|these|those|my|his|her|overall|greater|deeper|stronger|meaningful|genuine|user|customer|employee|team)\s+)*"
POLYSEMOUS = {
    "navigate": (
        r"navigat(?:e|es|ed|ing)",
        r"^\s+" + _DET + r"(?:[\w-]+\s+){0,2}?(?:complexit\w*|challeng\w*|uncertaint\w*|landscapes?|world|waters|journey|changes?|"
        r"transitions?|ambiguit\w*|terrain|maze|nuances?|realit\w*|difficult\w*|tensions?|pressures?|demands?|"
        r"cris[ie]s|future|intricac\w*|careers?|relationships?|politics|bureaucracy|ecosystems?|life|lives)\b",
        None,
    ),
    "landscape": (
        r"landscapes?",
        r"^\s+of\b",
        r"\b(?:competitive|regulatory|digital|business|political|media|tech|technology|technological|ai|startup|"
        r"market|security|threat|funding|investment|legal|economic|cultural|social|global|evolving|changing|"
        r"shifting|current|modern|today'?s|ever-changing|information|policy|healthcare|education(?:al)?|research|"
        r"vendor|product|software|data|retail|financial|career|job|talent|hiring|innovation|enterprise|consumer|"
        r"creator|saas|crypto|geopolitical|communications?)\s+$",
    ),
    "robust": (
        r"robust(?:ly|ness)?",
        r"^\s+(?:and\s+[\w-]+\s+)?(?:frameworks?|solutions?|approach(?:es)?|strateg(?:y|ies)|ecosystems?|communit(?:y|ies)|"
        r"discussions?|debates?|foundations?|understanding|support|partnerships?|set of|range of|suite|portfolio|"
        r"economy|growth|culture|dialogue|engagement|presence|offerings?|programmes?|programs?|toolkit|platforms?)\b",
        None,
    ),
    "dynamic": (
        r"dynamic",
        r"^\s+(?:and\s+[\w-]+\s+)?(?:world|environments?|landscapes?|teams?|cultures?|ecosystems?|markets?|industr(?:y|ies)|"
        r"field|space|nature|interplay|leaders?|personalit(?:y|ies)|individuals?|duo|professionals?|approach|"
        r"solutions?|experiences?|era|times|forces?|energy|communit(?:y|ies)|city|careers?|workplaces?|"
        r"organi[sz]ations?|compan(?:y|ies)|startups?|business(?:es)?)\b",
        r"\b(?:fast-paced|ever-changing|vibrant|exciting|innovative)\s+(?:and\s+)?$",
    ),
    "leverage": (
        r"leverag(?:e|es|ed|ing)",
        r"^\s+(?:the|our|your|their|its|this|these|those|existing|cutting-edge|advanced|modern|new|ai|data|"
        r"technolog(?:y|ies)|insights?|expertise|strengths?|power|capabilit\w*|resources|synerg\w*|tools?|platforms?)\b",
        r"\b(?:to|can|could|will|should|must|we|you|they|i|help(?:s|ed)?\s+\w+\s+to)\s+$",
    ),
    "enhance": (
        r"enhanc(?:e|es|ed|ing|ement|ements)",
        r"^\s+" + _DET + r"(?:experiences?|engagement|productivity|efficiency|capabilit\w*|understanding|collaboration|"
        r"communication|quality|performance|value|outcomes?|visibility|security|creativity|well-?being|skills?|"
        r"satisfaction|effectiveness|functionality|accessibility|reputation|presence|learning|innovation|growth|"
        r"decision-making|operations?|workflows?|processes|relationships?|trust|retention|offerings?|journey)\b",
        r"\b(?:further|greatly|ultimately|truly)\s+$",
    ),
    "elevate": (
        r"elevat(?:e|es|ed|ing)",
        r"^\s+" + _DET + r"(?:[\w-]+\s+)?(?:experiences?|game|brand|conversations?|discourse|standards?|work|careers?|"
        r"teams?|business|style|content|skills?|performance|quality|presence|voice|craft|profile|status|products?|"
        r"offerings?)\b|^\s+[\w\s]{0,40}?to new heights",
        None,
    ),
    "foster": (
        r"foster(?:s|ed|ing)?",
        r"^\s+" + _DET + r"(?:sense|cultures?|environments?|collaboration|innovation|growth|communit(?:y|ies)|"
        r"connections?|relationships?|trust|creativity|engagement|inclusion|inclusivity|inclusiveness|dialogue|"
        r"understanding|belonging|teamwork|learning|partnerships?|transparency|accountability|cooperation|"
        r"ownership|curiosity|loyalty|goodwill|diversity|resilience|empathy|open)\b",
        None,
    ),
    "harness": (
        r"harness(?:es|ed|ing)?",
        r"^\s+(?:the\s+(?:full\s+)?(?:power|potential|energy|capabilit\w*|strengths?)|(?:ai|data|technology|innovation|"
        r"insights?|creativity|talent|momentum|collective))\b",
        None,
    ),
    "comprehensive": (
        r"comprehensive(?:ly)?",
        r"^\s+(?:guides?|overviews?|approach|understanding|solutions?|suite|strateg(?:y|ies)|frameworks?|look|range|"
        r"platforms?|resources?|toolkit|roadmap|ecosystem|set of|array|exploration|breakdown|deep dive)\b",
        None,
    ),
    "facilitate": (
        r"facilitat(?:e|es|ed|ing)",
        r"^\s+(?:(?:a|an|the|more)\s+)?(?:seamless|smooth(?:er)?|growth|collaboration|communication|innovation|"
        r"learning|understanding|discussions?|dialogue|engagement|connections?|transitions?|adoption|knowledge|"
        r"meaningful|better|greater|deeper|informed)\b",
        None,
    ),
}

# Context-dependent words from the catalogue: always soft, and they count towards a cluster.
CONTEXT_WORDS = [
    r"journeys?", r"emphasi[sz](?:e|es|ed|ing)", r"essential(?:ly)?", r"highlight(?:s|ed|ing)?",
    r"perfectly", r"significant(?:ly)?", r"valuable",
    r"key(?=\s+(?:takeaways?|insights?|factors?|roles?|components?|elements?|aspects?|players?|drivers?|features?|"
    r"considerations?|benefits?|challenges?|steps?|parts?|questions?|differences?|lessons?|points?|areas?|themes?|"
    r"trends?|principles?|priorit(?:y|ies)|metrics?|stakeholders?|success|ingredients?|pillars?|learnings?|"
    r"findings?|strengths?|issues?|concepts?|skills?|capabilit(?:y|ies)|moments?|milestones?)\b)",
]

# Fixed collocations with a literal or trade sense. Never flagged.
ALLOWLIST = [
    r"foster (?:care|parents?|homes?|famil(?:y|ies)|child(?:ren)?|carers?|placements?)",
    r"enhanced due diligence",
    r"leverage ratios?",
    r"elevated (?:blood pressure|heart rate|temperature)",
    r"test harness(?:es)?",
    r"dynamic programming",
    r"dynamic range",
    r"robust standard errors?",
    r"landscape architect(?:s|ure)?",
    r"navigat(?:e|es|ed|ing) to",
    r"statistically significant",
    r"significant (?:digits|figures)",
]

FILLER_WORDS = [
    r"very", r"really", r"truly", r"actually", r"basically", r"essentially", r"ultimately",
    r"genuinely", r"honestly", r"incredibly", r"extremely", r"highly", r"simply", r"just",
    r"in order to", r"in terms of", r"a wide range of", r"a variety of", r"when it comes to",
    r"the fact that",
]

TELL_PHRASES = [
    r"it(?:'s| is) (?:important|worth|crucial|essential|vital) to (?:note|mention|remember|understand)(?: that)?",
    r"(?:it(?:'s| is) )?worth noting", r"it(?:'s| is) no secret",
    r"in today'?s", r"in an increasingly", r"in the digital age", r"in the ever-?evolving",
    r"in a world where", r"as we navigate", r"whether you(?:'re| are) an?\b",
    r"plays? an? (?:vital|crucial|key|significant|important|pivotal|central|essential) role",
    r"stands? as a testament", r"a testament to", r"serves? as a reminder",
    r"marks? an? (?:significant|pivotal|important|major) (?:milestone|moment|step|shift)",
    r"cannot be overstated", r"more important than ever", r"now more than ever",
    r"in an era of", r"a new era", r"rich cultural heritage", r"enduring legacy",
    r"a pivotal moment", r"broader movement", r"highlights? the importance",
    r"underscores? the (?:need|importance)",
    r"in conclusion", r"in summary", r"to sum up", r"to summari[sz]e", r"at the end of the day",
    r"the bottom line", r"key takeaways?", r"moving forward", r"as we look to the future",
    r"here'?s the thing", r"here'?s the truth", r"here'?s what you need to know",
    r"the result\?", r"the catch\?", r"the upshot\?", r"the takeaway\?", r"the answer\?",
    r"let'?s (?:dive|break|explore|take a|unpack|get)", r"without further ado",
    r"i hope this (?:email|message|note|letter) finds you well", r"i hope (?:this|that) helps",
    r"i am writing to (?:provide|inform|follow up|let you know|express|share)",
    r"please (?:do not|don'?t) hesitate", r"feel free to", r"i(?:'d| would) be happy to",
    r"great question", r"you(?:'re| are) touching on", r"thank you for reaching out",
    r"let me know if you(?:'d| would)? ?(?:like|need|want|have)",
    r"as an ai", r"as of my last", r"knowledge cutoff", r"i hope you(?:'re| are) doing well",
    r"exciting (?:news|times)", r"thrilled to", r"excited to (?:announce|share)",
    r"look no further", r"the world of", r"effortlessly",
    r"game[- ]?changer", r"a must-(?:read|have|visit)", r"in the realm of",
]

# Phrases that are tells in most prose but ordinary in some: review, do not auto-fix.
SOFT_PHRASES = [
    (r"deep[- ]dives?", "often a tell; fine as the name of a format"),
    (r"step[- ]by[- ]step", "often a tell; fine for instructions"),
    (r"everything from\b[^.?!]{1,60}?\bto\b", "false range: everything from X to Y"),
    (r"ranging from\b[^.?!]{1,60}?\bto\b", "false range: ranging from X to Y"),
    (r"experts (?:believe|say|agree|suggest)", "vague attribution: name who"),
    (r"(?:industry )?observers (?:note|say|believe)", "vague attribution: name who"),
    (r"(?:has|have) been described as", "vague attribution: name who"),
    (r"(?:is|are) widely (?:regarded|considered|seen|viewed) as", "vague attribution: name who"),
    (r"on the one hand", "hedged symmetry"),
]

CONNECTIVES_HARD = [
    r"moreover", r"furthermore", r"additionally", r"in addition", r"consequently",
    r"overall", r"in conclusion", r"in summary", r"to summari[sz]e", r"to sum up", r"ultimately",
    r"notably", r"importantly", r"crucially", r"interestingly", r"firstly", r"secondly", r"thirdly",
    r"lastly", r"on the other hand", r"that (?:being )?said", r"in essence", r"at its core",
    r"needless to say", r"it goes without saying",
]

CONNECTIVES_SOFT = [r"however", r"therefore", r"thus", r"hence", r"accordingly", r"nevertheless", r"nonetheless"]

HEDGES = [
    r"may potentially", r"could potentially", r"might potentially", r"could possibly", r"may possibly",
    r"might perhaps", r"it could be argued", r"arguably", r"to some extent", r"in some ways",
    r"somewhat", r"it seems that", r"it appears that", r"it is possible that", r"potentially", r"possibly",
    r"it may be the case", r"in many ways",
]

SIGNPOSTS = [
    r"this (?:section|article|post|note|letter|essay|piece|email|memo|guide) (?:will|explores|examines|outlines|discusses|covers|aims)",
    r"in what follows", r"in this (?:article|post|piece|guide|section)", r"first and foremost",
    r"below,? (?:i|we) (?:will|set out|outline|explain)",
]

# Speculation that fills a gap in what is known about a subject.
GAP_FILLING = [
    r"maintains? a (?:relatively |very )?low (?:public )?profile",
    r"keeps? (?:(?:his|her|their|its)\s+)?(?:personal |private )?(?:details|life|information|matters) (?:private|out of the public eye|under wraps)",
    r"(?:it is|it's|it was) (?:widely )?(?:believed|thought|said|rumou?red|understood|assumed|presumed) that",
    r"(?:likely|probably|presumably|possibly) (?:grew up|was born|attended|studied|spent (?:his|her|their) (?:early|childhood))",
    r"little is (?:publicly )?known about",
    r"details (?:about|of) (?:his|her|their) (?:early|personal|private) life (?:are|remain) (?:scarce|limited|unclear|unknown)",
]

APHORISM = re.compile(
    r"\b(?:is|are|was|were|becomes?|became|remains?)\s+(?:the|a)\s+(?:new\s+|real\s+|true\s+)?"
    r"(?:language|currency|architecture|grammar|operating system|lingua franca|oxygen|lifeblood|backbone|bedrock|"
    r"cornerstone|heartbeat|dna|fabric|north star|soul|glue|secret sauce|engine)\s+of\b"
    r"|\b(?:is|are)\s+the\s+new\s+(?:oil|gold|electricity|black|currency)\b",
    re.I,
)
COPULA_AVOIDANCE = re.compile(
    r"\b(?:serv(?:e|es|ed|ing)|stand(?:s|ing)?|stood|act(?:s|ed|ing)?|function(?:s|ed|ing)?)\s+as\s+"
    r"(?:a|an|the|our|their|its|his|her|my|your)\b",
    re.I,
)
NOT_BECAUSE = re.compile(
    r"\bnot because\b[^.?!]{1,100}?\bbut because\b|\bnot because\b[^.?!]{1,100}[.?!;]\s+(?:but\s+)?because\b",
    re.I,
)

CHATBOT_FIRST_LINE = re.compile(
    r"^\s*(?:sure|certainly|absolutely|of course|great|got it|understood|here(?:'s| is| are)|below is|"
    r"i(?:'ve| have) (?:rewritten|revised|updated|humani[sz]ed|edited)|(?:rewritten|revised|humani[sz]ed|edited) (?:version|draft|text)|"
    r"this version|the following)\b",
    re.I,
)
CHATBOT_LAST_PARA = re.compile(
    r"^\s*(?:i hope this helps|let me know if|feel free to|please (?:do not|don'?t) hesitate|would you like me to|"
    r"if you(?:'d| would) like|happy to (?:adjust|revise|tweak)|changes (?:made|i made)|what (?:i )?changed|note:)",
    re.I,
)

NEG_PARALLEL_SAME_SENTENCE = [
    r"\bnot (?:just|only|merely|simply|solely)\b[^.;:?!]{1,90}?\b(?:but|rather)\b",
    r"\b(?:it|this|that|which|he|she|they|we|you)\s*(?:is|'s|was|are|'re|were)\s*(?:n't|not)\b(?: about)?[^.;?!]{1,80}?[,;]\s*(?:it|this|that|they|we|you)\s*(?:is|'s|was|are|'re|were)\b",
    r"\bisn'?t (?:just|only|about|merely)\b[^.;?!]{1,80}?\b(?:it'?s|but|rather)\b",
    r"\b(?:less|more) about\b[^.;?!]{1,60}?\b(?:and|than) (?:more|less) about\b",
    r"\bnot (?:a|an|the)\b[^.;?!]{1,40}?,\s*(?:but|rather)\s(?:a|an|the)\b",
]
NEG_PARALLEL_ACROSS = re.compile(
    r"\b(?:isn'?t|is not|aren'?t|are not|wasn'?t|was not|not)\s(?:just |only |merely |simply |about )?[^.?!]{1,60}[.?!]\s+"
    r"(?:It|That|This|They)(?:'s| is| are|'re)\b",
)
# "You're not sending more email. You're sending email that's harder to ignore." The second
# sentence opens on the same pronoun the negated first sentence did.
NEG_PARALLEL_SAME_SUBJECT = re.compile(
    r"\b(i|you|we|they|he|she|it|this|that)"
    r"(?:'re|'m|'s|\s+(?:are|am|is|was|were|do|does|did|can|could|will|would|should|have|has|had)|\s+(?:ca|wo)(?=n't))?"
    r"(?:n't|\s+not|\s+never)\b[^.?!]{1,80}[.?!]\s+\1(?:'re|'m|'s)?\s",
    re.I,
)

TRIAD = re.compile(
    r"\b([A-Za-z][A-Za-z'-]*(?: [A-Za-z][A-Za-z'-]*)?), ([A-Za-z][A-Za-z'-]*(?: [A-Za-z][A-Za-z'-]*)?),? (?:and|or) ([A-Za-z][A-Za-z'-]*(?: [A-Za-z][A-Za-z'-]*)?)\b"
)

DASH = re.compile(r"[—–―]|(?<=\w)\s+-\s+(?=\w)|(?<=\w)--(?=\w)|(?<=\w)\s--\s(?=\w)")

MARKDOWN_LINE = re.compile(r"^\s*(?:#{1,6}\s|[-*+]\s|•\s|>\s|\|.*\||---+\s*$|\*\*\*+\s*$)")
MARKDOWN_INLINE = re.compile(r"\*\*[^*]+\*\*|__[^_]+__|`[^`]+`")
NUMBERED_LINE = re.compile(r"^\s*\d+[.)]\s")
HEADING_LINE = re.compile(r"^\s{0,3}#{1,6}\s+(.*)$")

SYMBOL_RANGES = [
    (0x2190, 0x21FF), (0x2200, 0x22FF), (0x2300, 0x23FF), (0x2460, 0x24FF), (0x2500, 0x259F),
    (0x25A0, 0x25FF), (0x2600, 0x27BF), (0x2900, 0x297F), (0x2B00, 0x2BFF),
    (0x1F000, 0x1FAFF), (0x20E3, 0x20E3), (0xFE0F, 0xFE0F),
]
# Arrows and mathematical operators: ordinary notation in forms that use markdown and maths.
MATH_RANGES = [(0x2190, 0x21FF), (0x2200, 0x22FF), (0x2308, 0x230B), (0x27F0, 0x27FF), (0x2900, 0x297F)]

OBJECT_PRONOUNS = {"it", "them", "this", "that", "me", "you", "us", "him", "her", "these", "those"}

PARTICIPLE_STOP = {
    "including", "according", "during", "following", "regarding", "concerning", "notwithstanding",
    "pending", "excluding", "barring", "considering", "depending", "owing", "morning", "evening",
    "thing", "something", "nothing", "anything", "everything", "king", "ring", "string", "wing",
    "spring", "bring", "sing", "meaning", "being", "building", "hearing", "filing", "pleading",
    "ruling", "finding", "proceeding", "wedding", "meeting", "writing", "reading", "drawing",
    "painting", "opening", "closing", "ending", "beginning", "warning", "training", "funding",
    "housing", "sitting", "standing", "understanding", "setting", "nothing", "failing", "saving",
    "undertaking", "holding", "listing", "briefing", "timing", "using", "having", "pursuing",
}
PARTICIPLE_TAIL = re.compile(r",\s+([A-Za-z]+ing)\b[^.!?]{3,}[.!?]\s*$")

FRAGMENT_PUNCH = re.compile(r"(?:^|(?<=[.!?]\s))(?:Not|No|Never|Always|Until now|Not anymore|Every single [A-Za-z]+)\b[^.!?]{0,30}\.")
SELF_QUESTION = re.compile(r"(?:^|(?<=[.!?]\s))(?:The|Our|My|Their|Your|His|Her) [A-Za-z]+\?|(?:^|(?<=[.!?]\s))(?:Why|How|So what|What next|And then)\?")

ABBREVIATIONS = [
    "Mr", "Mrs", "Ms", "Dr", "Prof", "Hon", "Rev", "St", "No", "Nos", "para", "paras", "r", "rr", "O", "s",
    "ss", "v", "vs", "Cap", "cl", "cf", "e.g", "i.e", "etc", "Ltd", "Inc", "Co", "Corp", "Pty", "plc",
    "Jan", "Feb", "Mar", "Apr", "Jun", "Jul", "Aug", "Sep", "Sept", "Oct", "Nov", "Dec", "approx", "vol",
    "p", "pp", "ed", "eds", "ch", "art", "arts", "sch", "reg", "regs", "ord", "al", "QC", "SC", "KC", "J", "JA",
]

STOPWORDS = {
    "the", "a", "an", "and", "or", "but", "of", "to", "in", "on", "for", "with", "is", "are", "was", "were",
    "be", "it", "its", "this", "that", "these", "those", "why", "how", "what", "when", "not", "no", "your",
    "you", "our", "we", "they", "their", "more", "most", "than", "as", "at", "by", "from", "into", "about",
    "do", "does", "don't", "can", "will", "should", "must", "have", "has", "one", "all", "every", "so",
}


def compile_list(patterns):
    return re.compile(r"(?<![\w-])(?:" + "|".join(patterns) + r")(?![\w-])", re.I)


RX_TELL = compile_list(TELL_WORDS)
RX_POLY = {name: (compile_list([pat]), re.compile(post, re.I) if post else None, re.compile(pre, re.I) if pre else None)
           for name, (pat, post, pre) in POLYSEMOUS.items()}
RX_CONTEXT = compile_list(CONTEXT_WORDS)
RX_ALLOW = compile_list(ALLOWLIST)
RX_FILLER = compile_list(FILLER_WORDS)
RX_PHRASE = compile_list(TELL_PHRASES)
RX_SOFT_PHRASES = [(compile_list([p]), note) for p, note in SOFT_PHRASES]
RX_HEDGE = compile_list(HEDGES)
RX_SIGNPOST = compile_list(SIGNPOSTS)
RX_GAP = compile_list(GAP_FILLING)
RX_CONN_HARD = re.compile(r"^\s*(?:" + "|".join(CONNECTIVES_HARD) + r")\b[,\s]", re.I)
RX_CONN_SOFT = re.compile(r"^\s*(?:" + "|".join(CONNECTIVES_SOFT) + r")\b[,\s]", re.I)
RX_NEG_SAME = [re.compile(p, re.I) for p in NEG_PARALLEL_SAME_SENTENCE]
SENTENCE_END = re.compile(r"[.!?]+[\"'”’)\]]*\s+")

# ---------------------------------------------------------------------------


def is_symbol(ch, allow_math=False):
    cp = ord(ch)
    if allow_math and any(lo <= cp <= hi for lo, hi in MATH_RANGES):
        return False
    return any(lo <= cp <= hi for lo, hi in SYMBOL_RANGES)


def split_sentences(paragraph):
    """Rough sentence splitter that protects common abbreviations and decimals."""
    text = paragraph
    for ab in ABBREVIATIONS:
        text = re.sub(r"\b" + re.escape(ab) + r"\.", lambda m, ab=ab: ab.replace(".", "\x00") + "\x00", text)
    text = re.sub(r"(\d)\.(\d)", lambda m: m.group(1) + "\x00" + m.group(2), text)
    parts = re.split(r"(?<=[.!?])[\"'”’)]?\s+(?=[\"'“‘(]?[A-Z0-9])", text)
    return [p.replace("\x00", ".").strip() for p in parts if p.strip()]


def context(line, start, end, width=38):
    a = max(0, start - width)
    b = min(len(line), end + width)
    snippet = line[a:b].replace("\n", " ")
    return ("..." if a > 0 else "") + snippet + ("..." if b < len(line) else "")


def overlaps(span, spans):
    return any(span[0] < e and s < span[1] for s, e in spans)


def sentence_spans(line):
    spans, start = [], 0
    for m in SENTENCE_END.finditer(line):
        spans.append((start, m.end()))
        start = m.end()
    spans.append((start, len(line)))
    return spans


def dash_matches(line):
    """Dashes used as punctuation. A dash or hyphen between two digits (2019–2021, 5 - 3) is a range or a sign."""
    out = []
    for m in DASH.finditer(line):
        if m.group(0) not in ("—", "―"):
            if line[:m.start()].rstrip()[-1:].isdigit() and line[m.end():].lstrip()[:1].isdigit():
                continue
        out.append(m)
    return out


def word_count(text):
    return len(re.findall(r"[A-Za-z0-9'’-]+", text))


def dash_rate(text):
    """Dashes per 1,000 words, counted the way the linter counts them."""
    n = sum(len(dash_matches(line)) for line in text.splitlines())
    words = word_count(text)
    return (n * 1000.0 / words if words else 0.0), n, words


def content_words(s):
    return {w.lower().rstrip("s") for w in re.findall(r"[A-Za-z][A-Za-z'’-]+", s)
            if w.lower() not in STOPWORDS and len(w) > 2}


def lint(text, allow_markdown=False, dash_allowance=None):
    """dash_allowance: the author's own dashes per 1,000 words, or None to rule dashes out."""
    findings = []
    md_sev = SOFT if allow_markdown else HARD
    dash_sev = HARD if dash_allowance is None else SOFT
    lines = text.splitlines()

    def add(category, severity, lineno, matched, note=""):
        findings.append({
            "category": category, "severity": severity, "line": lineno,
            "match": matched, "note": note,
        })

    # Line-level checks --------------------------------------------------
    numbered_run = 0
    dash_total = 0
    for i, line in enumerate(lines, 1):
        for m in dash_matches(line):
            dash_total += 1
            add("dash", dash_sev, i, context(line, m.start(), m.end()), "em/en dash or spaced hyphen used as a dash")
        if MARKDOWN_LINE.match(line):
            add("markdown", md_sev, i, context(line, 0, min(len(line), 60)), "heading, bullet, quote, rule or table")
        for m in MARKDOWN_INLINE.finditer(line):
            add("markdown", md_sev, i, context(line, m.start(), m.end()), "bold, underline or code markup")
        if NUMBERED_LINE.match(line):
            numbered_run += 1
            if numbered_run == 2:
                add("markdown", md_sev, i, context(line, 0, min(len(line), 60)), "numbered list")
        elif line.strip():
            numbered_run = 0
        for m in re.finditer(r"[•◦▪■‣]", line):
            add("markdown", md_sev, i, context(line, m.start(), m.end()), "bullet character")
        for j, ch in enumerate(line):
            if is_symbol(ch, allow_math=allow_markdown):
                add("symbol", HARD, i, context(line, j, j + 1), "emoji or symbol U+%04X" % ord(ch))

        # Vocabulary: fixed collocations are skipped; context-dependent words escalate when
        # figurative or when another tell sits in the same sentence.
        allow = [m.span() for m in RX_ALLOW.finditer(line)]
        phrases = [m for m in RX_PHRASE.finditer(line)]
        phrase_spans = [m.span() for m in phrases]
        tells = [m for m in RX_TELL.finditer(line) if not overlaps(m.span(), allow)]
        ctx = [m for m in RX_CONTEXT.finditer(line) if not overlaps(m.span(), allow + phrase_spans)]
        poly = []
        for name, (rx, post, pre) in RX_POLY.items():
            for m in rx.finditer(line):
                if overlaps(m.span(), allow + phrase_spans):
                    continue
                figurative = bool((post and post.search(line[m.end():m.end() + 90]))
                                  or (pre and pre.search(line[max(0, m.start() - 40):m.start()])))
                poly.append((name, m, figurative))
        marks = [m.span() for m in tells] + phrase_spans + [m.span() for m in ctx] + [m.span() for _, m, _ in poly]
        spans = sentence_spans(line)

        def same_sentence_others(span):
            for s, e in spans:
                if s <= span[0] < e:
                    return [x for x in marks if s <= x[0] < e and x != span]
            return []

        for m in tells:
            add("vocabulary", HARD, i, context(line, m.start(), m.end()), "tell word: " + m.group(0))
        for name, m, figurative in poly:
            others = same_sentence_others(m.span())
            if figurative:
                add("vocabulary", HARD, i, context(line, m.start(), m.end()), "tell word, figurative use: " + m.group(0))
            elif others:
                add("vocabulary", HARD, i, context(line, m.start(), m.end()),
                    "tell word beside other tells in the sentence: " + m.group(0))
            else:
                add("vocabulary", SOFT, i, context(line, m.start(), m.end()),
                    "context-dependent word: %s (keep it if literal or a trade term)" % m.group(0))
        for m in ctx:
            add("vocabulary", SOFT, i, context(line, m.start(), m.end()), "context-dependent word: " + m.group(0))
        for m in phrases:
            add("phrase", HARD, i, context(line, m.start(), m.end()), "tell phrase: " + m.group(0))
        for rx, note in RX_SOFT_PHRASES:
            for m in rx.finditer(line):
                add("phrase", SOFT, i, context(line, m.start(), m.end()), note + ": " + m.group(0))
        for m in RX_FILLER.finditer(line):
            add("filler", SOFT, i, context(line, m.start(), m.end()), "filler: " + m.group(0))
        for m in RX_HEDGE.finditer(line):
            add("hedge", SOFT, i, context(line, m.start(), m.end()), "hedge: " + m.group(0))
        for m in RX_SIGNPOST.finditer(line):
            add("signpost", SOFT, i, context(line, m.start(), m.end()), "signposting")
        for m in RX_GAP.finditer(line):
            add("gap-filling", SOFT, i, context(line, m.start(), m.end()), "speculation that fills a gap in what is known")
        for m in APHORISM.finditer(line):
            add("aphorism", SOFT, i, context(line, m.start(), m.end()), "formula: X is the language/currency/architecture of Y")
        for m in COPULA_AVOIDANCE.finditer(line):
            if not overlaps(m.span(), phrase_spans):
                add("copula avoidance", SOFT, i, context(line, m.start(), m.end()), "serves as / stands as / acts as: try 'is'")
        for rx in RX_NEG_SAME:
            for m in rx.finditer(line):
                add("negative parallelism", HARD, i, context(line, m.start(), m.end()), "not just X but Y / it's not X, it's Y")
        for m in NOT_BECAUSE.finditer(line):
            add("negative parallelism", SOFT, i, context(line, m.start(), m.end()), "not because X, but because Y")
        for m in TRIAD.finditer(line):
            items = [m.group(1), m.group(2), m.group(3)]
            first_tail = items[0].split()[-1].lower()
            if first_tail in OBJECT_PRONOUNS:
                continue  # "if you want to try it, comment below or message me" is a clause, not a list
            if all(len(it) <= 24 for it in items):
                add("triad", SOFT, i, context(line, m.start(), m.end()), "group of three; keep only if there are three things")
        for m in FRAGMENT_PUNCH.finditer(line):
            add("fragment", SOFT, i, context(line, m.start(), m.end()), "possible fragment used for punch")
        for m in SELF_QUESTION.finditer(line):
            add("self-answered question", SOFT, i, context(line, m.start(), m.end()), "short question the writer answers")

    if dash_allowance is not None and dash_total:
        words = word_count(text)
        allowed = 0 if dash_allowance <= 0 else max(1, int(dash_allowance * words / 1000.0 + 0.5))
        if dash_total > allowed:
            add("dash", HARD, 0, "%d dashes in %d words; the author's rate of %.1f per 1,000 words allows %d" % (
                dash_total, words, dash_allowance, allowed), "cut dashes down to the author's own rate")

    # A heading whose first sentence below says the heading again --------
    for idx, line in enumerate(lines):
        hm = HEADING_LINE.match(line)
        if not hm:
            continue
        head = content_words(re.sub(r"^\s*\d+[.)]?\s*", "", hm.group(1)))
        if len(head) < 2:
            continue
        j = idx + 1
        while j < len(lines) and not lines[j].strip():
            j += 1
        buf = []
        while j < len(lines) and lines[j].strip() and not HEADING_LINE.match(lines[j]):
            buf.append(lines[j].strip())
            j += 1
        if not buf or buf[0][:1] in (">", "!", "|", "-", "*", "+", "`") or NUMBERED_LINE.match(buf[0]):
            continue
        sents = split_sentences(" ".join(buf))
        if not sents:
            continue
        first = sents[0]
        if word_count(first) <= 25 and len(head & content_words(first)) / float(len(head)) >= 0.6:
            add("heading restatement", SOFT, idx + 2, context(first, 0, min(len(first), 70)),
                "the line under the heading says the heading again; start on something new")

    # Paragraph and sentence-level checks --------------------------------
    paragraphs = []
    buf, start = [], None
    for i, line in enumerate(lines, 1):
        if line.strip():
            if start is None:
                start = i
            buf.append(line.strip())
        elif buf:
            paragraphs.append((start, " ".join(buf)))
            buf, start = [], None
    if buf:
        paragraphs.append((start, " ".join(buf)))

    all_sentences = []
    for pstart, para in paragraphs:
        if RX_CONN_HARD.match(para):
            add("connective opener", HARD, pstart, context(para, 0, min(len(para), 50)), "paragraph opens on a connective")
        for m in NEG_PARALLEL_ACROSS.finditer(para):
            add("negative parallelism", SOFT, pstart, context(para, m.start(), m.end()), "possible 'This isn't X. It's Y.' across sentences")
        for m in NEG_PARALLEL_SAME_SUBJECT.finditer(para):
            if not any(m.start() < f.end() and f.start() < m.end() for f in NEG_PARALLEL_ACROSS.finditer(para)):
                add("negative parallelism", SOFT, pstart, context(para, m.start(), m.end()),
                    "possible 'You're not X. You're Y.' across sentences")
        sentences = split_sentences(para)
        all_sentences.extend(sentences)
        for s in sentences:
            if RX_CONN_HARD.match(s):
                add("connective opener", HARD, pstart, context(s, 0, min(len(s), 50)), "sentence opens on a connective")
            elif RX_CONN_SOFT.match(s):
                add("connective opener", SOFT, pstart, context(s, 0, min(len(s), 50)), "sentence opens on a connective (review)")
            m = PARTICIPLE_TAIL.search(s)
            if m and m.group(1).lower() not in PARTICIPLE_STOP:
                add("participial tail", SOFT, pstart, context(s, m.start(), m.end()), "sentence ends on a commenting -ing phrase")

    # Chatbot framing ----------------------------------------------------
    nonblank = [(i, l) for i, l in enumerate(lines, 1) if l.strip()]
    if nonblank:
        i, first = nonblank[0]
        if CHATBOT_FIRST_LINE.match(first):
            add("chatbot framing", HARD, i, context(first, 0, min(len(first), 60)), "assistant-style opener or preamble")
    if paragraphs:
        pstart, last = paragraphs[-1]
        if CHATBOT_LAST_PARA.match(last):
            add("chatbot framing", HARD, pstart, context(last, 0, min(len(last), 60)), "assistant-style closer or change log")

    # Sentence statistics ------------------------------------------------
    lengths = [len(re.findall(r"[A-Za-z0-9'’-]+", s)) for s in all_sentences]
    lengths = [n for n in lengths if n > 0]
    stats = {"sentences": len(lengths)}
    if lengths:
        mean = statistics.mean(lengths)
        sd = statistics.pstdev(lengths) if len(lengths) > 1 else 0.0
        cv = sd / mean if mean else 0.0
        stats.update({"mean_words": round(mean, 1), "stdev_words": round(sd, 1), "cv": round(cv, 2),
                      "shortest": min(lengths), "longest": max(lengths)})
        if len(lengths) >= 6 and cv < 0.35:
            add("uniform sentence length", SOFT, 0,
                "mean %.1f words, cv %.2f over %d sentences" % (mean, cv, len(lengths)),
                "vary sentence length; cv below 0.35 reads as machine rhythm")
    openers = [re.match(r"[\"'“‘(]?([A-Za-z']+)", s) for s in all_sentences]
    openers = [m.group(1).lower() for m in openers if m]
    run = 1
    for a, b in zip(openers, openers[1:]):
        run = run + 1 if a == b else 1
        if run == 3:
            add("repeated opener", SOFT, 0, "three consecutive sentences start with '%s'" % b, "vary sentence openings")
    stats["words"] = word_count(text)
    stats["dashes"] = dash_total
    if dash_allowance is not None:
        stats["author_dashes_per_1000"] = round(dash_allowance, 2)

    hard = sum(1 for f in findings if f["severity"] == HARD)
    soft = sum(1 for f in findings if f["severity"] == SOFT)
    return {"hard": hard, "soft": soft, "findings": findings, "stats": stats}


def report(result):
    out = []
    out.append("humanizer lint: %d hard finding%s, %d to review" % (
        result["hard"], "" if result["hard"] == 1 else "s", result["soft"]))
    s = result["stats"]
    if s.get("sentences"):
        out.append("sentences %d, mean %.1f words, shortest %d, longest %d, cv %.2f" % (
            s["sentences"], s["mean_words"], s["shortest"], s["longest"], s["cv"]))
    if "author_dashes_per_1000" in s:
        out.append("dashes %d; author's rate %.1f per 1,000 words" % (s["dashes"], s["author_dashes_per_1000"]))
    for sev, label in ((HARD, "HARD"), (SOFT, "REVIEW")):
        items = [f for f in result["findings"] if f["severity"] == sev]
        if not items:
            continue
        out.append(label)
        for f in items:
            where = ("line %d" % f["line"]) if f["line"] else "text"
            out.append("  %-24s %s: %s" % (f["category"], where, f["match"]))
            if f["note"] and f["note"] != f["match"]:
                out.append("  %-24s   %s" % ("", f["note"]))
    return "\n".join(out)


def vocabulary_listing():
    def show(title, items):
        return [title] + ["  " + x for x in items] + [""]
    out = []
    out += show("HARD: tell words (any use)", TELL_WORDS)
    out += show("SOFT unless figurative or beside other tells: words with a literal or trade sense",
                [pat for pat, _, _ in POLYSEMOUS.values()])
    out += show("NEVER FLAGGED: fixed collocations", ALLOWLIST)
    out += show("SOFT: context-dependent words (count towards a cluster)", CONTEXT_WORDS)
    out += show("HARD: tell phrases", TELL_PHRASES)
    out += show("SOFT: phrases to review", [p for p, _ in SOFT_PHRASES])
    out += show("SOFT: filler", FILLER_WORDS)
    out += show("SOFT: hedges", HEDGES)
    out += show("SOFT: signposting", SIGNPOSTS)
    out += show("SOFT: gap-filling speculation", GAP_FILLING)
    out += show("HARD: connective openers", CONNECTIVES_HARD)
    out += show("SOFT: connective openers", CONNECTIVES_SOFT)
    return "\n".join(out).rstrip()


def main(argv):
    flags = {"--json", "--allow-markdown", "--list"}
    valued = {"--author-sample", "--max-dashes-per-1000"}
    args, opts, i = [], {}, 1
    while i < len(argv):
        a = argv[i]
        if a in valued:
            if i + 1 >= len(argv):
                print("%s needs a value" % a)
                return 2
            opts[a] = argv[i + 1]
            i += 2
            continue
        if a.startswith("--"):
            if a not in flags:
                print("unknown option %s\n" % a)
                print(__doc__)
                return 2
            opts[a] = True
        else:
            args.append(a)
        i += 1
    if opts.get("--list"):
        print(vocabulary_listing())
        return 0
    if len(args) != 1:
        print(__doc__)
        return 2
    if args[0] == "-":
        text = sys.stdin.read()
    else:
        with open(args[0], encoding="utf-8") as fh:
            text = fh.read()
    allowance = None
    if "--author-sample" in opts:
        with open(opts["--author-sample"], encoding="utf-8") as fh:
            allowance = dash_rate(fh.read())[0]
    if "--max-dashes-per-1000" in opts:
        try:
            allowance = float(opts["--max-dashes-per-1000"])
        except ValueError:
            print("--max-dashes-per-1000 needs a number")
            return 2
    result = lint(text, allow_markdown=bool(opts.get("--allow-markdown")), dash_allowance=allowance)
    print(json.dumps(result, indent=2, ensure_ascii=False) if opts.get("--json") else report(result))
    return 1 if result["hard"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
