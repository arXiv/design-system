// The React host: the generated components, imported from the package consumers install
// (@arxiv/brand-templates, a file: dependency on the repository root). Plain JS: the only
// .jsx in the repository is generated. Under StrictMode, as the React consumers run it (in
// development, effects run twice). ?hide_announcement drops the band, ?hide_nav the nav;
// ?actions passes page actions, React elements with their own handler, as app.py's ?actions.
import { createElement as h, Fragment, StrictMode, useState } from "react";
import { createRoot } from "react-dom/client";
import Head from "@arxiv/brand-templates/Head";
import Header from "@arxiv/brand-templates/Header";
import Footer from "@arxiv/brand-templates/Footer";

const query = new URLSearchParams(location.search);
const STATIC = "/assets/";
const MEMBER = h("span", { className: "ack-member-inline" }, ", ", h("strong", null, "RWTH Aachen"));
const icon = () => h("svg", { viewBox: "0 0 24 24", "aria-hidden": "true" }, h("circle", { cx: 12, cy: 12, r: 9 }));
const label = (text) => h("span", { className: "is-sr-only" }, text);

function Actions() {
  const [clicks, setClicks] = useState(0);
  return h(Fragment, null,
    h("a", { href: "#pdf", title: "PDF" }, icon(), label("PDF")),
    h("button", { type: "button", title: "Contents", "data-clicks": clicks,
                  onClick: () => setClicks((n) => n + 1) }, icon(), label("Contents")));
}

createRoot(document.getElementById("root")).render(
  h(StrictMode, null,
    h(Head, { static_base: STATIC }),
    h(Header, { static_base: STATIC, hide_announcement: query.has("hide_announcement"), hide_nav: query.has("hide_nav"),
                header_page_actions: query.has("actions") ? h(Actions) : null }),
    h("main", { className: "ds-container" }, h("p", null, "React host")),
    h(Footer, { static_base: STATIC, member_institution: MEMBER })));
