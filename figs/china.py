"""Figures for the China post: device icons for the company cards, the head cross-section and the map.
Colors come from the page's CSS variables (build.py inlines the SVG), so they follow the theme toggle.
Run: python3 figs/china.py  → static/fig/china/*.svg
The map needs world-atlas 2.0.2 (countries-50m.json); it is downloaded into figs/.cache on the first run."""
import json
import math
import urllib.request
from pathlib import Path

HERE = Path(__file__).parent
OUT = HERE.parent / "static/fig/china"
CACHE = HERE / ".cache"

STYLE = """<style>
  .cn .ink { stroke: var(--text, #1c1b19); fill: none; } .cn .inkf { fill: var(--text, #1c1b19); }
  .cn .acc { stroke: var(--accent, #0e7470); fill: none; } .cn .accf { fill: var(--accent, #0e7470); }
  .cn .mid { stroke: var(--fig-mid, #9a968e); fill: none; } .cn .midf { fill: var(--fig-mid, #9a968e); }
  .cn .rulef { fill: var(--rule, #e4e1da); } .cn .rule { stroke: var(--rule, #e4e1da); fill: none; }
  .cn .bgf { fill: var(--bg, #fbfaf7); } .cn .softf { fill: var(--code-bg, #f1efe9); }
  .cn .bubble { fill: var(--accent, #0e7470); fill-opacity: .16; stroke: var(--accent, #0e7470); }
  .cn text { font-family: "Inter Tight", -apple-system, "Helvetica Neue", Arial, sans-serif; fill: var(--muted, #6b6862); }
  .cn .serif { font-family: "Source Serif 4", Georgia, serif; font-style: italic; fill: var(--text, #1c1b19); }
  .cn .strong { fill: var(--text, #1c1b19); }
</style>"""


def svg(w, h, body, label=""):
    aria = f' role="img" aria-label="{label}"' if label else ' aria-hidden="true"'
    return f'<svg class="cn" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}"{aria}>{STYLE}{body}</svg>\n'


def f(v):
    return f"{v:.1f}".rstrip("0").rstrip(".")


def path(pts, cls, w=1.2, close=False, extra=""):
    d = "M" + " L".join(f"{f(x)},{f(y)}" for x, y in pts) + (" Z" if close else "")
    return f'<path class="{cls}" d="{d}" stroke-width="{w}"{extra}/>'


def circle(x, y, r, cls, w=1.2, extra=""):
    return f'<circle class="{cls}" cx="{f(x)}" cy="{f(y)}" r="{f(r)}" stroke-width="{w}"{extra}/>'


def text(x, y, s, size=12, cls="", anchor="start"):
    c = f' class="{cls}"' if cls else ""
    return f'<text{c} x="{f(x)}" y="{f(y)}" font-size="{size}" text-anchor="{anchor}">{s}</text>'


# ---------- device icons (120 x 100) ----------
def disk(n_rows, n_cols):
    b = circle(60, 50, 36, "ink", 0.9, ' stroke-dasharray="3 4"') + circle(60, 50, 25, "ink", 1.3)
    dx, dy = 36 / max(n_cols, 1), 24 / max(n_rows, 1)
    for i in range(n_cols):
        for j in range(n_rows):
            b += circle(60 - 18 + dx / 2 + i * dx, 50 - 12 + dy / 2 + j * dy, 2.6 if n_cols <= 4 else 1.7, "accf", 0)
    return b


def threads(n=4):
    b = '<rect class="ink" x="44" y="10" width="32" height="12" rx="2" stroke-width="1.3"/>'
    for k in range(n):
        x = 49 + k * 22 / (n - 1)
        pts = [(x + 5 * math.sin(t / 7 + k) * (t / 70), 22 + t) for t in range(0, 70, 3)]
        b += path(pts, "ink", 1.1)
        for t in (56, 63):
            b += circle(x + 5 * math.sin(t / 7 + k) * (t / 70), 22 + t, 1.6, "accf", 0)
    return b


