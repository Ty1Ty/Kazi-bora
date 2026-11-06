"""Shared helpers: data model, layout (head / header / footer), JSON-LD, markdown, page writer, sitemap registry."""
import hashlib
import html
import json
import random
import re
from datetime import timedelta
from pathlib import Path

import config as C
import data as D

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "public"
STATIC = Path(__file__).resolve().parent / "static"
SITEMAP = []          # (path, lastmod, changefreq, priority)
esc = html.escape


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def ksh(n):
    return f"KSh {n:,}"


def url(path):
    return C.SITE_URL + path


def fmt_date(d):
    return f"{d.day} {d.strftime('%b %Y')}"


def plural(n, one, many=None):
    return f"{n} {one if n == 1 else (many or one + 's')}"


# ---------------------------------------------------------------- icons
ICONS = {
    "search": '<circle cx="11" cy="11" r="7"/><path d="m21 21-4.3-4.3"/>',
    "pin": '<path d="M20 10c0 6-8 12-8 12s-8-6-8-12a8 8 0 0 1 16 0Z"/><circle cx="12" cy="10" r="3"/>',
    "briefcase": '<rect x="2" y="7" width="20" height="14" rx="2"/><path d="M16 21V5a2 2 0 0 0-2-2h-4a2 2 0 0 0-2 2v16"/>',
    "clock": '<circle cx="12" cy="12" r="10"/><path d="M12 6v6l4 2"/>',
    "shield": '<path d="M12 22s8-4 8-10V5l-8-3-8 3v7c0 6 8 10 8 10Z"/><path d="m9 12 2 2 4-4"/>',
    "heart": '<path d="M19 14c1.5-1.5 3-3.2 3-5.5A5.5 5.5 0 0 0 16.5 3c-1.8 0-3 .5-4.5 2-1.5-1.5-2.7-2-4.5-2A5.5 5.5 0 0 0 2 8.5c0 2.3 1.5 4 3 5.5l7 7Z"/>',
    "arrow": '<path d="M5 12h14"/><path d="m12 5 7 7-7 7"/>',
    "check": '<path d="M20 6 9 17l-5-5"/>',
    "laptop": '<rect x="3" y="4" width="18" height="12" rx="2"/><path d="M2 20h20"/>',
    "cap": '<path d="M22 10 12 5 2 10l10 5 10-5Z"/><path d="M6 12v5c3 2 9 2 12 0v-5"/>',
    "building": '<rect x="4" y="2" width="16" height="20" rx="2"/><path d="M9 22v-4h6v4M8 6h.01M12 6h.01M16 6h.01M8 10h.01M12 10h.01M16 10h.01M8 14h.01M12 14h.01M16 14h.01"/>',
    "share": '<circle cx="18" cy="5" r="3"/><circle cx="6" cy="12" r="3"/><circle cx="18" cy="19" r="3"/><path d="m8.6 13.5 6.8 4M15.4 6.5l-6.8 4"/>',
    "menu": '<path d="M4 6h16M4 12h16M4 18h16"/>',
    "x": '<path d="M18 6 6 18M6 6l12 12"/>',
    "phone": '<path d="M22 16.9v3a2 2 0 0 1-2.2 2 19.8 19.8 0 0 1-8.6-3.1 19.5 19.5 0 0 1-6-6A19.8 19.8 0 0 1 2.1 4.2 2 2 0 0 1 4.1 2h3a2 2 0 0 1 2 1.7c.1 1 .4 1.9.7 2.8a2 2 0 0 1-.5 2.1L8.1 9.9a16 16 0 0 0 6 6l1.3-1.3a2 2 0 0 1 2.1-.4c.9.3 1.8.6 2.8.7a2 2 0 0 1 1.7 2Z"/>',
    "chat": '<path d="M21 11.5a8.5 8.5 0 0 1-12.6 7.4L3 21l2.1-5.2A8.5 8.5 0 1 1 21 11.5Z"/>',
    "file": '<path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8Z"/><path d="M14 2v6h6M8 13h8M8 17h8"/>',
    "users": '<path d="M16 21v-2a4 4 0 0 0-4-4H6a4 4 0 0 0-4 4v2"/><circle cx="9" cy="7" r="4"/><path d="M22 21v-2a4 4 0 0 0-3-3.9M16 3.1a4 4 0 0 1 0 7.8"/>',
    "mic": '<rect x="9" y="2" width="6" height="12" rx="3"/><path d="M19 10v1a7 7 0 0 1-14 0v-1M12 18v4"/>',
    "alert": '<path d="m21.7 18-8-14a2 2 0 0 0-3.4 0l-8 14A2 2 0 0 0 4 21h16a2 2 0 0 0 1.7-3Z"/><path d="M12 9v4M12 17h.01"/>',
    "bell": '<path d="M6 8a6 6 0 0 1 12 0c0 7 3 9 3 9H3s3-2 3-9"/><path d="M10.3 21a1.9 1.9 0 0 0 3.4 0"/>',
    "trend": '<path d="m22 7-8.5 8.5-5-5L2 17"/><path d="M16 7h6v6"/>',
    "star": '<path d="m12 2 3.1 6.3 6.9 1-5 4.9 1.2 6.8-6.2-3.3-6.2 3.3L8 14.2 3 9.3l6.9-1Z"/>',
    "print": '<path d="M6 9V2h12v7M6 18H4a2 2 0 0 1-2-2v-5a2 2 0 0 1 2-2h16a2 2 0 0 1 2 2v5a2 2 0 0 1-2 2h-2"/><rect x="6" y="14" width="12" height="8"/>',
    "plus": '<path d="M12 5v14M5 12h14"/>',
    "trash": '<path d="M3 6h18M8 6V4h8v2M19 6l-1 14H6L5 6M10 11v6M14 11v6"/>',
    "copy": '<rect x="9" y="9" width="13" height="13" rx="2"/><path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"/>',
    "chevron": '<path d="m6 9 6 6 6-6"/>',
    "mail": '<rect x="2" y="4" width="20" height="16" rx="2"/><path d="m22 7-10 6L2 7"/>',
    "lock": '<rect x="3" y="11" width="18" height="11" rx="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/>',
    "calendar": '<rect x="3" y="4" width="18" height="18" rx="2"/><path d="M16 2v4M8 2v4M3 10h18"/>',
    "flag": '<path d="M4 22V4M4 4h13l-2 4 2 4H4"/>',
}


