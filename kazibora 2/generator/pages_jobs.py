"""Job-related pages: home, job board hub, SEO landing pages, job detail, employers, employer tools."""
from urllib.parse import quote

import config as C
import data as D
from lib import *

J = JOBS
N_JOBS, N_VER = len(J), sum(1 for e in EMP.values() if e["verified"])
N_INT = sum(1 for j in J if j["level"] == "internship")
N_ENT = sum(1 for j in J if j["level"] == "entry")
N_REM = sum(1 for j in J if j["remote"])
NEWEST = sorted(J, key=lambda j: (j["ago"], j["title"]))
FEATURED = [j for j in NEWEST if j["featured"]]


def faq_home():
    return [(q, a.format(std=f"{C.PRICE_STANDARD:,}", feat=f"{C.PRICE_FEATURED:,}")) for q, a in D.FAQ_HOME]


def sal_range(jobs):
    jobs = [j for j in jobs if j["level"] != "internship"] or jobs
    if not jobs:
        return None
    return min(j["smin"] for j in jobs), max(j["smax"] for j in jobs)


def avg_pay(jobs):
    return round(sum((j["smin"] + j["smax"]) / 2 for j in jobs) / len(jobs) / 500) * 500 if jobs else 0


# ===================================================================== HOME
def build_home():
    cat_opts = options([(c["slug"], c["name"]) for c in CAT.values()], "Any field")
    loc_opts = options([(l["slug"], l["name"]) for l in LOC.values()], "Anywhere")
    chips = [("Internships", "/internships/"), ("Entry-level jobs", "/entry-level-jobs/"), ("Remote jobs", "/remote-jobs/"),
             ("Jobs in Nairobi", "/jobs-in-nairobi/"), ("Jobs in Mombasa", "/jobs-in-mombasa/"), ("ICT jobs", "/ict-jobs-in-kenya/"),
             ("Accounting jobs", "/finance-jobs-in-kenya/")]
    chips_html = "".join(f'<a class="chip" href="{h}">{t}</a>' for t, h in chips)
    hero = f'''<section class="hero"><div class="wrap hero-in">
<div class="hero-copy">
<p class="eyebrow">{ico("shield", "ico", 16)} Verified Kenyan opportunities</p>
<h1>Find <span class="hl">verified jobs</span>, internships &amp; skills in Kenya</h1>
<p class="lead">Search real vacancies from checked employers across all counties. Internships, entry-level roles and legitimate remote work, with free CV tools and interview prep to help you get hired.</p>
<form class="hero-search" action="/jobs/" method="get" role="search" aria-label="Search jobs">
<label class="sr" for="hq">Job title or keyword</label>
<div class="hs-field">{ico("search", "ico", 20)}<input id="hq" name="q" type="search" placeholder="Job title or skill" autocomplete="off"></div>
<label class="sr" for="hl">Location</label>
<div class="hs-field">{ico("pin", "ico", 20)}<select id="hl" name="location">{loc_opts}</select></div>
<label class="sr" for="hc">Category</label>
<div class="hs-field hs-cat">{ico("briefcase", "ico", 20)}<select id="hc" name="category">{cat_opts}</select></div>
<button class="btn btn-amber btn-lg" type="submit">Search jobs</button></form>
<p class="chips"><span>Popular:</span>{chips_html}</p>
<ul class="trust"><li>{ico("check", "ico", 16)} Free for job seekers</li><li>{ico("check", "ico", 16)} Employers checked by hand</li><li>{ico("check", "ico", 16)} One-click scam reporting</li></ul>
</div>
<div class="hero-art"><img src="/assets/img/hero.svg" width="640" height="520" alt="Illustration of a Nairobi skyline with job-seeker and employer cards" fetchpriority="high">
<div class="float-card fc1">{ico("shield", "ico", 18)}<span><b>Verified</b> employer</span></div>
<div class="float-card fc2">{ico("trend", "ico", 18)}<span><b>{N_JOBS}</b> open roles</span></div></div>
</div></section>
<section class="stats"><div class="wrap"><ul>
<li><b data-count="{N_JOBS}">{N_JOBS}</b><span>Open jobs</span></li><li><b data-count="{N_VER}">{N_VER}</b><span>Verified employers</span></li>
<li><b data-count="{N_INT}">{N_INT}</b><span>Internships</span></li><li><b data-count="{N_REM}">{N_REM}</b><span>Remote roles</span></li>
<li><b data-count="{len(LOC)}">{len(LOC)}</b><span>Towns &amp; cities covered</span></li></ul></div></section>'''

    quick = f'''<section class="section tight"><div class="wrap"><div class="quick">
<a class="q-card q-int" href="/internships/"><span class="q-ic">{ico("cap", "ico", 28)}</span><h2>Internships</h2><p>{N_INT} paid and attachment-style placements for students and fresh graduates.</p><span class="more">Browse internships {ico("arrow", "ico", 16)}</span></a>
<a class="q-card q-ent" href="/entry-level-jobs/"><span class="q-ic">{ico("trend", "ico", 28)}</span><h2>Entry-level jobs</h2><p>{N_ENT} roles asking for 0-2 years' experience, with training on the job.</p><span class="more">Start your career {ico("arrow", "ico", 16)}</span></a>
<a class="q-card q-rem" href="/remote-jobs/"><span class="q-ic">{ico("laptop", "ico", 28)}</span><h2>Remote jobs</h2><p>{N_REM} work-from-Kenya roles, screened for common remote-job scams.</p><span class="more">Work from anywhere {ico("arrow", "ico", 16)}</span></a>
<a class="q-card q-safe" href="/scam-checker/"><span class="q-ic">{ico("shield", "ico", 28)}</span><h2>Scam checker</h2><p>Answer a few questions to see if a job offer looks safe or suspicious.</p><span class="more">Check an offer {ico("arrow", "ico", 16)}</span></a>
</div></div></section>'''

    featured = f'''<section class="section"><div class="wrap"><div class="sec-head"><div><p class="kicker">Hand-picked</p><h2 class="sec-title">Featured jobs</h2></div><a class="more-link" href="/jobs/">View all jobs {ico("arrow", "ico", 16)}</a></div>
{job_list(FEATURED[:6])}</div></section>'''

    cats = "".join(
        f'<a class="cat-card" href="/{c["slug"]}-jobs-in-kenya/"><span class="cat-ic" aria-hidden="true">{c["emoji"]}</span><span class="cat-t">{c["name"]}</span>'
        f'<span class="cat-n">{plural(sum(1 for j in J if j["cat"]["slug"] == c["slug"]), "job")}</span></a>' for c in CAT.values())
    cat_section = f'<section class="section alt" id="categories"><div class="wrap"><div class="sec-head"><div><p class="kicker">Find your field</p><h2 class="sec-title">Browse jobs by category</h2></div></div><div class="cat-grid">{cats}</div></div></section>'

    why_items = [
        ("shield", "Verified employers only", "We check registration details, contacts and that the vacancy is real before a job goes live."),
        ("lock", "No fees, ever", "Employers promise in writing never to charge candidates. Report any advert that asks for money."),
        ("cap", "Built for first-time job seekers", "Dedicated internship and entry-level pages, plus guides for graduates with no experience."),
        ("laptop", "Remote work, screened", "Kenya-friendly remote roles checked against the most common remote-job scam patterns."),
        ("file", "Free CV and cover letter tools", "Build a clean, recruiter-friendly CV and a tailored cover letter in minutes."),
        ("mic", "Interview prep that works", f"{len(D.QUESTIONS)} real interview questions with coaching tips, in practice mode."),
    ]
    why = "".join(f'<div class="why-card"><span class="why-ic">{ico(i, "ico", 24)}</span><h3>{t}</h3><p>{p}</p></div>' for i, t, p in why_items)
    why_section = f'''<section class="section"><div class="wrap"><div class="sec-head center"><div><p class="kicker">Why KaziBora</p><h2 class="sec-title">A safer, smarter way to find work in Kenya</h2>
<p class="sec-sub">Job scams hurt. We built KaziBora so every opportunity you see has been looked at by a real person first.</p></div></div>
<div class="why-grid">{why}</div><p class="center-link"><a class="btn btn-outline" href="/verified-jobs/">See how verification works</a></p></div></section>'''

    latest = f'''<section class="section alt"><div class="wrap"><div class="sec-head"><div><p class="kicker">Just added</p><h2 class="sec-title">Latest jobs in Kenya</h2></div><a class="more-link" href="/jobs/">See all {N_JOBS} jobs {ico("arrow", "ico", 16)}</a></div>
{job_list(NEWEST[:8])}</div></section>'''

    locs = "".join(f'<a class="loc-card" href="/jobs-in-{l["slug"]}/"><span>{ico("pin", "ico", 18)} {l["name"]}</span><b>{sum(1 for j in J if j["loc"]["slug"] == l["slug"])} jobs</b></a>' for l in LOC.values())
    loc_section = f'<section class="section"><div class="wrap"><div class="sec-head"><div><p class="kicker">Near you</p><h2 class="sec-title">Jobs by city and county</h2></div></div><div class="loc-grid">{locs}</div></div></section>'

    tools = [("file", "Free CV builder", "Pick a template, fill in your details and print a polished CV.", "/cv-builder/"),
             ("mail", "Cover letter generator", "Create a tailored cover letter in three tones.", "/cover-letter-generator/"),
             ("mic", "Interview trainer", f"Practise {len(D.QUESTIONS)} questions with expert tips.", "/interview-prep/"),
             ("trend", "Salary guide", "See typical monthly pay by field and level in Kenya.", "/salary-guide/")]
    tool_html = "".join(f'<a class="tool-card" href="{h}"><span class="why-ic">{ico(i, "ico", 24)}</span><h3>{t}</h3><p>{p}</p><span class="more">Try it free {ico("arrow", "ico", 16)}</span></a>' for i, t, p, h in tools)
    tool_section = f'<section class="section alt"><div class="wrap"><div class="sec-head"><div><p class="kicker">Career toolkit</p><h2 class="sec-title">Everything you need to get hired</h2></div><a class="more-link" href="/career-advice/">Read career advice {ico("arrow", "ico", 16)}</a></div><div class="tool-grid">{tool_html}</div></div></section>'

    plans = f'''<section class="section employers-band"><div class="wrap"><div class="eb-grid"><div class="eb-copy"><p class="kicker light">For employers</p><h2>Hire verified talent across Kenya</h2>
<p>Reach job seekers who trust KaziBora. Post a job from <b>{ksh(C.PRICE_STANDARD)}</b>, upgrade to a featured listing for about three times the visibility, or save with a package.</p>
<ul class="ticks"><li>{ico("check", "ico", 18)} Verified badge builds candidate trust</li><li>{ico("check", "ico", 18)} Applications delivered to your inbox</li><li>{ico("check", "ico", 18)} Optional shortlisting and recruitment advertising</li></ul>
<p><a class="btn btn-amber btn-lg" href="/employers/post-a-job/">Post a job</a> <a class="btn btn-ghost-light btn-lg" href="/employers/pricing/">See pricing</a></p></div>
<div class="eb-plans"><div class="mini-plan"><span>Standard listing</span><b>{ksh(C.PRICE_STANDARD)}</b><small>30 days</small></div>
<div class="mini-plan hot"><span>Featured listing</span><b>{ksh(C.PRICE_FEATURED)}</b><small>30 days, top placement</small></div>
<div class="mini-plan"><span>Starter pack</span><b>{ksh(C.PRICE_STARTER_PACK)}</b><small>5 listings</small></div>
<div class="mini-plan"><span>Growth pack</span><b>{ksh(C.PRICE_GROWTH_PACK)}</b><small>10 listings, 3 featured</small></div></div></div></div></section>'''

    courses = "".join(f'<a class="course-card" href="/training/"><span class="course-ic">{c[6]}</span><h3>{esc(c[1])}</h3><p class="prov">{esc(c[0])}</p><p>{esc(c[5])}</p><p class="course-meta"><span>{c[2]}</span><span>{ksh(c[3])}</span></p></a>' for c in D.COURSES[:3])
    train = f'<section class="section"><div class="wrap"><div class="sec-head"><div><p class="kicker">Upskill</p><h2 class="sec-title">Training that employers ask for</h2></div><a class="more-link" href="/training/">All courses {ico("arrow", "ico", 16)}</a></div><div class="course-grid">{courses}</div></div></section>'

    arts = "".join(article_card(a) for a in ARTICLES[:3])
    art_section = f'<section class="section alt"><div class="wrap"><div class="sec-head"><div><p class="kicker">Career guidance</p><h2 class="sec-title">Advice from the KaziBora desk</h2></div><a class="more-link" href="/career-advice/">All articles {ico("arrow", "ico", 16)}</a></div><div class="art-grid">{arts}</div></div></section>'

    alert = alert_band()
    faq = faq_home()
    body = hero + quick + featured + cat_section + why_section + latest + loc_section + tool_section + plans + train + art_section + faq_html(faq) + alert
    page("/", f"{C.SITE_NAME}: Verified Jobs, Internships & Careers in Kenya", f"Find verified jobs in Kenya: internships, entry-level and remote roles from checked employers. Free CV builder, cover letters and interview prep. Never pay to apply.",
         body, active="", schema=[org_schema(), website_schema(), faq_schema(faq)], prio="1.0", freq="daily", main_cls="home")


