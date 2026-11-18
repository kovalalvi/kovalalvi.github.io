# /// script
# requires-python = ">=3.9"
# dependencies = ["markdown==3.7"]
# ///
"""Build the site into _site/.  Run: uv run build.py  (preview: python3 -m http.server -d _site)"""
import html
import shutil
from datetime import datetime, timezone
from email.utils import format_datetime
from pathlib import Path

import markdown

ROOT = Path(__file__).parent
OUT = ROOT / "_site"
SITE_URL = "https://kovalalvi.github.io"
TELEGRAM = "https://t.me/neural_cell"
BASE = (ROOT / "templates/base.html").read_text()


def page(title, description, url_path, content, og_type="website"):
    out = BASE
    for key, value in {
        "title": html.escape(title),
        "description": html.escape(description),
        "url": SITE_URL + url_path,
        "og_type": og_type,
    }.items():
        out = out.replace("{{" + key + "}}", value)
    return out.replace("{{content}}", content)  # content last: post text may contain "{{"


def write(url_path, text):
    path = OUT / url_path.lstrip("/") / "index.html" if url_path.endswith("/") else OUT / url_path.lstrip("/")
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text)


def obsidian_lists(md):
    """Obsidian starts a list right after a paragraph line; Python-Markdown needs a blank line first."""
    lines, out = md.split("\n"), []
    for i, line in enumerate(lines):
        is_item = line.lstrip().startswith(("- ", "* ", "1. "))
        prev = lines[i - 1] if i else ""
        if is_item and prev.strip() and not prev.lstrip().startswith(("- ", "* ", "1. ")):
            out.append("")
        out.append(line)
    return "\n".join(out)


def read_post(path):
    """posts/YYYY-MM-DD-slug.md with a `key: value` header between --- lines."""
    text = path.read_text()
    if not text.startswith("---\n"):
        raise SystemExit(f"{path}: no front matter")
    head, body = text[4:].split("\n---\n", 1)
    meta = dict(line.split(": ", 1) for line in head.strip().splitlines())
    for key in ("title", "description", "tag"):
        if key not in meta:
            raise SystemExit(f"{path}: missing '{key}' in front matter")
    date = datetime.strptime(path.name[:10], "%Y-%m-%d").replace(tzinfo=timezone.utc)
    return {
        **meta,
        "date": date,
        "url": f"/blog/{path.stem[11:]}/",
        "html": markdown.markdown(obsidian_lists(body),extensions=["extra", "sane_lists", "toc"]),
    }


def post_list(posts):
    rows = "".join(
        f'<li><span class="date">{p["date"]:%b %d, %Y}</span>'
        f'<span><a href="{p["url"]}">{html.escape(p["title"])}</a> <span class="tag">· {p["tag"]}</span></span></li>'
        for p in posts
    )
    return f'<ul class="posts">{rows}</ul>'


def post_page(p):
    discuss = f'<a href="{p["telegram"]}">Discuss on Telegram (RU)</a>' if "telegram" in p else f'<a href="{TELEGRAM}">Telegram channel (RU)</a>'
    return f"""<article>
<header><h1>{html.escape(p["title"])}</h1>
<div class="meta">{p["date"]:%B %d, %Y} · {p["tag"]}</div></header>
{p["html"]}
<div class="post-footer"><a href="/blog/">← All posts</a>{discuss}</div>
</article>
<script src="/toc.js" defer></script>"""


def feed(posts):
    items = "".join(
        f"""<item><title>{html.escape(p["title"])}</title><link>{SITE_URL}{p["url"]}</link>
<guid>{SITE_URL}{p["url"]}</guid><pubDate>{format_datetime(p["date"])}</pubDate>
<description>{html.escape(p["description"])}</description></item>"""
        for p in posts
    )
    return f"""<?xml version="1.0" encoding="utf-8"?>
<rss version="2.0"><channel><title>Aleksandr Kovalev</title><link>{SITE_URL}/</link>
<description>AI for brain-computer interfaces</description>{items}</channel></rss>
"""


def main():
    shutil.rmtree(OUT, ignore_errors=True)
    shutil.copytree(ROOT / "static", OUT)
    (OUT / ".nojekyll").touch()  # gh-pages branch: serve files as-is

    posts = sorted((read_post(p) for p in (ROOT / "posts").glob("*.md")), key=lambda p: p["date"], reverse=True)

    home = (ROOT / "templates/home.html").read_text().replace("{{posts}}", post_list(posts[:5]))
    write("/", page("Aleksandr Kovalev", "AI models for intracortical brain-computer interfaces.", "/", home))
    write("/blog/", page("Blog · Aleksandr Kovalev", "Notes on brain-computer interfaces and AI.", "/blog/",
                         f"<h1>Blog</h1>\n{post_list(posts)}"))
    for p in posts:
        write(p["url"], page(p["title"], p["description"], p["url"], post_page(p), og_type="article"))
    write("/feed.xml", feed(posts))
    print(f"built {len(posts)} posts → {OUT}")


if __name__ == "__main__":
    main()
