"""SVG figures for the review pages and the README (standard library only).

Every figure is drawn twice, for GitHub's light and dark themes, and embedded with
<picture> so GitHub picks the one matching the reader's theme.

Per-paper figures are data, not code: data/figures/<slug>.json lists them, and the
same few chart kinds below draw every paper's figures.

    {"figures": [
      {"id": "lineage", "kind": "mermaid", "title": "...", "caption": "...", "mermaid": "flowchart LR ..."},
      {"id": "baseline", "kind": "dots", "title": "...", "caption": "...", "unit": "WER (%)",
       "min": 20, "max": 40, "band": {"from": 25, "to": 27, "label": "..."},
       "rows": [{"label": "...", "note": "...", "value": 25.1, "err": 1.0, "estimate": false,
                 "highlight": false, "source": "..."}]},
      {"id": "reduction", "kind": "slope", "unit": "WER (%)", "max": 80, "left": "8", "right": "4",
       "series": [{"label": "...", "note": "...", "a": 68.0, "b": 76.8, "highlight": false, "source": "..."}]},
      {"id": "finetune", "kind": "lines", "unit": "WER (%)", "min": 30, "max": 50, "x": ["7", "6"],
       "xlabel": "...", "series": [{"label": "...", "values": [36.5, 42.9]}], "source": "..."}
    ]}
"""
from html import escape

FONT = "-apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial, sans-serif"

# GitHub page surfaces; categorical slots validated against them (all-pairs for the first three).
THEMES = {
    "light": {
        "bg": "#ffffff", "text": "#1f2328", "muted": "#59636e", "grid": "#e6e8eb", "axis": "#b7bdc5",
        "band": "#eef1f4", "empty": "#f3f4f6", "neutral": "#8c8b86",
        "series": ["#2a78d6", "#eb6834", "#1baf7a", "#6250d6"],
        "seq": ["#cde2fb", "#9ec5f4", "#6da7ec", "#3987e5", "#256abf", "#184f95", "#0d366b"],
    },
    "dark": {
        "bg": "#0d1117", "text": "#e6edf3", "muted": "#9198a1", "grid": "#21262d", "axis": "#3d444d",
        "band": "#161b22", "empty": "#151a21", "neutral": "#7d8590",
        "series": ["#3987e5", "#d95926", "#199e70", "#9085e9"],
        "seq": ["#0d2a52", "#104281", "#184f95", "#256abf", "#3987e5", "#6da7ec", "#b7d3f6"],
    },
}
HIGHLIGHT = 1  # "this paper" is always the second slot (orange), other papers the first (blue).


def fmt(v):
    return f"{v:.2f}".rstrip("0").rstrip(".") if isinstance(v, float) else str(v)


class Svg:
    def __init__(self, w, h, t, title):
        self.w, self.h, self.t = w, h, t
        self.parts = [
            f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'font-family="{FONT}" role="img" aria-label="{escape(title)}">',
            f"<title>{escape(title)}</title>",
            f'<rect width="{w}" height="{h}" fill="{t["bg"]}"/>',
        ]

    def add(self, s):
        self.parts.append(s)

    def text(self, x, y, s, size=12, fill=None, anchor="start", weight=None, italic=False):
        attrs = f' font-weight="{weight}"' if weight else ""
        attrs += ' font-style="italic"' if italic else ""
        self.add(f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" fill="{fill or self.t["text"]}" '
                 f'text-anchor="{anchor}"{attrs}>{escape(str(s))}</text>')

    def line(self, x1, y1, x2, y2, stroke, width=1, dash=None):
        d = f' stroke-dasharray="{dash}"' if dash else ""
        self.add(f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" stroke="{stroke}" '
                 f'stroke-width="{width}"{d}/>')

    def marker(self, x, y, color, shape="circle", hollow=False, r=5.5):
        fill, ring = (self.t["bg"], color) if hollow else (color, self.t["bg"])
        sw = 2 if hollow else 2
        if shape == "circle":
            self.add(f'<circle cx="{x:.1f}" cy="{y:.1f}" r="{r}" fill="{fill}" stroke="{ring}" stroke-width="{sw}"/>')
        elif shape == "square":
            s = r * 0.9
            self.add(f'<rect x="{x - s:.1f}" y="{y - s:.1f}" width="{2 * s:.1f}" height="{2 * s:.1f}" rx="1.5" '
                     f'fill="{fill}" stroke="{ring}" stroke-width="{sw}"/>')
        elif shape == "diamond":
            s = r * 1.2
            self.add(f'<path d="M{x:.1f},{y - s:.1f} L{x + s:.1f},{y:.1f} L{x:.1f},{y + s:.1f} L{x - s:.1f},{y:.1f} Z" '
                     f'fill="{fill}" stroke="{ring}" stroke-width="{sw}"/>')
        elif shape == "triangle":
            s = r * 1.2
            self.add(f'<path d="M{x:.1f},{y - s:.1f} L{x + s:.1f},{y + s * 0.8:.1f} L{x - s:.1f},{y + s * 0.8:.1f} Z" '
                     f'fill="{fill}" stroke="{ring}" stroke-width="{sw}"/>')

    def done(self):
        return "\n".join(self.parts + ["</svg>"]) + "\n"