def ico(name, cls="ico", size=20):
    return (f'<svg class="{cls}" width="{size}" height="{size}" viewBox="0 0 24 24" fill="none" stroke="currentColor" '
            f'stroke-width="2" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true" focusable="false">{ICONS[name]}</svg>')


# ---------------------------------------------------------------- data model
CAT = {c[0]: dict(slug=c[0], name=c[1], emoji=c[2], desc=c[3]) for c in D.CATEGORIES}
LOC = {l[0]: dict(slug=l[0], name=l[1], county=l[2], desc=l[3]) for l in D.LOCATIONS}
EMP = {}
for e in D.EMPLOYERS:
    EMP[e[0]] = dict(slug=e[0], name=e[1], industry=e[2], loc=e[3], size=e[4], verified=e[5], about=e[6],
                     url=f"/employers/{e[0]}/", logo=f"/assets/img/employers/{e[0]}.svg")

LOGO_COLORS = ["#0f6b4a", "#1d4ed8", "#b45309", "#7c3aed", "#be123c", "#0e7490", "#4d7c0f", "#a21caf", "#c2410c", "#334155"]


def initials(name):
    w = [x for x in re.split(r"[\s&]+", name) if x]
    return (w[0][0] + (w[1][0] if len(w) > 1 else "")).upper()


def logo_svg(name):
    col = LOGO_COLORS[int(hashlib.md5(name.encode()).hexdigest(), 16) % len(LOGO_COLORS)]
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="96" height="96" viewBox="0 0 96 96" role="img" aria-label="{esc(name)} logo (placeholder)">'
            f'<rect width="96" height="96" rx="20" fill="{col}"/><circle cx="78" cy="18" r="30" fill="#fff" opacity=".10"/>'
            f'<text x="48" y="60" text-anchor="middle" font-family="Arial,Helvetica,sans-serif" font-weight="700" font-size="38" fill="#fff">{initials(name)}</text></svg>')


