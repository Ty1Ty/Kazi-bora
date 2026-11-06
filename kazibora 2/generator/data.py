"""Placeholder content: fictional employers, sample jobs, categories, articles, interview questions."""

CATEGORIES = [
    ("ict", "ICT & Software", "💻", "Software development, IT support, data, networks and cybersecurity roles across Kenya's growing tech scene."),
    ("finance", "Accounting & Finance", "📊", "Accountants, auditors, credit officers and finance graduates, from Big-4 style audit trainees to SACCO and microfinance roles."),
    ("health", "Healthcare & Medical", "🩺", "Nurses, clinical officers, pharmacy technologists and hospital administrators in public, private and mission facilities."),
    ("education", "Education & Training", "🎓", "Teaching, tutoring, curriculum and corporate training jobs in schools, colleges and training institutes."),
    ("engineering", "Engineering & Construction", "🏗️", "Civil, electrical and solar engineering plus site and technical roles on building and infrastructure projects."),
    ("sales", "Sales & Marketing", "📣", "Sales executives, retail supervisors, digital marketers and brand roles, many with commission on top of base pay."),
    ("hospitality", "Hospitality & Tourism", "🏨", "Hotels, lodges, safari and restaurant jobs from the coast to the Rift Valley and Lamu."),
    ("ngo", "NGO & Development", "🤝", "Programme, monitoring and evaluation, WASH and community roles with non-profits and development partners."),
    ("customer", "Customer Service & BPO", "🎧", "Contact-centre, customer care and remote support roles, a common first step for many graduates."),
    ("logistics", "Logistics & Supply Chain", "🚚", "Port, freight, fleet, warehousing and procurement jobs linked to Mombasa, Nairobi and the regional corridors."),
    ("agriculture", "Agriculture & Agribusiness", "🌱", "Agronomy, extension, agri-sales and farm-management jobs with agritech firms and cooperatives."),
    ("admin", "Admin & Office", "🗂️", "Receptionists, office administrators, virtual assistants and executive support roles."),
    ("legal", "Legal & Compliance", "⚖️", "Legal assistants, compliance officers, paralegals and law-firm internships."),
    ("creative", "Creative & Media", "🎨", "Graphic design, video, writing and social media jobs with agencies and remote clients."),
]

LOCATIONS = [
    ("nairobi", "Nairobi", "Nairobi County", "Kenya's capital and biggest job market, with head offices, tech, NGOs and the regional headquarters of many multinationals."),
    ("mombasa", "Mombasa", "Mombasa County", "The coastal hub for port operations, shipping, tourism and hospitality."),
    ("kisumu", "Kisumu", "Kisumu County", "Western Kenya's lakeside city, growing fast in health, trade and digital services."),
    ("nakuru", "Nakuru", "Nakuru County", "A Rift Valley centre for agribusiness, hospitality, manufacturing and tourism."),
    ("eldoret", "Eldoret", "Uasin Gishu County", "North Rift's commercial centre, strong in agriculture, construction and education."),
    ("thika", "Thika", "Kiambu County", "An industrial and retail town on Nairobi's doorstep with factories, SACCOs and water projects."),
    ("lamu", "Lamu", "Lamu County", "A heritage destination with eco-lodges, dhow tourism and community enterprises."),
]

# slug, name, industry, location slug, size, verified, about
EMPLOYERS = [
    ("savanna-ledger", "Savanna Ledger Advisory", "Accounting & Advisory", "nairobi", "51-200 staff", True,
     "Savanna Ledger Advisory is a sample audit, tax and business advisory firm serving growing Kenyan companies and SACCOs."),
    ("pwani-port-logistics", "Pwani Port Logistics", "Freight & Logistics", "mombasa", "201-500 staff", True,
     "Pwani Port Logistics is a sample clearing and forwarding company moving cargo through the Port of Mombasa to the region."),
    ("kilimo-smart-agritech", "Kilimo Smart Agritech", "Agritech", "nakuru", "51-200 staff", True,
     "Kilimo Smart Agritech is a sample agritech company supplying inputs and advice to smallholder farmers across the Rift Valley."),
    ("jua-solar-kenya", "Jua Solar Kenya", "Renewable Energy", "nairobi", "51-200 staff", True,
     "Jua Solar Kenya is a sample solar installer serving homes, schools and small businesses."),
    ("maisha-health-network", "Maisha Health Network", "Healthcare", "kisumu", "201-500 staff", True,
     "Maisha Health Network is a sample group of private clinics and a referral hospital in western Kenya."),
    ("elimu-bora-academy", "Elimu Bora Academy", "Education", "nairobi", "51-200 staff", True,
     "Elimu Bora Academy is a sample primary school and corporate training provider."),
    ("ziwa-digital-labs", "Ziwa Digital Labs", "Software & Digital", "kisumu", "11-50 staff", True,
     "Ziwa Digital Labs is a sample software studio building web and mobile products for East African clients."),
    ("rift-valley-hotels", "Rift Valley Hotels & Safaris", "Hospitality", "nakuru", "201-500 staff", True,
     "Rift Valley Hotels & Safaris is a sample hotel group with lodges and safari circuits across the Rift Valley."),
    ("nyota-microfinance", "Nyota Microfinance", "Financial Services", "nairobi", "201-500 staff", True,
     "Nyota Microfinance is a sample deposit-taking microfinance institution with branches in several towns."),
    ("baraka-construction", "Baraka Construction & Engineering", "Construction", "eldoret", "201-500 staff", False,
     "Baraka Construction & Engineering is a sample contractor delivering roads, housing and institutional buildings."),
    ("twiga-retail-group", "Twiga Retail Group", "Retail & FMCG", "nairobi", "501-1000 staff", True,
     "Twiga Retail Group is a sample supermarket and wholesale chain with outlets in Nairobi and surrounding towns."),
    ("mto-water-trust", "Mto Water Trust", "NGO", "thika", "11-50 staff", True,
     "Mto Water Trust is a sample non-profit delivering clean water and sanitation to peri-urban communities."),
    ("harambee-youth-foundation", "Harambee Youth Foundation", "NGO", "nairobi", "51-200 staff", True,
     "Harambee Youth Foundation is a sample non-profit running youth skills and livelihoods programmes."),
    ("pembe-creative-studio", "Pembe Creative Studio", "Creative Agency", "nairobi", "11-50 staff", True,
     "Pembe Creative Studio is a sample agency producing brand, video and social content for local and regional clients."),
    ("lamu-coast-ecolodges", "Lamu Coast Eco-Lodges", "Tourism", "lamu", "51-200 staff", False,
     "Lamu Coast Eco-Lodges is a sample collection of boutique lodges working with local communities."),
    ("mlima-telecom", "Mlima Telecom Services", "Telecommunications", "nairobi", "501-1000 staff", True,
     "Mlima Telecom Services is a sample mobile and fibre operator serving consumers and businesses."),
    ("northwind-remote", "Northwind Remote Support", "Remote Services", "nairobi", "51-200 staff", True,
     "Northwind Remote Support is a sample international company hiring Kenya-based staff for remote customer and engineering roles."),
    ("afrilance-global", "Afrilance Global", "Remote Talent", "nairobi", "11-50 staff", True,
     "Afrilance Global is a sample remote talent company matching African freelancers with overseas clients."),
    ("mwangaza-legal", "Mwangaza Legal Partners", "Legal Services", "nairobi", "11-50 staff", True,
     "Mwangaza Legal Partners is a sample commercial law firm advising on corporate, property and compliance matters."),
    ("safiri-cargo", "Safiri Cargo Air Services", "Air Cargo", "nairobi", "51-200 staff", True,
     "Safiri Cargo Air Services is a sample air-freight handler operating from JKIA."),
]

