/**
 * VOKALIS LOGOPÄDIE – INTERACTIVE JAVASCRIPT
 * Vanilla ES6+ without external runtime dependencies.
 * Optimized for Core Web Vitals, INP, and strict security (XSS prevention).
 */

document.addEventListener('DOMContentLoaded', () => {
  initStickyHeader();
  initMobileNavigation();
  initTherapyFilter();
  initInteractiveAssistant();
  initFaqAccordion();
  initContactForm();
  initServiceWorker();
});

/**
 * Register lightweight offline service worker
 */
function initServiceWorker() {
  if ('serviceWorker' in navigator && window.location.protocol.startsWith('http')) {
    window.addEventListener('load', () => {
      navigator.serviceWorker.register('./sw.js')
        .catch(() => {
          // Graceful fallback if SW unsupported or registration blocked
        });
    });
  }
}


/**
 * Sanitize strings to prevent XSS
 */
function escapeHtml(str) {
  if (!str) return '';
  return String(str)
    .replace(/&/g, '&amp;')
    .replace(/</g, '&lt;')
    .replace(/>/g, '&gt;')
    .replace(/"/g, '&quot;')
    .replace(/'/g, '&#039;');
}

/* --------------------------------------------------------------------------
   1. Sticky Header with Throttled / Passive Scroll Detection
   -------------------------------------------------------------------------- */
function initStickyHeader() {
  const header = document.querySelector('.header');
  if (!header) return;

  let ticking = false;
  const onScroll = () => {
    if (!ticking) {
      window.requestAnimationFrame(() => {
        if (window.scrollY > 20) {
          header.classList.add('scrolled');
        } else {
          header.classList.remove('scrolled');
        }
        ticking = false;
      });
      ticking = true;
    }
  };

  window.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
}

/* --------------------------------------------------------------------------
   2. Mobile Drawer Navigation & Focus Trap
   -------------------------------------------------------------------------- */
function initMobileNavigation() {
  const toggle = document.querySelector('.mobile-toggle');
  const drawer = document.querySelector('.mobile-drawer');
  const overlay = document.querySelector('.mobile-overlay');
  const navLinks = document.querySelectorAll('.mobile-nav-link');

  if (!toggle || !drawer || !overlay) return;

  function openMenu() {
    toggle.classList.add('active');
    toggle.setAttribute('aria-expanded', 'true');
    drawer.classList.add('open');
    overlay.classList.add('active');
    document.body.style.overflow = 'hidden';
  }

  function closeMenu() {
    toggle.classList.remove('active');
    toggle.setAttribute('aria-expanded', 'false');
    drawer.classList.remove('open');
    overlay.classList.remove('active');
    document.body.style.overflow = '';
  }

  toggle.addEventListener('click', () => {
    const isOpen = drawer.classList.contains('open');
    isOpen ? closeMenu() : openMenu();
  });

  overlay.addEventListener('click', closeMenu);

  navLinks.forEach((link) => {
    link.addEventListener('click', closeMenu);
  });

  document.addEventListener('keydown', (e) => {
    if (e.key === 'Escape' && drawer.classList.contains('open')) {
      closeMenu();
      toggle.focus();
    }
  });
}

/* --------------------------------------------------------------------------
   3. Therapy Specialties Category Filter
   -------------------------------------------------------------------------- */
function initTherapyFilter() {
  const filterButtons = document.querySelectorAll('.filter-btn');
  const therapyCards = document.querySelectorAll('.therapy-card');

  if (!filterButtons.length || !therapyCards.length) return;

  filterButtons.forEach((btn) => {
    btn.addEventListener('click', () => {
      filterButtons.forEach((b) => {
        b.classList.remove('active');
        b.setAttribute('aria-selected', 'false');
      });
      btn.classList.add('active');
      btn.setAttribute('aria-selected', 'true');

      const filterValue = btn.getAttribute('data-filter');

      therapyCards.forEach((card) => {
        const cardCategory = card.getAttribute('data-category');
        if (filterValue === 'all' || cardCategory === filterValue) {
          card.style.display = 'flex';
        } else {
          card.style.display = 'none';
        }
      });
    });
  });
}

/* --------------------------------------------------------------------------
   4. Interactive Inquiry Assistant (Termin- & Bedarfsassistent)
   -------------------------------------------------------------------------- */
function initInteractiveAssistant() {
  const steps = document.querySelectorAll('.assistant-step');
  const indicators = document.querySelectorAll('.step-indicator');
  const nextBtns = document.querySelectorAll('.btn-step-next');
  const prevBtns = document.querySelectorAll('.btn-step-prev');
  const optionCards = document.querySelectorAll('.option-card');

  let currentStep = 1;
  const formData = {
    patientType: '',
    symptomArea: '',
    prescriptionStatus: ''
  };

  // Option selection
  optionCards.forEach((card) => {
    card.addEventListener('click', () => {
      const step = card.closest('.assistant-step');
      const stepIndex = parseInt(step.getAttribute('data-step'), 10);
      const value = card.getAttribute('data-value');

      // Clear previous selection in this step
      step.querySelectorAll('.option-card').forEach((c) => c.classList.remove('selected'));
      card.classList.add('selected');

      if (stepIndex === 1) formData.patientType = value;
      if (stepIndex === 2) formData.symptomArea = value;
      if (stepIndex === 3) formData.prescriptionStatus = value;

      // Enable next button for current step
      const nextBtn = step.querySelector('.btn-step-next');
      if (nextBtn) {
        nextBtn.removeAttribute('disabled');
      }
    });
  });

  function updateStepView(targetStep) {
    steps.forEach((s) => s.classList.remove('active'));
    indicators.forEach((ind) => {
      const indStep = parseInt(ind.getAttribute('data-step'), 10);
      ind.classList.remove('active', 'completed');
      if (indStep === targetStep) ind.classList.add('active');
      if (indStep < targetStep) ind.classList.add('completed');
    });

    const activeStepElem = document.querySelector(`.assistant-step[data-step="${targetStep}"]`);
    if (activeStepElem) {
      activeStepElem.classList.add('active');
    }

    // On final summary step (Step 4), update summary values safely
    if (targetStep === 4) {
      const summaryElem = document.getElementById('assistant-summary-text');
      const subjectInput = document.getElementById('contact-subject');
      const messageInput = document.getElementById('contact-message');

      const safePatient = escapeHtml(formData.patientType || 'Nicht angegeben');
      const safeSymptom = escapeHtml(formData.symptomArea || 'Allgemeine Anfrage');
      const safePrescription = escapeHtml(formData.prescriptionStatus || 'Offen');

      if (summaryElem) {
        summaryElem.innerHTML = `
          <strong>Patient:</strong> ${safePatient} &bull; 
          <strong>Bereich:</strong> ${safeSymptom} &bull; 
          <strong>Ärztliche Verordnung:</strong> ${safePrescription}
        `;
      }

      if (subjectInput) {
        subjectInput.value = `Therapieanfrage: ${formData.patientType || ''} (${formData.symptomArea || ''})`;
      }
      if (messageInput && !messageInput.value) {
        messageInput.value = `Hallo Vokalis-Team,\n\nich interessiere mich für eine logopädische Behandlung für: ${formData.patientType || ''}.\nBereich: ${formData.symptomArea || ''}\nRezeptstatus: ${formData.prescriptionStatus || ''}.\n\nBitte nehmen Sie bezüglich eines Erstgesprächs Kontakt mit mir auf.`;
      }
    }
  }

  nextBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      if (currentStep < 4) {
        currentStep++;
        updateStepView(currentStep);
      }
    });
  });

  prevBtns.forEach((btn) => {
    btn.addEventListener('click', () => {
      if (currentStep > 1) {
        currentStep--;
        updateStepView(currentStep);
      }
    });
  });
}

