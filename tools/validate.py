#!/usr/bin/env python3
"""Check that the plugin manifests, marketplaces, skills and docs agree with each other.

    python3 tools/validate.py

Checks:
  - every manifest and marketplace file is valid JSON
  - name, version, description, license and links match across plugin.json,
    .codex-plugin/plugin.json, .claude-plugin/plugin.json and the Claude marketplace entry
  - the newest release in CHANGELOG.md is the manifest version
  - each marketplace entry resolves to the plugin folder and has the fields its harness needs
  - .codex-plugin/ holds plugin.json and nothing else
  - every skill has SKILL.md whose name matches its folder (lowercase, hyphens, 64 characters
    at most) and a description of 1,024 characters at most, plus agents/openai.yaml with a
    display name and a short description of 64 characters at most
  - README.md names every skill
  - no file names a person on the forbidden list (the writers whose published work informed
    the forms, and the authors of the studies the catalogue cites); the list is stored as
    SHA-256 hashes of lowercase words and word pairs, so this file does not name them either

Prints a warning, without failing, when the skill descriptions together exceed Codex's
default skill-list budget of 8,000 characters. Exit status 0 when every check passes,
1 otherwise. Standard library only.
"""

import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PLUGIN = os.path.join(ROOT, "plugins", "writing-skills")
SKILLS = os.path.join(PLUGIN, "skills")
NAME_RE = re.compile(r"^[a-z0-9]+(?:-[a-z0-9]+)*$")
IDENTITY = ("name", "version", "description", "license", "homepage", "repository", "author")
CODEX_BUDGET = 8000
SKIP_DIRS = {".git", "dist", "__pycache__"}
BINARY = (".zip", ".skill", ".png", ".jpg", ".jpeg", ".gif", ".pdf", ".pyc")

# SHA-256 of names that must never appear in the repository, as lowercase single words or
# two-word sequences. To add a name, hash it the same way: sha256("first last".encode()).
FORBIDDEN_NAME_HASHES = {
    "07cd6ec7390d32ebc7a9483fb278b5b14c072ad3d2a414df509a83018b767b11", "0e10b1cf1c2673d885a2c31fefaf8c778bfa4340495a52c8c61e1cde152edf46",
    "15a541aae5bfd3cfc572c2fea793ea49442ca2a7f0008cf9cfd4151018570917", "168f11828b47eb4f127bf660f8e3285526e3308a03da1f3ffc1814c968990dbb",
    "1753c3be0a37cc9bb82cb546f7d0df14186424e3dbc1e1ab5ab452a680690418", "1b655480bea5d70b78a9ce02df88b3c35a57eedef9d09db9c21cfaf7b9d00978",
    "1f60f69f90127eb474c67f40dbbd9590212351be034fabe16e61236dcd9a861d", "281aca1a80b52620bd717e8b14a0386b8ada92ae859ac2c8a2ac222efa02edbb",
    "29277a80b244f58cac65955e69922e7aa04957688a194b1a91fda859f7c6362a", "2dbe33913ae5d6b16a801119f5fa1c419620c26d1a456e01490d697eb9b12589",
    "3495d79fd96988b4ea03923356cd92870273b16719b89f78f5fc897a54adbe28", "39593e8a6750dd0362c2fffb667ef9922daf0c9bd4d4fa356f020653cc575244",
    "3c1d36ce555d88f2b70c11d663579a9ca436a038c539de44f9945fec93e4053d", "3e02a0ac36a641b26683c9d5881e8b651ba1f495610fd66cd29ad9aa9c3bd665",
    "48cb0041ceae7ad8dc1d6af69cde36b531e7104177140f96cf536257872b1236", "51af5ffff51029a50790ad8c5b370956bc7e0c9eea39074618d028cc25ae59f6",
    "58cff11af9c89b7db2791bf92a459578f2bd5820c599259b11cc3fbc99156b79", "6301ea260891ccad8bd0b63b55fd685ec78a586b7d7f4634069c53e242dccb68",
    "6428a8fbbb0e120528bb604a66787102280e1b5e26db76633ce37c8a4526e445", "783e3d318953684721d021c7db0756dfda3654b27a1e2dd5a7f5ffb2f7fd8b32",
    "860b701dd62bc9226ddf838a3010a3a9c0bb1ca3aced05befd6f17e97efebe4c", "8f0ceb29ab0de86a283b3c069d17504158b37195538a06512375354c8ba34572",
    "9de053a064b57122fc5a499d0c4a52fdab7ee42a1e81432040e0aa8a4ab658cb", "a641f6f0abcd11424c522bc040a6da566f9b30116c29b0dd95f06dc7d655f73c",
    "ae33cb0b4251e9b847780ca858258e3caf9a009e97f13645464f14a58c93de26", "af5df0db1afe88190f9215bb66b8eefab08a95f2a2b52b7c5b0e01a526843cdf",
    "b437994f06e2368a09e3727249eb7fe0342c68930b7ba8de17adc8ed0f48476b", "c5f44825daa4b7e2a47fa76707173fcb8bd33c8d48daf293598b640f0e43ad16",
    "c7e96e2b79ef62d309a27744793926058156eea08da7f762609de26e04450723", "c80dd7193e8558716e7e9a3fb482d3d99ec1285719e1d1719643db75d1c472b1",
    "d0df918b14039e9b673ec659fccb9cdd35c0125b28bfefcd4af172ef199895a1", "d7d978de6f31e7fba53024dd249ba0b4b28d201056543f3d49b83b9c4dd84657",
    "ec87d0e0735ce8d20ddf792630a066ab99a7e3370281adc2eba9c3192033ff7f", "fa9bb27bf1e7fdce2e663270be1c9a9fb39041360aa61316ab1ede796c8dcbb0",
    "fbe09bf1edb07a0a5d4aef0563c7bec7705fc00e90b8ae8c994b13f14ba8c8a4",
}

