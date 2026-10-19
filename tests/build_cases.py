#!/usr/bin/env python3
"""Generate the style-check test drafts and tests/style_cases.json.

    python3 tests/build_cases.py

Each case is a markdown draft under tests/cases/<skill>/ plus the expectations the runner
checks: an exit status, or named checks that must pass or fail. The drafts are built from
neutral filler sentences, because style_check.py tests shape (length, headings, where the
bold sits, how the piece closes), not quality. Regenerate after editing this file; the
outputs are committed so the cases can be read without running anything.

Standard library only.
"""

import json
import os

HERE = os.path.dirname(os.path.abspath(__file__))

NUM = [
    "The billing team rebuilt the invoice service over {a} weeks and cut failed payments by {b} percent.",
    "Refund tickets fell from {a} a month to {b} after the change shipped.",
    "On-call engineers saw the same queue alert {a} times in {b} days before anyone traced the cause.",
    "The slowest {a} percent of requests took more than {b} milliseconds, which the average had hidden.",
    "A weekly release of about {a} changes was easier to review than a monthly release of {b}.",
    "The finance group asked for an export every {a} days rather than a live view with {b} charts.",
]
PLAIN = [
    "Most of the delay came from a queue that nobody owned.",
    "The old dashboard showed averages, and averages hide the slow requests at the tail.",
    "Customers noticed the faster checkout before the metrics did.",
    "Nobody had written down who could approve a refund, so every refund waited for the same two people.",
    "The fix was boring and it worked.",
    "Reviewers started reading the smaller changes properly instead of skimming them.",
    "The team stopped arguing about tools once the queue had an owner.",
    "A shorter path through the code made the next change cheaper as well.",
    "Support could answer the question in the ticket instead of escalating it.",
    "The release notes got shorter because there was less to explain.",
]
FP = [
    "I ran that team for a while and made the first version of this mistake myself.",
    "I used to think the answer was more process, and I was wrong about that.",
    "My notes from that quarter show the same pattern every week.",
    "I still check the queue on Monday mornings before I read anything else.",
]


class Gen:
    def __init__(self, seed=0):
        self.k = seed

    def sentence(self, kind):
        self.k += 1
        if kind == "num":
            return NUM[self.k % len(NUM)].format(a=3 + (self.k * 7) % 40, b=11 + (self.k * 13) % 80)
        if kind == "fp":
            return FP[self.k % len(FP)]
        return PLAIN[self.k % len(PLAIN)]

    def para(self, n=3, num=True, fp=False):
        out = []
        for j in range(n):
            if fp and j == 0:
                out.append(self.sentence("fp"))
            elif num and j % 2 == 0:
                out.append(self.sentence("num"))
            else:
                out.append(self.sentence("plain"))
        return " ".join(out)

    def paras(self, total_words, n=3, num=True, fp=False):
        out, count = [], 0
        while count < total_words:
            p = self.para(n, num=num, fp=fp)
            out.append(p)
            count += len(p.split())
        return out


def wc(text):
    return len(text.split())


CASES = []


def case(skill, cid, item, text, expect, variant=None, note=""):
    path = os.path.join("cases", skill, cid + ".md")
    os.makedirs(os.path.join(HERE, "cases", skill), exist_ok=True)
    with open(os.path.join(HERE, path), "w", encoding="utf-8") as fh:
        fh.write(text.rstrip() + "\n")
    CASES.append({"id": "%s/%s" % (skill, cid), "item": item, "skill": skill, "file": path,
                  "variant": variant, "expect": expect, "note": note, "words": wc(text)})


OK = [{"exit": 0}]


def fails(name):
    return [{"check": name, "passed": False}]


def passes(name):
    return [{"check": name, "passed": True}]


# ---------------------------------------------------------------- curated-evidence-page
def curated_default():
    g = Gen(1)
    out = ["# Fast builds", "",
           "This page collects public works finished quickly, with the elapsed days computed for each.", ""]
    for i in range(8):
        out += ["**Project %d.** %s The work took %d days from start to finish." % (i + 1, g.sentence("plain"), 30 + i * 17),
                "*Source: [primary account %d](https://example.org/source-%d)*" % (i + 1, i + 1), ""]
    out += ["The northern rail spur, approved in 2009, was still unfinished after 4,800 days. " + g.sentence("plain"), "",
            "This page leaves out private projects and anything without a primary source. Works offering hypotheses are listed separately, none endorsed.", "",
            "Send corrections or additions, with a source."]
    return "\n".join(out)


case("curated-evidence-page", "default-good", 0, curated_default(), OK)


