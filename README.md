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
`name`, `text` and `links` (`label`, `url`).

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
matter, in the order listed (newest first). To add news, add an entry at the top of that list.

| Field | What it is |
|---|---|
| `title`, `date`, `text` | Headline, month and year, and a few sentences |
| `category` | Label on the card. Names in `categories_list` also get a button at the top of the page; other items appear under All only |
| `photos` | One or more images: a list of `src` and `alt`, shown one at a time with buttons |
| `credit` | Optional. Credit line or short description of the images |
| `link`, `link_text` | Optional. Button linking to the paper or article |
| `home` | Optional. `home: true` shows this item on the Home page. Keep it on one item only |

Images go in `images/news/`, all as JPEG at 1200 x 900 pixels (4:3). Before adding one, check that
it shows no private details, such as a phone number on a poster, and that its licence allows reuse.
