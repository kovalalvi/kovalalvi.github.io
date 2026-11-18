# kovalalvi.github.io

Personal site and blog. Plain HTML/CSS, one Python build script, no framework.

- `templates/home.html` — the home page. `{{posts}}` becomes the 5 latest posts.
- `templates/base.html` — the frame around every page.
- `posts/YYYY-MM-DD-slug.md` — a post, served at `/blog/slug/`. The date is when the post was written (the vault draft's date or first commit), not the day it went on the site. Front matter: `title`, `description`, `tag` (my work / review / digest / tutorial), optional `image` (preview card) , `affiliation` (default UMH, Spain) and `toc: h2` (left rail shows only h2, not h3).
- `figs/*.py` — generators for SVG figures in `static/fig/` (`papers.py`: paper thumbnails; `china.py`: map, head cross-section and device icons for the China post). In a post, `<img class="svg" src="/fig/x.svg">` is inlined at build, so the figure follows the theme; add `wide` to break out of the text column.
- `static/` — copied as-is: `style.css`, `cv.pdf`, images.

Build and preview:

```bash
uv run build.py && python3 -m http.server -d _site 8000
```

Push to `main` → GitHub Action builds and deploys to the `gh-pages` branch.