def grid():
    b = '<path class="ink" d="M24 26 Q60 18 96 26 L96 78 Q60 70 24 78 Z" stroke-width="1.3"/>'
    b += '<path class="ink" d="M60 22 L60 12 Q62 6 84 5" stroke-width="1"/>'
    for i in range(10):
        for j in range(7):
            b += circle(30 + i * 6.6, 31 + j * 6.4 - 3 * math.sin(math.pi * i / 9) + 1.5, 1.2, "accf", 0)
    return b


def tiles():
    b = ""
    for x0, y0 in ((32, 22), (62, 22), (32, 52), (62, 52)):
        b += f'<rect class="ink" x="{x0}" y="{y0}" width="26" height="26" stroke-width="1.1"/>'
        for i in range(5):
            for j in range(5):
                b += circle(x0 + 4 + i * 4.5, y0 + 4 + j * 4.5, 0.9, "accf", 0)
    return b


def eye():
    return (circle(60, 50, 32, "ink", 1.3) + '<ellipse class="ink" cx="32" cy="50" rx="5" ry="14" stroke-width="1"/>'
            + '<path class="ink" d="M29 40 Q22 50 29 60" stroke-width="0.8"/>'
            + '<rect class="accf" x="83" y="43" width="7" height="14"/>')


def band():
    b = '<path class="ink" d="M24 70 Q60 4 96 70" stroke-width="2.4"/>'
    for t in (0.12, 0.31, 0.5, 0.69, 0.88):
        x = (1 - t) ** 2 * 24 + 2 * (1 - t) * t * 60 + t * t * 96
        y = (1 - t) ** 2 * 70 + 2 * (1 - t) * t * 4 + t * t * 70
        b += circle(x, y + 2, 3.6, "inkf", 0)
    return b


def waves():
    b = '<rect class="ink" x="14" y="34" width="12" height="32" rx="2" stroke-width="1.3"/>'
    for k in range(4):
        x = 34 + k * 12
        b += f'<path class="acc" d="M{x} {28 + k * 4} Q{x + 10} 50 {x} {72 - k * 4}" stroke-width="1.1" opacity="{1 - k * 0.18:.2f}"/>'
    return b + circle(98, 50, 4.5, "accf", 0) + path([(26, 34), (98, 50), (26, 66)], "mid", 0.7, extra=' stroke-dasharray="2 3"')


def unknown():
    return ('<rect class="ink" x="34" y="24" width="52" height="52" stroke-width="1" stroke-dasharray="3 3"/>'
            + text(60, 61, "?", 30, "serif", "middle"))


ICONS = {"neo": disk(2, 4), "pad": disk(4, 8), "threads": threads(), "grid": grid(), "tiles": tiles(),
         "eye": eye(), "band": band(), "waves": waves(), "unknown": unknown()}


