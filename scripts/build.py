#!/usr/bin/env python3
"""Generate every derived file of the repository (layout: docs/STRUCTURE.md).

Sources: data/reviews.jsonl, data/field.json, reviews/<slug>/{review.ja.md, refs.bib, slots.json,
figures.json, evaluation*.md, triage.ja.md}, components/<Mxx>/<topic>.json.
Generated: README.md, README.ja.md, data/papers.csv, data/metadata.json, figures/ (field figures),
reviews/<slug>/README.md, reviews/<slug>/figures/*.svg, components/README.md,
components/<Mxx>/README.md, components/<Mxx>/<topic>.csv.

    python3 scripts/build.py           # write files
    python3 scripts/build.py --check   # fail if generated files are out of date
"""
import csv
import re
import io
import json
import sys
from collections import Counter
from pathlib import Path

import figures as F

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REVIEWS_DIR = ROOT / "reviews"
FIG_DIR = ROOT / "figures"
COMPONENTS_DIR = ROOT / "components"
FIELD_JSON = DATA / "field.json"
SLOT_NAMES = {k: F.SLOTS[k][0] for k in sorted(F.SLOTS)}
REPO_URL = "https://github.com/supernaiter/silent-speech-review"

# Sections in display order. A paper goes to the first section whose rule matches.
SECTIONS = [
    ("surveys", "Surveys", "サーベイ"),
    ("epg", "Electropalatography & in-mouth sensors", "口蓋電極（EPG）・口腔内センサ"),
    ("ultrasound", "Ultrasound & tongue imaging", "超音波・舌の画像"),
    ("emg", "Surface EMG", "表面筋電（EMG）"),
    ("brain", "Brain signals (EEG, MEG, intracortical)", "脳信号（EEG・MEG・皮質内）"),
    ("rf", "Radar, RF & Wi-Fi", "レーダー・電波・Wi-Fi"),
    ("video", "Lip & face video", "唇・顔の映像"),
    ("acoustic", "Acoustic, whisper & wearable motion sensors", "音響・ささやき・装着型の動きセンサ"),
    ("other", "Other sensors", "その他のセンサ"),
]
SECTION_TITLES = {k: (en, ja) for k, en, ja in SECTIONS}

# Papers to read first, in order.
START_HERE = [
    "silent-speech-interfaces-in-the-era-of-large-language-models-a-comprehensive-taxonomy-and-system",
    "silent-speech-interfaces-for-speech-restoration-a-review",
    "digital-voicing-of-silent-speech",
    "sottovoce",
    "silentspeller",
    "liplearner-customizable-silent-speech-interactions-on-mobile-devices",
    "aessi-an-around-ear-silent-speech-interface-for-cross-day-online-reuse-without-test-day-calibrat",
    "reconstructing-unseen-sentences-from-speech-related-biosignals-for-open-vocabulary-neural-commun",
    "updating-the-silent-speech-challenge-benchmark-with-deep-learning",
]

MAINTAINER = "[Naoki Kimura](https://nao-ki-mura.com/) ([ORCID 0000-0001-9167-1923](https://orcid.org/0000-0001-9167-1923))"


def load():
    with open(DATA / "reviews.jsonl", encoding="utf-8") as f:
        papers = [json.loads(line) for line in f if line.strip()]
    papers.sort(key=lambda p: (-p["year"], p["title"].lower()))
    return papers


def tags(p, prefix):
    return [t.split(":", 1)[1] for t in p.get("tags", []) if t.startswith(prefix + ":")]


