"""Third fill: contractors, funding funnel, harm statistics; removes the 'nations' box.
Run after build_data.py and build_v2.py. Edit the CSVs directly afterwards."""
import csv, os
D = os.path.join(os.path.dirname(__file__), "data")
def read(n): return list(csv.DictReader(open(os.path.join(D, n), encoding="utf-8")))
def write(n, cols, rows):
    with open(os.path.join(D, n), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols); w.writeheader()
        for r in rows: w.writerow({c: r.get(c, "") for c in cols})

cfg = read("config.csv")
for r in cfg:
    if r["key"] == "country_label": r["value"] = "First Nations controlled organisations"
write("config.csv", list(cfg[0].keys()), cfg)

actors = [a for a in read("actors.csv") if a["id"] != "nations"]
A_COLS = list(read("actors.csv")[0].keys())
NEW = [
 ("halikos", "Halikos Group", 2020, "Builder of the Holtze youth detention centre ($55.1M contract, 2020). The site moved next to the adult prison after Halikos objected to the Don Dale site bordering its development.", "NT Independent", "https://ntindependent.com.au/halikos-given-55-million-to-build-new-youth-prison-after-objecting-to-original-location/"),
 ("njhomes", "NJ Homes", 2026, "Katherine builder awarded stage one of the Katherine prisoner work camp ($5.67M, 2026).", "Katherine Times", "https://www.katherinetimes.com.au/story/9290162/nj-homes-awarded-567m-katherine-work-camp-contract/"),
 ("bukmak", "Bukmak Constructions (Aboriginal-owned)", 2021, "Owned by the Arnhem Land Progress Association; $51.5M HomeBuild contract for 87 houses in Galiwin'ku.", "Territory Q", "https://territoryq.com.au/bukmak-boosted-by-51m-contract/"),
 ("consult", "Consultancies (EY, Deloitte and others)", 2013, "NT Government consultancy contracts: $33.6M in 2018-19 and $47.6M in 2019-20. EY's health contract grew from about $700,000 to over $4.3M without public tender; Deloitte reviewed school funding.", "NT Independent", "https://ntindependent.com.au/nt-governments-consultancy-contract-costs-continue-to-rise/"),
]
actors.append(dict(id="ntbudget", band="state", type="department", parent="ntg", col=14, label="NT budget and Treasury", era_labels="1978-2026:NT budget and Treasury", start_year=1978,
    summary="Where Commonwealth money arrives and is allocated. The Commonwealth Grants Commission sizes the NT's GST share largely by Aboriginal need; the NT decides where it is spent.",
    what_it_takes="Money assessed for Aboriginal need", source_title="NT Budget: revenue", source_url="https://budget.nt.gov.au/papers/guide/territory-governments-revenue", start_year_note="Self-government"))
for aid, label, st, summ, stt, su in NEW:
    actors.append(dict(id=aid, band="private", type="contractor", parent="", label=label, era_labels=f"{st}-2026:{label}", start_year=st, summary=summ, source_title=stt, source_url=su, start_year_note="First contract on record"))
order = {"private": ["churches", "pastoral", "south32", "glencore", "newmont", "gas", "indue", "consult", "mission", "oohc", "halikos", "njhomes", "bukmak"],
         "aboriginal": ["wett", "landcouncils", "aint", "rangers", "yilli", "acchos", "karu", "apont", "naaja", "anindilyakwa"]}
for a in actors:
    if a["band"] in order: a["col"] = order[a["band"]].index(a["id"]) + 1
write("actors.csv", A_COLS, actors)

ev = read("events.csv"); EV_COLS = list(ev[0].keys())
MOVE = {"Wave Hill walk-off": "land", "Whitlam hands land back to the Gurindji": "land", "Badari: High Court strikes down Remote Rent Framework": "housing",
        "Papunya tenants sue over heat": "housing", "Project Mangma stalled": "courts"}
for e in ev:
    if e["section"] == "nations": e["section"] = MOVE.get(e["title"], "land")