def build_jobs():
    jobs = []
    for (title, emp_slug, cat, loc, jtype, level, smin, smax, remote, ago, left, featured, urgent) in D.JOBS:
        e, c, l = EMP[emp_slug], CAT[cat], LOC[loc]
        slug = f"{slugify(title)}-at-{emp_slug}"
        rnd = random.Random(slug)
        resp = rnd.sample(D.CAT_RESP[cat], min(5, len(D.CAT_RESP[cat])))
        reqs = [D.LEVEL_REQ[level], D.CAT_SKILLS[cat],
                "Good written and spoken English and Kiswahili, plus honesty and reliability"]
        if remote:
            reqs.append("A reliable laptop, stable internet and backup power or data for working remotely")
        if level == "internship":
            bens = ["Monthly stipend", "Mentorship from an experienced supervisor", "Certificate and reference letter on completion",
                    "Strong chance of a permanent role for top performers"]
        else:
            bens = rnd.sample(D.BENEFITS, 4)
        posted = C.TODAY - timedelta(days=ago)
        deadline = C.TODAY + timedelta(days=left)
        jobs.append(dict(
            id=slug, slug=slug, title=title, emp=e, cat=c, loc=l, type=jtype, level=level, level_name=D.LEVELS[level],
            smin=smin, smax=smax, remote=remote, ago=ago, left=left, featured=featured, urgent=urgent,
            posted=posted, deadline=deadline, resp=resp, reqs=reqs, bens=bens, url=f"/jobs/{slug}/"))
    return jobs


JOBS = build_jobs()
ARTICLES = D.ARTICLES
ART_SLUGS = {a["slug"] for a in ARTICLES}


def sal(j, short=False):
    unit = "stipend / month" if j["level"] == "internship" else "/ month"
    if short:
        return f"KSh {j['smin']//1000}k–{j['smax']//1000}k"
    return f"KSh {j['smin']:,} – {j['smax']:,} {unit}"


def where(j):
    return f"Remote · Kenya" if j["remote"] else j["loc"]["name"]


# ---------------------------------------------------------------- markdown (tiny)
def inline(t):
    t = esc(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    t = re.sub(r"(?<![\*\w])\*([^*\n]+)\*(?![\*\w])", r"<em>\1</em>", t)

    def link(m):
        href = m.group(2)
        if href.startswith("/") and href.strip("/") in ART_SLUGS:
            href = f"/career-advice/{href.strip('/')}/"
        return f'<a href="{href}">{m.group(1)}</a>'
    return re.sub(r"\[([^\]]+)\]\(([^)]+)\)", link, t)


def md(text):
    out, buf, kind = [], [], None

    def flush():
        nonlocal buf, kind
        if buf:
            tag = "ul" if kind == "ul" else "ol"
            out.append(f"<{tag}>" + "".join(f"<li>{inline(b)}</li>" for b in buf) + f"</{tag}>")
        buf, kind = [], None
    for raw in text.strip().split("\n"):
        line = raw.rstrip()
        if not line.strip():
            flush()
            continue
        m_ul, m_ol = re.match(r"^[-*]\s+(.*)", line), re.match(r"^\d+\.\s+(.*)", line)
        if m_ul or m_ol:
            k = "ul" if m_ul else "ol"
            if kind and kind != k:
                flush()
            kind = k
            buf.append((m_ul or m_ol).group(1))
            continue
        flush()
        if line.startswith("### "):
            out.append(f"<h3>{inline(line[4:])}</h3>")
        elif line.startswith("## "):
            out.append(f"<h2>{inline(line[3:])}</h2>")
        else:
            out.append(f"<p>{inline(line)}</p>")
    flush()
    return "\n".join(out)


# ---------------------------------------------------------------- assets
def asset_ver(rel):
    p = STATIC / rel
    if not p.exists():
        p = PUB / rel
    return hashlib.md5(p.read_bytes()).hexdigest()[:8] if p.exists() else "0"


# ---------------------------------------------------------------- JSON-LD
def ld(obj):
    return '<script type="application/ld+json">' + json.dumps(obj, ensure_ascii=False, separators=(",", ":")) + "</script>"


def org_schema():
    same = []
    o = {"@context": "https://schema.org", "@type": "Organization", "@id": C.SITE_URL + "/#org", "name": C.SITE_NAME,
         "url": C.SITE_URL + "/", "logo": url("/assets/img/logo-512.png"), "description": C.SITE_TAGLINE,
         "areaServed": {"@type": "Country", "name": "Kenya"},
         "contactPoint": [{"@type": "ContactPoint", "telephone": C.CONTACT_PHONE_TEL, "contactType": "customer support",
                           "areaServed": "KE", "availableLanguage": ["English", "Swahili"]}]}
    if C.CONTACT_EMAIL:
        o["contactPoint"][0]["email"] = C.CONTACT_EMAIL
    if same:
        o["sameAs"] = same
    return o


def website_schema():
    return {"@context": "https://schema.org", "@type": "WebSite", "@id": C.SITE_URL + "/#website", "url": C.SITE_URL + "/",
            "name": C.SITE_NAME, "inLanguage": C.LOCALE, "publisher": {"@id": C.SITE_URL + "/#org"},
            "potentialAction": {"@type": "SearchAction", "target": {"@type": "EntryPoint", "urlTemplate": C.SITE_URL + "/jobs/?q={search_term_string}"},
                                "query-input": "required name=search_term_string"}}


def crumbs_schema(crumbs):
    return {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "name": n, "item": url(p)} for i, (n, p) in enumerate(crumbs)]}


