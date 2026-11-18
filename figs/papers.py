"""Paper glyphs in the "signals" style: each shows the paper's mechanism on (synthetic) data, no results.
Same canvas, line weight, palette; dark mode is inside the SVG, so it works in <img>.
Run: python3 figs/papers.py  → static/fig/paper-*.svg"""
import math
import random
from pathlib import Path

OUT = Path(__file__).parent.parent / "static/fig"
W, H = 240, 160  # 3:2
X0, X1 = 14, 226  # time axis

STYLE = """<style>
  svg { --ink: #1c1b19; --mid: #9a968e; --faint: #e4e1da; --acc: #b4441f; }
  @media (prefers-color-scheme: dark) {
    svg { --ink: #e8e5df; --mid: #6f6b64; --faint: #2e2c29; --acc: #e8825c; }
  }
  .faint { fill: var(--faint); }
  .l-ink { stroke: var(--ink); } .l-mid { stroke: var(--mid); } .l-acc { stroke: var(--acc); }
  line, polyline { fill: none; stroke-width: 1.6; stroke-linecap: round; stroke-linejoin: round; }
  text { font-family: "Inter Tight", -apple-system, "Helvetica Neue", Arial, sans-serif; font-size: 9px; fill: var(--mid); letter-spacing: .02em; }
</style>"""


def svg(body):
    return f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}">{STYLE}{body}</svg>\n'


def poly(pts, cls, width):
    return f'<polyline class="{cls}" style="stroke-width:{width}" points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in pts)}"/>'


def label(x, y, s):
    return f'<text x="{x}" y="{y}">{s}</text>'


def bumps(t, centers, width=0.006):
    return sum(a * math.exp(-((t - c) ** 2) / width) for c, a in centers)


def noisy_traces(rng, n_ch, top, gap, events, n=140, quiet=1.0, loud=4.5, width=0.003, spiky=False):
    """Channels whose noise grows around the events (high-gamma bursts, EMG activity)."""
    out = []
    for ch in range(n_ch):
        pts = []
        for i in range(n):
            t = i / (n - 1)
            amp = quiet + loud * bumps(t, [(e, 1) for e in events], width)
            v = rng.gauss(0, amp) * (1.6 if spiky and rng.random() < 0.15 else 1)
            pts.append((X0 + t * (X1 - X0), top + ch * gap + v))
        out.append(poly(pts, "l-mid", 1.0))
    return out


def mae():
    """V1 spike raster; masked patches (grey) are filled in by the model (accent spikes)."""
    rng = random.Random(11)
    rows, y0, dy = 12, 18, 10.5
    patches = [(40, 0, 3), (96, 4, 4), (150, 1, 3), (176, 7, 4), (60, 8, 3), (120, 9, 3)]  # (x, first row, rows)
    out = [f'<rect class="faint" x="{px}" y="{y0 + pr * dy - 5}" width="30" height="{n * dy}" rx="2"/>' for px, pr, n in patches]
    for r in range(rows):
        y, t = y0 + r * dy, X0
        while (t := t + rng.expovariate(1 / 9)) < X1:
            inside = any(px <= t < px + 30 and pr <= r < pr + n for px, pr, n in patches)
            out.append(f'<line class="{"l-acc" if inside else "l-ink"}" style="stroke-width:1.3" x1="{t:.1f}" y1="{y - 3.5}" x2="{t:.1f}" y2="{y + 3.5}"/>')
    out.append(label(X0, 152, "V1 spikes · masked patches reconstructed"))
    return svg("".join(out))


def fingerflex():
    """ECoG bursts on top, the decoded finger flexion below follows them."""
    rng = random.Random(5)
    events = [0.2, 0.52, 0.8]
    out = noisy_traces(rng, 4, 22, 15, events)
    flex = [(X0 + t * (X1 - X0), 132 - 36 * bumps(t, [(e + 0.03, a) for e, a in zip(events, (0.7, 1.0, 0.55))]))
            for t in (i / 99 for i in range(100))]
    out.append(poly(flex, "l-acc", 2.4))
    out += [label(X0, 12, "ECoG"), label(X0, 152, "finger flexion")]
    return svg("".join(out))


