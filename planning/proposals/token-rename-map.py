# The old-name -> new-name map used for the 2026-09-08 token rename.
# Kept as the record of what became what, for anyone tracing a name that
# no longer exists — in this repo, in the blog theme, or in a consuming repo
# that has not caught up. Not executable policy; the policy is in
# docs/DESIGN-POLICIES.md, "Design tokens".

# Old name -> new name. Longest-first application avoids prefix shadowing.
# Public stylesheet (--arxiv-*) and shared scales.
PUBLIC = {
    # ── text ──
    "--arxiv-repository-brown-on-blue": "--ds-text-on-accent",
    "--arxiv-repository-brown":         "--ds-text",
    "--arxiv-library-grey":             "--ds-text-muted",
    "--arxiv-grey-dis":                 "--ds-text-disabled",
    # ── surfaces ──
    "--arxiv-surface":                  "--ds-surface",
    "--arxiv-warm-wash":                "--ds-canvas",
    "--arxiv-card-grey":                "--ds-surface-muted",
    "--arxiv-header-bar":               "--ds-chrome",
    # ── borders ──
    "--arxiv-border-light":             "--ds-border",
    "--arxiv-grey-ui":                  "--ds-border-strong",
    "--arxiv-pill-border":              "--ds-border-muted",
    # ── links + focus ──
    "--arxiv-link-blue":                "--ds-link",
    "--arxiv-link-hover":               "--ds-link-hover",
    "--arxiv-link-visited":             "--ds-link-visited",
    "--arxiv-focus-ring-dark":          "--ds-focus-ring-on-dark",
    "--arxiv-focus-ring":               "--ds-focus-ring",
    # ── accent (Open Blue on public) ──
    "--arxiv-open-blue-bright":         "--ds-accent-hover",
    "--arxiv-open-blue":                "--ds-accent",
    "--arxiv-archival-blue":            "--ds-accent-strong",
    "--arxiv-active-bg":                "--ds-accent-wash",
    "--arxiv-tint-light":               "--ds-accent-surface",
    "--arxiv-tint-border":              "--ds-accent-border",
    # ── status ──
    "--arxiv-success-bg":     "--ds-success-bg",
    "--arxiv-success-border": "--ds-success-border",
    "--arxiv-success-fg":     "--ds-success-fg",
    "--arxiv-info-bg":        "--ds-info-bg",
    "--arxiv-info-border":    "--ds-info-border",
    "--arxiv-info-fg":        "--ds-info-fg",
    "--arxiv-warning-bg":     "--ds-warning-bg",
    "--arxiv-warning-border": "--ds-warning-border",
    "--arxiv-warning-fg":     "--ds-warning-fg",
    "--arxiv-error-bg":       "--ds-error-bg",
    "--arxiv-error-border":   "--ds-error-border",
    "--arxiv-error-fg":       "--ds-error-fg",
    # ── brand primitive (kept: it is a brand colour, not a role) ──
    "--arxiv-smileybones-yellow": "--ds-brand-smileybones-yellow",
    # ── type ──
    "--arxiv-font-sans":      "--ds-font-sans",
    "--arxiv-font-condensed": "--ds-font-condensed",
    "--arxiv-font-mono":      "--ds-font-mono",
    "--arxiv-font-serif":     "--ds-font-serif",
    # ── scales + layout (already partly --ds-) ──
    "--space-tight":   "--ds-space-tight",
    "--space-block":   "--ds-space-block",
    "--space-section": "--ds-space-section",
    "--space-1":  "--ds-space-1",  "--space-2":  "--ds-space-2",
    "--space-3":  "--ds-space-3",  "--space-4":  "--ds-space-4",
    "--space-6":  "--ds-space-6",  "--space-8":  "--ds-space-8",
    "--space-12": "--ds-space-12",
    "--gap-glyph": "--ds-gap-glyph",
    # ── component-scoped (site header surface tokens) ──
    "--hdr-bg":        "--ds-hdr-bg",
    "--hdr-fg-strong": "--ds-hdr-fg-strong",
    "--hdr-fg":        "--ds-hdr-fg",
    "--hdr-border":    "--ds-hdr-border",
    "--hdr-divider":   "--ds-hdr-divider",
    "--hdr-hover":     "--ds-hdr-hover",
    "--hdr-ring":      "--ds-hdr-ring",
}

# Staff stylesheet: bare names -> the same role vocabulary.
INTERNAL = {
    "--text-on-lime":  "--ds-text-on-accent",
    "--text":          "--ds-text",
    "--grey-dis":      "--ds-text-disabled",
    "--grey-hover-dark":"--ds-text-strong",
    "--grey":          "--ds-text-muted",
    "--surface-header":"--ds-surface-muted",
    "--surface-hover": "--ds-surface-hover",
    "--surface":       "--ds-surface",
    "--canvas":        "--ds-canvas",
    "--border":        "--ds-border",
    "--grey-ui":       "--ds-border-strong",
    "--icon-border":   "--ds-border-strong",
    "--grey-hover-bg": "--ds-surface-hover-strong",
    "--grey-active-bg":"--ds-surface-active",
    "--link-visited":  "--ds-link-visited",
    "--link-hover":    "--ds-link-hover",
    "--link-dis":      "--ds-link-disabled",
    "--link":          "--ds-link",
    "--focus-ring":    "--ds-focus-ring",
    # accent — Access Lime is the staff accent
    "--lime-active":   "--ds-accent-active",
    "--lime-hover":    "--ds-accent-hover",
    "--lime-dis-bg":   "--ds-accent-disabled-bg",
    "--lime-dis-text": "--ds-accent-disabled-fg",
    "--lime":          "--ds-accent",
    "--sec-bg-active": "--ds-accent-wash-active",
    "--sec-bg-hover":  "--ds-accent-wash-hover",
    "--sec-bg":        "--ds-accent-wash",
    "--sec-border-active":"--ds-accent-border-active",
    "--sec-border":    "--ds-accent-border",
    "--sec-dis-bg":    "--ds-disabled-bg",
    "--sec-dis-border":"--ds-disabled-border",
    "--sec-dis-text":  "--ds-disabled-fg",
    # destructive
    "--danger-ghost-active":"--ds-danger-wash-active",
    "--danger-ghost-hover": "--ds-danger-wash-hover",
    "--danger-dis-bg":      "--ds-danger-disabled-bg",
    "--danger-dis-text":    "--ds-danger-disabled-fg",
    "--danger-active":      "--ds-danger-active",
    "--danger-hover":       "--ds-danger-hover",
    "--danger":             "--ds-danger",
    # status
    "--success-bg":"--ds-success-bg","--success-border":"--ds-success-border","--success-fg":"--ds-success-fg",
    "--info-bg":"--ds-info-bg","--info-border":"--ds-info-border","--info-fg":"--ds-info-fg",
    "--warning-bg":"--ds-warning-bg","--warning-border":"--ds-warning-border","--warning-fg":"--ds-warning-fg",
    "--error-bg":"--ds-error-bg","--error-border":"--ds-error-border","--error-fg":"--ds-error-fg",
    # scales
    "--space-1":"--ds-space-1","--space-2":"--ds-space-2","--space-3":"--ds-space-3",
    "--space-4":"--ds-space-4","--space-6":"--ds-space-6","--space-8":"--ds-space-8",
    "--space-12":"--ds-space-12",
}
