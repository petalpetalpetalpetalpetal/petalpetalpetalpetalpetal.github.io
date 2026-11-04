"""Builds the CSV files in data/. Edit the CSVs directly afterwards; this script is only the first fill.
Run: python3 build_data.py
"""
import csv, os

OUT = os.path.join(os.path.dirname(__file__), "data")
os.makedirs(OUT, exist_ok=True)

def write(name, cols, rows):
    with open(os.path.join(OUT, name), "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, quoting=csv.QUOTE_MINIMAL)
        w.writeheader()
        for r in rows:
            w.writerow({c: r.get(c, "") for c in cols})

# ---------------------------------------------------------------- config
write("config.csv", ["key", "value", "note"], [
    {"key": "site_title", "value": "Taken, Year by Year", "note": "Page title"},
    {"key": "subtitle", "value": "How Commonwealth and Northern Territory institutions act on Aboriginal children and families, 1824 to today", "note": ""},
    {"key": "contact_email", "value": "petal.petal.petal.petal.petal@proton.me", "note": "Address that receives corrections"},
    {"key": "contact_note", "value": "Spotted an error, a missing source or a case that should be added? Email us with the item code below. Every message is read before anything changes.", "note": ""},
    {"key": "start_year", "value": "1824", "note": "First year on the slider"},
    {"key": "end_year", "value": "2026", "note": "Last year on the slider"},
    {"key": "default_year", "value": "2026", "note": "Year shown when the page opens"},
    {"key": "country_label", "value": "Country: sovereignty never ceded", "note": "Label of the band the map stands on"},
])

# ---------------------------------------------------------------- authorities (tier 0)
write("authorities.csv", ["id", "label", "start_year", "end_year", "position", "summary", "source_title", "source_url"], [
    {"id": "crown", "label": "British Crown (invading power)", "start_year": 1824, "end_year": 1862, "position": "centre",
     "summary": "Military forts built on Tiwi and Iwaidja Country: Fort Dundas (Melville Island, 1824-28), Fort Wellington (1827-29) and Port Essington (1838-49). Fort Dundas was abandoned after Tiwi resistance, cyclones and tropical conditions.",
     "source_title": "History of the Northern Territory (Wikipedia)", "source_url": "https://en.wikipedia.org/wiki/History_of_the_Northern_Territory"},
    {"id": "sa", "label": "South Australia", "start_year": 1863, "end_year": 1910, "position": "centre",
     "summary": "South Australia claimed the Territory by letters patent in 1863 and built Palmerston (Darwin) on Larrakia Country in 1869. Pastoral, mining and telegraph invasion followed, enforced by police-led massacres.",
     "source_title": "History of the Northern Territory (Wikipedia)", "source_url": "https://en.wikipedia.org/wiki/History_of_the_Northern_Territory"},
    {"id": "cwlth", "label": "Commonwealth of Australia", "start_year": 1911, "end_year": "", "position": "left",
     "summary": "Took control of the NT on 1 January 1911. Since 1978 it funds most NT services (over 70% of NT revenue in 2025-26) and runs income management, remote jobs and land rights law directly.",
     "source_title": "CityNews / AAP", "source_url": "https://citynews.com.au/2025/prison-spend-soars-to-cope-with-crackdown-on-bail-laws/"},
    {"id": "ntg", "label": "NT Administration (Commonwealth)", "start_year": 1911, "end_year": 1977, "position": "right",
     "summary": "The Commonwealth ran the Territory directly through an Administrator and its own branches (Chief Protector, later the Welfare Branch).",
     "source_title": "Bringing Them Home, ch. 9", "source_url": "https://www.humanrights.gov.au/our-work/bringing-them-home-chapter-9"},
    {"id": "ntg", "label": "NT Government", "start_year": 1978, "end_year": "", "position": "right",
     "summary": "Took over from the Commonwealth in 1978, with a Legislative Assembly headed by a Chief Minister. Runs police, courts, prisons, child protection, schools, housing and health on Aboriginal Country.",
     "source_title": "History of the Northern Territory (Wikipedia)", "source_url": "https://en.wikipedia.org/wiki/History_of_the_Northern_Territory"},
])

# ---------------------------------------------------------------- eras
write("eras.csv", ["id", "start_year", "end_year", "label", "summary", "source_title", "source_url"], [
    {"id": "e1", "start_year": 1824, "end_year": 1862, "label": "Invasion of the north coast", "summary": "British forts built on Tiwi and Iwaidja Country; all abandoned in the face of resistance and conditions.", "source_title": "History of the NT", "source_url": "https://en.wikipedia.org/wiki/History_of_the_Northern_Territory"},
    {"id": "e2", "start_year": 1863, "end_year": 1910, "label": "Frontier war and massacres", "summary": "South Australia claims the Territory; police and settlers massacre Aboriginal people to clear Country for pastoral runs, mines and the telegraph.", "source_title": "History of the NT", "source_url": "https://en.wikipedia.org/wiki/History_of_the_Northern_Territory"},
    {"id": "e3", "start_year": 1911, "end_year": 1952, "label": "Removal and confinement", "summary": "The Chief Protector is legal guardian of every Aboriginal child and controls Aboriginal women for life; children are stolen into compounds and missions.", "source_title": "Bringing Them Home, ch. 9", "source_url": "https://www.humanrights.gov.au/our-work/bringing-them-home-chapter-9"},
    {"id": "e4", "start_year": 1953, "end_year": 1972, "label": "Forced assimilation", "summary": "The Welfare Ordinance makes 15,711 Aboriginal Territorians wards of the state; child theft continues.", "source_title": "Indigenous Rights (NMA)", "source_url": "https://indigenousrights.net.au/civil_rights/albert_namatjira_and_citizenship,_1958-59/the_stud_book"},
    {"id": "e5", "start_year": 1973, "end_year": 1977, "label": "Land rights struggle", "summary": "Gurindji and other nations force land rights onto the agenda; the Land Rights Act passes in 1976.", "source_title": "Bringing Them Home, ch. 9", "source_url": "https://www.humanrights.gov.au/our-work/bringing-them-home-chapter-9"},
    {"id": "e6", "start_year": 1978, "end_year": 2006, "label": "Territory settler rule", "summary": "The NT Government takes control of police, prisons and child protection; Aboriginal deaths in custody force a Royal Commission (1991).", "source_title": "History of the NT", "source_url": "https://en.wikipedia.org/wiki/History_of_the_Northern_Territory"},
    {"id": "e7", "start_year": 2007, "end_year": 2012, "label": "The Intervention", "summary": "The Commonwealth suspends the Racial Discrimination Act to impose income management, alcohol bans, compulsory leases, police and the army.", "source_title": "NT National Emergency Response (Wikipedia)", "source_url": "https://en.wikipedia.org/wiki/Northern_Territory_National_Emergency_Response"},
    {"id": "e8", "start_year": 2013, "end_year": 2023, "label": "Intervention continued", "summary": "Intervention measures continue under new names; torture of children in Don Dale is exposed (2016).", "source_title": "Royal Commission (Wikipedia)", "source_url": "https://en.wikipedia.org/wiki/Royal_Commission_into_the_Protection_and_Detention_of_Children_in_the_Northern_Territory"},
    {"id": "e9", "start_year": 2024, "end_year": 2026, "label": "Mass incarceration and removal", "summary": "Criminal responsibility back to age 10, spit hoods back, the Child Placement Principle weakened, record imprisonment of Aboriginal people.", "source_title": "NAAJA", "source_url": "https://www.naaja.org.au/aboriginal-people-continue-to-be-locked-up-at-record-levels-putting-lives-at-risk/"},
])

# ---------------------------------------------------------------- sections (tier 1)
S = [
 # id, parent, col, label, start, end, stages, era_labels, summary, takes, aboriginal_led
 ("missions", "cwlth", 1, "Missions and compounds", 1913, 1980, "3", "1913-1980:Missions and compounds",
  "Government compounds and church missions that held children removed from their families.",
  "Family, language and Country", "Survivors' testimony to Bringing Them Home (1997)"),
 ("income", "cwlth", 2, "Income and work", 1863, "", "2", "1863-1967:Rations and stolen wages|1968-2006:Award wages and CDEP|2007-2026:Income management and CDP",
  "Who controls Aboriginal people's pay and welfare.",
  "Control of a family's own money and labour", "Wave Hill walk-off (1966); community-run CDEP"),
 ("land", "cwlth", 3, "Land and rangers", 1824, "", "", "1824-1862:Invaded Country|1863-1975:Dispossession for pastoral runs|1976-2026:Land rights and land councils",
  "Who holds and decides over land and water.",
  "Country and authority over it", "Wave Hill walk-off; land councils; ranger groups"),
 ("dev", "ntg", 4, "Development powers", 1978, "", "", "1978-2026:Development and resources",
  "NT powers to fast-track mining, gas and major projects.",
  "Say over development on Country", "Land councils and Nurrdalinji native title holders"),
 ("housing", "ntg", 5, "Housing and homelands", 1911, "", "1", "1911-1971:Reserves and confinement|1972-2026:Housing and homelands",
  "Remote, town camp and public housing, shelters, and evacuation.",
  "Safe shelter", "Papunya tenants' heat case; Badari High Court win; YiSSA"),
 ("health", "ntg", 6, "Health and alcohol services", 1911, "", "1", "1911-2026:Health and alcohol services",
  "Preventable disease, life expectancy, rehab and sobering-up services.",
  "Years of life", "AMSANT, Danila Dilba and Congress"),
 ("schools", "ntg", 7, "Schools", 1950, "", "4", "1950-1977:Welfare Branch schools|1978-2026:Schools",
  "Schools, language of teaching, funding, attendance enforcement and boarding.",
  "Education in the child's own language", "Bilingual schools; Aboriginal Assistant Teachers"),
 ("childprot", "ntg", 8, "Child removal and protection", 1910, "", "3", "1910-1952:Chief Protector (child theft)|1953-1977:Welfare Branch (wardship)|1978-2025:Child protection|2026-2026:Child protection (Every Child Matters Act)",
  "The agency that removes Aboriginal children and decides where they live.",
  "Family, language and Country", "Kin who come forward to care; SNAICC"),
 ("police", "ntg", 9, "Police and watch houses", 1870, "", "5", "1870-1910:Mounted Police (South Australia)|1911-1977:NT Police (Commonwealth)|1978-2026:NT Police",
  "Arrest, watch houses, protective custody and use of force.",
  "Liberty, and sometimes life", "NAAJA custody notification; families seeking justice"),
 ("courts", "ntg", 10, "Courts and bail", 1869, "", "6", "1869-2026:Courts and bail",
  "Criminal responsibility, bail, remand and the legal tests for genocide.",
  "Liberty without a finding of guilt", "Project Mangma; NAAJA"),
 ("custody", "ntg", 11, "Prisons and youth detention", 1883, "", "7|8", "1883-2026:Prisons and youth detention",
  "Youth detention, adult prisons, transfers and rehabilitation inside.",
  "Years of life with kin, and Country", "Anindilyakwa justice; Justice not Jails drivers"),
 ("legal", "ntg", 12, "Legal help and interpreters", 1972, "", "6|9", "1972-2026:Legal help and interpreters",
  "Aboriginal legal services, Legal Aid NT and the Aboriginal Interpreter Service.",
  "Being heard in your own language", "NAAJA; Aboriginal interpreters"),
]
write("sections.csv", ["id", "parent", "col", "label", "start_year", "end_year", "stages", "era_labels", "summary", "what_it_takes", "aboriginal_led", "start_year_note"],
      [dict(zip(["id", "parent", "col", "label", "start_year", "end_year", "stages", "era_labels", "summary", "what_it_takes", "aboriginal_led"], s),
            start_year_note="Approximate first year shown; edit if a better date is sourced") for s in S])

# ---------------------------------------------------------------- mechanisms (tier 2)
M = [
 # id, section, label, start, end, stage, limb, summary, takes
 ("m_kahlin", "missions", "Kahlin Compound and Half-Caste Home", 1913, 1939, "3", "e", "Darwin compound where removed children were kept in dormitories; inmates moved to Bagot in 1939.", "Family"),
 ("m_bungalow", "missions", "The Bungalow (Alice Springs)", 1914, 1942, "3", "e", "Home for removed children in Stuart, moved to Jay Creek (1928) and Temple Bar (1932).", "Family, Country"),
 ("m_retta", "missions", "Retta Dixon Home", 1946, 1980, "3", "e", "Darwin home opened after the war with 51 children, peaking at 120.", "Family"),
 ("m_south", "missions", "Removal to southern states", 1942, 1970, "3", "e", "Children evacuated south in 1942; from 1955 the Commonwealth sent part-Aboriginal children to southern foster homes and schools.", "Country"),
 ("m_rations", "income", "Rations and stolen wages", 1863, 1968, "2", "c", "Aboriginal stock workers paid in rations or below award; paying more than a set amount was illegal until 1968.", "Labour and pay"),
 ("m_cdep", "income", "CDEP (community-run work)", 1977, 2007, "2", "", "Community Development Employment Projects, run by communities; abolished by the Intervention.", ""),
 ("m_im", "income", "Compulsory income management", 2007, 2033, "2", "c", "Half of welfare quarantined on a card; extended to 2033.", "Control of money"),
 ("m_cdp", "income", "CDP and RJED remote jobs", 2015, "", "2", "c", "Community Development Program penalties, replaced by RJED from November 2025.", "Income"),
 ("m_pastoral", "land", "Dispossession for pastoral runs", 1863, "", "", "c", "Land taken for pastoral leases; Aboriginal people confined to reserves and stations.", "Country"),
 ("m_landrights", "land", "Land Rights Act and land councils", 1976, "", "", "", "Over 50% of NT land and 85% of its coastline is Aboriginal land.", ""),
 ("m_leases", "land", "Compulsory five-year leases", 2007, 2012, "", "c", "Intervention leases over township land.", "Control of community land"),
 ("m_rangers", "land", "Aboriginal ranger grants", 2017, "", "", "", "NT ranger grants, $12M over four years, dropped in 2025.", "Jobs on Country"),
 ("m_tc", "dev", "Territory Coordinator", 2025, "", "", "c", "Power to fast-track projects and override NT laws including the Heritage Act.", "Say over development"),
 ("m_beetaloo", "dev", "Beetaloo gas", 2018, "", "", "c", "Fracking exploration with public grants; native title holders object.", "Water and Country"),
 ("m_reserves", "housing", "Reserves and confinement", 1911, 1971, "1", "c", "People moved onto government settlements and reserves.", "Country"),
 ("m_overcrowd", "housing", "Remote overcrowding", 2007, "", "1", "c", "54% of remote community houses overcrowded (2022).", "Safe shelter"),
 ("m_deal", "housing", "Remote housing agreements", 2008, "", "1", "", "Joint Commonwealth-NT housing deals; $4B agreement from 2024, behind schedule.", ""),
 ("m_rent", "housing", "Remote rent and tenants' rights", 2023, "", "1", "c", "Remote Rent Framework struck down in Badari (2025); NT amends the Housing Act.", "Say over rent"),
 ("m_shelter", "housing", "Short-stay shelter and evacuation", 2023, "", "1", "c", "Flood evacuations to Darwin; YiSSA closure in 2026.", "Shelter near family"),
 ("m_rhd", "health", "Rheumatic heart disease", 1997, "", "1", "c", "1 in 17 First Nations Territorians live with RHD or ARF history (2024).", "Health"),
 ("m_life", "health", "Life expectancy", 2015, "", "", "c", "Aboriginal Territorians live 13.5 to 13.8 years less than non-Indigenous Territorians.", "Years of life"),
 ("m_hearing", "health", "Childhood hearing loss", 2011, "", "4", "c", "94% of Aboriginal prisoners tested had significant hearing loss.", "Being heard"),
 ("m_floor", "health", "Alcohol floor price", 2018, 2025, "", "", "$1.30 minimum unit price, scrapped February 2025.", ""),
 ("m_rehab", "health", "Rehab and sobering-up", 2024, "", "8", "b", "Darwin's only residential rehab and sobering-up shelter closed 2024; parole rehab cut.", "Exits from custody"),
 ("m_bilingual", "schools", "Bilingual education", 1973, "", "4", "", "Cut or targeted in 1980, 1998, 2008 and 2024; 21 schools in 1991, eight now.", "Language"),
 ("m_funding", "schools", "Funding by attendance", 2013, 2025, "4", "", "'Effective enrolment' sent money away from Aboriginal students.", "School resources"),
 ("m_attend", "schools", "Attendance", 2014, "", "4", "", "Schools reached Aboriginal students 54.7% of the time in 2025.", "Education"),
 ("m_truancy", "schools", "Truancy fines and income referrals", 2025, "", "4", "c", "Parents fined or referred to income management.", "Control of money"),
 ("m_protector", "childprot", "Chief Protector guardianship", 1910, 1957, "3", "e", "Chief Protector legal guardian of every Aboriginal child to 18; control of women for life (1918).", "Family"),
 ("m_wards", "childprot", "Wardship (Welfare Ordinance)", 1953, 1964, "3", "e", "Director of Welfare guardian of all 'wards'; 15,711 named on the 1957 register.", "Legal personhood"),
 ("m_acpp", "childprot", "Child Placement Principle", 1983, "", "3", "e", "In NT law since 1983; applies only 'as far as practicable' from 2026.", "Placement with kin"),
 ("m_kin", "childprot", "Kin placement", 2017, "", "3", "e", "Only 16.7% of children in care placed with kin (2026).", "Family"),
 ("m_oohc", "childprot", "Out-of-home care contracts", 2017, "", "3", "", "93% of $143.4M paid to non-government providers.", ""),
 ("m_mounted", "police", "Mounted police and massacres", 1870, 1933, "5", "a", "Police and settler reprisals, including Daly River (1884) and Coniston (1928).", "Life"),
 ("m_pubdrink", "police", "Public drinking offence", 2019, "", "5", "b", "Decriminalised in 2019 in line with the Royal Commission; re-criminalised October 2024.", "Liberty"),
 ("m_custody", "police", "Arrests and watch houses", 2020, "", "5", "b", "About 40 Aboriginal people a day taken into custody from December 2024.", "Liberty"),
 ("m_force", "police", "Use of force and weapons", 2017, "", "5", "b", "Spit hoods banned 2017, reinstated 2025; armed public safety officers; OC spray legal for the public.", "Safety"),
 ("m_deaths", "police", "Deaths in custody", 1980, "", "9", "a", "634 Indigenous deaths in custody nationally since 1991.", "Life"),
 ("m_recruit", "police", "Who polices", 2019, "", "5", "", "Ex-military and overseas recruitment.", ""),
 ("m_age", "courts", "Age of criminal responsibility", 1983, "", "5", "b", "10, raised to 12 in 2023, lowered to 10 in October 2024.", "Childhood"),
 ("m_doli", "courts", "Doli incapax (10 to 13)", 1983, "", "6", "b", "Children 10-13 presumed incapable of criminal intent, yet remanded.", "Liberty"),
 ("m_bail", "courts", "Bail laws", 2024, "", "6", "b", "Declan's Law (2024); last-resort principle removed (2025).", "Liberty"),
 ("m_remand", "courts", "Remand", 2024, "", "6", "b", "Youth remand averages 56 days; 41% of NT prisoners on remand (Nov 2025).", "Liberty without guilt"),
 ("m_mandatory", "courts", "Mandatory sentencing", 1997, 2001, "8", "b", "Mandatory jail for property offences, repealed 2001.", "Liberty"),
 ("m_genocide", "courts", "Genocide in Australian law", 1997, "", "", "", "Kruger (1997), Nulyarimma (1999), and the Attorney-General's consent gate since 2002.", "Access to a court"),
 ("m_youthdet", "custody", "Youth detention", 2016, "", "7", "b", "Don Dale footage (2016); Holtze the only youth centre from November 2024.", "Family"),
 ("m_transfer", "custody", "Transfers Alice Springs to Darwin", 2024, "", "7", "e", "60 children moved in 10 months; handcuffed commercial flights.", "Country"),
 ("m_prison", "custody", "Adult imprisonment", 1883, "", "8", "b", "4,515 per 100,000 Aboriginal adults (June 2026).", "Years with kin"),
 ("m_programs", "custody", "Programs inside", 2024, "", "8", "", "10 of 11 drug and alcohol sessions cancelled in six months.", "A way out"),
 ("m_naaja", "legal", "Aboriginal legal services (NAAJA)", 1972, "", "6", "", "Represents about 65% of everyone in NT criminal matters; Commonwealth-funded.", ""),
 ("m_ais", "legal", "Aboriginal Interpreter Service", 2000, "", "6", "", "Fills about half of requests; most interpreters casual.", "Being heard"),
 ("m_legalaid", "legal", "Legal Aid NT", 1990, "", "6", "", "Stopped new criminal grants for people not in custody.", "Representation"),
]
write("mechanisms.csv", ["id", "section", "label", "start_year", "end_year", "stage", "limb", "summary", "what_it_takes"],
      [dict(zip(["id", "section", "label", "start_year", "end_year", "stage", "limb", "summary", "what_it_takes"], m)) for m in M])

# ---------------------------------------------------------------- events
EV_COLS = ["id", "year", "end_year", "date", "section", "mechanism", "type", "title", "detail", "actor",
           "what_it_takes", "limb", "figure", "aboriginal_led", "state_account", "source_title", "source_url",
           "source_kind", "status", "stage", "tags"]
EV = []
def E(year, section, mechanism, type_, title, detail, actor="", takes="", limb="", figure="", led="no",
      state="", st="", su="", kind="", status="verified", date="", end="", stage="", tags=""):
    EV.append(dict(id=f"ev{len(EV)+1:03d}", year=year, end_year=end, date=date, section=section, mechanism=mechanism,
                   type=type_, title=title, detail=detail, actor=actor, what_it_takes=takes, limb=limb, figure=figure,
                   aboriginal_led=led, state_account=state, source_title=st, source_url=su, source_kind=kind,
                   status=status, stage=stage, tags=tags))

BTH = ("Bringing Them Home, ch. 9 (AHRC)", "https://www.humanrights.gov.au/our-work/bringing-them-home-chapter-9")
HNT = ("History of the Northern Territory (Wikipedia)", "https://en.wikipedia.org/wiki/History_of_the_Northern_Territory")
NTER = ("NT National Emergency Response (Wikipedia)", "https://en.wikipedia.org/wiki/Northern_Territory_National_Emergency_Response")
RC17 = ("Royal Commission into the Protection and Detention of Children in the NT (Wikipedia)", "https://en.wikipedia.org/wiki/Royal_Commission_into_the_Protection_and_Detention_of_Children_in_the_Northern_Territory")
NAAJA_REC = ("NAAJA: record incarceration", "https://www.naaja.org.au/aboriginal-people-continue-to-be-locked-up-at-record-levels-putting-lives-at-risk/")
S604 = ("NAAJA, Submission 604, racism inquiry (2026)", "")
S282 = ("Justice not Jails, Submission 282, racism inquiry (2026)", "")
S493 = ("Northern Land Council, Submission 493, racism inquiry (2026)", "")
S624 = ("ATESOL NT, Submission 624, racism inquiry (2026)", "")
S209 = ("Eric Fejo, Submission 209, racism inquiry (2026)", "")
BUDGET = ("AAP via Shepparton News: NT budget 2026/27", "https://www.sheppnews.com.au/national/northern-territory-budgets-hundreds-more-prison-beds/")
ABC_NAAJA = ("ABC: NAAJA youth justice submission (3 Feb 2026)", "https://www.abc.net.au/news/2026-02-03/naaja-scathing-submission-nt-youth-justice-national-inquiry/106297320")

# --- colonial frontier
E(1824, "land", "", "invasion", "British fort built on Tiwi Country", "Fort Dundas, the first British fort in northern Australia, on Melville Island; abandoned in 1828 after Tiwi resistance, cyclones and tropical conditions.", "British Crown", "Country", "", "", "no", "", *HNT, "reference", tags="settlement")
E(1838, "land", "", "invasion", "British fort at Port Essington", "Fort Victoria built on Iwaidja Country on the Cobourg Peninsula in October 1838; abandoned in December 1849.", "British Crown", "Country", "", "", "no", "", *HNT, "reference", tags="settlement")
E(1863, "land", "m_pastoral", "invasion", "South Australia claims the Territory", "Letters patent place Aboriginal Country under South Australia, opening it to survey and sale.", "South Australia", "Country", "c", "", "no", "", *HNT, "reference", tags="annexation")
E(1869, "land", "m_pastoral", "invasion", "Palmerston (Darwin) built on Larrakia Country", "Surveyor-General George Goyder establishes a settlement of 135 colonists.", "South Australia", "Country", "", "", "no", "", *HNT, "reference", tags="settlement")
E(1884, "police", "m_mounted", "violence", "Daly River massacre", "After four miners were killed at the Mt Hayward copper mine, police (Mounted Constable George Montagu, Inspector Paul Foelsche) and a civilian party led reprisals against Malak Malak, Woolwonga and Murrinh-patha people. Official estimate 20-30 dead; the Protector of Aborigines said 'not less than 150'.", "SA Mounted Police and settlers", "Life", "a", "20-30 official; up to 150", "no", "Police report put deaths at 20-30.", "Colonial Frontier Massacres map, Daly River", "https://c21ch.newcastle.edu.au/colonialmassacres/detail.php?r=704", "academic", date="1884-10", tags="massacre")
E(1889, "police", "m_mounted", "violence", "Jampawurru (Red Lily Spring) massacre", "Seven or eight Aboriginal men killed by a party including Gordon Buchanan.", "Settlers", "Life", "a", "7-8 killed", "no", "", "Australian Frontier Conflicts: NT", "https://australianfrontierconflicts.com.au/some-known-frontier-conflicts-in-the-northern-territory/", "academic", tags="massacre")
E(1892, "police", "m_mounted", "violence", "Police killings at Corella and Cresswell Downs", "Police-led expedition at Corella and Cresswell Downs after two settlers were killed; Aboriginal people killed, number unrecorded.", "SA Mounted Police", "Life", "a", "", "no", "", "Australian Frontier Conflicts: NT", "https://australianfrontierconflicts.com.au/some-known-frontier-conflicts-in-the-northern-territory/", "academic", tags="massacre")

# --- Commonwealth and the Chief Protector
E(1910, "childprot", "m_protector", "law", "Northern Territory Aboriginals Act", "The Chief Protector becomes 'legal guardian of every Aboriginal and every half-caste child up to the age of 18 years'.", "South Australia", "Family", "e", "", "no", "", *BTH, "government", tags="removal")
E(1911, "childprot", "m_protector", "law", "Commonwealth takes over; Chief Protector's powers", "On 1 January 1911 the Commonwealth takes control of the NT. Its Ordinance gives the Chief Protector 'the care, custody or control of any Aboriginal or half caste'. These powers last until 1957.", "Commonwealth", "Family", "e", "", "no", "", *BTH, "government", tags="removal")
E(1913, "missions", "m_kahlin", "institution", "Kahlin Compound opens", "Compound outside Darwin; girls kept in dormitories described as 'like birds in a cage'.", "Commonwealth", "Family", "e", "", "no", "", *BTH, "government", tags="removal")
E(1914, "missions", "m_bungalow", "institution", "The Bungalow opens in Stuart (Alice Springs)", "Removals of light-skinned children from Aboriginal camps begin.", "Commonwealth", "Family, Country", "e", "", "no", "", *BTH, "government", tags="removal")
E(1918, "childprot", "m_protector", "law", "Aboriginals Ordinance 1918", "The Chief Protector controls Aboriginal women 'from the moment they were born until they died', unless married to a man 'substantially of European origin'. In 1997 the High Court held (Kruger) that the Ordinance did not authorise genocide as the Convention defines it.", "Commonwealth", "Family, bodily autonomy", "e", "", "no", "", *BTH, "government", tags="removal")
E(1924, "missions", "m_kahlin", "institution", "Half-Caste Home opens in Darwin", "Separates Compound families.", "Commonwealth", "Family", "e", "", "no", "", *BTH, "government", tags="removal")
E(1928, "police", "m_mounted", "violence", "Coniston massacre", "Reprisal raids led by Constable George Murray after Frederick Brooks was killed at Yurrkuru. The Board of Enquiry found 31 Aboriginal people killed and said the party acted in self-defence; historians estimate at least double. The Board heard no Aboriginal witnesses except tracker Paddy and Aboriginal people had no counsel.", "NT Police and settlers", "Life", "a", "31 official; at least double estimated", "no", "Board of Enquiry: 'self-defence'.", "Central Land Council: Coniston", "https://www.clc.org.au/wp-content/uploads/Coniston-Brochure-2018.pdf", "sector", date="1928-08", tags="massacre")
E(1928, "courts", "m_genocide", "inquiry", "Coniston Board of Enquiry clears police", "Found the killings justified as self-defence, with evidence not made public.", "Commonwealth", "Justice", "", "", "no", "", "Central Land Council: Coniston", "https://www.clc.org.au/wp-content/uploads/Coniston-Brochure-2018.pdf", "sector", tags="impunity")
E(1929, "missions", "m_kahlin", "inquiry", "Bleakley report", "Estimates about 8,000 'half-castes' among roughly 21,000 Aboriginal people; finds institutions 'badly situated, inadequately financed and insufficiently supervised'.", "Commonwealth", "", "", "", "no", "", *BTH, "government")
E(1935, "missions", "m_bungalow", "data", "132 children at The Bungalow", "Then at Temple Bar.", "Commonwealth", "Family", "e", "132 children", "no", "", *BTH, "government")
E(1939, "missions", "m_kahlin", "policy", "McEwen's 'New Deal'", "Increases government control over people of mixed descent; Half-Caste Home inmates moved to Bagot Compound.", "Commonwealth", "Family", "e", "", "no", "", *BTH, "government", tags="assimilation")
E(1942, "missions", "m_south", "policy", "Children evacuated south after Darwin is bombed", "Mission children sent to homes in SA, NSW and Victoria.", "Commonwealth and missions", "Country", "e", "", "no", "", *BTH, "government")
E(1946, "missions", "m_retta", "institution", "Retta Dixon Home opens", "Opens after the war with 51 children, later peaking at 120; operates until 1980.", "Missions", "Family", "e", "51 to 120 children", "no", "", *BTH, "government")
E(1951, "childprot", "m_protector", "policy", "Removal age instructions", "Instructions limit removal of children under four, later lowered to three months.", "Commonwealth", "Family", "e", "", "no", "", *BTH, "government")
E(1953, "childprot", "m_wards", "law", "Welfare Ordinance 1953", "Repeals the 1918 Ordinance; the Director of Welfare becomes guardian of all 'wards'. A 1953 inquiry calls Retta Dixon 'a failure'.", "Commonwealth", "Legal personhood", "e", "", "no", "", *BTH, "government", tags="wardship")
E(1955, "missions", "m_south", "policy", "Southern fostering scheme", "The Commonwealth begins sending part-Aboriginal children to foster homes and schools in southern states, until the late 1960s.", "Commonwealth", "Country", "e", "", "no", "", *BTH, "government")
E(1957, "childprot", "m_wards", "law", "Register of Wards gazetted", "15,711 Aboriginal Territorians named as wards; only six full-descent people left off, including Albert Namatjira. Barry Christophers called it 'an instrument of torture against the Aborigines'.", "Commonwealth", "Legal personhood", "e", "15,711 wards", "no", "", "National Museum: the Stud Book", "https://indigenousrights.net.au/civil_rights/albert_namatjira_and_citizenship,_1958-59/the_stud_book", "reference", date="1957-05-13", tags="wardship")
E(1964, "childprot", "m_wards", "law", "Social Welfare Ordinance", "Reserve entry limited to people 'socially or economically in need of assistance'.", "Commonwealth", "", "", "", "no", "", *BTH, "government")
E(1965, "income", "m_rations", "court", "Equal wage decision deferred", "Equal wages for Aboriginal stockmen were decided but deferred three years after pastoralists said it would ruin the industry.", "Arbitration Commission", "Pay", "c", "", "no", "Pastoralists: equal pay would ruin the industry.", "Creative Spirits: Wave Hill", "https://www.creativespirits.info/aboriginalculture/politics/aboriginal-people-strike-walk-off-at-wave-hill", "reference")
E(1966, "land", "m_pastoral", "resistance", "Wave Hill walk-off", "On 23 August 1966 about 200 Gurindji stockmen and families, led by Vincent Lingiari, walk off Wave Hill station.", "Gurindji people", "", "", "about 200 people", "yes", "", "Creative Spirits: Wave Hill", "https://www.creativespirits.info/aboriginalculture/politics/aboriginal-people-strike-walk-off-at-wave-hill", "reference", date="1966-08-23", tags="resistance")
E(1967, "childprot", "m_wards", "data", "18% of Aboriginal children in government care", "Almost 18% of Territory Indigenous children in government care in 1967-68.", "Commonwealth", "Family", "e", "almost 18%", "no", "", *BTH, "government")
E(1968, "income", "m_rations", "law", "Equal wages take effect", "Paying Aboriginal workers more than a set amount in goods and money had been illegal until 1968.", "Commonwealth", "", "", "", "no", "", "Creative Spirits: Wave Hill", "https://www.creativespirits.info/aboriginalculture/politics/aboriginal-people-strike-walk-off-at-wave-hill", "reference")
E(1971, "childprot", "m_wards", "data", "97% of children in foster care Indigenous", "", "Commonwealth", "Family", "e", "97%", "no", "", *BTH, "government")
E(1973, "schools", "m_bilingual", "policy", "Assimilation policy formally abandoned", "Policy shifts from assimilation to self-management. Bilingual education begins in NT schools around this time (date to confirm).", "Commonwealth", "", "", "", "no", "", *BTH, "government", status="to source")
E(1975, "land", "m_pastoral", "resistance", "Whitlam hands land back to the Gurindji", "On 16 August 1975 Gough Whitlam pours soil into Vincent Lingiari's hands.", "Gurindji people", "", "", "", "yes", "", "Creative Spirits: Wave Hill", "https://www.creativespirits.info/aboriginalculture/politics/aboriginal-people-strike-walk-off-at-wave-hill", "reference", date="1975-08-16", tags="resistance")
E(1976, "land", "m_landrights", "law", "Aboriginal Land Rights (NT) Act", "Passed 16 December 1976, operating from 26 January 1977; creates the land councils.", "Commonwealth", "", "", "", "yes", "", *HNT, "reference", date="1976-12-16", tags="land rights")
E(1977, "income", "m_cdep", "policy", "CDEP begins", "Community Development Employment Projects, run by communities (start year to confirm).", "Commonwealth", "", "", "", "yes", "", *S493, "testimony", status="to source")
E(1978, "courts", "", "law", "NT Government takes control", "The Commonwealth hands the Territory to an NT Legislative Assembly with a Chief Minister.", "Commonwealth", "", "", "", "no", "", *HNT, "reference", date="1978-07-01")
E(1979, "childprot", "m_acpp", "resistance", "Karu Aboriginal child care agency founded", "", "Aboriginal community", "", "", "", "yes", "", *BTH, "government", tags="community control")
E(1980, "schools", "m_bilingual", "cut", "First move to end bilingual education", "The NT moved to end bilingual education in 1980, 1998, 2008 and 2024, never consulting communities first.", "NT Government", "Language", "", "", "no", "", *S624, "sector")
E(1983, "childprot", "m_acpp", "law", "Child Placement Principle enters NT law", "The Community Welfare Act is the first NT law to include the Aboriginal Child Placement Principle.", "NT Government", "", "", "", "no", "", *BTH, "government")
E(1983, "courts", "m_age", "law", "Age of criminal responsibility set at 10", "Under the NT Criminal Code (year to confirm).", "NT Government", "Childhood", "b", "10 years", "no", "", "", "", "", status="to source")
E(1987, "police", "m_deaths", "inquiry", "Royal Commission into Aboriginal Deaths in Custody begins", "Announced 10 August 1987; examined 99 deaths from 1980 to 1989.", "Commonwealth", "", "", "99 deaths examined", "no", "", "National Archives: RCIADIC", "https://www.naa.gov.au/explore-collection/first-australians/royal-commission-aboriginal-deaths-custody", "government", date="1987-08-10")
E(1991, "schools", "m_bilingual", "data", "Bilingual education at its peak", "21 schools in 17 languages.", "Communities and schools", "", "", "21 schools, 17 languages", "yes", "", *S624, "sector")
E(1991, "police", "m_deaths", "inquiry", "Royal Commission final report", "Signed 15 April 1991 with 339 recommendations.", "Commonwealth", "", "", "339 recommendations", "no", "", "National Archives: RCIADIC", "https://www.naa.gov.au/explore-collection/first-australians/royal-commission-aboriginal-deaths-custody", "government", date="1991-04-15")
E(1997, "courts", "m_mandatory", "law", "Mandatory sentencing for property offences", "Introduced 1997, repealed 2001 (dates to confirm against legislation).", "NT Government", "Liberty", "b", "", "no", "", "", "", "", status="to source")
E(1997, "courts", "m_genocide", "court", "Kruger v Commonwealth", "NT Stolen Generations plaintiffs lose; the High Court holds the 1918 Ordinance did not authorise genocide as the Convention defines it.", "High Court", "Access to justice", "e", "", "no", "", "International Crimes Database: Kruger", "https://www.internationalcrimesdatabase.org/Case/1041/Kruger-v-The-Commonwealth-of-Australia/", "court")
E(1997, "childprot", "m_protector", "inquiry", "Bringing Them Home", "Finds forced-removal policies fell within the international definition of genocide.", "Human Rights and Equal Opportunity Commission", "", "e", "", "no", "", "AHRC: Stolen Generations", "https://bullying.humanrights.gov.au/sites/default/files/content/pdf/social_justice/submissions_un_hr_committee/6_stolen_generations.pdf", "government")
E(1998, "schools", "m_bilingual", "cut", "Second move to end bilingual education", "", "NT Government", "Language", "", "", "no", "", *S624, "sector")
E(1999, "courts", "m_genocide", "court", "Nulyarimma v Thompson", "Federal Court holds 2:1 that genocide is not a crime in Australian law without legislation; Merkel J dissents.", "Federal Court", "Access to a court", "", "", "no", "", "Nulyarimma v Thompson (Wikipedia)", "https://en.wikipedia.org/wiki/Nulyarimma_v_Thompson", "reference")
E(2002, "courts", "m_genocide", "law", "Genocide offence with Attorney-General's consent gate", "Division 268 of the Criminal Code from 1 September 2002; any prosecution needs the Attorney-General's written consent (s 268.121).", "Commonwealth", "Access to a court", "", "", "no", "Consent is standard for universal-jurisdiction crimes.", "Mondaq: Senate on AG consent", "https://webiis08.mondaq.com/australia/crime/1549696/senate-recommends-rejecting-removal-of-requirement-for-ags-consent-to-prosecute-genocide", "news", date="2002-09-01")

# --- Intervention
E(2007, "income", "m_im", "law", "The Intervention", "Announced 21 June 2007, legislated in August. Income management, alcohol and pornography bans, compulsory five-year leases, suspended permits, CDEP abolished, extra police with army support. The Racial Discrimination Act exemption ran until 2010; only two of the 97 Little Children are Sacred recommendations were implemented.", "Commonwealth", "Control of money, land and movement", "c", "", "no", "Child protection emergency.", *NTER, "reference", date="2007-06-21", tags="intervention")
E(2007, "income", "m_cdep", "cut", "CDEP abolished", "Replaced with work for the dole, which NLC chair Matthew Ryan calls 'modern slavery'. Under CDEP people 'were happier and healthy in the homelands and the community'.", "Commonwealth", "Work", "c", "", "no", "", *S493, "testimony", tags="intervention")
E(2007, "land", "m_leases", "law", "Compulsory five-year leases", "Over township land in prescribed communities.", "Commonwealth", "Control of land", "c", "", "no", "", *NTER, "reference", tags="intervention")
E(2008, "schools", "m_bilingual", "cut", "Third move against bilingual education", "", "NT Government", "Language", "", "", "no", "", *S624, "sector")
E(2010, "income", "m_im", "law", "Racial Discrimination Act exemption ends", "UN Special Rapporteur James Anaya finds the measures racially discriminatory.", "Commonwealth", "", "", "", "no", "", *NTER, "reference")
E(2011, "health", "m_hearing", "data", "Hearing loss among prisoners", "94% of Aboriginal inmates tested in Darwin and Alice Springs prisons had significant hearing loss; most did not know.", "Researchers", "Being heard", "c", "94%", "no", "", "Vanderpoll and Howard, ILB", "https://www.ilc.unsw.edu.au/sites/ilc.unsw.edu.au/files/articles/ILB%207-28%20Hearing%20Loss%20-%20Vanderpoll_Howard.pdf", "academic")
E(2012, "income", "m_im", "law", "Stronger Futures", "The 2007 Act is replaced on 16 July 2012 by Stronger Futures, keeping many measures.", "Commonwealth", "", "c", "", "no", "", *NTER, "reference", date="2012-07-16")
E(2013, "schools", "m_funding", "policy", "'Effective enrolment' funding", "Funding follows attendance, not need; a Deloitte review found it flowed to mostly non-Aboriginal, urban students. Aboriginal students lost about $3,000 each a year against $340 for non-Aboriginal students.", "NT Government", "School resources", "", "-$3,000 per Aboriginal student a year", "no", "", *S624, "sector")
E(2014, "schools", "m_attend", "data", "Aboriginal attendance 68.2%", "Start of the steepest fall in four decades of data.", "NT schools", "", "", "68.2%", "no", "", *S624, "sector")
E(2015, "income", "m_cdp", "policy", "Community Development Program", "Over 50,000 financial penalties in one three-month period (start year to confirm).", "Commonwealth", "Income", "c", "50,000+ penalties in a quarter", "no", "", "NIRS", "https://nirs.org.au/news/featured/http-news-nirs-org-au-71462-2", "news", status="to source")
E(2015, "housing", "m_deal", "policy", "Homelands handed to the NT", "Commonwealth transfers homelands responsibility to the NT; leaders call it a 'backroom deal'.", "Commonwealth", "Services on homelands", "c", "", "no", "", "NIT: homelands funding", "https://nit.com.au/26-06-2026/25034/nt-aboriginal-leaders-urge-return-of-direct-homeland-funding-amid-infrastructure-concerns", "news")
E(2016, "custody", "m_youthdet", "inquiry", "Four Corners 'Australia's Shame'", "Aired 25 July 2016, showing abuse in Don Dale; a Royal Commission is called within days.", "ABC", "", "b", "", "no", "", *RC17, "reference", date="2016-07-25")
E(2017, "custody", "m_youthdet", "inquiry", "Royal Commission reports", "Tabled 17 November 2017: 142 findings and 226 recommendations, describing a 'constant roundabout' of school disengagement, court and placement breakdown.", "Commonwealth and NT", "", "", "226 recommendations", "no", "", *RC17, "reference", date="2017-11-17")
E(2017, "police", "m_force", "law", "Spit hoods banned for children", "Following the Royal Commission.", "NT Government", "", "", "", "no", "", "The Daily Aus", "https://thedailyaus.com.au/politics/nt-youth-crime-reforms-accused-of-risking-human-rights", "news")
E(2017, "land", "m_rangers", "funding", "NT Aboriginal Ranger Grants begin", "Pays for ranger equipment, facilities and training.", "NT Government", "", "", "", "yes", "", "NIT: ranger program", "https://nit.com.au/16-05-2025/17981/answers-sought-from-nt-government-over-12m-ranger-program-betrayal", "news")
E(2018, "health", "m_floor", "law", "Alcohol floor price", "$1.30 minimum unit price introduced.", "NT Government", "", "", "$1.30 per standard drink", "no", "", "NT Independent", "https://ntindependent.com.au/clp-lifts-minimum-unit-price-for-alcohol-amid-calls-to-keep-the-policy-in-place/", "news")
E(2019, "police", "m_pubdrink", "law", "Public drinking decriminalised", "Reform made in line with the Deaths in Custody Royal Commission.", "NT Government", "", "", "", "no", "", "ABC", "https://www.abc.net.au/news/2024-10-10/nt-government-to-introduce-new-public-drinking-law/104451210", "news")
E(2019, "police", "m_deaths", "death", "Kumanjayi Walker shot in Yuendumu", "The coroner later described some evidence of racism and violence in NT Police as deeply disturbing. Officer Zachary Rolfe had served five years in the Army.", "NT Police", "Life", "a", "", "no", "", "NIT", "https://nit.com.au/02-06-2025/18295/inquest-into-kumanjayi-walkers-death-delayed-as-yuendumu-mourns-another-death-in-police-custody", "news", date="2019-11-09")
E(2020, "police", "m_custody", "data", "23 Aboriginal people a day into custody", "January 2020 average.", "NT Police", "Liberty", "b", "23 a day", "no", "", *NAAJA_REC, "sector")
E(2021, "health", "m_floor", "data", "Floor price evaluation", "Menzies found a 14% fall in alcohol-related assaults and a 21% fall in alcohol-related family violence assaults after three years.", "Menzies School of Health Research", "", "", "-14% assaults; -21% DFV assaults", "no", "The CLP later cited a 38% rise in assaults.", "NT Independent", "https://ntindependent.com.au/clp-lifts-minimum-unit-price-for-alcohol-amid-calls-to-keep-the-policy-in-place/", "news")
E(2021, "custody", "m_prison", "data", "60.3% return to prison within two years", "People released in 2021-22; highest in Australia (national 43.0%).", "NT Corrections", "Years with kin", "b", "60.3%", "no", "", "Sentencing Advisory Council (ROGS)", "https://www.sentencingcouncil.vic.gov.au/sentencing-statistics/released-prisoners-returning-to-prison", "government")
E(2022, "housing", "m_overcrowd", "data", "54% of remote houses overcrowded", "National Audit Office report.", "Commonwealth and NT", "Safe shelter", "c", "54%", "no", "", "The Daily Aus", "https://www.thedailyaus.com.au/latest/federal-govt-signs-northern-territory-housing-deal", "news")
E(2022, "custody", "m_youthdet", "data", "$2,703.68 per child per day", "Cost of youth detention in 2022-23, about $987,000 a year.", "NT Government", "", "", "$2,703.68 a day", "no", "", "NT Parliament written answer", "https://parliament.nt.gov.au/__data/assets/pdf_file/0020/1464131/Answer-to-Written-Question-1.pdf", "government")
E(2023, "legal", "m_ais", "data", "Courts adjourn for lack of interpreters", "Interpreters employed fell by almost half over a decade; most of 170 registered are casual. One NAAJA client spent nearly two weeks on remand, his case adjourned three times.", "NT Government", "Being heard", "b", "about half of requests filled", "no", "", "ABC Law Report (2023)", "https://www.abc.net.au/news/2023-08-11/law-report-investigates-indigenous-court-interpreter-shortages/102696730", "news")
E(2023, "housing", "m_shelter", "event", "Kalkarindji and Daguragu flood evacuation", "About 700 people evacuated to Howard Springs for up to two months; Pigeon Hole residents still in tents three months on.", "NT Government", "Shelter on Country", "c", "about 700 people", "no", "", "NIT", "https://nit.com.au/26-03-2023/5390/first-group", "news")
E(2023, "courts", "m_age", "law", "Age of criminal responsibility raised to 12", "Under the previous Labor government (date to confirm).", "NT Government", "", "", "12 years", "no", "", "The Daily Aus", "https://www.thedailyaus.com.au/crime/nt-lowers-age-of-criminal-responsibility-to-10", "news", status="to source")

# --- current settings
E(2024, "courts", "m_age", "law", "Age lowered back to 10; Declan's Law", "Age of criminal responsibility lowered from 12 to 10; bail tightened with electronic monitoring for repeat offenders.", "NT Government", "Childhood", "b", "10 years", "no", "Getting children help sooner.", "The Daily Aus", "https://www.thedailyaus.com.au/crime/nt-lowers-age-of-criminal-responsibility-to-10", "news", date="2024-10")
E(2024, "police", "m_pubdrink", "law", "Public drinking offence returns", "Police can fine up to $925, issue a seven-day Banned Drinker Order and arrest, then check for warrants and bail breaches.", "NT Government", "Liberty", "b", "$925 fine", "no", "", "ABC", "https://www.abc.net.au/news/2024-10-10/nt-government-to-introduce-new-public-drinking-law/104451210", "news", date="2024-10")
E(2024, "custody", "m_youthdet", "policy", "Holtze becomes the only youth detention centre", "30 km from Darwin, no public transport; Alice Springs children moved there.", "NT Government", "Family", "e", "", "no", "", *S282, "sector", date="2024-11")
E(2024, "police", "m_custody", "data", "40 Aboriginal people a day into custody", "From December 2024, nearly double the 2020 average.", "NT Police", "Liberty", "b", "40 a day", "no", "", *NAAJA_REC, "sector")
E(2024, "housing", "m_deal", "funding", "$4 billion remote housing agreement", "10-year Commonwealth-NT deal for up to 2,700 homes; Commonwealth share $2.1B.", "Commonwealth and NT", "", "", "$4B", "no", "Largest remote housing investment in NT history.", "AAP", "https://aapnews.com.au/news/historic-4-billion-investment-in-remote-nt-housing", "news")
E(2024, "schools", "m_bilingual", "cut", "Bilingual funding cut, then reversed", "NT moved to cancel $2.12M of targeted bilingual funding (a quarter of one per cent of the education budget), reversed after ATESOL NT and ACTA objected.", "NT Government", "Language", "", "$2.12M", "yes", "", *S624, "sector", date="2024-10")
E(2024, "health", "m_rehab", "cut", "Darwin's only rehab and sobering-up shelter closes", "Mission Australia facility at Berrimah closed mid-2024 under the previous Labor government to make way for a women's prison; about 40 people in long-term rehab.", "NT Government", "Treatment", "b", "about 40 people", "no", "", "NT Greens campaign", "https://greens.org.au/nt/campaigns/save-rehab-services", "advocacy")
E(2024, "custody", "m_youthdet", "data", "Every audited child in youth justice known to child protection", "NT Children's Commissioner audit; 94% exposed to domestic or family violence.", "NT Children's Commissioner", "", "", "100%", "no", "", "NIT", "https://nit.com.au/25-10-2024/14474/truly-confronting-new-report-reveals-link-between-child-protection-and-youth-justice", "news")
E(2025, "health", "m_floor", "cut", "Floor price scrapped", "Despite objections from Danila Dilba, Congress, AMSANT, Larrakia Nation and the AMA.", "NT Government", "", "", "", "no", "Assaults rose 38% under the floor price (no source given).", "NT Independent", "https://ntindependent.com.au/clp-lifts-minimum-unit-price-for-alcohol-amid-calls-to-keep-the-policy-in-place/", "news", date="2025-02")
E(2025, "courts", "m_bail", "law", "Last-resort principle removed for custody", "Bail and Youth Justice amendments remove the last-resort principle for custody on arrest and remand.", "NT Government", "Liberty", "b", "", "no", "", "NT Attorney-General's Department", "https://agd.nt.gov.au/law-reform-reviews/law-reforms/strengthening-bail-in-the-nt", "government", date="2025-04")
E(2025, "police", "m_force", "law", "Spit hoods reinstated", "Youth Justice amendments: detention no longer a last resort, spit hoods back, wider use-of-force powers.", "NT Government", "Safety", "b", "", "no", "", "SBS", "https://www.sbs.com.au/news/article/mccarthy-raises-concerns-with-nt-about-return-of-spit-hoods-and-youth-incarceration/kpysg6reo", "news", date="2025-07")
E(2025, "courts", "m_bail", "data", "Aboriginal adults 2.07 times more likely to be refused bail", "Than similarly placed non-Aboriginal adults (1.64 times for police bail). Over 3,300 people refused bail January-August 2025.", "Courts and police", "Liberty", "b", "2.07x", "no", "", *S604, "sector")
E(2025, "courts", "m_remand", "data", "82% of detained children unsentenced", "Of 161 children held April-June 2025.", "NT Government", "Liberty", "b", "82%", "no", "", "NPY Women's Council", "https://www.npywc.org.au/wp-content/uploads/Position-Paper_Youth-Justice-Changes.pdf", "sector")
E(2025, "courts", "m_remand", "data", "41% of prisoners on remand", "November 2025; 52% unsentenced in Darwin Correctional Centre.", "NT Corrections", "Liberty", "b", "41%", "no", "", *S282, "sector", date="2025-11")
E(2025, "custody", "m_youthdet", "data", "95% of detained children Aboriginal", "57 of 60 on 6 August 2025.", "NT Government", "", "", "95%", "no", "", "NAAJA", "https://www.naaja.org.au/aboriginal-youth-in-detention-hits-record-high/", "sector", date="2025-08-06")
E(2025, "custody", "m_programs", "cut", "Programs cancelled inside", "In six months to March 2025, 10 of 11 drug and alcohol sessions and 34 of 46 psycho-educational programs cancelled.", "NT Corrections", "A way out", "", "10 of 11 cancelled", "no", "", *S604, "sector")
E(2025, "land", "m_rangers", "cut", "Ranger grants dropped", "$12M four-year program left out of the 2025 budget despite a CLP election promise; the budget gave corrections a record $495M.", "NT Government", "Jobs on Country", "", "-$12M", "no", "Funding had run out; the Commonwealth is the main funder.", "NIT", "https://nit.com.au/16-05-2025/17981/answers-sought-from-nt-government-over-12m-ranger-program-betrayal", "news")
E(2025, "dev", "m_tc", "law", "Territory Coordinator Act", "Passed 19 March 2025 over opposition from all four land councils, Larrakia Nation, APO NT and Nurrdalinji.", "NT Government", "Say over development", "c", "", "no", "Major projects bring jobs and growth.", "NIT", "https://nit.com.au/19-03-2025/16899/nt-coordinator-bill-passes-despite-public-opposition", "news", date="2025-03-19")
E(2025, "police", "m_deaths", "death", "Kumanjayi White dies after police restraint", "24-year-old Warlpiri man with disabilities under state care, restrained by two plain-clothes officers in an Alice Springs supermarket. The DPP declined to prosecute; inquest set for April 2027.", "NT Police", "Life", "a", "", "no", "Matter for the coroner.", "NIT", "https://nit.com.au/02-06-2025/18295/inquest-into-kumanjayi-walkers-death-delayed-as-yuendumu-mourns-another-death-in-police-custody", "news", date="2025-05-27")
E(2025, "police", "m_force", "law", "Pepper spray legal for the public", "One-year trial from 1 September 2025.", "NT Government", "Safety", "b", "", "no", "", "The Daily Aus", "https://www.thedailyaus.com.au/news/pepper-spray-is-legal-northern-territory", "news", date="2025-09-01")
E(2025, "schools", "m_truancy", "policy", "Parents referred to income management", "From October 2025 for persistent absence; 292 fines and 1,398 notices issued in 2025.", "NT Government", "Control of money", "c", "292 fines", "no", "Parental accountability.", "NIT", "https://nit.com.au/06-10-2025/20579/nt-government-to-refer-parents-of-truant-children-to-income-management", "news", date="2025-10")
E(2025, "schools", "m_attend", "data", "Schools reach Aboriginal students 54.7% of the time", "Against 84.9% for non-Aboriginal students; 40.0% in very remote schools.", "NT schools", "Education", "", "54.7%", "no", "", "NT DET 2025, table 3", "https://education.nt.gov.au/__data/assets/pdf_file/0010/1585045/e-and-a-web-2025-table-3.pdf", "government")
E(2025, "schools", "m_funding", "policy", "Effective enrolment ends", "Only under Commonwealth funding conditions.", "NT Government", "", "", "", "no", "", *S624, "sector")
E(2025, "legal", "m_naaja", "policy", "Push to redirect NAAJA funding", "The Chief Minister proposed moving some NAAJA funding to Legal Aid NT. NAAJA says the NT contributes nothing to its legal services.", "NT Government", "Representation", "", "", "no", "", "NIT", "https://nit.com.au/20-11-2025/21376/naaja-rejects-nt-government-push-to-redirect-funding-warns-comments-based-on-inaccurate-information", "news", date="2025-11")
E(2025, "housing", "m_rent", "court", "Badari: High Court strikes down Remote Rent Framework", "For denying tenants procedural fairness; the NT then amended the Housing Act so the Minister can set rent without consulting tenants.", "High Court / NT Government", "Say over rent", "c", "", "yes", "", *S604, "sector", date="2025-12")
E(2025, "police", "m_deaths", "death", "Woman dies in Tennant Creek watch house", "44-year-old Aboriginal woman; a week later the cause was undetermined.", "NT Police", "Life", "a", "", "no", "", "SBS NITV", "https://sbs.com.au/nitv/article/cause-of-death-still-undetermined-a-week-after-death-in-custody-of-44-year-old-aboriginal-woman/df6gm54ig", "news", date="2025-12")
E(2025, "income", "m_cdp", "policy", "RJED replaces CDP", "Up to 3,000 jobs, $707M, plus the Remote Australia Employment Service from 1 November 2025.", "Commonwealth", "", "", "3,000 jobs", "no", "", "NIT", "https://nit.com.au/30-06-2025/18820/Remote-Australia-Employment-Service-federal-government-grants-open-jobs", "news", date="2025-11-01")
E(2026, "custody", "m_transfer", "data", "60 children flown from Alice Springs to Darwin", "In 10 months, all Aboriginal, 10 girls, 16 with or being assessed for disability. Held in an adult transfer facility, handcuffed on commercial flights; families sometimes not told.", "NT Government", "Country, family", "e", "60 children", "no", "No legislative requirement to notify families.", "ABC: Children's Commissioner report", "https://www.abc.net.au/news/2026-01-29/nt-childrens-commissioner-youth-detention-transfer-report/106280082", "news", date="2026-01")
E(2026, "courts", "m_remand", "data", "Average youth remand 56 days", "One child aged 10-14 spent 238 days on remand before charges were dropped.", "NT courts and corrections", "Liberty without guilt", "b", "56 days", "no", "", *ABC_NAAJA, "news", date="2026-02-03")
E(2026, "courts", "m_doli", "data", "Remand without conviction", "Children 10-13 are presumed incapable of criminal intent, yet youth remand rose from 92 to 133 in a year while sentenced detention fell from 33 to 28.", "NT courts", "Liberty", "b", "92 to 133", "no", "", "NTCOSS submission", "https://ntcoss.org.au/wp-content/uploads/2025/12/Website-Version-NTCOSS-Submission-Youth-Justice-and-Incarceration-System.pdf", "sector")
E(2026, "childprot", "m_acpp", "law", "Every Child Matters Act", "Passed July 2026: the Child Placement Principle applies only 'as far as practicable'; protection orders capped at two years in favour of permanency; family's right to identify placement removed.", "NT Government", "Placement with kin", "e", "", "no", "The principle is restructured, not removed.", "NIT", "https://nit.com.au/22-07-2026/25507/this-is-neglect-controversial-nt-child-protection-laws-passes-despite-overwhelming-opposition", "news", date="2026-07")
E(2026, "childprot", "m_kin", "data", "Only 16.7% placed with kin", "About 90% of children in care are Aboriginal; lowest kin placement rate in Australia.", "NT Government", "Family", "e", "16.7%", "no", "", "ABC", "https://www.abc.net.au/news/2026-05-14/nt-government-new-child-protection-legislation-laws-explained/106674132", "news")
E(2026, "childprot", "m_oohc", "funding", "93% of out-of-home care money to providers", "$133.2M of $143.4M paid to non-government providers rather than family carers.", "NT Government", "", "", "$133.2M of $143.4M", "no", "", "CREATE Foundation", "https://www.create.org.au/get-informed/blog/create-foundations-northern-territory-budget-summary/", "sector")
E(2026, "custody", "m_prison", "data", "4,515 per 100,000 Aboriginal adults imprisoned", "June quarter 2026; national Aboriginal rate 2,719.", "NT Corrections", "Years with kin", "b", "4,515 per 100,000", "no", "", "ABS Corrective Services", "https://www.abs.gov.au/statistics/people/crime-and-justice/corrective-services-australia/latest-release", "government")
E(2026, "custody", "m_prison", "funding", "$525M corrections vs $4.9M diversion", "2026/27 budget, about 100 to 1; two work camps $238M.", "NT Government", "", "", "$525M vs $4.9M", "no", "Community safety; victims of crime fell 10.2%.", *BUDGET, "news")
E(2026, "income", "m_im", "law", "Income management extended to 2033", "Self-repeal dates removed despite Labor's 2022 promise to abolish compulsory income management; condemned by the Central Land Council.", "Commonwealth", "Control of money", "c", "", "no", "Protects money for food, rent and bills.", "NIT", "https://nit.com.au/24-09-2026/26644/causes-so-much-harm-experts-land-council-slam-federal-move-to-extend-compulsory-income-management", "news", date="2026-06")
E(2026, "housing", "m_shelter", "cut", "YiSSA short-stay shelter closes", "Darwin's largest short-stay shelter, run by Yilli Rreung Housing Aboriginal Corporation, held 383 residents including 145 children. The NT rejected a Commonwealth offer to share the purchase; Minister McCarthy said it objected because it was Aboriginal-run. Residents moved to Batchelor, about 100 km away.", "NT Government", "Shelter near family and services", "c", "383 residents, 145 children", "no", "Could not agree a fair price with the owner.", "NIT", "https://nit.com.au/09-10-2026/26882/nt-government-rejected-deal-to-keep-yissa-open-because-it-was-aboriginal-run", "news", date="2026-10-11")
E(2026, "housing", "m_shelter", "event", "Flood evacuations to Darwin", "About 1,000 people in evacuation centres in March; police raised their 'community safety posture' around centres. Evacuees' emergency payments were quarantined until they returned.", "NT Government", "Shelter on Country", "c", "about 1,000 people", "no", "", "NIT", "https://nit.com.au/09-03-2026/23054/crocs-and-rising-rivers-nt-towns-face-flood-disaster", "news", date="2026-03")
E(2026, "housing", "m_overcrowd", "resistance", "Papunya tenants sue over heat", "Australia's first case over housing unsafe in extreme heat.", "Papunya tenants", "", "", "", "yes", "", "NIT", "https://nit.com.au/22-04-2026/23843/remote-community-tenants-sue-nt-government-over-unsafe-housing-in-extreme-heat", "news")
E(2026, "police", "m_force", "policy", "Armed Police Public Safety Officers", "34 public housing and 22 transit officers armed and placed under police command; first squad deployed on Operation Ventura.", "NT Government", "Safety", "b", "56 officers", "no", "", "SBS NITV", "https://www.sbs.com.au/nitv/article/recipe-for-disaster-advocates-condemn-plan-to-bring-in-guns-for-bus-and-public-housing-officers-in-the-nt/e1onre3rc", "news")
E(2026, "police", "m_custody", "policy", "Operation Ventura (Palmerston)", "Over eight weeks: 118 arrests, 375 Banned Drinker Orders, 2,335 move-ons by week six, 76 protective custody apprehensions; targeted illegal camping and public housing.", "NT Police", "Liberty", "b", "118 arrests", "no", "Crime trends improve.", "NT Police", "https://pfes.nt.gov.au/newsroom/2026/operation-ventura-concludes-crime-trends-improve-across-territory", "government")
E(2026, "health", "m_rhd", "data", "1 in 17 First Nations Territorians live with RHD or ARF history", "At 31 December 2024; 4,597 on the register; highest in Barkly.", "Health system", "Health", "c", "5.9%", "no", "", "AIHW", "https://www.aihw.gov.au/reports/indigenous-australians/arf-rhd/contents/management-of-arf-and-rhd", "government")
E(2026, "health", "m_rehab", "cut", "Parole rehab (COMMIT) cut", "$2.1M for rehab beds and counselling for people on parole; the Parole Board chair said it 'will once again add to the very high rates of incarceration of Aboriginal people' (date to confirm).", "NT Government", "Exits from custody", "b", "-$2.1M", "no", "", "inkl / ABC", "https://www.inkl.com/news/parole-board-boss-says-nt-government-cuts-will-worsen-aboriginal-incarceration", "news", status="to source")
E(2026, "courts", "m_genocide", "court", "Genocide prosecution needs the Attorney-General", "A court held Uncle Robbie Thorpe's attempted genocide prosecution of King Charles would need the Attorney-General's consent.", "Court", "Access to a court", "", "", "yes", "", "Te Ao News / NITV", "https://www.teaonews.co.nz/2026/06/05/aboriginal-elder-has-made-his-arguments-for-prosecuting-king-charles-for-genocide-in-court/", "news")
E(2026, "courts", "m_remand", "resistance", "Project Mangma stalled", "Eric Fejo's five-week cultural diversion program, built over 14 months with Larrakia ceremony-ground authority and support from police, defence and the Chief Judge.", "Eric Fejo and community", "", "", "", "yes", "", *S209, "testimony", status="testimony")
E(2026, "custody", "m_prison", "resistance", "Anindilyakwa justice on Groote Eylandt", "An Anindilyakwa-led justice program linked to an 88% fall in crime, underpinned by housing.", "Anindilyakwa people", "", "", "-88% crime", "yes", "", *S282, "sector")
E(2026, "custody", "m_youthdet", "resistance", "Justice not Jails Drivers Network", "Volunteers drive families to visit children at Holtze.", "Justice not Jails", "", "", "", "yes", "", *S282, "sector")
E(2026, "custody", "m_prison", "testimony", "Eric Fejo: 85% never see daylight again", "A former prison officer of ten years says 18-year-olds once had an 8-12% chance of returning or dying by suicide; today he puts it at 85%. Shown beside the official 60.3% (different measures).", "", "", "", "85% (testimony)", "yes", "", *S209, "testimony", status="testimony")

write("events.csv", EV_COLS, EV)

# ---------------------------------------------------------------- links between sections
LK_COLS = ["id", "from", "to", "label", "start_year", "end_year", "evidence", "summary", "figure", "source_title", "source_url"]
L = [
 ("l_remove_missions", "childprot", "missions", "Removed children placed in compounds and missions", 1913, 1980, "nt",
  "Children removed under the Chief Protector and later the Welfare Branch were held in Kahlin, The Bungalow, Retta Dixon and missions.", "", *BTH),
 ("l_cp_police", "childprot", "police", "Care to custody", 2017, "", "nt",
  "Every audited child in youth justice had significant contact with child protection; nationally, 94% of those first supervised at 10 had child protection contact.", "100% of audited children", "NIT: Children's Commissioner audit", "https://nit.com.au/25-10-2024/14474/truly-confronting-new-report-reveals-link-between-child-protection-and-youth-justice"),
 ("l_police_courts", "police", "courts", "Arrest to bail court", 2024, "", "nt",
  "About 40 Aboriginal people a day taken into custody; Aboriginal adults 2.07 times more likely to be refused court bail than similarly placed others.", "2.07x bail refusal", *S604),
 ("l_courts_custody", "courts", "custody", "Remand to detention", 2024, "", "nt",
  "82% of detained children unsentenced; average youth remand 56 days; one child held 238 days before charges were dropped.", "82% unsentenced", *ABC_NAAJA),
 ("l_custody_cp", "custody", "childprot", "Prison to child removal", 2007, "", "gap",
  "A parent imprisoned or remanded leaves no one to care for children, who are removed. Widely reported by communities; no NT figure found yet.", "", "", ""),
 ("l_custody_housing", "custody", "housing", "Release into homelessness", 2007, "", "national",
  "More than half of ex-prisoners nationally are released into homelessness or precarious housing; public housing waits average five years.", "over half", "AHURI", "https://www.ahuri.edu.au/analysis/news/housing-ex-prisoners-reduces-interactions-justice-system-and-saves-money-report"),
 ("l_housing_cp", "housing", "childprot", "Poverty read as neglect", 2017, "", "nt",
  "Kin blocked from caring because their name is not on the lease, the house is overcrowded, or every adult lacks an Ochre card.", "", *S604),
 ("l_housing_health", "housing", "health", "Crowding to heart disease", 1997, "", "nt",
  "Only 57% of NT First Nations households live in acceptable housing; the poorest housing matches the highest ARF/RHD rates.", "57% acceptable housing", "AIHW", "https://www.aihw.gov.au/reports/indigenous-australians/arf-rhd/contents/introduction/socioeconomic-and-environmental-factors"),
 ("l_health_schools", "health", "schools", "Hearing loss to school", 2011, "", "nt",
  "Childhood ear disease leads to hearing loss, misread at school as non-compliance; 94% of Aboriginal prisoners tested had hearing loss.", "94%", "Vanderpoll and Howard", "https://www.ilc.unsw.edu.au/sites/ilc.unsw.edu.au/files/articles/ILB%207-28%20Hearing%20Loss%20-%20Vanderpoll_Howard.pdf"),
 ("l_schools_income", "schools", "income", "Truancy to income management", 2025, "", "nt",
  "Since October 2025 parents of persistently absent children are referred to income management; 385 referred in term 3, 2026, 208 accepted.", "385 referred", "National Tribune (NT Govt)", "https://www.nationaltribune.com.au/parental-accountability-for-school-attendance-continues-under-the-clp-government/"),
 ("l_schools_police", "schools", "police", "Arrest at school", 2024, "", "nt",
  "A 13-year-old with disabilities was arrested at school for allegedly shoplifting snacks.", "", "NAAJA", "https://www.naaja.org.au/aboriginal-youth-in-detention-hits-record-high/"),
 ("l_health_police", "health", "police", "Alcohol to arrest", 2024, "", "nt",
  "Cheaper alcohol after the floor price was scrapped, no sobering-up shelter in Darwin, and a $925 public drinking fine route people to watch houses.", "$925 fine", "NT Independent", "https://ntindependent.com.au/clp-lifts-minimum-unit-price-for-alcohol-amid-calls-to-keep-the-policy-in-place/"),
 ("l_legal_courts", "legal", "courts", "No interpreter, longer remand", 2023, "", "nt",
  "Darwin Local Court adjourns almost daily for lack of an interpreter; one client spent nearly two weeks on remand, his case adjourned three times.", "", "ABC Law Report", "https://www.abc.net.au/news/2023-08-11/law-report-investigates-indigenous-court-interpreter-shortages/102696730"),
 ("l_custody_transfer", "custody", "land", "Transfer off Country", 2024, "", "nt",
  "Alice Springs children flown to Holtze, families sometimes not told, no assured way home after release.", "60 children in 10 months", "ABC", "https://www.abc.net.au/news/2026-01-29/nt-childrens-commissioner-youth-detention-transfer-report/106280082"),
 ("l_dev_land", "dev", "land", "Fast-tracking over Country", 2025, "", "nt",
  "The Territory Coordinator can override NT laws including the Heritage Act; it cannot override the Land Rights Act.", "", "NIT", "https://nit.com.au/12-03-2025/16768/nt-coordinator-bill-land-councils-northern-territory"),
 ("l_housing_police", "housing", "police", "Evacuation and shelter to policing", 2023, "", "nt",
  "Evacuees held in crowded centres under heavier policing; YiSSA residents moved 100 km away. No data yet links this to later arrests.", "", "ABC", "https://www.abc.net.au/news/2026-03-20/cyclone-narelle-nt-numbulwar-evacuated-communities-prepare/106474694"),
 ("l_police_land", "police", "land", "Punitive expeditions clear Country", 1870, 1933, "nt",
  "Police and settler reprisals cleared land for pastoral runs; around half of all recorded massacres nationally were by police or government forces.", "", "Colonial Frontier Massacres map", "https://c21ch.newcastle.edu.au/colonialmassacres/detail.php?r=704"),
]
write("links.csv", LK_COLS, [dict(zip(LK_COLS, l)) for l in L])

# ---------------------------------------------------------------- examples (shown when zoomed into a link or section)
EX_COLS = ["id", "attach_to", "attach_id", "year", "title", "text", "kind", "consent", "source_title", "source_url"]
X = [
 ("x1", "link", "l_schools_police", 2024, "Arrested at school for snacks", "A 13-year-old with disabilities was arrested at school for allegedly shoplifting snacks.", "public record", "Reported publicly by NAAJA", "NAAJA", "https://www.naaja.org.au/aboriginal-youth-in-detention-hits-record-high/"),
 ("x2", "link", "l_courts_custody", 2026, "238 days, then charges dropped", "A child aged 10 to 14 spent 238 days on remand before the charges were dropped.", "public record", "De-identified in source", *ABC_NAAJA),
 ("x3", "link", "l_legal_courts", 2023, "Adjourned three times", "A NAAJA client spent nearly two weeks on remand because no interpreter was available; his case was adjourned three times.", "public record", "De-identified in source", "ABC Law Report", "https://www.abc.net.au/news/2023-08-11/law-report-investigates-indigenous-court-interpreter-shortages/102696730"),
 ("x4", "link", "l_custody_transfer", 2026, "Handcuffed on a commercial flight", "Children held in an adult transfer facility were handcuffed and flown to Darwin. One young person moved from Alice Springs was seriously assaulted by multiple detainees and has ongoing medical complications.", "public record", "De-identified in source", *ABC_NAAJA),
 ("x5", "section", "police", 2018, "11-year-old sprayed in a police van", "The NT Ombudsman found police sprayed an 11-year-old boy, hooded and handcuffed in the closed cage of a van, after he spat at officers; he was 'in extreme distress' (year to confirm).", "public record", "Ombudsman finding", "inkl / ABC", "https://www.inkl.com/news/after-cuffed-11yo-capsicum-sprayed-nt-police-deny-problem-with-managing-youth"),
 ("x6", "section", "police", 2025, "Kumanjayi White", "A Warlpiri man, 24, with disabilities and under state guardianship, died after police restraint in an Alice Springs supermarket. His family are calling for justice and transparency.", "public record", "Named publicly by family; use the family's framing", "NIT", "https://nit.com.au/23-10-2025/20872/family-of-kumanjayi-white-demand-justice-and-transparency-ahead-of-inquest"),
 ("x7", "link", "l_housing_cp", 2026, "Kin turned away by housing rules", "Composite drawn from NAAJA's submission: a grandmother asks to care for her grandchildren but is refused because her name is not on the lease and the house has too few bedrooms.", "composite", "Composite; not one person", *S604),
 ("x8", "section", "housing", 2025, "Septic maintenance and a child's death", "Coronial findings said two-year-old Kumanjayi Fly's death in Mount Liebig could have been prevented by septic maintenance.", "public record", "Coronial finding", *S604),
 ("x9", "link", "l_cp_police", 2026, "From care to the watch house", "Composite: a 12-year-old in residential care runs from placement, is picked up by police at night, held in a watch house and remanded because no bail address is approved.", "composite", "Composite; not one person", "Royal Commission Vol 3B", "https://rmo.nt.gov.au/_media/documents/rcpdcnt/Royal-Commission-NT-Final-Report-Volume-3B.pdf"),
 ("x10", "section", "police", 1928, "Coniston", "Families and Warlpiri, Anmatyerr and Kaytetye people name more killing sites than the Board of Enquiry recognised.", "public record", "Community history", "Central Land Council", "https://www.clc.org.au/wp-content/uploads/Coniston-Brochure-2018.pdf"),
 ("x11", "link", "l_remove_missions", 1935, "Kept 'like birds in a cage'", "Testimony to Bringing Them Home describes girls in the Kahlin dormitories.", "public record", "Published testimony", *BTH),
 ("x12", "link", "l_schools_income", 2026, "From absence to a SmartCard", "Composite: a mother whose son misses school after a family funeral is referred to income management; half her payment moves to the card.", "composite", "Composite; not one person", "NIT", "https://nit.com.au/06-10-2025/20579/nt-government-to-refer-parents-of-truant-children-to-income-management"),
]
write("examples.csv", EX_COLS, [dict(zip(EX_COLS, x)) for x in X])

# ---------------------------------------------------------------- money
MO_COLS = ["id", "year", "end_year", "section", "payer", "payee", "amount_aud", "kind", "label", "direction", "source_title", "source_url", "status"]
MO = [
 ("$1", 2026, 2026, "custody", "NT Government", "NT Corrections", 525000000, "per year", "Corrections, incl. $250M infrastructure", "spend", *BUDGET, "verified"),
 ("$2", 2026, 2026, "courts", "NT Government", "Diversion programs", 4900000, "per year", "Diversion programs", "spend", *BUDGET, "verified"),
 ("$3", 2026, 2026, "custody", "NT Government", "Prisoner work camps", 238000000, "total", "Two work camps (Darwin 192 beds, Katherine 198)", "spend", "AAP via Illawarra Mercury", "https://www.illawarramercury.com.au/story/9239297/northern-territory-budgets-hundreds-more-prison-beds/", "verified"),
 ("$4", 2025, 2025, "police", "NT Government", "Police, courts, corrections", 1540000000, "per year", "Law and order, a record", "spend", "AAP via The Leader", "https://www.theleader.com.au/story/9239297/northern-territory-budgets-hundreds-more-prison-beds/", "verified"),
 ("$5", 2025, 2031, "police", "Commonwealth (NTRAI)", "NT Police", 205800000, "6 years", "NTRAI remote policing", "spend", "Minister McCarthy", "https://ministers.pmc.gov.au/mccarthy/strengthening-critical-remote-services-northern-territory", "verified"),
 ("$6", 2025, 2031, "legal", "Commonwealth (NTRAI)", "Aboriginal Interpreter Service", 55000000, "6 years", "NTRAI interpreters", "spend", "Minister McCarthy", "https://ministers.pmc.gov.au/mccarthy/strengthening-critical-remote-services-northern-territory", "verified"),
 ("$7", 2025, 2031, "health", "Commonwealth (NTRAI)", "Community-led alcohol harm reduction", 76000000, "6 years", "NTRAI alcohol harm reduction", "spend", "Minister McCarthy", "https://ministers.pmc.gov.au/mccarthy/strengthening-critical-remote-services-northern-territory", "verified"),
 ("$8", 2025, 2031, "childprot", "Commonwealth (NTRAI)", "Child and Family Centres", 135900000, "6 years", "NTRAI child and family centres, women's safe spaces", "spend", "Minister McCarthy", "https://ministers.pmc.gov.au/mccarthy/strengthening-critical-remote-services-northern-territory", "verified"),
 ("$9", 2025, 2031, "schools", "Commonwealth (NTRAI)", "Early learning", 89200000, "6 years", "NTRAI early learning, school readiness", "spend", "Minister McCarthy", "https://ministers.pmc.gov.au/mccarthy/strengthening-critical-remote-services-northern-territory", "verified"),
 ("$10", 2025, 2031, "health", "Commonwealth (NTRAI)", "Children's oral and hearing health", 50500000, "6 years", "NTRAI hearing and oral health", "spend", "Minister McCarthy", "https://ministers.pmc.gov.au/mccarthy/strengthening-critical-remote-services-northern-territory", "verified"),
 ("$11", 2026, 2026, "childprot", "NT Government", "Out-of-home care", 143400000, "per year", "Out-of-home care total", "spend", "CREATE Foundation", "https://www.create.org.au/get-informed/blog/create-foundations-northern-territory-budget-summary/", "verified"),
 ("$12", 2026, 2026, "childprot", "NT Government", "Non-government care providers", 133200000, "per year", "Paid to providers (93%)", "spend", "CREATE Foundation", "https://www.create.org.au/get-informed/blog/create-foundations-northern-territory-budget-summary/", "verified"),
 ("$13", 2026, 2026, "childprot", "NT Government", "Kinship carers", 3500000, "per year", "Kinship carers", "spend", "Jenny's research", "", "to source"),
 ("$14", 2024, 2034, "housing", "Commonwealth and NT", "Remote housing", 4000000000, "10 years", "Remote housing agreement ($2.1B Commonwealth)", "spend", "AAP", "https://aapnews.com.au/news/historic-4-billion-investment-in-remote-nt-housing", "verified"),
 ("$15", 2015, 2018, "income", "Commonwealth", "Indue Ltd", 11889000, "contract", "Income Management Card Services (limited tender)", "spend", "AusTender CN3068992", "https://tenders.gov.au/Cn/Show/1FBD10FE-D17E-B1EE-45B1-389C42FA10B7", "verified"),
 ("$16", 2023, 2025, "income", "Commonwealth", "Indue Ltd", 20950000, "contract", "Card and Banking Services ('extreme urgency')", "spend", "AusTender CN3945982", "https://tenders.gov.au/Cn/Show/4ad3e78c-e7cb-494b-ab29-2eb586fbd30d", "verified"),
 ("$17", 2025, 2025, "land", "NT Government", "Aboriginal ranger groups", 12000000, "4 years", "Ranger grants dropped", "cut", "NIT", "https://nit.com.au/16-05-2025/17981/answers-sought-from-nt-government-over-12m-ranger-program-betrayal", "verified"),
 ("$18", 2026, 2026, "health", "NT Government", "Parole rehab (COMMIT)", 2100000, "grant", "Parole rehab and counselling cut", "cut", "inkl / ABC", "https://www.inkl.com/news/parole-board-boss-says-nt-government-cuts-will-worsen-aboriginal-incarceration", "to source"),
 ("$19", 2024, 2024, "schools", "NT Government", "Bilingual schools", 2120000, "per year", "Bilingual funding cut (reversed)", "cut", *S624, "verified"),
 ("$20", 2022, 2022, "custody", "NT Government", "Youth detention", 2703.68, "per child per day", "Youth detention unit cost", "spend", "NT Parliament", "https://parliament.nt.gov.au/__data/assets/pdf_file/0020/1464131/Answer-to-Written-Question-1.pdf", "verified"),
 ("$21", 2022, 2022, "legal", "NT Government", "Aboriginal Interpreter Service", 7634000, "per year", "Interpreter base budget 2022-23", "spend", "NT Parliament", "https://parliament.nt.gov.au/__data/assets/pdf_file/0009/1145277/Answer-to-Written-Question-362.pdf", "verified"),
 ("$22", 2025, 2025, "custody", "NT Government", "NT Corrections", 495000000, "per year", "Corrections, 2025 budget (record)", "spend", "SBS NITV", "https://www.sbs.com.au/nitv/article/nt-racking-up-debt-as-prison-costs-skyrocket-and-grant-funding-for-aboriginal-rangers-cut/t8wy9st8o", "verified"),
]
write("money.csv", MO_COLS, [dict(zip(MO_COLS, m)) for m in MO])
print("events:", len(EV), "links:", len(L), "examples:", len(X), "money:", len(MO))