# ---------- head cross-section (1000 x 520) ----------
def section():
    W, H = 1000, 520
    X0, X1 = 0, W
    curve = lambda x, base: base + 0.00013 * (x - 500) ** 2
    scalp = lambda x: curve(x, 250)
    skull_t = lambda x: curve(x, 274)
    skull_b = lambda x: curve(x, 318)
    dura = lambda x: curve(x, 326)
    cortex = lambda x: curve(x, 336) + 3 * math.sin(x / 23) + 2 * math.sin(x / 9)
    cortex_b = lambda x: curve(x, 440) + 4 * math.sin(x / 31)
    xs = list(range(X0, X1 + 1, 5))

    def band(top, bot, cls):
        return path([(x, top(x)) for x in xs] + [(x, bot(x)) for x in reversed(xs)], cls, 0, True)

    b = band(scalp, skull_t, "softf") + band(skull_t, skull_b, "bgf") + band(skull_b, dura, "softf")
    b += band(cortex, cortex_b, "rulef")
    for x in range(X0, X1, 9):
        b += path([(x, skull_t(x) + 5), (x + 7, skull_b(x) - 5)], "rule", 0.8)
    for fn, w in ((scalp, 1.2), (skull_t, 1), (skull_b, 1), (dura, 1.4), (cortex, 1.1)):
        b += path([(x, fn(x)) for x in xs], "ink", w)
    b += path([(x, cortex_b(x)) for x in xs], "mid", 0.8, extra=' stroke-dasharray="3 4"')
    for name, fn, dy in (("scalp", scalp, 15), ("skull", skull_t, 27), ("dura", dura, -3), ("cortex", cortex, 40)):
        b += text(12, fn(12) + dy, name, 13, "serif")

    def label(x, y, ty, name, fact):
        return (path([(x, y), (x, ty + 12)], "acc", 0.8) + text(x, ty - 6, name, 18, "serif", "middle")
                + text(x, ty + 10, fact, 12.5, "", "middle"))

    # Gestala: ultrasound from outside, focus in the brain
    x = 120; y = scalp(x)
    b += f'<rect class="ink" x="{x - 24}" y="{f(y - 30)}" width="48" height="14" rx="3" stroke-width="1.2"/>'
    for k in range(4):
        b += f'<path class="acc" d="M{x - 20 + k * 2} {f(y - 12 + k * 13)} Q{x} {f(y - 2 + k * 15)} {x + 20 - k * 2} {f(y - 12 + k * 13)}" stroke-width="1" opacity="{0.9 - k * 0.15:.2f}"/>'
    b += circle(x, cortex(x) + 40, 5, "accf", 0) + label(x, y - 32, 95, "Gestala", "ultrasound, no implant")
    # BrainCo: EEG on the scalp
    x = 270
    for xx in (246, 270, 294):
        b += f'<path class="inkf" d="M{xx - 8} {f(scalp(xx))} A8 8 0 0 1 {xx + 8} {f(scalp(xx))} Z"/>'
    b += f'<path class="ink" d="M228 {f(scalp(228) - 12)} Q270 {f(scalp(270) - 24)} 312 {f(scalp(312) - 12)}" stroke-width="2"/>'
    b += label(x, scalp(x) - 22, 165, "BrainCo", "EEG on the scalp")
    # Neuracle NEO: implant in the skull, contacts on the dura, coil on the scalp
    x = 420
    b += f'<rect class="bgf" x="{x - 32}" y="{f(skull_t(x) + 3)}" width="64" height="{f(dura(x) - skull_t(x) - 4)}"/>'
    b += f'<rect class="ink" x="{x - 32}" y="{f(skull_t(x) + 3)}" width="64" height="{f(dura(x) - skull_t(x) - 4)}" stroke-width="1.2"/>'
    for i in range(8):
        b += circle(x - 26 + i * 7.5, dura(x) - 3, 2.5, "accf", 0)
    b += f'<ellipse class="ink" cx="{x}" cy="{f(scalp(x) - 8)}" rx="38" ry="6" stroke-width="1" stroke-dasharray="3 3"/>'
    b += label(x, scalp(x) - 15, 95, "Neuracle NEO", "8 contacts above the dura · approved")
    # NeuroXess: thin grid on the cortex
    x0, x1 = 545, 655
    b += path([(x, cortex(x) - 2) for x in range(x0, x1 + 1, 3)], "ink", 2.6)
    for x in range(x0 + 4, x1, 8):
        b += circle(x, cortex(x) - 2, 1.7, "accf", 0)
    b += label(600, dura(600) - 4, 165, "NeuroXess", "256 ch grid on the cortex")
    # StairMed, AIT, BCIFlex: flexible threads into the cortex
    x = 760
    b += f'<rect class="bgf" x="{x - 20}" y="{f(skull_t(x) + 6)}" width="40" height="22" rx="3"/>'
    b += f'<rect class="ink" x="{x - 20}" y="{f(skull_t(x) + 6)}" width="40" height="22" rx="3" stroke-width="1.2"/>'
    for i, o in enumerate((-14, -6, 2, 10, 18)):
        sx = x + o - 2
        top, bot = skull_t(x) + 28, cortex(x) + 66 + i * 4
        b += f'<path class="ink" d="M{f(sx)} {f(top)} C{f(sx - 6)} {f(dura(x) + 18)},{f(sx + 8)} {f(cortex(x) + 38)},{f(sx + o * 0.6)} {f(bot)}" stroke-width="0.9"/>'
        for k in (0, 7, 14):
            b += circle(sx + o * 0.6, bot - 14 + k * 0.7, 1.5, "accf", 0)
    b += label(x, skull_t(x) + 4, 95, "StairMed · AIT · BCIFlex", "flexible threads into the cortex")
    # Zhonghua: a claim, nothing published
    x = 915
    b += f'<rect class="ink" x="{x - 22}" y="{f(skull_t(x) + 6)}" width="44" height="22" rx="3" stroke-width="1" stroke-dasharray="3 3"/>'
    b += text(x, cortex(x) + 60, "?", 30, "serif", "middle")
    b += label(x, skull_t(x) + 4, 165, "Zhonghua", "claims 65,536 ch, no paper")
    return svg(W, H, b, "Cross-section of the head: where each company's device sits, from the scalp to inside the cortex")


