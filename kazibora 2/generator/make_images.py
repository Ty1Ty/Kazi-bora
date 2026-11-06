#!/usr/bin/env python3
"""Generates the placeholder artwork (SVG + PNG) into generator/static/img. Run once; the output is committed.
PNGs (OG image, app icons) need Playwright + Chromium; if it is missing they are skipped and the committed ones stay."""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config as C                      # noqa: E402
import data as D                        # noqa: E402
from lib import ICONS                   # noqa: E402

IMG = Path(__file__).resolve().parent / "static" / "img"
ROOT_STATIC = Path(__file__).resolve().parent / "static" / "root"
(IMG / "articles").mkdir(parents=True, exist_ok=True)
ROOT_STATIC.mkdir(parents=True, exist_ok=True)

MARK = ('<defs><linearGradient id="g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#138a5b"/><stop offset="1" stop-color="#0b3d2e"/></linearGradient></defs>'
        '{bg}<path d="M20 16v32" stroke="#fff" stroke-width="7" stroke-linecap="round"/>'
        '<path d="M45 17 29 33l16 15" stroke="#fff" stroke-width="7" stroke-linecap="round" stroke-linejoin="round" fill="none"/><circle cx="47" cy="17" r="5" fill="#f5a524"/>')


def logo(rx=16, size=64):
    bg = f'<rect width="64" height="64" rx="{rx}" fill="url(#g)"/>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="{size}" height="{size}" viewBox="0 0 64 64" role="img" aria-label="KaziBora logo">{MARK.format(bg=bg)}</svg>'


def skyline(x0, y_base, seed=1):
    out, x = [], x0
    import random
    r = random.Random(seed)
    cols = ["#0b3d2e", "#0f5a41", "#14704f", "#0d4a36"]
    while x < 640:
        w, h = r.randint(34, 60), r.randint(70, 200)
        c = r.choice(cols)
        out.append(f'<rect x="{x}" y="{y_base - h}" width="{w}" height="{h}" rx="3" fill="{c}"/>')
        for wy in range(y_base - h + 12, y_base - 10, 18):
            for wx in range(x + 8, x + w - 8, 14):
                if r.random() > .35:
                    out.append(f'<rect x="{wx}" y="{wy}" width="6" height="9" rx="1.5" fill="#f5a524" opacity="{r.choice([.9, .7, .35])}"/>')
        x += w + r.randint(4, 10)
    # KICC-style tower
    out.append(f'<rect x="430" y="{y_base - 250}" width="22" height="250" fill="#06261c"/><ellipse cx="441" cy="{y_base - 258}" rx="34" ry="14" fill="#06261c"/>'
               f'<ellipse cx="441" cy="{y_base - 262}" rx="26" ry="9" fill="#0b3d2e"/><rect x="437" y="{y_base - 300}" width="8" height="40" fill="#06261c"/>')
    return "".join(out)


