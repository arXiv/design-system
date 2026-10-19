// GENERATED from templates/arxiv_brand/footer.html by templates/generate.py — do not edit
export default function Footer({ help_url = "https://info.arxiv.org", member_institution = "" }) {
  return (
    <>
      <footer className="ds-site-footer">{" "}
        <div className="ds-site-footer-grid">{" "}
          <div className="ds-site-footer-main">{" "}
            <div className="ds-site-footer-ack">{" "}
              We gratefully acknowledge support from our <a href={`${help_url}/about/funders.html`}><strong>major funders</strong></a>,{" "}
              <a href={`${help_url}/about/ourmembers.html`}><strong>member institutions</strong></a>{member_institution},{" "}
              and all contributors.{" "}
            </div>{" "}
            <nav className="ds-site-footer-links" aria-label="Site navigation">{" "}
              <a href={`${help_url}/about`}>About</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help`}>Help</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help/contact.html`}>Contact</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help/subscribe.html`}>Subscribe</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help/license/index.html`}>Copyright</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help/policies/privacy_policy.html`}>Privacy</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href={`${help_url}/help/web_accessibility.html`}>Accessibility</a> <span className="ds-site-footer-sep" aria-hidden="true">&middot;</span>{" "}
              <a href="https://status.arxiv.org/" target="_blank" rel="noopener noreferrer">Operational Status<span className="is-sr-only"> (opens in new tab)</span></a>{" "}
            </nav>{" "}
          </div>{" "}
        </div>{" "}
      </footer>
    </>
  );
}