def ticks(lo, hi, n=5):
    span = hi - lo
    step = next(s for s in (1, 2, 5, 10, 20, 25, 50, 100) if span / s <= n)
    v = lo - lo % step if lo % step else lo
    out = []
    while v <= hi + 1e-9:
        if v >= lo:
            out.append(v)
        v += step
    return out


def header(svg, fig, x):
    svg.text(x, 24, fig["title"], 15, weight="600")
    if fig.get("subtitle"):
        svg.text(x, 43, fig["subtitle"], 12, svg.t["muted"])


# ---------- dots: one row per result, optional error bar and reference band ----------

def dots(fig, t):
    rows = fig["rows"]
    lo, hi = fig["min"], fig["max"]
    W, left, right, top, rh = 760, 250, 70, 70, 34
    H = top + rh * len(rows) + 52
    svg = Svg(W, H, t, fig["title"])
    header(svg, fig, 16)
    x = lambda v: left + (v - lo) / (hi - lo) * (W - left - right)
    y0, y1 = top - 8, top + rh * len(rows) - 6
    band = fig.get("band")
    if band:
        svg.add(f'<rect x="{x(band["from"]):.1f}" y="{y0}" width="{x(band["to"]) - x(band["from"]):.1f}" '
                f'height="{y1 - y0}" fill="{t["band"]}"/>')
    for v in ticks(lo, hi):
        svg.line(x(v), y0, x(v), y1, t["grid"])
        svg.text(x(v), y1 + 18, fmt(v), 11, t["muted"], "middle")
    svg.text(x((lo + hi) / 2), y1 + 38, fig["unit"], 12, t["muted"], "middle")
    if band:
        svg.text(x(band["from"]) + 4, y0 + 12, band["label"], 11, t["muted"])
    for i, r in enumerate(rows):
        cy = top + 10 + rh * i + rh / 2
        color = t["series"][HIGHLIGHT if r.get("highlight") else 0]
        svg.text(16, cy - 2, r["label"], 13, weight="600" if r.get("highlight") else None)
        if r.get("note"):
            svg.text(16, cy + 13, r["note"], 11, t["muted"])
        svg.line(left, cy, x(r["value"]), cy, t["grid"], 1, "2 3")
        if r.get("err"):
            a, b = x(r["value"] - r["err"]), x(r["value"] + r["err"])
            svg.line(a, cy, b, cy, color, 2)
            svg.line(a, cy - 5, a, cy + 5, color, 2)
            svg.line(b, cy - 5, b, cy + 5, color, 2)
        svg.marker(x(r["value"]), cy, color, hollow=r.get("estimate", False))
        label = ("≈" if r.get("estimate") else "") + fmt(r["value"]) + (f" ± {fmt(r['err'])}" if r.get("err") else "")
        svg.text(x(r["value"] + (r.get("err") or 0)) + 10, cy + 4, label, 12, weight="600")
    if any(r.get("estimate") for r in rows):
        svg.marker(W - 186, 30, t["muted"], hollow=True, r=4.5)
        svg.text(W - 176, 34, "hollow = read from a plot", 11, t["muted"])
    return svg.done()


# ---------- slope: two conditions per series, e.g. 8 vs 4 electrodes ----------