def article_card(a):
    return (f'<a class="art-card" href="/career-advice/{a["slug"]}/"><img src="/assets/img/articles/{a["slug"]}.svg" width="640" height="360" loading="lazy" alt="">'
            f'<div><span class="tag">{esc(a["tag"])}</span><h3>{esc(a["title"])}</h3><p>{esc(a["desc"])}</p><span class="meta">{a["read"]} min read</span></div></a>')


def alert_band():
    return f'''<section class="cta-band alert-band" id="alerts"><div class="wrap cta-in"><div><h2>Get new verified jobs on WhatsApp or email</h2><p>Tell us what you are looking for. We send only matching, verified opportunities. Unsubscribe any time.</p></div>
<form class="inline-form" name="job-alert" method="POST" action="/thank-you/" data-netlify="true" netlify-honeypot="bot-field"><input type="hidden" name="form-name" value="job-alert">
<p class="hp" aria-hidden="true"><label>Leave empty <input name="bot-field" tabindex="-1"></label></p>
<label class="sr" for="al-c">Contact</label><input id="al-c" name="contact" type="text" placeholder="Email or WhatsApp number" required>
<label class="sr" for="al-i">Interest</label><select id="al-i" name="interest">{options([("any", "Any job")] + [(c["slug"], c["name"]) for c in CAT.values()] + [("internships", "Internships"), ("remote", "Remote jobs")])}</select>
<button class="btn btn-amber" type="submit">Create alert</button></form></div></section>'''


