"""Site-wide settings. Edit here, then run:  python3 generator/build.py   (or: python3 generator/build.py https://yourdomain.co.ke)
Everything (titles, canonicals, sitemap, schema, contact details) is regenerated from these values."""
import os
import sys
from datetime import date

SITE_NAME = "KaziBora"
SITE_TAGLINE = "Verified jobs, internships & skills in Kenya"
# No trailing slash. Change to your custom domain later (or pass it as the first argument to build.py).
SITE_URL = (sys.argv[1] if len(sys.argv) > 1 and sys.argv[1].startswith("http") else
            os.environ.get("SITE_URL") or os.environ.get("URL") or "https://kazibora.netlify.app").rstrip("/")
LOCALE = "en-KE"
TODAY = date.today()                            # build date used for lastmod / sample posting dates

# Contact details shown on the site (placeholders - change freely)
CONTACT_PHONE_DISPLAY = "+254 792 381 698"
CONTACT_PHONE_TEL = "+254792381698"
WHATSAPP_NUMBER = "254792381698"
CONTACT_EMAIL = ""     # optional; when empty no email address is shown and all enquiries go through forms/WhatsApp
CONTACT_LOCATION = "Nairobi, Kenya"
BUILDER_CREDIT = "Designed & built by Tyrone John"

# Optional marketing IDs. Leave empty and nothing loads. Fill in to switch on (a consent banner appears automatically).
GA4_ID = ""            # e.g. G-XXXXXXXXXX
GTM_ID = ""            # e.g. GTM-XXXXXXX (use instead of GA4_ID if you prefer Tag Manager)
GOOGLE_ADS_ID = ""     # e.g. AW-123456789
META_PIXEL_ID = ""
GOOGLE_SITE_VERIFICATION = ""   # Search Console meta token (optional)

# Pricing (KSh) - used across the employer pages
PRICE_STANDARD = 3000          # 30-day listing
PRICE_FEATURED = 5500          # 30-day featured listing
PRICE_STARTER_PACK = 13500     # 5 standard listings (10% off)
PRICE_GROWTH_PACK = 27000      # 10 listings, 3 featured (about 20% off)
PRICE_CV_BASIC = 1500          # CV rewrite
PRICE_CV_PRO = 3000            # CV + cover letter + LinkedIn tune-up
PRICE_CV_EXEC = 4500           # Senior/executive CV + cover letter + LinkedIn + interview coaching call
PRICE_BANNER = 15000           # homepage banner, per week
PRICE_NEWSLETTER = 8000        # job-alert newsletter sponsorship, per issue
PRICE_SOCIAL = 4000            # social-media job boost, per post
PRICE_SHORTLIST = 24000        # shortlisting service, per role

# Google rejects JobPosting markup for jobs that are not real. The sample listings are placeholders,
# so structured data is OFF by default. Set True once the listings are real, paid employer jobs.
EMIT_JOBPOSTING_SCHEMA = False

# Shows a small "demo data" ribbon + footer note. Set False when you replace the placeholder content with real listings.
SHOW_SAMPLE_NOTICE = True