def curated_questions():
    g = Gen(2)
    out = ["# Open questions", "", "These are questions about public works that I cannot answer yet.", ""]
    for i in range(20):
        link = " See [the filing](https://example.org/q-%d)." % i if i % 3 == 0 else ""
        out += ["**Why does project type %d finish faster than the others?** %s %s%s" % (i + 1, g.sentence("num"), g.sentence("plain"), link), ""]
    out += ["**What does the chart overstate?** The chart counts finished projects only, so it overstates how fast the typical one goes."]
    return "\n".join(out)


case("curated-evidence-page", "question-list-good", 13, curated_questions(), OK, variant="question-list")


def curated_reading():
    g = Gen(3)
    out = ["# Reading on public works", "", "A first cut at a reading list on how public works get built quickly.", ""]
    for i in range(10):
        out.append("- [Title %s](https://example.org/reading-%d) %s" % ("ABCDEFGHIJ"[i], i, g.sentence("plain")))
    out += ["", "This list leaves out the engineering manuals. It is a first cut and still in progress."]
    return "\n".join(out)


case("curated-evidence-page", "reading-list-good", 13, curated_reading(), OK, variant="reading-list")


def curated_dispatch(first_person=True):
    g = Gen(4)
    head = "I am not an expert on permitting." if first_person else "Permitting is not a simple subject."
    out = ["# Notes on permitting, 4 May 2026", "", head + " " + g.para(3, fp=first_person), ""]
    for p in g.paras(450, n=4, fp=False):
        out += [p, ""]
    if first_person:
        out += ["I first posted this on [my notes page](https://example.org/notes). My guess is that sequencing matters more than the rules.", ""]
        out += ["If you work on permitting and think I have this wrong, what am I missing?"]
    else:
        out += ["The notes first appeared on [the notes page](https://example.org/notes). Sequencing probably matters more than the rules.", ""]
        out += ["Readers who work on permitting may know what is missing here; what is it?"]
    return "\n".join(out)


case("curated-evidence-page", "dispatch-good", 13, curated_dispatch(), OK, variant="dispatch")
case("curated-evidence-page", "dispatch-no-first-person-bad", 13, curated_dispatch(False),
     fails("written in the first person"), variant="dispatch")


# ---------------------------------------------------------------- field-guide
def field_default(caption="A raw support trace", colon_intro=True):
    g = Gen(5)
    out = ["# Read the traces before you build a judge", "",
           "I have led evaluation work on 9 support products over 4 years. Most failed for one reason: nobody read the output before deciding what to measure.", "",
           "Contents: [Level 1](#level-1), [Level 2](#level-2), [Level 3](#level-3), [Recap](#recap).", ""]
    rules = ["**Read the traces before you write a single metric.**",
             "**Write the critique before you write the score.**",
             "**Build the judge only after you can predict its answers.**"]
    for i in range(3):
        out += ["## Level %d: %s" % (i + 1, ["Read 100 traces by hand", "Write critiques in a spreadsheet", "Build the judge last"][i]), ""]
        out += ["The common mistake at this level is skipping it. " + g.para(3), ""]
        if i == 0:
            out += ["Here is what one trace looked like:" if colon_intro else g.sentence("plain"), "",
                    "![%s](trace.png)" % caption, ""]
        for p in g.paras(330, n=4):
            out += [p, ""]
        out += [rules[i], ""]
    out += ["## Recap", "", "1. Read the traces.", "2. Write critiques.", "3. Build the judge last.", "",
            "None of this replaces talking to the people who use the product."]
    return "\n".join(out)


case("field-guide", "default-good", 0, field_default(), OK)
case("field-guide", "long-caption-bad", 15,
     field_default(caption="A screenshot of the raw support trace that the client exported from their logging tool", colon_intro=False),
     fails("short caption or a colon introduction"))


def field_faq():
    g = Gen(6)
    out = ["# Evals FAQ", "", "These are sharp opinions from evaluation work on 9 products, and some will age badly.", "",
           "| Reader | Start with |", "|---|---|", "| Engineer | the first question |", "| Product lead | the fourth question |", ""]
    qs = ["Should I buy an eval platform first?", "Do I need a judge model on day one?", "How many traces should I read?",
          "Should product managers label data?", "Is a 1 to 5 score useful?", "Can I reuse public benchmarks?",
          "Should I write a rubric before reading traces?", "How often should the judge be checked?",
          "Do I need a custom labelling tool?", "Should evals block a release?", "Who should own the eval set?",
          "Is synthetic data good enough?"]
    for i, q in enumerate(qs):
        out += ["## " + q, "", "%s **%s** %s" % (["No.", "Generally no.", "Yes."][i % 3],
                                                 "Start with the simplest thing that shows the failure.",
                                                 g.para(5)), "", g.para(4), ""]
    return "\n".join(out)


