// The React host: the generated components, imported from the package consumers install
// (@arxiv/brand-templates, a file: dependency on the repository root). Plain JS: the only
// .jsx in the repository is generated. Under StrictMode, as the React consumers run it (in
// development, effects run twice). ?hide_announcement drops the band.
import { createElement as h, StrictMode } from "react";
import { createRoot } from "react-dom/client";
import Head from "@arxiv/brand-templates/Head";
import Header from "@arxiv/brand-templates/Header";
import Footer from "@arxiv/brand-templates/Footer";

const query = new URLSearchParams(location.search);
const STATIC = "/assets/";
const MEMBER = '<span class="ack-member-inline">, <strong>RWTH Aachen</strong></span>';

createRoot(document.getElementById("root")).render(
  h(StrictMode, null,
    h(Head, { static_base: STATIC }),
    h(Header, { static_base: STATIC, hide_announcement: query.has("hide_announcement") }),
    h("main", { className: "ds-container" }, h("p", null, "React host")),
    h(Footer, { static_base: STATIC, member_institution: MEMBER })));
