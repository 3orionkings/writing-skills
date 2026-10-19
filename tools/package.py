#!/usr/bin/env python3
"""Build standalone skill packages from plugins/writing-skills/skills.

    python3 tools/package.py              write to dist/
    python3 tools/package.py --out DIR

Writes one <name>.skill per skill (a zip holding <name>/..., the layout claude.ai and other
skill uploaders accept) and writing-skills.zip, which holds skills/<name>/... for every skill
so it can be unzipped straight into a skills directory:

    unzip dist/writing-skills.zip -d ~/.claude      # Claude Code
    unzip dist/writing-skills.zip -d ~/.agents      # Codex

The plugins themselves need no build step; marketplaces install them from the repository.
The shared-file check and tools/validate.py run first, and nothing is written if either fails.
Standard library only.
"""

import os
import subprocess
import sys
import zipfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
SKILLS = os.path.join(ROOT, "plugins", "writing-skills", "skills")
SKIP_DIRS = {"__pycache__", ".git", "dist"}
SKIP_FILES = {".DS_Store"}


def files_under(base):
    for root, dirs, files in os.walk(base):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for f in sorted(files):
            if f not in SKIP_FILES and not f.endswith(".pyc"):
                yield os.path.join(root, f)


def preflight():
    for script, args in (("sync_shared.py", ["--check"]), ("validate.py", [])):
        r = subprocess.run([sys.executable, "-I", "-B", os.path.join(HERE, script)] + args,
                           capture_output=True, text=True)
        if r.returncode != 0:
            print(r.stdout + r.stderr)
            print("not packaging: tools/%s failed" % script)
            return False
    return True


def main(argv):
    out = os.path.join(ROOT, "dist")
    if len(argv) == 3 and argv[1] == "--out":
        out = argv[2]
    elif len(argv) != 1:
        print(__doc__)
        return 2
    if not preflight():
        return 1
    os.makedirs(out, exist_ok=True)
    names = sorted(n for n in os.listdir(SKILLS) if os.path.isfile(os.path.join(SKILLS, n, "SKILL.md")))
    for n in names:
        path = os.path.join(out, n + ".skill")
        with zipfile.ZipFile(path, "w", zipfile.ZIP_DEFLATED) as z:
            for f in files_under(os.path.join(SKILLS, n)):
                z.write(f, os.path.relpath(f, SKILLS))
        print("wrote", path)
    combined = os.path.join(out, "writing-skills.zip")
    with zipfile.ZipFile(combined, "w", zipfile.ZIP_DEFLATED) as z:
        for f in files_under(SKILLS):
            z.write(f, os.path.join("skills", os.path.relpath(f, SKILLS)))
    print("wrote", combined)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