def section_of(p):
    mods = set(tags(p, "modality"))
    sites = set(tags(p, "body_site"))
    title = p["title"].lower()
    sensor = p["en"].get("sensor", "").lower()
    if ("survey" in tags(p, "task") or any(w in title for w in ("review", "survey", "taxonomy", "introduction to"))) and "poster" not in title:
        return "surveys"
    if "electropalatography" in mods:
        return "epg"
    if "ultrasound" in sensor and any(w in sensor for w in ("tongue", "probe", "b-mode", "transducer", "imaging")):
        return "ultrasound"
    if "emg" in mods:
        return "emg"
    if mods & {"eeg", "magnetic"} or "brain" in sites or "intracortical" in sensor:
        return "brain"
    if "radar" in mods or any(w in sensor for w in ("radar", "wi-fi", "wifi", "rfid", "mmwave", "backscatter")):
        return "rf"
    if mods & {"video", "camera"}:
        return "video"
    if mods & {"acoustic", "microphone", "vibration", "ultrasound"}:
        return "acoustic"
    return "other"


def paper_link(p):
    return p.get("doi_url") or p.get("arxiv_url") or ""


def cell(s):
    return (s or "").replace("|", "\\|").replace("\n", " ").strip()


def authors_short(p):
    a = p.get("authors") or []
    if not a:
        return ""
    return a[0] + (" et al." if len(a) > 2 else (" and " + a[1] if len(a) == 2 else ""))


def counts(papers):
    by = Counter(section_of(p) for p in papers)
    return [(k, by[k]) for k, _, _ in SECTIONS if by[k]]


def source_updated(papers):
    meta = DATA / "metadata.json"
    if meta.exists():
        return json.loads(meta.read_text()).get("source_updated_at", "")
    return ""


def review_page(p, papers=()):
    e = p["en"]
    links = []
    if p.get("doi_url"):
        links.append(f"[DOI]({p['doi_url']})")
    if p.get("arxiv_url"):
        links.append(f"[arXiv]({p['arxiv_url']})")
    sec_en, sec_ja = SECTION_TITLES[section_of(p)]
    out = [
        f"# {p['title']}",
        "",
        f"{', '.join(p.get('authors') or [])}  ",
        f"{venue_year(p)} · {' · '.join(links)}",
        "",
        f"**Section:** [{sec_en}](../../README.md#{anchor(sec_en)}) · **Review basis:** {p.get('review_basis', '')}",
        "",
        f"A structured review of *{p['title']}* ({authors_short(p) + ', ' if authors_short(p) else ''}{venue_year(p)}) "
        f"for the silent speech interface field: sensor, task, evaluation conditions, results and limitations.",
        "",
        e["summary"],
        "",
        "## Evaluation conditions",
        "",
        "| | |",
        "| --- | --- |",
        f"| Sensor | {cell(e['sensor'])} |",
        f"| Task | {cell(e['task'])} |",
        f"| Vocabulary | {cell(e['vocabulary'])} |",
        f"| Speaker | {cell(e['speaker'])} |",
        f"| Session | {cell(e['session'])} |",
        f"| Online / offline | {cell(e['mode'])} |",
        f"| Key result | {cell(e['key_result'])} |",
        "",
        f"**Limitations.** {e['limitations']}",
        "",
    ]
    out += figures_section(p)
    comp = component_review(p)
    if comp:
        out += comp
    else:
        out += legacy_review(p)
    out += materials_section(p)
    out += related_and_footer(p, papers, sec_en)
    return "\n".join(out)


def paper_dir(p):
    return REVIEWS_DIR / p["slug"]


def component_review(p):
    """Full component-by-component review (Japanese), if reviews/<slug>/review.ja.md exists."""
    f = paper_dir(p) / "review.ja.md"
    if not f.exists():
        return []
    lines = f.read_text(encoding="utf-8").splitlines()
    if lines and lines[0].startswith("# "):
        lines = lines[1:]
    body = []
    fence = False
    for line in lines:
        if line.startswith("```"):
            fence = not fence
        if not fence and line.startswith("#"):
            line = "#" + line
        line = line.replace(f"]({p['slug']}.bib)", "](refs.bib)")
        line = re.sub(re.escape(REPO_URL) + r"/blob/main/reviews/([a-z0-9-]+)\.md", r"../\1/", line)
        body.append(line)
    return ["## 構成要素別レビュー（日本語）", "", *body, ""]


