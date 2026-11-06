# KaziBora - Verified Jobs, Internships & Skills in Kenya

A fast, static, SEO/SEM-optimised jobs platform for Kenya (placeholder content and images - replace at launch).
Designed & built by Tyrone John, +254 792 381 698.

## Deploy in 3 minutes

1. Create a GitHub repo and push this folder (`git init && git add . && git commit -m "KaziBora" && git push`).
2. In Netlify: **Add new site > Import from Git**, pick the repo. Settings are read from `netlify.toml`
   (build command `python3 generator/build.py`, publish directory `public`). Click **Deploy**.
3. Forms (job applications, employer registration, post-a-job, CV service, alerts, contact) are picked up by
   Netlify Forms automatically. Enable email notifications under **Site configuration > Forms**.

The repo holds only the source (under 100 files, so GitHub's web upload works). Netlify generates all 129 pages
in a few seconds on each deploy, and uses your site's address for canonicals and the sitemap automatically.

## What is included

- 49 sample verified jobs, 20 employer profiles, filters (keyword, location, category, level, type, remote, salary)
- Internship, entry-level and remote hubs; category and city landing pages (SEO)
- Employer registration, paid job posting, pricing (KSh 3,000 standard / 5,500 featured / packs), advertising packages
- CV builder, cover-letter generator, interview trainer, salary guide, scam checker, scam reporting
- CV writing service, training-provider partners, job alerts, saved jobs
- Career-advice articles, sitemap.xml, robots.txt, JSON-LD schema, Open Graph, PWA manifest, security headers

## Changing the domain, contact details, prices, IDs

Edit `generator/config.py` (site URL, phone, prices, Google Analytics / Ads / Meta Pixel IDs), then rebuild:

```bash
python3 generator/build.py https://yourdomain.co.ke
```

This regenerates `public/` including canonicals, sitemap and schema. Commit and push; Netlify redeploys.
Python 3 only, no packages to install. Sample listings live in `generator/data.py`.

## Before going live with real listings

- Set `EMIT_JOBPOSTING_SCHEMA = True` and `SHOW_SAMPLE_NOTICE = False` in `generator/config.py` once listings are real.
- Submit `https://yourdomain.co.ke/sitemap.xml` in Google Search Console.
