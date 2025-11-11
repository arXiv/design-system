# Visual Audit of the arXiv Platform

> **Audience:** Internal arXiv Stakeholders
> **Prepared by:** Shamsi Brinn
> **Date:** 11/10/2025


## 1. Executive Summary

The audit reveals the extent of arXiv's inconsistent interfaces: **arXiv's visual identity is made up of a patchwork of distinct, conflicting, incomplete, and fragmented visual languages.** The lack of a "single source of truth" for design results in a high level of inconsistency in layouts and user flow, as well as critical components like **Buttons**, **Forms**, and **Navigation**.

**The Impact:** An inconsistent, confusing, and dated user experience that errodes trust. On the development side it directly increases technical debt and slows down front-end development. Poor UI and HTML in forms also lowers data quality at the point of collection.
**The Path Forward:** We can turn it around with a single, unified design system applied across all of arXiv. A redesign is not a simple "reskin." It is a **unification project** to replace the patchwork of 8 systems with a single, modern design system that is consistent with our values (utilitarian, international, fast-loading) and goals (improve user experience and speed up development).

*Note: For this audit I reviewed newer versions of systems if they will be replacing legacy in a reasonable amount of time and with a resonable degree of certainty. ie: Admin Console, new Account and Registration, new Login, and Submit 2.0.*

> The short story: arXiv's design is highly inconsistent. The current state is bad for users and data quality and slows development. A unified design system is a foundational necessity for the platform's future.


## 2. The 11 Visual Languages We Currently Maintain

This audit identified *eleven* distinct (though incomplete) design systems, each with its own visual language, components, and layout. They are often mixed and matched on the same page.

| **Description** | **Example** |
| :--- | :--- |
| **Browse**: These pages are arXiv's most visited and have the greatest impact on the user experience as well as building the brand. They feature the 'standard' double red & black header, browser default link colors, Lucida font, and the use of tables for content organization. | ![Thumbnail of abstract page](images/thumb-browse.png) |
| **Search**: These pages were built more recently than Browse, in the 'NG' era. They use a different version of the red & black header and the Open Sans font. New UI elements were introduced including tag chicklets, colors, and cards. | ![thumbnail of search results](images/thumb-search.png)|
| **Super-legacy Forms**: Some of the oldest legacy code on arXiv can be found in forms that are still in use, immediately distinguised by the massive serif "arXiv.org" title in lieue of the logo, and their 90s-styled form inputs. | ![thumbnail of claim ownership page](images/thumb-old-legacy.png) |
| **arXiv Check**: arXiv Check introduces a right panel and reliance on accordions, and a color pallete that highlights access lime from the brand guide. Uses font IBM Plex Sans, our secondary brand font. Layouts and components have Bootstrap inffluence. Has dark mode, is responsive, accessibility is fair. | ![thumbnail of todo queue in arXiv Check](images/thumb-check.png) |
| **Admin Console**: This new system has some overlap with arXiv Check styles and we are working on bringing both systems closer together. This system introduces a right sidebar and shows strong Material UI inffluence. Has dark mode, is responsive, accessibility is fair. | ![thumbnail of paper details in Admin Console](images/thumb-admin-console.png) |
| **HTML pages**: The HTML paper pages were introduced a few years ago, relying mainly on student and new developer work. The header reinforced a 'in-progress' message which we are now ready to retire. It has a dark mode, is responsive, and accessibility is high. It uses the Rival Sans font with STIX Two for math and shows ar5iv stylistic inffluence. | ![Thumbnail of a paper rendered as HTML](images/thumb-html.png) |
| **PDF**: The look and feel are user-determined and vary. The arXiv watermark is our sole branding element on PDFs and uses a serif font (is it Lucida?). | ![Thumbnail of the first page of a PDF with the arXiv watermark](images/thumb-pdf.png) |
| **Info site**: The mkdocs-based sub site introduces a 3-column layout and a new version of the black & red header. It uses arXiv's brand fonts of Freight Sans Pro and Freight Text Pro. It also adds navigation, in-page section nav, and it's own search. It includes arXiv's first dark mode and is responsive and accessible. | ![Thumbnail of the donate page on the info site](images/thumb-info.png) |
| **Transactional Emails**: Emails are also a canvas for consistent branding. Setting content entirely aside, arXiv system emails have no branding even in text form, leaving them feeling 'unsigned' and un-anchored. | ![thumbnail of an endorsement-related email](images/thumb-email.png) |
| **Accounts and Login**: The account and registration pages have an emerging design style that is still in progress. They introduce breadcrumb navigation in the header, simplify the user flow, and feature modern form components and validation. | ![Thumbnail of the new user account page, still in progress](images/thumb-account.png) |
| **Submission**: The code and styling is from the NG era but modified recently to accomodate newer changes to submission functionality and content. The NG design introduces a prominent stepper, 2 column layout, box shadows, green primary buttons, and more modern form elements (but not consistent with the account and login form elements). | ![thumbnail of the upload page in the new submission](images/thumb-submit.png) |


