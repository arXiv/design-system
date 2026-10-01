// Server-renders generated components for test_targets.py: reads {components: {name: path},
// cases: [{component, props}]} on stdin, writes [{html, scripts, errors}]: the markup, the
// scripts its useEffect loads (run at once, against a stub document) and what React logged
// (a development build, so every warning shows).
const fs = require("fs");
const os = require("os");
const path = require("path");
const esbuild = require("esbuild");

(async () => {
  const { components, cases } = JSON.parse(fs.readFileSync(0, "utf8"));
  const dir = fs.mkdtempSync(path.join(os.tmpdir(), "brand-react-"));
  const shim = path.join(dir, "react.js");
  fs.writeFileSync(shim, `export * from ${JSON.stringify(require.resolve("react"))};\n` +
                         "export function useEffect(effect) { effect(); }\n");
  fs.writeFileSync(path.join(dir, "entry.js"), Object.entries(components).map(([name, file]) =>
    `export { default as ${name} } from ${JSON.stringify(file)};\n`).join("") +
    'export { renderToStaticMarkup } from "react-dom/server";\nexport { createElement } from "react";\n');
  const files = new Set(Object.values(components));
  await esbuild.build({
    entryPoints: [path.join(dir, "entry.js")], outfile: path.join(dir, "bundle.cjs"), bundle: true,
    platform: "node", jsx: "automatic", logLevel: "error", nodePaths: [path.join(__dirname, "node_modules")],
    define: { "process.env.NODE_ENV": '"development"' },
    plugins: [{ name: "effects-at-once", setup: (build) => build.onResolve({ filter: /^react$/ },
      (args) => (files.has(args.importer) ? { path: shim } : undefined)) }],
  });
  const lib = require(path.join(dir, "bundle.cjs"));
  const log = console.error;
  const results = cases.map(({ component, props }) => {
    const scripts = [], errors = [];
    global.document = { createElement: () => ({}), body: { appendChild: (s) => scripts.push(s.src) } };
    console.error = (format, ...args) => errors.push(String(format).replace(/%s/g, () => String(args.shift())));
    try {
      return { html: lib.renderToStaticMarkup(lib.createElement(lib[component], props)), scripts, errors };
    } catch (e) {
      return { html: "", scripts, errors: [...errors, `threw: ${e.message}`] };
    }
  });
  console.error = log;
  fs.rmSync(dir, { recursive: true, force: true });
  process.stdout.write(JSON.stringify(results));
})();
