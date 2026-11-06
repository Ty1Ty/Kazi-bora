# KaziBora - Verified Jobs, Internships & Skills in Kenya

A fast, static, SEO/SEM-optimised jobs platform for Kenya (placeholder content and images - replace at launch).
Designed & built by Tyrone John, +254 792 381 698.

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
