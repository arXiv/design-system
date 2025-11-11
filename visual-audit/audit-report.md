# A Visual Audit of the arXiv Platform

**Prepared for:** arXiv Stakeholders
**Prepared by:** Shamsi Brinn
**Date:** 11/10/2025


## 1. Executive Summary

The audit reveals the extent of arXiv's inconsistent interfaces: **arXiv's visual identity is made up of a patchwork of eleven distinct, conflicting, incomplete, and fragmented design systems.** The lack of a "single source of truth" for design results in severe inconsistencies in critical components like **Buttons**, **Forms**, and **Navigation**. As an example, I found 7+ styles for the primary "Submit" button, 3+ styles for text inputs, and at least 8 different page headers across arXiv.

**The Impact:** This fragmentation results in a inconsistent, confusing, and dated user experience that errodes trust. On the development side it directly increases technical debt and slows down front-end development. Poor UI and HTML in forms also lowers data quality at the point of entry.
**The Path Forward:** We can turn it around with a single, unified design system applied across all of arXiv. A redesign is not a simple "reskin." It is a **unification project** to replace the patchwork of 8 systems with a single, modern design system that is consistent with our values (utilitarian, international, fast-loading) and goals (improve user experience and speed up development).

*Note: For this audit I reviewed newer versions of systems if they will be replacing legacy in a reasonable amount of time and with a resonable degree of certainty. ie: Admin Console, new Account and Registration, new Login, and Submit 2.0.*

> The short story: arXiv's design is highly inconsistent. The current state is bad for users and data quality and slows development. A unified design system is a foundational necessity for the platform's future.


## 2. The 11 Design Systems We Currently Run

This audit identified *eleven* distinct (though incomplete) design systems, each with its own visual language, components, and layout. They are often mixed and matched on the same page.

| **System #** | **Name** | **Key Identifier(s)** | **Example Pages** |
| :--- | :--- | :--- | :--- |
| **2** | **"Browse"** | Primary double red & black header, browser default link color. | !(thumb-browse.png) |
| **2** | **"Search"** | Different red & black header, link color, tag chicklets, colors. | !(thumb-search.png)|
| **6** | **"Super-legacy Forms"** | Massive serif "arXiv.org" title, 90s-styled inputs. | !(thumb-old-legacy.png) |
| **1** | **Admin Console** | Some overlap with arXiv Check styles. Introduces right sidebar, Material UI inffluence | !(thumb-admin-console.png) |
| **4** | **arXiv Check** | Some overlap with Admin Console. Introduces right panels, multiple new UI paradigms, Bootstrap inffluence | !(thumb-check.png) |
| **3** | **"HTML pages"**| Red header, dark mode, dynamic | !(thumb-html.png) |
| **3** | **"PDF"**| Largely user-determined, with arXiv watermark | !(thumb-PDF.png) |
| **5** | **"Info site"** | 3-column layout, unique header, embedded search. | !(thumb-info.png) |
| **7** | **"Transactional Emails"**| No branding, system fonts, plain HTML. | !(thumb-email.png) |
| **8** | **"Accounts and Login"** | Emerging design style, introduces navigation, simplifies header | !(thumb-account.png) |
| **8** | **"Submission"** | Emerging design style, introduces navigation, simplifies header | !(thumb-submit.png) |


---

## 3. Examples

### Buttons
A platform's button is its single most critical component because it is the primary user flow signal. The only consistent aspect of arXiv's buttons styles is their inconsistency.

#### Main Styles
| **Solid Blue** | **Solid Green** | **Solid Olive** | **Solid Gray** | **White w/ Black Text** | **White w/ Red Text** | **Light Blue "Donate"** |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| Used for login and search. | Used for the submission flow. | Used only in the "CHECK" tool. | Used for "Search" on the homepage. |    |   | A unique, bordered style with a drop shadow. |
| `(Image: account-login.jpg)` | `(Image: submit-license.jpg)` | `(Image: check-home.png)` | `(Image: browse-home.jpg)` | `(Image: browse-search-advanced.jpg)` | `(Image: browse-abs.jpg)` | `(Image: info-donate.jpg)` |

#### Legacy Styles
| **Tiny Native Gray** | **Beveled Dark Blue** | 
| :--- | :--- | 
| The default HTML button. | A unique, 3D style. | 
| `(Image: registration - page 2.jpg)` | `(Image: you-are-not-endorsed.png)` | 


> Users should never have to guess what the primary action on a page looks like. This fragmentation damages user trust, and is the first component being addressed by the new design system.

---