---

## 3. Examples

### Buttons
A platform's button is the single most critical component. As the primary user flow signal, it should be consistent across all areas of arXiv that a users group access. But the only consistent aspect of arXiv's buttons styles is their inconsistency!

| **Description** | **Example** |
| :--- | :--- |
| **Abstract and HTML**: The single most performed action on our site is to view a PDF. At desktop widths, it is a simple 90s style text link using the browser default color. At mobile it takes on button styling. HTML pages use the third button style. | ![alt](images/button-abs.png) ![alt](images/button-abs-mobile.png) ![alt](images/button-html.png) |
| **User Account**: The new user accounts use the first button style, the current account uses the second style. | ![alt](images/button-account.png) ![alt](images/button-account-current.png) ![alt](images/button-secondary-reg.png) |
| **arXiv Check and Admin Console**: We are working to bring arXiv Check and Admin Console in line with each others visual languages to improve efficiency for the EUST. It is a work in progress, but visible here is the prominence of the Access Lime color that distinguishes moderation tools from other parts of the site (an example of strategic inconsistency). | ![alt](images/button-check.png) ![alt](images/button-check-green.png) ![alt](images/button-admin-console.png) ![alt](images/button-secondary-admin-console.png) ![alt](images/button-secondary-check.png) |
| **Info site**: The info site heavily relies on text links, but when we use buttons they have this style that is consistent with our brand guide. | ![alt](images/button-info.png) |
| **Legacy**: You will still come across legacy code in some parts of the arXiv platform that fall back to browser default styles, including the catchup form on the arXiv homepage.  | ![alt](images/button-legacy.png) |
| **Submission**: The new Submit 2.0 introduces green primary action buttons and a subtle secondary button style. | ![alt](images/button-submit.png) ![alt](images/button-secondary-submit.png)|
| **Search**: The button style, though blue like on some other parts of the site, is not consistent with the blue used on the user account, info site, and abs buttons. The font and margins also differ. | ![alt](images/button-search.png) |
| **Special**: Used in the header on browse to draw attention to limited-time messages, like Giving Week or the annual survey. | ![alt](images/button-special.png) 


> Users should never have to hunt around for or guess what the primary action on a page looks like. The visual fragmentation in arXiv buttons damages user trust, and is the first component being addressed by the new design system.

---

### Headers
A user should always know where they are and headers (along with navigation and breadcrumbs) provide that mental map. arXiv uses many different header and navigation styles, providing no consistent wayfinding or brand anchor for our users.

#### Seven unique Black & Red headers
Though these headers have some visual similarities they all use different code. Note the differences in logo use and spacing, breadcrumb styles, the thank you messages and donate links, and search. 

*Account*
![alt](images/header-account.png)

*Browse*
![alt](images/header-browse.png)

*Category Taxonomy*
![alt](images/header-cat-tax.png)