errors, warnings = [], []


def rel(path):
    return os.path.relpath(path, ROOT)


def load(path):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except FileNotFoundError:
        errors.append("missing %s" % rel(path))
    except ValueError as exc:
        errors.append("%s is not valid JSON: %s" % (rel(path), exc))
    return None


def frontmatter(text):
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    if not m:
        return None
    fields, key = {}, None
    for line in m.group(1).splitlines():
        km = re.match(r"^([A-Za-z_][\w-]*):\s?(.*)$", line)
        if km:
            key = km.group(1)
            fields[key] = km.group(2).strip()
        elif key and line.startswith((" ", "\t")):
            fields[key] = (fields[key] + " " + line.strip()).strip()
    for k, v in fields.items():
        if len(v) >= 2 and v[0] == v[-1] and v[0] in "\"'":
            fields[k] = v[1:-1]
    return fields


def yaml_value(text, key):
    m = re.search(r"^\s+%s:\s*\"((?:[^\"\\]|\\.)*)\"\s*$" % re.escape(key), text, re.M)
    return m.group(1) if m else None


def check_manifests():
    portable = load(os.path.join(PLUGIN, "plugin.json"))
    codex = load(os.path.join(PLUGIN, ".codex-plugin", "plugin.json"))
    claude = load(os.path.join(PLUGIN, ".claude-plugin", "plugin.json"))
    claude_mp = load(os.path.join(ROOT, ".claude-plugin", "marketplace.json"))
    codex_mp = load(os.path.join(ROOT, ".agents", "plugins", "marketplace.json"))
    if None in (portable, codex, claude, claude_mp, codex_mp):
        return None

    if not str(portable.get("$schema", "")).startswith("https://agent-plugins.org/schemas/"):
        errors.append("plugins/writing-skills/plugin.json needs the Agent Plugins $schema")
    if "extensions" in portable:
        errors.append("plugin.json must not carry an extensions block, or Codex ignores .codex-plugin/plugin.json")
    for label, m in (("plugin.json", portable), (".codex-plugin/plugin.json", codex), (".claude-plugin/plugin.json", claude)):
        for k in IDENTITY:
            if k not in m:
                errors.append("%s is missing %s" % (label, k))
            elif m[k] != portable.get(k):
                errors.append("%s: %s differs from plugin.json" % (label, k))
    if codex.get("skills") != "./skills/":
        errors.append('.codex-plugin/plugin.json needs "skills": "./skills/"')
    iface = codex.get("interface", {})
    for k in ("displayName", "shortDescription", "developerName", "category"):
        if not iface.get(k):
            errors.append(".codex-plugin/plugin.json interface is missing %s" % k)
    extra = sorted(set(os.listdir(os.path.join(PLUGIN, ".codex-plugin"))) - {"plugin.json"})
    if extra:
        errors.append(".codex-plugin/ must hold only plugin.json, found %s" % ", ".join(extra))

    entries = [p for p in claude_mp.get("plugins", []) if p.get("name") == portable.get("name")]
    if len(entries) != 1:
        errors.append(".claude-plugin/marketplace.json needs exactly one entry named %s" % portable.get("name"))
    else:
        e = entries[0]
        for k in ("version", "description", "license"):
            if e.get(k) != portable.get(k):
                errors.append(".claude-plugin/marketplace.json entry: %s differs from plugin.json" % k)
        src = os.path.normpath(os.path.join(ROOT, e.get("source", "")))
        if src != PLUGIN:
            errors.append(".claude-plugin/marketplace.json source should be ./plugins/writing-skills")
    if claude_mp.get("metadata", {}).get("version") != portable.get("version"):
        errors.append(".claude-plugin/marketplace.json metadata.version differs from plugin.json")

    entries = [p for p in codex_mp.get("plugins", []) if p.get("name") == portable.get("name")]
    if len(entries) != 1:
        errors.append(".agents/plugins/marketplace.json needs exactly one entry named %s" % portable.get("name"))
    else:
        e = entries[0]
        src = e.get("source", {})
        path = src.get("path", "") if isinstance(src, dict) else src
        if not path.startswith("./") or os.path.normpath(os.path.join(ROOT, path)) != PLUGIN:
            errors.append(".agents/plugins/marketplace.json source.path should be ./plugins/writing-skills")
        policy = e.get("policy", {})
        for k in ("installation", "authentication"):
            if not policy.get(k):
                errors.append(".agents/plugins/marketplace.json policy is missing %s" % k)
        if not e.get("category"):
            errors.append(".agents/plugins/marketplace.json entry is missing category")
    return portable.get("version")


