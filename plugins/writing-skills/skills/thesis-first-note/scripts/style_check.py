#!/usr/bin/env python3
"""Check a draft against the structural rules of this style skill.

Usage:
    python3 style_check.py DRAFT.md                    human-readable report
    python3 style_check.py DRAFT.md --variant NAME     check against one of the form's other formats
    python3 style_check.py DRAFT.md --json             machine-readable report
    python3 style_check.py DRAFT.md --spec other.json
    python3 style_check.py --list-variants             the formats this skill's spec defines

The spec is style.json in the skill folder (next to SKILL.md) unless --spec names another.
Without --variant the base spec applies (the form's default format). A variant overrides
keys of the base spec; a key set to null switches that check off for the variant.
Exit status: 0 when every required check passes, 1 when one fails, 2 on a usage error.

The checks are mechanical on purpose: length, headings, lists, where the thesis sits,
whether a method paragraph or an objection exists, whether figures carry captions,
whether the close summarises. They catch the shape of a piece, not its quality.
Pair this with scripts/lint.py, which catches machine-writing tells at sentence level.

The body ends at the first footnote definition ([^1]: ...), at a heading such as
References, Sources, Citation, Endnotes, Notes, Acknowledgements or Related reading, and
before a closing Published or Updated footer. Checks on the close, the opening and the
headings read the body only, so a summarising close cannot hide above the footnotes.

Standard library only. Python 3.8 or later.
"""

import json
import os
import re
import sys

HEADING = re.compile(r"^\s{0,3}(#{1,6})\s+(.*)$")
BULLET = re.compile(r"^\s*(?:[-*+]|•)\s+")
NUMBERED = re.compile(r"^\s*(?:\d+[.)]|\d+/)\s+")
FENCE = re.compile(r"^\s*```")
RULE = re.compile(r"^\s{0,3}(?:-{3,}|\*{3,}|_{3,})\s*$")
FOOTNOTE_DEF = re.compile(r"^\s{0,3}\[\^[^\]]+\]:")
END_HEADING = re.compile(
    r"^(?:\d+[.)]?\s+)?(?:references?|sources?|citations?|cite this(?: post| piece)?|endnotes?|foot-?notes?|notes|"
    r"acknowledge?ments?|related(?: reading| posts)?|further reading|bibliography|appendix(?:es)?\b.*)\s*:?\s*$",
    re.I)
