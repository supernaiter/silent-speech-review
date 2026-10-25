#!/usr/bin/env python3
"""Generate README.md, README.ja.md, data/papers.csv, data/metadata.json and
reviews/<slug>.md from data/reviews.jsonl (the single source of truth).

    python3 scripts/build.py           # write files
    python3 scripts/build.py --check   # fail if generated files are out of date
"""
import csv
import io
import json
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
REVIEWS_DIR = ROOT / "reviews"
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
    if any(w in title for w in ("review", "survey", "taxonomy", "introduction to")) and "poster" not in title:
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


def review_page(p):
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
        f"**Section:** [{sec_en}](../README.md#{anchor(sec_en)}) · **Review basis:** {p.get('review_basis', '')}",
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
    out += [
        "",
        "---",
        "",
        f"Part of the [Silent Speech Interface Review]({REPO_URL}). "
        f"Found an error? [Open an issue]({REPO_URL}/issues/new?template=correction.yml).",
        "",
    ]
    return "\n".join(out)


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
            f"| {p['year']} | [{cell(p['title'])}](reviews/{p['slug']}.md) | {cell(e['task'])} | "
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
        "[日本語の説明](README.ja.md)",
        "",
        f"**Sections:** {nav}",
        "",
        "## Start here",
        "",
    ]
    for i, slug in enumerate(START_HERE, 1):
        p = by_slug.get(slug)
        if p:
            out.append(f"{i}. [{p['title']}](reviews/{slug}.md) ({p['year']}). {p['en']['summary']}")
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
            out += [f"- [{p['title']}](reviews/{p['slug']}.md) ({p['year']}). {p['en']['summary']}" for p in rows]
            out.append("")
        else:
            out += [f"## {en}", ""] + table(rows) + [""]
    out += [
        "## Data",
        "",
        "| File | Contents |",
        "| --- | --- |",
        "| [`data/papers.csv`](data/papers.csv) | One row per paper with the English evaluation fields, links and tags. |",
        "| [`data/reviews.jsonl`](data/reviews.jsonl) | Full structured reviews: English summary fields plus the full review, evaluation conditions, limits and evidence statements. This is the source every other file is generated from. |",
        "| [`reviews/`](reviews/) | One readable page per paper. |",
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
    ]
    for key, n in counts(papers):
        en, ja = SECTION_TITLES[key]
        out.append(f"- [{ja}](README.md#{anchor(en)})：{n}本")
    out += ["", "## 最初に読む論文", ""]
    for i, slug in enumerate(START_HERE, 1):
        p = by_slug.get(slug)
        if p:
            out.append(f"{i}. [{p['title']}](reviews/{slug}.md)（{p['year']}）{p.get('expert_take_short', '')}")
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
            p.get("doi", ""), p.get("arxiv_id", ""), paper_link(p), f"{REPO_URL}/blob/main/reviews/{p['slug']}.md",
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


def outputs(papers):
    files = {
        ROOT / "README.md": readme(papers),
        ROOT / "README.ja.md": readme_ja(papers),
        DATA / "papers.csv": papers_csv(papers),
        DATA / "metadata.json": metadata(papers),
    }
    for p in papers:
        files[REVIEWS_DIR / f"{p['slug']}.md"] = review_page(p)
    return files


def main():
    check = "--check" in sys.argv
    papers = load()
    files = outputs(papers)
    expected = set(files)
    stale = [p for p in REVIEWS_DIR.glob("*.md") if p not in expected] if REVIEWS_DIR.exists() else []
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
        path.write_text(text, encoding="utf-8")
    print(f"Wrote {len(files)} files for {len(papers)} papers.")


if __name__ == "__main__":
    main()