def slope(fig, t):
    series = fig["series"]
    W, H, top, bottom = 760, 380, 76, 56
    xa, xb = 300, 470
    lo, hi = fig.get("min", 0), fig["max"]
    svg = Svg(W, H, t, fig["title"])
    header(svg, fig, 16)
    y = lambda v: top + (hi - v) / (hi - lo) * (H - top - bottom)
    for v in ticks(lo, hi):
        svg.line(xa - 30, y(v), xb + 30, y(v), t["grid"])
        svg.text(xa - 38, y(v) + 4, fmt(v), 11, t["muted"], "end")
    svg.text(xa - 38, top - 16, fig["unit"], 11, t["muted"], "end")
    svg.text(xa, H - 22, fig["left"], 12, t["muted"], "middle")
    svg.text(xb, H - 22, fig["right"], 12, t["muted"], "middle")
    for i, s in enumerate(series):
        color = t["series"][HIGHLIGHT if s.get("highlight") else (0 if i == 0 else 2)]
        svg.line(xa, y(s["a"]), xb, y(s["b"]), color, 2.5)
        svg.marker(xa, y(s["a"]), color, hollow=s.get("estimate_a", False))
        svg.marker(xb, y(s["b"]), color)
        svg.text(xa - 12, y(s["a"]) + 4, ("≈" if s.get("estimate_a") else "") + fmt(s["a"]), 12, anchor="end", weight="600")
        rel = (s["b"] - s["a"]) / s["a"] * 100
        svg.text(xb + 12, y(s["b"]) - 2, f"{fmt(s['b'])}  ({rel:+.0f}% relative)", 12, weight="600")
        svg.text(xb + 12, y(s["b"]) + 13, s["label"] + (f" · {s['note']}" if s.get("note") else ""), 11, t["muted"])
    return svg.done()


# ---------- lines: a few conditions across an ordinal x (shape + color per series) ----------

SHAPES = ["circle", "square", "diamond", "triangle"]


def lines(fig, t):
    xs, series = fig["x"], fig["series"]
    lo, hi = fig["min"], fig["max"]
    W, H, left, right, top, bottom = 760, 400, 70, 40, 96, 60
    svg = Svg(W, H, t, fig["title"])
    header(svg, fig, 16)
    colors = [t["neutral"]] + t["series"][:1] + t["series"][2:4]
    # legend in one row above the plot
    lx = left
    for i, s in enumerate(series):
        svg.marker(lx + 6, 64, colors[i], SHAPES[i], r=4.5)
        svg.text(lx + 16, 68, s["label"], 12)
        lx += 28 + 7 * len(s["label"])
    x = lambda j: left + 40 + j * (W - left - right - 80) / (len(xs) - 1)
    y = lambda v: top + (hi - v) / (hi - lo) * (H - top - bottom)
    for v in ticks(lo, hi):
        svg.line(left, y(v), W - right, y(v), t["grid"])
        svg.text(left - 8, y(v) + 4, fmt(v), 11, t["muted"], "end")
    svg.text(left - 8, top - 12, fig["unit"], 11, t["muted"], "end")
    for j, lab in enumerate(xs):
        svg.text(x(j), H - bottom + 20, lab, 12, t["muted"], "middle")
    svg.text((left + W - right) / 2, H - 16, fig["xlabel"], 12, t["muted"], "middle")
    off = lambda i: (i - (len(series) - 1) / 2) * 7  # small dodge so equal values stay visible
    for i, s in enumerate(series):
        pts = [(x(j) + off(i), y(v)) for j, v in enumerate(s["values"])]
        svg.add(f'<polyline points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="none" '
                f'stroke="{colors[i]}" stroke-width="2" stroke-linejoin="round"/>')
    for i, s in enumerate(series):
        for (a, b) in [(x(j) + off(i), y(v)) for j, v in enumerate(s["values"])]:
            svg.marker(a, b, colors[i], SHAPES[i], r=4.5)
    return svg.done()


# ---------- heatmap: papers per section and year (README) ----------