DATE_TOKEN = r"(?:\d|\b(?:jan|feb|mar|apr|may|jun|jul|aug|sep|oct|nov|dec)[a-z]*\b|\bDATE\b)"
FOOTER = re.compile(r"^\s*[\[*_(]*\s*(?:originally |first )?(?:published|updated|last updated|update)\b(?=.{0,60}?" + DATE_TOKEN + ")", re.I)
LEADING_NOTE = re.compile(r"^\s*[\[*_(]*\s*(?:updated?|edit(?:ed)?|note)\b", re.I)
LINK = re.compile(r"\[[^\]]+\]\((?:https?://|#)[^)]+\)|https?://\S+")
BOLD = re.compile(r"\*\*[^*\n]+\*\*|__[^_\n]+__")
IMAGE = re.compile(r"!\[([^\]]*)\]\(([^)]+)\)")
NUMBER = re.compile(r"(?<![A-Za-z])\d[\d,.]*(?:%|x|\s?(?:ms|s|KB|MB|GB|k|m|bn|million|billion|days?|weeks?|months?|years?|hours?|minutes?|words?|people|teams?|engineers?|traces?|samples?|responses?|customers?|users?))?")
SUMMARY_OPENERS = re.compile(r"^\s*(?:in (?:summary|conclusion|short|closing)|to (?:sum up|summari[sz]e|recap|conclude)|overall|all in all|to wrap up|in this (?:post|essay|article|piece)[, ]|as (?:we have|we've|i have|i've) seen|so,? to summari[sz]e)\b", re.I)
METHOD = re.compile(r"\b(?:i (?:interviewed|surveyed|spoke (?:to|with)|talked (?:to|with)|read|reviewed|labell?ed|sampled|ran|measured|tested|asked)|interviews? with|survey(?:ed)? (?:of|over)|\d+\s+(?:people|engineers|managers|teams|respondents|responses|interviews|traces|samples|examples|conversations|clients|companies|papers|posts|cases)|based on (?:my|our) (?:experience|work) (?:with|at|across)|across (?:\d+|dozens of|several) (?:teams|clients|companies|engagements))\b", re.I)
# "To be clear" marks a concession, not an objection, so it no longer counts here.
OBJECTION = re.compile(r"\b(?:the (?:best|strongest|obvious|standard|usual|fairest) (?:objection|counter-?argument|argument against|reply)|one (?:might|could|may) (?:object|argue|say|ask)|you (?:might|could|may) (?:object|argue|say|ask)|a (?:sceptic|skeptic|critic) (?:would|might|could|will)|the (?:sceptic|skeptic|critic)'?s? (?:view|case|reply)|(?:critics|sceptics|skeptics) (?:say|argue|will say|would say)|(?:some|many|others) (?:will|would|might) (?:say|argue|object)|the case against|counter-?argument|the (?:rival|alternative|simplest) explanation|against this|objections?)\b", re.I)
DEFINITION = re.compile(r"\b(?:is|are)\s+(?:a|an|the|when|what|how|any|one|another)\b|\brefers? to\b|\bmeans\b|\bis defined as\b|\bdenotes\b|\bdescribes\b|\bis the name for\b", re.I)
EXPLETIVE = re.compile(r"^\W*(?:it|this|there|here|that|these|those)\s*(?:is|are|was|were|'s)\b", re.I)
FIRST_PERSON = re.compile(r"\b(?:I|I'm|I've|I'd|I'll|me|my|mine|myself)\b")
IMPERATIVE_FIRST = {
    "be", "do", "don't", "stop", "start", "give", "take", "ask", "say", "write", "read", "find", "focus", "think",
    "speak", "listen", "prioritise", "prioritize", "manage", "escalate", "communicate", "get", "make", "keep",
    "hire", "fire", "build", "ship", "learn", "look", "know", "refuse", "explain", "love", "move", "own", "plan",
    "choose", "pick", "measure", "treat", "trust", "never", "always", "avoid", "lead", "let", "put", "run", "set",
    "show", "use", "work", "cut", "define", "state", "name", "test", "try", "go", "come", "tell", "invest", "prefer",
    "demand", "expect", "fix", "delegate", "decide", "drop", "kill", "slow", "speed", "default", "assume", "beware",
    "celebrate", "check", "praise", "protect", "quit", "remember", "forget", "repeat", "simplify", "write",
}
CLAIM_VERBS = {
    "is", "are", "was", "were", "be", "been", "not", "never", "always", "should", "must", "can", "cannot",
    "could", "will", "would", "need", "needs", "win", "wins", "matter", "matters", "beat", "beats", "make", "makes",
    "kill", "kills", "work", "works", "fail", "fails", "break", "breaks", "scale", "scales", "cost", "costs", "has",
    "have", "does", "do", "gets", "comes", "goes", "belongs", "starts", "ends", "compounds", "counts", "lies",
    "loses", "pays", "hurts", "helps", "depends", "requires", "means", "takes", "adds", "becomes", "remains",
    "stays", "runs", "moves", "ships", "grows", "shrinks", "decays", "leaks", "outlasts", "it's", "that's",
    "there's", "what's", "change", "changes", "come", "go", "lose", "take", "give", "get", "keep", "keeps", "hold",
    "holds", "last", "lasts", "follow", "follows", "lead", "leads", "drive", "drives", "save", "saves", "pay",
    "help", "hurt", "depend", "require", "add", "become", "remain", "stay", "grow", "ship", "run", "move", "beat",
    "won", "lost", "made", "took", "gave", "got", "came", "went", "grew", "ran", "held", "kept", "led", "drove",
    "became", "broke", "outgrew", "did", "had", "said", "says", "say", "wants", "want", "feels", "feel", "looks",
    "look", "belong", "start", "end", "count", "lie", "decay", "leak", "outlast", "shrink",
}
NOT_VERB_ED = {"speed", "seed", "feed", "need", "bed", "red", "shed", "hundred", "kindred", "sacred", "naked",
               "wicked", "rugged", "beloved", "embed", "biased", "based", "advanced", "detailed", "limited", "related"}