def E(year, actor, type_, title, detail, who, takes, figure, led, state, st, su, kind, status="verified", date=""):
    ev.append(dict(id=f"ev{len(ev)+1:03d}", year=year, date=date, section=actor, type=type_, title=title, detail=detail, actor=who, what_it_takes=takes, figure=figure,
                   aboriginal_led=led, state_account=state, source_title=st, source_url=su, source_kind=kind, status=status))
E(2020, "halikos", "contract", "$55.1M to build the Holtze youth prison", "Site placed next to the adult prison, against the Royal Commission's advice; Halikos had objected to the Don Dale site bordering its North Crest development, land the NT gave it free in 2016.", "NT Government", "", "$55.1M", "no", "The government denied moving the site at Halikos's request.", "NT Independent", "https://ntindependent.com.au/halikos-given-55-million-to-build-new-youth-prison-after-objecting-to-original-location/", "news", date="2020-07-16")
E(2026, "njhomes", "contract", "Katherine work camp, stage one", "99 beds, planned to expand to 198, at the CDU Katherine Rural Campus.", "NT Government", "", "$5.67M", "no", "", "Katherine Times", "https://www.katherinetimes.com.au/story/9290162/nj-homes-awarded-567m-katherine-work-camp-contract/", "news", date="2026-06")
E(2021, "bukmak", "contract", "87 houses for Galiwin'ku", "HomeBuild contract over five years to an Aboriginal-owned builder.", "NT Government", "", "$51.5M", "yes", "", "Territory Q", "https://territoryq.com.au/bukmak-boosted-by-51m-contract/", "news", date="2021-07")
E(2020, "consult", "contract", "EY health contract grows to $4.3M without tender", "Awarded April 2020 at about $700,000; referred to the ICAC.", "NT Government", "", "$4.3M", "no", "", "NT Independent", "https://ntindependent.com.au/nt-governments-consultancy-contract-costs-continue-to-rise/", "news")
E(2019, "consult", "data", "Consultancy contracts $47.6M a year", "2019-20; $33.6M in 2018-19. Infrastructure department the largest user.", "NT Government", "", "$47.6M", "no", "", "NT Independent", "https://ntindependent.com.au/nt-governments-consultancy-contract-costs-continue-to-rise/", "news")
E(2015, "ntbudget", "data", "GST assessed for Aboriginal need spent elsewhere", "Of $3.4B in Commonwealth Grants Commission assessments for 2015-16, 68% was assessed for Aboriginal people's needs, but the NT's own expenditure review found it spent 53%: about $500M went elsewhere (Yothu Yindi Foundation submission).", "NT Government", "Services for Aboriginal communities", "about $500M", "no", "The NT argued the system is fair and redistribution would widen disadvantage.", "The Guardian via inkl", "https://www.inkl.com/news/500m-meant-for-indigenous-services-was-spent-elsewhere-by-nt-government", "news")
E(2018, "ntbudget", "testimony", "'Ripped off countrymen in the bush'", "Former NT Aboriginal affairs minister Ken Vowles: 'We have ripped off countrymen in the bush for many, many years to prop up the [Darwin] northern suburbs.'", "Ken Vowles", "", "", "no", "", "NT Independent", "https://ntindependent.com.au/analysis-the-nt-government-has-been-misusing-federal-indigenous-disadvantage-money-for-years-and-the-feds-need-to-end-it/", "news", status="testimony")
for e in ev:
    if e["title"] in ("GST assessed for Aboriginal need spent elsewhere", "'Ripped off countrymen in the bush'"): e["section"] = "ntbudget"
write("events.csv", EV_COLS, ev)

fl = read("flows.csv"); F_COLS = list(fl[0].keys())
for f in fl:
    if f["to"] == "nations": f["to"] = "" if f["from"] == "ntg" else "aint"
    if f["from"] == "aint" and f["to"] == "aint": f["to"] = ""