# ===================================================================== JOB BOARD
def filter_panel():
    cats = options([(c["slug"], c["name"]) for c in CAT.values()], "All categories")
    locs = options([(l["slug"], l["name"]) for l in LOC.values()], "All locations")
    types = options([(t, t) for t in ("Full-time", "Part-time", "Contract", "Internship")], "All job types")
    lv = "".join(f'<label class="chk"><input type="checkbox" name="level" value="{k}"> {v}</label>' for k, v in D.LEVELS.items())
    return f'''<aside class="filters" aria-label="Job filters"><div class="f-head"><h2>Filters</h2><button class="link-btn" type="button" data-reset>Reset all</button></div>
<div class="f-group"><label for="f-q">Keyword</label><div class="hs-field">{ico("search", "ico", 18)}<input id="f-q" name="q" type="search" placeholder="Title, skill or company" autocomplete="off"></div></div>
<div class="f-group"><label for="f-cat">Category</label><select id="f-cat" name="category">{cats}</select></div>
<div class="f-group"><label for="f-loc">Location</label><select id="f-loc" name="location">{locs}</select></div>
<div class="f-group"><label for="f-type">Job type</label><select id="f-type" name="type">{types}</select></div>
<fieldset class="f-group"><legend>Experience level</legend>{lv}</fieldset>
<div class="f-group"><label for="f-sal">Minimum monthly pay</label><select id="f-sal" name="salary">{options([("30000", "KSh 30,000+"), ("50000", "KSh 50,000+"), ("80000", "KSh 80,000+"), ("120000", "KSh 120,000+")], "Any pay")}</select></div>
<label class="chk"><input type="checkbox" name="remote" value="1"> Remote only</label>
<label class="chk"><input type="checkbox" name="verified" value="1"> Verified employers only</label>
<button class="btn btn-primary filters-apply" type="button" data-close-filters>Show results</button></aside>'''


def build_jobs_hub():
    ordered = sorted(J, key=lambda j: (not j["featured"], j["ago"]))
    body = f'''{hero_small("Jobs in Kenya", f"Search {N_JOBS} verified jobs, internships and remote roles. Filter by category, location, level and pay.", [("Home", "/"), ("Jobs", "/jobs/")])}
<section class="section tight"><div class="wrap jobs-layout">
<button class="btn btn-outline filters-open" type="button" data-open-filters>{ico("search", "ico", 18)} Filters</button>
{filter_panel()}
<div class="results" id="results"><div class="res-bar"><p id="res-count" aria-live="polite"><b>{N_JOBS}</b> jobs found</p>
<label class="sr" for="sort">Sort jobs</label><select id="sort" name="sort"><option value="relevance">Featured first</option><option value="newest">Newest</option><option value="closing">Closing soon</option><option value="pay">Highest pay</option></select></div>
<div id="active-filters" class="active-filters"></div>
{job_list(ordered)}
<p class="empty" id="no-results" hidden>No jobs match those filters. Try removing a filter, or <a href="#alerts">create a job alert</a> and we will message you when a match appears.</p>
<p class="center-link"><button class="btn btn-outline" id="more-btn" type="button" hidden>Show more jobs</button></p></div>
</div></section>
{alert_band()}'''
    page("/jobs/", "Jobs in Kenya: Search Verified Vacancies | KaziBora", f"Search {N_JOBS} verified jobs in Kenya. Filter by category, county, experience level, pay and remote. Internships, entry-level and remote roles from checked employers.",
         body, active="jobs", schema=[itemlist_schema(ordered)], crumbs=[("Home", "/"), ("Jobs", "/jobs/")], prio="0.95", freq="daily", main_cls="board")


def landing(path, title, desc, h1, lead, jobs, crumbs, intro, tips=None, faq=None, related=None, active="jobs", prio="0.8", cta=None):
    tips_html = ""
    if tips:
        tips_html = '<aside class="tip-card"><h2>Quick tips</h2><ul class="ticks">' + "".join(f"<li>{ico('check', 'ico', 18)} {t}</li>" for t in tips) + "</ul></aside>"
    rel_html = ""
    if related:
        rel_html = '<section class="section tight"><div class="wrap"><h2 class="sec-title sm">Explore more</h2><div class="chips big">' + "".join(f'<a class="chip" href="{h}">{t}</a>' for t, h in related) + "</div></div></section>"
    rng = sal_range(jobs)
    stat = f'<p class="stat-line">{plural(len(jobs), "open job")} &middot; typical pay {ksh(rng[0])} to {ksh(rng[1])} a month</p>' if rng else ""
    body = f'''{hero_small(h1, lead, crumbs, stat)}
<section class="section tight"><div class="wrap two-col"><div class="main-col">{job_list(jobs)}
<div class="seo-text">{intro}</div></div><div class="side-col">{tips_html}
<div class="side-card"><h2>Never miss a job</h2><p>Get verified matches by email or WhatsApp.</p><a class="btn btn-primary" href="/job-alerts/">Create a job alert</a></div>
<div class="side-card"><h2>Polish your application</h2><p>Build a CV and cover letter in minutes.</p><a class="btn btn-outline" href="/cv-builder/">Free CV builder</a></div></div></div></section>
{faq_html(faq) if faq else ""}{rel_html}{cta or ""}'''
    schemas = [itemlist_schema(jobs)] if jobs else []
    if faq:
        schemas.append(faq_schema(faq))
    page(path, title, desc, body, active=active, schema=schemas, crumbs=crumbs, prio=prio, freq="daily")