NON_VERB_ATE_ISE = {
    "private", "climate", "senate", "ultimate", "accurate", "adequate", "appropriate", "corporate", "candidate",
    "certificate", "delicate", "desperate", "fortunate", "immediate", "intimate", "passionate", "enterprise",
    "expertise", "premise", "franchise", "otherwise", "precise", "concise", "wise", "late", "state", "rate",
    "date", "gate", "plate", "fate", "mate", "debate", "estate", "pirate", "chocolate", "template", "update",
}


def split_sentences(text):
    text = re.sub(r"\b(?:Mr|Mrs|Ms|Dr|Prof|No|vs|e\.g|i\.e|etc|Cap|para|Ltd|Inc|Co)\.", lambda m: m.group(0).replace(".", "\x00"), text)
    text = re.sub(r"(\d)\.(\d)", lambda m: m.group(1) + "\x00" + m.group(2), text)
    parts = re.split(r"(?<=[.!?])[\"'”’)*_]*\s+(?=[\"'“‘(*_]*[A-Z0-9])", text)
    return [p.replace("\x00", ".").strip() for p in parts if p.strip()]


def words(s):
    return re.findall(r"[A-Za-z0-9'’-]+", s)


def plain(s):
    """Text of a markdown fragment without emphasis or link targets."""
    s = re.sub(r"\[([^\]]*)\]\([^)]*\)", r"\1", s)
    return re.sub(r"[*_`]+", "", s).strip()


def bold_sentences(text):
    """Bold runs long enough to be a sentence; a bold name or label does not count."""
    return [b for b in BOLD.findall(text) if len(words(b)) >= 4]


def parse(text):
    lines = text.splitlines()
    title, title_idx = None, None
    in_code = False
    for i, line in enumerate(lines):
        if FENCE.match(line):
            in_code = not in_code
            continue
        m = HEADING.match(line)
        if not in_code and m and len(m.group(1)) == 1:
            title, title_idx = m.group(2).strip(), i
            break
    body_lines = [l for i, l in enumerate(lines) if i != title_idx]
    if title is None:
        for line in lines:
            if line.strip():
                title = line.strip()
                break

    # Mark code lines, then find where the body ends.
    code = []
    in_code = False
    for l in body_lines:
        if FENCE.match(l):
            code.append(True)
            in_code = not in_code
        else:
            code.append(in_code)
    cut, seen = len(body_lines), False
    for i, l in enumerate(body_lines):
        if code[i]:
            continue
        if FOOTNOTE_DEF.match(l):
            cut = i
            break
        m = HEADING.match(l)
        if m and seen and END_HEADING.match(plain(m.group(2))):
            cut = i
            break
        if l.strip():
            seen = True
    end = cut
    while end > 0:
        l = body_lines[end - 1]
        if not l.strip() or RULE.match(l) or (FOOTER.match(l) and len(words(l)) <= 30):
            end -= 1
        else:
            break
    body = body_lines[:end]
    bcode = code[:end]

    headings = [HEADING.match(l).group(2).strip() for l, c in zip(body_lines, code) if not c and HEADING.match(l)]
    body_headings = [(i, len(HEADING.match(l).group(1)), HEADING.match(l).group(2).strip())
                     for i, (l, c) in enumerate(zip(body, bcode)) if not c and HEADING.match(l)]
    bullets = [l for l, c in zip(body, bcode) if not c and BULLET.match(l) and not RULE.match(l)]
    numbered = [l for l, c in zip(body, bcode) if not c and NUMBERED.match(l)]
    paragraphs, buf = [], []
    for l, c in zip(body, bcode):
        s = l.strip()
        if (s and not c and not HEADING.match(l) and not BULLET.match(l) and not NUMBERED.match(l)
                and not IMAGE.match(s) and not s.startswith("|") and not RULE.match(l) and not FOOTNOTE_DEF.match(l)):
            buf.append(s)
        elif buf:
            paragraphs.append(" ".join(buf))
            buf = []
    if buf:
        paragraphs.append(" ".join(buf))
    prose = "\n".join(l for l, c in zip(body_lines, code) if not c)
    body_prose = "\n".join(l for l, c in zip(body, bcode) if not c)
    # Numbers are counted in body prose only: headings, list markers, link targets and footnote
    # markers carry numerals that are not evidence.
    num_lines = []
    for l, c in zip(body, bcode):
        if c or HEADING.match(l) or IMAGE.match(l.strip()):
            continue
        l = NUMBERED.sub("", l)
        l = re.sub(r"\]\([^)]*\)", "]", l)
        l = re.sub(r"https?://\S+", "", l)
        l = re.sub(r"\[\^[^\]]+\]", "", l)
        num_lines.append(l)
    return {
        "title": title or "", "headings": headings, "body_headings": body_headings, "bullets": bullets,
        "numbered": numbered, "paragraphs": paragraphs, "body_lines": body, "all_lines": body_lines,
        "prose": prose, "body_prose": body_prose, "number_text": "\n".join(num_lines),
        "word_count": len(words(prose)), "links": LINK.findall(prose), "images": IMAGE.findall(prose),
        "tables": [l for l, c in zip(body, bcode) if not c and l.strip().startswith("|")],
        "tail_excluded": len(body_lines) - end,
    }