### Forms
After buttons, form inputs are the most common interactive element. Forms play a critical role in data quality by increasing user comprehension and accessibility. arXivs platform currently waffles between a variety of custom styles and browser defaults.

#### Checkboxes
| **Custom Blue Checkbox** | **Native Browser Checkbox** |
| :--- | :--- |
| `(Image: account-login.jpg)` | `(Image: submit-verify.jpg)` |

#### Text Inputs
| **New Auth** | **Admin Console** | **Legacy** |
| :--- | :--- | :--- |
| White background, thin gray border. | Light gray background, no border. | 3D `inset` border, white background. |
| `(Image: account-login.jpg)` | `(Image: admin-console-memb-inst.jpg)` | `(Image: claim-with-paper-password.png)` |


> This inconsistency is a classic sign of high technical debt. With no design system, new front end work usually meant introducing new styles instead of reusing existing components.

---

### Headers
A user should always know where they are and headers (along with navigation and breadcrumbs) provide that mental map. arXiv uses many different header and navigation styles, providing no consistent wayfinding or brand anchor.

| **Browse** | **Older browse** | **?** |
| :--- | :--- | :--- |
| ? | ? | ?|
| `(Image: admin-console-dashboard.jpg)` | `(Image: account-user-page.jpg)` | `(Image: info-policies.jpg)` |

| **Admin Console** | **New Account page** | **Info site** |
| :--- | :--- | :--- |
| Light gray, "ADMIN" logo, right-nav. | Black top bar, main red bar, `user` sub-nav. | Red bar *with search embedded in it*. |
| `(Image: admin-console-dashboard.jpg)` | `(Image: account-user-page.jpg)` | `(Image: info-policies.jpg)` |

| **HTML pages** | **arXiv Check** | **Super-legacy** |
| :--- | :--- | :--- |
| Minimal dark gray/black bar. | Light gray bar, "CHECK" logo. | No header, just a massive serif title. |
| `(Image: browse-html.jpg)` | `(Image: check-home.png)` | `(Image: endorsement-form-for-endorsER.png)` |

---

## 3. A "Frankenstein" Page

Many pages are built by "stitching together" components from multiple systems. This creates an incoherent and jarring user experience.

The screen `you-are-not-endorsed.png` is a perfect example, combining **five different visual styles** into one view:

1.  **Header:** From **System 2** (Public-Facing).
2.  **Stepper:** A new, text-based `>>` style. **(Style 1)**
3.  **Error Banner:** A new, red banner style. **(Style 2)**
4.  **Section Headers:** New, solid-red background headers. **(Style 3)**
5.  **Info Box:** A new, bordered-box style. **(Style 4)**
6.  **Primary Button:** A new, 3D/beveled dark blue "Continue" button. **(Style 5)**

> **"So What?"**
> When a single page has no internal visual consistency, the user cannot learn the platform's interaction patterns. This page alone has 3 new button/banner styles not seen anywhere else.

---

## 7. The Root Cause: An Ignored "Source of Truth"

The audit of `info-brand-colors.jpg` revealed an **"official" brand guideline**.

**This guideline is almost universally ignored.**

This is the "smoking gun" of the platform's dysfunction. A design system exists, but it is not being used or enforced.

* **The "Official" Blue:** `Open Blue (#006FBA)`
* **The "Actual" Blue:** `Brighter Blue (#007BFF)`
* **The Conflict:** The "Public-Facing" system (System 2), the most visible part of the platform, uses a different blue than the one specified in its *own* brand documentation.

> **"So What?"**
> This proves that the root cause is a lack of **process and governance**. Without a team empowered to build, maintain, and enforce a single system, fragmentation will continue indefinitely.

---

## 8. Conclusion & Path Forward

The visual evidence is clear: the platform is suffering from severe design fragmentation. This is not a simple "visual cleanup" project; it is a foundational imperative to create a **single, unified design system**.

### Recommendations

1.  **Establish a Design Authority:** Form a dedicated team (Design, Product, Engineering) with the authority and resources to own the new design system.
2.  **Unify "Money Components" First:** The new system must start by solving the most fragmented components: **Buttons**, **Form Inputs**, and **Colors**.
3.  **Consolidate Page Shells:** The next priority is to create one global **Header** and **Footer** to be used across the entire platform.
4.  **Create a Migration Plan:** Systematically replace the 8+ legacy systems, starting with the highest-traffic user flows (System 2: Public-Facing) before migrating internal tools.

This unification will reduce technical debt, accelerate development, and—most importantly—provide a coherent, professional, and trustworthy experience for your users.