def heatmap(title, subtitle, rows, cols, counts, t):
    W = 760
    left, top, cw, ch = 300, 64, (760 - 300 - 56) / len(cols), 30
    H = top + ch * len(rows) + 44
    svg = Svg(W, H, t, title)
    svg.text(16, 24, title, 15, weight="600")
    svg.text(16, 43, subtitle, 12, t["muted"])
    peak = max(max(r) for r in counts) or 1
    for j, c in enumerate(cols):
        svg.text(left + cw * j + cw / 2, top + ch * len(rows) + 18, c, 11, t["muted"], "middle")
    svg.text(W - 28, top - 8, "total", 11, t["muted"], "middle")
    for i, (label, row) in enumerate(zip(rows, counts)):
        cy = top + ch * i
        svg.text(left - 10, cy + ch / 2 + 4, label, 12, anchor="end")
        for j, n in enumerate(row):
            cx = left + cw * j
            if n:
                step = min(len(t["seq"]) - 1, 1 + int((n - 1) / peak * (len(t["seq"]) - 1)))
                fill = t["seq"][step]
            else:
                fill = t["empty"]
            svg.add(f'<rect x="{cx + 1:.1f}" y="{cy + 1:.1f}" width="{cw - 2:.1f}" height="{ch - 2:.1f}" rx="3" fill="{fill}"/>')
            if n:
                if t is THEMES["light"]:
                    ink = "#ffffff" if step >= 4 else t["text"]
                else:
                    ink = "#0d1117" if step >= 5 else t["text"]
                svg.text(cx + cw / 2, cy + ch / 2 + 4, n, 11, ink, "middle", "600")
        svg.text(W - 28, cy + ch / 2 + 4, sum(row), 12, t["muted"], "middle", "600")
    return svg.done()


KINDS = {"dots": dots, "slope": slope, "lines": lines}


def render(fig):
    """Return {"light": svg, "dark": svg} for a chart figure, or None for mermaid."""
    if fig["kind"] == "mermaid":
        return None
    return {mode: KINDS[fig["kind"]](fig, t) for mode, t in THEMES.items()}


def picture(base, alt):
    """Markdown/HTML that shows base-light.svg or base-dark.svg according to GitHub's theme."""
    return (f'<picture><source media="(prefers-color-scheme: dark)" srcset="{base}-dark.svg">'
            f'<img alt="{escape(alt)}" src="{base}-light.svg"></picture>')


def data_table(fig):
    k = fig["kind"]
    if k == "dots":
        out = ["| Result | Conditions | " + fig["unit"] + " | Source |", "| --- | --- | --- | --- |"]
        for r in fig["rows"]:
            v = ("≈" if r.get("estimate") else "") + fmt(r["value"]) + (f" ± {fmt(r['err'])}" if r.get("err") else "")
            out.append(f"| {r['label']} | {r.get('note', '')} | {v} | {r.get('source', '')} |")
    elif k == "slope":
        out = [f"| Paper | Conditions | {fig['left']} | {fig['right']} | Source |", "| --- | --- | --- | --- | --- |"]
        for s in fig["series"]:
            a = ("≈" if s.get("estimate_a") else "") + fmt(s["a"])
            out.append(f"| {s['label']} | {s.get('note', '')} | {a} | {fmt(s['b'])} | {s.get('source', '')} |")
    elif k == "lines":
        out = ["| " + fig["xlabel"] + " | " + " | ".join(s["label"] for s in fig["series"]) + " |",
               "| --- |" + " --- |" * len(fig["series"])]
        for j, xv in enumerate(fig["x"]):
            out.append(f"| {xv} | " + " | ".join(fmt(s["values"][j]) for s in fig["series"]) + " |")
    elif k == "mechanism":
        judged = any(v.get("verdict") for v in fig["slots"].values())
        out = ["| Component | This paper | Common practice | Papers with this practice | Verdict |", "| --- | --- | --- | --- | --- |"] \
            if judged else ["| Component | This paper |", "| --- | --- |"]
        for key, (label, _, _) in sorted(SLOTS.items()):
            v = fig["slots"].get(key, {})
            row = f"| {key} {label} | {' '.join(v.get('choice') or ['not reported'])} |"
            if judged:
                verdict = " ".join(VERDICTS[v["verdict"]][:2]) if v.get("verdict") else ""
                if v.get("note"):
                    verdict += f" ({v['note']})"
                cnt = f"{v['matched']:,} of {v['n']:,}" if v.get("matched") is not None else v.get("n", "")
                row += f" {v.get('field', '')} | {cnt} | {verdict} |"
            out.append(row)
    elif k == "coverage":
        out = ["| Component | Papers recording it | Share |", "| --- | --- | --- |"]
        for key, (label, _, _) in sorted(SLOTS.items()):
            n = fig["counts"].get(key, 0)
            flag = fig.get("flags", {}).get(key)
            out.append(f"| {key} {label} | {n:,} of {fig['total']:,}{' (' + flag + ')' if flag else ''} | {n / fig['total'] * 100:.1f}% |")
    else:
        return []
    return out


# ---------- mechanism: the fixed 13-component map (same layout for every figure) ----------
# Slots and routes follow the wiki ledger's mechanism template (spec v2.1, M01-M13).

