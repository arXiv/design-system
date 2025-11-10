# A Visual Audit of the arXiv Platform

**Prepared for:** arXiv Stakeholders
**Prepared by:** Shamsi Brinn
**Date:** 11/10/2025



## 1. Executive Summary

This audit of 53 platform screenshots reveals a critical finding: **arXiv is not one platform, but a patchwork of at least eight distinct, conflicting, and fragmented design systems.**

This fragmentation has created a disjointed, confusing, and dated user experience. The lack of a "single source of truth" for design results in severe inconsistencies in the most critical components—specifically **Buttons**, **Forms**, and **Navigation**.

* **The Problem:** We found 7+ styles for the primary "Submit" button, 3+ styles for text inputs, and at least 8 different page headers.
* **The Impact:** This fragmentation directly increases technical debt, slows down feature development, confuses users, and erodes brand trust.
* **The Path Forward:** A redesign is not a simple "reskin." It must be a **unification project** to replace these 8+ legacy systems with a single, modern, and enforceable design system.

> This report visually demonstrates the scale of this dysfunction. The evidence is clear: the current state is unmanageable, and a unified design system is a foundational necessity for the platform's future.

---

## 2. The 8 Systems Currently Running Your Platform

Our audit identified eight distinct "mini" design systems, each with its own visual language, components, and layout. They are often mixed and matched on the same page.

| **System #** | **Name** | **Key Identifier(s)** | **Example Screen(s)** |
| :--- | :--- | :--- | :--- |
| **1** | **"Admin Console"** | Pale Green sidebar (`#EFF5E0`), light-gray header. | `admin-console-dashboard.jpg` |
| **2** | **"Public-Facing"** | Red & Black header (`#B31B1B`), Blue action color. | `account-login.jpg`, `browse-abs.jpg` |
| **3** | **"Reading Experience"**| Minimal dark/black header, focus on content. | `browse-html.jpg`, `browse-PDF.jpg` |
| **4** | **"CHECK Tool"** | `CHECK` logo, Olive-Green primary button. | `check-home.png` |
| **5** | **"Info & Brand"** | 3-column layout, header with embedded search. | `info-donate.jpg`, `info-policies.jpg` |
| **6** | **"Bare-Bones Forms"** | Massive serif "arXiv.org" title, 3D-inset inputs. | `claim-with-paper-password.png` |
| **7** | **"Transactional Email"**| No branding, system fonts, plain HTML. | `endorsement-code-email.png` |
| **8** | **"Headerless Forms"** | No header/footer, plain black text title. | `registration - page 2.jpg` |

---

## 3. Anatomy of a "Frankenstein" Page

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

## 4. CRITICAL FAILURE: 7+ Styles for One Primary Action

A platform's "Submit" or "Continue" button is its most critical component. We found **seven** different styles for this single action, demonstrating a total lack of standardization.

### Style 1: The "Solid Color" Button (4 Variations)

The most common pattern, but the color is inconsistent and context-dependent.

| **Solid Blue** | **Solid Green** | **Solid Olive** | **Solid Gray** |
| :--- | :--- | :--- | :--- |
| Used for login and search. | Used for the submission flow. | Used only in the "CHECK" tool. | Used for "Search" on the homepage. |
| `(Image: account-login.jpg)` | `(Image: submit-license.jpg)` | `(Image: check-home.png)` | `(Image: browse-home.jpg)` |

### Style 2: The "Ghost/White" Button (2 Variations)

Used as a primary action, but its styling is inconsistent.

| **White w/ Black Text** | **White w/ Red Text** |
| :--- | :--- |
| `(Image: browse-search-advanced.jpg)` | `(Image: browse-abs.jpg)` |

### Style 3: The "Legacy/One-Off" Button (3 Variations)

These styles appear to be from different eras of development.

| **Tiny Native Gray** | **Beveled Dark Blue** | **Light Blue "Donate"** |
| :--- | :--- | :--- |
| The default HTML button. | A unique, 3D style. | A unique, bordered style with a drop shadow. |
| `(Image: registration - page 2.jpg)` | `(Image: you-are-not-endorsed.png)` | `(Image: info-donate.jpg)` |

> **"So What?"**
> Users should never have to guess what the primary action on a page looks like. This fragmentation is the single most damaging inconsistency on the platform.

---

## 5. INCONSISTENCY: Forms & Inputs

After buttons, form inputs are the most common interactive element. The platform is undecided on whether to use native browser styles or custom styles.

### The "Checkbox Test": Custom vs. Native

Even within the **same user flow (System 2)**, the checkbox style is inconsistent.

| **Custom Blue Checkbox** | **Native Browser Checkbox** |
| :--- | :--- |
| `(Image: account-login.jpg)` | `(Image: submit-verify.jpg)` |

### The "Text Input Test": 3 Competing Styles

Users are presented with different text fields on almost every form.

| **Style 1: Modern** | **Style 2: Admin** | **Style 3: Legacy** |
| :--- | :--- | :--- |
| White background, thin gray border. | Light gray background, no border. | 3D `inset` border, white background. |
| `(Image: account-login.jpg)` | `(Image: admin-console-memb-inst.jpg)` | `(Image: claim-with-paper-password.png)` |

> **"So What?"**
> This inconsistency makes the platform feel unpolished and untrustworthy. It's a classic sign of high technical debt, where new code is written instead of reusing existing components.

---

## 6. INCONSISTENCY: Page Headers & Navigation

A user should always know "where" they are. The platform uses at least 6 different header styles, providing no single, consistent brand anchor.

| **Header 1: Admin (Sys 1)** | **Header 2: Public (Sys 2)** | **Header 3: Info (Sys 5)** |
| :--- | :--- | :--- |
| Light gray, "ADMIN" logo, right-nav. | Black top bar, main red bar, `user` sub-nav. | Red bar *with search embedded in it*. |
| `(Image: admin-console-dashboard.jpg)` | `(Image: account-user-page.jpg)` | `(Image: info-policies.jpg)` |

| **Header 4: Reader (Sys 3)** | **Header 5: CHECK (Sys 4)** | **Header 6: Bare-Bones (Sys 6)** |
| :--- | :--- | :--- |
| Minimal dark gray/black bar. | Light gray bar, "CHECK" logo. | No header, just a massive serif title. |
| `(Image: browse-html.jpg)` | `(Image: check-home.png)` | `(Image: endorsement-form-for-endorsER.png)` |

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