def check_changelog(version):
    try:
        text = open(os.path.join(ROOT, "CHANGELOG.md"), encoding="utf-8").read()
    except FileNotFoundError:
        errors.append("missing CHANGELOG.md")
        return
    m = re.search(r"^## \[(\d+\.\d+\.\d+)\]", text, re.M)
    if not m:
        errors.append("CHANGELOG.md has no '## [x.y.z]' release heading")
    elif version and m.group(1) != version:
        errors.append("newest CHANGELOG.md release is %s, manifests say %s" % (m.group(1), version))


def check_skills():
    names, total = [], 0
    for n in sorted(os.listdir(SKILLS)):
        d = os.path.join(SKILLS, n)
        if not os.path.isdir(d):
            continue
        names.append(n)
        path = os.path.join(d, "SKILL.md")
        if not os.path.isfile(path):
            errors.append("skills/%s has no SKILL.md" % n)
            continue
        fm = frontmatter(open(path, encoding="utf-8").read())
        if fm is None:
            errors.append("skills/%s/SKILL.md has no frontmatter" % n)
            continue
        name, desc = fm.get("name", ""), fm.get("description", "")
        if name != n:
            errors.append("skills/%s/SKILL.md name is %r, expected %r" % (n, name, n))
        if not NAME_RE.match(name) or len(name) > 64:
            errors.append("skills/%s: name must be lowercase words joined by hyphens, 64 characters at most" % n)
        if not desc:
            errors.append("skills/%s/SKILL.md has no description" % n)
        elif len(desc) > 1024:
            errors.append("skills/%s description is %d characters; the limit is 1,024" % (n, len(desc)))
        total += len(desc)
        ypath = os.path.join(d, "agents", "openai.yaml")
        if not os.path.isfile(ypath):
            errors.append("skills/%s has no agents/openai.yaml" % n)
            continue
        y = open(ypath, encoding="utf-8").read()
        short = yaml_value(y, "short_description")
        if not yaml_value(y, "display_name"):
            errors.append("skills/%s/agents/openai.yaml has no display_name" % n)
        if not short:
            errors.append("skills/%s/agents/openai.yaml has no short_description" % n)
        elif len(short) > 64:
            errors.append("skills/%s short_description is %d characters; keep it to 64" % (n, len(short)))
    if total > CODEX_BUDGET:
        warnings.append("skill descriptions total %d characters, over Codex's default %d-character skill list; "
                        "Codex shortens them unless skills.max_context_tokens is raised (see README)" % (total, CODEX_BUDGET))
    return names


def check_no_names():
    for base, dirs, files in os.walk(ROOT):
        dirs[:] = sorted(d for d in dirs if d not in SKIP_DIRS)
        for f in sorted(files):
            if f.endswith(BINARY):
                continue
            path = os.path.join(base, f)
            try:
                lines = open(path, encoding="utf-8").read().splitlines()
            except (UnicodeDecodeError, OSError):
                continue
            for i, line in enumerate(lines, 1):
                words = re.findall(r"[a-z0-9]+", line.lower())
                grams = words + [a + " " + b for a, b in zip(words, words[1:])]
                if any(hashlib.sha256(g.encode()).hexdigest() in FORBIDDEN_NAME_HASHES for g in grams):
                    errors.append("%s:%d names a person on the forbidden list" % (rel(path), i))


def check_readme(names):
    try:
        text = open(os.path.join(ROOT, "README.md"), encoding="utf-8").read()
    except FileNotFoundError:
        errors.append("missing README.md")
        return
    for n in names:
        if ("`%s`" % n) not in text:
            errors.append("README.md does not list the %s skill" % n)


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    version = check_manifests()
    check_changelog(version)
    names = check_skills()
    check_readme(names)
    check_no_names()
    for w in warnings:
        print("warning: " + w)
    for e in errors:
        print("error: " + e)
    print("validate: %d skills, version %s, %d error%s" % (len(names), version, len(errors), "" if len(errors) == 1 else "s"))
    return 1 if errors else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
