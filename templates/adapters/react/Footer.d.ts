// GENERATED from templates/arxiv_brand/footer.html by templates/generate.py — do not edit
import type { ReactElement } from 'react';

export interface FooterProps {
  /** Root URL of the design-system asset route, with a trailing slash; production by default (init_app reads BRAND_STATIC_BASE). Default: "https://static.arxiv.org/static/design-system/latest/". */
  static_base?: string;
  /** Scheme + HELP_SERVER, no trailing slash: donate and every footer info link. Default: "https://info.arxiv.org". */
  help_url?: string;
  /** Per request, the IP-matched member: '' (an anonymous reader), '<span class="ack-member-inline">, <strong>Name</strong></span>', or that span empty and hidden, which chrome/header.js fills from the same-origin /institutional_banner. Default: "". */
  member_institution?: string;
}

export default function Footer(props: FooterProps): ReactElement;
