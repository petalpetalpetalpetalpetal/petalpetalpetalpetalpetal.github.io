# Taken, Year by Year

A one-page power map of the Commonwealth and Northern Territory institutions that act on Aboriginal children and families, the money behind them, the companies they pay, and the Aboriginal-controlled organisations that work, from 1824 to today.

## How the page works
- **Top row:** governments (British Crown, South Australia, Commonwealth, NT), with who held office in the chosen year.
- **Departments:** zoomed out, each box shows its funding for the year; zoomed in, every recorded change up to that year.
- **Companies, contractors and charities:** a middle band.
- **Country:** Aboriginal-controlled organisations and nations.
- **Money button:** blue ledger view of payments, cuts and results.
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
| `links.csv` | an arrow between departments | `from`, `to`, `evidence` (nt / national / gap) |
| `examples.csv` | a case on an arrow | `attach_id`, `kind` (public record / composite), `consent` |
| `mechanisms.csv` | a named mechanism | grouping used in some details |

Status values: `verified` (linked source), `to source`, `testimony`, `reference`.

`build_data.py` and `build_v2.py` produced the first fill. Edit the CSV files directly from now on.
