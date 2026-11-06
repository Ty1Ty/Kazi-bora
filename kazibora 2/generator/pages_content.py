"""Tools, guidance, training and company pages."""
import json
import re

import config as C
import data as D
from lib import *
from pages_jobs import alert_band, article_card, avg_pay, faq_home, sal_range, J

PHONE_LINK = f'<a href="tel:{C.CONTACT_PHONE_TEL}">{C.CONTACT_PHONE_DISPLAY}</a>'


def crumb(*items):
    return [("Home", "/")] + list(items)


# ===================================================================== CV / COVER LETTER
def build_cv():
    c = crumb(("CV builder", "/cv-builder/"))
    faq = [("Is the CV builder free?", "Yes. It is completely free, with no sign-up. Your details stay in your browser and are never uploaded."),
           ("How do I save my CV as a PDF?", "Click Print / Save as PDF and choose &ldquo;Save as PDF&rdquo; as the destination. Turn off headers and footers for the cleanest result.".replace("&ldquo;", "“").replace("&rdquo;", "”")),
           ("How long should a Kenyan CV be?", "One page for students and entry-level candidates, and two pages for experienced professionals."),
           ("Can you write my CV for me?", f"Yes. See our <a href=\"/cv-writing-service/\">CV writing service</a> from {ksh(C.PRICE_CV_BASIC)}.")]
    body = f'''{hero_small("Free CV builder for Kenya", "Fill in your details, pick a template and print a clean, recruiter-friendly CV. Works on your phone, saves automatically in your browser.", c)}
<section class="section tight"><div class="wrap">
<div class="cv-toolbar" role="toolbar" aria-label="CV tools"><label>Template <select id="cv-template"><option value="classic">Classic</option><option value="modern">Modern</option><option value="compact">Compact (1 page)</option></select></label>
<label>Colour <select id="cv-accent"><option value="#0f6b4a">Forest green</option><option value="#1d4ed8">Blue</option><option value="#7c3aed">Purple</option><option value="#be123c">Crimson</option><option value="#1f2937">Charcoal</option></select></label>
<button class="btn btn-sm btn-outline" type="button" id="cv-sample">Load sample</button><button class="btn btn-sm btn-outline" type="button" id="cv-clear">Clear all</button>
<button class="btn btn-sm btn-primary" type="button" id="cv-print">{ico("print", "ico", 16)} Print / Save as PDF</button></div>
<div class="cv-layout"><form class="cv-form form" id="cv-form" onsubmit="return false" autocomplete="off">
<fieldset><legend>Your details</legend>
<div class="grid2">{field("Full name", "name", extra='data-cv="name"')}{field("Professional title", "title", extra='data-cv="title"', ph="e.g. Accounts Assistant")}</div>
<div class="grid2">{field("Email", "email", "email", extra='data-cv="email"')}{field("Phone", "phone", "tel", extra='data-cv="phone"')}</div>
<div class="grid2">{field("Town / county", "location", extra='data-cv="location"')}{field("LinkedIn or portfolio (optional)", "link", extra='data-cv="link"')}</div></fieldset>
<fieldset><legend>Profile</legend>{field("Short profile (3-4 lines)", "summary", "textarea", extra='data-cv="summary"', help_="Who you are, what you do well and the role you want.")}</fieldset>
<fieldset><legend>Work experience</legend><div id="cv-exp"></div><button class="btn btn-sm btn-outline" type="button" id="add-exp">{ico("plus", "ico", 16)} Add job</button></fieldset>
<fieldset><legend>Education</legend><div id="cv-edu"></div><button class="btn btn-sm btn-outline" type="button" id="add-edu">{ico("plus", "ico", 16)} Add education</button></fieldset>
<fieldset><legend>Skills, languages &amp; referees</legend>{field("Skills (comma separated)", "skills", extra='data-cv="skills"', ph="Excel, QuickBooks, customer service")}
{field("Languages (comma separated)", "languages", extra='data-cv="languages"', ph="English, Kiswahili")}{field("Referees", "referees", "textarea", extra='data-cv="referees"', help_="Name, job title, organisation and phone. Ask permission first. Leave blank for &ldquo;Available on request&rdquo;.")}</fieldset>
</form>
<div class="cv-preview-wrap"><p class="mini">Live preview</p><div id="cv-preview" class="cv t-classic" aria-live="polite"></div></div></div>
<div class="tip-strip"><p><b>Tip:</b> Start every bullet with an action verb and add numbers where you can. Read our <a href="/career-advice/how-to-write-a-cv-in-kenya/">guide to writing a CV in Kenya</a>. Want an expert to do it? <a href="/cv-writing-service/">Try our CV writing service</a>.</p></div></div></section>
{faq_html(faq)}{cta_band("Now find the right job", "Match your new CV to verified jobs in Kenya.", ("Browse jobs", "/jobs/"), ("Write a cover letter", "/cover-letter-generator/"))}'''
    page("/cv-builder/", "Free CV Builder for Kenya: Create & Download a Professional CV | KaziBora", "Build a professional CV in minutes with our free Kenyan CV builder. Choose a template, edit live and save as PDF. No sign-up, private and mobile-friendly.",
         body, active="tools", schema=[faq_schema(faq), {"@context": "https://schema.org", "@type": "WebApplication", "name": "KaziBora CV Builder", "applicationCategory": "BusinessApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "KES"}, "url": url("/cv-builder/")}],
         crumbs=c, prio="0.9", extra='<script src="/assets/js/cv.js" defer></script>')

    c = crumb(("Cover letter generator", "/cover-letter-generator/"))
    faq = [("What should a cover letter include?", "Your contact details, the employer's name, the job title, two or three reasons you are a good fit with examples, and a polite call to action."),
           ("How long should a cover letter be?", "Half to three-quarters of a page. Keep it specific and easy to scan."),
           ("Should I send a cover letter with every application?", "Yes, unless the advert says not to. Tailor each letter to the job and company.")]
    tones = options([("professional", "Professional"), ("enthusiastic", "Enthusiastic"), ("concise", "Short and direct")])
    body = f'''{hero_small("Free cover letter generator", "Answer a few questions and get a tailored cover letter in seconds. Edit it, copy it or print it.", c)}
<section class="section tight"><div class="wrap cl-layout"><form class="form cl-form" id="cl-form" onsubmit="return false" autocomplete="off">
<fieldset><legend>About you</legend><div class="grid2">{field("Your full name", "name", req=True, ph="e.g. Brian Otieno")}{field("Phone", "phone", "tel", ph="07XX XXX XXX")}</div>
<div class="grid2">{field("Email", "email", "email")}{field("Town / county", "town", ph="Nairobi")}</div></fieldset>
<fieldset><legend>The job</legend><div class="grid2">{field("Job title", "job", req=True, ph="e.g. Customer Care Representative")}{field("Company", "company", req=True, ph="e.g. Mlima Telecom Services")}</div>
{field("Hiring manager (optional)", "manager", ph="e.g. Ms. Achieng")}</fieldset>
<fieldset><legend>Your pitch</legend>{field("Experience level", "level", "select", False, options([("graduate", "Recent graduate / student"), ("some", "1-3 years' experience"), ("experienced", "4+ years' experience")]))}
{field("Top three skills (comma separated)", "skills", ph="communication, Excel, problem solving")}{field("One achievement or project", "achievement", "textarea", False, "e.g. Led a student team that raised KSh 80,000 for a community project")}
{field("Tone", "tone", "select", False, tones)}</fieldset></form>
<div class="cl-out-wrap"><div class="cv-toolbar"><button class="btn btn-sm btn-primary" type="button" id="cl-copy">{ico("copy", "ico", 16)} Copy letter</button><button class="btn btn-sm btn-outline" type="button" id="cl-print">{ico("print", "ico", 16)} Print</button></div>
<div id="cl-out" class="letter" contenteditable="true" aria-label="Your cover letter (editable)" spellcheck="true"></div><p class="mini">You can edit the letter directly before copying it.</p></div></div></section>
{faq_html(faq)}{cta_band("Pair it with a polished CV", "Use our free CV builder next.", ("Build my CV", "/cv-builder/"))}'''
    page("/cover-letter-generator/", "Free Cover Letter Generator for Kenya | KaziBora", "Create a professional cover letter in seconds with our free generator. Tailored to Kenyan employers, with three tones. Copy or print, no sign-up.",
         body, active="tools", schema=[faq_schema(faq)], crumbs=c, prio="0.8", extra='<script src="/assets/js/cv.js" defer></script>')

    # CV writing service
    c = crumb(("CV writing service", "/cv-writing-service/"))
    pk = [("CV Basic", C.PRICE_CV_BASIC, ["Professional rewrite of your CV", "ATS-friendly layout", "1 revision", "Delivered in 48 hours"], False),
          ("CV Pro", C.PRICE_CV_PRO, ["Everything in Basic", "Tailored cover letter", "LinkedIn profile tune-up", "2 revisions, 24-hour rush option"], True),
          ("Executive", C.PRICE_CV_EXEC, ["Everything in Pro", "Senior / leadership positioning", "30-minute interview coaching call", "Unlimited revisions for 14 days"], False)]
    cards = "".join(f'<div class="plan{" hot" if h else ""}">{"<span class=ribbon>Best value</span>" if h else ""}<h3>{n}</h3><p class="price"><b>{ksh(p)}</b></p><ul class="ticks">{"".join(f"<li>{ico(chr(99)+chr(104)+chr(101)+chr(99)+chr(107), chr(105)+chr(99)+chr(111), 18)} {f}</li>" for f in feats)}</ul></div>' for n, p, feats, h in pk)
    fields = (field("Full name", "name", req=True) + field("Phone / WhatsApp", "phone", "tel", True) + field("Email", "email", "email", True)
              + field("Package", "package", "select", True, options([(n, f"{n}: {ksh(p)}") for n, p, *_ in pk], "Choose a package"))
              + field("Target job or industry", "target", ph="e.g. Accounting, entry-level") + field("Anything we should know?", "notes", "textarea", False)
              + field("Upload your current CV (optional)", "cv", "file", False, extra='accept=".pdf,.doc,.docx"'))
    faq = [("How does the CV writing service work?", "Choose a package, send us your current CV or notes and we write a polished CV tailored to your target jobs. You review it and request changes."),
           ("How do I pay?", "We send an M-Pesa request or invoice after you submit the form. Work starts when payment is confirmed."),
           ("Will my details stay private?", "Yes. We use your information only to prepare your documents.")]
    body = f'''{hero_small("Professional CV writing in Kenya", "Let an expert turn your experience into a CV that gets interviews. Optional paid service, fully separate from our free tools.", c)}
<section class="section tight"><div class="wrap"><div class="plan-grid three">{cards}</div></div></section>
<section class="section alt"><div class="wrap narrow"><h2 class="sec-title">Order your CV</h2><div class="form-card">{form("cv-service", fields, "Request my CV", "We contact you within one working day.", enctype="multipart/form-data")}</div></div></section>{faq_html(faq)}'''
    page("/cv-writing-service/", f"Professional CV Writing Service in Kenya from {ksh(C.PRICE_CV_BASIC)} | KaziBora", f"Get a professionally written CV, cover letter and LinkedIn profile in Kenya. Packages from {ksh(C.PRICE_CV_BASIC)}, delivered in 48 hours.",
         body, active="tools", schema=[faq_schema(faq), {"@context": "https://schema.org", "@type": "Service", "name": "CV writing service", "provider": {"@id": C.SITE_URL + "/#org"}, "areaServed": "KE",
                                                                                          "offers": [{"@type": "Offer", "name": n, "price": str(p), "priceCurrency": "KES"} for n, p, *_ in pk]}], crumbs=c, prio="0.7")


# ===================================================================== INTERVIEW PREP
def build_interview():
    c = crumb(("Interview prep", "/interview-prep/"))
    cats = []
    for q in D.QUESTIONS:
        if q[0] not in cats:
            cats.append(q[0])
    chips = '<button class="chip is-on" type="button" data-iq-cat="">All</button>' + "".join(f'<button class="chip" type="button" data-iq-cat="{esc(k)}">{esc(k)}</button>' for k in cats)
    items = "".join(f'<details class="faq-item iq" data-cat="{esc(q[0])}"><summary><span class="iq-cat">{esc(q[0])}</span>{esc(q[1])}</summary><div><p><b>How to answer:</b> {esc(q[2])}</p></div></details>' for q in D.QUESTIONS)
    faq = [(q[1], q[2]) for q in D.QUESTIONS[:8]]
    star = [("S", "Situation", "Set the scene in one or two sentences."), ("T", "Task", "Explain your responsibility or the goal."), ("A", "Action", "Describe what you did, step by step. Use &ldquo;I&rdquo;, not &ldquo;we&rdquo;."), ("R", "Result", "Share the outcome with numbers and what you learned.")]
    star_html = "".join(f'<div class="star"><b>{a}</b><h3>{b}</h3><p>{d}</p></div>'.replace("&ldquo;", "“").replace("&rdquo;", "”") for a, b, d in star)
    day = ["Research the employer: products, news, values and the job advert", "Prepare three STAR stories and two questions to ask", "Plan your route or test your link and power for online interviews", "Carry copies of your CV, certificates and ID", "Arrive 15 minutes early, dress neatly and switch off your phone", "Send a thank-you message the same day"]
    day_html = "".join(f'<li><label class="chk"><input type="checkbox"> {d}</label></li>' for d in day)
    body = f'''{hero_small("Interview preparation trainer", f"Practise {len(D.QUESTIONS)} common interview questions for Kenyan employers, with coaching tips for each. Free, no sign-up.", c)}
<section class="section tight"><div class="wrap">
<div class="practice" id="practice" hidden><div class="pr-top"><span class="pr-label">Practice mode</span><span class="pr-timer" id="pr-timer" aria-live="off">02:00</span></div><p class="pr-q" id="pr-q"></p><p class="pr-tip" id="pr-tip" hidden></p>
<div class="pr-btns"><button class="btn btn-primary" type="button" id="pr-start">Start timer</button><button class="btn btn-outline" type="button" id="pr-reveal">Show tip</button><button class="btn btn-outline" type="button" id="pr-next">Next question</button><button class="link-btn" type="button" id="pr-close">Close</button></div></div>
<div class="iq-bar"><button class="btn btn-amber" type="button" id="pr-open">{ico("mic", "ico", 18)} Start practice mode</button><div class="chips" id="iq-chips" role="group" aria-label="Question categories">{chips}</div></div>
<div class="faq" id="iq-list">{items}</div></div></section>
<section class="section alt"><div class="wrap"><div class="sec-head center"><div><p class="kicker">The STAR method</p><h2 class="sec-title">Structure every behavioural answer</h2></div></div><div class="star-grid">{star_html}</div></div></section>
<section class="section"><div class="wrap narrow"><h2 class="sec-title">Interview day checklist</h2><ul class="checklist">{day_html}</ul>
<p>Read more: <a href="/career-advice/common-interview-questions-and-answers-kenya/">common interview questions and answers in Kenya</a> and <a href="/career-advice/how-to-prepare-for-a-panel-interview/">how to prepare for a panel interview</a>.</p></div></section>
{cta_band("Ready to apply?", "Find verified jobs and apply in minutes.", ("Browse jobs", "/jobs/"), ("Build my CV", "/cv-builder/"))}'''
    page("/interview-prep/", f"Interview Questions & Answers for Kenya: Free Practice Trainer | KaziBora", f"Practise {len(D.QUESTIONS)} common interview questions for Kenyan jobs with expert answer tips, STAR method guide and an interview-day checklist. Free.",
         body, active="tools", schema=[faq_schema(faq)], crumbs=c, prio="0.8", extra='<script src="/assets/js/tools.js" defer></script>')


# ===================================================================== SAFETY
def build_safety():
    c = crumb(("Scam checker", "/scam-checker/"))
    flags = "".join(f'<label class="flag"><input type="checkbox" value="{k}" data-w="{w}"><span>{esc(t)}</span></label>' for k, t, w in D.SCAM_FLAGS)
    faq = [("How do I know if a job offer is a scam?", "Warning signs include being asked to pay any fee, interviews only on chat apps, offers without a real interview, and requests for ID or bank details too early."),
           ("What should I do if I already paid a scammer?", "Stop contacting them, keep all messages and receipts, report to your payment provider (M-Pesa 234 or your bank) and to the police. Then report the advert to us."),
           ("Does a legitimate employer ever charge fees?", "No. Genuine employers do not charge for applications, interviews, training, uniforms or medicals.")]
    body = f'''{hero_small("Job scam checker", "Tick anything that applies to the offer you received. We will show how risky it looks and what to do next. Nothing you tick is stored or sent.", c)}
<section class="section tight"><div class="wrap two-col"><div class="main-col"><form id="scam-form" class="scam-form" onsubmit="return false"><fieldset><legend>Does any of this match your job offer?</legend>{flags}</fieldset></form></div>
<aside class="side-col"><div class="result-card" id="scam-result" aria-live="polite"><p class="mini">Your result</p><div class="meter" aria-hidden="true"><i id="scam-bar"></i></div><h2 id="scam-title">Tick the boxes that apply</h2><p id="scam-text">We will assess the risk as you go.</p><div id="scam-actions"></div></div></aside></div></section>
<section class="section alt"><div class="wrap narrow"><h2 class="sec-title">Stay safe: five golden rules</h2><ol class="num-list big"><li><b>Never pay</b> to get a job, interview, training or uniform.</li><li><b>Verify the company</b> on its official website and phone number.</li><li><b>Insist on a real interview</b> in a proper office or on a company video call.</li><li><b>Keep documents safe</b>: share ID and bank details only after a signed offer.</li><li><b>Trust your instincts</b> and ask a friend or us if you are unsure.</li></ol>
<p><a class="btn btn-primary" href="/report-scam/">Report a suspicious job</a> <a class="btn btn-outline" href="/career-advice/how-to-spot-fake-job-adverts-in-kenya/">Read: how to spot fake job adverts</a></p></div></section>{faq_html(faq)}'''
    page("/scam-checker/", "Job Scam Checker for Kenya: Is This Job Offer Real? | KaziBora", "Check if a job offer in Kenya is a scam. Answer a few questions and get an instant risk rating plus what to do next. Free and private.",
         body, active="tools", schema=[faq_schema(faq)], crumbs=c, prio="0.8", extra='<script src="/assets/js/tools.js" defer></script>')

    c = crumb(("Report a job", "/report-scam/"))
    fields = (field("Job link or title", "job", req=True, ph="Paste the link or name of the advert") + field("Employer or recruiter name", "employer")
              + field("What happened?", "issue", "select", True, options([(v, v) for v in ("Asked me to pay a fee", "Fake company or recruiter", "Job does not exist", "Asked for ID or bank details", "Misleading pay or duties", "Other")], "Choose an issue"))
              + field("Details", "details", "textarea", True, "Tell us what happened. Do not include passwords or PINs.") + field("Your email or phone (optional)", "contact", help_="Only if you want us to follow up."))
    body = f'''{hero_small("Report a suspicious job", "Help us protect other job seekers. We review every report quickly and remove listings that break our rules.", c)}
<section class="section tight"><div class="wrap two-col narrow-form"><div class="main-col"><div class="form-card">{form("report-scam", fields, "Send report", "Reports are reviewed by our verification team.")}</div></div>
<aside class="side-col"><div class="side-card"><h2>Already paid?</h2><p>Contact your payment provider immediately, keep all receipts and messages, and report to the police.</p></div><div class="side-card"><h2>Not sure?</h2><a class="btn btn-outline" href="/scam-checker/">Use the scam checker</a></div></aside></div></section>'''
    page("/report-scam/", "Report a Fake or Suspicious Job in Kenya | KaziBora", "Report a suspicious job advert or recruiter in Kenya. Our verification team reviews every report and removes listings that break our rules.", body, active="tools", crumbs=c, prio="0.5")

    c = crumb(("How we verify", "/verified-jobs/"))
    steps = "".join(f'<div class="step"><span class="step-n">{n}</span><h3>{t}</h3><p>{p}</p></div>' for n, t, p in D.VERIFY_STEPS)
    faq = [("What does the Verified badge mean?", "It means the employer passed our checklist: identity checked, vacancy confirmed, no-fee promise signed and advert reviewed."),
           ("Can a verified job still be a scam?", "Our checks greatly reduce risk but no system is perfect. If anything feels wrong, use the Report button and we will investigate."),
           ("What is &ldquo;verification pending&rdquo;?".replace("&ldquo;", "“").replace("&rdquo;", "”"), "The employer has submitted details and our team is still checking. Take extra care and never pay.")]
    body = f'''{hero_small("How KaziBora verifies jobs and employers", "Trust is our product. Here is exactly what happens before a job appears on KaziBora.", c)}
<section class="section"><div class="wrap"><div class="steps five">{steps}</div></div></section>
<section class="section alt"><div class="wrap two-col"><div class="main-col"><h2 class="sec-title sm">What the Verified badge tells you</h2><ul class="ticks big">
<li>{ico("check", "ico", 18)} The company exists and has a working contact</li><li>{ico("check", "ico", 18)} The vacancy is genuine and currently open</li><li>{ico("check", "ico", 18)} The employer has promised never to charge candidates</li><li>{ico("check", "ico", 18)} A person at KaziBora read the advert for red flags</li></ul></div>
<div class="side-col"><div class="side-card"><h2>See something wrong?</h2><a class="btn btn-primary" href="/report-scam/">Report a job</a></div><div class="side-card"><h2>Test an offer</h2><a class="btn btn-outline" href="/scam-checker/">Scam checker</a></div></div></div></section>{faq_html(faq)}'''
    page("/verified-jobs/", "How We Verify Jobs & Employers in Kenya | KaziBora", "See how KaziBora verifies employers and vacancies: identity checks, genuine vacancy confirmation, a no-fee promise and fast scam reporting.", body, active="tools", schema=[faq_schema(faq)], crumbs=c, prio="0.7")


# ===================================================================== SALARY GUIDE
def build_salary():
    c = crumb(("Salary guide", "/salary-guide/"))
    rows = []
    for cat in CAT.values():
        jobs = [j for j in J if j["cat"]["slug"] == cat["slug"] and j["level"] != "internship"]
        if jobs:
            rows.append((cat, len(jobs), avg_pay(jobs), min(j["smin"] for j in jobs), max(j["smax"] for j in jobs)))
    rows.sort(key=lambda r: -r[2])
    trs = "".join(f'<tr><th scope="row"><a href="/{r[0]["slug"]}-jobs-in-kenya/">{r[0]["emoji"]} {r[0]["name"]}</a></th><td>{r[1]}</td><td><b>{ksh(r[2])}</b></td><td>{ksh(r[3])} – {ksh(r[4])}</td></tr>' for r in rows)
    lv = "".join(f'<tr><th scope="row">{v}</th><td>{sum(1 for j in J if j["level"] == k)}</td><td><b>{ksh(avg_pay([j for j in J if j["level"] == k]))}</b></td><td>{ksh(min(j["smin"] for j in J if j["level"] == k))} – {ksh(max(j["smax"] for j in J if j["level"] == k))}</td></tr>' for k, v in D.LEVELS.items())
    lc = "".join(f'<tr><th scope="row"><a href="/jobs-in-{l["slug"]}/">{l["name"]}</a></th><td>{sum(1 for j in J if j["loc"]["slug"] == l["slug"])}</td><td><b>{ksh(avg_pay([j for j in J if j["loc"]["slug"] == l["slug"]]))}</b></td></tr>' for l in LOC.values() if any(j["loc"]["slug"] == l["slug"] for j in J))
    head = '<thead><tr><th>{}</th><th>Jobs</th><th>Average monthly pay</th>{}</tr></thead>'
    body = f'''{hero_small("Salary guide for Kenya", "See typical monthly pay by field, experience level and town, based on the jobs listed on KaziBora.", c)}
<section class="section tight"><div class="wrap"><p class="note-card">Figures are averages of the mid-point of advertised pay ranges on this site{" (demo data until real listings replace it)" if C.SHOW_SAMPLE_NOTICE else ""}. Use them as a guide, not a promise. Internships are listed under experience level.</p>
<h2 class="sec-title sm">By category (excluding internships)</h2><div class="table-wrap"><table class="cmp">{head.format("Category", "<th>Pay range</th>")}<tbody>{trs}</tbody></table></div>
<h2 class="sec-title sm">By experience level</h2><div class="table-wrap"><table class="cmp">{head.format("Level", "<th>Pay range</th>")}<tbody>{lv}</tbody></table></div>
<h2 class="sec-title sm">By town</h2><div class="table-wrap"><table class="cmp">{head.format("Town", "")}<tbody>{lc}</tbody></table></div>
<p>Negotiating an offer? Read <a href="/career-advice/salary-negotiation-in-kenya/">salary negotiation in Kenya</a>.</p></div></section>{cta_band("Find a job that pays what you are worth", "Filter by minimum pay on the job board.", ("Browse jobs", "/jobs/"))}'''
    page("/salary-guide/", "Salary Guide Kenya: Average Monthly Pay by Job & Level | KaziBora", "Salary guide for Kenya: average monthly pay by category, experience level and town, from internships to senior roles. Updated from live KaziBora listings.",
         body, active="tools", crumbs=c, prio="0.8")


# ===================================================================== ADVICE
def build_articles():
    c = crumb(("Career advice", "/career-advice/"))
    tags = []
    for a in ARTICLES:
        if a["tag"] not in tags:
            tags.append(a["tag"])
    first = ARTICLES[0]
    lead = (f'<a class="art-feature" href="/career-advice/{first["slug"]}/"><img src="/assets/img/articles/{first["slug"]}.svg" width="640" height="360" alt=""><div><span class="tag">{esc(first["tag"])}</span><h2>{esc(first["title"])}</h2><p>{esc(first["desc"])}</p><span class="more">Read the guide {ico("arrow", "ico", 16)}</span></div></a>')
    grid = "".join(article_card(a) for a in ARTICLES[1:])
    body = f'''{hero_small("Career advice for Kenyan job seekers", "Practical guides on CVs, interviews, internships, remote work and staying safe from job scams.", c)}
<section class="section tight"><div class="wrap">{lead}<div class="art-grid">{grid}</div></div></section>
{cta_band("Put the advice into practice", "Build your CV, practise interviews and apply to verified jobs.", ("Browse jobs", "/jobs/"), ("Free CV builder", "/cv-builder/"))}'''
    page("/career-advice/", "Career Advice Kenya: CV, Interview & Job Search Guides | KaziBora", "Free career advice for Kenyans: how to write a CV and cover letter, ace interviews, find internships and entry-level jobs, work remotely and avoid job scams.",
         body, active="learn", crumbs=c, prio="0.8", schema=[{"@context": "https://schema.org", "@type": "CollectionPage", "name": "Career advice", "url": url("/career-advice/")}])

    for i, a in enumerate(ARTICLES):
        c = crumb(("Career advice", "/career-advice/"), (a["title"], f"/career-advice/{a['slug']}/"))
        html_body = md(a["body"])
        toc, n = [], [0]

        def addid(m):
            t = re.sub(r"<[^>]+>", "", m.group(1))
            sid = slugify(t)
            toc.append((sid, t))
            return f'<h2 id="{sid}">{m.group(1)}</h2>'
        html_body = re.sub(r"<h2>(.*?)</h2>", addid, html_body)
        toc_html = '<nav class="toc" aria-label="In this article"><h2>In this article</h2><ol>' + "".join(f'<li><a href="#{s}">{t}</a></li>' for s, t in toc) + "</ol></nav>" if len(toc) > 2 else ""
        faq = a.get("faq", [])
        faq_block = ""
        if faq:
            faq_block = '<h2 id="faq">Frequently asked questions</h2><div class="faq">' + "".join(f'<details class="faq-item"><summary>{esc(q)}</summary><div><p>{inline(an)}</p></div></details>' for q, an in faq) + "</div>"
        pub = C.TODAY - __import__("datetime").timedelta(days=4 + i * 5)
        related = [x for x in ARTICLES if x["slug"] != a["slug"]]
        related = sorted(related, key=lambda x: x["tag"] != a["tag"])[:3]
        sch = [{"@context": "https://schema.org", "@type": "Article", "headline": a["title"], "description": a["desc"], "image": url(f"/assets/img/articles/{a['slug']}.svg"),
                "datePublished": pub.isoformat(), "dateModified": C.TODAY.isoformat(), "inLanguage": C.LOCALE,
                "author": {"@type": "Organization", "name": f"{C.SITE_NAME} Editorial Team"}, "publisher": {"@id": C.SITE_URL + "/#org"},
                "mainEntityOfPage": url(f"/career-advice/{a['slug']}/")}]
        if faq:
            sch.append(faq_schema(faq))
        body = f'''<section class="page-hero art-hero"><div class="wrap narrow">{breadcrumbs_html(c)}<span class="tag">{esc(a["tag"])}</span><h1>{esc(a["title"])}</h1><p class="lead">{esc(a["desc"])}</p>
<p class="byline">By {C.SITE_NAME} Editorial Team &middot; {fmt_date(pub)} &middot; {a["read"]} min read</p></div></section>
<section class="section tight"><div class="wrap narrow"><img class="art-cover" src="/assets/img/articles/{a["slug"]}.svg" width="640" height="360" alt="">{toc_html}<article class="prose">{html_body}{faq_block}</article>
<div class="share"><span>Share:</span><a class="btn btn-sm btn-outline" href="https://wa.me/?text={__import__("urllib.parse").parse.quote(a["title"] + " " + url("/career-advice/" + a["slug"] + "/"))}" target="_blank" rel="noopener">WhatsApp</a><button class="btn btn-sm btn-outline" type="button" data-copy="{url("/career-advice/" + a["slug"] + "/")}">Copy link</button></div></div></section>
<section class="section alt"><div class="wrap"><h2 class="sec-title">Keep reading</h2><div class="art-grid">{"".join(article_card(x) for x in related)}</div></div></section>
{cta_band("Ready for your next role?", "Browse verified jobs and apply free.", ("Browse jobs", "/jobs/"))}'''
        page(f"/career-advice/{a['slug']}/", f"{a['title']} | KaziBora", a["desc"], body, active="learn", schema=sch, crumbs=c, prio="0.7", og_type="article",
             og=f"/assets/img/og-image.png")


# ===================================================================== TRAINING
def build_training():
    c = crumb(("Training & courses", "/training/"))
    cards = "".join(f'<div class="course-card"><span class="course-ic">{co[6]}</span><h3>{esc(co[1])}</h3><p class="prov">{esc(co[0])}</p><p>{esc(co[5])}</p><p class="course-meta"><span>{co[2]}</span><span>{esc(co[4])}</span><b>{ksh(co[3])}</b></p>'
                    f'<a class="btn btn-outline btn-sm" href="#enquire" data-course="{esc(co[1])}">Enquire</a></div>' for co in D.COURSES)
    fields = (field("Full name", "name", req=True) + field("Phone / WhatsApp", "phone", "tel", True) + field("Email", "email", "email")
              + field("Course", "course", "select", True, options([(co[1], co[1]) for co in D.COURSES], "Choose a course"), extra='data-course-select') + field("Questions", "message", "textarea"))
    jsonld = [{"@context": "https://schema.org", "@type": "Course", "name": co[1], "description": co[5], "provider": {"@type": "Organization", "name": co[0].replace("Sample: ", "")},
               "offers": {"@type": "Offer", "price": str(co[3]), "priceCurrency": "KES", "category": "Paid"}} for co in D.COURSES[:4]] if False else []
    body = f'''{hero_small("Training & courses for Kenyan careers", "Short, practical courses from training partners that match the skills employers ask for in our job listings.", c)}
<section class="section tight"><div class="wrap"><p class="note-card">{"Demo content: course providers and prices are placeholders until real partners are signed. " if C.SHOW_SAMPLE_NOTICE else ""}KaziBora may earn a referral fee from partners. It never affects the price you pay.</p><div class="course-grid">{cards}</div></div></section>
<section class="section alt" id="enquire"><div class="wrap narrow"><h2 class="sec-title">Enquire about a course</h2><div class="form-card">{form("course-enquiry", fields, "Send enquiry", "A training partner will contact you.")}</div>
<p class="center-link">Run a training institute? <a href="/training-partners/">Become a training partner</a>.</p></div></section>'''
    page("/training/", "Training & Courses in Kenya: Upskill for Jobs | KaziBora", "Find short courses in Kenya that employers want: Excel, digital marketing, web development, customer service, bookkeeping and more. From trusted training partners.",
         body, active="learn", schema=jsonld, crumbs=c, prio="0.7", extra='<script src="/assets/js/tools.js" defer></script>')

    c = crumb(("Training partners", "/training-partners/"))
    fields = (field("Institution name", "institution", req=True) + field("Contact person", "contact", req=True) + field("Email or phone", "contact_info", req=True) + field("Website", "website", "url")
              + field("Course areas", "areas", "textarea", False, "e.g. ICT, finance, hospitality") + field("Partnership interest", "interest", "select", True, options([("Listing", "Course listings"), ("Referral", "Referral partnership"), ("Co-branded", "Co-branded bootcamp"), ("Employer-sponsored", "Employer-sponsored training")], "Choose")))
    body = f'''{hero_small("Partner with KaziBora", "Reach motivated job seekers who are actively looking to upskill, and help them get hired.", c)}
<section class="section"><div class="wrap"><div class="why-grid"><div class="why-card"><span class="why-ic">{ico("users", "ico", 24)}</span><h3>Targeted learners</h3><p>Courses appear beside job categories and in career guides, where learners are ready to act.</p></div>
<div class="why-card"><span class="why-ic">{ico("trend", "ico", 24)}</span><h3>Pay on results</h3><p>Referral commission on enrolments, with optional featured placement.</p></div>
<div class="why-card"><span class="why-ic">{ico("building", "ico", 24)}</span><h3>Employer-linked</h3><p>Connect courses to skills real employers list in their vacancies.</p></div></div></div></section>
<section class="section alt"><div class="wrap narrow"><h2 class="sec-title">Apply to become a partner</h2><div class="form-card">{form("training-partner", fields, "Apply", "We reply within three working days.")}</div></div></section>'''
    page("/training-partners/", "Become a Training Partner | List Courses on KaziBora", "Training providers in Kenya: list your courses on KaziBora and reach job seekers who want to upskill. Referral and featured placement options.", body, active="employers", crumbs=c, prio="0.5")


# ===================================================================== COMPANY / UTILITY
def build_company():
    c = crumb(("About", "/about/"))
    body = f'''{hero_small("About KaziBora", "Kazi bora means &ldquo;better work&rdquo; in Kiswahili. We help Kenyans find safe, verified opportunities and help employers hire with confidence.".replace("&ldquo;", "“").replace("&rdquo;", "”"), c)}
<section class="section"><div class="wrap two-col"><div class="main-col prose"><h2>Our mission</h2><p>Too many Kenyan job seekers lose money and trust to fake adverts. KaziBora exists to change that: every employer is verified, every listing is checked, and job seekers never pay to apply.</p>
<h2>What we focus on</h2><ul><li><strong>Verified Kenyan opportunities</strong> from checked employers.</li><li><strong>Internships and entry-level jobs</strong> for students and fresh graduates.</li><li><strong>Legitimate remote work</strong> screened for scams.</li><li><strong>Career tools</strong>: CV builder, cover letters, interview prep and salary data.</li></ul>
<h2>How we make money</h2><p>Job seekers use KaziBora free. We earn from employer job listings, featured listings and packages, recruitment advertising, optional CV writing services and referral partnerships with training providers. Paid placement never replaces verification.</p>
<h2>Where we are going</h2><p>We begin with opportunities across Kenya, then expand to more remote roles and international opportunities open to Kenyans, always with the same verification promise.</p></div>
<aside class="side-col"><div class="side-card"><h2>Talk to us</h2><p>{PHONE_LINK}<br>{C.CONTACT_LOCATION}</p><a class="btn btn-primary" href="/contact/">Contact us</a></div><div class="side-card"><h2>Hiring?</h2><a class="btn btn-outline" href="/employers/">Employer solutions</a></div></aside></div></section>'''
    page("/about/", "About KaziBora: Verified Jobs & Careers Platform in Kenya", "KaziBora connects Kenyan job seekers with verified employers. Learn about our mission, verification promise and how we make money.", body, crumbs=c, prio="0.5",
         schema=[{"@context": "https://schema.org", "@type": "AboutPage", "name": "About KaziBora", "url": url("/about/")}])

    c = crumb(("Contact", "/contact/"))
    fields = field("Your name", "name", req=True) + field("Email or phone", "contact", req=True) + field("I am a...", "who", "select", False, options([(v, v) for v in ("Job seeker", "Employer", "Training provider", "Other")], "Choose")) + field("Message", "message", "textarea", True)
    email_li = f'<li>{ico("mail", "ico", 18)} <a href="mailto:{C.CONTACT_EMAIL}">{C.CONTACT_EMAIL}</a></li>' if C.CONTACT_EMAIL else ""
    body = f'''{hero_small("Contact KaziBora", "Questions about a job, a listing or advertising? We reply within one working day.", c)}
<section class="section tight"><div class="wrap two-col narrow-form"><div class="main-col"><div class="form-card">{form("contact", fields, "Send message")}</div></div>
<aside class="side-col"><div class="side-card"><h2>Reach us directly</h2><ul class="link-list"><li>{ico("phone", "ico", 18)} {PHONE_LINK}</li><li>{ico("chat", "ico", 18)} <a href="https://wa.me/{C.WHATSAPP_NUMBER}" target="_blank" rel="noopener">WhatsApp chat</a></li>{email_li}<li>{ico("pin", "ico", 18)} {C.CONTACT_LOCATION}</li></ul><p class="mini">Mon to Fri, 8:00am - 5:00pm EAT</p></div></aside></div></section>'''
    page("/contact/", "Contact KaziBora | Support for Job Seekers & Employers", f"Contact KaziBora by phone, WhatsApp or form. Help for job seekers, employers and training partners in Kenya. Call {C.CONTACT_PHONE_DISPLAY}.", body, crumbs=c, prio="0.5",
         schema=[{"@context": "https://schema.org", "@type": "ContactPage", "name": "Contact KaziBora", "url": url("/contact/")}])

    c = crumb(("Job alerts", "/job-alerts/"))
    fields = (field("Email or WhatsApp number", "contact", req=True) + field("What are you looking for?", "keywords", ph="e.g. accountant, internship, remote")
              + field("Category", "category", "select", False, options([(x["name"], x["name"]) for x in CAT.values()], "Any category")) + field("Location", "location", "select", False, options([(x["name"], x["name"]) for x in LOC.values()] + [("Remote", "Remote")], "Anywhere in Kenya"))
              + field("Experience level", "level", "select", False, options([(v, v) for v in D.LEVELS.values()], "Any level")))
    body = f'''{hero_small("Free job alerts", "Get verified jobs that match your search, straight to your inbox or WhatsApp. No spam, unsubscribe any time.", c)}
<section class="section tight"><div class="wrap narrow"><div class="form-card">{form("job-alert-full", fields, "Create my alert", "We only send verified jobs. You can stop alerts at any time.")}</div></div></section>'''
    page("/job-alerts/", "Free Job Alerts in Kenya | Email & WhatsApp | KaziBora", "Create a free job alert and get verified jobs in Kenya that match your skills, location and experience level by email or WhatsApp.", body, active="jobs", crumbs=c, prio="0.6")

    c = crumb(("Saved jobs", "/saved-jobs/"))
    body = f'''{hero_small("Your saved jobs", "Jobs you have saved on this device. Saved jobs are stored in your browser only.", c)}
<section class="section tight"><div class="wrap"><div id="saved-list" class="job-list"></div><p class="empty" id="saved-empty" hidden>You have not saved any jobs yet. Tap the heart on a job to save it here. <a href="/jobs/">Browse jobs</a>.</p></div></section>'''
    page("/saved-jobs/", "Saved Jobs | KaziBora", "Your saved jobs on KaziBora.", body, active="jobs", crumbs=c, noindex=True)

    legal_note = '<p class="note-card">This is a template for a new platform. Have a qualified Kenyan lawyer review it before launch and update the business details.</p>'
    c = crumb(("Privacy policy", "/privacy/"))
    body = f'''{hero_small("Privacy policy", f"How {C.SITE_NAME} collects, uses and protects your information. Last updated {fmt_date(C.TODAY)}.", c)}
<section class="section tight"><div class="wrap narrow prose">{legal_note}<h2>Information we collect</h2><p>Information you submit through forms (name, contact details, CV and application messages), basic usage data and, only if you accept cookies, analytics data. The CV builder and cover letter tools run in your browser and your entries are not sent to our servers.</p>
<h2>How we use it</h2><p>To deliver applications to employers, process employer registrations and payments, send job alerts you asked for, prevent fraud and improve the service.</p>
<h2>Sharing</h2><p>We share your application only with the employer you applied to. We do not sell personal data. Service providers (hosting, forms, analytics) process data on our behalf.</p>
<h2>Your rights</h2><p>Under the Kenya Data Protection Act, 2019 you may ask to access, correct or delete your data. Contact us on {PHONE_LINK} or through the <a href="/contact/">contact form</a>.</p>
<h2>Cookies</h2><p>We use essential storage for features such as saved jobs. Analytics and advertising cookies load only after you give consent.</p><h2>Security</h2><p>We use HTTPS and limit access to personal data. No online service is completely risk-free.</p></div></section>'''
    page("/privacy/", "Privacy Policy | KaziBora", "How KaziBora collects, uses and protects personal information in line with the Kenya Data Protection Act, 2019.", body, crumbs=c, prio="0.3")

    c = crumb(("Terms of use", "/terms/"))
    body = f'''{hero_small("Terms of use", f"Rules for using {C.SITE_NAME}. Last updated {fmt_date(C.TODAY)}.", c)}
<section class="section tight"><div class="wrap narrow prose">{legal_note}<h2>Using the platform</h2><p>You agree to use KaziBora lawfully and honestly. Job seekers must provide accurate information. Employers must post genuine vacancies.</p>
<h2>No fees for job seekers</h2><p>Employers must never charge candidates for applications, interviews, training, uniforms or medicals. Breaching this rule leads to removal and a ban.</p>
<h2>Employer listings and payments</h2><p>Listings are published after verification and payment. Fees are stated in Kenya shillings. Refund terms are on the <a href="/employers/pricing/">pricing page</a>.</p>
<h2>Content and accuracy</h2><p>We work hard to verify employers but cannot guarantee every vacancy or outcome. Do your own checks and report anything suspicious.</p>
<h2>Liability</h2><p>To the extent permitted by law, KaziBora is not liable for losses arising from hiring decisions or third-party content.</p><h2>Governing law</h2><p>These terms are governed by the laws of Kenya.</p></div></section>'''
    page("/terms/", "Terms of Use | KaziBora", "Terms of use for KaziBora, the Kenyan jobs and careers platform: rules for job seekers, employers and partners.", body, crumbs=c, prio="0.3")

    c = crumb(("Sitemap", "/sitemap/"))
    sec = lambda t, links: f'<div><h2>{t}</h2><ul>' + "".join(f'<li><a href="{h}">{n}</a></li>' for n, h in links) + "</ul></div>"
    body = f'''{hero_small("Sitemap", "Every section of KaziBora in one place.", c)}<section class="section tight"><div class="wrap sitemap-grid">
{sec("Jobs", [("All jobs", "/jobs/"), ("Internships", "/internships/"), ("Entry-level jobs", "/entry-level-jobs/"), ("Remote jobs", "/remote-jobs/"), ("Employer directory", "/employers/directory/"), ("Saved jobs", "/saved-jobs/")])}
{sec("Categories", [(x["name"], f'/{x["slug"]}-jobs-in-kenya/') for x in CAT.values()])}
{sec("Locations", [(f'Jobs in {x["name"]}', f'/jobs-in-{x["slug"]}/') for x in LOC.values()])}
{sec("Career tools", [("CV builder", "/cv-builder/"), ("Cover letter generator", "/cover-letter-generator/"), ("Interview prep", "/interview-prep/"), ("Scam checker", "/scam-checker/"), ("Salary guide", "/salary-guide/"), ("CV writing service", "/cv-writing-service/")])}
{sec("Career advice", [(a["title"], f'/career-advice/{a["slug"]}/') for a in ARTICLES])}
{sec("Employers", [("Employer home", "/employers/"), ("Post a job", "/employers/post-a-job/"), ("Pricing", "/employers/pricing/"), ("Register", "/employers/register/"), ("Advertising", "/employers/advertising/"), ("Training partners", "/training-partners/")])}
{sec("Company", [("About", "/about/"), ("How we verify", "/verified-jobs/"), ("Contact", "/contact/"), ("Report a job", "/report-scam/"), ("Privacy", "/privacy/"), ("Terms", "/terms/")])}
</div></section>'''
    page("/sitemap/", "Sitemap | KaziBora", "Browse every section of KaziBora: jobs, categories, locations, career tools, advice and employer services.", body, crumbs=c, prio="0.3")

    # thank-you + 404
    body = f'''<section class="section center-page"><div class="wrap narrow center"><span class="big-ic ok">{ico("check", "ico", 40)}</span><h1>Thank you!</h1><p class="lead">We have received your submission and will be in touch soon if a reply is needed.</p>
<p><a class="btn btn-primary" href="/jobs/">Browse jobs</a> <a class="btn btn-outline" href="/">Back to home</a></p></div></section>'''
    page("/thank-you/", "Thank you | KaziBora", "Your submission was received.", body, noindex=True)
    body = f'''<section class="section center-page"><div class="wrap narrow center"><span class="big-ic">{ico("search", "ico", 40)}</span><h1>Page not found</h1><p class="lead">That page may have moved or the job may have closed. Try a search or browse our latest verified jobs.</p>
<form class="hero-search simple" action="/jobs/" method="get" role="search"><div class="hs-field">{ico("search", "ico", 20)}<input name="q" type="search" placeholder="Search jobs" aria-label="Search jobs"></div><button class="btn btn-primary btn-lg" type="submit">Search</button></form>
<p><a class="btn btn-outline" href="/">Home</a> <a class="btn btn-outline" href="/internships/">Internships</a> <a class="btn btn-outline" href="/remote-jobs/">Remote jobs</a></p></div></section>'''
    page("/404.html", "Page not found | KaziBora", "Page not found.", body, noindex=True)


def build_all():
    build_cv()
    build_interview()
    build_safety()
    build_salary()
    build_articles()
    build_training()
    build_company()