def faq_schema(faq):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
        {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faq]}


def itemlist_schema(items):
    return {"@context": "https://schema.org", "@type": "ItemList", "itemListElement": [
        {"@type": "ListItem", "position": i + 1, "url": url(j["url"]), "name": j["title"]} for i, j in enumerate(items[:30])]}


def jobposting_schema(j):
    e = j["emp"]
    s = {"@context": "https://schema.org", "@type": "JobPosting", "title": j["title"],
         "description": f"<p>{esc(e['about'])}</p>" + "<ul>" + "".join(f"<li>{esc(r)}</li>" for r in j["resp"]) + "</ul>",
         "datePosted": j["posted"].isoformat(), "validThrough": j["deadline"].isoformat() + "T23:59",
         "employmentType": {"Full-time": "FULL_TIME", "Part-time": "PART_TIME", "Contract": "CONTRACTOR", "Internship": "INTERN"}[j["type"]],
         "hiringOrganization": {"@type": "Organization", "name": e["name"], "logo": url(e["logo"])},
         "jobLocation": {"@type": "Place", "address": {"@type": "PostalAddress", "addressLocality": j["loc"]["name"],
                                                        "addressRegion": j["loc"]["county"], "addressCountry": "KE"}},
         "baseSalary": {"@type": "MonetaryAmount", "currency": "KES", "value": {"@type": "QuantitativeValue", "minValue": j["smin"],
                                                                                  "maxValue": j["smax"], "unitText": "MONTH"}},
         "directApply": True, "identifier": {"@type": "PropertyValue", "name": C.SITE_NAME, "value": j["slug"]}}
    if j["remote"]:
        s["jobLocationType"] = "TELECOMMUTE"
        s["applicantLocationRequirements"] = {"@type": "Country", "name": "Kenya"}
    return s


# ---------------------------------------------------------------- layout
NAV = [
    ("Jobs", "jobs", [
        ("Browse all jobs", "/jobs/", "briefcase"), ("Internships", "/internships/", "cap"),
        ("Entry-level jobs", "/entry-level-jobs/", "trend"), ("Remote jobs", "/remote-jobs/", "laptop"),
        ("Saved jobs", "/saved-jobs/", "heart"), ("Verified employers", "/employers/directory/", "building")]),
    ("Career tools", "tools", [
        ("CV builder", "/cv-builder/", "file"), ("Cover letter generator", "/cover-letter-generator/", "mail"),
        ("Interview prep trainer", "/interview-prep/", "mic"), ("Scam checker", "/scam-checker/", "shield"),
        ("Salary guide", "/salary-guide/", "trend"), ("CV writing service", "/cv-writing-service/", "star")]),
    ("Learn", "learn", [
        ("Career advice", "/career-advice/", "file"), ("Training & courses", "/training/", "cap")]),
]