def hero():
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="520" viewBox="0 0 640 520" role="img" aria-label="Nairobi skyline with job cards">
<defs><linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#fff4d9"/><stop offset=".55" stop-color="#ffe0a3"/><stop offset="1" stop-color="#d9efe3"/></linearGradient>
<linearGradient id="gr" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#138a5b"/><stop offset="1" stop-color="#0b3d2e"/></linearGradient></defs>
<rect width="640" height="520" fill="url(#sky)"/><circle cx="500" cy="130" r="70" fill="#f5a524" opacity=".9"/><circle cx="500" cy="130" r="100" fill="#f5a524" opacity=".18"/>
<g>{skyline(-10, 380, 7)}</g>
<rect y="380" width="640" height="140" fill="#0b3d2e"/><rect y="380" width="640" height="8" fill="#138a5b"/>
<g transform="translate(70 330)"><path d="M0 60C0 30 20 14 70 14s70 16 70 46Z" fill="#0f5a41"/><rect x="66" y="52" width="8" height="40" fill="#5b3a1e"/><path d="M-20 30C10 8 40 0 70 8s60-6 90 22C130 20 100 22 70 24 40 22 10 20-20 30Z" fill="#14704f"/></g>
<g transform="translate(60 250)"><rect width="330" height="190" rx="22" fill="#fff"/><rect x="24" y="24" width="52" height="52" rx="14" fill="url(#gr)"/><path d="M42 36v28M62 38 50 50l12 12" stroke="#fff" stroke-width="5" fill="none" stroke-linecap="round" stroke-linejoin="round"/>
<rect x="92" y="28" width="150" height="14" rx="7" fill="#14211c"/><rect x="92" y="52" width="100" height="10" rx="5" fill="#b9c9c1"/><rect x="238" y="26" width="68" height="24" rx="12" fill="#e3f4ec"/><circle cx="252" cy="38" r="5" fill="#138a5b"/><rect x="262" y="35" width="34" height="6" rx="3" fill="#138a5b"/>
<rect x="24" y="96" width="82" height="24" rx="12" fill="#e0e7ff"/><rect x="114" y="96" width="70" height="24" rx="12" fill="#fff3dc"/><rect x="192" y="96" width="60" height="24" rx="12" fill="#fae8ff"/>
<rect x="24" y="140" width="170" height="12" rx="6" fill="#dfe7e2"/><rect x="24" y="160" width="120" height="10" rx="5" fill="#eef3ef"/><rect x="226" y="136" width="80" height="34" rx="17" fill="#f5a524"/><rect x="244" y="148" width="44" height="10" rx="5" fill="#2a1a00" opacity=".7"/></g>
<g transform="translate(330 140)"><rect width="250" height="150" rx="20" fill="#fff" stroke="#e3ebe6"/><circle cx="46" cy="50" r="24" fill="#f5a524"/><circle cx="46" cy="44" r="9" fill="#fff"/><path d="M28 70c3-12 33-12 36 0" fill="#fff"/>
<rect x="84" y="32" width="110" height="12" rx="6" fill="#14211c"/><rect x="84" y="54" width="80" height="9" rx="4.5" fill="#b9c9c1"/><rect x="22" y="94" width="206" height="10" rx="5" fill="#dfe7e2"/><rect x="22" y="114" width="150" height="10" rx="5" fill="#eef3ef"/></g>
</svg>'''


def employers_hero():
    bars = "".join(f'<rect x="{40 + i * 38}" y="{200 - h}" width="24" height="{h}" rx="6" fill="{"#f5a524" if i == 4 else "#138a5b"}"/>' for i, h in enumerate([50, 80, 64, 110, 140, 96]))
    rows = ""
    for i, (n, c) in enumerate([("#0f6b4a", "#e3f4ec"), ("#1d4ed8", "#e0e7ff"), ("#be123c", "#fdecea"), ("#b45309", "#fff3dc")]):
        y = 250 + i * 52
        rows += (f'<circle cx="64" cy="{y + 16}" r="16" fill="{n}"/><rect x="92" y="{y + 4}" width="120" height="10" rx="5" fill="#14211c"/><rect x="92" y="{y + 22}" width="80" height="8" rx="4" fill="#b9c9c1"/>'
                 f'<rect x="300" y="{y + 6}" width="72" height="22" rx="11" fill="{c}"/>')
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="520" viewBox="0 0 640 520" role="img" aria-label="Employer dashboard with applicants">
<defs><linearGradient id="e" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff4d9"/><stop offset="1" stop-color="#d9efe3"/></linearGradient></defs>
<rect width="640" height="520" fill="url(#e)"/><circle cx="560" cy="80" r="120" fill="#f5a524" opacity=".18"/>
<g transform="translate(70 40)"><rect width="440" height="450" rx="24" fill="#fff" stroke="#dfe7e2"/><rect x="24" y="24" width="140" height="14" rx="7" fill="#14211c"/><rect x="24" y="48" width="200" height="9" rx="4.5" fill="#b9c9c1"/>
<rect x="318" y="22" width="98" height="30" rx="15" fill="#e3f4ec"/><circle cx="336" cy="37" r="6" fill="#138a5b"/><rect x="348" y="33" width="56" height="8" rx="4" fill="#138a5b"/>
<g transform="translate(0 60)">{bars}</g><g transform="translate(0 -10)">{rows}</g></g>
<g transform="translate(400 330)"><rect width="190" height="120" rx="18" fill="#0b3d2e"/><text x="22" y="52" font-family="Arial,sans-serif" font-size="38" font-weight="700" fill="#fff">48</text><text x="22" y="76" font-family="Arial,sans-serif" font-size="14" fill="#b9d6c8">new applicants</text><rect x="22" y="90" width="90" height="10" rx="5" fill="#f5a524"/></g>
</svg>'''


ART_ICON = {"CV & Cover Letters": "file", "Safety & Scams": "shield", "Interview Preparation": "mic", "Internships": "cap", "Entry-Level Careers": "trend", "Remote Work": "laptop", "Career Growth": "trend"}
PALETTES = [("#0f6b4a", "#0b3d2e", "#f5a524"), ("#b91c1c", "#7f1d1d", "#fde68a"), ("#1d4ed8", "#1e3a8a", "#fcd34d"), ("#7c3aed", "#4c1d95", "#fbbf24"), ("#0e7490", "#164e63", "#fcd34d"), ("#b45309", "#78350f", "#fde68a"),
            ("#be185d", "#831843", "#fde68a"), ("#047857", "#064e3b", "#fbbf24"), ("#4338ca", "#312e81", "#fcd34d")]


