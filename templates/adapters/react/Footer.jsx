// GENERATED from templates/arxiv_brand/footer.html by templates/generate.py — do not edit
export default function Footer({ static_base = "https://static.arxiv.org/static/design-system/latest/", help_url = "https://info.arxiv.org", member_institution = "" }) {
  return (
    <>
      <footer className="ds-site-footer">{" "}
        <div className="ds-site-footer-grid">{" "}
          <div className="ds-site-footer-main">{" "}
            <div className="ds-site-footer-ack">{" "}
              We gratefully acknowledge support from our <strong>major funders</strong>,{" "}
              <a href={`${help_url}/about/ourmembers.html`}><strong>member institutions</strong></a><span dangerouslySetInnerHTML={{ __html: member_institution }} />,{" "}
              and <a href={`${help_url}/about/give_to_arxiv.html`}>all contributors</a>.{" "}
            </div>{" "}
            <nav className="ds-site-footer-links" aria-label="Site navigation">{" "}
              <a href={`${help_url}/about`}>About</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help`}>Help</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help/contact.html`}>Contact</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help/subscribe`}>Subscribe</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help/license/index.html`}>Copyright</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help/policies/privacy_policy.html`}>Privacy</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help/web_accessibility.html`}>Accessibility</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href="https://status.arxiv.org/" target="_blank" rel="noopener noreferrer">Operational Status<span className="is-sr-only"> (opens in new tab)</span></a>{" "}
            </nav>{" "}
          </div>{" "}
          <div className="ds-site-footer-funders">{" "}
            <div className="ds-site-footer-funders-label">Major funding support from</div>{" "}
            <div className="ds-site-footer-funders-logos">{" "}
              <a className="ds-funder-link" href="https://www.simonsfoundation.org/" target="_blank" rel="noopener noreferrer">{" "}
                <img className="ds-funder-logo" src={`${static_base}funders/simons-foundation.png`} alt="Simons Foundation" /><span className="is-sr-only"> (opens in new tab)</span>{" "}
              </a>{" "}
              <a className="ds-funder-link" href="https://www.sfi.org.bm/" target="_blank" rel="noopener noreferrer">{" "}
                <img className="ds-funder-logo" src={`${static_base}funders/simons-foundation-international.png`} alt="Simons Foundation International" /><span className="is-sr-only"> (opens in new tab)</span>{" "}
              </a>{" "}
              <a className="ds-funder-link" href="https://www.schmidtsciences.org/" target="_blank" rel="noopener noreferrer">{" "}
                <img className="ds-funder-logo" src={`${static_base}funders/schmidt-sciences.png`} alt="Schmidt Sciences" /><span className="is-sr-only"> (opens in new tab)</span>{" "}
              </a>{" "}
            </div>{" "}
          </div>{" "}
        </div>{" "}
      </footer>
    </>
  );
}