def first_content_paragraph(d):
    for p in d["paragraphs"]:
        if not LEADING_NOTE.match(p):
            return p
    return ""


def heading_asserts(h):
    h = re.sub(r"^\s*(?:\d+[.)]?|step \d+:?)\s*", "", plain(h), flags=re.I)
    ws = [w.lower().replace("’", "'") for w in words(h)]
    if not ws:
        return False
    if ws[0] in IMPERATIVE_FIRST:
        return True
    return any(w in CLAIM_VERBS or w.endswith("n't") for w in ws) or any(
        len(w) >= 5 and w.endswith("ed") and w not in NOT_VERB_ED for w in ws[1:])


def title_ok(t):
    ws = [w.lower().replace("’", "'") for w in words(plain(t))]
    if not ws or len(ws) > 5:
        return False, "%d words" % len(ws)
    if ws[0] in IMPERATIVE_FIRST:
        return True, "imperative"
    if ws[0].endswith(("ize", "ise", "ate")) and ws[0] not in NON_VERB_ATE_ISE:
        return True, "imperative"
    if any(w in CLAIM_VERBS or w.endswith("n't") for w in ws[1:]):
        return True, "thesis"
    return False, "neither an imperative nor a claim"


def caption_after(lines, idx):
    """An emphasised line straight after an image line is its caption."""
    for l in lines[idx + 1:idx + 3]:
        s = l.strip()
        if not s:
            continue
        return plain(s) if s[:1] in ("*", "_") else ""
    return ""


def full_sentence(cap):
    cap = re.sub(r"\s*\((?:image )?(?:source|credit|via|from)\b[^)]*\)\s*$", "", cap, flags=re.I)
    cap = cap.rstrip(" )]\"'”’")
    return len(words(cap)) >= 6 and cap.endswith((".", "!", "?"))


def image_lines(lines):
    return [(i, m) for i, l in enumerate(lines) for m in [IMAGE.search(l)] if m]