def header(active=""):
    items = []
    for label, key, subs in NAV:
        subhtml = "".join(f'<li><a href="{h}">{ico(i, "ico", 18)}<span>{t}</span></a></li>' for t, h, i in subs)
        items.append(f'<li class="has-sub{" is-active" if active == key else ""}"><button type="button" class="sub-toggle" aria-expanded="false">{label}{ico("chevron", "ico chev", 16)}</button>'
                     f'<ul class="sub">{subhtml}</ul></li>')
    nav = "".join(items)
    return f'''<a class="skip" href="#main">Skip to content</a>
<div class="flagbar" aria-hidden="true"><i></i><i></i><i></i></div>
<div class="topbar"><div class="wrap topbar-in">
<p>{ico("shield", "ico", 16)} Every employer verified &middot; We never charge job seekers</p>
<p class="topbar-r"><a href="tel:{C.CONTACT_PHONE_TEL}">{ico("phone", "ico", 15)} {C.CONTACT_PHONE_DISPLAY}</a><a href="https://wa.me/{C.WHATSAPP_NUMBER}" rel="noopener" target="_blank">{ico("chat", "ico", 15)} WhatsApp</a></p>
</div></div>
<header class="site-header" id="top"><div class="wrap head-in">
<a class="brand" href="/" aria-label="{C.SITE_NAME} home"><img src="/assets/img/logo.svg" width="38" height="38" alt=""><span>Kazi<b>Bora</b></span></a>
<button class="nav-toggle" type="button" aria-label="Open menu" aria-expanded="false" aria-controls="site-nav">{ico("menu", "ico open", 26)}{ico("x", "ico close", 26)}</button>
<nav id="site-nav" class="site-nav" aria-label="Main"><ul>{nav}
<li class="plain{" is-active" if active == "employers" else ""}"><a href="/employers/">For employers</a></li></ul>
<a class="btn btn-amber nav-cta" href="/employers/post-a-job/">Post a job</a></nav>
</div></header>'''