# ---------- map (1000 x 640) ----------
COMPANIES = [  # name, city, lon, lat, total raised $M (None = not public)
    ("StairMed", "Shanghai", 121.47, 31.23, 387), ("NeuroXess", "Shanghai", 121.47, 31.23, 168),
    ("AIT", "Shanghai", 121.47, 31.23, 118), ("Neuracle", "Shanghai", 121.47, 31.23, None),
    ("BrainCo", "Hangzhou", 120.15, 30.27, 370), ("NanoChap", "Hangzhou", 120.15, 30.27, 149),
    ("Mindtrix", "Suzhou", 120.58, 31.30, 74),
    ("BCIFlex", "Beijing", 116.40, 39.90, 93), ("Beinao", "Beijing", 116.40, 39.90, 30),
    ("Xinsheng Shijie", "Beijing", 116.40, 39.90, 15),
    ("Gestala", "Chengdu", 104.07, 30.67, 85), ("Zhonghua", "Wuhan", 114.30, 30.59, None)]


def world():
    CACHE.mkdir(exist_ok=True)
    p = CACHE / "countries-50m.json"
    if not p.exists():
        urllib.request.urlretrieve("https://cdn.jsdelivr.net/npm/world-atlas@2.0.2/countries-50m.json", p)
    return json.loads(p.read_text())


def decode(topo):
    """TopoJSON → {id: [rings in lon/lat]}."""
    (sx, sy), (tx, ty) = topo["transform"]["scale"], topo["transform"]["translate"]
    arcs = []
    for arc in topo["arcs"]:
        x = y = 0
        pts = []
        for dx, dy in arc:
            x += dx; y += dy
            pts.append((x * sx + tx, y * sy + ty))
        arcs.append(pts)

    def ring(idx):
        out = []
        for i in idx:
            a = arcs[i] if i >= 0 else arcs[~i][::-1]
            out.extend(a if not out else a[1:])
        return out

    shapes, used = {}, {}
    for g in topo["objects"]["countries"]["geometries"]:
        polys = [g["arcs"]] if g["type"] == "Polygon" else g.get("arcs", []) if g["type"] == "MultiPolygon" else []
        shapes[g.get("id")] = [ring(r) for poly in polys for r in poly]
        for poly in polys:
            for r in poly:
                for i in r:
                    used.setdefault(i if i >= 0 else ~i, set()).add(g.get("id"))
    return shapes, arcs, used


