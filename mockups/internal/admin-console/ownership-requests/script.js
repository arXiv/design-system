// ── Auto-detect name matches and pre-set decisions ───────────
// If the requestor's name appears in the author list (marked with
// <mark class="requestor">), auto-set the decision to "Author".
document.querySelectorAll('.papers-table tbody tr').forEach(row => {
  const hasMatch = row.querySelector('mark.requestor') !== null;
  row.dataset.nameMatch = hasMatch ? 'yes' : 'no';

  // Auto-set to Author if name match and no decision yet
  if (hasMatch && !row.dataset.decision) {
    const authorBtn = row.querySelector('.ds-seg-btn.seg-author');
    if (authorBtn) {
      authorBtn.classList.add('active');
      row.dataset.decision = 'author';
    }
  }
});

// ── Segmented decision control ────────────────────────────────
// Clicking a segment button marks it active, clears siblings,
// and updates data-decision on the parent <tr> for row highlighting.
document.querySelectorAll('.decision-group .ds-seg-btn').forEach(btn => {
  btn.addEventListener('click', function () {
    const group = this.closest('.decision-group');
    const row   = this.closest('tr');

    // Clear active from all buttons in this group
    group.querySelectorAll('.ds-seg-btn').forEach(b => b.classList.remove('active'));

    // Mark this button active
    this.classList.add('active');

    // Update row highlight
    if (row) row.dataset.decision = this.dataset.value;
  });
});

// ── Reject All ───────────────────────────────────────────────
// Sets "No" on every undecided row (no active button yet).
document.getElementById('btn-reject-all').addEventListener('click', function () {
  document.querySelectorAll('.papers-table tbody tr').forEach(row => {
    if (!row.dataset.decision) {
      const noBtn = row.querySelector('.ds-seg-btn.seg-no');
      if (noBtn) {
        row.querySelectorAll('.ds-seg-btn').forEach(b => b.classList.remove('active'));
        noBtn.classList.add('active');
        row.dataset.decision = 'no';
      }
    }
  });
});

// ── Name match filter ────────────────────────────────────────
const matchFilter = document.getElementById('match-filter');
const paperRows   = document.querySelectorAll('.papers-table tbody tr');

function applyMatchFilter() {
  const val = matchFilter.value;
  paperRows.forEach(row => {
    if (val === 'all') {
      row.classList.remove('filter-hidden');
    } else {
      row.classList.toggle('filter-hidden', row.dataset.nameMatch !== val);
    }
  });
}

matchFilter.addEventListener('change', applyMatchFilter);