def footer():
    pop_loc = "".join(f'<li><a href="/jobs-in-{l["slug"]}/">Jobs in {l["name"]}</a></li>' for l in LOC.values())
    pop_cat = "".join(f'<li><a href="/{c["slug"]}-jobs-in-kenya/">{c["name"]} jobs</a></li>' for c in list(CAT.values())[:8])
    contact_email = f'<li>{ico("mail", "ico", 16)} <a href="mailto:{C.CONTACT_EMAIL}">{C.CONTACT_EMAIL}</a></li>' if C.CONTACT_EMAIL else ""
    sample = ('<p class="sample-note">Demo content: the employers, jobs, courses and prices on this site are placeholders for design and testing. '
              'Replace them with real, verified listings before launch.</p>') if C.SHOW_SAMPLE_NOTICE else ""
    return f'''<footer class="site-footer"><div class="wrap">
<div class="foot-top">
<div class="foot-brand"><a class="brand brand-light" href="/"><img src="/assets/img/logo.svg" width="38" height="38" alt=""><span>Kazi<b>Bora</b></span></a>
<p>{C.SITE_TAGLINE}. Kenyan jobs, internships, entry-level roles and legitimate remote work, checked before they reach you.</p>
<ul class="contact"><li>{ico("phone", "ico", 16)} <a href="tel:{C.CONTACT_PHONE_TEL}">{C.CONTACT_PHONE_DISPLAY}</a></li>
<li>{ico("chat", "ico", 16)} <a href="https://wa.me/{C.WHATSAPP_NUMBER}" target="_blank" rel="noopener">Chat on WhatsApp</a></li>
{contact_email}<li>{ico("pin", "ico", 16)} {C.CONTACT_LOCATION}</li></ul></div>
<nav aria-label="Job seekers"><h2>Job seekers</h2><ul><li><a href="/jobs/">Browse jobs</a></li><li><a href="/internships/">Internships</a></li><li><a href="/entry-level-jobs/">Entry-level jobs</a></li><li><a href="/remote-jobs/">Remote jobs</a></li><li><a href="/saved-jobs/">Saved jobs</a></li><li><a href="/job-alerts/">Job alerts</a></li><li><a href="/training/">Training &amp; courses</a></li></ul></nav>
<nav aria-label="Career tools"><h2>Career tools</h2><ul><li><a href="/cv-builder/">Free CV builder</a></li><li><a href="/cover-letter-generator/">Cover letter generator</a></li><li><a href="/interview-prep/">Interview prep</a></li><li><a href="/scam-checker/">Scam checker</a></li><li><a href="/salary-guide/">Salary guide</a></li><li><a href="/cv-writing-service/">CV writing service</a></li><li><a href="/career-advice/">Career advice</a></li></ul></nav>
<nav aria-label="Employers"><h2>Employers</h2><ul><li><a href="/employers/">Hire with KaziBora</a></li><li><a href="/employers/post-a-job/">Post a job</a></li><li><a href="/employers/pricing/">Pricing &amp; packages</a></li><li><a href="/employers/register/">Employer registration</a></li><li><a href="/employers/advertising/">Recruitment advertising</a></li><li><a href="/employers/directory/">Employer directory</a></li><li><a href="/training-partners/">Training partners</a></li></ul></nav>
<nav aria-label="Popular searches"><h2>Popular searches</h2><ul>{pop_loc}</ul></nav>
<nav aria-label="Popular categories"><h2>Categories</h2><ul>{pop_cat}<li><a href="/#categories">All categories</a></li></ul></nav>
</div>
<div class="foot-mid"><p><strong>Stay safe:</strong> KaziBora never asks job seekers for money. If an advert asks you to pay, <a href="/report-scam/">report it</a> or check it with our <a href="/scam-checker/">scam checker</a>.</p></div>
{sample}
<div class="foot-bot"><p>&copy; {C.TODAY.year} {C.SITE_NAME}. All rights reserved. {C.BUILDER_CREDIT}.</p>
<ul><li><a href="/about/">About</a></li><li><a href="/verified-jobs/">How we verify</a></li><li><a href="/contact/">Contact</a></li><li><a href="/privacy/">Privacy</a></li><li><a href="/terms/">Terms</a></li><li><a href="/sitemap/">Sitemap</a></li></ul></div>
</div></footer>
<a class="wa-float" href="https://wa.me/{C.WHATSAPP_NUMBER}?text=Hello%20KaziBora" target="_blank" rel="noopener" aria-label="Chat with us on WhatsApp">{ico("chat", "ico", 26)}</a>'''


FONTS = ("https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800"
         "&family=Plus+Jakarta+Sans:wght@400;500;600;700&display=swap")


def head(title, desc, path, og="/assets/img/og-image.png", schema=(), noindex=False, extra="", og_type="website"):
    canon = url(path)
    suffix = f" | {C.SITE_NAME}"
    if len(title) > 62 and title.endswith(suffix):
        title = title[: -len(suffix)]          # keep SERP titles untruncated; brand is dropped only when too long
    robots = "noindex, follow" if noindex else "index, follow, max-image-preview:large, max-snippet:-1, max-video-preview:-1"
    ver_css, ver_js = asset_ver("css/style.css"), asset_ver("js/app.js")
    kb = {"ga4": C.GA4_ID, "gtm": C.GTM_ID, "ads": C.GOOGLE_ADS_ID, "meta": C.META_PIXEL_ID,
          "phone": C.CONTACT_PHONE_DISPLAY, "today": C.TODAY.isoformat(), "demo": bool(C.SHOW_SAMPLE_NOTICE)}
    verif = f'<meta name="google-site-verification" content="{C.GOOGLE_SITE_VERIFICATION}">' if C.GOOGLE_SITE_VERIFICATION else ""
    return f'''<!doctype html>
<html lang="en-KE">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{esc(title)}</title>
<meta name="description" content="{esc(desc if len(desc) <= 160 else desc[:157].rsplit(" ", 1)[0] + "...")}">
<meta name="robots" content="{robots}">
<link rel="canonical" href="{canon}">
<link rel="alternate" hreflang="en-KE" href="{canon}">
<link rel="alternate" hreflang="x-default" href="{canon}">
<meta name="theme-color" content="#0b3d2e">
<meta name="geo.region" content="KE"><meta name="geo.placename" content="Kenya">
{verif}
<meta property="og:site_name" content="{C.SITE_NAME}"><meta property="og:locale" content="en_KE">
<meta property="og:type" content="{og_type}"><meta property="og:title" content="{esc(title)}">
<meta property="og:description" content="{esc(desc)}"><meta property="og:url" content="{canon}">
<meta property="og:image" content="{url(og)}"><meta property="og:image:width" content="1200"><meta property="og:image:height" content="630">
<meta property="og:image:alt" content="{C.SITE_NAME}: {esc(C.SITE_TAGLINE)}">
<meta name="twitter:card" content="summary_large_image"><meta name="twitter:title" content="{esc(title)}">
<meta name="twitter:description" content="{esc(desc)}"><meta name="twitter:image" content="{url(og)}">
<link rel="icon" href="/favicon.svg" type="image/svg+xml"><link rel="icon" href="/assets/img/favicon-32.png" sizes="32x32" type="image/png">
<link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png"><link rel="manifest" href="/manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="{FONTS}" media="print" onload="this.media='all'">
<noscript><link rel="stylesheet" href="{FONTS}"></noscript>
<link rel="stylesheet" href="/assets/css/style.css?v={ver_css}">
<script>window.KB={json.dumps(kb)};</script>
<script src="/assets/js/app.js?v={ver_js}" defer></script>
{extra}
{"".join(ld(s) for s in schema)}
</head>'''