def legacy_review(p):
    out = []
    jp = is_japanese(p.get("expert_take_long", "") + p.get("expert_take_short", ""))
    L = (lambda ja, en: ja) if jp else (lambda ja, en: en)
    out += [L("## 日本語レビュー", "## Full review"), ""]
    for ja, en, key in [
        ("要点", "In short", "expert_take_short"),
        ("レビュー", "Review", "expert_take_long"),
        ("この論文の価値", "Why it matters", "expert_true_value"),
        ("それまでの到達点", "Prior state of the art", "canon_before"),
        ("何が変わったか", "What changed", "delta_from_canon"),
        ("分野での位置づけ", "Position in the field", "position_in_field"),
        ("実用上の意味", "Practical value", "practical_value"),
        ("前進した軸", "Advanced", "axes_moved"),
        ("未解決の軸", "Unresolved", "axes_unresolved"),
        ("後退・限定した軸", "Narrowed or regressed", "axes_regressed"),
    ]:
        if p.get(key):
            out += [f"### {L(ja, en)}", "", p[key], ""]
    out += [f"### {L('評価条件', 'Evaluation details')}", "", L("| 項目 | 内容 |", "| Item | Details |"), "| --- | --- |"]
    for ja, en, key in [
        ("課題", "Task", "task"), ("入力", "Input", "input_modality"), ("センサ", "Sensor", "sensor_hardware"),
        ("装着部位", "Body site", "body_site"), ("出力", "Output", "output_type"),
        ("語彙の種類", "Vocabulary type", "vocabulary_type"), ("語彙数", "Vocabulary size", "vocabulary_size"),
        ("指標と結果", "Metrics and results", "metrics"), ("評価方法", "Evaluation protocol", "evaluation_mode"),
    ]:
        if p.get(key):
            out.append(f"| {L(ja, en)} | {cell(p[key])} |")
    out += ["", f"### {L('限界', 'Limits')}", ""]
    for ja, en, key in [
        ("技術", "Technical", "technical_limits"), ("評価", "Evaluation", "evaluation_limits"),
        ("実運用", "Deployment", "deployment_limits"), ("このレビューの範囲", "Scope of this review", "scope_limits"),
    ]:
        if p.get(key):
            out.append(f"- **{L(ja + '：', en + ':')}** {p[key]}")
    ev = p.get("evidence") or []
    if ev:
        out += ["", f"### {L('根拠', 'Evidence')}", ""]
        for x in ev:
            where = x.get("section_or_location")
            loc = L(f"（{where}）", f" ({where})") if where else ""
            out.append(f"- {x['statement']}{loc}")
    return out


def related_and_footer(p, papers, sec_en):
    out = []
    related = sorted(
        (q for q in papers if q["slug"] != p["slug"] and section_of(q) == section_of(p)),
        key=lambda q: (abs(q["year"] - p["year"]), -q["year"], q["title"].lower()),
    )[:6]
    if related:
        out += ["", f"## More reviews in {sec_en}", ""]
        out += [f"- [{q['title']}](../{q['slug']}/) ({q['year']}). {q['en']['summary']}" for q in related]
    out += [
        "",
        "---",
        "",
        f"Part of the [Silent Speech Interface Review]({REPO_URL}). "
        f"Found an error? [Open an issue]({REPO_URL}/issues/new?template=correction.yml).",
        "",
    ]
    return out


def paper_figures(p):
    f = paper_dir(p) / "figures.json"
    return json.loads(f.read_text(encoding="utf-8"))["figures"] if f.exists() else []


def figures_section(p):
    figs = paper_figures(p)
    if not figs:
        return []
    out = ["## Figures", ""]
    for fig in figs:
        out += [f"### {fig['title']}", ""]
        if fig["kind"] == "mermaid":
            out += ["```mermaid", fig["mermaid"].rstrip(), "```"]
        else:
            out.append(F.picture(f"figures/{fig['id']}", fig["title"]))
        if fig.get("caption"):
            out += ["", fig["caption"]]
        rows = F.data_table(fig)
        if rows:
            out += ["", "<details><summary>Data</summary>", ""] + rows + ["", "</details>"]
        out.append("")
    return out


