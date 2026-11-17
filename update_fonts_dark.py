# -*- coding: utf-8 -*-

# 1. Update index.html
with open("d:/Adobe Illustrator/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# Update Google Fonts link to include Moul, Kantumruy Pro, Inter, Plus Jakarta Sans, Fira Code
old_fonts = '<link href="https://fonts.googleapis.com/css2?family=Kantumruy+Pro:wght@400;600;700;800&family=Playfair+Display:ital,wght@0,600;0,800;1,600&display=swap" rel="stylesheet">'
new_fonts = '<link href="https://fonts.googleapis.com/css2?family=Fira+Code:wght@400;500;600;700&family=Inter:wght@400;500;600;700;800&family=Kantumruy+Pro:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400;1,600&family=Moul&family=Plus+Jakarta+Sans:wght@500;600;700;800&display=swap" rel="stylesheet">'

if old_fonts in html:
    html = html.replace(old_fonts, new_fonts)

# Add Dark Mode toggle button right before or after the timer pill in header
old_timer_end = '</div>\n  </header>'
dark_toggle_html = """      <!-- Dark Mode Toggle Button -->
      <button class="theme-toggle-btn" id="theme-toggle-btn" title="ប្តូរពន្លឺ / ងងឹត (Toggle Dark/Light Mode)" aria-label="Toggle Dark Mode">
        <span class="theme-icon-sun">
          <svg width="17" height="17" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <circle cx="12" cy="12" r="5"></circle>
            <line x1="12" y1="1" x2="12" y2="3"></line>
            <line x1="12" y1="21" x2="12" y2="23"></line>
            <line x1="4.22" y1="4.22" x2="5.64" y2="5.64"></line>
            <line x1="18.36" y1="18.36" x2="19.78" y2="19.78"></line>
            <line x1="1" y1="12" x2="3" y2="12"></line>
            <line x1="21" y1="12" x2="23" y2="12"></line>
            <line x1="4.22" y1="19.78" x2="5.64" y2="18.36"></line>
            <line x1="18.36" y1="5.64" x2="19.78" y2="4.22"></line>
          </svg>
        </span>
        <span class="theme-icon-moon">
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round">
            <path d="M21 12.79A9 9 0 1 1 11.21 3 7 7 0 0 0 21 12.79z"></path>
          </svg>
        </span>
        <span class="theme-btn-label">Dark</span>
      </button>
    </div>
  </header>"""

if old_timer_end in html and "theme-toggle-btn" not in html:
    html = html.replace(old_timer_end, dark_toggle_html)

with open("d:/Adobe Illustrator/index.html", "w", encoding="utf-8") as f:
    f.write(html)
print("Updated index.html successfully!")