def breadcrumbs_html(crumbs):
    parts = []
    for i, (n, p) in enumerate(crumbs):
        if i == len(crumbs) - 1:
            parts.append(f'<li aria-current="page">{esc(n)}</li>')
        else:
            parts.append(f'<li><a href="{p}">{esc(n)}</a></li>')
    return '<nav class="crumbs" aria-label="Breadcrumb"><ol>' + "".join(parts) + "</ol></nav>"


def write(path, content):
    p = PUB / path.strip("/") / "index.html" if not path.endswith(".html") else PUB / path.strip("/")
    p.parent.mkdir(parents=True, exist_ok=True)
    p.write_text(content, encoding="utf-8")


def page(path, title, desc, body, *, active="", schema=(), og="/assets/img/og-image.png", crumbs=None, noindex=False,
         prio="0.6", freq="monthly", extra="", og_type="website", main_cls="", skip_main=False):
    sch = list(schema)
    if crumbs and len(crumbs) > 1:
        sch.append(crumbs_schema(crumbs))
    html_ = head(title, desc, path, og, sch, noindex, extra, og_type)
    html_ += f'\n<body>\n{header(active)}\n<main id="main" class="{main_cls}">\n{body}\n</main>\n{footer()}\n</body>\n</html>\n'
    write(path, html_)
    if not noindex and not path.endswith(".html"):
        SITEMAP.append((path, C.TODAY.isoformat(), freq, prio))


def hero_small(h1, lead, crumbs=None, extra=""):
    bc = breadcrumbs_html(crumbs) if crumbs else ""
    return f'<section class="page-hero"><div class="wrap">{bc}<h1>{h1}</h1><p class="lead">{lead}</p>{extra}</div></section>'


# ---------------------------------------------------------------- shared components
def verified_badge(e=None):
    if e is not None and not e["verified"]:
        return '<span class="badge pending" title="Verification in progress">Verification pending</span>'
    return f'<span class="badge verified" title="Business details, vacancy and no-fee promise checked">{ico("shield", "ico", 14)} Verified</span>'


