"""Offline package checks; no model calls or third-party dependencies.

Installation checks retain their newly created scratch directory rather than
deleting files. The operating system's temp-directory policy controls its life.
"""

import hashlib
import re
import shutil
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = {
    "broad-explorer", "data-analyst", "diagnostician", "discovery",
    "implementer", "research-scout", "reviewer", "security-auditor",
}
READ_ONLY = EXPECTED - {"implementer"}


def read_definition(path):
    text = path.read_text(encoding="utf-8")
    parts = text.split("---", 2)
    if len(parts) != 3 or parts[0] or not parts[1].strip():
        raise ValueError("missing frontmatter")
    fields = {}
    for line in parts[1].strip().splitlines():
        key, separator, value = line.partition(":")
        if not separator or key in fields or not value.strip():
            raise ValueError("invalid or duplicate scalar field")
        fields[key] = value.strip()
    if not parts[2].strip():
        raise ValueError("empty instructions")
    return fields, parts[2]


class DefinitionTests(unittest.TestCase):
    def test_exact_role_set(self):
        self.assertEqual({p.stem for p in (ROOT / "agents").glob("*.md")}, EXPECTED)

    def test_frontmatter_and_names(self):
        for path in (ROOT / "agents").glob("*.md"):
            with self.subTest(path=path.name):
                fields, body = read_definition(path)
                self.assertEqual(fields["name"], path.stem)
                self.assertRegex(fields["name"], r"^[a-z][a-z-]*$")
                self.assertIn(fields["model"], {"haiku", "sonnet", "opus"})
                self.assertIn("description", fields)
                self.assertIn("tools", fields)
                self.assertNotIn("maxTurns", fields)
                if "effort" in fields:
                    self.assertEqual(fields["effort"], "high")
                self.assertTrue(body.strip())

    def test_read_only_tool_boundaries(self):
        for name in READ_ONLY:
            fields, _ = read_definition(ROOT / "agents" / (name + ".md"))
            self.assertFalse({"Bash", "Write", "Edit", "Agent"} & set(fields["tools"].split(", ")))

    def test_implementer_has_explicit_editing_tools(self):
        fields, body = read_definition(ROOT / "agents/implementer.md")
        self.assertTrue({"Bash", "Write", "Edit"} <= set(fields["tools"].split(", ")))
        self.assertIn("explicit authorization", body)
        self.assertIn("independent reviewer", body)

    def test_standalone_prompts(self):
        for path in (ROOT / "agents").glob("*.md"):
            text = path.read_text(encoding="utf-8")
            self.assertNotRegex(text, r"[A-Za-z]:[\\/]|/(?:home|Users)/|\.\./")
            self.assertNotIn(".md)", text)
            self.assertTrue(text.isascii(), path.name)

    def test_no_builtin_override(self):
        self.assertFalse((ROOT / "agents/Explore.md").exists())
        self.assertNotIn("Explore", EXPECTED)


class InstallationTests(unittest.TestCase):
    def test_copy_to_clean_project(self):
        with tempfile.TemporaryDirectory(prefix="subagent-tiers-check-") as scratch:
            installed = Path(scratch) / "project/.claude/agents"
            installed.mkdir(parents=True)
            for source in (ROOT / "agents").glob("*.md"):
                shutil.copyfile(source, installed / source.name)
            self.assertEqual({p.stem for p in installed.glob("*.md")}, EXPECTED)
            for name in EXPECTED:
                source = ROOT / "agents" / (name + ".md")
                target = installed / source.name
                self.assertEqual(hashlib.sha256(source.read_bytes()).digest(), hashlib.sha256(target.read_bytes()).digest())
                fields, body = read_definition(target)
                self.assertEqual(fields["name"], name)
                self.assertTrue(body.strip())

    def test_positive_control_rejects_bad_definition(self):
        with tempfile.TemporaryDirectory(prefix="subagent-tiers-negative-") as scratch:
            broken = Path(scratch) / "broken.md"
            broken.write_text("Instructions without frontmatter", encoding="utf-8")
            with self.assertRaises(ValueError):
                read_definition(broken)


class DocumentationTests(unittest.TestCase):
    def test_relative_markdown_links(self):
        for path in ROOT.rglob("*.md"):
            if ".git" in path.parts:
                continue
            for target in re.findall(r"\]\(([^)]+)\)", path.read_text(encoding="utf-8")):
                if "://" in target or target.startswith(("#", "mailto:")):
                    continue
                target = target.split("#", 1)[0]
                if target:
                    self.assertTrue((path.parent / target).exists(), f"{path.name}: {target}")

    def test_tiers_are_guidance_not_execution(self):
        text = (ROOT / "docs/TIERS.md").read_text(encoding="utf-8")
        for tier in ("K0", "K1", "K2", "K3"):
            self.assertIn(tier, text)
        self.assertIn("not automatic routing rules", text)
        self.assertIn("No K3 agent is bundled", text)


if __name__ == "__main__":
    unittest.main()