LEVELS = {"internship": "Internship", "entry": "Entry-level", "mid": "Mid-level", "senior": "Senior"}

# title, employer, category, location, type, level, sal_min, sal_max, remote, posted_days_ago, deadline_days, featured, urgent
JOBS = [
    ("Senior Accountant", "savanna-ledger", "finance", "nairobi", "Full-time", "senior", 140000, 190000, False, 1, 24, True, False),
    ("Graduate Trainee - Audit", "savanna-ledger", "finance", "nairobi", "Full-time", "entry", 45000, 60000, False, 2, 20, False, False),
    ("Accounts Assistant", "nyota-microfinance", "finance", "nairobi", "Full-time", "entry", 40000, 55000, False, 3, 18, False, False),
    ("Credit Officer", "nyota-microfinance", "finance", "thika", "Full-time", "mid", 60000, 85000, False, 5, 21, False, False),
    ("Remote Part-time Bookkeeper", "afrilance-global", "finance", "nairobi", "Part-time", "entry", 35000, 55000, True, 4, 26, False, False),
    ("Port Operations Intern", "pwani-port-logistics", "logistics", "mombasa", "Internship", "internship", 15000, 20000, False, 2, 16, False, False),
    ("Supply Chain Officer", "pwani-port-logistics", "logistics", "mombasa", "Full-time", "mid", 80000, 110000, False, 1, 28, True, False),
    ("Fleet Coordinator", "safiri-cargo", "logistics", "nairobi", "Full-time", "mid", 70000, 95000, False, 6, 19, False, False),
    ("Customs Clearing Trainee", "safiri-cargo", "logistics", "nairobi", "Full-time", "entry", 35000, 50000, False, 3, 22, False, False),
    ("Agronomist", "kilimo-smart-agritech", "agriculture", "nakuru", "Full-time", "mid", 75000, 100000, False, 4, 25, False, False),
    ("Agribusiness Sales Intern", "kilimo-smart-agritech", "agriculture", "nakuru", "Internship", "internship", 12000, 18000, False, 5, 15, False, False),
    ("Farmer Training Officer", "kilimo-smart-agritech", "agriculture", "eldoret", "Contract", "entry", 45000, 60000, False, 7, 20, False, False),
    ("Solar Installation Technician", "jua-solar-kenya", "engineering", "nairobi", "Full-time", "entry", 40000, 60000, False, 2, 17, False, True),
    ("Electrical Engineer (Solar)", "jua-solar-kenya", "engineering", "nairobi", "Full-time", "mid", 110000, 150000, False, 6, 30, False, False),
    ("Civil Engineering Intern", "baraka-construction", "engineering", "eldoret", "Internship", "internship", 15000, 20000, False, 3, 14, False, False),
    ("Site Supervisor", "baraka-construction", "engineering", "eldoret", "Full-time", "mid", 85000, 115000, False, 8, 23, False, False),
    ("Registered Nurse", "maisha-health-network", "health", "kisumu", "Full-time", "mid", 65000, 90000, False, 1, 27, False, False),
    ("Clinical Officer", "maisha-health-network", "health", "kisumu", "Full-time", "mid", 70000, 95000, False, 2, 29, True, False),
    ("Pharmaceutical Technologist", "maisha-health-network", "health", "kisumu", "Full-time", "entry", 40000, 55000, False, 5, 21, False, False),
    ("Primary School Teacher", "elimu-bora-academy", "education", "nairobi", "Full-time", "mid", 45000, 65000, False, 4, 26, False, False),
    ("Graduate Teaching Assistant", "elimu-bora-academy", "education", "nairobi", "Part-time", "entry", 25000, 35000, False, 6, 18, False, False),
    ("Corporate Trainer", "elimu-bora-academy", "education", "nairobi", "Contract", "mid", 80000, 120000, False, 9, 31, False, False),
    ("Front-End Developer", "ziwa-digital-labs", "ict", "kisumu", "Full-time", "mid", 90000, 130000, False, 1, 25, True, False),
    ("IT Support Intern", "ziwa-digital-labs", "ict", "kisumu", "Internship", "internship", 15000, 20000, False, 3, 15, False, False),
    ("Junior Data Analyst", "mlima-telecom", "ict", "nairobi", "Full-time", "entry", 55000, 75000, False, 2, 22, False, False),
    ("Network Engineer", "mlima-telecom", "ict", "nairobi", "Full-time", "mid", 100000, 140000, False, 7, 28, False, False),
    ("Customer Care Representative", "mlima-telecom", "customer", "nairobi", "Full-time", "entry", 30000, 42000, False, 1, 12, False, True),
    ("Remote Customer Support Agent", "northwind-remote", "customer", "nairobi", "Full-time", "entry", 50000, 75000, True, 2, 24, True, False),
    ("Remote Virtual Assistant", "afrilance-global", "admin", "nairobi", "Contract", "entry", 40000, 65000, True, 3, 27, False, False),
    ("Remote Content Writer", "afrilance-global", "creative", "nairobi", "Contract", "entry", 35000, 60000, True, 5, 25, False, False),
    ("Remote Social Media Manager", "afrilance-global", "creative", "nairobi", "Contract", "mid", 60000, 90000, True, 6, 23, False, False),
    ("Remote Full-Stack Developer", "northwind-remote", "ict", "nairobi", "Full-time", "mid", 180000, 260000, True, 4, 30, True, False),
    ("Hotel Front Office Intern", "rift-valley-hotels", "hospitality", "nakuru", "Internship", "internship", 12000, 16000, False, 2, 13, False, False),
    ("Sous Chef", "rift-valley-hotels", "hospitality", "nakuru", "Full-time", "mid", 65000, 90000, False, 6, 20, False, False),
    ("Lodge Host (Entry-level)", "lamu-coast-ecolodges", "hospitality", "lamu", "Full-time", "entry", 30000, 40000, False, 5, 19, False, False),
    ("Lodge Manager", "lamu-coast-ecolodges", "hospitality", "lamu", "Full-time", "senior", 130000, 170000, False, 8, 32, False, False),
    ("Retail Store Supervisor", "twiga-retail-group", "sales", "nairobi", "Full-time", "mid", 55000, 75000, False, 3, 21, False, False),
    ("Sales Executive (Entry-level)", "twiga-retail-group", "sales", "thika", "Full-time", "entry", 30000, 45000, False, 1, 14, False, True),
    ("Digital Marketing Officer", "pembe-creative-studio", "sales", "nairobi", "Full-time", "mid", 70000, 95000, False, 4, 24, False, False),
    ("Graphic Design Intern", "pembe-creative-studio", "creative", "nairobi", "Internship", "internship", 12000, 18000, False, 2, 16, False, False),
    ("Video Editor", "pembe-creative-studio", "creative", "nairobi", "Contract", "mid", 60000, 90000, False, 7, 22, False, False),
    ("Programme Officer - Youth Livelihoods", "harambee-youth-foundation", "ngo", "nairobi", "Full-time", "mid", 95000, 130000, False, 1, 26, True, False),
    ("Community Mobilisation Intern", "harambee-youth-foundation", "ngo", "kisumu", "Internship", "internship", 12000, 15000, False, 4, 17, False, False),
    ("WASH Project Assistant", "mto-water-trust", "ngo", "thika", "Contract", "entry", 45000, 60000, False, 3, 20, False, False),
    ("Monitoring & Evaluation Officer", "mto-water-trust", "ngo", "thika", "Full-time", "mid", 90000, 120000, False, 6, 25, False, False),
    ("Legal Assistant", "mwangaza-legal", "legal", "nairobi", "Full-time", "entry", 40000, 55000, False, 2, 19, False, False),
    ("Compliance Officer", "mwangaza-legal", "legal", "nairobi", "Full-time", "mid", 95000, 130000, False, 5, 27, False, False),
    ("Legal Intern", "mwangaza-legal", "legal", "nairobi", "Internship", "internship", 12000, 18000, False, 3, 15, False, False),
    ("Office Administrator", "jua-solar-kenya", "admin", "nairobi", "Full-time", "entry", 32000, 45000, False, 4, 18, False, False),
]