def field_figures(prefix, lang="en"):
    f = FIELD_JSON
    if not f.exists():
        return []
    out = []
    for fig in json.loads(f.read_text(encoding="utf-8"))["figures"]:
        out += [F.picture(f"{prefix}figures/field/{fig['id']}", fig["title"]), ""]
        if lang == "en" and fig.get("caption"):
            out += [fig["caption"], ""]
    return out


def field_map(papers):
    first = 2018
    cols = [f"≤{first - 1}"] + [str(y) for y in range(first, max(p["year"] for p in papers) + 1)]
    keys = [k for k, _, _ in SECTIONS if any(section_of(p) == k for p in papers)]
    grid = [[0] * len(cols) for _ in keys]
    for p in papers:
        j = 0 if p["year"] < first else p["year"] - first + 1
        grid[keys.index(section_of(p))][j] += 1
    rows = [SECTION_TITLES[k][0] for k in keys]
    title = f"Reviewed papers by sensor and year (n={len(papers)})"
    sub = "Each cell counts the papers reviewed here, not the whole literature."
    return {mode: F.heatmap(title, sub, rows, cols, grid, t) for mode, t in F.THEMES.items()}


MATERIAL_FILES = [
    ("review.ja.md", "構成要素別レビューの本文（元データ）"),
    ("refs.bib", "参考文献（BibTeX）"),
    ("slots.json", "13 部品それぞれの、この論文の選択・分野の通例・該当論文数・判定"),
    ("figures.json", "図の定義"),
]


def topics():
    """All topic tables: components/<Mxx>/<topic>.json."""
    out = []
    for f in sorted(COMPONENTS_DIR.glob("M[0-9][0-9]/*.json")) if COMPONENTS_DIR.exists() else []:
        d = json.loads(f.read_text(encoding="utf-8"))
        d["_path"] = f
        out.append(d)
    return out


def tally_line(d):
    t = d.get("tally", {})
    return f"確認済み {t.get('confirmed_unique', 0)}、読んだ候補 {t.get('read', 0)}、未読 {t.get('unread', 0)}"


def materials_section(p):
    d = paper_dir(p)
    rows = [(f, desc) for f, desc in MATERIAL_FILES if (d / f).exists()]
    for f in sorted(d.glob("evaluation*.md")):
        rows.append((f.name, "執筆者と別の評価者による検証"))
    if (d / "triage.ja.md").exists():
        rows.append(("triage.ja.md", "評価の指摘を原典で確かめた判定と対応"))
    used = [t for t in topics() if p["slug"] in t.get("used_by", [])]
    if not rows and not used:
        return []
    out = ["", "## 材料", "", "このレビューを作るのに使ったデータです。原典の全文は含みません。", ""]
    out += [f"- [`{f}`]({f})：{desc}" for f, desc in rows]
    for t in used:
        rel = t["_path"].relative_to(ROOT).with_suffix(".csv").as_posix()
        out.append(f"- [`{rel}`](../../{rel})：{t['slot']} の話題「{t['topic']}」の候補論文と採否（{tally_line(t)}）")
    return out + [""]


def topic_csv(d):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    w.writerow(["decision", "paper_id", "title", "year", "found_via", "reason", "location", "quote"])
    order = {"include": 0, "exclude": 1}
    for c in sorted(d.get("candidates", []), key=lambda c: (order.get(c.get("decision"), 2), c["pid"])):
        w.writerow([c.get("decision") or "unread", c["pid"], c.get("title") or "", c.get("year") or "",
                    "+".join(c.get("via") or []), c.get("reason") or "", c.get("loc") or "", c.get("quote") or ""])
    return buf.getvalue()