def cover(i, a):
    c1, c2, acc = PALETTES[i % len(PALETTES)]
    icon = ICONS["file" if a["tag"] == "CV & Cover Letters" and "cover" in a["slug"] and False else ART_ICON.get(a["tag"], "star")]
    if "cover-letter" in a["slug"]:
        icon = ICONS["mail"]
    if "panel" in a["slug"]:
        icon = ICONS["users"]
    circles = "".join(f'<circle cx="{x}" cy="{y}" r="{r}" fill="#fff" opacity="{o}"/>' for x, y, r, o in [(80, 60, 90, .06), (560, 300, 140, .07), (330, 340, 60, .05), (600, 40, 40, .08)])
    return f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="360" viewBox="0 0 640 360" role="img" aria-label="{a["title"]} cover illustration">
<defs><linearGradient id="a" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{c1}"/><stop offset="1" stop-color="{c2}"/></linearGradient></defs>
<rect width="640" height="360" fill="url(#a)"/>{circles}
<g transform="translate(232 82) scale(7)" fill="none" stroke="#fff" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" opacity=".95">{icon}</g>
<circle cx="520" cy="80" r="22" fill="{acc}"/><rect x="40" y="300" width="120" height="10" rx="5" fill="#fff" opacity=".5"/><rect x="40" y="320" width="80" height="8" rx="4" fill="#fff" opacity=".3"/></svg>'''


def main():
    (IMG / "logo.svg").write_text(logo(), encoding="utf-8")
    (ROOT_STATIC / "favicon.svg").write_text(logo(), encoding="utf-8")
    (IMG / "hero.svg").write_text(hero(), encoding="utf-8")
    (IMG / "employers-hero.svg").write_text(employers_hero(), encoding="utf-8")
    for i, a in enumerate(D.ARTICLES):
        (IMG / "articles" / f"{a['slug']}.svg").write_text(cover(i, a), encoding="utf-8")
    print("SVGs written")
    try:
        from playwright.sync_api import sync_playwright
    except Exception:
        print("Playwright not available: skipping PNGs")
        return
    og = f'''<html><body style="margin:0;width:1200px;height:630px;font-family:'Helvetica Neue',Arial,sans-serif;background:linear-gradient(135deg,#072e22,#0f6b4a);color:#fff;position:relative;overflow:hidden">
<div style="position:absolute;right:-120px;top:-120px;width:520px;height:520px;border-radius:50%;background:#f5a524;opacity:.22"></div>
<div style="position:absolute;left:0;top:0;right:0;height:10px;display:flex"><i style="flex:1;background:#111"></i><i style="flex:1;background:#bb1e1e"></i><i style="flex:1;background:#138a5b"></i></div>
<div style="position:absolute;left:72px;top:70px;display:flex;align-items:center;gap:20px">{logo(18, 84)}<span style="font-size:58px;font-weight:800;letter-spacing:-1px">Kazi<span style="color:#f5a524">Bora</span></span></div>
<div style="position:absolute;left:72px;top:215px;width:900px;font-size:78px;line-height:1.05;font-weight:800;letter-spacing:-2px">Verified jobs, internships &amp; skills in Kenya</div>
<div style="position:absolute;left:72px;top:455px;font-size:30px;color:#cfe9db">Free CV tools · Interview prep · Scam-safe job search</div>
<div style="position:absolute;left:72px;top:530px;display:flex;gap:14px;font-size:24px;font-weight:700"><span style="background:#f5a524;color:#2a1a00;padding:12px 26px;border-radius:40px">Internships</span><span style="background:rgba(255,255,255,.15);padding:12px 26px;border-radius:40px">Entry-level</span><span style="background:rgba(255,255,255,.15);padding:12px 26px;border-radius:40px">Remote jobs</span></div>
</body></html>'''
    with sync_playwright() as p:
        b = p.chromium.launch()
        pg = b.new_page(viewport={"width": 1200, "height": 630})
        pg.set_content(og)
        pg.screenshot(path=str(IMG / "og-image.png"))
        for name, size, rx in [("logo-192", 192, 40), ("logo-512", 512, 112), ("apple-touch-icon", 180, 0), ("favicon-32", 32, 8)]:
            pg2 = b.new_page(viewport={"width": size, "height": size})
            pg2.set_content(f'<html><body style="margin:0;background:transparent">{logo(rx, size)}</body></html>')
            pg2.screenshot(path=str(IMG / f"{name}.png"), omit_background=(rx != 0))
        b.close()
    print("PNGs written")


if __name__ == "__main__":
    main()