# Category-specific building blocks used to compose each job description
CAT_RESP = {
    "ict": ["Design, build and maintain reliable software or systems for internal teams and customers", "Troubleshoot incidents, document fixes and share lessons with the team", "Write clean, tested and well-documented work that others can maintain", "Collaborate with product, design and operations colleagues in short delivery cycles", "Keep security, data protection and backup practices front of mind", "Support users and stakeholders with clear, friendly communication"],
    "finance": ["Prepare accurate ledgers, reconciliations and monthly management reports", "Support statutory filings and maintain a clear audit trail", "Review transactions for errors, anomalies and policy breaches", "Work with auditors, tax advisers and finance leadership on deadlines", "Maintain confidential client and company records", "Recommend practical improvements to financial controls and workflows"],
    "health": ["Deliver safe, patient-centred care in line with national clinical guidelines", "Keep accurate patient records and follow infection-prevention protocols", "Work with doctors, nurses and pharmacy teams on patient plans", "Educate patients and families on treatment, prevention and follow-up", "Take part in outreach, screening and community health activities", "Join shift rotations and support continuous quality improvement"],
    "education": ["Plan and deliver engaging lessons or training sessions aligned to the curriculum", "Assess learner progress and give constructive feedback", "Maintain a safe, inclusive and well-organised learning space", "Communicate regularly with parents, learners or client organisations", "Prepare learning materials and keep records up to date", "Take part in staff meetings and professional development"],
    "engineering": ["Carry out installation, supervision or design work to approved standards", "Follow site safety rules and ensure the team uses protective equipment", "Prepare progress reports, measurements and material requests", "Coordinate with suppliers, subcontractors and clients on schedules", "Inspect completed work and resolve snags quickly", "Maintain accurate drawings, logs and compliance records"],
    "sales": ["Meet monthly sales or campaign targets through consistent activity", "Build lasting relationships with customers and partners", "Track leads, orders and results in simple reports", "Present products clearly and handle objections honestly", "Support promotions, merchandising and in-store or online campaigns", "Share customer feedback to help improve the offer"],
    "hospitality": ["Welcome guests warmly and deliver consistently excellent service", "Follow food-safety, hygiene and health-and-safety standards", "Coordinate with housekeeping, kitchen and front-office teams", "Handle guest requests and complaints calmly and professionally", "Support bookings, billing and daily reports", "Represent the property's values and local culture with pride"],
    "ngo": ["Support the planning and delivery of community programmes and partner activities", "Collect, clean and report programme data accurately and on time", "Engage communities, local government and partners respectfully", "Prepare donor-ready narrative and financial updates", "Follow safeguarding, anti-fraud and accountability policies", "Travel to project sites as required"],
    "customer": ["Respond to customers by phone, chat or email with accuracy and empathy", "Resolve queries at first contact wherever possible", "Log every interaction clearly in the support system", "Escalate complex issues with the right context", "Meet service-level targets for response and quality", "Share customer insights to improve products and processes"],
    "logistics": ["Plan, track and coordinate shipments, vehicles or stock movements", "Prepare and verify shipping, customs and delivery documents", "Liaise with agents, drivers, port and warehouse teams", "Keep inventory and delivery records accurate", "Identify delays early and propose workable solutions", "Follow safety, compliance and cost-control procedures"],
    "agriculture": ["Support farmers with practical advice on crops, inputs and good practice", "Run demonstration plots, field days and training sessions", "Collect field data and report on adoption and yields", "Build trust with farmer groups, cooperatives and local leaders", "Promote products and services responsibly and honestly", "Travel regularly within the assigned area"],
    "admin": ["Manage calendars, correspondence and documents with care", "Prepare simple reports, minutes and presentations", "Coordinate meetings, travel and office logistics", "Keep files and records organised and confidential", "Handle visitors, calls and messages professionally", "Support colleagues across teams with day-to-day requests"],
    "legal": ["Draft, review and file agreements, notices and other legal documents", "Research legislation, case law and regulatory guidance", "Support due-diligence and compliance reviews", "Maintain organised matter files and deadlines", "Liaise with courts, registries and clients as directed", "Protect client confidentiality at all times"],
    "creative": ["Produce original, on-brief creative work to agreed deadlines", "Adapt content for different platforms and audiences", "Take feedback well and iterate quickly", "Keep assets, files and style guides organised", "Support campaigns with ideas, scheduling and reporting", "Stay current with tools, trends and good practice"],
}
CAT_SKILLS = {
    "ict": "Practical skills in the relevant stack or tools, plus problem solving and clear written communication",
    "finance": "Strong numeracy, attention to detail and working knowledge of accounting software such as QuickBooks, Sage or Excel",
    "health": "Valid registration with the relevant Kenyan professional council and a calm, caring approach",
    "education": "Strong communication, patience and a genuine interest in how people learn",
    "engineering": "Technical competence for the role and a strong safety mindset; registration with the relevant board is an advantage",
    "sales": "Confident communication, resilience and comfort working towards targets",
    "hospitality": "Warm, professional manner and willingness to work shifts, weekends and holidays",
    "ngo": "Good report-writing, data and stakeholder skills; experience with community-based work is an advantage",
    "customer": "Excellent spoken and written English and Kiswahili, typing speed and a patient attitude",
    "logistics": "Organisation, document accuracy and familiarity with logistics or inventory systems",
    "agriculture": "Field-based experience, strong local-language communication and willingness to travel",
    "admin": "Excellent organisation, Microsoft Office or Google Workspace skills and discretion",
    "legal": "Careful drafting, research ability and integrity; admission or progress toward admission to the Kenyan bar is an advantage",
    "creative": "A portfolio or sample work, creative curiosity and reliable delivery",
}
LEVEL_REQ = {
    "internship": "Currently enrolled in, or a recent graduate of, a relevant certificate, diploma or degree programme",
    "entry": "Certificate, diploma or degree in a relevant field with 0-2 years' experience; recent graduates are welcome to apply",
    "mid": "Diploma or degree in a relevant field with 3-5 years' experience in a similar role",
    "senior": "Degree in a relevant field (professional qualifications an advantage) with 7+ years' experience including team leadership",
}
BENEFITS = [
    "Competitive monthly pay, reviewed annually", "Medical cover after probation", "Paid leave and public holidays",
    "Mentorship and on-the-job training", "Clear path to a permanent role after a strong performance review",
    "Training allowance for approved courses", "Friendly, collaborative team", "Transport or lunch allowance",
]

