# kovalalvi.github.io

Personal site and blog. Plain HTML/CSS, one Python build script, no framework.

- `templates/home.html` — the home page. `{{posts}}` becomes the 5 latest posts.
- `templates/base.html` — the frame around every page.
- `posts/YYYY-MM-DD-slug.md` — a post, served at `/blog/slug/`. The date is when the post was written (the vault draft's date or first commit), not the day it went on the site. Front matter: `title`, `description`, `tag` (my work / review / digest / tutorial), optional `telegram` (link to the RU post), `image` (preview card) and `affiliation` (default UMH, Spain).
- `static/` — copied as-is: `style.css`, `cv.pdf`, images.

Build and preview:

```bash
uv run build.py && python3 -m http.server -d _site 8000
```

Push to `main` → GitHub Action builds and deploys to the `gh-pages` branch.