def build_landings():
    cat_links = [(f'{c["name"]} jobs', f'/{c["slug"]}-jobs-in-kenya/') for c in CAT.values()]
    loc_links = [(f'Jobs in {l["name"]}', f'/jobs-in-{l["slug"]}/') for l in LOC.values()]
    hub = [("Internships", "/internships/"), ("Entry-level jobs", "/entry-level-jobs/"), ("Remote jobs", "/remote-jobs/")]

    # internships
    ints = sorted([j for j in J if j["level"] == "internship"], key=lambda j: j["ago"])
    faq_i = [("Are KaziBora internships paid?", "Most internships on KaziBora state a monthly stipend. Each listing shows the pay range, and employers must never charge you to apply or to take part."),
             ("Can I apply for an internship before I graduate?", "Yes. Many internships accept students in their final year or on long breaks. Check the requirements on each listing."),
             ("How do I stand out with no work experience?", "Highlight class projects, volunteering, short courses and leadership roles. Use our CV builder and cover letter generator to present them clearly.")]
    landing("/internships/", "Internships in Kenya for Students & Graduates (Paid) | KaziBora",
            f"Find {len(ints)} verified internships in Kenya for students and fresh graduates. Paid placements in ICT, finance, engineering, hospitality, NGOs and more.",
            "Internships in Kenya", "Verified internships and attachments for students and recent graduates, with stipends shown on every listing.", ints,
            [("Home", "/"), ("Internships", "/internships/")],
            "<h2>Find an internship in Kenya that builds your career</h2><p>An internship is the quickest way to turn classroom knowledge into experience employers trust. KaziBora lists internships from verified Kenyan employers in Nairobi, Mombasa, Kisumu, Nakuru, Eldoret and beyond, across ICT, finance, engineering, hospitality, health, NGOs and creative work.</p><p>Every listing is checked, shows the stipend range and carries our no-fee promise. If an internship ever asks you to pay for placement, training or a uniform, <a href=\"/report-scam/\">report it</a> and we will investigate.</p>"
            "<h3>How to apply for an internship</h3><ol><li>Build a one-page CV with our <a href=\"/cv-builder/\">CV builder</a>.</li><li>Write a short, specific cover letter with the <a href=\"/cover-letter-generator/\">cover letter generator</a>.</li><li>Apply early: many internships close in two to three weeks.</li><li>Practise common questions in the <a href=\"/interview-prep/\">interview trainer</a>.</li></ol>",
            ["Apply to five or more internships, not one", "Mention your course units and projects that match the role", "Ask about the stipend and the supervisor in the interview", "Never pay a placement or &ldquo;registration&rdquo; fee"],
            faq_i, [("Entry-level jobs", "/entry-level-jobs/"), ("Remote jobs", "/remote-jobs/"), ("Read: how to land an internship", "/career-advice/internships-in-kenya-how-to-find-and-win-one/")] + loc_links[:4], prio="0.9")

    ents = sorted([j for j in J if j["level"] == "entry"], key=lambda j: j["ago"])
    faq_e = [("Can I get a job in Kenya with no experience?", "Yes. Many employers hire graduates and school leavers for roles that include on-the-job training. Look for titles with &ldquo;assistant&rdquo;, &ldquo;trainee&rdquo;, &ldquo;officer&rdquo; or &ldquo;junior&rdquo;.".replace("&ldquo;", "“").replace("&rdquo;", "”")),
             ("What is a typical entry-level salary in Kenya?", f"On KaziBora, entry-level roles typically pay between {ksh(min(j['smin'] for j in ents))} and {ksh(max(j['smax'] for j in ents))} a month, depending on the field and location."),
             ("Do entry-level employers charge fees?", "No. A genuine employer never charges for applications, interviews, training or uniforms.")]
    landing("/entry-level-jobs/", "Entry-Level Jobs in Kenya: No Experience Required | KaziBora",
            f"Browse {len(ents)} verified entry-level jobs in Kenya for fresh graduates and first-time job seekers. Trainee, assistant and junior roles with on-the-job training.",
            "Entry-level jobs in Kenya", "Verified roles for fresh graduates and first-time job seekers, from trainees to junior officers.", ents,
            [("Home", "/"), ("Entry-level jobs", "/entry-level-jobs/")],
            "<h2>Start your career with a verified entry-level job</h2><p>Your first job sets the pace for your career. These entry-level roles ask for little or no experience and come from employers who have passed KaziBora verification, so you can apply with confidence.</p><p>Not sure where to begin? Read our guide on <a href=\"/career-advice/entry-level-jobs-in-kenya-no-experience/\">entry-level jobs in Kenya with no experience</a>, then add a course from our <a href=\"/training/\">training partners</a> to strengthen your CV.</p>",
            ["Apply even if you meet most requirements, not all", "Show projects, attachments and volunteering", "Learn one in-demand tool: Excel, Canva or QuickBooks", "Prepare for the question &ldquo;Tell us about yourself&rdquo;"],
            faq_e, [("Internships", "/internships/"), ("Training & courses", "/training/"), ("Interview prep", "/interview-prep/")] + loc_links[:4], prio="0.9")

    rem = sorted([j for j in J if j["remote"]], key=lambda j: j["ago"])
    faq_r = [("Are remote jobs on KaziBora real?", "Remote roles go through the same verification as other jobs plus extra checks for common remote-job scams: unpaid &ldquo;training&rdquo;, equipment fees and fake cheque schemes.".replace("&ldquo;", "“").replace("&rdquo;", "”")),
             ("Can I work remotely from anywhere in Kenya?", "Yes. These roles are open to people based in Kenya with a reliable laptop, internet and backup power. International remote jobs will be added as the platform grows."),
             ("How will I be paid?", "Each listing shows the pay range. Ask the employer how and when you will be paid (M-Pesa, bank transfer or international platforms) and get it in writing before you start.")]
    landing("/remote-jobs/", "Remote Jobs in Kenya: Work From Home Vacancies | KaziBora",
            f"Find {len(rem)} verified remote jobs for Kenyans: customer support, virtual assistants, developers, writers and more. Screened for scams.",
            "Remote jobs for Kenyans", "Work from home or anywhere in Kenya with employers we have screened for remote-job scams.", rem,
            [("Home", "/"), ("Remote jobs", "/remote-jobs/")],
            "<h2>Legitimate remote work from Kenya</h2><p>Remote work can open doors to local and international employers, but it is also where scammers hide. Every remote job on KaziBora is checked for a real employer, a real role and a no-fee promise. We look especially for red flags such as paid &ldquo;training&rdquo;, equipment deposits and interviews held only over chat apps.</p><p>We are starting with Kenya-friendly remote roles and will add more international remote opportunities as the platform grows. Read our guide to <a href=\"/career-advice/remote-jobs-for-kenyans-legitimate-ways-to-start/\">legitimate ways to start remote work</a>.</p>",
            ["Test your power backup and internet before interviews", "Build a portfolio or work samples", "Never buy equipment for an employer before a signed contract", "Use our scam checker on any offer that feels off"],
            faq_r, [("Internships", "/internships/"), ("Entry-level jobs", "/entry-level-jobs/"), ("Scam checker", "/scam-checker/")] + cat_links[:4], active="jobs", prio="0.9")

    # categories
    for c in CAT.values():
        jobs = sorted([j for j in J if j["cat"]["slug"] == c["slug"]], key=lambda j: (not j["featured"], j["ago"]))
        rng = sal_range(jobs)
        pay = f" Typical monthly pay on KaziBora runs from {ksh(rng[0])} to {ksh(rng[1])}." if rng else ""
        intern = sum(1 for j in jobs if j["level"] == "internship")
        faq_c = [(f"How do I find {c['name'].lower()} jobs in Kenya?", f"Use the filters on this page to narrow {c['name'].lower()} vacancies by county, level and pay, then create a job alert so new verified roles reach you first."),
                 (f"Are there internships or entry-level {c['name'].lower()} jobs?", f"Yes. This category currently has {plural(intern, 'internship')} and {plural(sum(1 for j in jobs if j['level'] == 'entry'), 'entry-level role')}, all from verified employers.")]
        landing(f"/{c['slug']}-jobs-in-kenya/", f"{c['name']} Jobs in Kenya: Verified Vacancies | KaziBora",
                f"Find {len(jobs)} verified {c['name'].lower()} jobs in Kenya, from internships to senior roles. Apply free, no fees, employers checked.",
                f"{c['name']} jobs in Kenya", c["desc"], jobs, [("Home", "/"), ("Jobs", "/jobs/"), (c["name"], f"/{c['slug']}-jobs-in-kenya/")],
                f"<h2>{c['name']} jobs across Kenya</h2><p>{c['desc']}{pay} Browse the latest verified vacancies, or filter the full <a href=\"/jobs/?category={c['slug']}\">job board</a> by location and level.</p><p>Applying is always free. If an employer asks you to pay, <a href=\"/report-scam/\">report the advert</a>.</p>",
                None, faq_c, [(t, h) for t, h in cat_links if f"/{c['slug']}-" not in h][:6] + hub, prio="0.8")

    # locations
    for l in LOC.values():
        jobs = sorted([j for j in J if j["loc"]["slug"] == l["slug"]], key=lambda j: (not j["featured"], j["ago"]))
        top = sorted({j["cat"]["name"] for j in jobs})[:4]
        faq_l = [(f"What jobs are available in {l['name']}?", f"{l['name']} currently has {plural(len(jobs), 'verified job')} on KaziBora, including roles in {', '.join(top)}."),
                 (f"Are there remote or internship jobs for {l['name']}?", "Yes. Use the Remote and Experience level filters on the job board to see internships, entry-level and remote roles that suit you.")]
        landing(f"/jobs-in-{l['slug']}/", f"Jobs in {l['name']}, Kenya: Latest Verified Vacancies | KaziBora",
                f"Find {len(jobs)} verified jobs in {l['name']}, {l['county']}. Internships, entry-level and professional roles from checked employers. Apply free.",
                f"Jobs in {l['name']}", l["desc"], jobs, [("Home", "/"), ("Jobs", "/jobs/"), (f"Jobs in {l['name']}", f"/jobs-in-{l['slug']}/")],
                f"<h2>Working in {l['name']}</h2><p>{l['desc']} Browse the latest verified vacancies in {l['name']} and {l['county']}, then use our <a href=\"/salary-guide/\">salary guide</a> to know what to expect.</p>"
                f"<p>Looking for something different? Try <a href=\"/remote-jobs/\">remote jobs</a> that can be done from {l['name']} or other towns.</p>",
                None, faq_l, [(t, h) for t, h in loc_links if f"-{l['slug']}/" not in h][:5] + hub, prio="0.8")