def component_outputs(papers):
    files = {}
    ts = topics()
    titles = {p["slug"]: p["title"] for p in papers}
    by_slot = {}
    for t in ts:
        by_slot.setdefault(t["slot"], []).append(t)
        files[t["_path"].with_suffix(".csv")] = topic_csv(t)
    for slot, items in by_slot.items():
        out = [f"# {slot} {SLOT_NAMES.get(slot, '')}", "",
               "この部品について調べた話題と、確認済みの論文。各話題の表は分野全体（wiki の台帳と全文）を検索し、候補を原典で読んで採否を決めたもの。", ""]
        for t in items:
            name = t["_path"].stem
            out += [f"## {t['topic']}", "",
                    f"- 採否表：[`{name}.csv`]({name}.csv)（{tally_line(t)}、wiki {t.get('wiki_commit', '')[:7]}）"]
            if t.get("inclusion_rule"):
                out.append(f"- 採る条件：{t['inclusion_rule']}")
            if t.get("used_by"):
                out.append("- 使ったレビュー：" + "、".join(f"[{titles.get(s, s)}](../../reviews/{s}/)" for s in t["used_by"]))
            inc = [c for c in t.get("candidates", []) if c.get("decision") == "include"]
            if inc:
                out += ["", "| 論文 | 年 | 根拠の位置 |", "| --- | --- | --- |"]
                out += [f"| {cell(c.get('title') or c['pid'])} | {c.get('year') or ''} | {cell(c.get('loc') or '')} |" for c in inc]
            out.append("")
        files[COMPONENTS_DIR / slot / "README.md"] = "\n".join(out)
    idx = ["# 13 部品の索引", "",
           "音声意図のデコードは、センサーを問わず 13 の部品（M01〜M13）で書ける。ここには、レビューのために部品ごとに分野全体を調べた結果を置く。表は回を重ねて追記していく。", "",
           "| 部品 | 内容 | 話題 |", "| --- | --- | --- |"]
    for slot, name in SLOT_NAMES.items():
        items = by_slot.get(slot, [])
        cell_t = "、".join(f"[{t['topic']}]({slot}/)" for t in items) if items else "—"
        idx.append(f"| {slot} | {name} | {cell_t} |")
    files[COMPONENTS_DIR / "README.md"] = "\n".join(idx) + "\n"
    return files


def venue_year(p):
    v, y = p.get("venue", ""), str(p["year"])
    return v if (y in v or "'" + y[2:] in v) else f"{v} {y}".strip()


def is_japanese(text):
    jp = sum(1 for c in text if "\u3040" <= c <= "\u30ff" or "\u4e00" <= c <= "\u9fff")
    return jp > len(text) * 0.1


def anchor(title):
    s = title.lower()
    s = "".join(c for c in s if c.isalnum() or c in " -")
    return s.replace(" ", "-")


def table(rows):
    out = [
        "| Year | Paper | Task | Vocabulary | Speaker | Session | Online | Key result |",
        "| --- | --- | --- | --- | --- | --- | --- | --- |",
    ]
    for p in rows:
        e = p["en"]
        out.append(
            f"| {p['year']} | [{cell(p['title'])}](reviews/{p['slug']}/) | {cell(e['task'])} | "
            f"{cell(e['vocabulary'])} | {cell(e['speaker'])} | {cell(e['session'])} | {cell(e['mode'])} | "
            f"{cell(e['key_result'])} |"
        )
    return out


