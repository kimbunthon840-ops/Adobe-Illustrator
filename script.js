/* ==========================================================================
   Exam Masterclass Interactive Script
   ========================================================================== */

document.addEventListener('DOMContentLoaded', () => {
  // ==================== 00. DARK / LIGHT THEME CONTROLLER ====================
  const themeToggleBtn = document.getElementById('theme-toggle-btn');
  const themeLabel = themeToggleBtn ? themeToggleBtn.querySelector('.theme-btn-label') : null;

  function applyTheme(theme) {
    document.documentElement.setAttribute('data-theme', theme);
    localStorage.setItem('illustrator_preferred_theme', theme);
    if (themeLabel) {
      themeLabel.textContent = theme === 'dark' ? 'Light' : 'Dark';
    }
    if (themeToggleBtn) {
      themeToggleBtn.setAttribute('title', theme === 'dark' ? 'ប្តូរទៅ Light Mode' : 'ប្តូរទៅ Dark Mode');
    }
  }

  // Detect initial theme
  const savedTheme = localStorage.getItem('illustrator_preferred_theme');
  if (savedTheme) {
    applyTheme(savedTheme);
  } else if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
    applyTheme('dark');
  } else {
    applyTheme('light');
  }

  if (themeToggleBtn) {
    themeToggleBtn.addEventListener('click', () => {
      const currentTheme = document.documentElement.getAttribute('data-theme') || 'light';
      const nextTheme = currentTheme === 'dark' ? 'light' : 'dark';
      applyTheme(nextTheme);
      showToast(nextTheme === 'dark' ? '🌙 Dark Mode Activated' : '☀️ Light Mode Activated');
    });
  }



  // ==================== 0. PROJECT TAB SWITCHER ====================
  const projTabs = document.querySelectorAll('.proj-tab-btn');
  const projectWrappers = document.querySelectorAll('.project-section-wrapper');

  projTabs.forEach(tab => {
    tab.addEventListener('click', (e) => {
      e.preventDefault();
      const targetId = tab.getAttribute('data-target');

      projTabs.forEach(t => t.classList.remove('active'));
      tab.classList.add('active');

      projectWrappers.forEach(wrap => {
        if (wrap.id === targetId) {
          wrap.classList.add('active');
        } else {
          wrap.classList.remove('active');
        }
      });

      window.scrollTo({ top: 0, behavior: 'smooth' });
      if (targetId === 'project-3-wrapper') {
        showToast('📝 Switched to Quiz 3: Theory Assessment');
      } else if (targetId === 'project-2-wrapper') {
        showToast('📂 Switched to Project 2: Business Card');
      } else {
        showToast('🎨 Switched to Project 1: Logo Design');
      }
    });
  });
  const TOTAL_EXAM_SECONDS = 90 * 60; // 5400 seconds
  let remainingSeconds = TOTAL_EXAM_SECONDS;
  let timerInterval = null;
  let isTimerRunning = false;

  const timerDisplay = document.getElementById('timer-display');
  const timerToggleBtn = document.getElementById('timer-toggle');
  const timerResetBtn = document.getElementById('timer-reset');

  function formatTime(totalSec) {
    const hours = Math.floor(totalSec / 3600);
    const minutes = Math.floor((totalSec % 3600) / 60);
    const seconds = totalSec % 60;
    return `${hours.toString().padStart(2, '0')}:${minutes.toString().padStart(2, '0')}:${seconds.toString().padStart(2, '0')}`;
  }

  function updateTimerDisplay() {
    if (timerDisplay) {
      timerDisplay.textContent = formatTime(remainingSeconds);
      if (remainingSeconds <= 600) { // Under 10 mins
        timerDisplay.style.color = '#dc2626';
      } else {
        timerDisplay.style.color = 'inherit';
      }
    }
  }

  function startTimer() {
    if (isTimerRunning) return;
    isTimerRunning = true;
    if (timerToggleBtn) {
      timerToggleBtn.innerHTML = `
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
          <rect x="6" y="4" width="4" height="16"></rect>
          <rect x="14" y="4" width="4" height="16"></rect>
        </svg>
      `;
      timerToggleBtn.setAttribute('title', 'Pause Exam Timer');
    }

    timerInterval = setInterval(() => {
      if (remainingSeconds > 0) {
        remainingSeconds--;
        updateTimerDisplay();
      } else {
        clearInterval(timerInterval);
        isTimerRunning = false;
        showToast('⏰ Time is up! 1 hour 30 minutes completed.');
        if (timerToggleBtn) {
          timerToggleBtn.innerHTML = `<svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>`;
        }
      }
    }, 1000);
  }

  function pauseTimer() {
    isTimerRunning = false;
    clearInterval(timerInterval);
    if (timerToggleBtn) {
      timerToggleBtn.innerHTML = `
        <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
          <polygon points="5 3 19 12 5 21 5 3"></polygon>
        </svg>
      `;
      timerToggleBtn.setAttribute('title', 'Start Exam Timer');
    }
  }

  if (timerToggleBtn) {
    timerToggleBtn.addEventListener('click', () => {
      if (isTimerRunning) {
        pauseTimer();
      } else {
        startTimer();
      }
    });
  }

  if (timerResetBtn) {
    timerResetBtn.addEventListener('click', () => {
      pauseTimer();
      remainingSeconds = TOTAL_EXAM_SECONDS;
      updateTimerDisplay();
      showToast('Timer reset to 01:30:00');
    });
  }

  updateTimerDisplay();


  // ==================== 2. VECTOR LOGO INTERACTIVE MODES ====================
  const svgLogoElement = document.getElementById('ai-logo-svg');
  const btnModeFull = document.getElementById('btn-mode-full');
  const btnModeOutline = document.getElementById('btn-mode-outline');
  const btnModeGuides = document.getElementById('btn-mode-guides');

  if (btnModeFull && svgLogoElement) {
    btnModeFull.addEventListener('click', () => {
      svgLogoElement.classList.remove('show-guides', 'outline-mode');
      updateCtrlButtons(btnModeFull);
      showToast('Artwork Preview Mode Active');
    });
  }

  if (btnModeOutline && svgLogoElement) {
    btnModeOutline.addEventListener('click', () => {
      svgLogoElement.classList.toggle('outline-mode');
      btnModeOutline.classList.toggle('active');
      showToast(svgLogoElement.classList.contains('outline-mode') ? 'Wireframe / Outline Mode (Ctrl+Y)' : 'Outline Mode Off');
    });
  }

  if (btnModeGuides && svgLogoElement) {
    btnModeGuides.addEventListener('click', () => {
      svgLogoElement.classList.toggle('show-guides');
      btnModeGuides.classList.toggle('active');
      showToast(svgLogoElement.classList.contains('show-guides') ? 'Construction Guides Visible' : 'Guides Hidden');
    });
  }

  function updateCtrlButtons(activeBtn) {
    document.querySelectorAll('.ctrl-btn').forEach(b => {
      if (b === activeBtn) b.classList.add('active');
      else if (b.id !== 'btn-mode-outline' && b.id !== 'btn-mode-guides') b.classList.remove('active');
    });
  }


  // ==================== 3. COLOR COPY TO CLIPBOARD ====================
  const copyButtons = document.querySelectorAll('.copy-btn');
  copyButtons.forEach(btn => {
    btn.addEventListener('click', (e) => {
      const code = btn.getAttribute('data-code') || btn.parentElement.textContent.replace('Copy', '').trim();
      navigator.clipboard.writeText(code).then(() => {
        showToast(`Copied "${code}" to clipboard!`);
      }).catch(() => {
        showToast(`Value: ${code}`);
      });
    });
  });


  // ==================== 4. EXAM CHECKLISTS & SCORE TRACKER ====================
  const checklistCards = document.querySelectorAll('.checklist-card');

  checklistCards.forEach((card, cardIdx) => {
    const rows = card.querySelectorAll('.checklist-row');
    const checkboxes = card.querySelectorAll('.checklist-checkbox');
    const fill = card.querySelector('.progress-fill');
    const percentLabel = card.querySelector('.progress-percent');
    const countLabel = card.querySelector('.checked-count');
    const storageKey = `illustrator_exam_checklist_${cardIdx}`;

    function updateCard() {
      let checked = 0;
      checkboxes.forEach(cb => {
        if (cb.checked) {
          checked++;
          cb.closest('.checklist-row').classList.add('checked');
        } else {
          cb.closest('.checklist-row').classList.remove('checked');
        }
      });

      const total = checkboxes.length;
      const pct = total > 0 ? Math.round((checked / total) * 100) : 0;
      if (fill) fill.style.width = `${pct}%`;
      if (percentLabel) percentLabel.textContent = `${pct}% Ready`;
      if (countLabel) countLabel.textContent = `${checked} / ${total} Requirements`;

      const states = Array.from(checkboxes).map(cb => cb.checked);
      localStorage.setItem(storageKey, JSON.stringify(states));
    }

    // Restore
    const saved = localStorage.getItem(storageKey);
    if (saved) {
      try {
        const parsed = JSON.parse(saved);
        checkboxes.forEach((cb, idx) => {
          if (parsed[idx] !== undefined) cb.checked = parsed[idx];
        });
      } catch (e) {
        console.warn('Error reading saved state', e);
      }
    }
    updateCard();

    rows.forEach(r => {
      r.addEventListener('click', (e) => {
        if (e.target.tagName.toLowerCase() !== 'input') {
          const cb = r.querySelector('.checklist-checkbox');
          if (cb) cb.checked = !cb.checked;
        }
        updateCard();
      });
    });
  });


  // ==================== 5. MODAL FOR ORIGINAL EXAM SHEET IMAGE ====================
  const modal = document.getElementById('image-modal');
  const modalImg = document.getElementById('modal-img');
  const modalClose = document.getElementById('modal-close');
  const examImageBoxes = document.querySelectorAll('.exam-image-box');

  examImageBoxes.forEach(box => {
    box.addEventListener('click', () => {
      const img = box.querySelector('img');
      if (img && modal && modalImg) {
        modalImg.src = img.src;
        modal.classList.add('show');
        document.body.style.overflow = 'hidden';
      }
    });
  });

  if (modalClose) {
    modalClose.addEventListener('click', () => {
      modal.classList.remove('show');
      document.body.style.overflow = '';
    });
  }

  if (modal) {
    modal.addEventListener('click', (e) => {
      if (e.target === modal) {
        modal.classList.remove('show');
        document.body.style.overflow = '';
      }
    });
  }


  // ==================== 6. TUTORIAL ACTIVE STEP SCROLL-SPY ====================
  const stepLinks = document.querySelectorAll('.step-nav-link');
  const stepCards = document.querySelectorAll('.step-card');

  window.addEventListener('scroll', () => {
    let currentStep = '';
    stepCards.forEach(card => {
      const cardTop = card.offsetTop - 140;
      if (window.scrollY >= cardTop) {
        currentStep = card.getAttribute('id');
      }
    });

    stepLinks.forEach(link => {
      link.classList.remove('active');
      if (link.getAttribute('href') === `#${currentStep}`) {
        link.classList.add('active');
      }
    });
  });


  // ==================== 7. TOAST NOTIFICATION HELPER ====================
  function showToast(message) {
    let toast = document.getElementById('toast-msg');
    if (!toast) {
      toast = document.createElement('div');
      toast.id = 'toast-msg';
      toast.className = 'toast-msg';
      document.body.appendChild(toast);
    }
    toast.innerHTML = `
      <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="#22c55e" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round">
        <path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path>
        <polyline points="22 4 12 14.01 9 11.01"></polyline>
      </svg>
      <span>${message}</span>
    `;
    toast.classList.add('show');

    clearTimeout(toast._timeout);
    toast._timeout = setTimeout(() => {
      toast.classList.remove('show');
    }, 3000);
  }

  // ==================== 8. INTERACTIVE QUIZ APPLICATION ====================
  const quizCards = document.querySelectorAll('.quiz-card');
  const quizScoreDisplay = document.getElementById('quiz-score-display');
  const quizStatusText = document.getElementById('quiz-status-text');
  const quizResetBtn = document.getElementById('quiz-reset-btn');

  function updateQuizScore() {
    let answered = 0;
    let correct = 0;
    const total = quizCards.length;

    quizCards.forEach(card => {
      if (card.classList.contains('answered-correct')) {
        answered++;
        correct++;
      } else if (card.classList.contains('answered-wrong')) {
        answered++;
      }
    });

    if (quizScoreDisplay) {
      quizScoreDisplay.textContent = `${correct} / ${total}`;
    }
    if (quizStatusText) {
      if (answered === total) {
        if (correct === total) {
          quizStatusText.textContent = '🎉 អបអរសាទរ! អ្នកឆ្លើយត្រូវទាំងអស់ ១០០% (Perfect Score)';
          showToast('🌟 Perfect Score! You got 5/5 on the Quiz!');
        } else {
          quizStatusText.textContent = `អ្នកឆ្លើយបាន ${correct}/${total} ត្រូវ។ អាចចុច Reset ដើម្បីហាត់ម្តងទៀត!`;
        }
      } else {
        quizStatusText.textContent = `បានឆ្លើយ ${answered} នៃ ${total} សំណួរ`;
      }
    }
  }

  quizCards.forEach(card => {
    const optionBtns = card.querySelectorAll('.quiz-option-btn');
    const explanationBox = card.querySelector('.quiz-explanation-box');

    optionBtns.forEach(btn => {
      btn.addEventListener('click', () => {
        if (card.classList.contains('answered-correct') || card.classList.contains('answered-wrong')) {
          return; // Already answered
        }

        const isCorrect = btn.getAttribute('data-correct') === 'true';

        optionBtns.forEach(b => {
          b.disabled = true;
          if (b.getAttribute('data-correct') === 'true') {
            b.classList.add('correct');
          }
        });

        if (isCorrect) {
          btn.classList.add('correct');
          card.classList.add('answered-correct');
          showToast('✅ ត្រឹមត្រូវ! (Correct Answer)');
        } else {
          btn.classList.add('wrong');
          card.classList.add('answered-wrong');
          showToast('❌ មិនត្រឹមត្រូវ! (Incorrect)');
        }

        if (explanationBox) {
          explanationBox.classList.add('show');
        }

        updateQuizScore();
      });
    });
  });

  if (quizResetBtn) {
    quizResetBtn.addEventListener('click', () => {
      quizCards.forEach(card => {
        card.classList.remove('answered-correct', 'answered-wrong');
        const optionBtns = card.querySelectorAll('.quiz-option-btn');
        optionBtns.forEach(btn => {
          btn.disabled = false;
          btn.classList.remove('correct', 'wrong');
        });
        const explanationBox = card.querySelector('.quiz-explanation-box');
        if (explanationBox) {
          explanationBox.classList.remove('show');
        }
      });
      updateQuizScore();
      showToast('🔄 Quiz has been reset. Good luck!');
    });
  }

  updateQuizScore();
});
