// Chromium against the Flask host (app.py). The *.brand.test names resolve to it, so the
// banner's shared dismissal can be tested across two "sites" on one parent domain.
const { defineConfig } = require("@playwright/test");

module.exports = defineConfig({
  testDir: __dirname,
  reporter: [["list"]],
  use: {
    screenshot: "only-on-failure",
    launchOptions: { args: ["--host-resolver-rules=MAP *.brand.test 127.0.0.1"] },
  },
  projects: [{ name: "chromium", use: { browserName: "chromium" } }],
  webServer: {
    command: "python3 app.py",
    cwd: __dirname,
    url: "http://127.0.0.1:5001/jinja",
    env: { PORT: "5001" },
    reuseExistingServer: false,
  },
});