/* --------------------------------------------------------------------------
   5. FAQ Accordion Logic
   -------------------------------------------------------------------------- */
function initFaqAccordion() {
  const faqItems = document.querySelectorAll('.faq-item');

  faqItems.forEach((item) => {
    const questionBtn = item.querySelector('.faq-question');
    if (!questionBtn) return;

    questionBtn.addEventListener('click', () => {
      const isActive = item.classList.contains('active');

      // Close all other items for a clean single-open accordion experience
      faqItems.forEach((other) => {
        if (other !== item) {
          other.classList.remove('active');
          const btn = other.querySelector('.faq-question');
          if (btn) btn.setAttribute('aria-expanded', 'false');
        }
      });

      if (isActive) {
        item.classList.remove('active');
        questionBtn.setAttribute('aria-expanded', 'false');
      } else {
        item.classList.add('active');
        questionBtn.setAttribute('aria-expanded', 'true');
      }
    });
  });
}

/* --------------------------------------------------------------------------
   6. Contact Form Client-side Validation & Feedback
   -------------------------------------------------------------------------- */
function initContactForm() {
  const form = document.getElementById('contact-form');
  if (!form) return;

  form.addEventListener('submit', (e) => {
    e.preventDefault();

    const name = form.querySelector('#contact-name')?.value.trim();
    const email = form.querySelector('#contact-email')?.value.trim();
    const privacy = form.querySelector('#contact-privacy')?.checked;

    if (!name || !email || !privacy) {
      alert('Bitte füllen Sie alle erforderlichen Felder aus und akzeptieren Sie die Datenschutzhinweise.');
      return;
    }

    const submitBtn = form.querySelector('button[type="submit"]');
    submitBtn.innerHTML = `
      <svg style="width:18px;height:18px;animation:spin 1s linear infinite;margin-right:8px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2">
        <circle cx="12" cy="12" r="10" stroke-opacity="0.25"/>
        <path d="M12 2a10 10 0 0 1 10 10" />
      </svg>
      Wird übermittelt...
    `;
    submitBtn.disabled = true;

    // Simulate dispatch feedback
    setTimeout(() => {
      form.innerHTML = `
        <div style="text-align: center; padding: 2.5rem 1rem;">
          <div style="width: 60px; height: 60px; background-color: var(--success-subtle); color: var(--success); border-radius: 50%; display: inline-flex; align-items: center; justify-content: center; margin-bottom: 1.5rem;">
            <svg style="width: 32px; height: 32px;" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5">
              <path stroke-linecap="round" stroke-linejoin="round" d="M5 13l4 4L19 7" />
            </svg>
          </div>
          <h3 style="font-size: 1.5rem; font-weight: 800; color: var(--secondary); margin-bottom: 0.75rem;">Vielen Dank für Ihre Anfrage!</h3>
          <p style="color: var(--text-secondary); max-width: 480px; margin: 0 auto 1.5rem; line-height: 1.6;">
            Wir haben Ihre Nachricht erhalten und werden uns zeitnah mit Ihnen für eine Terminabsprache in Verbindung setzen.
          </p>
          <button type="button" class="btn btn-outline btn-sm" onclick="location.reload()">Weitere Anfrage senden</button>
        </div>
      `;
    }, 800);
  });
}
