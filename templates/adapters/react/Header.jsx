// GENERATED from templates/arxiv_brand/header.html by templates/generate.py — do not edit
import { useEffect } from 'react';

export default function Header({ static_base = "https://static.arxiv.org/static/design-system/latest/", header_variant = "", base_url = "https://arxiv.org", auth_url = "https://arxiv.org", account_path = "/user", help_url = "https://info.arxiv.org", hide_nav = false, hide_announcement = false, signed_in = false }) {
  useEffect(() => {
    const tags = [`${static_base}chrome/banner.js`, `${static_base}chrome/header.js`].map((src) => {
      const s = document.createElement('script');
      s.src = src;
      document.body.appendChild(s);
      return s;
    });
    return () => { tags.forEach((s) => s.remove()); };
  }, [static_base]);

  return (
    <>
      {!hide_announcement && (<>
      <div id="ds-announcement"></div>
      </>)}
      <header className={`ds-site-header ${header_variant}`}>{" "}
        <a aria-hidden="true" tabIndex="-1" href={`${base_url}/IgnoreMe`} className="is-sr-only"></a>{" "}
        <a href={`${base_url}/`} className="ds-site-header-logo" aria-label="archive home">{" "}
          <img src={`${static_base}logos/arxiv-logo.svg`} alt="archive" />{" "}
        </a>{" "}
        <button type="button" id="ds-nav-toggle" className="ds-site-header-nav-toggle"
          aria-label="Open menu" aria-controls="ds-site-header-nav" aria-expanded="false">{" "}
          <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" focusable="false">{" "}
            <line x1="3" y1="6" x2="21" y2="6" /><line x1="3" y1="12" x2="21" y2="12" /><line x1="3" y1="18" x2="21" y2="18" />{" "}
          </svg>{" "}
        </button>{" "}
        {!hide_nav && (<>{" "}
        <nav className="ds-site-header-nav" id="ds-site-header-nav" aria-label="Main navigation">{" "}
          <a id="ds-search-toggle" href={`${base_url}/search`} aria-controls="ds-search-overlay" aria-expanded="false">{" "}
            <svg className="ds-nav-icon" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" aria-hidden="true" focusable="false">{" "}
              <circle cx="11" cy="11" r="8" />{" "}
              <line x1="21" y1="21" x2="16.65" y2="16.65" />{" "}
            </svg>{" "}
            Search{" "}
          </a>{" "}
          <a href={`${base_url}/submit`}>Submit</a>{" "}
          <a href={`${help_url}/about/donate.html`}>Donate</a>{" "}
          <span className="ds-site-header-divider" aria-hidden="true"></span>{" "}
          {signed_in && (<><a href={`${auth_url}${account_path}`} className="ds-site-header-login">Account</a></>)}{" "}
          {!signed_in && (<><a href={`${auth_url}/login`} className="ds-site-header-login">Log in</a></>)}{" "}
        </nav>{" "}
        </>)}{" "}
      </header>
      {!hide_nav && (<>
      <div className="ds-search-overlay" id="ds-search-overlay" hidden>{" "}
        <div className="ds-search-overlay-panel" role="search">{" "}
          <form method="GET" action={`${base_url}/search`}>{" "}
            <label htmlFor="ds-search-input" className="is-sr-only">Search arXiv</label>{" "}
            <input type="text" name="query" id="ds-search-input" className="ds-input" autoComplete="off"
              placeholder="Search papers by title, author, abstract, or ID..." />{" "}
            <input type="hidden" name="searchtype" value="all" />{" "}
            <input type="hidden" name="source" value="header" />{" "}
          </form>{" "}
          <p className="ds-hint">{" "}
            Press Enter to search &middot; <a href={`${base_url}/search/advanced`}>Advanced search</a>{" "}
          </p>{" "}
        </div>{" "}
      </div>
      </>)}
    </>
  );
}
