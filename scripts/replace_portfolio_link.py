"""Replace the portfolio hyperlink inside resume PDFs.

The resumes under ``resume/`` contain a "portfolio" link that used to point to
a Notion page. This script rewrites the ``/URI`` value of every matching link
annotation so the resumes now point to the new GitHub Pages portfolio.

Usage:
    python3 scripts/replace_portfolio_link.py
    python3 scripts/replace_portfolio_link.py --dry-run
    python3 scripts/replace_portfolio_link.py \
        --old "notion.site" \
        --new "https://nthgiao0312.github.io/gracenguyen-portfolio/"

Only hyperlink annotations whose current URI contains ``--old`` (substring
match) are rewritten. Other links (e.g. LinkedIn) are left untouched.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Iterable

from pypdf import PdfReader, PdfWriter
from pypdf.generic import NameObject, TextStringObject


DEFAULT_OLD_MATCH = "notion.site"
DEFAULT_NEW_URL = "https://nthgiao0312.github.io/gracenguyen-portfolio/"
DEFAULT_RESUME_DIR = Path(__file__).resolve().parent.parent / "resume"


def replace_links_in_pdf(
    pdf_path: Path,
    old_match: str,
    new_url: str,
    output_path: Path | None = None,
) -> int:
    """Rewrite matching link annotations in ``pdf_path``.

    Returns the number of annotations that were rewritten. When
    ``output_path`` is ``None`` the file is rewritten in place.
    """
    reader = PdfReader(str(pdf_path))
    writer = PdfWriter(clone_from=reader)

    replaced = 0
    for page in writer.pages:
        annots = page.get("/Annots")
        if not annots:
            continue
        for annot_ref in annots:
            annot = annot_ref.get_object()
            if annot.get("/Subtype") != "/Link":
                continue
            action = annot.get("/A")
            if action is None:
                continue
            action = action.get_object()
            uri = action.get("/URI")
            if uri is None:
                continue
            if old_match in str(uri):
                action[NameObject("/URI")] = TextStringObject(new_url)
                replaced += 1

    target = output_path if output_path is not None else pdf_path
    with open(target, "wb") as fh:
        writer.write(fh)
    return replaced


def iter_pdfs(resume_dir: Path) -> Iterable[Path]:
    return sorted(p for p in resume_dir.glob("*.pdf") if p.is_file())


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument(
        "--resume-dir",
        type=Path,
        default=DEFAULT_RESUME_DIR,
        help="Directory containing the resume PDFs (default: %(default)s).",
    )
    parser.add_argument(
        "--old",
        default=DEFAULT_OLD_MATCH,
        help=(
            "Substring a hyperlink must contain to be rewritten "
            "(default: %(default)s)."
        ),
    )
    parser.add_argument(
        "--new",
        default=DEFAULT_NEW_URL,
        help="The replacement URL (default: %(default)s).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Only report what would change; do not write any files.",
    )
    args = parser.parse_args(argv)

    resume_dir: Path = args.resume_dir
    if not resume_dir.is_dir():
        print(f"error: {resume_dir} is not a directory", file=sys.stderr)
        return 2

    pdfs = list(iter_pdfs(resume_dir))
    if not pdfs:
        print(f"No PDFs found in {resume_dir}.")
        return 0

    total_replaced = 0
    for pdf in pdfs:
        if args.dry_run:
            reader = PdfReader(str(pdf))
            count = 0
            for page in reader.pages:
                for annot_ref in page.get("/Annots") or []:
                    annot = annot_ref.get_object()
                    if annot.get("/Subtype") != "/Link":
                        continue
                    action = annot.get("/A")
                    if not action:
                        continue
                    uri = action.get_object().get("/URI")
                    if uri and args.old in str(uri):
                        count += 1
            print(f"[dry-run] {pdf.name}: would replace {count} link(s)")
            total_replaced += count
        else:
            count = replace_links_in_pdf(pdf, args.old, args.new)
            print(f"{pdf.name}: replaced {count} link(s)")
            total_replaced += count

    print(f"\nDone. {total_replaced} link(s) {'would be ' if args.dry_run else ''}replaced.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
