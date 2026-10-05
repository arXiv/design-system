You are a frontend developer at arXiv. This repository is the arXiv design system. Follow its guidance for AI assistants.

# Redesign the simple search page

arXiv's search at arxiv.org/search is being redesigned on the design system. Build a static HTML page that shows the new design of the results page. It is a public page for researchers.

Work only from this repository and this brief. Do not fetch anything from the network, and do not copy the current page's design.

## What a searcher can do

- Type a query, and choose which field to search. The fields are: All fields, Title, Author(s), Abstract, Comments, Journal reference, ACM classification, MSC classification, Report number, arXiv identifier, DOI, ORCID, License (URI), arXiv author ID, Help pages, Full text.
- Choose to show or hide abstracts in the results.
- Go to Advanced Search, which is a separate page.
- Choose how many results are on a page: 25, 50, 100 or 200.
- Choose the order: Announcement date (newest first), Announcement date (oldest first), Submission date (newest first), Submission date (oldest first), Relevance.
- Move between pages of results. Search returns at most 10,000 results, so the last pages of a very large result set cannot be reached. The searcher is told this and asked to refine the search.

The page works as an ordinary form sent with GET. The searcher can always see and change the query that produced the results.

## What each result shows

Always: the arXiv identifier, linked to the paper's abstract page; links to each available format; the subject categories, with the primary one first; the title; the authors, each linked to a search for that author; the date this version was submitted; the month the paper was first announced.

When abstracts are shown: an excerpt of the abstract, which the searcher can open to read the whole abstract and close again.

Only when the record has them: comments, journal reference, report number, MSC class, ACM class, a DOI linked to doi.org, and the date version 1 was submitted when the result is a later version.

A result lists at most 25 authors. Beyond that it says how many more are not shown.

The words that matched the query are marked wherever they appear in a result. A category code such as astro-ph.CO has a full name, and the searcher can find out what it is.

## The page

`build/search/results.html`. The query is "lensing" in All fields. There are 18,659 results, 50 to a page, newest announcement first, and this is page 1. With 50 to a page, the last page that can be reached is page 200. Build the six results in the sample content below; the real page would show 50.

## How to build

Use the design system for everything it covers. Where it has no answer, do what its guidance says to do in that case.

If you need CSS that the design system does not provide, put all of it in `build/search/search.css` and nowhere else. Do not change any existing file.

Do not run git commands and do not start a server.

## Your final message

At most 15 short lines, in three parts:

1. The parts of the design system you used.
2. Each place the design system had no answer: what you did, and why.
3. Anything in this brief you did not do, and why.
