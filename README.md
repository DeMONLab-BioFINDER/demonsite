# DeMON Lab website

The DeMON Lab website, built with [Quarto](https://quarto.org). Netlify publishes the
committed `_site` folder as it is, so after changing a page, rebuild the site and commit the
changed source files together with `_site`.

## Building the site

Use Quarto 1.9.37 with the R environment that has the packages the pages need
(`rentrez`, `xml2`, `tidyverse`, `reactable`, `tm`, `topicmodels`, `tidytext`,
`ggwordcloud`, `visNetwork`, `htmltools`):

```bash
rm -rf .quarto          # clear cached R results first (stop any running preview before this)
quarto render           # full build into _site
quarto preview          # local preview while editing
```

## Publishing

There is no build step on the server: Netlify watches `master` on GitHub and publishes the
committed `_site` folder within a minute or two of each push.

1. Edit the `.qmd` files (and `styles.css`, `index.css` or images).
2. Do a full build as above and look at the changed pages. No page should show R warnings.
3. Commit the source files **and the whole `_site` folder** together.
4. Push to `master`.

Before committing, leave out local files: `.DS_Store`, images that no page uses, and personal
helper files. If a page looks wrong after publishing, revert the commit and push again; Netlify
then publishes the previous version.

The weekly workflow in `.github/workflows/update-papers.yml` rebuilds only the Publications page
every Monday and pushes to `master` when the list of papers changes. For it to push, the
repository's Actions settings must allow workflows "Read and write permissions".

## Research page

The Research page (`projects.qmd`) has one chapter per research theme, with the theme's text, its
highlighted papers and figures that change on their own. The tiles at the top, the chapters and the
figure displays are built from the `topics` list in the page's front matter. To add, remove,
reorder or edit a theme, paper or figure, change only that list; no HTML or CSS is needed.

| Field | What it is |
|---|---|
| `id` | Short name used in the link from the tile, e.g. `pet` (letters and dashes) |
| `color` | Soft colour of the theme, from Paul Tol's colour-blind-safe "light" scheme (#77AADD, #99DDFF, #44BB99, #BBCC33, #AAAA00, #EEDD88, #EE8866, #FFAABB). Tiles use dark text on it; buttons and dots use a darker shade made from it automatically |
| `name`, `subtitle` | The two lines on the tile and the chapter heading |
| `icon` | Icon from `images/icons/`, shown on the tile and chapter heading |
| `text` | One or more paragraphs (simple HTML such as `<em>` is allowed) |
| `papers` | The theme's highlighted papers; the first is open when the page loads |
| `lead`, `photo` | Lead author and round photo from `members/images/round/` |
| `journal`, `date`, `title`, `url` | The paper's details and link |
| `summary` | A few sentences in plain language |
| `credit` | Credit line under the figures |
| `figures` | The paper's images: `src`, `label` and `alt`, shown one after another every 5 seconds |

The `software` list in the same front matter builds the Software cards after the themes: each tool has a
`name`, `text` and `links` (`label`, `url`), and optionally a `logo` (a small square image in
`images/software/`, shown next to the name).

Notes:

- Icons come from [Bioicons](https://bioicons.com). If an icon's licence needs credit, add it to
  `icon_credit` in the front matter.
- Figures go in `images/news/` as JPEG at 1200 x 900 pixels (4:3). Only reuse figures whose licence
  allows it, and credit the paper in `credit`.
- The figures can be paused, and they do not change by themselves for people who prefer reduced motion.
- Chapters are `<article>` elements, not `<section>`. The Quarto theme has a rule
  `section:target::before` that adds an invisible spacer to the `<section>` a link jumps to, and in a
  two-column grid that spacer takes a cell and splits the columns.

## Home page: Latest from the Lab

The "Latest from the Lab" section on the Home page (`index.qmd`) is not edited by hand. Each full
build fills it from two lists:

- **Latest publication:** the first entry in `papers` in `research-publications.qmd`, so keep that
  list newest first.
- **News:** the entry in `news.qmd` marked `home: true`, or the newest entry if none is marked.

The Home page changes only after a full build (`quarto render`). `quarto preview` rebuilds only the
page you edited, so it won't show the change on Home. The live site changes once the rebuilt
`_site` is published.

## Publications page (All publications)

The top menu item "Research Publications" opens a small menu with two entries: "Highlights"
(`research-publications.qmd`) and "All publications" (`papers.qmd`). The full list is built from
PubMed and Jake's ORCID profile, so a new paper appears once it is in one of them (the weekly
workflow above refreshes it). The four word clouds are found automatically from the abstracts, and
each is given the colour of the Research page theme (PET, fMRI, Omics, AI) whose key words it
shares most, so the same colour means the same thing on both pages.

## Research Publications page

The Research Publications page (`research-publications.qmd`) shows the lab's highlighted papers
as cards. One card is built per entry in the `papers` list in the page's front matter, in the
order listed (newest first). To add, remove or edit a paper, change only that list.

| Field | What it is |
|---|---|
| `lead` | Lead author, shown as "Name et al." |
| `photo`, `page` | Round photo from `members/images/round/` and the member page of the lead author |
| `journal`, `date`, `title`, `url` | The paper's details and link |
| `summary` | A few sentences in plain language |
| `figure`, `alt`, `credit` | Image shown at the top of the card (4:3 works best), its description and credit line |

## News page

The News page (`news.qmd`) is written by hand from the lab's LinkedIn posts: LinkedIn does not
update it automatically. One card is built per entry in the `news` list in the page's front
matter. The cards are sorted by `date`, newest first, whatever order they are written in, so a new
entry can go anywhere in the list (items from the same month keep their order). The date must look
like `Nov 2026`: the build stops with a message if it does not.

| Field | What it is |
|---|---|
| `title`, `date`, `text` | Headline, month and year, and a few sentences |
| `category` | Which subtab the item appears under: `Awards`, `Publications`, `Conferences` or `News` (shown as "In the media"). The subtabs and their order are set in the `sections` list; Openings is always last |
| `photos` | Optional. One or more images: a list of `src` and `alt`, shown one at a time with buttons. An item with no photo shows the lab logo in a box of the same size |
| `fit` | Optional. `fit: figure` shows the images whole in a taller (4:3) box instead of cropping them. Use it for paper figures and slides; every item in the Publications subtab does this by itself |
| `fit: portrait` | Optional. For a tall photo (for example a team portrait): it is shown whole, centred on a blurred copy of itself, instead of being cropped to the wide box |
| `focus` | Optional. Where the crop of a photo is centred, as `"50% 20%"` (across, down). The default is `"50% 30%"`; a smaller second number shows more of the top |
| `credit` | Optional. Credit line or short description of the images |
| `link`, `link_text` | Optional. Button linking to the paper or article |
| `home` | Optional. By default the Home page shows the newest news item that has a photo and is not in the Publications subtab. `home: true` pins one item there instead; keep it on one item only, and remove it when the item should no longer be pinned |

Images go in `images/news/` as JPEG, no wider than 1200 pixels. Photos are cropped to a wide
2:1 box, so keep the people and the subject in the middle; paper figures (see `fit`) are not cropped.
Before adding one, check that it shows no private details, such as a phone number on a poster, and
that its licence allows reuse.

## Openings (on the News page)

The Openings subtab of the News page (link: `news.html#openings`) lists the lab's positions, from the `openings` list in the
front matter of `news.qmd` (newest first). To add a position, add an entry at the top of that list.
The day after its deadline a position is marked with a "Closed" tag by itself (the button to the ad stays)
(when the site is rebuilt, and also in the visitor's browser), so old entries can stay.

| Field | What it is |
|---|---|
| `title` | Job title, as in the Lund University ad |
| `type`, `location`, `start` | Kind of position and length, workplace, start date |
| `deadline` | Last day to apply, written as `YYYY-MM-DD` |
| `reference` | Optional. Lund University reference number (e.g. PA2026/3011) |
| `summary` | A few sentences about the position, in our own words |
| `contact` | Optional. Name of the person to contact (no phone numbers or emails) |
| `link` | Link to the ad on lu.varbi.com |