def readme(papers):
    by_slug = {p["slug"]: p for p in papers}
    years = [p["year"] for p in papers]
    updated = source_updated(papers)[:10]
    nav = " · ".join(f"[{SECTION_TITLES[k][0]}](#{anchor(SECTION_TITLES[k][0])}) ({n})" for k, n in counts(papers))
    out = [
        "# Silent Speech Interface Review",
        "",
        f"Reviews of **{len(papers)} silent speech interface (SSI) papers** ({min(years)}–{max(years)}), "
        "each with the conditions its results were measured under. "
        f"Maintained by {MAINTAINER}. Last updated {updated}.",
        "",
        "Silent speech interfaces turn articulation without audible voice into text or speech, using lip video, "
        "ultrasound tongue imaging, EMG, EEG, electropalatography, radar, acoustic sensing and more. "
        "Accuracies in this field are hard to compare: one paper recognizes 10 words from one speaker in one session, "
        "another decodes open sentences from new speakers on a later day. "
        "This review puts those conditions next to every headline number.",
        "",
        "Topics covered: silent speech recognition, lip reading and visual speech recognition (VSR), lip-to-speech and "
        "video-to-speech synthesis, EMG-to-speech, ultrasound tongue imaging, imagined and inner speech decoding from EEG and MEG, "
        "brain-to-text and speech neuroprostheses, radar and Wi-Fi sensing, and wearable silent speech text entry.",
        "",
        "[日本語の説明](README.ja.md)",
        "",
        f"**Sections:** {nav}",
        "",
        "## The field in 13 components",
        "",
        *field_figures(""),
        F.picture("figures/field-map", "Reviewed papers by sensor and year"),
        "",
        "## Start here",
        "",
    ]
    for i, slug in enumerate(START_HERE, 1):
        p = by_slug.get(slug)
        if p:
            out.append(f"{i}. [{p['title']}](reviews/{slug}/) ({p['year']}). {p['en']['summary']}")
    datasets = [p for p in papers if any(w in p["title"].lower() for w in ("dataset", "corpus", "benchmark")) and "closed-corpus" not in p["title"].lower()]
    if datasets:
        out += ["", "## Datasets and benchmarks", ""]
        out += [f"- [{p['title']}](reviews/{p['slug']}/) ({p['year']}). {p['en']['summary']}" for p in datasets]
    out += [
        "",
        "## How to read the tables",
        "",
        "- **Vocabulary**: the size of the set the system chooses from. A closed set of 10 commands is much easier than open sentences.",
        "- **Speaker**: *Speaker-dependent* means the model was trained and tested on the same person; *Speaker-independent* means it was tested on people not seen in training; *Both* means both were reported.",
        "- **Session**: *Same session* tests on data recorded in the same sitting; *Cross-session* and *Cross-day* test after the sensor was taken off and put back on, which is closer to real use.",
        "- **Online**: whether the system ran live with a user, or was evaluated offline on recorded data.",
        "- **Not stated** means the paper does not say. Each paper's page lists its limitations and a full review (in English or Japanese).",
        "",
    ]
    for key, n in counts(papers):
        en, _ = SECTION_TITLES[key]
        rows = [p for p in papers if section_of(p) == key]
        if key == "surveys":
            out += [f"## {en}", ""]
            out += [f"- [{p['title']}](reviews/{p['slug']}/) ({p['year']}). {p['en']['summary']}" for p in rows]
            out.append("")
        else:
            out += [f"## {en}", ""] + table(rows) + [""]
    out += [
        "## Data",
        "",
        "| File | Contents |",
        "| --- | --- |",
        "| [`data/papers.csv`](data/papers.csv) | One row per paper with the English evaluation fields, links and tags. |",
        "| [`data/reviews.jsonl`](data/reviews.jsonl) | Bibliographic data, classification and English summary fields for every paper, plus the older itemized reviews. |",
        "| [`reviews/`](reviews/) | One folder per paper: the readable page, and for component reviews the review text, references, per-component verdicts, figures, and the independent evaluation with its triage. |",
        "| [`components/`](components/) | The 13 components (M01–M13): for each topic searched across the field, every candidate paper with its include/exclude decision and reason. |",
        "| [`docs/STRUCTURE.md`](docs/STRUCTURE.md) | Where every file lives and which files are generated. |",
        "",
        "## How the reviews are made",
        "",
        "Each review is written from the paper's full text where available (the `review_basis` field says which). "
        "The English summary fields are condensed from each full review. "
        "Numbers are the authors' reported results under the stated conditions, not a re-run.",
        "",
        "## Contributing",
        "",
        f"- Suggest a paper: [open an issue]({REPO_URL}/issues/new?template=add-paper.yml).",
        f"- Report an error in a review: [open an issue]({REPO_URL}/issues/new?template=correction.yml).",
        "- Send a pull request: see [CONTRIBUTING.md](CONTRIBUTING.md). Edits go to `data/reviews.jsonl`; `python3 scripts/build.py` regenerates everything else.",
        "",
        "## Citation",
        "",
        "If you use this review, please cite it using [`CITATION.cff`](CITATION.cff) (GitHub's \"Cite this repository\" button).",
        "",
        "## License",
        "",
        "Review text and data: [CC BY 4.0](LICENSE). Paper titles, authors and metadata belong to their respective publishers.",
        "",
    ]
    return "\n".join(out)