def alvi():
    """8-channel sEMG on top, many joint angles of the hand decoded below."""
    rng = random.Random(8)
    events = [0.15, 0.42, 0.7, 0.88]
    out = noisy_traces(rng, 8, 17, 7, events, n=180, quiet=0.35, loud=2.6, width=0.002, spiky=True)
    for k in range(4):
        centers = [(e + 0.02 + 0.01 * k, rng.uniform(0.4, 1.0)) for e in events]
        pts = [(X0 + t * (X1 - X0), 92 + 14 * k - 12 * bumps(t, centers, 0.004)) for t in (i / 119 for i in range(120))]
        out.append(poly(pts, "l-acc" if k == 1 else "l-ink", 2.2 if k == 1 else 1.2))
    out += [label(X0, 10, "sEMG, 8 channels"), label(X0, 152, "joint angles of the hand")]
    return svg("".join(out))


def miranda():
    """Mirror training: the intact hand's movement (left) drives a mirrored virtual hand (right)."""
    mid = W / 2
    out = [f'<line class="l-mid" style="stroke-dasharray:3 4;stroke-width:1.2" x1="{mid}" y1="14" x2="{mid}" y2="134"/>']
    for k, a in enumerate((1.0, 0.75, 0.55)):
        y0 = 48 + k * 34
        left = [(X0 + 8 + t * (mid - X0 - 16), y0 - 26 * a * bumps(t, [(0.3, 1), (0.75, 0.7)], 0.01)) for t in (i / 59 for i in range(60))]
        right = [(2 * mid - x, y) for x, y in left]
        out.append(poly(left, "l-ink", 1.6 if k == 0 else 1.1))
        out.append(poly(right, "l-acc", 2.2 if k == 0 else 1.1))
    out += [label(X0, 152, "intact hand"), f'<text x="{X1}" y="152" text-anchor="end">virtual mirrored hand</text>']
    return svg("".join(out))


def beira():
    """Fast EEG on top; slow subcortical BOLD below, delayed by the hemodynamic lag."""
    rng = random.Random(3)
    events = [0.12, 0.45, 0.62]
    out = noisy_traces(rng, 4, 20, 13, events, n=200, quiet=1.2, loud=3.0, width=0.002)
    lag = 0.14
    bold = [(X0 + t * (X1 - X0), 130 - 34 * bumps(t, [(e + lag, a) for e, a in zip(events, (0.8, 0.6, 0.9))], 0.012))
            for t in (i / 119 for i in range(120))]
    out.append(poly(bold, "l-acc", 2.4))
    e, x_e, x_b = events[0], X0 + events[0] * (X1 - X0), X0 + (events[0] + lag) * (X1 - X0)
    out.append(f'<line class="l-mid" style="stroke-dasharray:2 3;stroke-width:1" x1="{x_e:.1f}" y1="72" x2="{x_e:.1f}" y2="100"/>')
    out.append(f'<line class="l-mid" style="stroke-width:1" x1="{x_e:.1f}" y1="100" x2="{x_b:.1f}" y2="100"/>')
    out.append(f'<polyline class="l-mid" style="stroke-width:1" points="{x_b - 4:.1f},97 {x_b:.1f},100 {x_b - 4:.1f},103"/>')
    out += [label(X0, 10, "EEG"), label(X0, 152, "subcortical BOLD, hemodynamic lag")]
    return svg("".join(out))


if __name__ == "__main__":
    OUT.mkdir(parents=True, exist_ok=True)
    for name, make in {"mae": mae, "alvi": alvi, "miranda": miranda, "fingerflex": fingerflex, "beira": beira}.items():
        (OUT / f"paper-{name}.svg").write_text(make())
        print("wrote", OUT / f"paper-{name}.svg")
