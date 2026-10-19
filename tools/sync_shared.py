#!/usr/bin/env python3
"""Copy the shared files into every skill, then fail if any copy differs from its source.

    python3 tools/sync_shared.py            copy shared/ into the skills, then verify
    python3 tools/sync_shared.py --check    verify only; change nothing
    python3 tools/sync_shared.py --skills DIR --shared DIR

shared/lint.py               -> <skill>/scripts/lint.py for all twelve skills
shared/style_check.py        -> <skill>/scripts/style_check.py for the eleven style skills
shared/human-writing-rules.md -> <skill>/references/human-writing-rules.md for the eleven style skills

Edit the file in shared/, never a copy. Exit status 0 when every copy matches, 1 when one
differs or is missing, 2 on a usage error. Standard library only.
"""

import filecmp
import os
import shutil
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
STYLE_SKILLS = ["curated-evidence-page", "field-guide", "mechanism-essay", "one-idea-post", "patterns-survey",
                "principle-column", "reportage-deep-dive", "strategy-pattern-essay", "taxonomy-explainer",
                "technical-principles-essay", "thesis-first-note"]
TARGETS = [
    ("lint.py", "scripts/lint.py", ["humanizer"] + STYLE_SKILLS),
    ("style_check.py", "scripts/style_check.py", STYLE_SKILLS),
    ("human-writing-rules.md", "references/human-writing-rules.md", STYLE_SKILLS),
]


def skill_dir(skills, name):
    """An unzipped .skill file nests one level (DIR/name/name/SKILL.md); accept either layout."""
    nested = os.path.join(skills, name, name)
    return nested if os.path.isfile(os.path.join(nested, "SKILL.md")) else os.path.join(skills, name)


def main(argv):
    opts = {"--skills": os.path.join(os.path.dirname(HERE), "plugins", "writing-skills", "skills"),
            "--shared": os.path.join(os.path.dirname(HERE), "shared")}
    check_only = False
    i = 1
    while i < len(argv):
        if argv[i] == "--check":
            check_only = True
            i += 1
        elif argv[i] in opts and i + 1 < len(argv):
            opts[argv[i]] = argv[i + 1]
            i += 2
        else:
            print(__doc__)
            return 2
    skills, shared = opts["--skills"], opts["--shared"]
    copied, bad = 0, []
    for src_name, rel, names in TARGETS:
        src = os.path.join(shared, src_name)
        if not os.path.isfile(src):
            print("missing source %s" % src)
            return 1
        for n in names:
            dst = os.path.join(skill_dir(skills, n), rel)
            if not check_only and not (os.path.isfile(dst) and filecmp.cmp(src, dst, shallow=False)):
                os.makedirs(os.path.dirname(dst), exist_ok=True)
                shutil.copyfile(src, dst)
                copied += 1
            if not (os.path.isfile(dst) and filecmp.cmp(src, dst, shallow=False)):
                bad.append(os.path.join(n, rel))
    for b in bad:
        print("differs from shared/: %s" % b)
    total = sum(len(names) for _, _, names in TARGETS)
    print("%s%d of %d copies match shared/" % ("" if check_only else "copied %d; " % copied, total - len(bad), total))
    return 1 if bad else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
