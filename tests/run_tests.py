#!/usr/bin/env python3
"""Run the writing-skills test suite against a folder of skills.

    python3 -I -B tests/run_tests.py                      the skills in plugins/writing-skills/skills
    python3 -I -B tests/run_tests.py --skills DIR [--tree DIR] [--label NAME] [--out FILE]

--skills is the folder holding one directory per skill (humanizer, field-guide, ...).
--tree is the folder holding shared/ and tools/ (defaults to the repository root).
A skill directory may also be nested one level (DIR/name/name/SKILL.md), as an unzipped
.skill file is, so the original packages can be tested as they were shipped.

Suites:
  lint      tests/lint_cases.json and tests/vocab_catalogue.json against humanizer's lint.py
  style     tests/style_cases.json against each skill's style_check.py (build with build_cases.py)
  docs      tests/doc_checks.json: required and forbidden wording in SKILL.md and reference files
  shared    every copy of lint.py, style_check.py and the rules file is identical; the sync script passes

Exit status 0 when every test passes, 1 otherwise. Standard library only.
"""

import json
import os
import re
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STYLE_SKILLS = ["curated-evidence-page", "field-guide", "mechanism-essay", "one-idea-post", "patterns-survey",
                "principle-column", "reportage-deep-dive", "strategy-pattern-essay", "taxonomy-explainer",
                "technical-principles-essay", "thesis-first-note"]
ALL_SKILLS = ["humanizer"] + STYLE_SKILLS


def skill_dir(root, name):
    nested = os.path.join(root, name, name)
    return nested if os.path.isfile(os.path.join(nested, "SKILL.md")) else os.path.join(root, name)


def py(args, stdin=None):
    p = subprocess.run([sys.executable, "-I", "-B"] + args, input=stdin, capture_output=True, text=True, cwd=HERE)
    return p.returncode, p.stdout, p.stderr


def finding_matches(f, want):
    for k, v in want.items():
        if k in ("category", "severity"):
            if f.get(k) != v:
                return False
        elif v.lower() not in str(f.get(k, "")).lower():
            return False
    return True


def run_lint(root):
    lint = os.path.join(skill_dir(root, "humanizer"), "scripts", "lint.py")
    results = []
    for c in json.load(open(os.path.join(HERE, "lint_cases.json"), encoding="utf-8")):
        if "argv_only" in c:
            code, out, _ = py([lint] + c["argv_only"])
            data = None
        else:
            code, out, _ = py([lint, "-", "--json"] + c.get("args", []), stdin=c["text"])
            try:
                data = json.loads(out)
            except ValueError:
                data = None
        problems = []
        for e in c["expect"]:
            if "exit" in e:
                if code != e["exit"]:
                    problems.append("exit %d, wanted %d" % (code, e["exit"]))
            elif "stdout" in e:
                if e["stdout"] not in out:
                    problems.append("output lacks %r" % e["stdout"])
            elif data is None:
                problems.append("no JSON report (exit %d)" % code)
                break
            elif "hard" in e:
                if data["hard"] != e["hard"]:
                    problems.append("%d hard findings, wanted %d: %s" % (data["hard"], e["hard"], "; ".join(
                        "%s/%s" % (f["category"], f["note"]) for f in data["findings"] if f["severity"] == "hard")[:160]))
            elif "has" in e:
                if not any(finding_matches(f, e["has"]) for f in data["findings"]):
                    problems.append("no finding %s" % json.dumps(e["has"]))
            elif "lacks" in e:
                hit = [f for f in data["findings"] if finding_matches(f, e["lacks"])]
                if hit:
                    problems.append("unwanted %s/%s: %s" % (hit[0]["category"], hit[0]["severity"], hit[0]["note"]))
        results.append({"suite": "lint", "id": c["id"], "item": c["item"], "passed": not problems, "detail": "; ".join(problems)})

    cat = json.load(open(os.path.join(HERE, "vocab_catalogue.json"), encoding="utf-8"))
    missed = []
    for w in cat["words"]:
        code, out, _ = py([lint, "-", "--json"], stdin=cat["template"].format(w=w))
        try:
            data = json.loads(out)
        except ValueError:
            missed.append(w)
            continue
        if not any(f["category"] in ("vocabulary", "filler", "phrase") for f in data["findings"]):
            missed.append(w)
    results.append({"suite": "lint", "id": "vocab-catalogue-all-linted", "item": cat["item"], "passed": not missed,
                    "detail": ("not flagged: " + ", ".join(missed)) if missed else "%d words" % len(cat["words"])})
    return results


def run_style(root):
    results = []
    path = os.path.join(HERE, "style_cases.json")
    if not os.path.exists(path):
        return [{"suite": "style", "id": "style_cases.json", "item": 0, "passed": False, "detail": "run build_cases.py first"}]
    for c in json.load(open(path, encoding="utf-8")):
        script = os.path.join(skill_dir(root, c["skill"]), "scripts", "style_check.py")
        args = [script, os.path.join(HERE, c["file"]), "--json"] + (["--variant", c["variant"]] if c["variant"] else [])
        code, out, _ = py(args)
        try:
            data = json.loads(out)
        except ValueError:
            data = None
        problems = []
        for e in c["expect"]:
            if "exit" in e:
                if code != e["exit"]:
                    fails = [x["check"] + ": " + x["evidence"] for x in (data or {}).get("checks", []) if not x["passed"]]
                    problems.append("exit %d, wanted %d%s" % (code, e["exit"], (" [" + " | ".join(fails)[:200] + "]") if fails else
                                                              (" (usage error: no variant support)" if code == 2 else "")))
            elif data is None:
                problems.append("no JSON report (exit %d)" % code)
                break
            else:
                hit = [x for x in data["checks"] if e["check"].lower() in x["check"].lower()]
                if not hit:
                    problems.append("check '%s' missing" % e["check"])
                elif hit[0]["passed"] != e["passed"]:
                    problems.append("'%s' %s: %s" % (hit[0]["check"], "passed" if hit[0]["passed"] else "failed", hit[0]["evidence"][:100]))
        results.append({"suite": "style", "id": c["id"] + (" --variant " + c["variant"] if c["variant"] else ""), "item": c["item"],
                        "passed": not problems, "detail": "; ".join(problems)})
    return results


