// GENERATED from templates/arxiv_brand/header.html by templates/generate.py — do not edit
import type { ReactElement } from 'react';

export interface HeaderProps {
  /** Root URL of the design-system asset route, with a trailing slash; production by default (init_app reads BRAND_STATIC_BASE). Default: "https://static.arxiv.org/static/design-system/latest/". */
  static_base?: string;
  /** Extra classes on .ds-site-header (arxiv-docs passes mkdocs-material's 'md-header'). Default: "". */
  header_variant?: string;
  /** Scheme + BASE_SERVER, no trailing slash: home, search, submit and the IgnoreMe trap (init_app reads BASE_SERVER and EXTERNAL_URL_SCHEME). Default: "https://arxiv.org". */
  base_url?: string;
  /** Scheme + AUTH_SERVER (else BASE_SERVER), no trailing slash: /login and account_path; "" makes them site-relative. Default: "https://arxiv.org". */
  auth_url?: string;
  /** The signed-in Account page on auth_url, with its leading slash (the keycloak account portal: /user-account/). Default: "/user". */
  account_path?: string;
  /** Scheme + HELP_SERVER, no trailing slash: donate and every footer info link. Default: "https://info.arxiv.org". */
  help_url?: string;
  /** Drop the public nav and the search overlay, for a sub-site with its own (info.arxiv.org). Default: false. */
  hide_nav?: boolean;
  /** Drop the announcement band, for a host that shows none (a staff tool, an embedded view). Default: false. */
  hide_announcement?: boolean;
  /** Per session: one "Account" link (auth_url + account_path, where the reader logs out) instead of "Log in". Default: false. */
  signed_in?: boolean;
}

export default function Header(props: HeaderProps): ReactElement;