ARTICLES = [
    {
        "slug": "how-to-write-a-cv-in-kenya", "title": "How to Write a CV in Kenya That Gets Interviews",
        "desc": "A practical guide to writing a clear, one-to-two page Kenyan CV: layout, what to include, what to leave out, and mistakes recruiters see every day.",
        "tag": "CV & Cover Letters", "read": 6, "emoji": "📄",
        "body": """Recruiters in Kenya often review dozens of CVs for a single vacancy, so yours has to be easy to scan in under a minute. The good news is that a strong CV follows a simple, repeatable structure.

## Keep it to one or two pages
Entry-level and internship candidates should stay on **one page**. Experienced professionals can use two. Anything longer rarely gets read in full.

## The structure that works
- **Contact details:** full name, phone number, professional email address, and your town or county. A LinkedIn link is a bonus.
- **Personal profile:** three or four lines describing who you are, what you do well and the role you want.
- **Work experience:** list your most recent job first. Under each role, write three to five bullet points that start with action verbs and show results.
- **Education:** highest qualification first, with the institution and year of completion.
- **Skills:** list tools, software and languages that match the job advert.
- **Referees:** two professional referees with their name, job title, organisation and phone number. Always ask for their permission first.

## Write results, not duties
Instead of "Responsible for sales", write "Increased monthly shop sales by 18% over six months by introducing a customer follow-up list". Numbers make your work believable.

## Tailor it for each job
Read the advert carefully and mirror its key words honestly. Many employers use applicant tracking tools or quick keyword scans before a person looks at your CV.

## No experience? Use what you have
Include internships, industrial attachments, volunteering, class projects, church or community leadership and any short courses. Employers hiring at entry level know you are just starting out.

## Mistakes to avoid
- An unprofessional email address
- Spelling errors and inconsistent fonts
- Sharing sensitive details like your ID number or bank information
- Long paragraphs instead of short bullet points
- Photos are optional; only include one if the advert asks

Ready to put this into practice? Our free [CV Builder](/cv-builder/) lets you fill in your details, choose a template and download a clean PDF in minutes.""",
        "faq": [("Should I put a photo on my CV in Kenya?", "Only if the employer asks for one. Most recruiters care more about your skills and results than a photo."),
                ("How many referees should I list?", "Two professional referees are normal. Choose people who have supervised your work and tell them to expect a call.")],
    },
    {
        "slug": "how-to-spot-fake-job-adverts-in-kenya", "title": "How to Spot Fake Job Adverts in Kenya (and Stay Safe)",
        "desc": "Learn the red flags of job scams in Kenya, from upfront fees to WhatsApp-only recruiters, and the steps to verify an employer before you apply or travel.",
        "tag": "Safety & Scams", "read": 6, "emoji": "🛡️",
        "body": """Job scams prey on people who are working hard to find a break. Knowing the warning signs protects your money, your identity and your safety.

## Red flags that should stop you
- **You are asked to pay.** A genuine employer does not charge for interviews, medical tests, uniforms, registration, visas or "processing". Payment before a job is the most common scam.
- **Vague company details.** No physical address, no website, or a website created last week.
- **Free email addresses.** Be careful when a "big company" recruits from a personal Gmail or Yahoo address.
- **Pressure and secrecy.** "Reply in one hour", "tell no one" or "limited slots" are tactics to stop you thinking.
- **Too good to be true.** A very high salary for no experience or a "work from your phone" job paying far above the market.
- **Odd interview arrangements.** Interviews in homes, hotels, parked cars or by chat message only, with no video or phone call.
- **Requests for sensitive data too early.** Bank PINs, passwords and copies of your ID before an offer is not normal.

## How to verify an employer
1. Search for the company's official website and find the same vacancy on its **careers page**.
2. Call the company using a number you found independently, not the one in the message.
3. Check the business name on the official registry and look for real reviews and news.
4. Confirm the recruiter on the company's official social media or LinkedIn page.
5. Ask for the offer in writing and read it carefully before you sign.

## Overseas job offers need extra care
Jobs abroad are a popular scam target. Verify any agency with the relevant Kenyan authorities before sending money or documents, and never pay for a visa through an individual's personal phone number.

## If you have been targeted
Stop all contact, keep screenshots and receipts, tell someone you trust and report it to the police and the platform where you saw the advert. You can also use our [report form](/report-scam/).

Not sure about an advert? Try the [KaziBora Scam Checker](/scam-checker/) for a quick risk score.""",
        "faq": [("Is it normal to pay a fee to apply for a job in Kenya?", "No. Genuine employers do not charge candidates to apply, interview or be hired. Treat any request for payment as a major red flag."),
                ("What should I do if I already sent money?", "Stop paying immediately, keep every receipt and message, and report to the police and the platform where you found the advert.")],
    },
    {
        "slug": "common-interview-questions-and-answers-kenya", "title": "10 Common Interview Questions and How to Answer Them",
        "desc": "Prepare for Kenyan job interviews with ten of the most common questions, what employers really want to hear, and a simple structure for strong answers.",
        "tag": "Interview Preparation", "read": 7, "emoji": "🎤",
        "body": """Most interviews in Kenya, from banks to NGOs to start-ups, circle around the same handful of questions. Preparing a clear answer to each one lets you stay calm and sound confident.

## A simple framework: Situation, Task, Action, Result
For any question that asks for an example, use the **STAR method**. Briefly set the *situation*, explain your *task*, describe the *action* you took and finish with the *result*.

## The ten questions
**1. Tell us about yourself.** Give a 60-90 second summary: who you are, your key experience or studies, and why this role fits.

**2. Why do you want to work here?** Show you have researched the organisation. Mention its work, values or recent news.

**3. What are your strengths?** Choose two strengths relevant to the job and back each with a short example.

**4. What is your biggest weakness?** Pick a real, minor weakness and explain what you are doing to improve it.

**5. Describe a time you worked in a team.** Highlight your role, how you handled disagreements and what the team achieved.

**6. Tell us about a time you solved a problem.** Use STAR and finish with a measurable result if possible.

**7. How do you handle pressure and deadlines?** Describe how you prioritise, communicate and stay organised.

**8. Where do you see yourself in five years?** Show ambition that fits the organisation, such as growing your skills and taking on more responsibility.

**9. Why should we hire you?** Link your top skills directly to the needs in the job advert.

**10. What are your salary expectations?** Research typical pay for the role, give a realistic range and stay open to discussion.

## Before the interview
- Read the job advert again and prepare examples for each requirement.
- Plan your route, or test your internet and camera for online interviews.
- Dress neatly and arrive 15 minutes early.
- Prepare two or three questions to ask the panel.

Practise out loud with our free [Interview Prep Trainer](/interview-prep/), which gives you random questions, a timer and answer tips.""",
        "faq": [("How long should my answer to 'tell us about yourself' be?", "Aim for 60 to 90 seconds covering your background, strengths and why you want this role."),
                ("Is it okay to ask questions at the end of an interview?", "Yes. Asking about team goals, training or success in the first 90 days shows interest and preparation.")],
    },
    {
        "slug": "internships-in-kenya-how-to-find-and-win-one", "title": "Internships in Kenya: How to Find and Win One",
        "desc": "Where to look for internships and attachments in Kenya, how to apply, what to expect to be paid, and how to turn an internship into a permanent job.",
        "tag": "Internships", "read": 6, "emoji": "🎒",
        "body": """An internship is often the bridge between college and a career. It gives you real experience, references and sometimes a permanent job offer.

## Internship, attachment or graduate trainee?
- **Industrial attachment:** a short placement, often required by your college or university.
- **Internship:** a fixed-term role, usually three to twelve months, for students and recent graduates.
- **Graduate trainee:** a structured development programme at a company, normally for new graduates.

## Where to find opportunities
- Browse verified roles on our [internships page](/internships/).
- Check company careers pages and the career office at your institution.
- Contact small and medium businesses directly; many do not advertise.
- Tell family, lecturers and alumni that you are looking.

## Applying the right way
1. Prepare a one-page CV that highlights your course work, projects and skills.
2. Write a short cover letter explaining what you want to learn and what you can offer. Use our [cover letter generator](/cover-letter-generator/).
3. Follow the application instructions exactly, including subject lines and deadlines.
4. Follow up politely after a week if you hear nothing.

## Stipends and fairness
Some internships pay a stipend, some cover transport and lunch, and some are unpaid. Ask early about hours, duties, supervision and pay. Be cautious if you are asked to pay for the opportunity itself.

## Make the most of it
- Set clear learning goals in the first week.
- Ask for feedback regularly and act on it.
- Keep a record of what you accomplish.
- Build relationships with people across teams.
- Ask for a recommendation letter before you leave.

## Turning an internship into a job
Be reliable, take initiative and solve problems. Tell your supervisor you would like to stay and ask what skills you should build to be considered.""",
        "faq": [("Are internships in Kenya paid?", "It varies. Many offer a stipend or allowances, while some are unpaid. Always clarify pay, hours and supervision before you start."),
                ("When should I start looking for an internship?", "Start three to four months before you want to begin, since many employers recruit in cycles.")],
    },
    {
        "slug": "entry-level-jobs-in-kenya-no-experience", "title": "Entry-Level Jobs in Kenya: How to Get Hired With No Experience",
        "desc": "A realistic plan for landing your first job in Kenya without work experience: roles to target, skills to build, and how to stand out to employers.",
        "tag": "Entry-Level Careers", "read": 6, "emoji": "🚀",
        "body": """Everyone is asked for experience, yet nobody explains how to get it. The answer is to prove you can do the work in other ways.

## Roles that often welcome beginners
- Customer care and call-centre agent
- Sales and retail executive
- Accounts assistant and graduate trainee
- Teaching assistant and tutor
- Office administrator and receptionist
- IT support and junior data analyst
- Community and project assistants with NGOs

Browse current openings on our [entry-level jobs](/entry-level-jobs/) page.

## Build proof of skill
- **Take short courses** in Excel, digital marketing, customer service or coding. See our [training partners](/training/).
- **Do a small project:** build a simple website, run a social page for a local business, or analyse a public dataset.
- **Volunteer** with a school, church, youth group or community organisation and note your results.
- **Create a portfolio** of your best work online.

## Rewrite your CV around transferable skills
Teamwork, communication, reliability, leadership and problem-solving are valuable. Show them with examples from school, sports, clubs or family business.

## Apply smartly
1. Pick roles where you meet at least 60 percent of the requirements.
2. Customise your CV and cover letter for each one.
3. Apply early. Many employers review applications as they arrive.
4. Prepare for interviews with our [Interview Prep Trainer](/interview-prep/).

## Be open to a stepping stone
Your first role may not be perfect. Aim for one where you will learn, get a supervisor who gives feedback and build a good reference.

## Stay safe
Never pay to be hired. If the advert asks for money, walk away and read our guide to [spotting fake job adverts](/how-to-spot-fake-job-adverts-in-kenya/).""",
        "faq": [("Can I get a job in Kenya with no experience?", "Yes. Many employers hire graduates and school leavers for customer care, sales, admin and trainee roles, and train them on the job.")],
    },
    {
        "slug": "remote-jobs-for-kenyans-legitimate-ways-to-start", "title": "Remote Jobs for Kenyans: Legitimate Ways to Get Started",
        "desc": "How to find genuine remote work from Kenya, which skills are in demand, how payment works, and how to avoid common remote-job scams.",
        "tag": "Remote Work", "read": 7, "emoji": "🌍",
        "body": """Remote work lets you earn from Kenya for local or international employers. It also attracts scammers, so careful steps matter.

## Skills in demand for remote work
- Customer support and technical support
- Virtual assistance and administration
- Content writing, editing and transcription
- Web and software development
- Graphic design, video editing and social media management
- Bookkeeping and data entry

## Where genuine remote jobs come from
- Verified listings on our [remote jobs](/remote-jobs/) page
- Established freelancing and remote-work platforms with dispute handling
- Companies that publish openings on their own careers pages
- Referrals from people you trust in your industry

## What you need
- A reliable laptop and backup power
- Stable internet with a backup option such as mobile data
- A quiet place to work during agreed hours
- A professional online profile and portfolio
- Clear written English and strong time management

## Getting paid
Employers and clients commonly pay through bank transfer, mobile money or international payment services. Compare fees and exchange rates before you choose. Keep invoices and records, and ask a qualified adviser about your tax obligations.

## Remote-job red flags
- You are asked to buy equipment from the "employer" with a promise of reimbursement.
- You are sent a cheque or payment and asked to forward part of it.
- The interview is a chat message only, and the offer comes within minutes.
- The employer refuses a contract or asks you to pay for training or software.

## Start small and build up
Take a short contract or part-time role, collect strong reviews and grow your rates. Use our [CV Builder](/cv-builder/) to prepare a CV suited to remote roles that highlights communication and self-management.""",
        "faq": [("Can I work remotely for foreign companies from Kenya?", "Yes, many companies hire Kenya-based workers as contractors or employees. Check the contract, pay terms and your own tax obligations.")],
    },
    {
        "slug": "how-to-write-a-cover-letter-kenya", "title": "How to Write a Cover Letter That Recruiters Actually Read",
        "desc": "A simple four-paragraph cover letter formula for Kenyan job applications, with tips for graduates, career changers and internship applicants.",
        "tag": "CV & Cover Letters", "read": 5, "emoji": "✉️",
        "body": """A cover letter is your chance to explain who you are in your own voice. Keep it short, specific and polite.

## The four-paragraph formula
**1. Opening.** Name the job you are applying for and where you saw it. Add one sentence about why you are excited.

**2. Your value.** Pick two or three requirements from the advert and show how you meet them, using a short example for each.

**3. Why this employer.** Show you understand what the organisation does and why you want to be part of it.

**4. Closing.** Thank the reader, say you would welcome an interview and share your phone number and email.

## Address a person when you can
If the advert gives a name or job title, use it: "Dear Ms Wanjiru" or "Dear Hiring Manager". Avoid "To whom it may concern" when you can.

## Length and format
- Maximum one page, around 250-350 words
- Plain, professional font such as Arial or Calibri, size 11 or 12
- Save as a PDF unless the employer asks for another format

## Tips for common situations
- **Graduates:** lead with your studies, projects, attachment and leadership roles.
- **Career changers:** explain your transferable skills and why you are changing direction.
- **Internship applicants:** say what you hope to learn and how you will contribute.

## Proofread twice
Read your letter aloud, check the company name and job title, and ask a friend to review it.

Save time with our free [Cover Letter Generator](/cover-letter-generator/), then edit the draft so it sounds like you.""",
        "faq": [("Do I need a cover letter if the advert does not ask for one?", "A short, tailored cover letter or email message usually helps, even when it is optional.")],
    },
    {
        "slug": "salary-negotiation-in-kenya", "title": "Salary Negotiation in Kenya: A Beginner's Guide",
        "desc": "How to research pay, respond to salary questions and negotiate an offer confidently and respectfully in the Kenyan job market.",
        "tag": "Career Growth", "read": 6, "emoji": "💰",
        "body": """Many people accept the first offer because they worry about seeming greedy. A polite, well-prepared conversation about pay is normal and professional.

## Do your homework first
- Check pay ranges on listings for similar roles, such as those on our [jobs page](/jobs/).
- Talk to people in the field about typical pay for your level.
- Consider the whole package: basic pay, allowances, medical cover, leave, training and growth.

## Know your numbers
Work out your **minimum acceptable pay**, your **target** and your **ideal**. Remember to factor in transport, rent and statutory deductions so you know your real take-home pay.

## When they ask for your expectation
Give a range based on research, with your target near the middle. For example: "Based on the responsibilities and my experience, I am looking for between KSh 70,000 and KSh 85,000, and I am open to discussing the full package."

## Negotiating an offer
1. Thank them and show enthusiasm.
2. Ask for time to review the offer in writing.
3. Explain the value you bring with specific examples.
4. Make a clear, polite request for the amount or benefit you want.
5. Be ready to compromise on other items such as leave, review dates or training budget.

## If they say no
Ask what would make a higher salary possible, such as a six-month review. Get any promises written in your contract.

## Things to avoid
- Giving an ultimatum you are not ready to follow through on
- Comparing yourself negatively to colleagues
- Accepting verbally before you have seen the written offer

Remember that confidence and courtesy go together. Employers respect candidates who know their value and communicate it well.""",
        "faq": [("Is it acceptable to negotiate salary in Kenya?", "Yes. Most employers expect some discussion, especially for mid-level and senior roles. Stay polite and back your request with evidence.")],
    },
    {
        "slug": "how-to-prepare-for-a-panel-interview", "title": "How to Prepare for a Panel Interview",
        "desc": "Panel interviews are common in Kenya, especially in public institutions, banks and NGOs. Learn how to prepare, answer well and make a strong impression.",
        "tag": "Interview Preparation", "read": 5, "emoji": "👥",
        "body": """A panel interview means several interviewers question you at once. It feels intimidating, but the preparation is straightforward.

## Understand the format
Panels often include a hiring manager, a human resources officer and a technical expert. Each person may ask about a different area, such as skills, culture or policy.

## Research the people and the organisation
- Read the job description and the organisation's recent news.
- If you know who is on the panel, look up their roles.
- Prepare to explain how your skills match the organisation's goals.

## During the interview
- **Greet everyone** and shake hands if offered.
- **Make eye contact** with the person asking, then include the others as you answer.
- **Take a moment** to think before answering; short pauses show confidence.
- **Use STAR examples** for behavioural questions.
- **Ask for clarification** if you do not understand a question.

## Handle tough moments
If you do not know an answer, be honest and explain how you would find out. If you make a mistake, correct it calmly and continue.

## Questions to ask the panel
- What would success look like in the first six months?
- How is performance reviewed?
- What training or development is available?

## Close well
Thank each panel member, restate your interest and ask about next steps. Send a short thank-you email the same day if you have a contact address.

Practise with our [Interview Prep Trainer](/interview-prep/) and ask a friend to play the role of the panel.""",
        "faq": [("How do I answer when different panel members ask different things?", "Look at the person asking, answer directly, and glance at the others as you finish so everyone feels included.")],
    },
]