def description(text):
    m = re.search(r"^description:\s*(.*)$", text, re.M)
    return m.group(1) if m else ""


def run_docs(root):
    results = []
    for c in json.load(open(os.path.join(HERE, "doc_checks.json"), encoding="utf-8")):
        problems = []
        for rel in c["files"]:
            name, sub = rel.split("/", 1)
            path = os.path.join(skill_dir(root, name), sub)
            if not os.path.exists(path):
                problems.append("%s missing" % rel)
                continue
            text = open(path, encoding="utf-8").read()
            desc = description(text)
            for rx in c.get("present", []):
                if not re.search(rx, text):
                    problems.append("%s lacks /%s/" % (rel, rx))
            for rx in c.get("absent", []):
                m = re.search(rx, text)
                if m:
                    problems.append("%s still has '%s'" % (rel, m.group(0)))
            for rx in c.get("description_present", []):
                if not re.search(rx, desc):
                    problems.append("%s description lacks /%s/" % (rel, rx))
            for rx in c.get("description_absent", []):
                if re.search(rx, desc):
                    problems.append("%s description has /%s/" % (rel, rx))
            if c.get("description_max") and len(desc) > c["description_max"]:
                problems.append("%s description is %d characters" % (rel, len(desc)))
            if c.get("description_max") and not re.search(r"^name:\s*%s\s*$" % re.escape(name), text, re.M):
                problems.append("%s name does not match its folder" % rel)
        results.append({"suite": "docs", "id": c["id"], "item": c["item"], "passed": not problems,
                        "detail": "; ".join(problems[:4]) + (" (+%d more)" % (len(problems) - 4) if len(problems) > 4 else "")})
    return results


def run_shared(root, tree):
    results = []
    for rel, names in [("scripts/lint.py", ALL_SKILLS), ("scripts/style_check.py", STYLE_SKILLS),
                       ("references/human-writing-rules.md", STYLE_SKILLS)]:
        texts = {}
        for n in names:
            p = os.path.join(skill_dir(root, n), rel)
            texts[n] = open(p, encoding="utf-8").read() if os.path.exists(p) else None
        variants = set(texts.values())
        results.append({"suite": "shared", "id": "identical " + rel, "item": 23, "passed": len(variants) == 1 and None not in variants,
                        "detail": "%d copies, %d distinct" % (len(texts), len(variants))})
    sync = os.path.join(tree, "tools", "sync_shared.py")
    if os.path.exists(sync):
        code, out, err = py([sync, "--check", "--skills", root, "--shared", os.path.join(tree, "shared")])
        results.append({"suite": "shared", "id": "sync_shared.py --check", "item": 23, "passed": code == 0,
                        "detail": (out + err).strip().splitlines()[-1] if (out + err).strip() else "exit %d" % code})
    else:
        results.append({"suite": "shared", "id": "sync_shared.py --check", "item": 23, "passed": False, "detail": "no tools/sync_shared.py"})
    return results


def main(argv):
    opts = {"--skills": os.path.join(os.path.dirname(HERE), "plugins", "writing-skills", "skills"), "--tree": os.path.dirname(HERE), "--label": "", "--out": None}
    i = 1
    while i < len(argv):
        if argv[i] in opts and i + 1 < len(argv):
            opts[argv[i]] = argv[i + 1]
            i += 2
        else:
            print(__doc__)
            return 2
    root = os.path.abspath(opts["--skills"])
    tree = os.path.abspath(opts["--tree"])
    results = run_lint(root) + run_style(root) + run_docs(root) + run_shared(root, tree)
    passed = sum(r["passed"] for r in results)
    lines = ["writing-skills tests%s: %d of %d passed" % ((" (" + opts["--label"] + ")") if opts["--label"] else "", passed, len(results)),
             "skills: %s" % root, ""]
    for suite in ("lint", "style", "docs", "shared"):
        rs = [r for r in results if r["suite"] == suite]
        lines.append("%s: %d of %d passed" % (suite, sum(r["passed"] for r in rs), len(rs)))
        for r in rs:
            lines.append("  %s  [item %2s] %s%s" % ("ok  " if r["passed"] else "FAIL", r["item"], r["id"],
                                                 ("  ->  " + r["detail"]) if (r["detail"] and not r["passed"]) else ""))
        lines.append("")
    text = "\n".join(lines)
    print(text)
    if opts["--out"]:
        with open(opts["--out"], "w", encoding="utf-8") as fh:
            fh.write(text + "\n")
        with open(os.path.splitext(opts["--out"])[0] + ".json", "w", encoding="utf-8") as fh:
            json.dump(results, fh, indent=1)
    return 0 if passed == len(results) else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
