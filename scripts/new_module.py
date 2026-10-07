"""Scaffold a new module doc and lab folder from the module template.

Usage: uv run python scripts/new_module.py 26 "My Topic" [--level L3]
"""

from __future__ import annotations

import argparse
import re
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
TEMPLATE = ROOT / "docs" / "templates" / "module-design-doc.md"


def slugify(title: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("number", type=int)
    parser.add_argument("title")
    parser.add_argument("--level", default="L?")
    args = parser.parse_args()

    num = f"{args.number:02d}"
    slug = slugify(args.title)
    doc_dir = ROOT / "docs" / "modules" / f"{num}-{slug}"
    lab_dir = ROOT / "labs" / f"{num}_{slug.replace('-', '_')}"
    if doc_dir.exists():
        raise SystemExit(f"{doc_dir} already exists")

    text = TEMPLATE.read_text()
    text = text.replace("  - template\n", f"  - {args.level}\n", 1)
    text = text.replace("# NN. Module Title", f"# {num}. {args.title}", 1)
    text = text.replace("**Level:** L?", f"**Level:** {args.level}", 1)
    text = text.replace("**Status:** stub / draft / complete", "**Status:** stub", 1)
    text = text.replace("YYYY-MM-DD", date.today().isoformat(), 1)
    text = text.replace("labs/NN_slug/", f"{lab_dir.relative_to(ROOT)}/")

    doc_dir.mkdir(parents=True)
    (doc_dir / "index.md").write_text(text)
    lab_dir.mkdir(parents=True, exist_ok=True)
    module_doc = f"docs/modules/{num}-{slug}/index.md"
    readme = f"# Lab {num}: {args.title}\n\nModule doc: `{module_doc}`\n\n## Task\n\nTODO\n"
    (lab_dir / "README.md").write_text(readme)
    print(f"Created {doc_dir.relative_to(ROOT)}/index.md and {lab_dir.relative_to(ROOT)}/README.md")
    print(
        "Next: add the module to docs/modules/.nav.yml (sidebar), docs/modules/index.md, "
        "and docs/learning-path/progress.md"
    )


if __name__ == "__main__":
    main()
