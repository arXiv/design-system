// Opt-in modal behavior (shows on every page load; no persistence)
document.addEventListener('DOMContentLoaded', function () {
  const modal = document.getElementById('optin-modal');
  if (!modal) return;
  const closeBtn = document.getElementById('optin-close');
  const agreeBtn = document.getElementById('optin-agree');
  const rejectBtn = document.getElementById('optin-reject');
  const overlay = document.getElementById('optin-overlay');
  const desc = document.getElementById('optin-desc');
  const thanks = document.getElementById('optin-thanks');
  const cookieLink = document.getElementById('cookie-preference-link');
  const doneBtn = document.getElementById('optin-done');
  const legal = document.getElementById('optin-legal');
  const originalDescText = desc ? desc.textContent : '';

  const ACCEPT_MSG = {
    lead: "Thanks for opting in.",
    rest: " The arXiv Research Opt-In cookie has been set — your reading data may now be used to support arXiv research. You can change your choice anytime under Cookie Preference."
  };
  const REJECT_MSG = {
    lead: "Your choice has been saved.",
    rest: " The arXiv Research Opt-In cookie records that you've declined, so your reading data will not be used for research. You can change your choice anytime under Cookie Preference."
  };

  function reset() {
    if (agreeBtn) {
      agreeBtn.disabled = false;
      agreeBtn.style.display = '';
      const spinner = agreeBtn.querySelector('.spinner');
      if (spinner) spinner.style.display = 'none';
    }
    if (rejectBtn) {
      rejectBtn.disabled = false;
      rejectBtn.style.display = '';
    }
    if (desc) {
      desc.textContent = originalDescText;
      desc.hidden = false;
    }
    if (thanks) {
      thanks.hidden = true;
      thanks.textContent = '';
    }
    if (doneBtn) doneBtn.style.display = 'none';
    if (legal) legal.style.display = '';
  }

  function show() {
    reset();
    modal.classList.remove('hidden');
    modal.removeAttribute('aria-hidden');
  }

  function hide() {
    modal.classList.add('hidden');
    modal.setAttribute('aria-hidden', 'true');
  }

  // Show on each load (refresh shows it again)
  show();

  // Re-open from footer link to change choice
  cookieLink && cookieLink.addEventListener('click', function (e) {
    e.preventDefault();
    show();
  });

  // Dismiss handlers
  closeBtn && closeBtn.addEventListener('click', hide);
  document.addEventListener('keydown', function (e) {
    if (e.key === 'Escape' && !modal.classList.contains('hidden')) hide();
  });

  function showConfirmation(message) {
    if (desc) { desc.textContent = ''; desc.hidden = true; }
    if (legal) legal.style.display = 'none';
    if (agreeBtn) agreeBtn.style.display = 'none';
    if (rejectBtn) rejectBtn.style.display = 'none';
    if (thanks) {
      thanks.textContent = '';
      const lead = document.createElement('strong');
      lead.textContent = message.lead;
      thanks.appendChild(lead);
      thanks.appendChild(document.createTextNode(message.rest));
      thanks.hidden = false;
    }
    if (doneBtn) {
      doneBtn.style.display = '';
      doneBtn.focus();
    }
  }

  // Close button shown after confirmation
  doneBtn && doneBtn.addEventListener('click', hide);

  // Reject action: show confirmation
  rejectBtn && rejectBtn.addEventListener('click', function () {
    showConfirmation(REJECT_MSG);
  });

  // Agree action: show spinner + confirmation
  agreeBtn && agreeBtn.addEventListener('click', function () {
    agreeBtn.disabled = true;
    const spinner = agreeBtn.querySelector('.spinner');
    if (spinner) spinner.style.display = 'inline-block';
    if (desc) desc.textContent = 'Processing...';
    setTimeout(function () {
      showConfirmation(ACCEPT_MSG);
    }, 700);
  });
});