def job_card(j, compact=False):
    e = j["emp"]
    tags = [f'<span class="tag lvl-{j["level"]}">{j["level_name"]}</span>']
    if j["remote"]:
        tags.append('<span class="tag t-remote">Remote</span>')
    if j["featured"]:
        tags.append('<span class="tag t-feat">Featured</span>')
    if j["urgent"]:
        tags.append('<span class="tag t-urgent">Urgent</span>')
    attrs = (f'data-id="{j["id"]}" data-title="{esc(j["title"].lower())}" data-company="{esc(e["name"].lower())}" '
             f'data-cat="{j["cat"]["slug"]}" data-loc="{j["loc"]["slug"]}" data-level="{j["level"]}" data-type="{j["type"]}" '
             f'data-remote="{int(j["remote"])}" data-verified="{int(e["verified"])}" data-featured="{int(j["featured"])}" '
             f'data-salary="{j["smax"]}" data-ago="{j["ago"]}" data-left="{j["left"]}"')
    return f'''<article class="job-card{" is-featured" if j["featured"] else ""}" {attrs}>
<a class="job-logo" href="{e["url"]}" tabindex="-1" aria-hidden="true"><img src="{e["logo"]}" width="56" height="56" alt="" loading="lazy"></a>
<div class="job-main">
<h3><a href="{j["url"]}">{esc(j["title"])}</a></h3>
<p class="job-co"><a href="{e["url"]}">{esc(e["name"])}</a> {verified_badge(e)}</p>
<ul class="job-meta"><li>{ico("pin", "ico", 16)} {esc(where(j))}</li><li>{ico("briefcase", "ico", 16)} {j["type"]}</li><li>{ico("trend", "ico", 16)} {esc(sal(j, True))} /mo</li></ul>
<p class="job-tags">{"".join(tags)}</p>
</div>
<div class="job-side"><button type="button" class="save" data-save="{j["id"]}" aria-pressed="false" aria-label="Save {esc(j["title"])}">{ico("heart", "ico", 20)}</button>
<span class="when" data-posted>Posted {ago_text(j["ago"])}</span><span class="closes" data-closes>Closes {fmt_date(j["deadline"])}</span>
<a class="btn btn-sm btn-primary" href="{j["url"]}">View job</a></div>
</article>'''


def ago_text(n):
    return "today" if n == 0 else ("yesterday" if n == 1 else f"{n} days ago")


def job_list(jobs, empty="No jobs here yet. Check back soon or set up a job alert."):
    if not jobs:
        return f'<p class="empty">{empty}</p>'
    return '<div class="job-list">' + "".join(job_card(j) for j in jobs) + "</div>"


def faq_html(faq, heading="Frequently asked questions"):
    items = "".join(f'<details class="faq-item"><summary>{esc(q)}</summary><div><p>{inline(a)}</p></div></details>' for q, a in faq)
    return f'<section class="section"><div class="wrap narrow"><h2 class="sec-title">{heading}</h2><div class="faq">{items}</div></div></section>'


def form(name, fields, button="Submit", note="", cls="", enctype=""):
    enc = f' enctype="{enctype}"' if enctype else ""
    return (f'<form class="form {cls}" name="{name}" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="bot-field"{enc}>'
            f'<input type="hidden" name="form-name" value="{name}">'
            f'<p class="hp" aria-hidden="true"><label>Leave this empty <input name="bot-field" tabindex="-1" autocomplete="off"></label></p>'
            f'{fields}<button class="btn btn-primary btn-lg" type="submit">{button}</button>{("<p class=form-note>" + note + "</p>") if note else ""}</form>')


def field(label, name, typ="text", req=False, ph="", extra="", help_=""):
    r = " required" if req else ""
    star = ' <span class="req" aria-hidden="true">*</span>' if req else ""
    h = f'<small>{help_}</small>' if help_ else ""
    if typ == "textarea":
        inp = f'<textarea id="f-{name}" name="{name}" rows="4" placeholder="{esc(ph)}"{r} {extra}></textarea>'
    elif typ == "select":
        inp = f'<select id="f-{name}" name="{name}"{r} {extra}>{ph}</select>'
    else:
        inp = f'<input id="f-{name}" name="{name}" type="{typ}" placeholder="{esc(ph)}"{r} {extra}>'
    return f'<div class="fld"><label for="f-{name}">{label}{star}</label>{inp}{h}</div>'


def options(pairs, first=None):
    o = f'<option value="">{first}</option>' if first else ""
    return o + "".join(f'<option value="{esc(v)}">{esc(t)}</option>' for v, t in pairs)


def cta_band(title, text, primary, secondary=None):
    sec = f'<a class="btn btn-ghost-light btn-lg" href="{secondary[1]}">{secondary[0]}</a>' if secondary else ""
    return (f'<section class="cta-band"><div class="wrap cta-in"><div><h2>{title}</h2><p>{text}</p></div>'
            f'<div class="cta-btns"><a class="btn btn-amber btn-lg" href="{primary[1]}">{primary[0]}</a>{sec}</div></div></section>')
