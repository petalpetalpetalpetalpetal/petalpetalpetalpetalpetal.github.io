"""Second fill: turns the first data set into a power map.
Reads data/*.csv written by build_data.py, writes actors, flows, outcomes, officeholders,
and reassigns events to the actor responsible. Edit the CSVs directly afterwards."""
import csv, os
D = os.path.join(os.path.dirname(__file__), "data")
def read(n): return list(csv.DictReader(open(os.path.join(D, n), encoding="utf-8")))
def write(n, cols, rows):
    with open(os.path.join(D, n), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for r in rows: w.writerow({c: r.get(c, "") for c in cols})

secs = {s["id"]: s for s in read("sections.csv")}
ev = read("events.csv"); mech = read("mechanisms.csv")

# ------------------------------------------------------------------ actors
A_COLS = ["id", "band", "type", "parent", "col", "label", "era_labels", "start_year", "end_year", "summary", "what_it_takes", "source_title", "source_url", "start_year_note"]
actors = []
state_cols = {"missions": 1, "income": 2, "land": 3, "dev": 5, "housing": 6, "health": 7, "schools": 8, "childprot": 9, "police": 10, "courts": 11, "custody": 12, "legal": 13}
for sid, s in secs.items():
    r = dict(s); r["band"] = "state"; r["type"] = "department"; r["col"] = state_cols[sid]
    if sid == "legal":
        r["label"] = "Legal Aid and interpreters"; r["era_labels"] = "1990-2026:Legal Aid NT and Aboriginal Interpreter Service"
        r["start_year"] = 1990; r["summary"] = "NT-run legal aid and the Aboriginal Interpreter Service."
    if sid == "land":
        r["label"] = "Land and land rights law"
    actors.append(r)
actors.append(dict(id="aba", band="state", type="statutory fund", parent="cwlth", col=4, label="Aboriginals Benefit Account", era_labels="1977-2026:Aboriginals Benefit Account",
    start_year=1977, summary="Commonwealth account that receives royalty equivalents for mining on Aboriginal land and pays land councils and grants.",
    what_it_takes="Control over Aboriginal royalty money", source_title="ABA annual report 2018-19", source_url="https://www.pmc.gov.au/sites/default/files/reports/publications/annual_reports/2018-19-HTML/node/40.html",
    start_year_note="Start set to when the Land Rights Act began operating; confirm"))

PRIV = [
 ("churches", 1, "Church missions", 1913, 1980, "Churches ran missions that held removed children, such as Croker Island and Retta Dixon.", "Bringing Them Home, ch. 9", "https://www.humanrights.gov.au/our-work/bringing-them-home-chapter-9"),
 ("indue", 2, "Indue Ltd", 2015, "", "Runs the income management SmartCard under limited-tender Commonwealth contracts.", "AusTender CN3945982", "https://tenders.gov.au/Cn/Show/4ad3e78c-e7cb-494b-ab29-2eb586fbd30d"),
 ("pastoral", 3, "Pastoral companies", 1863, "", "Cattle stations on taken land, where Aboriginal stock workers were paid in rations; the Gurindji walked off Wave Hill station in 1966.", "Creative Spirits: Wave Hill", "https://www.creativespirits.info/aboriginalculture/politics/aboriginal-people-strike-walk-off-at-wave-hill"),
 ("south32", 4, "GEMCO (South32): Groote manganese", 1965, "", "Large-scale manganese mining on Groote Eylandt since the 1960s, about 10% of world supply; royalties flow to Anindilyakwa through the ABA.", "ORIC: Working with the big end of town", "https://www.oric.gov.au/publications/spotlight/working-big-end-town"),
 ("newmont", 5, "Newmont: Tanami gold", 2005, "", "Gold mines on Warlpiri Country; royalties paid to Kurra Aboriginal Corporation fund WETT.", "CLC: WETT", "https://clc.org.au/wett"),
 ("gas", 6, "Beetaloo gas companies", 2018, "", "Fracking exploration in the Beetaloo Basin with public grants; Nurrdalinji native title holders object.", "SBS", "https://www.sbs.com.au/news/not-now-not-ever-nt-traditional-owners-remain-united-against-gas-fracking"),
 ("glencore", 7, "Glencore: McArthur River Mine", 1992, "", "Zinc, lead and silver mine near Borroloola; the river diversion destroyed dreaming sites. Royalties go to the NT Government.", "NIT", "https://nit.com.au/27-02-2026/22887/nt-must-pay-traditional-owners-more-than-50-million-over-mcarthur-river-mine-court-rules"),
 ("mission", 8, "Mission Australia", 2010, "", "Ran Darwin's only residential rehab, detox and sobering-up service at Berrimah until 2024.", "NT Greens campaign", "https://greens.org.au/nt/campaigns/save-rehab-services"),
 ("oohc", 9, "Out-of-home care providers", 2017, "", "Life Without Barriers, Pathfinders, Carpentaria and purchased home-based care providers paid $133.2M of $143.4M in out-of-home care funding.", "CREATE Foundation", "https://www.create.org.au/get-informed/blog/create-foundations-northern-territory-budget-summary/"),
]
for i, (aid, col, label, st, en, summ, stt, su) in enumerate(PRIV):
    actors.append(dict(id=aid, band="private", type="company or charity", parent="", col=col, label=label, era_labels=f"{st}-2026:{label}", start_year=st, end_year=en, summary=summ,
                       source_title=stt, source_url=su, start_year_note="Approximate first year shown"))

ABO = [
 ("nations", 1, "Nations and communities standing their ground", 1824, "Strikes, court cases, protests and community programs led by Aboriginal nations and communities.", "", ""),
 ("wett", 2, "Warlpiri Education and Training Trust", 2005, "Warlpiri-directed gold royalties for language, education and youth programs: over $63M since 2005.", "CLC: WETT", "https://clc.org.au/wett"),
 ("landcouncils", 3, "Land councils (NLC, CLC, Anindilyakwa, Tiwi)", 1976, "Statutory Aboriginal land councils created by the Land Rights Act; funded from the ABA.", "ABA annual report 2018-19", "https://www.pmc.gov.au/sites/default/files/reports/publications/annual_reports/2018-19-HTML/node/40.html"),
 ("aint", 4, "Aboriginal Investment NT", 2022, "Aboriginal-controlled corporation investing royalty money and making community grants.", "NIT", "https://nit.com.au/20-08-2026/26038/735-million-backing-aboriginal-led-economic-development-across-the-nt"),
 ("rangers", 5, "Aboriginal ranger groups", 2017, "Rangers caring for Country; the CLC alone supports 15 groups and 90+ rangers.", "NIT", "https://nit.com.au/16-05-2025/17981/answers-sought-from-nt-government-over-12m-ranger-program-betrayal"),
 ("yilli", 6, "Yilli Rreung Housing Aboriginal Corporation", 2000, "Ran YiSSA, Darwin's largest short-stay shelter for people from remote communities.", "Hot100", "https://www.hot100fm.com.au/local-news/locals/territory-government-refuses-commonwealth-bid-to-keep-yissa-open/"),
 ("acchos", 7, "Aboriginal community-controlled health (AMSANT, Danila Dilba, Congress)", 1973, "Community-controlled health services and their peak body.", "", ""),
 ("karu", 8, "Aboriginal child and family organisations", 1979, "Aboriginal child care agencies, from Karu (1979) to today's community-controlled child and family centres.", "Bringing Them Home, ch. 9", "https://www.humanrights.gov.au/our-work/bringing-them-home-chapter-9"),
 ("apont", 9, "APO NT (Aboriginal Peak Organisations NT)", 2010, "Alliance of Aboriginal peak bodies; partner in the NTRAI agreement.", "NT Aboriginal Affairs", "https://aboriginalaffairs.nt.gov.au/our-priorities/northern-territory-remote-aboriginal-investment"),
 ("naaja", 10, "NAAJA (Aboriginal legal service)", 1972, "Represents about 65% of everyone in NT criminal matters, funded by the Commonwealth.", "NAAJA", "https://www.naaja.org.au/naaja-responds-to-comments-made-by-ntg-about-using-naaja-funds-for-other-purposes/"),
 ("anindilyakwa", 11, "Anindilyakwa justice (Groote Archipelago)", 2019, "Community Justice Group, Community Court, Peacemakers and Healing Centre.", "NIT", "https://nit.com.au/11-07-2025/19082/aboriginal-led-initiatives-deliver-remarkable-outcomes-on-groote-eylandt-justice-healing"),
]
for aid, col, label, st, summ, stt, su in ABO:
    actors.append(dict(id=aid, band="aboriginal", type="Aboriginal-controlled", parent="", col=col, label=label, era_labels=f"{st}-2026:{label}", start_year=st, summary=summ,
                       source_title=stt, source_url=su, start_year_note="Approximate first year shown; confirm founding year"))
write("actors.csv", A_COLS, actors)

# ------------------------------------------------------------------ events: reassign and add
MOVE = {"Wave Hill walk-off": "nations", "Whitlam hands land back to the Gurindji": "nations", "Karu Aboriginal child care agency founded": "karu",
        "NT Aboriginal Ranger Grants begin": "rangers", "Ranger grants dropped": "rangers", "Badari: High Court strikes down Remote Rent Framework": "nations",
        "Papunya tenants sue over heat": "nations", "Project Mangma stalled": "nations", "Anindilyakwa justice on Groote Eylandt": "anindilyakwa",
        "Push to redirect NAAJA funding": "naaja"}
for e in ev:
    if e["title"] in MOVE: e["section"] = MOVE[e["title"]]; e["mechanism"] = ""
for m in mech:
    if m["id"] == "m_naaja": m["section"] = "naaja"
    if m["id"] == "m_rangers": m["section"] = "rangers"

def E(year, actor, type_, title, detail, actor_name, takes, figure, led, state, st, su, kind, status="verified", date="", mech=""):
    ev.append(dict(id=f"ev{len(ev)+1:03d}", year=year, date=date, section=actor, mechanism=mech, type=type_, title=title, detail=detail, actor=actor_name,
                   what_it_takes=takes, figure=figure, aboriginal_led=led, state_account=state, source_title=st, source_url=su, source_kind=kind, status=status))
ABA = ("ABA annual report 2018-19", "https://www.pmc.gov.au/sites/default/files/reports/publications/annual_reports/2018-19-HTML/node/40.html")
E(1977, "aba", "funding", "Royalty equivalents start flowing to the ABA", "The Commonwealth pays amounts equal to royalties from mining on Aboriginal land into the Aboriginals Benefit Account, which pays land councils, royalty associations and grants.", "Commonwealth", "", "", "no", "", *ABA, "government", status="to source")
E(2018, "aba", "data", "$426.1M in, about $10M out as grants", "2018-19: $426.1M royalty equivalents received; $59.0M to land councils for administration, $122.7M to royalty associations, about $10M in beneficial grants; over $1B held in term deposits.", "Commonwealth", "Control over Aboriginal royalty money", "$426.1M received", "no", "", *ABA, "government")
E(2021, "aba", "law", "Aboriginal Investment NT created", "Legislation creates an Aboriginal-controlled corporation to invest ABA money and make grants, with $500M initial funding plus $60M a year for three years. Senator Thorpe argued it lacked free, prior and informed consent.", "Commonwealth", "", "$500M + $60M a year", "no", "", "NT Independent", "https://ntindependent.com.au/new-aboriginal-controlled-body-given-oversight-of-how-federal-mining-royalty-grants-money-distributed/", "news", date="2021-12")
E(2022, "aint", "institution", "AINT begins with $500M", "Board majority elected through the four land councils.", "Aboriginal Investment NT", "", "$500M", "yes", "", "NT Independent", "https://ntindependent.com.au/new-aboriginal-controlled-body-given-oversight-of-how-federal-mining-royalty-grants-money-distributed/", "news")
E(2025, "aint", "funding", "14 community grants approved", "$11.1M of Community Impact and Innovation Grants against a $10M allocation; an initial corpus of $680M of Aboriginal money.", "Aboriginal Investment NT", "", "$11.1M", "yes", "", "AINT Senate Estimates opening statement", "https://www.aph.gov.au/-/media/Estimates/fpa/supp2526/14_AINT_Opening_Statement.pdf", "government", date="2025-10")
E(2026, "aint", "funding", "$73.5M granted since 2022", "Including about $26M for community-led projects and $11M in business grants.", "Aboriginal Investment NT", "", "$73.5M", "yes", "", "NIT", "https://nit.com.au/20-08-2026/26038/735-million-backing-aboriginal-led-economic-development-across-the-nt", "news", date="2026-08")
WETT = ("CLC: WETT", "https://clc.org.au/wett")
E(2005, "wett", "institution", "Warlpiri set up WETT", "Yapa teachers and traditional owners of the Tanami/Granites mines create an education trust funded by gold royalties.", "Warlpiri people", "", "", "yes", "", *WETT, "sector")
E(2018, "wett", "resistance", "Indigenous Governance Award", "WETT's Yapa-majority advisory committee wins the award.", "Warlpiri people", "", "", "yes", "", *WETT, "sector")
E(2024, "wett", "resistance", "$63M invested; National NAIDOC education award", "Playgroups, youth diversion, Warlpiri language in schools, learning centres in four communities.", "Warlpiri people", "", "$63M since 2005", "yes", "", *WETT, "sector")
GL = ("NIT: McArthur River ruling", "https://nit.com.au/27-02-2026/22887/nt-must-pay-traditional-owners-more-than-50-million-over-mcarthur-river-mine-court-rules")
E(1992, "glencore", "policy", "McArthur River Project agreement", "Agreement between the NT Government and Mount Isa Mines starts the project.", "NT Government", "Country", "", "no", "", *GL, "news")
E(2007, "glencore", "law", "NT validates open-cut conversion", "After native title holders challenged approval to convert to open-cut, the NT passed validating legislation; the McArthur River was diverted.", "NT Government", "Dreaming sites", "", "no", "", *GL, "news")
E(2026, "glencore", "court", "NT ordered to pay $54M for cultural loss", "The Federal Court found the NT liable for extinguishing native title; the river diversion caused 'irreversible disturbance of dreaming sites and routes'. Brought by the Gudanji, Yanyuwa and Yanyuwa-Marra peoples.", "Federal Court", "Dreaming sites", "$54M", "yes", "", *GL, "news", date="2026-02-27")
E(1965, "south32", "institution", "Large-scale manganese mining on Groote", "GEMCO, then a BHP subsidiary, begins large-scale mining in the 1960s (year approximate).", "GEMCO", "Country", "", "no", "", "ORIC", "https://www.oric.gov.au/publications/spotlight/working-big-end-town", "government", status="to source")
E(2018, "landcouncils", "funding", "Anindilyakwa royalty associations receive $86.5M", "2018-19 ABA payments to royalty associations: Anindilyakwa $86.5M, CLC $18.3M, NLC $17.9M.", "Commonwealth (ABA)", "", "$86.5M", "yes", "", *ABA, "government")
E(1976, "landcouncils", "institution", "Land councils created", "The Land Rights Act creates the land councils; the NLC operated as the sole council for nearly ten years (Fejo, Sub 209).", "Commonwealth", "", "", "yes", "", "History of the NT", "https://en.wikipedia.org/wiki/History_of_the_Northern_Territory", "reference")
E(2025, "landcouncils", "resistance", "All four land councils oppose the Territory Coordinator", "They said it excludes Aboriginal people from development decisions on their land.", "Land councils", "", "", "yes", "", "NIT", "https://nit.com.au/12-03-2025/16768/nt-coordinator-bill-land-councils-northern-territory", "news")
E(2026, "landcouncils", "resistance", "CLC condemns income management extension", "", "Central Land Council", "", "", "yes", "", "NIT", "https://nit.com.au/24-09-2026/26644/causes-so-much-harm-experts-land-council-slam-federal-move-to-extend-compulsory-income-management", "news")
ANI = ("NIT: Groote outcomes", "https://nit.com.au/11-07-2025/19082/aboriginal-led-initiatives-deliver-remarkable-outcomes-on-groote-eylandt-justice-healing")
E(2024, "anindilyakwa", "institution", "NT's first Community Court on Groote", "Works with the Local Court to give culturally appropriate sentencing options, under a Law and Justice Local Decision Making Agreement.", "Anindilyakwa people", "", "", "yes", "", *ANI, "news")
E(2025, "anindilyakwa", "institution", "32-bed Healing Centre opens on Country", "For men aged 17 to 25 referred through community services and courts.", "Anindilyakwa people", "", "32 beds", "yes", "", *ANI, "news", date="2025-03")
E(2025, "anindilyakwa", "data", "Recorded offences down 87.5%", "1,041 offences in 2019 to 130 in the 12 months to July 2025; youth offences 267 to 28.", "Anindilyakwa people", "", "-87.5%", "yes", "", *ANI, "news", date="2025-07")
E(2025, "anindilyakwa", "funding", "Peacemaker Program", "29 Peacemakers from all 14 clans resolve disputes before police are involved; $6.2M Commonwealth funding.", "Groote Archipelago Community Justice Group", "", "$6.2M", "yes", "", "NIAA", "https://www.niaa.gov.au/our-work/closing-gap/culturally-grounded-justice-groote-archipelago", "government")
E(2025, "acchos", "resistance", "Oppose scrapping the alcohol floor price", "Danila Dilba, Congress, AMSANT and Larrakia Nation objected.", "Aboriginal health services", "", "", "yes", "", "NT Independent", "https://ntindependent.com.au/clp-lifts-minimum-unit-price-for-alcohol-amid-calls-to-keep-the-policy-in-place/", "news")
E(2026, "acchos", "resistance", "Truancy fines called 'subtle structural racism'", "AMSANT chair Rob McPhee told the federal racism inquiry; the NT Government made no submission and did not appear.", "AMSANT", "", "", "yes", "", "ABC", "https://www.abc.net.au/news/2026-07-16/federal-racism-inquiry-darwin-hearings-nt-government-no-show/106918532", "news", date="2026-07")
E(2025, "naaja", "data", "27% not connected to custody notification", "In January 2025, 27% of 374 Aboriginal people taken into Palmerston watch house could not speak to NAAJA's custody notification service.", "NAAJA", "", "27%", "yes", "", "NAAJA", "https://www.naaja.org.au/aboriginal-people-continue-to-be-locked-up-at-record-levels-putting-lives-at-risk/", "sector", date="2025-01")
E(2026, "naaja", "resistance", "Submission to the racism inquiry", "Systemic racism must be judged by outcome; NAAJA was consulted on none of the current government's laws before introduction.", "NAAJA", "", "", "yes", "", "NAAJA, Submission 604", "", "sector")
E(2025, "apont", "funding", "NTRAI partner; $61M to deliver directly", "Partner with the Commonwealth and NT in the $842.6M agreement; to deliver $61M over five years.", "APO NT", "", "$61M", "yes", "", "APO NT job advertisement", "https://static.ethicaljobs.com.au/media/1787276445284_TnuDD_.pdf", "sector")
E(2026, "aba", "data", "NTRAI: nothing paid by May 2026", "The $842.6M Commonwealth-NT agreement was due to start in December 2025; no payments had been made by May 2026.", "Commonwealth", "", "$0 paid", "no", "Funding will be paid retrospectively.", "NIT", "https://nit.com.au/25-05-2026/24445/no-funding-spent-under-842-million-nt-remote-aboriginal-services-agreement-documents-reveal", "news", date="2026-05")
E(2026, "yilli", "cut", "YiSSA forced to close", "The NT rejected a Commonwealth offer to share the purchase; Minister McCarthy said it objected because YiSSA was Aboriginal-run. 383 residents, including 145 children, moved to Batchelor.", "NT Government", "Shelter near family", "383 residents", "no", "Could not agree a fair price with the owner.", "NIT", "https://nit.com.au/09-10-2026/26882/nt-government-rejected-deal-to-keep-yissa-open-because-it-was-aboriginal-run", "news", date="2026-10-11")
E(2015, "indue", "funding", "Card services contract grows to $11.9M", "Income Management Card Services 2015-18, limited tender, from $4.675M to $11.889M.", "Commonwealth", "", "$11.9M", "no", "", "AusTender CN3068992", "https://tenders.gov.au/Cn/Show/1FBD10FE-D17E-B1EE-45B1-389C42FA10B7", "government")
E(2023, "indue", "funding", "$20.95M contract under 'extreme urgency'", "Card and Banking Services 2023-25, from $11.887M to $20.95M.", "Commonwealth", "", "$20.95M", "no", "", "AusTender CN3945982", "https://tenders.gov.au/Cn/Show/4ad3e78c-e7cb-494b-ab29-2eb586fbd30d", "government")
E(2025, "oohc", "data", "Nearly 1 in 3 children in care allegedly harmed", "Children's Commissioner, 2024-25; most substantiated harm in purchased home-based care, which the 2017 Royal Commission recommended phasing out.", "Care providers", "Safety", "almost 1 in 3", "no", "", "ABC", "https://www.abc.net.au/news/2026-06-02/almost-one-third-nt-children-in-care-harmed-commissioner-report/106747302", "news")
E(2026, "oohc", "funding", "New residential care contracts", "Intensive therapeutic residential care contracts with Life Without Barriers, Pathfinders and Carpentaria from 14 May 2026.", "NT Government", "", "", "no", "", "NT Govt via Mirage", "https://www.miragenews.com/new-partners-bolster-support-for-vulnerable-kids-1681921/", "government", date="2026-05-14")
E(2024, "mission", "cut", "Berrimah rehab and sobering-up closes", "Darwin's only combined residential rehab, detox and sobering-up service closes to make way for a women's prison; about 40 people in long-term rehab.", "NT Government", "Treatment", "about 40 people", "no", "", "NT Greens campaign", "https://greens.org.au/nt/campaigns/save-rehab-services", "advocacy")
E(2025, "gas", "resistance", "Nurrdalinji challenge Beetaloo fracking", "Native title holders seek federal water-trigger assessment; some say they had no chance to give free, prior and informed consent.", "Nurrdalinji native title holders", "", "", "yes", "", "1earthmedia", "https://1earthmedia.com/legal-challenge-to-protect-beetaloo-water-from-fracking/", "news")
E(1966, "pastoral", "resistance", "Gurindji strike at Wave Hill station", "About 200 Gurindji stock workers and families walk off over pay and conditions.", "Gurindji people", "", "", "yes", "", "Creative Spirits: Wave Hill", "https://www.creativespirits.info/aboriginalculture/politics/aboriginal-people-strike-walk-off-at-wave-hill", "reference", date="1966-08-23")
E(1946, "churches", "institution", "Missions hold removed children", "Early 1950s: NT missions care for about 360 mixed-descent children; Retta Dixon opens after the war.", "Churches and Commonwealth", "Family", "about 360 children", "no", "", "Bringing Them Home, ch. 9", "https://www.humanrights.gov.au/our-work/bringing-them-home-chapter-9", "government")
EV_COLS = list(read("events.csv")[0].keys())
write("events.csv", EV_COLS, ev)
write("mechanisms.csv", list(mech[0].keys()), mech)

# ------------------------------------------------------------------ flows (money)
F_COLS = ["id", "from", "to", "year", "end_year", "amount_aud", "per", "kind", "label", "status", "source_title", "source_url", "note"]
BUD = ("AAP via Shepparton News", "https://www.sheppnews.com.au/national/northern-territory-budgets-hundreds-more-prison-beds/")
FC = ("Funding Centre: NT budget 2026-27", "https://explore.fundingcentre.com.au/articles/whats-in-the-2026-27-nt-budget-for-your-organisation")
MC = ("Minister McCarthy: NTRAI lines", "https://ministers.pmc.gov.au/mccarthy/strengthening-critical-remote-services-northern-territory")
F = [
 ("cwlth", "ntg", 2024, 2024, 6323000000, "year", "revenue", "GST and Commonwealth grants, 72% of NT revenue", "verified", "NT Budget: revenue", "https://budget.nt.gov.au/papers/guide/territory-governments-revenue", ""),
 ("glencore", "ntg", 2024, 2024, 218000000, "year", "royalty", "Mining royalties to the NT, all mines combined", "verified", "NT Budget: revenue", "https://budget.nt.gov.au/papers/guide/territory-governments-revenue", "Total for all NT mines, not Glencore alone"),
 ("cwlth", "aba", 2018, 2018, 426100000, "year", "royalty equivalent", "Royalty equivalents for mining on Aboriginal land", "verified", *ABA, ""),
 ("aba", "landcouncils", 2018, 2018, 59000000, "year", "grant", "Land council administration", "verified", *ABA, ""),
 ("aba", "landcouncils", 2018, 2018, 122700000, "year", "royalty", "To royalty associations in mining areas", "verified", *ABA, "Anindilyakwa $86.5M"),
 ("aba", "aint", 2022, 2024, 680000000, "total", "transfer", "Corpus of Aboriginal money for AINT", "verified", "AINT Senate Estimates", "https://www.aph.gov.au/-/media/Estimates/fpa/supp2526/14_AINT_Opening_Statement.pdf", ""),
 ("aint", "nations", 2022, 2026, 73500000, "total", "grant", "Community, business and cultural grants since 2022", "verified", "NIT", "https://nit.com.au/20-08-2026/26038/735-million-backing-aboriginal-led-economic-development-across-the-nt", ""),
 ("newmont", "wett", 2005, 2024, 63000000, "total", "royalty", "Gold royalties directed by Warlpiri to education (via Kurra)", "verified", *WETT, ""),
 ("ntg", "nations", 2026, 2026, 54743408, "once", "compensation", "Court-ordered compensation, McArthur River", "verified", *GL, "$54M cultural loss + $743,408 economic loss"),
 ("ntg", "police", 2026, 2026, 654000000, "year", "budget", "Police", "verified", *FC, ""),
 ("ntg", "custody", 2026, 2026, 525000000, "year", "budget", "Corrections, incl. $250M infrastructure", "verified", *BUD, ""),
 ("ntg", "custody", 2025, 2025, 495000000, "year", "budget", "Corrections (record)", "verified", "SBS NITV", "https://www.sbs.com.au/nitv/article/nt-racking-up-debt-as-prison-costs-skyrocket-and-grant-funding-for-aboriginal-rangers-cut/t8wy9st8o", ""),
 ("ntg", "courts", 2026, 2026, 4900000, "year", "budget", "Diversion programs", "verified", *BUD, ""),
 ("ntg", "housing", 2026, 2026, 1800000000, "year", "budget", "Urban and remote housing", "verified", *FC, ""),
 ("ntg", "schools", 2024, 2024, 923200000, "year", "budget", "Education budget (65.3% school-managed)", "verified", "ATESOL NT, Submission 624", "", ""),
 ("ntg", "childprot", 2026, 2026, 143400000, "year", "budget", "Out-of-home care", "verified", "CREATE Foundation", "https://www.create.org.au/get-informed/blog/create-foundations-northern-territory-budget-summary/", ""),
 ("childprot", "oohc", 2026, 2026, 133200000, "year", "contract", "Paid to non-government care providers (93%)", "verified", "CREATE Foundation", "https://www.create.org.au/get-informed/blog/create-foundations-northern-territory-budget-summary/", ""),
 ("childprot", "karu", 2026, 2026, 3500000, "year", "payment", "Kinship carers (families, not organisations)", "to source", "Jenny's research", "", "Shown under family and child organisations for want of a family node"),
 ("cwlth", "police", 2025, 2031, 205800000, "6 years", "grant", "NTRAI remote policing", "verified", *MC, "None paid by May 2026"),
 ("cwlth", "legal", 2025, 2031, 55000000, "6 years", "grant", "NTRAI interpreters", "verified", *MC, ""),
 ("cwlth", "karu", 2025, 2031, 135900000, "6 years", "grant", "NTRAI child and family centres, women's safe spaces", "verified", *MC, "Recipient mix of government and community-controlled not public"),
 ("cwlth", "apont", 2025, 2030, 61000000, "5 years", "grant", "APO NT direct delivery under NTRAI", "verified", "APO NT job advertisement", "https://static.ethicaljobs.com.au/media/1787276445284_TnuDD_.pdf", ""),
 ("cwlth", "housing", 2024, 2034, 2100000000, "10 years", "grant", "Commonwealth share of $4B remote housing", "verified", "AAP", "https://aapnews.com.au/news/historic-4-billion-investment-in-remote-nt-housing", "About $844M new money"),
 ("income", "indue", 2015, 2018, 11889000, "contract", "contract", "Income Management Card Services", "verified", "AusTender CN3068992", "https://tenders.gov.au/Cn/Show/1FBD10FE-D17E-B1EE-45B1-389C42FA10B7", ""),
 ("income", "indue", 2023, 2025, 20950000, "contract", "contract", "Card and Banking Services ('extreme urgency')", "verified", "AusTender CN3945982", "https://tenders.gov.au/Cn/Show/4ad3e78c-e7cb-494b-ab29-2eb586fbd30d", ""),
 ("cwlth", "anindilyakwa", 2025, 2025, 6200000, "program", "grant", "Peacemaker Program", "verified", "NIAA", "https://www.niaa.gov.au/our-work/closing-gap/culturally-grounded-justice-groote-archipelago", ""),
 ("cwlth", "naaja", 2025, 2026, "", "year", "grant", "Commonwealth funds NAAJA's legal services; the NT contributes nothing", "verified", "NAAJA", "https://www.naaja.org.au/naaja-responds-to-comments-made-by-ntg-about-using-naaja-funds-for-other-purposes/", "Amount not public"),
 ("ntg", "rangers", 2025, 2025, 12000000, "4 years", "cut", "Ranger grants dropped", "verified", "NIT", "https://nit.com.au/16-05-2025/17981/answers-sought-from-nt-government-over-12m-ranger-program-betrayal", ""),
 ("health", "mission", 2024, 2024, "", "", "cut", "Berrimah rehab and sobering-up closed", "verified", "NT Greens campaign", "https://greens.org.au/nt/campaigns/save-rehab-services", ""),
 ("health", "", 2026, 2026, 2100000, "grant", "cut", "Parole rehab (COMMIT) cut", "to source", "inkl / ABC", "https://www.inkl.com/news/parole-board-boss-says-nt-government-cuts-will-worsen-aboriginal-incarceration", ""),
 ("schools", "", 2024, 2024, 2120000, "year", "cut", "Bilingual funding cut, then reversed", "verified", "ATESOL NT, Submission 624", "", ""),
 ("ntg", "yilli", 2026, 2026, "", "", "cut", "YiSSA closed; Commonwealth offer to share purchase refused", "verified", "ABC", "https://www.abc.net.au/news/2026-09-21/dialysis-patients-fear-short-stay-yissa-accommodation-shutdown/107173878", ""),
 ("cwlth", "gas", 2021, 2021, 50000000, "grant", "grant", "Grant to fast-track Beetaloo exploration", "to source", "SBS", "https://www.sbs.com.au/news/not-now-not-ever-nt-traditional-owners-remain-united-against-gas-fracking", "Year to confirm"),
 ("cwlth", "ntg", 2025, 2031, 842600000, "6 years", "grant", "NTRAI total, nothing paid by May 2026", "verified", "NIT", "https://nit.com.au/25-05-2026/24445/no-funding-spent-under-842-million-nt-remote-aboriginal-services-agreement-documents-reveal", ""),
]
write("flows.csv", F_COLS, [dict(zip(F_COLS, [f"f{i+1:02d}"] + list(f))) for i, f in enumerate(F)])

# ------------------------------------------------------------------ outcomes (what the money buys)
O_COLS = ["id", "actor", "year", "program", "measure", "value", "cost", "caveat", "control", "source_title", "source_url", "status"]
O = [
 ("custody", 2026, "Prisons", "Return to prison within two years (released 2021-22)", "60.3%, highest in Australia", "$525M a year", "Adults; national rate 43.0%", "government", "Sentencing Advisory Council (ROGS)", "https://www.sentencingcouncil.vic.gov.au/sentencing-statistics/released-prisoners-returning-to-prison", "verified"),
 ("custody", 2022, "Youth detention", "Cost per child", "$2,703.68 a day", "about $987,000 a year", "", "government", "NT Parliament", "https://parliament.nt.gov.au/__data/assets/pdf_file/0020/1464131/Answer-to-Written-Question-1.pdf", "verified"),
 ("courts", 2026, "Diversion", "Young people not reoffending within a year of diversion or court", "76%; diverted reoffended less than those sent to court", "$4.9M a year", "AIC study of NT youth 2000-05; diverted youth were lower-risk, so not like-for-like with prison", "government", "AIC 2007", "https://aic.gov.au/publications/tandi/tandi339", "verified"),
 ("anindilyakwa", 2025, "Community Justice Group, Community Court, Peacemakers, Healing Centre", "Recorded offences, 2019 vs 12 months to July 2025", "-87.5% (1,041 to 130); youth 267 to 28", "$6.2M Commonwealth (Peacemakers)", "Not adjusted for population or reporting changes; full program cost not public", "aboriginal", "NIT", "https://nit.com.au/11-07-2025/19082/aboriginal-led-initiatives-deliver-remarkable-outcomes-on-groote-eylandt-justice-healing", "verified"),
 ("health", 2021, "Alcohol floor price", "Assaults after three years", "-14% alcohol-related; -21% alcohol-related family violence", "No cost to government (a price rule)", "Scrapped February 2025", "government", "NT Independent", "https://ntindependent.com.au/clp-lifts-minimum-unit-price-for-alcohol-amid-calls-to-keep-the-policy-in-place/", "verified"),
 ("income", 2025, "Compulsory income management", "Effect on its own goals", "No improvement; appeared to increase welfare dependence", "Indue contract $20.95M (2023-25)", "ANU evaluation of New Income Management", "government", "Gray and Bray submission", "https://polis.cass.anu.edu.au/files/docs/2025/6/Sub03_Prof_Matthew_Gray_Dr_J._Rob_Bray_PSM.pdf", "verified"),
 ("schools", 2025, "Funding by attendance (2013-2025)", "Aboriginal attendance", "68.2% (2014) to 54.7% (2025); Aboriginal students lost about $3,000 each a year", "", "Attendance has many causes", "government", "ATESOL NT, Submission 624", "", "verified"),
 ("wett", 2024, "Warlpiri Education and Training Trust", "Recognition and reach", "Learning centres in four communities; 2018 Indigenous Governance Award; 2024 NAIDOC education award", "$63M of Warlpiri royalties since 2005", "No attendance or results data found yet", "aboriginal", "CLC: WETT", "https://clc.org.au/wett", "verified"),
 ("aba", 2018, "Aboriginals Benefit Account", "Share of receipts paid as grants", "About 2.4% ($10M of $426.1M)", "", "Most payments go to land council administration and royalty associations", "government", *ABA, "verified"),
 ("aint", 2026, "Aboriginal Investment NT", "Granted to Aboriginal communities and businesses", "$73.5M since 2022", "", "Outcomes of grants not yet reported", "aboriginal", "NIT", "https://nit.com.au/20-08-2026/26038/735-million-backing-aboriginal-led-economic-development-across-the-nt", "verified"),
 ("oohc", 2025, "Purchased home-based and residential care", "Children allegedly harmed in care", "Nearly 1 in 3 (2024-25)", "$133.2M a year to providers", "", "private", "ABC", "https://www.abc.net.au/news/2026-06-02/almost-one-third-nt-children-in-care-harmed-commissioner-report/106747302", "verified"),
]
write("outcomes.csv", O_COLS, [dict(zip(O_COLS, [f"o{i+1:02d}"] + list(o))) for i, o in enumerate(O)])

# ------------------------------------------------------------------ office holders
H_COLS = ["id", "person", "role", "actor", "start", "end", "party", "note", "source_title", "source_url", "status"]
H = []
def h(person, role, actor, start, end, party="", note="", st="", su="", status="verified"):
    H.append(dict(id=f"h{len(H)+1:03d}", person=person, role=role, actor=actor, start=start, end=end, party=party, note=note, source_title=st, source_url=su, status=status))
ADM = ("Administrator of the NT", "https://www.wikiwand.com/en/Administrator_of_the_Northern_Territory")
for p, s, e in [("Boyle Travers Finniss", "1864-03-03", "1865-11-04"), ("William Bloomfield Douglas", "1870-04-27", "1873-06-30"), ("George Byng Scott", "1873-10-06", "1876-06-30"),
                ("Edward William Price", "1876-07-01", "1883-03-06"), ("John Parsons", "1884-03-19", "1890-02-14"), ("John Knight", "1890-07-16", "1892-01-10"),
                ("Charles James Dashwood", "1892-02-24", "1905-01-31"), ("Charles Edward Herbert", "1905-02-01", "1910-02-08"), ("Samuel Mitchell", "1910-04-01", "1912-03-25")]:
    h(p, "Government Resident", "sa", s, e, "", "South Australia's officer in the Territory", *ADM)
for p, s, e in [("John Gilruth", "1912-03-25", "1919-08-01"), ("Henry Ernest Carey", "1919-08-01", "1921-01-17"), ("Frederic Urquhart", "1921-01-17", "1927-03-01"),
                ("Robert Weddell", "1927-03-01", "1937-03-29"), ("Aubrey Abbott", "1937-03-29", "1946-07-01"), ("Arthur Driver", "1946-07-01", "1951-07-01"),
                ("Frank Wise", "1951-07-01", "1956-07-01"), ("James Archer", "1956-07-01", "1961-04-01"), ("Roger Nott", "1961-04-01", "1964-10-01"),
                ("Roger Dean", "1964-10-01", "1970-03-04"), ("Frederick Chaney", "1970-03-04", "1973-12-10"), ("Jock Nelson", "1973-12-10", "1975-11-12")]:
    h(p, "Administrator", "ntg", s, e, "", "Commonwealth's ruler of the Territory", *ADM)
h("Cecil Cook", "Chief Protector of Aborigines", "childprot", "1927-03-01", "1939-12-31", "", "Reported in 1934 that children 'have been removed to half-caste institutions under Government control'", "ADB: Cook", "https://adb.anu.edu.au/biography/cook-cecil-evelyn-mick-12343")
h("E.W.P. Chinnery", "Head of Native Affairs", "childprot", "1939-01-01", "1946-12-31", "", "Seconded from New Guinea to bring 'New Guinea methods' to the Territory", "ADB: Chinnery", "https://adb.anu.edu.au/biography/chinnery-ernest-william-pearson-5583")
h("Harry Giese", "Director of Welfare", "childprot", "1954-07-15", "1970-12-31", "", "Ran the Welfare Branch that administered wardship", "ADB: Giese", "https://adb.anu.edu.au/biography/giese-harry-christian-33894")
h("Paul Hasluck", "Minister for Territories", "cwlth", "1951-05-11", "1963-12-18", "Liberal", "Architect of assimilation policy", "Indigenous Rights: Hasluck", "https://indigenousrights.net.au/people/pagination/paul_hasluck", "verified")
PM = [("Andrew Fisher", "1910-04-29", "1913-06-24", "Labor"), ("Joseph Cook", "1913-06-24", "1914-09-17", "Liberal"), ("Andrew Fisher", "1914-09-17", "1915-10-27", "Labor"),
      ("Billy Hughes", "1915-10-27", "1923-02-09", "Labor / Nationalist"), ("Stanley Bruce", "1923-02-09", "1929-10-22", "Nationalist"), ("James Scullin", "1929-10-22", "1932-01-06", "Labor"),
      ("Joseph Lyons", "1932-01-06", "1939-04-07", "United Australia"), ("Earle Page", "1939-04-07", "1939-04-26", "Country"), ("Robert Menzies", "1939-04-26", "1941-08-29", "United Australia"),
      ("Arthur Fadden", "1941-08-29", "1941-10-07", "Country"), ("John Curtin", "1941-10-07", "1945-07-05", "Labor"), ("Frank Forde", "1945-07-06", "1945-07-13", "Labor"),
      ("Ben Chifley", "1945-07-13", "1949-12-19", "Labor"), ("Robert Menzies", "1949-12-19", "1966-01-26", "Liberal"), ("Harold Holt", "1966-01-26", "1967-12-19", "Liberal"),
      ("John McEwen", "1967-12-19", "1968-01-10", "Country"), ("John Gorton", "1968-01-10", "1971-03-10", "Liberal"), ("William McMahon", "1971-03-10", "1972-12-05", "Liberal"),
      ("Gough Whitlam", "1972-12-05", "1975-11-11", "Labor"), ("Malcolm Fraser", "1975-11-11", "1983-03-11", "Liberal"), ("Bob Hawke", "1983-03-11", "1991-12-20", "Labor"),
      ("Paul Keating", "1991-12-20", "1996-03-11", "Labor"), ("John Howard", "1996-03-11", "2007-12-03", "Liberal"), ("Kevin Rudd", "2007-12-03", "2010-06-24", "Labor"),
      ("Julia Gillard", "2010-06-24", "2013-06-27", "Labor"), ("Kevin Rudd", "2013-06-27", "2013-09-18", "Labor"), ("Tony Abbott", "2013-09-18", "2015-09-15", "Liberal"),
      ("Malcolm Turnbull", "2015-09-15", "2018-08-24", "Liberal"), ("Scott Morrison", "2018-08-24", "2022-05-23", "Liberal"), ("Anthony Albanese", "2022-05-23", "", "Labor")]
for p, s, e, party in PM:
    h(p, "Prime Minister", "cwlth", s, e, party, "", "Australia's Prime Ministers (National Archives)", "", "reference")
IM = ("Minister for Indigenous Australians", "https://en.wikipedia.org/wiki/Minister_for_Indigenous_Australians")
for p, s, e, party in [("Bill Wentworth", "1968-02-28", "1971-05-31", "Liberal"), ("Peter Howson", "1971-05-31", "1972-12-05", "Liberal"), ("Gough Whitlam", "1972-12-05", "1972-12-19", "Labor"),
                       ("Gordon Bryant", "1972-12-19", "1973-10-09", "Labor"), ("Jim Cavanagh", "1973-10-09", "1975-06-06", "Labor"), ("Les Johnson", "1975-06-06", "1975-11-11", "Labor"),
                       ("Tom Drake-Brockman", "1975-11-11", "1975-12-22", "National Country"), ("Ian Viner", "1975-12-22", "1978-12-05", "Liberal"), ("Fred Chaney", "1978-12-05", "1980-11-03", "Liberal"),
                       ("Peter Baume", "1980-11-03", "1982-05-07", "Liberal"), ("Ian Wilson", "1982-05-07", "1983-03-11", "Liberal"), ("Clyde Holding", "1983-03-11", "1987-07-24", "Labor"),
                       ("Gerry Hand", "1987-07-24", "1990-04-04", "Labor"), ("Robert Tickner", "1990-04-04", "1996-03-11", "Labor"), ("John Herron", "1996-03-11", "2001-01-30", "Liberal"),
                       ("Philip Ruddock", "2001-01-30", "2003-10-07", "Liberal"), ("Amanda Vanstone", "2003-10-07", "2006-01-27", "Liberal"), ("Mal Brough", "2006-01-27", "2007-12-03", "Liberal"),
                       ("Jenny Macklin", "2007-12-03", "2013-09-18", "Labor"), ("Nigel Scullion", "2013-09-18", "2019-05-29", "National"), ("Ken Wyatt", "2019-05-29", "2022-05-23", "Liberal"),
                       ("Linda Burney", "2022-06-01", "2024-07-29", "Labor"), ("Malarndirri McCarthy", "2024-07-29", "", "Labor")]:
    h(p, "Commonwealth minister for Aboriginal affairs", "cwlth", s, e, party, "", *IM)
CM = ("Chief Minister of the NT", "https://en.wikipedia.org/wiki/Chief_Minister_of_the_Northern_Territory")
for p, s, e, party in [("Paul Everingham", "1978-07-01", "1984-10-15", "CLP"), ("Ian Tuxworth", "1984-10-16", "1986-05-13", "CLP"), ("Stephen Hatton", "1986-05-14", "1988-07-12", "CLP"),
                       ("Marshall Perron", "1988-07-13", "1995-05-24", "CLP"), ("Shane Stone", "1995-05-25", "1999-02-07", "CLP"), ("Denis Burke", "1999-02-08", "2001-08-27", "CLP"),
                       ("Clare Martin", "2001-08-27", "2007-11-26", "Labor"), ("Paul Henderson", "2007-11-26", "2012-08-28", "Labor"), ("Terry Mills", "2012-08-29", "2013-03-13", "CLP"),
                       ("Adam Giles", "2013-03-14", "2016-08-30", "CLP"), ("Michael Gunner", "2016-08-31", "2022-05-13", "Labor"), ("Natasha Fyles", "2022-05-13", "2023-12-21", "Labor"),
                       ("Eva Lawler", "2023-12-21", "2024-08-28", "Labor"), ("Lia Finocchiaro", "2024-08-28", "", "CLP")]:
    h(p, "Chief Minister", "ntg", s, e, party, "", *CM)
A14 = ("NT Parliament: 14th Assembly ministries", "https://parliament.nt.gov.au/members/previous-assemblies/Fourteenth-Assembly-Ministries-Consolidated.pdf")
A15 = ("NT Parliament: 15th Assembly ministries", "https://parliament.nt.gov.au/__data/assets/pdf_file/0005/1553567/MASTER-15th-Assembly-Government-Ministries-by-Assembly-as-at-11-September-2024.pdf")
for p, role, actor, s, e, party, src in [
    ("Nicole Manison", "Minister for Police", "police", "2020-09-08", "2022-05-22", "Labor", A14), ("Kate Worden", "Minister for Police", "police", "2022-05-23", "2023-10-29", "Labor", A14),
    ("Brent Potter", "Minister for Police", "police", "2023-10-30", "2024-06-20", "Labor", A14), ("Lia Finocchiaro", "Minister for Police", "police", "2024-08-27", "", "CLP", A15),
    ("Selena Uibo", "Attorney-General", "courts", "2020-09-08", "2022-05-22", "Labor", A14), ("Chansey Paech", "Attorney-General", "courts", "2022-05-23", "2024-06-20", "Labor", A14),
    ("Gerard Maley", "Attorney-General", "courts", "2024-08-27", "2024-09-09", "CLP", A15), ("Marie-Clare Boothby", "Attorney-General", "courts", "2024-09-10", "", "CLP", A15),
    ("Gerard Maley", "Minister for Corrections", "custody", "2024-09-10", "", "CLP", A15),
    ("Kate Worden", "Minister for Territory Families", "childprot", "2020-09-08", "2023-10-29", "Labor", A14), ("Ngaree Ah Kit", "Minister for Territory Families", "childprot", "2023-10-30", "2024-06-20", "Labor", A14),
    ("Robyn Cahill", "Minister for Children and Families; Child Protection", "childprot", "2024-09-10", "", "CLP", A15),
    ("Lauren Moss", "Minister for Education", "schools", "2020-09-08", "2022-05-22", "Labor", A14), ("Eva Lawler", "Minister for Education", "schools", "2022-05-23", "2023-12-20", "Labor", A14),
    ("Mark Monaghan", "Minister for Education", "schools", "2023-12-21", "2024-06-20", "Labor", A14), ("Jo Hersey", "Minister for Education and Training", "schools", "2024-09-10", "", "CLP", A15),
    ("Chansey Paech", "Minister for Remote Housing and Town Camps", "housing", "2020-09-08", "2022-05-22", "Labor", A14), ("Selena Uibo", "Minister for Remote Housing and Homelands", "housing", "2022-05-23", "2024-06-20", "Labor", A14),
    ("Steve Edgington", "Minister for Housing; Aboriginal Affairs; Health", "housing", "2024-09-10", "", "CLP", A15),
    ("Natasha Fyles", "Minister for Health", "health", "2020-09-08", "2023-12-20", "Labor", A14), ("Selena Uibo", "Minister for Health", "health", "2023-12-21", "2024-06-20", "Labor", A14),
    ("Steve Edgington", "Minister for Health", "health", "2024-09-10", "", "CLP", A15),
    ("Nicole Manison", "Minister for Mining", "dev", "2020-09-08", "2023-12-20", "Labor", A14), ("Mark Monaghan", "Minister for Mining", "dev", "2023-12-21", "2024-06-20", "Labor", A14),
    ("Gerard Maley", "Minister for Mining and Energy", "dev", "2024-09-10", "", "CLP", A15), ("Lia Finocchiaro", "Minister for Territory Coordinator", "dev", "2024-09-10", "", "CLP", A15)]:
    h(p, role, actor, s, e, party, "", *src)
write("officeholders.csv", H_COLS, H)
for f in ["sections.csv", "money.csv"]:
    p = os.path.join(D, f)
    if os.path.exists(p): os.remove(p)
print(len(actors), "actors", len(ev), "events", len(F), "flows", len(O), "outcomes", len(H), "office holders")