case("field-guide", "faq-good", 13, field_faq(), OK, variant="faq")


def field_teardown():
    g = Gen(7)
    out = ["# Most eval dashboards measure the wrong thing", "", g.para(3), ""]
    for h in ["The dashboard counts what is easy", "Three examples from one quarter", "What to measure instead"]:
        out += ["## " + h, ""]
        for p in g.paras(720, n=4):
            out += [p, ""]
    out += ["A dashboard is a good servant and a bad product manager."]
    return "\n".join(out)


case("field-guide", "teardown-good", 13, field_teardown(), OK, variant="teardown")


def field_notes():
    g = Gen(8)
    out = ["# Notes from a talk on evals", "", "These are the annotated slides from a talk given to a product team.", ""]
    for i in range(10):
        out += ["## Slide %d: %s" % (i + 1, ["The demo that worked", "The trace nobody read", "The spreadsheet", "The judge",
                                             "Agreement over time", "The cost", "What changed", "What did not",
                                             "Questions", "Close"][i]), ""]
        out += [g.para(4), "", g.para(3), "", "Q: " + g.sentence("plain"), "", "A: " + g.sentence("num"), ""]
    return "\n".join(out)


case("field-guide", "notes-page-good", 13, field_notes(), OK, variant="notes-page")


# ---------------------------------------------------------------- mechanism-essay
def mechanism_default(objection=True, numbers=True, figure=False):
    g = Gen(9)
    out = ["# Cheaper inference will widen the gap between careful and careless teams", "",
           "**Cheaper inference will reward the teams that measure their work, because the savings flow to whoever can tell good output from bad.** "
           "This piece does not argue that cost is the only factor, and parts of it may be wrong.", "",
           g.para(3, num=numbers), "",
           "1. Framework", "2. Where the savings go", "3. %s" % ("Objections" if objection else "Limits"), "4. What follows", "",
           "## 1. Framework", ""]
    for p in g.paras(500, n=4, num=numbers):
        out += [p, ""]
    if figure:
        out += ["![A chart of cost per task falling over two years.](cost.png)", ""]
    out += ["## 2. Where the savings go", ""]
    for p in g.paras(600, n=4, num=numbers):
        out += [p, ""]
    out += ["## 3. %s" % ("Objections" if objection else "Limits"), ""]
    if objection:
        out += ["The strongest objection is that cheaper inference helps everyone equally. " + g.para(3, num=numbers), ""]
    else:
        out += ["To be clear, cheaper inference helps everyone to some degree. " + g.para(3, num=numbers), ""]
    for p in g.paras(400, n=4, num=numbers):
        out += [p, ""]
    out += ["## 4. What follows", ""]
    for p in g.paras(300, n=4, num=numbers):
        out += [p, ""]
    out += ["**Teams should measure before they buy.**", "", "## Notes", "",
            "[^1]: A footnote that carries a caveat." if not numbers else "[^1]: The estimate assumes 2026 prices."]
    return "\n".join(out)


case("mechanism-essay", "default-good", 0, mechanism_default(), OK)
case("mechanism-essay", "figure-bad", 15, mechanism_default(figure=True), fails("no figures or tables"))
case("mechanism-essay", "heading-numbers-only-bad", 14, mechanism_default(numbers=False), fails("specific numbers"),
     note="the only numerals are heading numbers, list markers and a footnote marker")
case("mechanism-essay", "to-be-clear-only-bad", 14, mechanism_default(objection=False), fails("strongest objection"),
     note="a concession ('To be clear') but no objection")


# ---------------------------------------------------------------- one-idea-post
def one_idea(title="Give feedback early", close="Say the hard thing in the first week.", footnote=None):
    g = Gen(10)
    out = ["# " + title, "", "Most managers wait too long to give hard feedback.", ""]
    out += ["Still, waiting feels kind. " + g.para(3, fp=True), ""]
    for p in g.paras(330, n=4, fp=False):
        out += [p, ""]
    out += ["Give the feedback while the work is still fresh. It will not always land well.", "", close]
    if footnote:
        out += ["", footnote]
    return "\n".join(out)