def F(fr, to, y, ye, amt, per, kind, label, status, st, su, note=""):
    fl.append(dict(id=f"f{len(fl)+1:02d}", **{"from": fr}, to=to, year=y, end_year=ye, amount_aud=amt, per=per, kind=kind, label=label, status=status, source_title=st, source_url=su, note=note))
G = ("The Guardian via inkl", "https://www.inkl.com/news/500m-meant-for-indigenous-services-was-spent-elsewhere-by-nt-government")
F("cwlth", "ntbudget", 2015, 2015, 3400000000, "year", "GST assessment", "GST assessed by the Grants Commission (68% for Aboriginal need)", "verified", *G, "68% = about $2.3B assessed for Aboriginal need")
F("ntbudget", "", 2015, 2015, 500000000, "year", "diverted", "Assessed for Aboriginal need but spent elsewhere (53% spent)", "verified", *G, "Yothu Yindi Foundation analysis of the NT's own expenditure review")
F("custody", "halikos", 2020, 2020, 55100000, "contract", "contract", "Holtze youth detention centre build", "verified", "NT Independent", "https://ntindependent.com.au/halikos-given-55-million-to-build-new-youth-prison-after-objecting-to-original-location/")
F("custody", "njhomes", 2026, 2026, 5670000, "contract", "contract", "Katherine work camp stage one", "verified", "Katherine Times", "https://www.katherinetimes.com.au/story/9290162/nj-homes-awarded-567m-katherine-work-camp-contract/")
F("housing", "bukmak", 2021, 2026, 51500000, "5 years", "contract", "87 houses in Galiwin'ku (Aboriginal-owned builder)", "verified", "Territory Q", "https://territoryq.com.au/bukmak-boosted-by-51m-contract/")
F("health", "consult", 2020, 2020, 4300000, "contract", "contract", "EY health contract (no public tender)", "verified", "NT Independent", "https://ntindependent.com.au/nt-governments-consultancy-contract-costs-continue-to-rise/")
F("ntbudget", "consult", 2019, 2019, 47600000, "year", "contract", "All NT consultancy contracts 2019-20", "verified", "NT Independent", "https://ntindependent.com.au/nt-governments-consultancy-contract-costs-continue-to-rise/")
F("cwlth", "ntg", 2012, 2012, 2000000000, "year", "Indigenous expenditure", "Commonwealth direct spending on Aboriginal Territorians 2012-13", "verified", "Productivity Commission, Indigenous Expenditure Report 2014 (NT)", "https://assets.pc.gov.au/ongoing/indigenous-expenditure-report/2014/ier-2014-factsheet9-nt.pdf", "NT Government added $2.7B; 71% through mainstream services")
for f in fl:
    if f["from"] == "ntg": f["from"] = "ntbudget"
    if f["to"] == "ntg": f["to"] = "ntbudget"
write("flows.csv", F_COLS, fl)

oc = read("outcomes.csv"); O_COLS = list(oc[0].keys())
oc.append(dict(id=f"o{len(oc)+1:02d}", actor="ntbudget", year=2015, program="GST assessed for Aboriginal need", measure="Share of assessed GST spent on Aboriginal people", value="53% spent against 68% assessed; about $500M elsewhere", cost="$3.4B assessed", caveat="NT counts 95% of corrections spending as Indigenous expenditure because 95% of prisoners are Aboriginal", control="government", source_title=G[0], source_url=G[1], status="verified"))
oc.append(dict(id=f"o{len(oc)+1:02d}", actor="ntbudget", year=2012, program="Indigenous expenditure in the NT", measure="Public order and safety: share spent on Aboriginal people", value="70.6% of public order and safety spending; 29% of all Indigenous expenditure Indigenous-specific", cost="$4.7B total Indigenous expenditure, 55.7% of NT direct expenditure", caveat="Expenditure 'on' Aboriginal people includes police and prisons", control="government", source_title="Productivity Commission IER 2014 (NT)", source_url="https://assets.pc.gov.au/ongoing/indigenous-expenditure-report/2014/ier-2014-factsheet9-nt.pdf", status="verified"))
write("outcomes.csv", O_COLS, oc)