# ===================================================================== JOB DETAIL
def build_job_pages():
    for j in J:
        e, c, l = j["emp"], j["cat"], j["loc"]
        share_txt = quote(f"{j['title']} at {e['name']} ({where(j)}) on KaziBora: {url(j['url'])}")
        related = [x for x in sorted(J, key=lambda x: x["ago"]) if x["cat"]["slug"] == c["slug"] and x["id"] != j["id"]][:3]
        if len(related) < 3:
            related += [x for x in NEWEST if x["id"] != j["id"] and x not in related][: 3 - len(related)]
        tags = [f'<span class="tag lvl-{j["level"]}">{j["level_name"]}</span>', f'<span class="tag">{j["type"]}</span>']
        if j["remote"]:
            tags.append('<span class="tag t-remote">Remote</span>')
        if j["featured"]:
            tags.append('<span class="tag t-feat">Featured</span>')
        if j["urgent"]:
            tags.append('<span class="tag t-urgent">Urgent</span>')
        form_fields = (field("Full name", "name", req=True, ph="e.g. Wanjiru Kamau") + field("Email address", "email", "email", True, "you@example.com")
                       + field("Phone / WhatsApp", "phone", "tel", True, "07XX XXX XXX")
                       + field("Your CV (PDF or Word)", "cv", "file", False, extra='accept=".pdf,.doc,.docx"', help_="Max 8MB. No CV yet? Use our free CV builder.")
                       + field("Short cover note", "note", "textarea", False, "Why are you a good fit for this role?")
                       + f'<input type="hidden" name="job_title" value="{esc(j["title"])}"><input type="hidden" name="job_url" value="{url(j["url"])}"><input type="hidden" name="employer" value="{esc(e["name"])}">'
                       + '<label class="chk"><input type="checkbox" name="consent" required> I agree to KaziBora sharing my application with this employer.</label>')
        apply = form("job-application", form_fields, "Submit application", "Free to apply. KaziBora and verified employers never charge applicants.", "apply-form", "multipart/form-data")
        overview = [("Employer", f'<a href="{e["url"]}">{esc(e["name"])}</a>'), ("Location", esc(where(j))), ("Job type", j["type"]), ("Experience", j["level_name"]),
                    ("Pay", esc(sal(j))), ("Category", f'<a href="/{c["slug"]}-jobs-in-kenya/">{c["name"]}</a>'),
                    ("Posted", f'<span data-posted-long data-ago="{j["ago"]}">{fmt_date(j["posted"])}</span>'), ("Deadline", f'<span data-closes-long data-left="{j["left"]}">{fmt_date(j["deadline"])}</span>')]
        ov = "".join(f"<div><dt>{k}</dt><dd>{v}</dd></div>" for k, v in overview)
        body = f'''<section class="job-head"><div class="wrap">{breadcrumbs_html([("Home", "/"), ("Jobs", "/jobs/"), (c["name"], f'/{c["slug"]}-jobs-in-kenya/'), (j["title"], j["url"])])}
<div class="jh-in"><img class="jh-logo" src="{e["logo"]}" width="72" height="72" alt="{esc(e["name"])} logo (placeholder)">
<div><h1>{esc(j["title"])}</h1><p class="jh-co"><a href="{e["url"]}">{esc(e["name"])}</a> {verified_badge(e)}</p>
<ul class="job-meta big"><li>{ico("pin", "ico", 18)} {esc(where(j))}</li><li>{ico("briefcase", "ico", 18)} {j["type"]}</li><li>{ico("trend", "ico", 18)} {esc(sal(j))}</li><li>{ico("calendar", "ico", 18)} Closes <span data-closes-long data-left="{j["left"]}">{fmt_date(j["deadline"])}</span></li></ul>
<p class="job-tags">{"".join(tags)}</p></div>
<div class="jh-actions"><a class="btn btn-amber btn-lg" href="#apply">Apply now</a><button type="button" class="btn btn-outline save-btn" data-save="{j["id"]}" aria-pressed="false">{ico("heart", "ico", 18)} <span>Save job</span></button></div></div></div></section>
<section class="section tight"><div class="wrap job-layout"><article class="job-body">
<div class="safe-box">{ico("shield", "ico", 22)}<p><b>Verified listing.</b> We checked this employer's details and confirmed the vacancy. Applying is free: never pay to be considered for a job. <a href="/report-scam/?job={j["slug"]}">Report this job</a></p></div>
<h2>About the role</h2><p>{esc(e["name"])} is hiring a <strong>{esc(j["title"])}</strong> to join its team{"" if j["remote"] else " in " + esc(l["name"])}{" on a remote basis, open to candidates in Kenya" if j["remote"] else ""}. {esc(e["about"])}</p>
<p>This is a {j["level_name"].lower()}, {j["type"].lower()} position in {c["name"].lower()}. The right person will grow quickly with support from experienced colleagues.</p>
<h2>Key responsibilities</h2><ul>{"".join(f"<li>{esc(r)}</li>" for r in j["resp"])}</ul>
<h2>Requirements</h2><ul>{"".join(f"<li>{esc(r)}</li>" for r in j["reqs"])}</ul>
<h2>What you will get</h2><ul>{"".join(f"<li>{esc(b)}</li>" for b in j["bens"])}</ul>
<h2>How to apply</h2><p>Complete the application form on this page before <strong data-closes-long data-left="{j["left"]}">{fmt_date(j["deadline"])}</strong>. Shortlisted candidates will be contacted by phone or email. You will <strong>never</strong> be asked to pay any fee at any stage of this recruitment.</p>
<div class="share"><span>Share this job:</span><a class="btn btn-sm btn-outline" href="https://wa.me/?text={share_txt}" target="_blank" rel="noopener">{ico("chat", "ico", 16)} WhatsApp</a>
<a class="btn btn-sm btn-outline" href="https://www.linkedin.com/sharing/share-offsite/?url={quote(url(j["url"]))}" target="_blank" rel="noopener">LinkedIn</a>
<a class="btn btn-sm btn-outline" href="https://twitter.com/intent/tweet?text={share_txt}" target="_blank" rel="noopener">X</a>
<button class="btn btn-sm btn-outline" type="button" data-copy="{url(j["url"])}">{ico("copy", "ico", 16)} Copy link</button></div>
{"<p class='sample-inline'>Demo listing: this vacancy is placeholder content for design and testing.</p>" if C.SHOW_SAMPLE_NOTICE else ""}
</article>
<aside class="job-side-col"><div class="side-card"><h2>Job overview</h2><dl class="overview">{ov}</dl></div>
<div class="side-card apply-card" id="apply"><h2>Apply for this job</h2>{apply}</div>
<div class="side-card"><h2>About {esc(e["name"])}</h2><p>{esc(e["about"])}</p><p class="mini">{esc(e["industry"])} &middot; {esc(e["size"])} &middot; {esc(LOC[e["loc"]]["name"])}</p><a class="btn btn-outline btn-sm" href="{e["url"]}">View company profile</a></div>
<div class="side-card"><h2>Prepare to stand out</h2><ul class="link-list"><li><a href="/cv-builder/">Build your CV</a></li><li><a href="/cover-letter-generator/">Write a cover letter</a></li><li><a href="/interview-prep/">Practise interview questions</a></li></ul></div></aside></div></section>
<section class="section alt"><div class="wrap"><h2 class="sec-title">Similar jobs you may like</h2>{job_list(related)}</div></section>'''
        desc = f"{j['title']} at {e['name']} in {where(j)}. {j['type']}, {j['level_name'].lower()}, {sal(j, True)}/month. Apply before {fmt_date(j['deadline'])}. Verified Kenyan job."
        schemas = [jobposting_schema(j)] if C.EMIT_JOBPOSTING_SCHEMA else []
        page(j["url"], f"{j['title']} at {e['name']}, {where(j)} | KaziBora", desc[:300], body, active="jobs", schema=schemas,
             crumbs=[("Home", "/"), ("Jobs", "/jobs/"), (c["name"], f'/{c["slug"]}-jobs-in-kenya/'), (j["title"], j["url"])], prio="0.7", freq="weekly", og_type="article")