case("one-idea-post", "default-good", 0, one_idea(), OK)
case("one-idea-post", "confessional-good", 13, one_idea(), OK, variant="confessional")
case("one-idea-post", "title-noun-bad", 14, one_idea(title="Quarterly planning notes"), fails("title is a short imperative or thesis"))
case("one-idea-post", "title-gerund-bad", 14, one_idea(title="Breaking things"), fails("title is a short imperative or thesis"))
case("one-idea-post", "title-thesis-good", 14, one_idea(title="Feedback is a gift"), passes("title is a short imperative or thesis"))
case("one-idea-post", "close-12-words-bad", 15, one_idea(close="Say the hard thing in the first week, before it hardens further."),
     fails("last sentence under"), note="prose says under twelve words; this close has twelve")
case("one-idea-post", "close-above-footnote-bad", 12,
     one_idea(close="Say the hard thing in the first week, because every week you wait makes the conversation harder for both of you.",
              footnote="[^1]: Internal survey, 2026."),
     fails("last sentence under"), note="a long close hidden above a short footnote")


def one_idea_list(items=10):
    g = Gen(11)
    out = ["# Keep a decision log", "", "Teams forget why they decided things, and then they decide them again.", ""]
    for p in g.paras(470, n=4):
        out += [p, ""]
    for i in range(items):
        out.append("%d. **%s.** %s %s %s %s" % (i + 1, ["Date every entry", "Name the owner", "Write the options", "Record the cost",
                                                      "Say what would change it", "Link the data", "Keep it short", "Review monthly",
                                                      "Close old entries", "Share it widely", "Keep the losers", "Note the dissent"][i % 12],
                                           g.sentence("num"), g.sentence("plain"), g.sentence("plain"), g.sentence("num")))
    out += ["", "Start the log this week."]
    return "\n".join(out)


case("one-idea-post", "list-essay-good", 13, one_idea_list(), OK, variant="list-essay",
     note="over 1,400 words, which the old spec rejected")
case("one-idea-post", "list-essay-short-list-bad", 13, one_idea_list(items=4), fails("numbered items"), variant="list-essay")


def one_idea_mini(first_person=False):
    g = Gen(12)
    body = [g.para(3, fp=first_person), g.para(3), g.para(3), g.para(2)]
    if first_person:
        body.append("I learned this the slow way, and my team paid for it.")
    out = ["# Write the decision down", "", "A decision nobody wrote down gets made again.", ""] + sum([[p, ""] for p in body], [])
    out += ["Write it down today."]
    return "\n".join(out)


case("one-idea-post", "miniature-good", 13, one_idea_mini(), OK, variant="miniature")
case("one-idea-post", "miniature-first-person-bad", 13, one_idea_mini(True), fails("first person at most"), variant="miniature")


# ---------------------------------------------------------------- patterns-survey
def patterns_default(questions=True, references=True, summary=False):
    g = Gen(13)
    items = [("Evals", "catch regressions early"), ("Retrieval", "ground every answer"), ("Guardrails", "stop the worst replies")]
    out = ["# Patterns for support bots: what held up in production", "",
           "> A model is only as good as the examples you check it against.", "",
           "This post covers three patterns.", ""]
    out += ["- [%s: %s](#%s)" % (a, b, a.lower()) for a, b in items] + [""]
    for k, (a, b) in enumerate(items):
        out += ["## %s: %s" % (a, b), "", "### Why %s%s" % (a.lower(), "?" if questions else ""), "", g.para(3), "",
                "### More about %s" % a.lower(), "",
                "**Study %d** ([link](https://example.org/paper-%d)) shows %s" % (k + 1, k + 1, g.para(3)), "",
                "### How to apply %s" % a.lower(), "",
                "**Build a labelled set of examples before you tune anything.** " + g.para(3), "",
                "**Check the set against production every month.** " + g.para(2), "", g.para(4), ""]
    out += ["## Conclusion", ""]
    if summary:
        out += ["To sum up, the three patterns cover testing, grounding and safety."]
    else:
        out += ["Which of these patterns will still matter in two years? What would make evals cheap enough to run on every change?"]
    if references:
        out += ["", "## References", "", "1. Study 1. https://example.org/paper-1", "2. Study 2. https://example.org/paper-2", "",
                "## Citation", "", "Author, Patterns for support bots, 2026."]
    return "\n".join(out)


case("patterns-survey", "default-good", 0, patterns_default(), OK)
case("patterns-survey", "no-question-headings-no-references-bad", 15, patterns_default(questions=False, references=False),
     fails("question headings") + fails("References or Sources section"))
case("patterns-survey", "summary-above-references-bad", 12, patterns_default(summary=True),
     fails("closing paragraph does not summarise"))