# ------------------------------------------------------------------ harm (deaths and injuries)
H_COLS = ["id", "actor", "year", "end_year", "kind", "measure", "value", "count", "scope", "note", "source_title", "source_url", "status"]
S282 = ("Justice not Jails, Submission 282 (2026)", "")
CD = ("NT Child Deaths Review and Prevention Committee via The Guardian (inkl)", "https://www.inkl.com/news/indigenous-overrepresented-in-every-category-of-child-or-infant-death-in-nt")
HM = [
 ("police", 1884, 1884, "killed", "Daly River massacre", "20-30 official; 'not less than 150' (Protector of Aborigines)", 150, "NT", "", "Colonial Frontier Massacres map", "https://c21ch.newcastle.edu.au/colonialmassacres/detail.php?r=704", "verified"),
 ("police", 1928, 1928, "killed", "Coniston massacre", "31 official; historians estimate at least double", 62, "NT", "Count uses the lower historians' estimate", "Central Land Council", "https://www.clc.org.au/wp-content/uploads/Coniston-Brochure-2018.pdf", "verified"),
 ("police", 1788, 1930, "killed", "Frontier massacres across Australia", "10,374 people killed in 438 recorded massacres; about half by police or government forces", "", "national", "", "SBS NITV", "https://www.sbs.com.au/nitv/article/the-massacre-maps-research-into-colonial-era-violence-has-revealed-its-final-grim-toll/e5enesien", "verified"),
 ("police", 1989, 2025, "died in custody", "Aboriginal deaths in NT police custody", "40 Aboriginal people (against 20 non-Indigenous), 1989-90 to 2024-25", 40, "NT", "", *S282, "verified"),
 ("police", 1991, 2025, "died in custody", "NT share of Aboriginal deaths in custody", "14.3% of deaths since 1991, against 7.8% of the First Nations population", "", "NT", "", *S282, "verified"),
 ("custody", 2024, 2024, "died in custody", "Indigenous deaths in custody, Australia, 2024-25", "33, the most since records began in 1979-80 (26 in prison)", "", "national", "", "NIT", "https://nit.com.au/11-12-2025/21758/record-deaths-in-custody-trigger-urgent-demands-for-commonwealth-action", "verified"),
 ("custody", 1991, 2026, "died in custody", "Indigenous deaths in custody since the Royal Commission", "634 (16 in 2026 to date)", "", "national", "", "AAP via Newcastle Herald", "https://www.newcastleherald.com.au/story/9255241/", "verified"),
 ("police", 2019, 2019, "died in custody", "Kumanjayi Walker, Yuendumu", "Shot by police", 1, "NT", "", "NIT", "https://nit.com.au/02-06-2025/18295/inquest-into-kumanjayi-walkers-death-delayed-as-yuendumu-mourns-another-death-in-police-custody", "verified"),
 ("police", 2025, 2025, "died in custody", "Kumanjayi White, Alice Springs", "Died after police restraint", 1, "NT", "", "NIT", "https://nit.com.au/02-06-2025/18295/inquest-into-kumanjayi-walkers-death-delayed-as-yuendumu-mourns-another-death-in-police-custody", "verified"),
 ("police", 2025, 2025, "died in custody", "Woman in Tennant Creek watch house", "Died; no nurse on duty", 1, "NT", "", "NIT", "https://nit.com.au/28-12-2025/21943/no-nurse-on-duty-as-indigenous-woman-dies-in-custody-from-medical-episode-in-tennant-creek", "verified"),
 ("childprot", 2011, 2015, "child deaths", "Child death rate, 2011-15", "138 per 100,000 Aboriginal children against 33 for non-Aboriginal children", "", "NT", "", *CD, "verified"),
 ("childprot", 2011, 2015, "child deaths", "Infant death rate, 2011-15", "1,479 per 100,000 Aboriginal infants against 284 non-Aboriginal", "", "NT", "", *CD, "verified"),
 ("childprot", 2011, 2015, "child deaths", "Child deaths in families known to child protection", "More than 25% of 242 child deaths", "", "NT", "", *CD, "verified"),
 ("oohc", 2024, 2025, "harmed in care", "Children allegedly harmed in care, 2024-25", "Nearly 1 in 3; most substantiated harm in purchased home-based care", "", "NT", "", "ABC", "https://www.abc.net.au/news/2026-06-02/almost-one-third-nt-children-in-care-harmed-commissioner-report/106747302", "verified"),
 ("childprot", 2017, 2017, "odds", "Children on care orders under youth justice supervision", "27 times more likely", "", "NT", "", "Royal Commission Vol 3B", "https://rmo.nt.gov.au/_media/documents/rcpdcnt/Royal-Commission-NT-Final-Report-Volume-3B.pdf", "verified"),
 ("childprot", 2022, 2023, "odds", "First Nations young people in both child protection and youth justice", "26 times more likely; 94% of those first supervised at 10 had child protection contact", "", "national", "", "NIT", "https://nit.com.au/25-10-2024/14474/truly-confronting-new-report-reveals-link-between-child-protection-and-youth-justice", "verified"),
 ("custody", 2021, 2023, "odds", "Released prisoners back within two years", "60.3%, highest in Australia", "", "NT", "", "Sentencing Advisory Council (ROGS)", "https://www.sentencingcouncil.vic.gov.au/sentencing-statistics/released-prisoners-returning-to-prison", "verified"),
 ("custody", 2026, 2026, "injured", "Child assaulted after transfer to Darwin", "Seriously assaulted by multiple detainees; ongoing medical complications", 1, "NT", "", "ABC", "https://www.abc.net.au/news/2026-02-03/naaja-scathing-submission-nt-youth-justice-national-inquiry/106297320", "verified"),
 ("police", 2018, 2018, "injured", "11-year-old pepper sprayed in a police van", "Hooded and handcuffed; 'in extreme distress' (Ombudsman); year to confirm", 1, "NT", "", "inkl / ABC", "https://www.inkl.com/news/after-cuffed-11yo-capsicum-sprayed-nt-police-deny-problem-with-managing-youth", "to source"),
 ("health", 2020, 2022, "years of life", "Life expectancy gap", "13.5 years (men) and 13.8 years (women) below non-Indigenous Territorians", "", "NT", "", "ABS", "https://www.abs.gov.au/AUSSTATS/abs@.nsf/DetailsPage/3302.0.55.0032015-2017", "verified"),
 ("health", 1997, 2005, "deaths", "Rheumatic heart disease deaths", "90% Indigenous; death rate about 55 times the non-Indigenous rate at age 50", "", "NT", "", "Colquhoun et al. 2015", "https://pmc.ncbi.nlm.nih.gov/articles/PMC4608059", "verified"),
 ("housing", 2025, 2025, "deaths", "Kumanjayi Fly, Mount Liebig", "A two-year-old's death the coroner found septic maintenance could have prevented", 1, "NT", "", "NAAJA, Submission 604 (2026)", "", "verified"),
 ("custody", 2011, 2011, "injured", "Hearing loss among Aboriginal prisoners", "94% tested had significant hearing loss", "", "NT", "", "Vanderpoll and Howard", "https://www.ilc.unsw.edu.au/sites/ilc.unsw.edu.au/files/articles/ILB%207-28%20Hearing%20Loss%20-%20Vanderpoll_Howard.pdf", "verified"),
]
write("harm.csv", H_COLS, [dict(zip(H_COLS, [f"d{i+1:02d}"] + list(h))) for i, h in enumerate(HM)])
print(len(actors), "actors;", len(ev), "events;", len(fl), "flows;", len(HM), "harm rows")