# category, question, tip
QUESTIONS = [
    ("General", "Tell us about yourself.", "Give a 60-90 second summary: current role or studies, two key strengths, and why this job fits. Avoid reading your CV line by line."),
    ("General", "Why do you want to work for this organisation?", "Mention specific things you learned from research: its mission, products, recent projects or values, and link them to your goals."),
    ("General", "What are your greatest strengths?", "Choose two strengths relevant to the job and give a short example for each."),
    ("General", "What is your biggest weakness?", "Name a real but manageable weakness and explain the steps you are taking to improve."),
    ("General", "Where do you see yourself in five years?", "Show realistic ambition: building expertise, taking on responsibility and contributing to the organisation."),
    ("General", "Why should we hire you?", "Match your top three skills to the needs in the advert and finish with your enthusiasm to contribute."),
    ("General", "What are your salary expectations?", "Give a researched range, mention that you are open to discussing the full package, and avoid naming a number far outside the market."),
    ("Behavioural", "Describe a time you worked in a team to achieve a goal.", "Use STAR. Highlight your specific contribution and the shared result."),
    ("Behavioural", "Tell us about a time you faced a difficult problem and how you solved it.", "Pick a real challenge, explain the steps you took and quantify the outcome if you can."),
    ("Behavioural", "Give an example of when you disagreed with a colleague or supervisor.", "Focus on respectful communication and the resolution, not on blame."),
    ("Behavioural", "Describe a time you failed. What did you learn?", "Be honest, take responsibility and spend most of your answer on what you changed afterwards."),
    ("Behavioural", "Tell us about a time you had to meet a tight deadline.", "Explain how you prioritised, communicated and delivered. Mention what you would improve next time."),
    ("Behavioural", "Describe a time you showed leadership.", "Leadership can be informal: leading a class project, a youth group or a shift. Show how you motivated others."),
    ("Entry-level", "You have no work experience. Why should we consider you?", "Point to attachments, projects, volunteering and training. Stress your eagerness to learn and reliability."),
    ("Entry-level", "What did you enjoy most about your studies?", "Choose a subject or project connected to the job and explain what it taught you."),
    ("Entry-level", "How do you handle feedback?", "Show that you welcome it, ask clarifying questions and apply it quickly, with a short example."),
    ("Entry-level", "What skills are you currently trying to improve?", "Name one or two relevant skills and any courses or practice you are doing."),
    ("Customer Service", "How would you handle an angry customer?", "Listen calmly, apologise for the experience, clarify the issue, offer a solution and follow up."),
    ("Customer Service", "What does great customer service mean to you?", "Talk about being helpful, respectful, quick and honest, and fixing problems at first contact."),
    ("Remote Work", "How do you stay productive when working from home?", "Describe your routine, workspace, communication habits and how you manage time and distractions."),
    ("Remote Work", "How would you handle a power or internet outage during work hours?", "Mention backup power and data options, telling your manager early and having a plan to catch up."),
    ("Remote Work", "How do you communicate with a team across different time zones?", "Talk about clear written updates, shared calendars and being responsive in agreed overlap hours."),
    ("Panel & Situational", "What would you do in your first 30 days in this role?", "Say you would listen, learn the systems, meet stakeholders and agree on early priorities with your manager."),
    ("Panel & Situational", "If you saw a colleague breaking a company policy, what would you do?", "Show integrity: raise it respectfully with the colleague or supervisor following company procedure."),
    ("Panel & Situational", "Do you have any questions for us?", "Always ask something: success measures, team culture, training and next steps in the process."),
]