# ===================================================================== EMPLOYERS
def plan_cards():
    def card(name, price, unit, feats, hot=False, cta="Choose plan", plan=""):
        li = "".join(f"<li>{ico('check', 'ico', 18)} {f}</li>" for f in feats)
        return (f'<div class="plan{" hot" if hot else ""}">{"<span class=ribbon>Most popular</span>" if hot else ""}<h3>{name}</h3><p class="price"><b>{ksh(price)}</b> <span>{unit}</span></p>'
                f'<ul class="ticks">{li}</ul><a class="btn {"btn-amber" if hot else "btn-primary"}" href="/employers/post-a-job/?plan={plan}">{cta}</a></div>')
    return '<div class="plan-grid">' + (
        card("Standard listing", C.PRICE_STANDARD, "/ 30 days", ["1 job live for 30 days", "Verified badge", "Applications by email", "Shared on our job alerts"], plan="standard")
        + card("Featured listing", C.PRICE_FEATURED, "/ 30 days", ["Top-of-page placement", "Homepage featured slot", "About 3x the visibility", "Shared on social and WhatsApp"], True, "Feature my job", "featured")
        + card("Starter pack", C.PRICE_STARTER_PACK, "/ 5 listings", ["5 standard listings, 10% off", "Use within 6 months", "Company profile page", "Priority review"], plan="starter")
        + card("Growth pack", C.PRICE_GROWTH_PACK, "/ 10 listings", ["10 listings, 3 featured", "Use within 12 months", "Newsletter mention", "Account manager"], plan="growth")) + "</div>"


