I built the three pages and `build/search/search.css`. I also added `build/search/search.js`, which the brief did not ask for. I checked the pages with a local Chrome screenshot of the results and invalid-query pages. I did not screenshot or test the no-results page, the 360px width, or the keyboard.

**1. Design system parts used**
- Setup and chrome: `using.html` setup, header, footer, theme toggle and skip link.
- Form and layout: forms (`.ds-form`, `.ds-field`, `.ds-check`, `.field-error`), buttons, the error and info alerts, and the numbered-pages pager.
- Result content: tags with tooltips for categories, the show-more pattern for abstracts, the date-row wording from the versions page, and the card grid for search tips.

**2. Where the design system had no answer**
- **Matched words:** there is no highlight style. I used `mark.search-match` with the accent wash plus bold, so colour is not the only cue.
- **Result list and label/value rows:** neither exists. I used spacing between results instead of boxes, and a compact label/value list based on the data card.
- **Date row:** `.ds-date-row` is documented but not in the stylesheet. I styled it in `search.css`.
- **Tooltip position:** I anchored it to the category row so it cannot run off narrow screens.
- **Radio-group fieldset:** I added a small reset for it.
- **Excerpt toggle:** the excerpt is not a prefix of the full abstract, so I swap two paragraphs with a show-more button added by script. Without script the full abstract shows.

**3. Not done, or done differently**
- **10,000-result notice:** this page has only 8,291 results, so nothing is unreachable. I show it as a standing hint under the pager and left the markup for the capped case in a comment.
- **Authors:** no sample result has more than 25, so the "N more authors not shown" text is in the generator and in a comment, not visible.
- **Dates:** I followed the design system's labels. On result 6 the v1 date shows as "Submitted" and the latest version's date as "Revised … (this version)".
- **Form action:** the form posts to `/search/`, so submitting does not work when the file is opened locally. Author links also point to `/search/…`, and the format and abstract links point to arxiv.org.
- **Author search names:** I guessed the "Surname, Forename" order from the displayed name.
- **Not run:** the drift check and policy checks.