# provider, course, duration, price KSh, mode, blurb, emoji
COURSES = [
    ("Sample: Skillhive Institute", "Excel for Work & Data Analysis", "6 weeks", 8500, "Online + weekend class", "Formulas, pivot tables and dashboards that employers ask for in finance, admin and operations roles.", "📈"),
    ("Sample: Digitali Academy", "Digital Marketing Foundations", "8 weeks", 12000, "Online", "SEO, social media, email and paid-ads basics with a live campaign project for your portfolio.", "📣"),
    ("Sample: CodeSavanna", "Web Development Bootcamp", "12 weeks", 25000, "Hybrid, Nairobi", "HTML, CSS, JavaScript and Git, finishing with three portfolio projects.", "💻"),
    ("Sample: Skillhive Institute", "Customer Service Excellence", "3 weeks", 4500, "Online", "Phone, chat and email support skills, handling difficult customers and meeting service targets.", "🎧"),
    ("Sample: LedgerLab Training", "QuickBooks & Practical Bookkeeping", "5 weeks", 9500, "In person, Nairobi", "Set up accounts, reconcile and prepare reports using accounting software and real case studies.", "🧾"),
    ("Sample: PM Pathways", "Project Management Essentials", "6 weeks", 11000, "Online", "Plan, budget and track projects using tools used by NGOs and companies; prepares you for professional certification.", "🗓️"),
    ("Sample: Studio Kali", "Graphic Design with Canva & Figma", "6 weeks", 9000, "Online", "Brand basics, social graphics and layouts with feedback on your portfolio pieces.", "🎨"),
    ("Sample: Zungumza Coaching", "Interview & Communication Skills", "2 weeks", 3500, "Online", "Mock interviews, CV review and confident communication for graduates and career changers.", "🎤"),
]

