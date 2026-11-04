# Taken, Year by Year

A one-page, zoomable evidence map of how Commonwealth and Northern Territory institutions act on Aboriginal children and families, from 1824 to today.

## Publish on GitHub Pages (free)
1. Create a public repository and upload `index.html`, `README.md` and the `data` folder.
2. In the repository, open **Settings → Pages**, choose **Deploy from a branch**, branch `main`, folder `/ (root)`.
3. The site appears at `https://<your-username>.github.io/<repository-name>/` within a minute or two.

## Edit the content
All content lives in `data/*.csv`. Edit in Excel, Numbers or Google Sheets and save as CSV (UTF-8). No code changes are needed.

| File | One row is | Key columns |
|---|---|---|
| `config.csv` | a site setting | `contact_email` (where corrections go), `default_year`, slider range |
| `authorities.csv` | a governing authority for a period | `id` (crown, sa, cwlth, ntg), `start_year`, `end_year`, `label` |
| `eras.csv` | a period shown on the time bar | `start_year`, `end_year`, `label`, `summary` |
| `sections.csv` | a tier-1 box (an institution) | `parent` (cwlth or ntg), `col` (left-to-right position), `era_labels` (`1911-1952:Chief Protector|1953-1977:Welfare Branch`) |
| `mechanisms.csv` | a tier-2 card inside a box | `section`, `start_year`, `end_year`, `limb` (a–e), `summary`, `what_it_takes` |
| `events.csv` | a dated change, figure or response | `year`, `section`, `mechanism`, `type`, `figure`, `aboriginal_led` (yes/no), `state_account`, `source_title`, `source_url`, `status` (verified / to source / testimony) |
| `links.csv` | an arrow between two boxes | `from`, `to`, `start_year`, `end_year`, `evidence` (nt / national / gap) |
| `examples.csv` | a case shown when zoomed into an arrow or box | `attach_to` (link or section), `attach_id`, `kind` (public record / composite), `consent` |
| `money.csv` | a payment, budget line or cut | `section`, `year`, `end_year`, `amount_aud`, `kind`, `direction` (spend / cut), `status` |

Rules the content follows: the institution is the subject of each sentence; government positions go in `state_account`; testimony is marked `testimony`, not ranked below official data; anything without a source stays `to source` until one is found.

`build_data.py` was used for the first fill only. Edit the CSV files directly from now on.