SLOTS = {
    "M01": ("Training-time act", 1, 0), "M03": ("Train / calibrate", 2, 0), "M02": ("Teacher signal", 3, 0),
    "M04": ("Use-time act", 0, 1), "M05": ("Sensing", 1, 1), "M06": ("Decoding", 2, 1),
    "M08": ("Output", 3, 1), "M09": ("Confirmation", 4, 1), "M10": ("Correction", 5, 1),
    "M13": ("Hardware & limits", 1, 2), "M07": ("Runtime aids", 2, 2),
    "M11": ("Eval reference", 3, 2), "M12": ("Evaluation", 4, 2),
}
ROUTES = [("M01", "M03"), ("M02", "M03"), ("M03", "M06"), ("M04", "M05"), ("M05", "M06"), ("M07", "M06"),
          ("M06", "M08"), ("M08", "M09"), ("M09", "M10"), ("M10", "M04"), ("M08", "M12"), ("M11", "M12"),
          ("M11", "M06"), ("M13", "M05")]
LANES = ["Training", "Use", "Setup & evaluation"]
VERDICTS = {  # status colours, always shown with an icon and a word, never colour alone
    "ahead": ("▲", "Ahead", "#0ca30c"), "standard": ("●", "Standard", None),
    "behind": ("▼", "Behind", "#ec835a"), "missing": ("✕", "Not reported", "#d03b3b"),
    "na": ("–", "Not applicable", None),
}
BW, BH, GX, GY = 136, 156, 22, 44


def wrap(s, n):
    out, cur = [], ""
    for w in s.split():
        parts = [w]
        if len(w) > n:  # break long slash lists such as EEG/MEG/EMA/...
            parts = [p + "/" for p in w.split("/")[:-1]] + [w.split("/")[-1]]
        for i, part in enumerate(parts):
            glue = "" if i else " "
            if cur and len(cur) + len(glue) + len(part) > n:
                out.append(cur)
                cur = part
            else:
                cur = (cur + glue + part) if cur else part
    return out + ([cur] if cur else [])


def component_map(fig, t, top, present, paint):
    """Draw the 13 boxes and their routes; paint(svg, key, x, y) fills each box."""
    left = 16
    W = left * 2 + 6 * BW + 5 * GX
    H = top + 3 * BH + 2 * GY + 16
    svg = Svg(W, H, t, fig["title"])
    header(svg, fig, left)
    pos = {k: (left + c * (BW + GX), top + r * (BH + GY)) for k, (_, c, r) in SLOTS.items()}
    svg.add(f'<defs><marker id="a" viewBox="0 0 8 8" refX="7" refY="4" markerWidth="7" markerHeight="7" '
            f'orient="auto"><path d="M0,0 L8,4 L0,8 Z" fill="{t["muted"]}"/></marker></defs>')

    def anchor(k, side):
        x, y = pos[k]
        return {"l": (x, y + BH / 2), "r": (x + BW, y + BH / 2), "t": (x + BW / 2, y), "b": (x + BW / 2, y + BH)}[side]

    for a, b in ROUTES:
        ca, ra = SLOTS[a][1:]
        cb, rb = SLOTS[b][1:]
        on = a in present and b in present
        stroke, dash, w = (t["muted"], "", 1.5) if on else (t["axis"], ' stroke-dasharray="3 4"', 1.2)
        if (a, b) == ("M10", "M04"):  # the correction loop runs over the top
            x1, y1 = anchor(a, "t")
            x2, y2 = anchor(b, "t")
            yy = top - 30
            path = f"M{x1},{y1} L{x1},{yy} L{x2},{yy} L{x2},{y2 - 1}"
        elif ra == rb:
            (x1, y1), (x2, y2) = (anchor(a, "r"), anchor(b, "l")) if ca < cb else (anchor(a, "l"), anchor(b, "r"))
            path = f"M{x1},{y1} L{x2},{y2}"
        elif ca == cb:
            (x1, y1), (x2, y2) = (anchor(a, "b"), anchor(b, "t")) if ra < rb else (anchor(a, "t"), anchor(b, "b"))
            path = f"M{x1},{y1} L{x2},{y2}"
        else:
            x1, y1 = anchor(a, "t" if ra > rb else "b")
            x2, y2 = anchor(b, "b" if ra > rb else "t")
            x1 += -BW / 4 if ca > cb else BW / 4
            x2 += BW / 4 if ca > cb else -BW / 4
            path = f"M{x1},{y1} L{x2},{y2}"
        svg.add(f'<path d="{path}" fill="none" stroke="{stroke}" stroke-width="{w}"{dash} marker-end="url(#a)"/>')
    for i, lane in enumerate(LANES):
        x = pos["M04"][0] if i == 1 else pos["M05"][0]
        svg.text(x, top + i * (BH + GY) - 8, lane.upper(), 10, t["muted"], weight="600")
    for k, (label, _, _) in SLOTS.items():
        x, y = pos[k]
        paint(svg, k, x, y)
        svg.text(x + 10, y + 16, k, 10, t["muted"], weight="600")
        svg.text(x + 10, y + 31, label, 12, t["text"], weight="700")
    return svg


