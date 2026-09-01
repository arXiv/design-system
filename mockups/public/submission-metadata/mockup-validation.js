/* ============================================================================
   arXiv submission — form validation behavior
   Mockup script. Demonstrates the interaction model; not production code.

   Three things live here, and only the first two need to be built:

     1. renderState()  — how a validation result becomes visible markup.
                         Server-rendered today. This function is the reference
                         for what the Jinja template must produce.
     2. Process / Continue gating and the in-progress state.
     3. The scenario switcher, which is mockup scaffolding. Delete it.

   The submission system validates on the server, so nothing here runs on
   keystroke or blur. When client-side validation arrives, the same
   renderState() shape applies — only the trigger changes.
   ========================================================================= */
(function () {
  'use strict';

  /* --- Scenario data -------------------------------------------------------
     Each entry is a validation result for one field:
       tier    'error'   cannot proceed
               'warning' can proceed, submission may be held for review
               'info'    value was changed automatically; review it
       text    the message. Written per docs/STYLE.md: no contractions,
               says what is wrong and what to do about it.
       highlight optional. The offending substring. The message quotes it,
               the field marks it, and a "Show me" control selects it.
               NEVER echo the whole field value — see section 7 of the CSS.
       normalize optional, info only. Applies the transformation the info
               message is reporting, so the field actually shows the corrected
               value. An info message saying "extra spaces were removed" beside
               a field still full of extra spaces is worse than none at all.
     ---------------------------------------------------------------------- */
  /* Real violations of the abstract rules on info.arxiv.org/help/prep, several
     at a time in one field. That is the case that stresses the design: the
     alert has to stay readable when three of its rows name the same field, and
     the field has to show four messages without the form losing its shape. */
  var SCENARIOS = {
    unprocessed: {
      label: 'Not yet processed',
      fields: {}
    },

    errors: {
      label: 'Blocking errors',
      fields: {
        authors_display: {
          tier: 'error',
          text: 'The author list could not be parsed. Use "GivenName FamilyName" ' +
                'or "I. FamilyName", and separate authors with a comma.'
        },
        abstract: [
          {
            tier: 'error',
            text: 'Do not begin the abstract with the word "Abstract". Remove',
            highlight: 'Abstract: '
          },
          {
            tier: 'error',
            text: 'The abstract contains HTML markup, which is not permitted. Remove',
            highlight: '<br>'
          }
        ],
        /* The title is tidied on every run. Automatic corrections are
           applied during processing regardless of what else failed, so
           this info message belongs in every processed state, not only
           the clean ones. */
        title: {
          tier: 'info',
          normalize: true,
          text: 'Extra spaces were removed from your title. Please confirm it reads correctly.'
        }
      }
    },

    mixed: {
      label: 'Errors and warnings',
      fields: {
        abstract: [
          {
            tier: 'error',
            text: 'Do not begin the abstract with the word "Abstract". Remove',
            highlight: 'Abstract: '
          },
          {
            tier: 'error',
            text: 'The abstract contains HTML markup, which is not permitted. Remove',
            highlight: '<br>'
          },
          {
            tier: 'warning',
            text: 'Font commands are not processed and will appear literally in the ' +
                  'announcement. Remove',
            highlight: '\\em '
          },
          {
            tier: 'warning',
            text: 'Add a space between a URL and the punctuation that follows it, ' +
                  'or the full stop becomes part of the link:',
            highlight: 'https://example.org/heavy-tail-sgd.'
          }
        ],
        acm_class: {
          tier: 'warning',
          text: 'This does not look like an ACM classification code. The expected ' +
                'form is F.2.2 or I.2.7. Check',
          highlight: 's 25'
        },
        title: {
          tier: 'info',
          normalize: true,
          text: 'Extra spaces were removed from your title. Please confirm it reads correctly.'
        }
      }
    },

    warnings: {
      label: 'Warnings only',
      fields: {
        abstract: [
          {
            tier: 'warning',
            text: 'Font commands are not processed and will appear literally in the ' +
                  'announcement. Remove',
            highlight: '\\em '
          },
          {
            tier: 'warning',
            text: 'Add a space between a URL and the punctuation that follows it, ' +
                  'or the full stop becomes part of the link:',
            highlight: 'https://example.org/heavy-tail-sgd.'
          }
        ],
        acm_class: {
          tier: 'warning',
          text: 'This does not look like an ACM classification code. The expected ' +
                'form is F.2.2 or I.2.7. Check',
          highlight: 's 25'
        },
        title: {
          tier: 'info',
          normalize: true,
          text: 'Extra spaces were removed from your title. Please confirm it reads correctly.'
        }
      }
    },

    clean: {
      label: 'All clear',
      fields: {
        title: {
          tier: 'info',
          normalize: true,
          text: 'Extra spaces were removed from your title. Please confirm it reads correctly.'
        }
      }
    }
  };

  /* Field label text, used to build the summary links. */
  var FIELD_LABELS = {
    title:           'Title',
    authors_display: 'Authors',
    abstract:        'Abstract',
    comments:        'Comments',
    doi:             'DOI',
    journal_ref:     'Journal reference',
    report_num:      'Report number',
    acm_class:       'ACM classification',
    msc_class:       'MSC classification'
  };

  var SUMMARY_ICON = { error: '✕', warning: '⚠', info: '↻', success: '✓' };

  function all(sel) {
    return Array.prototype.slice.call(document.querySelectorAll(sel));
  }

  var summaryEl       = document.getElementById('form-summary');
  /* Two of each: the sidebar repeats its controls top and bottom, so every
     control is a set. Nothing here may assume a single element. */
  var processBtns   = all('[data-process]');
  var continueBtns  = all('[data-continue]');

  /* One reason, for every unavailable state. Deliberately generic: on a form
     nobody has filled in yet there is no way to know whether there WILL be
     errors, so the message must not claim there are any. */
  var CONTINUE_REASON = 'Process and resolve any errors before continuing';

  /* There is no separate status line any more. The alerts are the result, and
     a second running commentary beside the button only repeated them. */

  var reduceMotion = window.matchMedia('(prefers-reduced-motion: reduce)');

  /* The values as submitted. Processing rewrites info-tier fields, so
     these are kept in order to restore the "not yet processed" state. Captured
     once at load: this is scaffolding for the scenario switcher, not something
     the real page needs. */
  var ORIGINAL = {};
  Object.keys(FIELD_LABELS).forEach(function (name) {
    var el = document.getElementById(name);
    if (el) ORIGINAL[name] = el.value;
  });

  /* ---------------------------------------------------------------------
     Clearing. Every render starts from a clean slate so that states cannot
     accumulate — the commonest bug in hand-rolled validation display.
     --------------------------------------------------------------------- */
  function clearAll() {
    Object.keys(FIELD_LABELS).forEach(function (name) {
      var input = document.getElementById(name);
      if (!input) return;
      input.classList.remove('is-invalid', 'is-warning', 'is-info', 'is-empty-required');
      input.removeAttribute('aria-invalid');
      input.removeAttribute('aria-describedby');

      if (ORIGINAL[name] !== undefined) input.value = ORIGINAL[name];

      var msg = document.getElementById(name + '-msg');
      if (msg) msg.parentNode.removeChild(msg);

      var wrap = input.closest('.field-highlight');
      if (wrap) unwrapHighlight(wrap, input);
    });
    summaryEl.hidden = true;
    summaryEl.innerHTML = '';
  }

  /* ---------------------------------------------------------------------
     One field's message.

     The message element carries an id and the input points at it with
     aria-describedby, so the message is read out when the field receives
     focus. Without that wiring a screen reader user hears the label and
     nothing else, and the entire validation display is invisible to them.
     --------------------------------------------------------------------- */
  /* A field may carry several problems at once, at different tiers. The data is
     either one result object or an array of them; everything below works on the
     array. */
  function listOf(v) { return Array.isArray(v) ? v : [v]; }

  var TIER_RANK = { info: 0, warning: 1, error: 2 };
  function worstTier(results) {
    return results.reduce(function (acc, r) {
      return TIER_RANK[r.tier] > TIER_RANK[acc] ? r.tier : acc;
    }, 'info');
  }

  var TIER_PREFIX = {
    error:   'Error: ',
    warning: 'Warning: ',
    info:    'Changed automatically: '
  };

  function renderField(name, value) {
    var input = document.getElementById(name);
    if (!input) return;
    var results = listOf(value);

    /* Apply whatever the info messages report, before anything reads the value.
       The author sees the corrected text and a message saying what changed —
       which is the whole point of the tier. */
    results.forEach(function (rr) {
      if (rr.normalize) input.value = input.value.replace(/\s+/g, ' ').trim();
    });

    /* The control shows the worst tier present. A field with an error and a
       warning is a field you cannot proceed past, so it reads as an error. */
    var worst = worstTier(results);
    if (worst === 'error')        input.classList.add('is-invalid');
    else if (worst === 'warning') input.classList.add('is-warning');
    else if (worst === 'info')    input.classList.add('is-info');
    if (worst === 'error') input.setAttribute('aria-invalid', 'true');

    /* One problem renders as a paragraph. Several render as a list — numbered,
       because "the second one" has to be sayable when someone is working
       through them, and because a run of loose paragraphs under one field stops
       looking like a set of separate problems. */
    var container;
    if (results.length === 1) {
      container = buildMessage(input, results[0], 'p');
    } else {
      container = document.createElement('ol');
      container.className = 'field-messages';
      results.forEach(function (r) {
        container.appendChild(buildMessage(input, r, 'li'));
      });
    }
    container.id = name + '-msg';

    input.parentNode.insertBefore(container, input.nextSibling);
    input.setAttribute('aria-describedby', container.id);

    /* Every highlight in one pass: the backdrop is painted once with all the
       matches, each marked at its own tier. */
    var marks = results.filter(function (r) { return r.highlight; })
                       .map(function (r) { return { needle: r.highlight, tier: r.tier }; });
    if (marks.length) applyHighlights(input, marks);
  }

  function buildMessage(input, result, tag) {
    var el = document.createElement(tag);
    el.className = 'field-' + result.tier;

    /* The tier is otherwise carried only by color and a decorative glyph, so it
       is also stated in text for a screen reader. */
    var sr = document.createElement('span');
    sr.className = 'is-sr-only';
    sr.textContent = TIER_PREFIX[result.tier];
    el.appendChild(sr);
    el.appendChild(document.createTextNode(result.text));

    if (result.highlight) {
      var count = occurrences(input.value, result.highlight);
      el.appendChild(document.createTextNode(' '));
      var code = document.createElement('code');
      code.className = 'field-match';
      /* Matched with its surrounding whitespace, shown without it. "Abstract: "
         has to include the trailing space to be the string we mean, but a chip
         with a hanging space reads as a typo. */
      code.textContent = result.highlight.trim();
      el.appendChild(code);
      /* No full stop after the chip. Half these matches already end in
         punctuation, and "Remove <code>Abstract:</code>." reads as a mistake. */
      if (count > 1) {
        el.appendChild(document.createTextNode(' (' + count + ' instances)'));
      }
      el.appendChild(document.createTextNode(' '));
      var locate = document.createElement('button');
      locate.type = 'button';
      locate.className = 'field-locate';
      locate.textContent = count > 1 ? 'Show me each one' : 'Show me';
      locate.addEventListener('click', function () {
        selectNextMatch(input, result.highlight);
      });
      el.appendChild(locate);
    }
    return el;
  }

  function occurrences(hay, needle) {
    var n = 0, i = hay.indexOf(needle);
    while (i !== -1) { n++; i = hay.indexOf(needle, i + needle.length); }
    return n;
  }

  /* "Show me" — select the next match and scroll the field to it. This is what
     makes the pattern work on a long abstract: the user does not have to hunt.
     It serves keyboard users too, since it moves the caret rather than just
     moving the viewport. Cycles, so repeated presses walk every instance. */
  var locateCursor = {};
  function selectNextMatch(input, needle) {
    var key = input.id + '::' + needle;
    var from = locateCursor[key] || 0;
    var at = input.value.indexOf(needle, from);
    if (at === -1) at = input.value.indexOf(needle);
    if (at === -1) return;
    locateCursor[key] = at + needle.length;
    input.focus();
    input.setSelectionRange(at, at + needle.length);
    if (input.tagName === 'TEXTAREA') syncBackdrop(input);
  }

  /* Paint marks behind the control. Works for input and textarea alike; the
     backdrop mirrors the control's wrapping and scroll position.

     All matches are laid down in one pass over the value, so overlapping or
     adjacent problems cannot double-wrap the same characters. Each mark carries
     its own tier, because a field can hold an error and a warning at once and
     the two must not look the same. */
  function applyHighlights(input, marks) {
    var value = input.value;

    /* Locate every occurrence of every needle, then sort by position. */
    var hits = [];
    marks.forEach(function (m) {
      var i = value.indexOf(m.needle);
      while (i !== -1) {
        hits.push({ start: i, end: i + m.needle.length, tier: m.tier });
        i = value.indexOf(m.needle, i + m.needle.length);
      }
    });
    if (!hits.length) return;
    hits.sort(function (a, b) { return a.start - b.start; });

    var wrap = document.createElement('div');
    wrap.className = 'field-highlight';
    input.parentNode.insertBefore(wrap, input);
    wrap.appendChild(input);

    var backdrop = document.createElement('div');
    backdrop.className = 'field-highlight-backdrop';
    if (input.tagName === 'INPUT') backdrop.classList.add('is-single-line');
    backdrop.setAttribute('aria-hidden', 'true');

    /* Built with text nodes, never innerHTML: the value is author input, and
       this is a page whose whole job is rejecting HTML in author input. */
    var cursor = 0;
    hits.forEach(function (h) {
      if (h.start < cursor) return;          /* overlaps one already painted */
      backdrop.appendChild(document.createTextNode(value.slice(cursor, h.start)));
      var mark = document.createElement('mark');
      mark.className = 'mark-' + h.tier;
      mark.textContent = value.slice(h.start, h.end);
      backdrop.appendChild(mark);
      cursor = h.end;
    });
    backdrop.appendChild(document.createTextNode(value.slice(cursor)));
    wrap.insertBefore(backdrop, input);

    input.addEventListener('scroll', function () { syncBackdrop(input); });

    /* Offsets go stale the moment the user types, so the marks are dropped on
       first edit rather than left pointing at the wrong characters. The
       messages stay: they still name what to look for. */
    input.addEventListener('input', function onEdit() {
      input.removeEventListener('input', onEdit);
      backdrop.remove();
    });
  }

  function syncBackdrop(input) {
    var wrap = input.closest('.field-highlight');
    var backdrop = wrap && wrap.querySelector('.field-highlight-backdrop');
    if (!backdrop) return;
    backdrop.scrollTop = input.scrollTop;
    backdrop.scrollLeft = input.scrollLeft;
  }

  function unwrapHighlight(wrap, input) {
    wrap.parentNode.insertBefore(input, wrap);
    wrap.parentNode.removeChild(wrap);
  }

  /* ---------------------------------------------------------------------
     Page-level summary — one alert per severity, never a mixed one.

     Errors and warnings do not share a box. Red has to mean "you cannot
     proceed"; the moment a non-blocking item appears inside a red alert, red
     stops meaning that and the user has to read every line to find out which
     kind each one is. Separate alerts also let each carry a heading that says
     what it is, instead of a heading that has to hedge across both.

     Order is severity: blocking errors, then warnings, then the record of what
     was changed automatically. All three are optional and any combination can
     appear.

     Every count and every list is derived from the field results, so a summary
     cannot disagree with the fields it describes.
     --------------------------------------------------------------------- */
  function plural(n, one, many) { return n === 1 ? one : many; }

  function buildAlert(tier, title, body, problems) {
    var box = document.createElement('div');
    box.className = 'form-summary form-summary-' + tier;

    var icon = document.createElement('span');
    icon.className = 'form-summary-icon';
    icon.setAttribute('aria-hidden', 'true');
    icon.textContent = SUMMARY_ICON[tier];

    var content = document.createElement('div');
    content.className = 'form-summary-content';

    var h = document.createElement('p');
    h.className = 'form-summary-title';
    h.textContent = title;
    content.appendChild(h);

    var p = document.createElement('p');
    p.textContent = body;
    content.appendChild(p);

    if (problems && problems.length) {
      /* Ordered, not unordered. The heading states a count — "3 blocking
         errors" — so numbering lets the reader check the list against it and
         keep track of which ones are done. It also disambiguates rows that
         name the same field, which happens whenever one field has several
         problems. The rows are in form order, top to bottom, so an ordered
         list is honest about the sequence too. */
      var ul = document.createElement('ol');
      problems.forEach(function (pr) {
        var name = pr.name;
        var li = document.createElement('li');
        var a = document.createElement('a');
        a.href = '#' + name;
        /* Field name on every row, even when a field contributes several rows.
           Repeating "Abstract" three times is not noise: without it the reader
           cannot tell whether three problems are in one field or three. */
        a.appendChild(document.createTextNode(FIELD_LABELS[name] + ' — ' + pr.text));
        /* The row carries the match too. Without it a message written to lead
           into one ("… Remove") ends mid-sentence in the summary. */
        if (pr.highlight) {
          a.appendChild(document.createTextNode(' '));
          var chip = document.createElement('code');
          chip.className = 'field-match';
          chip.textContent = pr.highlight.trim();
          a.appendChild(chip);
        }
        a.addEventListener('click', function (e) {
          e.preventDefault();
          var target = document.getElementById(name);
          if (!target) return;
          target.focus();
          target.scrollIntoView({
            block: 'center',
            /* prefers-reduced-motion must be checked in JS: scrollIntoView
               ignores the CSS media query entirely. */
            behavior: reduceMotion.matches ? 'auto' : 'smooth'
          });
        });
        li.appendChild(a);
        ul.appendChild(li);
      });
      content.appendChild(ul);
    }

    box.appendChild(icon);
    box.appendChild(content);
    return box;
  }

  function renderSummary(scenario, processed) {
    /* Flatten to one row per problem, not per field. */
    var problems = [];
    Object.keys(scenario.fields).forEach(function (name) {
      listOf(scenario.fields[name]).forEach(function (r) {
        problems.push({ name: name, tier: r.tier, text: r.text,
                        highlight: r.highlight });
      });
    });
    var by = function (t) {
      return problems.filter(function (pr) { return pr.tier === t; });
    };
    var errors = by('error'), warnings = by('warning'), infos = by('info');

    if (!processed) return;
    summaryEl.hidden = false;

    /* The heading is the count. "2 blocking errors" answers "how bad is this?"
       in two words, which is the question someone scanning actually has — and
       it keeps all three headings parallel: count, then what they are.

       The body says what the tier MEANS, once, rather than restating the count
       in a longer sentence. */
    if (errors.length) {
      summaryEl.appendChild(buildAlert('error',
        errors.length + plural(errors.length, ' blocking error', ' blocking errors'),
        'Blocking errors must be corrected before you can continue. ' +
        'Click on an item to jump to that field.',
        errors));
    }

    if (warnings.length) {
      summaryEl.appendChild(buildAlert('warning',
        warnings.length + plural(warnings.length, ' warning', ' warnings'),
        'You may continue with warnings, but your submission may experience ' +
        'delays in announcement. Click on an item to jump to that field.',
        warnings));
    }

    /* The verdict precedes the supporting detail: when nothing is blocking,
       "can I proceed?" is the question the user actually has. Automatic changes
       are reported after it, and always reported — never folded into the green
       alert, which would read as "no action needed" for something the author is
       being explicitly asked to check. */
    if (!errors.length && !warnings.length) {
      summaryEl.appendChild(buildAlert('success', 'No problems found',
        'Select Continue to move on to the final preview.', null));
    }

    /* "Automatic changes", not "Informational": the other two headings name
       what the items ARE, not which tier they belong to. Naming the tier would
       make this the odd one out and would tell the reader less. */
    if (infos.length) {
      summaryEl.appendChild(buildAlert('info',
        infos.length + plural(infos.length, ' automatic change', ' automatic changes'),
        'arXiv corrected these for you. Please check that they read correctly. ' +
        'Click on an item to jump to that field.',
        infos));
    }
  }

  /* ---------------------------------------------------------------------
     Continue gating.
     --------------------------------------------------------------------- */
  function setContinue(enabled) {
    /* Exactly one primary on screen, and it is always the next step. Once
       Continue is available, Process steps back to secondary — it is still
       there, still usable, just no longer the thing to do.

       Process is never disabled. The clean result only describes the values
       that were submitted, and every field is still editable, so someone who
       fixes a typo afterwards has to be able to re-run the check. Disabling it
       would answer "does editing invalidate the result?" by assuming the form
       cannot change, which is not true. */
    processBtns.forEach(function (b) {
      b.classList.toggle('ds-btn-primary', !enabled);
      b.classList.toggle('ds-btn-secondary', enabled);
    });

    continueBtns.forEach(function (btn) {
      btn.setAttribute('aria-disabled', enabled ? 'false' : 'true');
      var host = btn.closest('.ds-tooltip-host');
      if (!host) return;
      /* The visible tooltip and the screen-reader description are written from
         the same string, so the two can never disagree. */
      var text = enabled ? '' : CONTINUE_REASON;
      host.querySelector('.ds-tooltip-body').textContent = text;
      host.querySelector('[data-continue-reason]').textContent = text;
      if (enabled) hideTip(host);
    });
  }

  /* ---------------------------------------------------------------------
     Tooltip. Shows on hover and on focus — a keyboard user has no hover, so
     focus has to be a trigger or the explanation is mouse-only.
     --------------------------------------------------------------------- */
  function tipEligible(host) {
    var btn = host.querySelector('[data-continue]');
    return btn && btn.getAttribute('aria-disabled') === 'true';
  }
  function showTip(host) {
    if (!tipEligible(host) || host.dataset.dismissed === 'true') return;
    host.querySelector('[data-continue-tip]').hidden = false;
  }
  function hideTip(host) {
    var tip = host.querySelector('[data-continue-tip]');
    if (tip) tip.hidden = true;
  }

  all('.ds-tooltip-host').forEach(function (host) {
    var btn = host.querySelector('[data-continue]');

    host.addEventListener('mouseenter', function () {
      host.dataset.dismissed = 'false';
      showTip(host);
    });
    host.addEventListener('mouseleave', function () { hideTip(host); });

    btn.addEventListener('focus', function () {
      host.dataset.dismissed = 'false';
      showTip(host);
    });
    btn.addEventListener('blur', function () { hideTip(host); });

    /* Dismissible without moving focus, per WCAG 1.4.13. The dismissed flag
       stops the next mousemove or focus event immediately reopening it. */
    host.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      if (host.querySelector('[data-continue-tip]').hidden) return;
      e.stopPropagation();
      host.dataset.dismissed = 'true';
      hideTip(host);
    });
  });

  continueBtns.forEach(function (btn) {
    btn.addEventListener('click', function (e) {
      if (btn.getAttribute('aria-disabled') !== 'true') return;
      /* aria-disabled does not block activation the way the disabled
         attribute does, so the handler has to. In exchange the button stays
         focusable and can say why it is unavailable. */
      e.preventDefault();
      /* Touch has no hover, so a tap has to surface the same explanation.
         Focus stays put: the tooltip now answers the question in place, and
         moving focus on top of that is motion the user did not ask for. */
      var host = btn.closest('.ds-tooltip-host');
      if (host) { host.dataset.dismissed = 'false'; showTip(host); }
    });
  });

  /* ---------------------------------------------------------------------
     Render a whole state.
     --------------------------------------------------------------------- */
  function renderState(key) {
    var scenario = SCENARIOS[key];
    clearAll();

    Object.keys(scenario.fields).forEach(function (name) {
      renderField(name, scenario.fields[name]);
    });
    renderSummary(scenario, key !== 'unprocessed');

    var tiers = [];
    Object.keys(scenario.fields).forEach(function (n) {
      listOf(scenario.fields[n]).forEach(function (r) { tiers.push(r.tier); });
    });
    var hasError = tiers.indexOf('error') !== -1;

    if (key === 'unprocessed') {
      setContinue(false);
    } else if (hasError) {
      setContinue(false);
    } else if (tiers.indexOf('warning') !== -1) {
      setContinue(true);
    } else {
      setContinue(true);
    }

    document.querySelectorAll('[data-scenario]').forEach(function (b) {
      b.setAttribute('aria-pressed', String(b.dataset.scenario === key));
    });
  }

  /* ---------------------------------------------------------------------
     Process button, with its in-progress state.
     --------------------------------------------------------------------- */
  var pendingScenario = 'errors';

  processBtns.forEach(function (btn) {
    btn.addEventListener('click', function () {
      if (btn.classList.contains('is-processing')) return;

      /* Both Process buttons enter the in-progress state together. Leaving the
         other one live would let a second run start mid-flight. */
      var originals = processBtns.map(function (b) { return b.innerHTML; });
      processBtns.forEach(function (b) {
        b.classList.add('is-processing');
        b.setAttribute('aria-disabled', 'true');
        b.innerHTML = '<span class="spinner" aria-hidden="true"></span>Processing…';
      });

      var result = pendingScenario === 'unprocessed' ? 'errors' : pendingScenario;

      window.setTimeout(function () {
        processBtns.forEach(function (b, i) {
          b.classList.remove('is-processing');
          b.setAttribute('aria-disabled', 'false');
          b.innerHTML = originals[i];
        });
        pendingScenario = result;
        renderState(result);

        /* Focus moves to the summary. Otherwise focus stays on Process and a
           screen reader user is not told that anything happened — and the
           summary is both the answer and the route to every problem in it. */
        summaryEl.focus();
      }, 900);
    });
  });

  /* --- Mockup scaffolding. Delete when porting. --------------------------- */
  document.querySelectorAll('[data-scenario]').forEach(function (btn) {
    btn.addEventListener('click', function () {
      pendingScenario = btn.dataset.scenario;
      renderState(pendingScenario);
    });
  });

  renderState('unprocessed');
  pendingScenario = 'errors';
})();