def patterns_essay():
    g = Gen(14)
    out = ["# Write the small proposal first", "", "The simpler proposal usually loses the planning meeting and wins the year.", "",
           "> Simple things should be simple.", "", "See [the planning notes](https://example.org/a), [the review](https://example.org/b) and [the follow-up](https://example.org/c)."]
    for h in ["Why does the big proposal win the room?", "Write the small version anyway", "What it costs you"]:
        out += ["", "## " + h, ""]
        for p in g.paras(430, n=4):
            out += [p, ""]
    out += ["**First, the small proposal ships before the big one is staffed.** " + g.sentence("num"), "",
            "**Second, it tells you which half of the big one mattered.** " + g.sentence("plain"), "",
            "Nobody remembers the meeting; they remember what shipped."]
    return "\n".join(out)


case("patterns-survey", "essay-good", 13, patterns_essay(), OK, variant="essay")


# ---------------------------------------------------------------- principle-column
def principle_default(paragraphs=20, target=None):
    g = Gen(15)
    out = ["Every company I talk to says its teams are too slow, and they are right that something is off.", "",
           "The speed is not the problem.", ""]
    n = 2
    while n < paragraphs - 1:
        if n % 5 == 4:
            out += ["Most of that work was the wrong work.", ""]
        else:
            out += [g.para(3, fp=(n % 3 == 0)), ""]
        n += 1
    out += ["I think the teams that measure outcomes will pull ahead, though I would not bet on how soon."]
    text = "\n".join(out)
    while target and wc(text) < target:
        text = text.replace("The speed is not the problem.", "The speed is not the problem. " + g.sentence("plain"), 1)
    return text


case("principle-column", "default-good", 0, principle_default(), OK)
case("principle-column", "few-paragraphs-bad", 15,
     "\n\n".join(Gen(16).paras(700, n=6, fp=True)[:8]) + "\n\nI think this will hold, though not everywhere.",
     fails("paragraph count"))
def principle_short(target=550):
    g = Gen(17)
    out = []
    while wc("\n\n".join(out)) < target - 30:
        out.append(g.para(2, fp=(len(out) % 3 == 0)))
    out.append("I think this holds.")
    return "\n\n".join(out)


case("principle-column", "short-550-bad", 15, principle_short(), fails("length within 600"),
     note="between 500 and 600 words: the prose says 600 to 1,700")


def principle_confessions():
    g = Gen(18)
    out = ["I have made every mistake on this list at least once, and some of them twice.", "", g.para(2, fp=True), ""]
    for i, h in enumerate(["I hired for speed", "I skipped the reference calls", "I promoted the loudest engineer",
                           "I waited to give feedback", "I owned too many decisions", "I wrote the strategy alone",
                           "I trusted the dashboard", "I said yes to every customer", "I cancelled the retros",
                           "I stopped writing things down"]):
        out += ["## %d. **%s**" % (i + 1, h), "", g.para(4, fp=(i % 2 == 0)), ""]
    out += ["I expect to add to this list, which is the worst thing I can say about it."]
    return "\n".join(out)


case("principle-column", "confessional-list-good", 13, principle_confessions(), OK, variant="confessional-list")


def principle_coaching():
    g = Gen(19)
    out = ["# You are allowed to be bad at this for a while", "",
           "If you lead a team alone, you will spend your first year getting worse before you get better. I did.", ""]
    for i, h in enumerate(["Pick one instrument", "Practise the boring scales", "Ask the coaching questions", "Keep score honestly"]):
        out += ["## %d. %s" % (i + 1, h), ""]
        for p in g.paras(330, n=4, fp=(i == 0)):
            out += [p, ""]
        out += ["What would you do differently next week? Write it down.", ""]
    out += ["Start small. Keep going."]
    return "\n".join(out)


case("principle-column", "coaching-good", 13, principle_coaching(), OK, variant="coaching")


# ---------------------------------------------------------------- reportage-deep-dive
def reportage_default(bold_everywhere=True, summary_close=False, related=True):
    g = Gen(20)
    out = ["# How support teams run on-call", "",
           "> How do other companies run on-call for support engineers? (a reader question)", "",
           "**This issue covers how three companies run on-call for support engineering, and what I would copy.**", "",
           "1. How on-call is staffed", "2. What the data shows", "3. What to copy", "",
           "## 1. How on-call is staffed", "",
           "When I joined my second company, on-call rotated every month. **The teams that rotated weekly kept their engineers longer.** " + g.sentence("num"), "",
           "For this issue I interviewed 14 engineers at 3 companies and read 212 survey responses. Two companies did not reply. " + g.sentence("plain"), "",
           g.para(4), "", g.para(4), "", g.para(4), "",
           "## 2. What the data shows", "",
           g.para(4), "", g.para(4), "",
           "![Teams with weekly rotations reported fewer missed pages in the reader survey. Source: reader survey.](chart.png)", "",
           "The survey is small and not representative. **The pattern still held at every company I spoke to.** " + g.sentence("num"), "",
           "## 3. What to copy", "",
           ("**Rotate weekly and pay for the nights.** " if bold_everywhere else "Rotate weekly and pay for the nights. ") + g.para(4), "", g.para(4), "",
           "## Advice", "",
           "**Write the rotation down before the next incident.** " + g.sentence("plain"), "",
           "**Pay for the nights in money, not thanks.** " + g.sentence("num"), ""]
    if summary_close:
        out += ["In conclusion, weekly rotations and paid nights are what the three companies have in common.", "",
                "Published 3 March 2026. Updated 5 March 2026."]
        return "\n".join(out)
    out += ["Thanks to the two reviewers who read drafts of this issue.", ""]
    if related:
        out += ["## Related reading", "", "- [On-call pay](https://example.org/oncall-pay)", ""]
    out += ["Published 3 March 2026. Updated 5 March 2026."]
    return "\n".join(out)