def mechanism(fig, t):
    """One paper: its choice per component and a verdict against common practice."""
    slots = fig["slots"]
    present = {k for k, v in slots.items() if v.get("choice")}

    def paint(svg, k, x, y):
        v = slots.get(k, {})
        icon, word, color = VERDICTS.get(v.get("verdict"), ("", "", None))
        has = k in present
        na = v.get("verdict") == "na"
        dash = "" if has and not na else ' stroke-dasharray="3 3"'
        svg.add(f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="6" fill="{t["band"] if has and not na else t["bg"]}" '
                f'stroke="{color or t["axis"]}" stroke-width="{2.5 if color else 1}"{dash}/>')
        body = [ln for c in (v.get("choice") or ["not reported"]) for ln in wrap(c, 19)][:3]
        for j, ln in enumerate(body):
            svg.text(x + 10, y + 50 + j * 15, ln, 12, t["text"] if has else t["muted"], italic=not has)
        if v.get("field"):
            svg.line(x + 10, y + 94, x + BW - 10, y + 94, t["axis"])
            if v.get("matched") is not None:
                n = f"{v['matched']:,} papers share it"
            else:
                n = f"n={v['n']}" if v.get("n") is not None else ""
            body = wrap("Field: " + v["field"], 23)
            if len(body) > 3:
                body = body[:2] + [body[2][:21] + "…"]
            for j, ln in enumerate(body + ([n] if n else [])):
                svg.text(x + 10, y + 107 + j * 12, ln, 10, t["muted"])
        if word:
            svg.text(x + BW - 10, y + 16, f"{icon} {word}", 10, color or t["muted"], "end", "700")

    svg = component_map(fig, t, 112, present, paint)
    lx = 16
    for key in ("ahead", "standard", "behind", "missing", "na"):
        icon, word, color = VERDICTS[key]
        svg.text(lx, 72, f"{icon} {word}", 11, color or t["muted"], weight="700")
        lx += 22 + 7.5 * len(word)
    svg.text(lx + 4, 72, "vs. common practice on any sensor", 11, t["muted"])
    return svg.done()


def coverage(fig, t):
    """The whole field: share of ledger entries that record each component (flags mark known under-recording)."""
    counts, total, flags = fig["counts"], fig["total"], fig.get("flags", {})
    present = set(SLOTS)

    def paint(svg, k, x, y):
        share = counts.get(k, 0) / total
        svg.add(f'<rect x="{x}" y="{y}" width="{BW}" height="{BH}" rx="6" fill="{t["bg"]}" stroke="{t["axis"]}"/>')
        # bar along the bottom of the box: length = share
        svg.add(f'<rect x="{x + 10}" y="{y + BH - 22}" width="{BW - 20}" height="8" rx="4" fill="{t["empty"]}"/>')
        if share > 0:
            svg.add(f'<rect x="{x + 10}" y="{y + BH - 22}" width="{max(4, (BW - 20) * share):.1f}" height="8" rx="4" '
                    f'fill="{t["series"][0]}"/>')
        pct = f"{share * 100:.0f}%" if share >= 0.01 else f"{share * 100:.1f}%"
        svg.text(x + 10, y + 78, pct, 30, t["text"], weight="700")
        svg.text(x + 10, y + 98, f"{counts.get(k, 0):,} of {total:,}", 11, t["muted"])
        if k in flags:
            svg.text(x + 10, y + 112, "△ " + flags[k], 10, t["muted"], weight="600")

    svg = component_map(fig, t, 112, present, paint)
    if fig.get("note"):
        svg.text(16, 72, fig["note"], 11, t["muted"])
    return svg.done()


KINDS["mechanism"] = mechanism
KINDS["coverage"] = coverage
