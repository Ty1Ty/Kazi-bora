#!/usr/bin/env python3
"""Builds the complete static site into ./public (ready for GitHub + Netlify).

    python3 generator/build.py                       # uses SITE_URL from config.py
    python3 generator/build.py https://yourdomain.co.ke
"""
import json
import shutil
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import config as C                      # noqa: E402
import lib                              # noqa: E402
from lib import PUB, STATIC, SITEMAP, EMP, JOBS, esc, sal, where  # noqa: E402
import pages_jobs                       # noqa: E402
import pages_content                    # noqa: E402


def main():
    if PUB.exists():
        shutil.rmtree(PUB)
    PUB.mkdir(parents=True)

    # static assets (css, js, images) -> /assets
    shutil.copytree(STATIC, PUB / "assets", ignore=shutil.ignore_patterns("root"))
    root_static = STATIC / "root"
    if root_static.exists():
        for f in root_static.iterdir():
            shutil.copy(f, PUB / f.name)
    # employer logos (generated placeholders)
    logo_dir = PUB / "assets" / "img" / "employers"
    logo_dir.mkdir(parents=True, exist_ok=True)
    for e in EMP.values():
        (logo_dir / f"{e['slug']}.svg").write_text(lib.logo_svg(e["name"]), encoding="utf-8")

    pages_jobs.build_all()
    pages_content.build_all()

    # jobs.json (used by the Saved jobs page)
    index = [{"id": j["id"], "title": j["title"], "company": j["emp"]["name"], "where": where(j), "type": j["type"], "level": j["level_name"],
              "pay": sal(j, True) + " /mo", "url": j["url"], "logo": j["emp"]["logo"], "verified": j["emp"]["verified"], "remote": j["remote"],
              "ago": j["ago"], "left": j["left"]} for j in JOBS]
    (PUB / "assets" / "jobs.json").write_text(json.dumps(index, separators=(",", ":")), encoding="utf-8")

    # sitemap.xml
    urls = "".join(f"<url><loc>{lib.url(p)}</loc><lastmod>{lm}</lastmod><changefreq>{cf}</changefreq><priority>{pr}</priority></url>\n" for p, lm, cf, pr in sorted(SITEMAP, key=lambda x: (-float(x[3]), x[0])))
    (PUB / "sitemap.xml").write_text(f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{urls}</urlset>\n', encoding="utf-8")

    # robots.txt
    (PUB / "robots.txt").write_text(
        f"User-agent: *\nAllow: /\nDisallow: /thank-you/\nDisallow: /saved-jobs/\n\nSitemap: {C.SITE_URL}/sitemap.xml\n", encoding="utf-8")

    # manifest
    (PUB / "manifest.webmanifest").write_text(json.dumps({
        "name": f"{C.SITE_NAME}: {C.SITE_TAGLINE}", "short_name": C.SITE_NAME, "description": C.SITE_TAGLINE, "start_url": "/", "scope": "/",
        "display": "standalone", "background_color": "#f6f8f5", "theme_color": "#0b3d2e", "lang": "en-KE",
        "icons": [{"src": "/assets/img/logo-192.png", "sizes": "192x192", "type": "image/png"},
                  {"src": "/assets/img/logo-512.png", "sizes": "512x512", "type": "image/png"},
                  {"src": "/assets/img/logo-512.png", "sizes": "512x512", "type": "image/png", "purpose": "maskable"}]}, indent=2), encoding="utf-8")

    # Netlify headers + redirects
    (PUB / "_headers").write_text("""/*
  X-Content-Type-Options: nosniff
  X-Frame-Options: DENY
  Referrer-Policy: strict-origin-when-cross-origin
  Permissions-Policy: camera=(), microphone=(), geolocation=(), interest-cohort=()
  Strict-Transport-Security: max-age=31536000; includeSubDomains
  Content-Security-Policy: frame-ancestors 'none'

/assets/css/*
  Cache-Control: public, max-age=31536000, immutable

/assets/js/*
  Cache-Control: public, max-age=31536000, immutable

/assets/img/*
  Cache-Control: public, max-age=604800

/assets/jobs.json
  Cache-Control: public, max-age=3600

/sitemap.xml
  Content-Type: application/xml; charset=utf-8

/manifest.webmanifest
  Content-Type: application/manifest+json
""", encoding="utf-8")
    (PUB / "_redirects").write_text("""# Friendly aliases (301)
/jobs-in-kenya            /jobs/                          301
/job                      /jobs/                          301
/vacancies                /jobs/                          301
/internship               /internships/                   301
/graduate-jobs            /entry-level-jobs/              301
/entry-level              /entry-level-jobs/              301
/remote                   /remote-jobs/                   301
/work-from-home           /remote-jobs/                   301
/cv                       /cv-builder/                    301
/cover-letter             /cover-letter-generator/        301
/interview                /interview-prep/                301
/scam                     /scam-checker/                  301
/report                   /report-scam/                   301
/salaries                 /salary-guide/                  301
/blog                     /career-advice/                 301
/blog/*                   /career-advice/:splat/          301
/careers                  /career-advice/                 301
/courses                  /training/                      301
/post-a-job               /employers/post-a-job/          301
/post-job                 /employers/post-a-job/          301
/employer                 /employers/                     301
/pricing                  /employers/pricing/             301
/register                 /employers/register/            301
/kenya-jobs               /jobs/                          301
""", encoding="utf-8")

    n = sum(1 for _ in PUB.rglob("index.html"))
    print(f"Built {n} pages, {len(SITEMAP)} sitemap URLs -> {PUB}")


if __name__ == "__main__":
    main()