case("reportage-deep-dive", "default-good", 0, reportage_default(), OK)
case("reportage-deep-dive", "section-without-bold-bad", 15, reportage_default(bold_everywhere=False),
     fails("a bold thesis sentence in every section"))
case("reportage-deep-dive", "summary-above-footer-bad", 12, reportage_default(summary_close=True),
     fails("closing paragraph does not summarise"))


def reportage_guide():
    g = Gen(21)
    out = ["# Traits of a strong support engineer", "",
           "A strong support engineer is one who closes the loop between a customer's problem and the code that caused it. " + g.sentence("num"), ""]
    for i in range(9):
        out += ["## %d. %s" % (i + 1, ["They write things down", "They read the logs first", "They reproduce before they reply",
                                       "They know the escalation path", "They close the loop", "They say no clearly",
                                       "They measure their queue", "They teach the next hire", "They fix the docs"][i]), "",
                "**This trait shows up in the first month or not at all.** " + g.para(4), "", g.para(4), ""]
    out += ["Pick one trait and practise it for a month."]
    return "\n".join(out)


case("reportage-deep-dive", "evergreen-guide-good", 13, reportage_guide(), OK, variant="evergreen-guide")


def reportage_commentary():
    g = Gen(22)
    out = ["# The week in incidents", "", "*The week in incidents is a series about outages and what they teach.*", "",
           "This issue covers four topics.", "",
           "1. **The payments outage.** " + g.sentence("plain"), "2. **A new on-call rule.** " + g.sentence("plain"),
           "3. **Cuts at a vendor.** " + g.sentence("plain"), "4. **A tool worth trying.** " + g.sentence("plain"), "",
           "## 1. The payments outage", "", "At 09:14 the first alert fired. At 09:31 the status page still showed green. " + g.para(3), "",
           "![](status.png)", "***At 09:31 the status page still showed green. Source: [status page](https://example.org/status).***", ""]
    for h in ["2. A new on-call rule", "3. Cuts at a vendor", "4. A tool worth trying"]:
        out += ["## " + h, ""]
        for p in g.paras(220, n=4):
            out += [p, ""]
    out += ["The status page has since been fixed, which is more than can be said for the vendor."]
    return "\n".join(out)


case("reportage-deep-dive", "commentary-good", 13, reportage_commentary(), OK, variant="commentary")


# ---------------------------------------------------------------- strategy-pattern-essay
def strategy_default(bold_thesis=True):
    g = Gen(23)
    second = ("**The companies that win turn one customer's work into the next customer's reason to arrive.** " if bold_thesis
              else "The companies that win turn one customer's work into the next customer's reason to arrive. ")
    out = ["# Loops beat funnels", "",
           "Every company eventually sells what its best customers already do." + ("" if bold_thesis else " **Acme** is the example here."), "",
           second + g.para(2), "", g.para(3), ""]
    for h in ["Work loops", "One variable", "Cost structure"]:
        out += ["## " + h, ""]
        for p in g.paras(450, n=4):
            out += [p, ""]
    out += ["This does not compound forever; returns fall once most of a market is inside the loop.", "",
            "The rival explanation is simpler: timing. " + g.para(2), "", g.para(3), "",
            "The best product is the one its users keep shipping for you.", "",
            "*Thanks to the two readers who argued with the draft.*", "", "## Notes", "", "1. A note."]
    return "\n".join(out)


case("strategy-pattern-essay", "default-good", 0, strategy_default(), OK)
case("strategy-pattern-essay", "bold-name-only-bad", 14, strategy_default(bold_thesis=False),
     fails("a bold thesis sentence within"), note="the only bold run is a company name")


