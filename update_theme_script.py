# -*- coding: utf-8 -*-

# 1. Update script.js with Theme Toggle handler
with open("d:/Adobe Illustrator/script.js", "r", encoding="utf-8") as f:
    js = f.read()

theme_js = """  // ==================== 00. DARK / LIGHT THEME CONTROLLER ====================
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

"""

if "theme-toggle-btn" not in js:
    # Insert right at start of DOMContentLoaded handler
    start_marker = "document.addEventListener('DOMContentLoaded', () => {"
    js = js.replace(start_marker, start_marker + "\n" + theme_js)
    with open("d:/Adobe Illustrator/script.js", "w", encoding="utf-8") as f:
        f.write(js)
    print("Updated script.js with dark mode logic!")