FAQ_HOME = [
    ("Is KaziBora free for job seekers?", "Yes. Searching and applying for jobs, using the CV builder, cover letter generator, interview trainer and scam checker are all free. Optional paid services, like professional CV writing, are clearly marked."),
    ("How do you verify jobs and employers?", "Every employer goes through our verification checklist: business registration details, working contact information, a check that the vacancy is genuine and a policy that employers never charge candidates. Listings that pass receive a Verified badge. Read the full process on our verification page."),
    ("Do you list internships and entry-level jobs?", "Yes. Internships and entry-level roles each have their own page and filters, so graduates and first-time job seekers can find suitable opportunities quickly."),
    ("Can I find remote jobs from Kenya?", "Yes. We list Kenya-friendly remote roles and check each one against common remote-job scam patterns. International openings will expand as the platform grows."),
    ("How much does it cost employers to post a job?", "A standard 30-day job listing costs KSh {std}, a featured listing costs KSh {feat}, and there are discounted multi-job packages. See the employer page for the full price list."),
    ("What should I do if I see a suspicious job advert?", "Do not pay or share personal documents. Use the Report a Job button on the listing or our report form so our team can review it and remove it if necessary."),
]

VERIFY_STEPS = [
    ("1", "Business identity check", "We ask for the company's registered name, registration or KRA PIN details and a working business phone number or official email."),
    ("2", "Genuine vacancy check", "We confirm the role exists by contacting the employer or matching it to an official careers page or notice."),
    ("3", "No-fee promise", "Employers agree in writing that candidates will never be asked to pay for applications, interviews, training, medicals or uniforms."),
    ("4", "Content review", "Our team reviews each advert for unrealistic promises, missing details and common scam wording before it goes live."),
    ("5", "Report & remove", "Every listing has a one-click Report button. Reported listings are reviewed quickly and removed if they break our rules."),
]

SCAM_FLAGS = [
    ("pay", "The employer asks me to pay a fee (application, interview, training, medical, uniform, visa or registration).", 5),
    ("freemail", "The recruiter uses a free email address (Gmail, Yahoo, etc.) even though they claim to be a big company.", 2),
    ("noweb", "I cannot find an official website, careers page or physical address for the company.", 3),
    ("whatsapp", "All communication is through WhatsApp, Telegram or text messages only.", 2),
    ("pressure", "I am being pressured to respond or pay quickly (\"slots are almost full\").", 3),
    ("toogood", "The pay or benefits are far higher than normal for the work and experience asked.", 3),
    ("noint", "I was offered the job without any real interview or with a chat-only interview.", 3),
    ("idearly", "They want my ID, bank details, PIN or passwords before a formal offer.", 4),
    ("cheque", "They want to send me money and ask me to forward part of it to someone else.", 5),
    ("place", "The interview is in a private home, hotel room or unusual location.", 3),
    ("typos", "The advert has many spelling mistakes and vague duties.", 1),
    ("secret", "I have been told to keep the opportunity secret from family or friends.", 3),
]
