# kovalalvi.github.io

Personal site and blog. Plain HTML/CSS, one Python build script, no framework.

- `templates/home.html` — the home page. `{{posts}}` becomes the 5 latest posts.
- `templates/base.html` — the frame around every page.
- `posts/YYYY-MM-DD-slug.md` — a post, served at `/blog/slug/`. Front matter: `title`, `description`, `tag` (review / essay / digest), optional `telegram` (link to the RU post).
- `static/` — copied as-is: `style.css`, `cv.pdf`, images.

Build and preview:

```bash
uv run build.py && python3 -m http.server -d _site 8000
```

Push to `main` → GitHub Action builds and deploys to the `gh-pages` branch.