def build_employer_pages():
    steps = [("1", "Register", "Create your employer profile with your business details."), ("2", "Post & verify", "Submit your vacancy. We verify the business and the role, usually within one working day."),
             ("3", "Pay securely", "Pay by M-Pesa, bank transfer or invoice once your listing is approved."), ("4", "Hire", "Receive applications in your inbox and shortlist the best candidates.")]
    steps_html = "".join(f'<div class="step"><span class="step-n">{n}</span><h3>{t}</h3><p>{p}</p></div>' for n, t, p in steps)
    faq = [("How much does it cost to post a job in Kenya on KaziBora?", f"A standard 30-day listing costs {ksh(C.PRICE_STANDARD)} and a featured listing costs {ksh(C.PRICE_FEATURED)}. Packages bring the cost per listing down."),
           ("How does verification work?", "We confirm your business identity, check the vacancy is genuine and ask you to commit to a no-fee hiring process. Most employers are approved within one working day."),
           ("How do I pay?", "After your listing is approved we send an M-Pesa request, bank details or an invoice. Your job goes live once payment is confirmed."),
           ("Can you shortlist candidates for me?", f"Yes. Our shortlisting service ({ksh(C.PRICE_SHORTLIST)} per role) advertises, screens and delivers a shortlist of matched candidates."),
           ("What happens if my listing does not get applicants?", "Tell us within 7 days and we will promote it through our alerts and social channels at no extra cost.")]
    body = f'''<section class="hero hero-emp"><div class="wrap hero-in"><div class="hero-copy"><p class="eyebrow">{ico("building", "ico", 16)} For employers</p><h1>Hire <span class="hl">verified talent</span> in Kenya</h1>
<p class="lead">Post jobs where candidates feel safe. KaziBora attracts serious job seekers with verified listings, internship and entry-level pipelines and legitimate remote talent.</p>
<p><a class="btn btn-amber btn-lg" href="/employers/post-a-job/">Post a job from {ksh(C.PRICE_STANDARD)}</a> <a class="btn btn-ghost-light btn-lg" href="/employers/register/">Register as an employer</a></p>
<ul class="trust"><li>{ico("check", "ico", 16)} Live in about a day</li><li>{ico("check", "ico", 16)} Applications to your inbox</li><li>{ico("check", "ico", 16)} No contract</li></ul></div>
<div class="hero-art"><img src="/assets/img/employers-hero.svg" width="640" height="520" alt="Employer dashboard illustration with applicants and a verified badge"></div></div></section>
<section class="section"><div class="wrap"><div class="sec-head center"><div><p class="kicker">How it works</p><h2 class="sec-title">From vacancy to shortlist in four steps</h2></div></div><div class="steps">{steps_html}</div></div></section>
<section class="section alt"><div class="wrap"><div class="sec-head center"><div><p class="kicker">Pricing</p><h2 class="sec-title">Simple, transparent job posting prices</h2><p class="sec-sub">Prices in Kenya shillings. No hidden fees, no subscription.</p></div></div>{plan_cards()}
<p class="center-link"><a class="btn btn-outline" href="/employers/pricing/">Compare all plans and services</a></p></div></section>
<section class="section"><div class="wrap"><div class="sec-head center"><div><p class="kicker">Why employers choose us</p><h2 class="sec-title">Quality over volume</h2></div></div><div class="why-grid">
<div class="why-card"><span class="why-ic">{ico("shield", "ico", 24)}</span><h3>Trusted by candidates</h3><p>The Verified badge tells job seekers your vacancy is real, so you get better applications.</p></div>
<div class="why-card"><span class="why-ic">{ico("cap", "ico", 24)}</span><h3>Graduate pipeline</h3><p>Dedicated internship and entry-level pages reach students and fresh graduates.</p></div>
<div class="why-card"><span class="why-ic">{ico("laptop", "ico", 24)}</span><h3>Remote talent</h3><p>Hire Kenya-based remote workers screened for reliability and skills.</p></div>
<div class="why-card"><span class="why-ic">{ico("users", "ico", 24)}</span><h3>Shortlisting service</h3><p>Let us advertise, screen and shortlist for you when you are short on time.</p></div>
<div class="why-card"><span class="why-ic">{ico("bell", "ico", 24)}</span><h3>Job alerts and social reach</h3><p>Your job reaches subscribers by email, WhatsApp and social media.</p></div>
<div class="why-card"><span class="why-ic">{ico("trend", "ico", 24)}</span><h3>Advertising packages</h3><p>Banner, newsletter and social boosts to build your employer brand.</p></div></div></div></section>
{faq_html(faq)}
{cta_band("Ready to hire?", "Register once and post your first job today.", ("Post a job", "/employers/post-a-job/"), ("Talk to us", "/contact/"))}'''
    page("/employers/", f"Post a Job in Kenya | Hire Verified Talent from {ksh(C.PRICE_STANDARD)} | KaziBora", f"Post jobs in Kenya from {ksh(C.PRICE_STANDARD)}. Reach verified, serious job seekers, interns and remote talent. Featured listings, packages and shortlisting available.",
         body, active="employers", schema=[faq_schema(faq)], crumbs=[("Home", "/"), ("Employers", "/employers/")], prio="0.9")

    # pricing
    rows = [("Duration", "30 days", "30 days", "6 months to use", "12 months to use"), ("Jobs included", "1", "1", "5", "10 (3 featured)"),
            ("Verified badge", "✓", "✓", "✓", "✓"), ("Top placement", "-", "✓", "-", "3 jobs"), ("Homepage slot", "-", "✓", "-", "3 jobs"),
            ("Job alert and social share", "Alert", "Alert + social", "Alert", "Alert + social"), ("Company profile page", "✓", "✓", "✓", "✓"),
            ("Price", ksh(C.PRICE_STANDARD), ksh(C.PRICE_FEATURED), ksh(C.PRICE_STARTER_PACK), ksh(C.PRICE_GROWTH_PACK))]
    thead = "<tr><th></th><th>Standard</th><th class='hot'>Featured</th><th>Starter pack</th><th>Growth pack</th></tr>"
    tbody = "".join("<tr><th scope='row'>" + r[0] + "</th>" + "".join(f"<td>{x}</td>" for x in r[1:]) + "</tr>" for r in rows)
    addons = [("Shortlisting service", C.PRICE_SHORTLIST, "per role", "We advertise, screen and deliver 8-10 matched candidates."),
              ("Urgent tag", 1000, "per listing", "Highlight a closing-soon vacancy in search results."),
              ("Social media boost", C.PRICE_SOCIAL, "per post", "Your job on our social channels and WhatsApp status."),
              ("Re-post / extend 30 days", 2000, "per listing", "Keep a listing live for another 30 days.")]
    addon_html = "".join(f'<div class="why-card"><h3>{t}</h3><p class="price"><b>{ksh(p)}</b> <span>{u}</span></p><p>{d}</p></div>' for t, p, u, d in addons)
    pay_faq = [("Which payment methods do you accept?", "M-Pesa, bank transfer and invoice for registered companies. We confirm payment before your job goes live."),
               ("Do prices include VAT?", "Prices shown are placeholders in Kenya shillings. Confirm VAT treatment for your business before launch."),
               ("Can I get a refund?", "If we cannot verify your vacancy we refund in full. Once a verified listing is live, fees are non-refundable.")]
    body = f'''{hero_small("Job posting prices in Kenya", "Choose a single listing or save with a package. Every plan includes verification and the Verified badge.", [("Home", "/"), ("Employers", "/employers/"), ("Pricing", "/employers/pricing/")])}
<section class="section tight"><div class="wrap">{plan_cards()}</div></section>
<section class="section"><div class="wrap"><h2 class="sec-title">Compare plans</h2><div class="table-wrap"><table class="cmp">{thead}{tbody}</table></div></div></section>
<section class="section alt"><div class="wrap"><h2 class="sec-title">Add-ons and services</h2><div class="why-grid">{addon_html}</div><p class="center-link"><a class="btn btn-outline" href="/employers/advertising/">See recruitment advertising packages</a></p></div></section>
{faq_html(pay_faq, "Pricing questions")}{cta_band("Get your first job live today", "Verification usually takes one working day.", ("Post a job", "/employers/post-a-job/"))}'''
    page("/employers/pricing/", f"Job Posting Prices in Kenya: From {ksh(C.PRICE_STANDARD)} | KaziBora Employers", f"KaziBora job posting prices: standard {ksh(C.PRICE_STANDARD)}, featured {ksh(C.PRICE_FEATURED)}, starter and growth packages. Compare plans and add-ons.",
         body, active="employers", schema=[faq_schema(pay_faq)], crumbs=[("Home", "/"), ("Employers", "/employers/"), ("Pricing", "/employers/pricing/")], prio="0.8")

    # register
    inds = ["Accounting & Finance", "Agriculture", "Construction", "Education", "Healthcare", "Hospitality & Tourism", "ICT & Software", "Legal", "Logistics", "Manufacturing", "NGO / Non-profit", "Retail", "Other"]
    fields = (field("Company or organisation name", "company", req=True, ph="Registered business name") + field("KRA PIN or registration number", "reg_no", req=True, ph="Used only for verification")
              + field("Contact person", "contact", req=True) + field("Job title", "role", ph="e.g. HR Manager") + field("Work email", "email", "email", True) + field("Phone / WhatsApp", "phone", "tel", True, "07XX XXX XXX")
              + field("Website or social page", "website", "url", False, "https://") + field("Industry", "industry", "select", True, options([(i, i) for i in inds], "Choose industry"))
              + field("Company size", "size", "select", False, options([(s, s) for s in ("1-10", "11-50", "51-200", "201-500", "500+")], "Choose size"))
              + field("Town / county", "county", "select", True, options([(l["name"], l["name"]) for l in LOC.values()] + [("Other", "Other")], "Choose location"))
              + field("What are you hiring for?", "needs", "textarea", False, "Roles, how many people and when")
              + '<label class="chk"><input type="checkbox" name="no_fee" required> We promise never to charge candidates any fee at any stage of recruitment.</label>')
    body = f'''{hero_small("Employer registration", "Tell us about your organisation. We verify every employer before their first job goes live, which protects job seekers and your reputation.", [("Home", "/"), ("Employers", "/employers/"), ("Register", "/employers/register/")])}
<section class="section tight"><div class="wrap two-col narrow-form"><div class="main-col"><div class="form-card">{form("employer-registration", fields, "Register my company", "We review registrations within one working day and contact you by phone or email.")}</div></div>
<aside class="side-col"><div class="side-card"><h2>What happens next</h2><ol class="num-list"><li>We review your details</li><li>We confirm your business and contact</li><li>You post jobs and pay when approved</li></ol></div>
<div class="side-card"><h2>Need help?</h2><p>Call or WhatsApp {C.CONTACT_PHONE_DISPLAY}.</p><a class="btn btn-outline" href="https://wa.me/{C.WHATSAPP_NUMBER}" target="_blank" rel="noopener">Chat on WhatsApp</a></div></aside></div></section>'''
    page("/employers/register/", "Employer Registration | Register to Post Jobs in Kenya | KaziBora", "Register your company on KaziBora to post verified jobs in Kenya. Quick verification, paid listings and applications delivered to your inbox.",
         body, active="employers", crumbs=[("Home", "/"), ("Employers", "/employers/"), ("Register", "/employers/register/")], prio="0.7")

    # post a job
    plans = [("standard", f"Standard listing: {ksh(C.PRICE_STANDARD)}"), ("featured", f"Featured listing: {ksh(C.PRICE_FEATURED)}"),
             ("starter", f"Starter pack (5 listings): {ksh(C.PRICE_STARTER_PACK)}"), ("growth", f"Growth pack (10 listings): {ksh(C.PRICE_GROWTH_PACK)}")]
    plan_radios = "".join(f'<label class="radio"><input type="radio" name="plan" value="{v}"{" checked" if v == "standard" else ""} data-price="{p}"> {t}</label>'
                          for (v, t), p in zip(plans, [C.PRICE_STANDARD, C.PRICE_FEATURED, C.PRICE_STARTER_PACK, C.PRICE_GROWTH_PACK]))
    fields = (f'<fieldset class="fld"><legend>Choose a plan</legend><div class="radios">{plan_radios}</div></fieldset>'
              + field("Company name", "company", req=True) + field("Contact person", "contact", req=True) + field("Work email", "email", "email", True) + field("Phone / WhatsApp", "phone", "tel", True)
              + field("Job title", "job_title", req=True, ph="e.g. Sales Executive") + field("Category", "category", "select", True, options([(c["name"], c["name"]) for c in CAT.values()], "Choose category"))
              + field("Experience level", "level", "select", True, options([(v, v) for v in D.LEVELS.values()], "Choose level")) + field("Job type", "type", "select", True, options([(t, t) for t in ("Full-time", "Part-time", "Contract", "Internship")], "Choose type"))
              + field("Location", "location", "select", True, options([(l["name"], l["name"]) for l in LOC.values()] + [("Remote (Kenya)", "Remote (Kenya)"), ("Other", "Other")], "Choose location"))
              + field("Monthly pay range (KSh)", "salary", ph="e.g. 45,000 - 60,000") + field("Application deadline", "deadline", "date", True)
              + field("Job description", "description", "textarea", True, "Responsibilities, requirements and benefits")
              + field("How should candidates apply?", "apply_via", "select", True, options([("KaziBora form", "Through KaziBora (applications to my email)"), ("External link", "External link or careers page")], "Choose"))
              + field("Payment method", "payment", "select", True, options([("M-Pesa", "M-Pesa"), ("Bank transfer", "Bank transfer"), ("Invoice", "Invoice (registered company)")], "Choose payment method"))
              + '<label class="chk"><input type="checkbox" name="no_fee" required> We confirm this vacancy is genuine and we will never charge candidates a fee.</label>'
              + '<p class="price-total">Total to pay after approval: <b id="plan-total">' + ksh(C.PRICE_STANDARD) + "</b></p>")
    body = f'''{hero_small("Post a job in Kenya", "Fill in the details below. We verify your vacancy, send you payment details and publish your job, usually within one working day.", [("Home", "/"), ("Employers", "/employers/"), ("Post a job", "/employers/post-a-job/")])}
<section class="section tight"><div class="wrap two-col narrow-form"><div class="main-col"><div class="form-card">{form("post-a-job", fields, "Submit job for verification", "You pay only after your listing is approved.")}</div></div>
<aside class="side-col"><div class="side-card"><h2>Included in every listing</h2><ul class="ticks"><li>{ico("check", "ico", 18)} Verified badge</li><li>{ico("check", "ico", 18)} Applications by email</li><li>{ico("check", "ico", 18)} Company profile page</li><li>{ico("check", "ico", 18)} Job alert inclusion</li></ul></div>
<div class="side-card"><h2>Pay how you prefer</h2><p>M-Pesa, bank transfer or invoice. We send payment details after your vacancy is approved.</p></div>
<div class="side-card"><h2>Hiring several people?</h2><p>Save with the <a href="/employers/pricing/">Starter or Growth pack</a>.</p></div></aside></div></section>'''
    page("/employers/post-a-job/", f"Post a Job in Kenya: Paid Job Listing from {ksh(C.PRICE_STANDARD)} | KaziBora", "Post your vacancy on KaziBora. Verified listings, featured placement and packages. Pay by M-Pesa or bank transfer after approval.",
         body, active="employers", crumbs=[("Home", "/"), ("Employers", "/employers/"), ("Post a job", "/employers/post-a-job/")], prio="0.8")

    # advertising
    pkgs = [("Homepage banner", C.PRICE_BANNER, "per week", "A prime banner slot on our homepage and job pages, linking to your careers page or campaign.", "banner"),
            ("Newsletter sponsorship", C.PRICE_NEWSLETTER, "per issue", "Your logo, message and featured jobs in our job-alert newsletter.", "newsletter"),
            ("Social media boost", C.PRICE_SOCIAL, "per post", "A designed post for your vacancy on our social channels and WhatsApp status.", "social"),
            ("Employer brand page", 12000, "per quarter", "A premium company profile with video, culture photos and all your jobs in one place.", "brand"),
            ("Campus and graduate drive", 35000, "per campaign", "Reach students and fresh graduates for an intake or internship programme.", "campus"),
            ("Shortlisting service", C.PRICE_SHORTLIST, "per role", "We advertise, screen and deliver a shortlist of matched candidates.", "shortlist")]
    cards = "".join(f'<div class="plan"><h3>{t}</h3><p class="price"><b>{ksh(p)}</b> <span>{u}</span></p><p>{d}</p></div>' for t, p, u, d, _ in pkgs)
    fields = (field("Company", "company", req=True) + field("Contact person", "contact", req=True) + field("Email or WhatsApp", "contact_info", req=True)
              + field("Package of interest", "package", "select", True, options([(t, t) for t, *_ in pkgs], "Choose package")) + field("Tell us about your goals", "goals", "textarea", False))
    body = f'''{hero_small("Recruitment advertising packages", "Put your employer brand in front of Kenya's verified job seekers, graduates and remote talent.", [("Home", "/"), ("Employers", "/employers/"), ("Advertising", "/employers/advertising/")])}
<section class="section tight"><div class="wrap"><div class="plan-grid three">{cards}</div></div></section>
<section class="section alt"><div class="wrap narrow"><h2 class="sec-title">Request a quote</h2><div class="form-card">{form("advertising-enquiry", fields, "Request a quote", "We reply within one working day.")}</div></div></section>'''
    page("/employers/advertising/", "Recruitment Advertising in Kenya: Banners, Newsletter & Social | KaziBora", "Recruitment advertising packages in Kenya: homepage banners, newsletter sponsorship, social media job boosts, employer brand pages and graduate campaigns.",
         body, active="employers", crumbs=[("Home", "/"), ("Employers", "/employers/"), ("Advertising", "/employers/advertising/")], prio="0.6")

    # directory + profiles
    cards = "".join(f'<a class="emp-card" href="{e["url"]}"><img src="{e["logo"]}" width="64" height="64" alt="" loading="lazy"><div><h3>{esc(e["name"])}</h3><p>{esc(e["industry"])} &middot; {esc(LOC[e["loc"]]["name"])}</p>{verified_badge(e)} <span class="mini">{plural(sum(1 for j in J if j["emp"]["slug"] == e["slug"]), "open job")}</span></div></a>' for e in EMP.values())
    body = f'''{hero_small("Verified employers in Kenya", "Companies and organisations that passed KaziBora verification and are hiring now.", [("Home", "/"), ("Employers", "/employers/"), ("Directory", "/employers/directory/")])}
<section class="section tight"><div class="wrap"><div class="emp-grid">{cards}</div></div></section>{cta_band("Is your company hiring?", "Join our verified employers.", ("Register", "/employers/register/"))}'''
    page("/employers/directory/", "Verified Employers in Kenya: Company Directory | KaziBora", "Browse verified employers hiring in Kenya. See company profiles, open jobs and locations for companies that passed KaziBora verification.",
         body, active="jobs", crumbs=[("Home", "/"), ("Employers", "/employers/"), ("Directory", "/employers/directory/")], prio="0.6")

    for e in EMP.values():
        jobs = sorted([j for j in J if j["emp"]["slug"] == e["slug"]], key=lambda j: j["ago"])
        org = {"@context": "https://schema.org", "@type": "Organization", "name": e["name"], "description": e["about"], "url": url(e["url"]), "logo": url(e["logo"]),
               "address": {"@type": "PostalAddress", "addressLocality": LOC[e["loc"]]["name"], "addressCountry": "KE"}}
        body = f'''<section class="job-head"><div class="wrap">{breadcrumbs_html([("Home", "/"), ("Employers", "/employers/"), ("Directory", "/employers/directory/"), (e["name"], e["url"])])}
<div class="jh-in"><img class="jh-logo" src="{e["logo"]}" width="72" height="72" alt="{esc(e["name"])} logo (placeholder)"><div><h1>{esc(e["name"])}</h1><p class="jh-co">{verified_badge(e)} <span class="mini">{esc(e["industry"])} &middot; {esc(e["size"])} &middot; {esc(LOC[e["loc"]]["name"])}</span></p></div></div></div></section>
<section class="section tight"><div class="wrap two-col"><div class="main-col"><h2 class="sec-title sm">About {esc(e["name"])}</h2><p>{esc(e["about"])}</p><h2 class="sec-title sm">Open jobs at {esc(e["name"])}</h2>{job_list(jobs, "No open jobs right now. Create a job alert to hear when this employer hires.")}</div>
<div class="side-col"><div class="side-card"><h2>Company details</h2><dl class="overview"><div><dt>Industry</dt><dd>{esc(e["industry"])}</dd></div><div><dt>Size</dt><dd>{esc(e["size"])}</dd></div><div><dt>Location</dt><dd>{esc(LOC[e["loc"]]["name"])}</dd></div><div><dt>Status</dt><dd>{"Verified" if e["verified"] else "Verification pending"}</dd></div></dl></div>
<div class="side-card"><h2>Hiring too?</h2><a class="btn btn-primary" href="/employers/post-a-job/">Post a job</a></div></div></div></section>'''
        page(e["url"], f"{e['name']}: Jobs & Company Profile | KaziBora", f"{e['name']} is hiring in Kenya. See {plural(len(jobs), 'open job')}, company details and verification status on KaziBora.",
             body, active="jobs", schema=[org], crumbs=[("Home", "/"), ("Employers", "/employers/"), ("Directory", "/employers/directory/"), (e["name"], e["url"])], prio="0.5")


def build_all():
    build_home()
    build_jobs_hub()
    build_landings()
    build_job_pages()
    build_employer_pages()
