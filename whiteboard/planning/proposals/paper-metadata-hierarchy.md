# Paper metadata hierarchy (draft)

Drafted 2026-10-05 for Shamsi's review. Which facts about a paper come first, in a list of papers and on one paper's page, based on arXiv's own user research. When it is agreed, it becomes a docs page and the search result pattern follows it.

The evidence behind each line (quotes, with Jira keys and interview dates) is in `~/arxiv/research/paper-metadata/evidence-2026-10-05.md`. It stays out of this repository because the repository is public and the quotes come from named participants. Jira keys below point into the UX Data Hub.

## In a list of papers

Search results, new-submission listings, an author's papers.

| Order | Field | Evidence |
|---|---|---|
| 1 | **Title** | The first-pass filter: readers decide from the title whether to read on (two interviews; AUXDH-813, -1101). |
| 2 | **Authors**, each a link | Second. Many readers follow authors they trust (AUXDH-798; survey items 5, 43, 59), and author search is a main way into arXiv. Contested: some readers ignore authors, and one asked for names to be hidden for fairness (AUXDH-1029). |
| 3 | **Date** | Directly under the authors. The one observation that places a field in a search result asks for exactly this (AUXDH-767). Recency matters to many readers (about six complaints about sort order). |
| 4 | **Abstract** | Where the decision is made. Evidence is split between showing it and opening it on demand (AUXDH-40 against AUXDH-38 and -812). Show the excerpt, with Show more for the rest, and keep the reader's choice to hide abstracts. |
| 5 | **Formats** (PDF, HTML) and the **identifier** | The actions after the decision (AUXDH-1101, -38). Nobody reports scanning the identifier to decide. |
| 6 | **Categories**, primary first | No evidence for their place in a list. Kept on the line with the identifier. |
| 7 | **Comments, journal reference, DOI** | No evidence for lists. Shown when present, last, in smaller type. |
| — | Report number, MSC and ACM class, licence | No evidence for lists, and often empty (AUXDH-1170). Proposal: show them in a list only when the search matched them. |

## On one paper's page

Where it differs from a list:

- **Title, authors, abstract, then the actions.** The download button between the authors and the abstract interrupts the reading order (AUXDH-894). In the 2019 feedback, about 14 people wanted it after the abstract or less prominent, 4 under the title, 2 at the top.
- **The date under the authors** (AUXDH-983), and **one date display, not two**: a dateline at the top and a history at the bottom read as duplicates (AUXDH-913).
- **DOI and journal reference matter here**, more than in lists (AUXDH-938, -1140, -1018).
- **The HTML format link next to PDF**, not under "other formats" (accessibility interviews, Part D).
- **Versions:** readers cannot tell how versions differ (AUXDH-17).

## What readers get wrong

Each of these suggests a rule.

1. **They confuse submitted and announced dates** (AUXDH-744). Every date carries its label; the Versions date row already does this.
2. **They read the identifier as a year:** 2003.xxxx looks like 2003 (AUXDH-1155, -1156). A visible date near the identifier prevents it.
3. **Journal publication does not show** (AUXDH-1018, -1918), partly because authors rarely fill in the fields (AUXDH-1170).
4. **Two date displays look like duplicates** on the abstract page (AUXDH-913).

## Where the evidence is thin

- **No study watches people scan a list.** The list order rests on requests, complaints and two interviews. A short task-based test of a results page would settle it.
- **Only the date has a stated position in a result** (AUXDH-767). Title before authors before abstract comes from the abstract page (AUXDH-894) and from lists that name the three fields without ranking them.
- **Citation counts** are asked for (AUXDH-751, -1008, -1114) and strongly opposed (AUXDH-1122, -1101). Not proposed here.
- **Sample skew:** much of the evidence is from the 2018 search relaunch and a 2019 mobile survey of mostly physicists, before HTML papers existed.

## Two corrections to the research notes

- `ux-observations-themes.md` says about 2,950 observations; the export has 1,588 rows.
- `accessibility-interviews-synthesis.md` section 20 files a quote about how screen readers pronounce the name "arXiv" as evidence about announcing the identifier. The raw notes are about the name. There is no interview evidence about how the identifier is announced.