*Info*
![alt](images/header-info.png)

*Login*
![alt](images/header-login.png)

*Submit*
![alt](images/header-submit.png)

*Endorsement*
![alt](images/header-endorsement.png)

#### Admin and Moderation Headers
*arXiv Check*
![alt](images/header-check-mod.png)

*Admin Console*
![alt](images/header-admin-console.png)

> The new Design System will introduce a shared header with the right amount of controlled customization to balance the needs of arXiv's different platform sections. It will include navigation and search elements, branding, and other content deemed strategically necessary.


---

### Forms
After buttons, form inputs are the most important interactive elements. Forms play a critical role in data quality by increasing user comprehension and accessibility. arXivs platform currently waffles between a variety of custom styles as well as browser defaults.

| **Description** | **Example** |
| :--- | :--- |
|  **Browse**: The forms in this section can both be seen on the homepage: the catchup form and search in the header. Each employs it's own styles without refences to the other's visual language. And both predate arXiv's brand guidelines. |  ![alt](images/form-browse.png) ![alt](images/form-header.png) |
|  **Submission**: These styles are from the NG era. They are more modern, and have improved usability and accessibility over Browse, but also add to the visual and design patchwork. |  ![alt](images/form-submit.png) |
|  **Account pages**: This is some of our most recent and modern code and probably our most accessible forms to date. But without a Design System to build on they are heavily influenced by Material UI rather than arXiv's brand guidelines. |  ![alt](images/form-account.png) |
|  **Legacy**: Not much to say here! These legacy forms fall back to browser default styles. They are surprisingly compatible with screen readers but usability is low. |  ![alt](images/form-legacy.png) |
|  **HTML Papers**: This is our only form on the HTML papers page, but is a good example of how the lack of a Design System leads to a vacuum in which new visual languages get created ad hoc. |  ![alt](images/form-html.png) |
|  **Search**: These styles share the most with Submit 2.0, as they are both NG era. But there are still significant differences between them and they do not have a shared underlying base so will likely diverge more as time goes on. |  ![alt](images/form-search.png) |

> This inconsistency is a classic sign of high technical debt. With no design system, new front end work usually meant introducing new styles instead of reusing existing components. The Design System will make it easy to build forms with high usability and accessibility, and that are consistent with our brand guidelines.

---

## 4. Conclusion & Path Forward

The visual evidence is clear: the platform is suffering from severe design fragmentation. This is not a simple "visual cleanup" project; We need a **single, unified design system** that we can apply across our systems, and that maintains the right balance of consistency and flexibility to meet the needs of each repository.

### Next Steps

1.  **Form a Design System team:** A dedicated team has been formed (Carly, Deyan, Shamsi) with the authority and resources to own the new design system. 
2.  **Focus on high value components:** The first step of the team is to roll out our most high value component: **The Button**. This will be a right-sized proof of concept for the design system framework, as well as an opportunity for the dev team to see it in action and get to know how it works. 
3.  **Expand the Design System to more components:** The next priority is to create one global **Header** and **Footer** to be used across the entire platform. The header includes multiple components (links, forms, logo, message boxes) so this is a significant expansion of the Design System. Our next priority after these shared element groups is **Forms**, also extremely high value.
4. **Complete the visual design system:** Simultaneously with #3 (expanding to more components) we will be making decisions about their visual display and coherence with a redesign. arXiv's redesign will emphasize utilitarianism, increasing usability, fast page load, internationalization, and accessibility. All design decisions will be embedded directly into the Design System so they can be deployed everywhere, consistently, with ease.
4.  **Integration:** Systematically apply the Design System to each repository once that repo code is moved to the cloud. Implementation order will probably follow which code is ready (ie: Submit and Wombat) rather than prioritizing our most high traffic systems (Browse and HTML papers).

> The implementation of the Design System will reduce technical debt, ease development pain, and—most importantly—provide a coherent, professional, and trustworthy experience for users.