# ---------------------------------------------------------------- taxonomy-explainer
def taxonomy_default(definition=True):
    g = Gen(24)
    first = ("Reward hacking is when a trained agent exploits a flaw in its reward signal instead of doing the intended task."
             if definition else "Few topics in machine learning have drawn as much attention this year.")
    out = ["# Reward hacking", "", "[Updated on 1 May 2026: added the detection section.]", "",
           first + " These notes cover causes, detection and mitigation, and leave out multi-agent settings because a fair survey of them would double the length.", "",
           "Contents: [Causes](#causes), [Detection](#detection), [Mitigation](#mitigation), [Open problems](#open-problems).", ""]
    k = 0
    for top, subs in [("Causes", ["Misspecified rewards", "Proxy drift"]), ("Detection", ["Held-out checks"]), ("Mitigation", ["Reward modelling"])]:
        out += ["## " + top, "", "This section covers %s." % top.lower(), ""]
        for s in subs:
            k += 1
            out += ["### " + s, "", "**Method %d** ([Author et al. 202%d](https://example.org/paper-%d)) %s" % (k, k, k, g.para(4)), ""]
            for p in g.paras(330, n=4):
                out += [p, ""]
            if k == 1:
                out += ["![Fig. 1. Agents trained for longer found more exploits in the same environment. (Image source: Author et al. 2021)](fig1.png)", ""]
    out += ["## Open problems", "", "- Can detection keep up with more capable agents?", "- What would a reward that cannot be gamed look like?", "",
            "## Citation", "", "Author, Reward hacking, 2026.", "", "## References", "",
            "1. [Author et al. 2021](https://example.org/paper-1)", "2. [Author et al. 2022](https://example.org/paper-2)"]
    return "\n".join(out)


case("taxonomy-explainer", "default-good", 0, taxonomy_default(), OK,
     note="the figure caption ends in an image credit, as the skeleton shows")
case("taxonomy-explainer", "why-it-matters-opening-bad", 15, taxonomy_default(definition=False),
     fails("first sentence is a definition"))


# ---------------------------------------------------------------- technical-principles-essay
def technical_default(topic_heading=False):
    g = Gen(25)
    heads = ["1. Pre-rendered pages are not optional",
             "2. The history of web performance" if topic_heading else "2. Every round trip costs at least 40 ms",
             "3. Optimistic updates are wrong for payments"]
    out = ["# Fast pages are a product decision", "",
           "I gave a talk on page speed last year and rebuilt this blog's renderer afterwards. Two questions keep coming up, and I will answer both through one lens: what the reader waits for.", ""]
    for i, h in enumerate(heads):
        out += ["## " + h, "", "> %s %s" % (g.sentence("plain"), g.sentence("plain")), "",
                "The measured number is 1.%d seconds on a mid-range phone ([trace](https://example.org/trace-%d)). %s" % (i + 2, i, g.para(3)), "",
                "![The pre-rendered page painted %d00 milliseconds earlier on the same phone.](paint-%d.png)" % (i + 3, i), "",
                g.para(4), "", g.para(4), "", g.para(4), "", g.para(3), "", "The exception is checkout, where a wrong answer costs more than a slow one.", ""]
    out += ["Here is the walkthrough on this blog ([source](https://example.org/blog-source)). " + g.para(3), "",
            "The web is fast when we let it be."]
    return "\n".join(out)


case("technical-principles-essay", "default-good", 0, technical_default(), OK)
case("technical-principles-essay", "topic-heading-bad", 14, technical_default(topic_heading=True),
     fails("headings assert a claim"), note="a five-word topic heading the old check skipped")


def technical_short(headings=False):
    g = Gen(26)
    out = ["# Ship the boring renderer", ""]
    for i in range(22):
        if headings and i == 10:
            out += ["## What changed", ""]
        out += [g.sentence("num" if i % 4 == 0 else "plain"), ""]
    out += ["The [trace is public](https://example.org/trace).", "", "Boring renderers age well."]
    return "\n".join(out)


case("technical-principles-essay", "short-note-good", 13, technical_short(), OK, variant="short-note")
case("technical-principles-essay", "short-note-headings-bad", 13, technical_short(headings=True), fails("no headings"), variant="short-note")


def technical_announcement():
    g = Gen(27)
    out = ["# The next renderer", "",
           "We built this because every team we worked with lost a week a quarter to slow previews. " + g.para(3), ""]
    for h in ["From pages to apps", "From servers to the edge", "From builds to instant previews"]:
        out += ["## " + h, ""]
        for p in g.paras(260, n=4):
            out += [p, ""]
    out += ["| Old primitive | New primitive |", "|---|---|", "| Build | Preview |", "| Server | Edge |", "",
            "The [launch notes](https://example.org/launch) list the rest.", "", "Previews should feel like saving a file."]
    return "\n".join(out)


