# Taken, Year by Year

A one-page power map of the Commonwealth and Northern Territory institutions that act on Aboriginal children and families, the money behind them, the companies they pay, and the Aboriginal-controlled organisations that work, from 1824 to today.

## How the page works
- **Top row:** governments (British Crown, South Australia, Commonwealth, NT), with who held office in the chosen year.
- **Departments:** zoomed out, each box shows its funding for the year; zoomed in, every recorded change up to that year.
- **Companies, contractors and charities:** a middle band.
- **Country:** Aboriginal-controlled organisations and nations.
- **Funded button:** blue view of payments, cuts and results. Click any box or line to follow only that money.
- **Divested button:** red view of money cut, withheld or diverted (flows with kind cut, diverted or withheld).
- **Deaths and harm** (`harm.csv`) appear in each box’s list of changes with a content note, and as a red count on the box.
- **Search:** words plus one year, a range, before or after.
- **Sidebar (desktop):** Details, Saved (pins kept in the viewer's browser) and Who held power. On phones, tap for a pop-up; the Panel button opens the sidebar.

## Edit the content
All content lives in `data/*.csv`. Edit in Excel, Numbers or Google Sheets and save as CSV (UTF-8).

| File | One row is | Key columns |
|---|---|---|
| `config.csv` | a site setting | `contact_email`, `default_year`, slider range |
| `authorities.csv` | a government for a period | `id` (crown, sa, cwlth, ntg), `start_year`, `end_year` |
| `eras.csv` | a period on the time bar | `label`, `summary` |
| `actors.csv` | a box on the map | `band` (state / private / aboriginal), `parent` (cwlth or ntg for departments), `col` (left-to-right), `era_labels` (`1911-1952:Chief Protector|…`) |
| `events.csv` | a dated change | `year`, `section` (actor id), `type`, `figure`, `aboriginal_led`, `state_account`, `source_title`, `source_url`, `status` |
| `flows.csv` | a payment or cut | `from`, `to` (actor or government id), `year`, `end_year`, `amount_aud`, `per` (year, 6 years, total, contract…), `kind` (budget, grant, contract, royalty, cut…) |
| `outcomes.csv` | a recorded result | `actor`, `measure`, `value`, `cost`, `caveat`, `control` |
| `officeholders.csv` | a person in an office | `person`, `role`, `actor`, `start`, `end`, `party`, `source_url` |
| `harm.csv` | a death, injury, rate or odds statistic (Deaths view) | `actor`, `year`, `end_year`, `kind`, `measure`, `value`, `count`, `scope` (NT / national) |
| `links.csv` | an arrow between departments | `from`, `to`, `evidence` (nt / national / gap) |
| `examples.csv` | a case on an arrow | `attach_id`, `kind` (public record / composite), `consent` |
| `mechanisms.csv` | a named mechanism | grouping used in some details |

Status values: `verified` (linked source), `to source`, `testimony`, `reference`.

`build_data.py`, `build_v2.py` and `build_v3.py` produced the first fill. Edit the CSV files directly from now on.
