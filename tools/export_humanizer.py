#!/usr/bin/env python3
"""Copy the humanizer into a checkout of the standalone repository, github.com/3orionkings/humanizer.

    python3 tools/export_humanizer.py ../humanizer           copy the files, then verify
    python3 tools/export_humanizer.py ../humanizer --check   verify only; change nothing

This repository is the source of the humanizer. The standalone repository holds the same skill
at its root (SKILL.md, scripts/, references/) for Claude Code and skill installers, a second copy
under codex/skills/humanizer/ for its Codex and ChatGPT plugin (Codex reads skills from a folder of
skill folders), the linter's test cases, and its own README, manifests and CI. Run this after any
change to the humanizer or to shared/lint.py, then commit in the standalone checkout. Never edit the exported copies there.

Exit status 0 when every copy matches, 1 when one differs or is missing, 2 on a usage error.
Standard library only.
"""

import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKILL = os.path.join(ROOT, "plugins", "writing-skills", "skills", "humanizer")

# (source, destination relative to the standalone root)
FILES = [
    (os.path.join(SKILL, "SKILL.md"), "SKILL.md"),
    (os.path.join(SKILL, "scripts", "lint.py"), os.path.join("scripts", "lint.py")),
    (os.path.join(SKILL, "references", "ai-tells.md"), os.path.join("references", "ai-tells.md")),
    (os.path.join(SKILL, "SKILL.md"), os.path.join("codex", "skills", "humanizer", "SKILL.md")),
    (os.path.join(SKILL, "scripts", "lint.py"), os.path.join("codex", "skills", "humanizer", "scripts", "lint.py")),
    (os.path.join(SKILL, "references", "ai-tells.md"), os.path.join("codex", "skills", "humanizer", "references", "ai-tells.md")),
    (os.path.join(ROOT, "tests", "lint_cases.json"), os.path.join("tests", "lint_cases.json")),
    (os.path.join(ROOT, "tests", "vocab_catalogue.json"), os.path.join("tests", "vocab_catalogue.json")),
    (os.path.join(ROOT, "tests", "cases", "lint", "author-sample-dashes.txt"),
     os.path.join("tests", "cases", "lint", "author-sample-dashes.txt")),
    (os.path.join(ROOT, "tests", "cases", "lint", "author-sample-plain.txt"),
     os.path.join("tests", "cases", "lint", "author-sample-plain.txt")),
]

# The skill's Files section points at this repository's sync tool; the standalone copy points here.
SKILL_NOTE = [(
        "The same file ships in every style skill; edit it only through `tools/sync_shared.py` in the source tree.",
        "The same linter ships with every skill in the writing-skills collection "
        "(github.com/3orionkings/writing-skills), which is its source.",
)]
REWRITES = {"SKILL.md": SKILL_NOTE, os.path.join("codex", "skills", "humanizer", "SKILL.md"): SKILL_NOTE}


def exported(src, rel):
    with open(src, encoding="utf-8") as fh:
        text = fh.read()
    for old, new in REWRITES.get(rel, []):
        if old not in text:
            raise SystemExit("export_humanizer: expected text not found in %s: %r" % (rel, old[:60]))
        text = text.replace(old, new)
    return text


def main(argv):
    args = [a for a in argv[1:] if not a.startswith("--")]
    check = "--check" in argv
    unknown = [a for a in argv[1:] if a.startswith("--") and a != "--check"]
    if unknown or len(args) != 1:
        print(__doc__)
        return 2
    dest = os.path.abspath(args[0])
    if not os.path.isdir(dest):
        print("export_humanizer: %s is not a directory" % dest)
        return 2
    bad = 0
    for src, rel in FILES:
        target = os.path.join(dest, rel)
        if rel in REWRITES:
            want = exported(src, rel)
            if not check:
                os.makedirs(os.path.dirname(target) or dest, exist_ok=True)
                with open(target, "w", encoding="utf-8") as fh:
                    fh.write(want)
            same = os.path.isfile(target) and open(target, encoding="utf-8").read() == want
        else:
            if not check:
                os.makedirs(os.path.dirname(target), exist_ok=True)
                shutil.copyfile(src, target)
            same = os.path.isfile(target) and open(target, "rb").read() == open(src, "rb").read()
        if not same:
            bad += 1
            print("differs: %s" % rel)
    print("%s %d files; %d of %d match" % ("checked" if check else "exported", len(FILES), len(FILES) - bad, len(FILES)))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