def check(text, spec):
    d = parse(text)
    results = []

    def add(name, passed, evidence):
        results.append({"check": name, "passed": bool(passed), "evidence": evidence})

    w = spec.get("words")
    if w:
        n = d["word_count"]
        lo, hi = w.get("min", 0), w.get("max", 10 ** 9)
        add("length within %d to %d words" % (lo, hi) if "max" in w else "length of at least %d words" % lo,
            lo <= n <= hi, "%d words" % n)

    heads = [h for _, _, h in d["body_headings"]]
    h = spec.get("headings")
    if h == "none":
        add("no headings", not heads, "%d headings" % len(heads) if heads else "none")
    elif isinstance(h, dict):
        lo, hi = h.get("min", 0), h.get("max", 10 ** 9)
        label = "at least %d headings" % lo if "max" not in h else "%d to %d headings" % (lo, hi)
        add(label, lo <= len(heads) <= hi, "%d headings" % len(heads))

    if spec.get("heading_max_words"):
        mx = spec["heading_max_words"]
        long_ones = [x for x in heads if len(words(x)) > mx]
        add("headings of %d words or fewer" % mx, not long_ones, "; ".join(long_ones[:3]) if long_ones else "all short")

    if spec.get("headings_assert"):
        weak = [x for x in heads if not heading_asserts(x)]
        add("headings assert a claim rather than naming a topic", not weak, "; ".join(weak[:3]) if weak else "headings carry claims")

    b = spec.get("bullets")
    if b == "none":
        add("no bullet lists", not d["bullets"], "%d bullet lines" % len(d["bullets"]) if d["bullets"] else "none")

    nl = spec.get("numbered_list")
    if nl == "none":
        add("no numbered lists", not d["numbered"], "%d numbered lines" % len(d["numbered"]) if d["numbered"] else "none")
    elif nl == "required_near_top":
        top = d["body_lines"][:40]
        numbered_heads = [x for _, _, x in d["body_headings"][:6] if re.match(r"^\d", x)]
        has = any(NUMBERED.match(l) for l in top) or len(numbered_heads) >= 2
        add("numbered outline or numbered sections near the top", has, "found" if has else "no numbered list or numbered headings in the first 40 lines")
    elif isinstance(nl, dict):
        items = len(d["numbered"]) + len([x for x in heads if re.match(r"^\d+[.):]?\s", plain(x))])
        lo, hi = nl.get("min", 0), nl.get("max", 10 ** 9)
        label = "at least %d numbered items" % lo if "max" not in nl else "%d to %d numbered items" % (lo, hi)
        add(label, lo <= items <= hi, "%d numbered items" % items)

    fs = spec.get("first_sentence_max_words")
    if fs:
        p = first_content_paragraph(d)
        first = split_sentences(p) if p else []
        n = len(words(first[0])) if first else 0
        add("first sentence under %d words" % (fs + 1), bool(first) and n <= fs, "%d words: %s" % (n, (first[0] if first else "")[:90]))

    if spec.get("require_definition_first_sentence"):
        p = first_content_paragraph(d)
        first = split_sentences(p)[0] if p else ""
        ok = bool(first) and bool(DEFINITION.search(first)) and not EXPLETIVE.match(first)
        add("first sentence is a definition", ok, first[:100] or "no opening paragraph")

    bt = spec.get("bold_thesis_within_paragraphs")
    if bt:
        found = bold_sentences(" ".join(d["paragraphs"][:bt]))
        add("a bold thesis sentence within the first %d paragraphs" % bt, bool(found),
            found[0][:90] if found else "no bold sentence early (a bold name or label does not count)")

    if spec.get("bold_thesis_per_section"):
        hs = d["body_headings"]
        if hs:
            top = min(level for _, level, _ in hs)
            secs = [(i, x) for i, level, x in hs if level == top]
            missing = []
            for k, (i, x) in enumerate(secs):
                stop = secs[k + 1][0] if k + 1 < len(secs) else len(d["body_lines"])
                if not bold_sentences("\n".join(d["body_lines"][i + 1:stop])):
                    missing.append(x)
            add("a bold thesis sentence in every section", not missing,
                ("no bold sentence under: " + "; ".join(missing[:3])) if missing else "%d sections" % len(secs))
        else:
            add("a bold thesis sentence in every section", False, "no section headings")

    note = " (closing material after the body excluded)" if d["tail_excluded"] else ""
    if spec.get("forbid_summary_closer") and d["paragraphs"]:
        last = d["paragraphs"][-1]
        bad = bool(SUMMARY_OPENERS.match(plain(last)))
        add("closing paragraph does not summarise", not bad, last[:100] + note)

    cm = spec.get("close_max_words")
    if cm and d["paragraphs"]:
        last_s = split_sentences(d["paragraphs"][-1])
        n = len(words(last_s[-1])) if last_s else 0
        add("last sentence under %d words" % (cm + 1), n <= cm, "%d words: %s" % (n, (last_s[-1] if last_s else "")[:90]))

    if spec.get("require_question_close") and d["paragraphs"]:
        last = plain(d["paragraphs"][-1]).rstrip()
        add("closes on a question or an invitation", last.endswith("?") or re.search(r"\b(?:let me know|send (?:me|it|them)|email me|tell me|if you know|suggestions|corrections|additions|i will add|add it)\b", last, re.I), last[-100:])

    if spec.get("require_method_paragraph"):
        cut = int(len(d["paragraphs"]) * 0.5) + 1
        head = " ".join(d["paragraphs"][:cut])
        m = METHOD.search(head)
        add("a method sentence with counts in the first half", bool(m), m.group(0) if m else "no sentence saying how the material was gathered")

    if spec.get("require_objection"):
        m = OBJECTION.search(d["body_prose"])
        add("the strongest objection is raised in the text", bool(m), m.group(0) if m else "no objection, counter-argument or rival explanation found")

    rn = spec.get("require_numbers_min")
    if rn:
        nums = NUMBER.findall(d["number_text"])
        add("at least %d specific numbers" % rn, len(nums) >= rn, "%d numbers in the body (heading numerals and list markers not counted)" % len(nums))

    rl = spec.get("require_links_min")
    if rl:
        add("at least %d links to sources" % rl, len(d["links"]) >= rl, "%d links" % len(d["links"]))

    if spec.get("require_entry_links") or spec.get("require_entry_numbers"):
        lines = d["body_lines"]
        entries = []
        for i, l in enumerate(lines):
            if BOLD.match(l.strip()) or BULLET.match(l):
                block = [l]
                for nxt in lines[i + 1:]:
                    if not nxt.strip() or BOLD.match(nxt.strip()) or BULLET.match(nxt):
                        break
                    block.append(nxt)
                entries.append(block)
        if spec.get("require_entry_links"):
            bad = [e for e in entries if not any(LINK.search(x) for x in e)]
            add("every entry carries a source link", entries and not bad, "%d entries, %d without a link" % (len(entries), len(bad)))
        if spec.get("require_entry_numbers"):
            nonum = [e for e in entries if not re.search(r"\d", re.sub(r"\]\([^)]*\)|https?://\S+", "", " ".join(e)))]
            add("every entry carries a number or a date", entries and not nonum, "%d entries, %d without a number" % (len(entries), len(nonum)))

    fc = spec.get("figure_captions_full_sentence")
    if fc:
        imgs = image_lines(d["body_lines"])
        if imgs:
            short = []
            for i, m in imgs:
                alt = plain(m.group(1))
                if not (full_sentence(alt) or full_sentence(caption_after(d["body_lines"], i))):
                    short.append(alt or m.group(2))
            add("every figure has a full-sentence caption", not short, "; ".join(short[:3]) if short else "%d figures captioned" % len(imgs))
        elif fc == "if_present":
            add("every figure has a full-sentence caption", True, "no figures (link or describe them instead)")
        else:
            add("figures present (expected for this form)", False, "no images in the draft")

    if spec.get("figure_captions_short"):
        imgs = image_lines(d["body_lines"])
        bad = []
        for i, m in imgs:
            alt = plain(m.group(1)) or caption_after(d["body_lines"], i)
            prev = next((l.strip() for l in reversed(d["body_lines"][:i]) if l.strip()), "")
            if not (1 <= len(words(alt)) <= 9 or prev.endswith(":")):
                bad.append(alt[:60] or m.group(2))
        add("every figure has a short caption or a colon introduction", not bad,
            "; ".join(bad[:3]) if bad else ("%d figures" % len(imgs) if imgs else "no figures"))

    if spec.get("figures") == "none":
        add("no figures or tables", not d["images"] and not d["tables"],
            "%d images, %d table lines" % (len(d["images"]), len(d["tables"])))

    if spec.get("require_references_section"):
        has = any(re.match(r"^(?:\d+[.)]?\s+)?(?:references|sources|further reading|citation|bibliography)", plain(x), re.I) for x in d["headings"])
        add("a References or Sources section at the end", has, "found" if has else "none")

    if spec.get("require_open_questions_close"):
        tail = " ".join(d["paragraphs"][-3:]) + " " + " ".join(h for _, _, h in d["body_headings"][-3:])
        has = bool(re.search(r"\bopen (?:questions?|problems?)\b|\?\s*$", tail, re.I)) or any(x.strip().endswith("?") for x in d["body_lines"][-15:])
        add("closes on open questions rather than a summary", has, "found" if has else "no open questions near the end")

    mp = spec.get("max_paragraph_sentences")
    if mp:
        long_p = [p for p in d["paragraphs"] if len(split_sentences(p)) > mp]
        add("paragraphs of %d sentences or fewer" % mp, not long_p, "%d long paragraphs" % len(long_p) if long_p else "all within limit")

    pc = spec.get("paragraphs")
    if isinstance(pc, dict):
        lo, hi = pc.get("min", 0), pc.get("max", 10 ** 9)
        n = len(d["paragraphs"])
        add("paragraph count between %d and %d" % (lo, hi), lo <= n <= hi, "%d paragraphs" % n)

    fp = spec.get("max_first_person_per_1000_words")
    if fp is not None:
        n = len(FIRST_PERSON.findall(d["prose"]))
        rate = n * 1000.0 / max(1, d["word_count"])
        add("first person at most %d per 1,000 words" % fp, rate <= fp, "%.0f per 1,000 words" % rate)

    if spec.get("require_first_person"):
        n = len(FIRST_PERSON.findall(d["prose"]))
        add("written in the first person", n >= 2, "%d first-person words" % n)

    if spec.get("require_imperative_title"):
        t = d["title"].strip().strip("\"'")
        ok, why = title_ok(t)
        add("title is a short imperative or thesis", bool(t) and ok, "%s (%s)" % (t, why) if t else "no title")

    if spec.get("require_boxed_principles"):
        # a quoted or blockquoted restatement under each heading
        n = len([l for l in d["body_lines"] if l.strip().startswith(">")])
        add("each principle is restated in a blockquote under its heading", n >= max(1, len(heads) // 2), "%d blockquotes for %d headings" % (n, len(heads)))

    if spec.get("require_bold_lead_ins_min"):
        n = len(BOLD.findall(d["body_prose"]))
        add("at least %d bold lead-in sentences" % spec["require_bold_lead_ins_min"], n >= spec["require_bold_lead_ins_min"], "%d bold runs" % n)

    if spec.get("require_question_headings_min"):
        q = [x for x in heads if plain(x).endswith("?")]
        add("at least %d question headings" % spec["require_question_headings_min"], len(q) >= spec["require_question_headings_min"], "%d question headings" % len(q))

    if spec.get("require_callouts_or_steps"):
        steps = len(d["numbered"]) + len([x for x in heads if re.match(r"^(?:step|level)\s*\d", plain(x), re.I)])
        add("numbered steps or levels present", steps >= 3, "%d step markers" % steps)

    failed = [r for r in results if not r["passed"]]
    return {"spec": spec.get("name", ""), "passed": len(results) - len(failed), "failed": len(failed), "checks": results,
            "stats": {"words": d["word_count"], "headings": len(heads), "paragraphs": len(d["paragraphs"]), "links": len(d["links"]), "images": len(d["images"])}}


def resolve(spec, variant):
    """The base spec with one variant's overrides applied. Raises KeyError for an unknown variant."""
    variants = spec.get("variants", {})
    out = {k: v for k, v in spec.items() if k != "variants"}
    if variant:
        over = variants[variant]
        for k, v in over.items():
            if k == "description":
                continue
            if v is None:
                out.pop(k, None)
            else:
                out[k] = v
        out["name"] = "%s, %s" % (spec.get("name", ""), variant)
    return out


def report(r):
    out = ["style check (%s): %d passed, %d failed" % (r["spec"], r["passed"], r["failed"])]
    s = r["stats"]
    out.append("%d words, %d headings, %d paragraphs, %d links, %d images" % (s["words"], s["headings"], s["paragraphs"], s["links"], s["images"]))
    for c in r["checks"]:
        out.append("  %s  %s: %s" % ("ok  " if c["passed"] else "FAIL", c["check"], c["evidence"]))
    return "\n".join(out)


def main(argv):
    valued = {"--spec", "--variant"}
    flags = {"--json", "--list-variants"}
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
    spec_path = opts.get("--spec") or os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "style.json")
    with open(spec_path, encoding="utf-8") as fh:
        spec = json.load(fh)
    variants = spec.get("variants", {})
    if opts.get("--list-variants"):
        print("%s: base spec, plus %s" % (spec.get("name", ""), ", ".join(sorted(variants)) or "no variants"))
        for name in sorted(variants):
            print("  --variant %s: %s" % (name, variants[name].get("description", "")))
        return 0
    if len(args) != 1:
        print(__doc__)
        return 2
    variant = opts.get("--variant")
    if variant and variant not in variants:
        print("unknown variant '%s' for %s; known: %s" % (variant, spec.get("name", ""), ", ".join(sorted(variants)) or "none"))
        return 2
    draft = args[0]
    if draft == "-":
        text = sys.stdin.read()
    else:
        with open(draft, encoding="utf-8") as fh:
            text = fh.read()
    r = check(text, resolve(spec, variant))
    print(json.dumps(r, indent=2) if opts.get("--json") else report(r))
    return 1 if r["failed"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