def readme_ja(papers):
    by_slug = {p["slug"]: p for p in papers}
    updated = source_updated(papers)[:10]
    out = [
        "# サイレントスピーチ・インタフェース論文レビュー",
        "",
        f"サイレントスピーチ・インタフェース（SSI）の論文 **{len(papers)}本** を、結果がどの条件で測られたかと一緒にレビューしています。"
        f"管理：[木村直紀](https://nao-ki-mura.com/ja/)（[ORCID](https://orcid.org/0000-0001-9167-1923)）。最終更新 {updated}。",
        "",
        "SSIの精度は、語彙の大きさ、話者依存か、別日に付け直して測ったか、オンラインで動かしたかで大きく変わります。"
        "このレビューは、各論文の主な数字の横にこれらの条件を並べます。英語の比較表は [README](README.md) にあります。"
        "各論文のページには、英語の要約と評価条件の下に全文レビュー（日本語または英語）があります。",
        "",
        "## センサ別の本数",
        "",
        F.picture("figures/field-map", "センサと年ごとのレビュー本数"),
        "",
        "## 13の部品で見た分野",
        "",
        "センサが何であれ、発話意図の解読は同じ13の部品（学習時と利用時の行為、計測、復号、出力、確認と訂正、評価など）で記述できます。"
        "図の割合は、論文台帳がその部品を記録している割合で、分野の実態そのものではありません。"
        "利用時の補助情報（M07：言語モデルや辞書）は台帳の記入漏れが多いと分かっており（復号論文3,245本中、記録78本に対し、本文で使用に触れるものは推定約200本多い）、"
        "一方、確認（M09）と訂正（M10）は分野で実際に少なく（記述があるのは65本、漏れは推定十数本で文字入力BCIと入力システムに偏る）、"
        "学習専用の教師情報（M02）も記入漏れが多いと確認されました（記録31本に対し推定250本以上）。",
        "",
        *field_figures("", "ja"),
    ]
    for key, n in counts(papers):
        en, ja = SECTION_TITLES[key]
        out.append(f"- [{ja}](README.md#{anchor(en)})：{n}本")
    out += ["", "## 最初に読む論文", ""]
    for i, slug in enumerate(START_HERE, 1):
        p = by_slug.get(slug)
        if p:
            out.append(f"{i}. [{p['title']}](reviews/{slug}/)（{p['year']}）{p.get('expert_take_short', '')}")
    out += [
        "",
        "## 論文の追加と誤りの報告",
        "",
        f"Issue で受け付けています（[論文の追加]({REPO_URL}/issues/new?template=add-paper.yml)、[誤りの報告]({REPO_URL}/issues/new?template=correction.yml)）。",
        "",
    ]
    return "\n".join(out)


def papers_csv(papers):
    buf = io.StringIO()
    w = csv.writer(buf, lineterminator="\n")
    cols = ["paper_id", "slug", "year", "title", "venue", "authors", "doi", "arxiv_id", "paper_url", "review_page",
            "section", "summary", "sensor", "task", "vocabulary", "speaker", "session", "mode", "key_result",
            "limitations", "modality", "body_site"]
    w.writerow(cols)
    for p in papers:
        e = p["en"]
        w.writerow([
            p["paper_id"], p["slug"], p["year"], p["title"], p.get("venue", ""), "; ".join(p.get("authors") or []),
            p.get("doi", ""), p.get("arxiv_id", ""), paper_link(p), f"{REPO_URL}/tree/main/reviews/{p['slug']}",
            section_of(p), e["summary"], e["sensor"], e["task"], e["vocabulary"], e["speaker"], e["session"],
            e["mode"], e["key_result"], e["limitations"], "|".join(tags(p, "modality")), "|".join(tags(p, "body_site")),
        ])
    return buf.getvalue()