def china_map():
    W, H = 1000, 640
    lon0, lat0, k = 104.5, 35.5, 15.2  # center and px per degree of longitude
    my = lambda lat: math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))
    proj = lambda lon, lat: (W * 0.47 + (lon - lon0) * k, H * 0.52 - (my(lat) - my(lat0)) * k * 180 / math.pi)
    b = f'<defs><clipPath id="cn-clip"><rect width="{W}" height="{H}"/></clipPath></defs><g clip-path="url(#cn-clip)">'
    shapes, arcs, used = decode(world())

    def screen(lonlat_pts):
        pts, last = [], None
        for lon, lat in lonlat_pts:
            px, py = proj(lon, lat)
            q = (round(min(max(px, -10), W + 10)), round(min(max(py, -10), H + 10)))  # clamp: off-canvas coast collapses onto the frame
            if last is None or abs(q[0] - last[0]) + abs(q[1] - last[1]) >= 3:
                pts.append(q); last = q
        return pts

    in_view = lambda r: any(55 < lon < 155 and 0 < lat < 62 for lon, lat in r)
    for cid, rings in shapes.items():
        for r in rings:
            if not in_view(r):
                continue
            pts = screen(r)
            xs_, ys_ = [q[0] for q in pts], [q[1] for q in pts]
            if len(pts) > 3 and max(xs_) - min(xs_) + max(ys_) - min(ys_) > 8 and any(0 <= q[0] <= W and 0 <= q[1] <= H for q in pts):
                b += path(pts, "rulef" if cid == "156" else "softf", 0, True)
    # borders, as on the international Google Maps: de facto lines, disputed China-India border dashed
    CN, IN = "156", "356"
    for i, users in used.items():
        if not in_view(arcs[i]):
            continue
        pts = screen(arcs[i])
        on_canvas = [q for q in pts if 0 <= q[0] <= W and 0 <= q[1] <= H]
        if len(pts) < 2 or not on_canvas:
            continue
        if CN in users and IN in users:
            b += path(pts, "mid", 0.9, extra=' stroke-dasharray="4 3"')
        elif CN in users:
            b += path(pts, "mid", 0.7)
        else:
            b += path(pts, "rule", 0.6)
    b += "</g>"

    # one bubble per city: area = total raised by the companies there; every company listed in the labels
    cities = {}
    for name, city, lon, lat, m in COMPANIES:
        c = cities.setdefault(city, {"lonlat": (lon, lat), "rows": [], "sum": 0})
        c["rows"].append((name, m)); c["sum"] += m or 0
    rad = lambda m: math.sqrt(m) * 2.1 if m else 8
    for city, c in sorted(cities.items(), key=lambda kv: -kv[1]["sum"]):
        x, y = proj(*c["lonlat"])
        known = all(m for _, m in c["rows"])
        b += circle(x, y, rad(c["sum"]), "bubble", 1, "" if c["sum"] else ' stroke-dasharray="3 3" fill-opacity="0"')
    for city, c in cities.items():
        b += circle(*proj(*c["lonlat"]), 2.4, "inkf", 0)

    money = lambda name, m: {"Mindtrix": "$74M+", "Beinao": "~$30M, state"}.get(name, f"${m}M" if m else "not public")

    def block(city, lx, ly, anchor="start"):
        c = cities[city]; x, y = proj(*c["lonlat"])
        total = ""
        if len(c["rows"]) > 1:
            total = f'  <tspan class="strong" font-style="normal" font-size="14" font-family="Inter Tight, -apple-system, Arial, sans-serif">${c["sum"]}M{"+" if not all(m for _, m in c["rows"]) else ""}</tspan>'
        out = text(lx, ly, city + total, 17, "serif", anchor)
        tx = lx - 6 if anchor == "start" else lx + 6
        out += path([(x, y), (tx, ly - 5)], "mid", 0.7)
        for i, (name, m) in enumerate(sorted(c["rows"], key=lambda r: -(r[1] or 0))):
            out += text(lx, ly + 20 + i * 18, f'<tspan class="strong">{name}</tspan>  {money(name, m)}', 13.5, "", anchor)
        return out

    b += block("Beijing", 830, 130)
    b += block("Shanghai", 830, 270)
    b += block("Suzhou", 830, 383)
    b += block("Hangzhou", 830, 440)
    b += block("Chengdu", 515, 350, "end")
    b += block("Wuhan", 610, 560, "end")
    b += text(40, 78, "$1.5B", 54, "serif")
    b += text(42, 104, "raised in total by the companies in this post", 15)
    b += text(40, 612, "Circle area = total money raised by the companies in each city. Neuracle and Zhonghua: not public. Mindtrix: Suzhou, from one source.", 12.5)
    return svg(W, H, b, "Map of China: where the twelve companies are and how much each has raised in total, about $1.5 billion together")


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, body in ICONS.items():
        (OUT / f"dev-{name}.svg").write_text(svg(120, 100, body))
    (OUT / "section.svg").write_text(section())
    (OUT / "map.svg").write_text(china_map())
    print("wrote", sorted(p.name for p in OUT.glob("*.svg")))