case("technical-principles-essay", "announcement-good", 13, technical_announcement(), OK, variant="announcement")


def technical_single():
    g = Gen(28)
    out = ["# Render on the server first", "",
           "**Rendering on the server first is the cheapest speed-up most teams have not taken.** " + g.para(2), ""]
    for i, h in enumerate(["Isn't this premature?", "Doesn't it cost more?", "Won't caching solve it?"]):
        out += ["## " + h, "", "The [benchmark %d](https://example.org/bench-%d) answers this. %s" % (i + 1, i + 1, g.para(4)), ""]
        for p in g.paras(330, n=4):
            out += [p, ""]
    out += ["![The server-rendered version painted in 1.2 seconds against 2.9 for the client version.](demo.png)", "",
            "Here is the walkthrough ([code](https://example.org/code)). " + g.para(3), "", "Ship the page, then the script."]
    return "\n".join(out)


case("technical-principles-essay", "single-thesis-good", 13, technical_single(), OK, variant="single-thesis")


def technical_year():
    g = Gen(29)
    out = ["# The year in rendering", "", "I wrote one note a week this year; these are the claims that held up. " + g.sentence("num"), ""]
    claims = ["Static pages won the year", "Edge caching beats clever code", "Hydration costs more than it saves",
              "Fonts are still the slowest asset", "Images need explicit sizes", "Third-party scripts are the real budget",
              "Server components are worth the move", "Streaming is not optional", "Benchmarks need real phones",
              "Previews change how teams review", "Bundle size still matters", "Most regressions come from one dependency"]
    for i, c in enumerate(claims):
        out += ["## " + c, "", "%s[^%d] See [note %d](https://example.org/note-%d)." % (g.para(4), i + 1, i + 1, i + 1), "", g.para(3), "",
                "> \"%s\"" % g.sentence("plain"), ""]
    out += ["Next year will be quieter, I hope.", ""]
    out += ["[^%d]: Footnote %d." % (i + 1, i + 1) for i in range(len(claims))]
    return "\n".join(out)


case("technical-principles-essay", "year-in-review-good", 13, technical_year(), OK, variant="year-in-review")


# ---------------------------------------------------------------- thesis-first-note
def thesis_default(first="I think small teams should own fewer tools.", close="Own fewer tools, and know each one well.", footnote=False):
    g = Gen(30)
    out = [first, "", "There is some truth to the other side.", ""]
    for p in g.paras(380, n=4):
        out += [p, ""]
    out += ["A cabinetmaker owns a few tools and knows each one. " + g.para(2), "", close]
    if footnote:
        out += ["", "[^1]: The team was twelve people at the time."]
    return "\n".join(out)


case("thesis-first-note", "default-good", 0, thesis_default(), OK)
case("thesis-first-note", "first-sentence-13-bad", 15, thesis_default(first="I think small teams should own far fewer tools than they do today."),
     fails("first sentence under"), note="13 words; the prose says under twelve")
case("thesis-first-note", "summary-above-footnote-bad", 12,
     thesis_default(close="In short, fewer tools, better known, beat more tools half-learned.", footnote=True),
     fails("closing paragraph does not summarise"))
case("thesis-first-note", "close-above-footnote-good", 12, thesis_default(footnote=True),
     passes("closing paragraph does not summarise"), note="control: a proper close above a footnote")


def thesis_headed():
    g = Gen(31)
    out = ["I think every team should write its own tools down.", "", "There is some truth to the opposite view.", ""]
    for h in ["Start with what you use", "Cut the duplicates", "Write the list down", "Review it every quarter"]:
        out += ["## " + h, ""]
        for p in g.paras(240, n=4):
            out += [p, ""]
    out += ["- Keep one tracker.", "- Keep one chat tool.", "- Keep one place for docs.", "", "We are hiring people who like short lists."]
    return "\n".join(out)


case("thesis-first-note", "headed-essay-good", 13, thesis_headed(), OK, variant="headed-essay")

# A variant name the spec does not define is a usage error, before and after.
case("one-idea-post", "unknown-variant", 13, one_idea(), [{"exit": 2}], variant="no-such-variant")


if __name__ == "__main__":
    with open(os.path.join(HERE, "style_cases.json"), "w", encoding="utf-8") as fh:
        json.dump(CASES, fh, indent=1)
        fh.write("\n")
    print("%d style cases written" % len(CASES))