def metadata(papers):
    old = {}
    meta = DATA / "metadata.json"
    if meta.exists():
        old = json.loads(meta.read_text())
    return json.dumps({
        "source_updated_at": old.get("source_updated_at", ""),
        "counts": {
            "papers": len(papers),
            "evidence_records": sum(len(p.get("evidence") or []) for p in papers),
            "by_section": dict(counts(papers)),
        },
    }, indent=2, ensure_ascii=False) + "\n"


def moved_stub(p):
    """Page at the pre-folder URL reviews/<slug>.md, so indexed links keep working."""
    return "\n".join([
        f"# {p['title']}",
        "",
        f"**This review has moved to [reviews/{p['slug']}/]({p['slug']}/).**",
        "",
        p["en"].get("summary", ""),
        "",
        f"[Read the full review]({p['slug']}/) · [All reviews](../README.md)",
        "",
    ])


def outputs(papers):
    files = {
        ROOT / "README.md": readme(papers),
        ROOT / "README.ja.md": readme_ja(papers),
        DATA / "papers.csv": papers_csv(papers),
        DATA / "metadata.json": metadata(papers),
    }
    moved_list = DATA / "moved_pages.txt"
    moved = set(moved_list.read_text(encoding="utf-8").split()) if moved_list.exists() else set()
    for p in papers:
        files[paper_dir(p) / "README.md"] = review_page(p, papers)
        if p["slug"] in moved:
            files[REVIEWS_DIR / f"{p['slug']}.md"] = moved_stub(p)
        for fig in paper_figures(p):
            for mode, svg in (F.render(fig) or {}).items():
                files[paper_dir(p) / "figures" / f"{fig['id']}-{mode}.svg"] = svg
    files.update(component_outputs(papers))
    f = FIELD_JSON
    for fig in (json.loads(f.read_text(encoding="utf-8"))["figures"] if f.exists() else []):
        for mode, svg in F.render(fig).items():
            files[FIG_DIR / "field" / f"{fig['id']}-{mode}.svg"] = svg
    for mode, svg in field_map(papers).items():
        files[FIG_DIR / f"field-map-{mode}.svg"] = svg
    return files


def main():
    check = "--check" in sys.argv
    papers = load()
    files = outputs(papers)
    expected = set(files)
    stale = [p for p in REVIEWS_DIR.glob("*.md") if p not in expected] if REVIEWS_DIR.exists() else []
    stale += [p for p in REVIEWS_DIR.glob("*/README.md") if p not in expected] if REVIEWS_DIR.exists() else []
    stale += [p for p in REVIEWS_DIR.glob("*/figures/*.svg") if p not in expected] if REVIEWS_DIR.exists() else []
    stale += [p for p in FIG_DIR.rglob("*.svg") if p not in expected] if FIG_DIR.exists() else []
    stale += [p for p in COMPONENTS_DIR.rglob("*") if p.suffix in (".md", ".csv") and p not in expected] if COMPONENTS_DIR.exists() else []
    if check:
        bad = [str(p.relative_to(ROOT)) for p, text in files.items() if not p.exists() or p.read_text(encoding="utf-8") != text]
        bad += [str(p.relative_to(ROOT)) + " (not in data)" for p in stale]
        if bad:
            print("Generated files are out of date. Run: python3 scripts/build.py")
            print("\n".join("  " + b for b in bad[:50]))
            sys.exit(1)
        print(f"OK: {len(files)} generated files are up to date.")
        return
    REVIEWS_DIR.mkdir(exist_ok=True)
    for p in stale:
        p.unlink()
    for path, text in files.items():
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(text, encoding="utf-8")
    print(f"Wrote {len(files)} files for {len(papers)} papers.")


if __name__ == "__main__":
    main()
