# -*- coding: utf-8 -*-
import io

project_3_html = """
  <!-- ==================== PROJECT 3: THEORY QUIZ WRAPPER ==================== -->
  <div class="project-section-wrapper" id="project-3-wrapper">

    <!-- HERO SECTION 3 -->
    <section class="hero hero-theme-purple" id="hero-3">
      <div class="hero-container">
        <div class="hero-left">
          <div class="hero-tag" style="background: rgba(124, 58, 237, 0.25); border-color: rgba(196, 181, 253, 0.5); color: #e9d5ff;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
              <path d="M9 11l3 3L22 4"></path>
              <path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path>
            </svg>
            វិញ្ញាសាទ្រឹស្តីទី៣ • Graphic Design Knowledge Assessment
          </div>
          <h2 class="hero-title">កម្រងសំណួរ ៣៖ <span>វាយតម្លៃសមត្ថភាពចំណេះដឹង</span></h2>
          <p class="hero-subtitle">
            ដំណោះស្រាយពេញលេញ និងការពន្យល់ស៊ីជម្រៅលើសំណួរពហុជ្រើសរើស (MCQ) ទាំង ៥ សំណួរ ស្តីអំពី <strong>ប្រព័ន្ធពណ៌បោះពុម្ព (CMYK) vs បណ្តាញសង្គម (RGB)</strong>, ប្រភេទឯកសារដើមរបស់ Illustrator (<strong>.AI</strong>), ដង់ស៊ីតេភីកសែល (<strong>Resolution</strong>), និង Shortcut <strong>Create Outline (Ctrl + Shift + O)</strong>។
          </p>

          <div class="hero-badges">
            <div class="hero-badge-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#d8b4fe" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><path d="M9.09 9a3 3 0 0 1 5.83 1c0 2-3 3-3 3"></path><line x1="12" y1="17" x2="12.01" y2="17"></line></svg>
              សំណួរ៖ <strong>៥ សំណួរ (Multiple Choice)</strong>
            </div>
            <div class="hero-badge-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#d8b4fe" stroke-width="2"><path d="M22 11.08V12a10 10 0 1 1-5.93-9.14"></path><polyline points="22 4 12 14.01 9 11.01"></polyline></svg>
              ពិន្ទុអតិបរមា៖ <strong>100% Full Score</strong>
            </div>
            <div class="hero-badge-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#d8b4fe" stroke-width="2"><polygon points="13 2 3 14 12 14 11 22 21 10 12 10 13 2"></polygon></svg>
              ប្រព័ន្ធ៖ <strong>Interactive Quiz Engine</strong>
            </div>
          </div>

          <div class="hero-actions">
            <a href="#interactive-quiz-app" class="btn-primary btn-purple">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              ចាប់ផ្តើមធ្វើតេស្ត (Start Interactive Quiz)
            </a>
            <a href="#exam-brief-3" class="btn-secondary">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line></svg>
              មើលចម្លើយ &amp; ការបកស្រាយ (Answers)
            </a>
          </div>
        </div>

        <div class="hero-right">
          <div class="hero-preview-card" style="border-top: 4px solid #7c3aed;">
            <span class="card-label" style="background: #7c3aed;">Theory Assessment</span>
            <div style="padding: 1.5rem 1rem; text-align: left;">
              <div style="display: flex; align-items: center; gap: 0.75rem; margin-bottom: 1rem;">
                <div style="width: 44px; height: 44px; border-radius: 50%; background: #f3e8ff; display: flex; align-items: center; justify-content: center; color: #7c3aed; font-size: 1.3rem; font-weight: 800;">
                  ?
                </div>
                <div>
                  <h4 style="font-size: 1rem; color: #1e293b; margin: 0;">តេស្តចំណេះដឹងទូទៅ</h4>
                  <p style="font-size: 0.8rem; color: #64748b; margin: 0;">Graphic Design &amp; Pre-press</p>
                </div>
              </div>
              <ul style="list-style: none; display: flex; flex-direction: column; gap: 0.5rem; font-size: 0.85rem; color: #334155;">
                <li>✔ 1. ពណ៌បោះពុម្ព &rarr; <strong>CMYK</strong></li>
                <li>✔ 2. ពណ៌ Facebook Flyer &rarr; <strong>RGB</strong></li>
                <li>✔ 3. ឯកសារ Adobe Illustrator &rarr; <strong>.AI</strong></li>
                <li>✔ 4. ដង់ស៊ីតេ Pixel &rarr; <strong>Resolution</strong></li>
                <li>✔ 5. Shortcut Create Outline &rarr; <strong>Ctrl+Shift+O</strong></li>
              </ul>
            </div>
            <p style="font-size: 0.82rem; color: #7c3aed; font-weight: 700; margin-top: 0.5rem; text-align: center;">
              100% Answer Accuracy Verified
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 1: ORIGINAL EXAM SHEET & DETAILED ANSWERS -->
    <section class="container" id="exam-brief-3">
      <div class="section-header">
        <span class="section-tag" style="color: #7c3aed;">QUIZ ANSWER KEY</span>
        <h3 class="section-title">សន្លឹកកិច្ចការដើម និងចម្លើយត្រឹមត្រូវទាំង ៥ សំណួរ</h3>
        <p class="section-subtitle">
          ដកស្រង់លម្អិតចេញពីរូបភាពសន្លឹកសំណួរទី៣ ជាមួយការពន្យល់នូវរាល់ហេតុផលបច្ចេកទេស និងវិទ្យាសាស្ត្រក្រាហ្វិក។
        </p>
      </div>

      <div class="exam-breakdown-grid">
        <!-- Original Scan -->
        <div class="card">
          <h4 class="card-title">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
            រូបភាពសន្លឹកសំណួរទី៣ (Original Quiz Sheet)
          </h4>
          <div class="exam-image-box" title="Click to open full-screen view">
            <img src="exam-sample-3.jpg" alt="Knowledge Assessment Quiz Sheet">
            <div class="image-overlay-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              ចុចដើម្បីពង្រីកមើលច្បាស់ (Click to Zoom)
            </div>
          </div>
          <p style="font-size: 0.82rem; color: #64748b; margin-top: 0.85rem; text-align: center;">
            កម្រងសំណួរវាយតម្លៃសមត្ថភាពចំណេះដឹង (Knowledge Competency Assessment)
          </p>
        </div>

        <!-- Comprehensive Explanations List -->
        <div class="card">
          <h4 class="card-title">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
            វិភាគចម្លើយត្រឹមត្រូវ (Detailed Answer Explanations)
          </h4>

          <ul class="rules-list">
            <!-- Q1 -->
            <li class="rule-item" style="border-left-color: #7c3aed;">
              <div class="rule-num" style="background: #7c3aed;">1</div>
              <div class="rule-content">
                <h4>សំណួរទី ១៖ តើពណ៌អ្វីដែលត្រូវប្រើសម្រាប់ការរចនាដើម្បីបោះពុម្ពជាទូទៅ ?</h4>
                <p>ចម្លើយត្រឹមត្រូវ៖ <strong style="color: #16a34a; font-size: 1rem;">ខ. CMYK</strong></p>
                <p style="margin-top: 0.25rem;"><strong>ការពន្យល់បច្ចេកទេស៖</strong> <strong>CMYK</strong> (Cyan, Magenta, Yellow, Key/Black) គឺជាប្រព័ន្ធពណ៌ Subtractive Color Model ដែលទឹកថ្នាំទាំងបួនត្រូវបាញ់លាយលើក្រដាសដើម្បីបង្កើតជារូបភាពបោះពុម្ព Offset ឬ Digital។ ប្រសិនបើប្រើ RGB ទៅបោះពុម្ព នោះពណ៌នៅលើក្រដាសនឹងប្រែជាខុសពីអេក្រង់ទាំងស្រុង។</p>
              </div>
            </li>

            <!-- Q2 -->
            <li class="rule-item" style="border-left-color: #7c3aed;">
              <div class="rule-num" style="background: #7c3aed;">2</div>
              <div class="rule-content">
                <h4>សំណួរទី ២៖ ក្នុងការធ្វើហ្វូយយ៉ាសម្រាប់ផុសនៅលើហ្វេសបុក តើយើងយក Color Mode ប្រភេទអ្វី ?</h4>
                <p>ចម្លើយត្រឹមត្រូវ៖ <strong style="color: #16a34a; font-size: 1rem;">ក. RGB</strong></p>
                <p style="margin-top: 0.25rem;"><strong>ការពន្យល់បច្ចេកទេស៖</strong> <strong>RGB</strong> (Red, Green, Blue) គឺជាប្រព័ន្ធពណ៌ Additive Color Model បង្កើតឡើងដោយកាំរស្មីពន្លឺនៃអេក្រង់ (Display Monitors, Smartphones, Tablets)។ រាល់ការងារឌីជីថលទាំងអស់សម្រាប់ Facebook, Instagram, Websites ត្រូវតែប្រើ RGB ដើម្បីទទួលបានពណ៌ស្រស់ថ្លា និងមិនខូចពណ៌។</p>
              </div>
            </li>

            <!-- Q3 -->
            <li class="rule-item" style="border-left-color: #7c3aed;">
              <div class="rule-num" style="background: #7c3aed;">3</div>
              <div class="rule-content">
                <h4>សំណួរទី ៣៖ ប្រភេទឯកសារមួយណាដែលជាកម្មវិធី Adobe Illustrator ?</h4>
                <p>ចម្លើយត្រឹមត្រូវ៖ <strong style="color: #16a34a; font-size: 1rem;">គ. AI</strong></p>
                <p style="margin-top: 0.25rem;"><strong>ការពន្យល់បច្ចេកទេស៖</strong> <strong>.AI</strong> (Adobe Illustrator Artwork) គឺជាទម្រង់ឯកសារមេដើម (Native Format) របស់ Adobe Illustrator។ ចំណែកឯ PSD ជាឯកសាររបស់ Photoshop, PNG ជារូបភាព Raster គ្មាន Background, និង SVG គឺជា Open Standard Scalable Vector Graphics។</p>
              </div>
            </li>

            <!-- Q4 -->
            <li class="rule-item" style="border-left-color: #7c3aed;">
              <div class="rule-num" style="background: #7c3aed;">4</div>
              <div class="rule-content">
                <h4>សំណួរទី ៤៖ ដង់ស៊ីតេភីកសែល (pixel) នៅលើអេក្រង់ត្រូវបានគេស្គាល់ថា:</h4>
                <p>ចម្លើយត្រឹមត្រូវ៖ <strong style="color: #16a34a; font-size: 1rem;">ក. គុណភាពបង្ហាញ (resolution)</strong></p>
                <p style="margin-top: 0.25rem;"><strong>ការពន្យល់បច្ចេកទេស៖</strong> ចំនួនគ្រាប់ភីកសែលក្នុងមួយឯកតាផ្ទៃ (Pixels Per Inch - PPI) គឺជាកម្រិតបង្ហាញ ឬ <strong>Resolution</strong>។ កាលណាដង់ស៊ីតេភីកសែលកាន់តែច្រើន រូបភាពនៅលើអេក្រង់កាន់តែម៉ត់ច្បាស់ មិនបែកគ្រាប់។</p>
              </div>
            </li>

            <!-- Q5 -->
            <li class="rule-item" style="border-left-color: #7c3aed;">
              <div class="rule-num" style="background: #7c3aed;">5</div>
              <div class="rule-content">
                <h4>សំណួរទី ៥៖ តើ Shortcut មួយណានៅក្នុងកម្មវិធី Illustrator ដែលប្រើសម្រាប់ Create Outline (Kill Fonts) ?</h4>
                <p>ចម្លើយត្រឹមត្រូវ៖ <strong style="color: #16a34a; font-size: 1rem;">ខ. Ctrl + Shift + O</strong></p>
                <p style="margin-top: 0.25rem;"><strong>ការពន្យល់បច្ចេកទេស៖</strong> <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd> (Menu: <code>Type &gt; Create Outlines</code>) គឺជា Shortcut ផ្លូវការសម្រាប់សម្លាប់ Font ទៅជា Vector Curves។<br>
                <span style="color: #b91c1c; font-weight: 700;">⚠️ ចំណាំសំខាន់៖</span> ក្នុងសន្លឹកវិញ្ញាសាមានស្នាមគូសខ្មៅដៃក្បែរ <em>ឃ. Ctrl + G</em> ដែលជាចម្លើយខុស! ព្រោះ <kbd>Ctrl</kbd> + <kbd>G</kbd> គឺសម្រាប់ Group វត្ថុ, <kbd>Ctrl</kbd> + <kbd>O</kbd> គឺសម្រាប់ Open File, និង <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>P</kbd> គឺសម្រាប់ Place File។</p>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTION 2: INTERACTIVE LIVE QUIZ APP -->
    <section class="container" id="interactive-quiz-app">
      <div class="section-header">
        <span class="section-tag" style="color: #7c3aed;">PRACTICE &amp; TEST</span>
        <h3 class="section-title">កម្មវិធីធ្វើតេស្តសាកល្បងជាក់ស្តែង (Interactive Quiz Simulator)</h3>
        <p class="section-subtitle">
          ចុចលើជម្រើសនីមួយៗ (ក, ខ, គ, ឃ) ដើម្បីដឹងចម្លើយភ្លាមៗ និងពិនិត្យពិន្ទុរបស់អ្នក
        </p>
      </div>

      <div class="quiz-container">

        <!-- Live Score Banner -->
        <div class="quiz-score-banner">
          <div class="score-stats">
            <h3 id="quiz-status-text">សូមជ្រើសរើសចម្លើយសម្រាប់សំណួរទាំង ៥ ខាងក្រោម</h3>
            <p style="opacity: 0.9; font-size: 0.9rem; margin: 0;">ពិន្ទុនឹងត្រូវបានគណនាភ្លាមៗពេលអ្នកចុចជ្រើសរើស</p>
          </div>
          <div style="display: flex; align-items: center; gap: 1rem;">
            <div class="score-pill-badge">
              ពិន្ទុ៖ <span id="quiz-score-display">0 / 5</span>
            </div>
            <button class="btn-secondary" id="quiz-reset-btn" style="padding: 0.45rem 1rem; font-size: 0.85rem; border-color: rgba(255,255,255,0.4);">
              🔄 ធ្វើឡើងវិញ (Reset)
            </button>
          </div>
        </div>

        <!-- Question 1 Card -->
        <div class="quiz-card" id="quiz-card-1">
          <div class="quiz-q-header">
            <div>
              <h4 class="quiz-q-title">១. តើពណ៌អ្វីដែលត្រូវប្រើសម្រាប់ការរចនាដើម្បីបោះពុម្ពជាទូទៅ ?</h4>
              <div class="quiz-q-en">Which color model is generally used for design intended for printing?</div>
            </div>
            <span class="quiz-q-num">Q1 • 20 Pts</span>
          </div>

          <div class="quiz-options-list">
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ក</span>
              <span>RGB</span>
            </button>
            <button class="quiz-option-btn" data-correct="true">
              <span class="quiz-option-letter">ខ</span>
              <span>CMYK (Cyan, Magenta, Yellow, Key/Black)</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">គ</span>
              <span>HSB (Hue, Saturation, Brightness)</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ឃ</span>
              <span>LAB</span>
            </button>
          </div>

          <div class="quiz-explanation-box">
            <strong style="color: #16a34a;">✅ ចម្លើយត្រឹមត្រូវគឺ ខ. CMYK:</strong>
            ការបោះពុម្ពលើក្រដាសប្រើប្រាស់ទឹកថ្នាំ ៤ ពណ៌គឺ Cyan (ផ្ទៃមេឃ), Magenta (ផ្កាឈូកក្រម៉ៅ), Yellow (លឿង), និង Black (ខ្មៅ)។ វត្ថុធាតុបោះពុម្ពជា Subtractive Color Model ដូច្នេះការងារបោះពុម្ពទាំងអស់ត្រូវតែកំណត់ជា CMYK។
          </div>
        </div>

        <!-- Question 2 Card -->
        <div class="quiz-card" id="quiz-card-2">
          <div class="quiz-q-header">
            <div>
              <h4 class="quiz-q-title">២. ក្នុងការធ្វើហ្វូយយ៉ាសម្រាប់ផុសនៅលើហ្វេសបុក តើយើងយក Color Mode ប្រភេទអ្វី ?</h4>
              <div class="quiz-q-en">When designing a flyer for posting on Facebook, which Color Mode do we use?</div>
            </div>
            <span class="quiz-q-num">Q2 • 20 Pts</span>
          </div>

          <div class="quiz-options-list">
            <button class="quiz-option-btn" data-correct="true">
              <span class="quiz-option-letter">ក</span>
              <span>RGB (Red, Green, Blue)</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ខ</span>
              <span>CMYK</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">គ</span>
              <span>HSB</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ឃ</span>
              <span>LAB</span>
            </button>
          </div>

          <div class="quiz-explanation-box">
            <strong style="color: #16a34a;">✅ ចម្លើយត្រឹមត្រូវគឺ ក. RGB:</strong>
            Facebook ជាបណ្តាញសង្គមឌីជីថលដែលបង្ហាញនៅលើអេក្រង់កុំព្យូទ័រ និងទូរសព្ទដៃ។ អេក្រង់ឌីជីថលដំណើរការដោយពន្លឺ RGB (Red, Green, Blue)។ ប្រសិនបើយើង Export រូបភាពជា CMYK ទៅផុសលើ Facebook នោះពណ៌នឹងស្រអាប់ និងខុសពណ៌ដើមទាំងស្រុង។
          </div>
        </div>

        <!-- Question 3 Card -->
        <div class="quiz-card" id="quiz-card-3">
          <div class="quiz-q-header">
            <div>
              <h4 class="quiz-q-title">៣. ប្រភេទឯកសារមួយណាដែលជាកម្មវិធី Adobe Illustrator ?</h4>
              <div class="quiz-q-en">Which file format natively belongs to Adobe Illustrator?</div>
            </div>
            <span class="quiz-q-num">Q3 • 20 Pts</span>
          </div>

          <div class="quiz-options-list">
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ក</span>
              <span>PSD (Photoshop Document)</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ខ</span>
              <span>PNG (Portable Network Graphics)</span>
            </button>
            <button class="quiz-option-btn" data-correct="true">
              <span class="quiz-option-letter">គ</span>
              <span>AI (Adobe Illustrator Artwork)</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ឃ</span>
              <span>SVG (Scalable Vector Graphics)</span>
            </button>
          </div>

          <div class="quiz-explanation-box">
            <strong style="color: #16a34a;">✅ ចម្លើយត្រឹមត្រូវគឺ គ. AI:</strong>
            កន្ទុយឯកសារ <code>.AI</code> តំណាងឲ្យ Adobe Illustrator Artwork ដែលជា Native Format ផ្តាច់មុខរបស់កម្មវិធីនេះ។ កន្ទុយ <code>.PSD</code> ជារបស់ Photoshop, <code>.PNG</code> ជារូបភាព Raster, និង <code>.SVG</code> ជា Open Standard Vector។
          </div>
        </div>

        <!-- Question 4 Card -->
        <div class="quiz-card" id="quiz-card-4">
          <div class="quiz-q-header">
            <div>
              <h4 class="quiz-q-title">៤. ដង់ស៊ីតេភីកសែល (pixel) នៅលើអេក្រង់ត្រូវបានគេស្គាល់ថា:</h4>
              <div class="quiz-q-en">The pixel density on a screen is technically known as:</div>
            </div>
            <span class="quiz-q-num">Q4 • 20 Pts</span>
          </div>

          <div class="quiz-options-list">
            <button class="quiz-option-btn" data-correct="true">
              <span class="quiz-option-letter">ក</span>
              <span>គុណភាពបង្ហាញ (resolution)</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ខ</span>
              <span>ទំហំអេក្រង់ (Screen Size)</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">គ</span>
              <span>ទំហំភីកសែល (Pixel Size)</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ឃ</span>
              <span>ភាពច្បាស់នៃអេក្រង់ (Screen Sharpness)</span>
            </button>
          </div>

          <div class="quiz-explanation-box">
            <strong style="color: #16a34a;">✅ ចម្លើយត្រឹមត្រូវគឺ ក. គុណភាពបង្ហាញ (resolution):</strong>
            ដង់ស៊ីតេភីកសែល ឬកំហាប់គ្រាប់ភីកសែលក្នុងមួយអ៊ីញ (PPI - Pixels Per Inch / DPI) ត្រូវបានកំណត់ជានិយមន័យបច្ចេកទេសថាជា <strong>គុណភាពបង្ហាញ (Resolution)</strong>។ កាលណា PPI កាន់តែខ្ពស់ រូបភាពកាន់តែម៉ត់ច្បាស់ល្អ។
          </div>
        </div>

        <!-- Question 5 Card -->
        <div class="quiz-card" id="quiz-card-5">
          <div class="quiz-q-header">
            <div>
              <h4 class="quiz-q-title">៥. តើ Shortcut មួយណានៅក្នុងកម្មវិធី Illustrator ដែលប្រើសម្រាប់ Create Outline (Kill Fonts) ?</h4>
              <div class="quiz-q-en">Which keyboard shortcut in Adobe Illustrator is used for Create Outline (Kill Fonts)?</div>
            </div>
            <span class="quiz-q-num">Q5 • 20 Pts</span>
          </div>

          <div class="quiz-options-list">
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ក</span>
              <span>Ctrl + O (បើកឯកសារ / Open File)</span>
            </button>
            <button class="quiz-option-btn" data-correct="true">
              <span class="quiz-option-letter">ខ</span>
              <span>Ctrl + Shift + O (Create Outlines / សម្លាប់ Font)</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">គ</span>
              <span>Ctrl + Shift + P (ដាក់រូបភាព / Place File)</span>
            </button>
            <button class="quiz-option-btn" data-correct="false">
              <span class="quiz-option-letter">ឃ</span>
              <span>Ctrl + G (ចងក្រុមកិច្ចការ / Group Objects)</span>
            </button>
          </div>

          <div class="quiz-explanation-box">
            <strong style="color: #16a34a;">✅ ចម្លើយត្រឹមត្រូវគឺ ខ. Ctrl + Shift + O:</strong>
            Shortcut <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd> បម្លែងអក្សរទាំងអស់ទៅជា Vector Path ដែលគេហៅសាមញ្ញថាសម្លាប់ Font (Create Outline) ដើម្បីកុំឲ្យបាត់ Font ពេលបើកលើកុំព្យូទ័រផ្សេង។<br>
            <span style="color: #b91c1c; font-weight: 700;">ចំណាំពិសេស៖</span> ស្នាមខ្មៅដៃដែលគូសលើសន្លឹកវិញ្ញាសានៅជិត <em>ឃ. Ctrl + G</em> គឺជាចម្លើយខុស! ព្រោះ <kbd>Ctrl</kbd> + <kbd>G</kbd> គឺសម្រាប់ Group វត្ថុចូលគ្នាប៉ុណ្ណោះ។
          </div>
        </div>

      </div>
    </section>

    <!-- SECTION 3: THEORY MASTER CHEAT SHEET -->
    <section class="container" style="padding-top: 1rem;">
      <div class="card" style="border-top: 4px solid #7c3aed;">
        <h4 style="font-size: 1.25rem; font-weight: 800; color: #4c1d95; margin-bottom: 1.2rem; display: flex; align-items: center; gap: 0.6rem;">
          <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#7c3aed" stroke-width="2"><path d="M4 19.5A2.5 2.5 0 0 1 6.5 17H20"></path><path d="M6.5 2H20v20H6.5A2.5 2.5 0 0 1 4 19.5v-15A2.5 2.5 0 0 1 6.5 2z"></path></svg>
          តារាងសង្ខេបទ្រឹស្តីស្នូលសម្រាប់ត្រៀមប្រឡង (Exam Theory Summary Matrix)
        </h4>

        <div style="overflow-x: auto;">
          <table class="code-table" style="font-size: 0.9rem;">
            <thead>
              <tr style="background: #f3e8ff; color: #4c1d95; font-weight: 800;">
                <th style="padding: 0.75rem; text-align: left;">ប្រធានបទ</th>
                <th style="padding: 0.75rem; text-align: left;">Print / បោះពុម្ព</th>
                <th style="padding: 0.75rem; text-align: left;">Digital / អេក្រង់ &amp; Facebook</th>
                <th style="padding: 0.75rem; text-align: left;">ចំណាំបច្ចេកទេស</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td style="padding: 0.75rem; font-weight: 700;">Color Mode</td>
                <td style="padding: 0.75rem; color: #0284c7; font-weight: 700;">CMYK (Cyan, Magenta, Yellow, Black)</td>
                <td style="padding: 0.75rem; color: #7c3aed; font-weight: 700;">RGB (Red, Green, Blue)</td>
                <td style="padding: 0.75rem; font-size: 0.82rem; color: #64748b;">Subtractive (ទឹកថ្នាំ) vs Additive (ពន្លឺ)</td>
              </tr>
              <tr>
                <td style="padding: 0.75rem; font-weight: 700;">Standard Resolution</td>
                <td style="padding: 0.75rem; font-weight: 700;">300 PPI (High Quality)</td>
                <td style="padding: 0.75rem; font-weight: 700;">72 PPI – 144 PPI (Screen)</td>
                <td style="padding: 0.75rem; font-size: 0.82rem; color: #64748b;">កម្រិតដង់ស៊ីតេភីកសែលបង្ហាញ</td>
              </tr>
              <tr>
                <td style="padding: 0.75rem; font-weight: 700;">Native Format</td>
                <td style="padding: 0.75rem; font-family: monospace; font-weight: 700;">.AI (Illustrator Artwork)</td>
                <td style="padding: 0.75rem; font-family: monospace; font-weight: 700;">.PSD, .PNG, .JPG</td>
                <td style="padding: 0.75rem; font-size: 0.82rem; color: #64748b;">Vector Master File vs Raster Images</td>
              </tr>
              <tr>
                <td style="padding: 0.75rem; font-weight: 700;">Font Protection</td>
                <td style="padding: 0.75rem; font-family: monospace; font-weight: 700;">Ctrl + Shift + O (Create Outline)</td>
                <td style="padding: 0.75rem; font-family: monospace; font-weight: 700;">Export as PNG/JPG</td>
                <td style="padding: 0.75rem; font-size: 0.82rem; color: #64748b;">បម្លែង Text ទៅជា Paths ការពារបាត់ Font</td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>
    </section>

  </div>
  <!-- ==================== END PROJECT 3 ==================== -->
"""

with open("d:/Adobe Illustrator/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Update Project Switcher Bar to include 3rd Tab
old_switch_target = '<span>គម្រោង ២៖ ការរចនានាមប័ណ្ណ (Business Card)</span>\n    </button>'
new_switch_btn = """<span>គម្រោង ២៖ ការរចនានាមប័ណ្ណ (Business Card)</span>
    </button>
    <button class="proj-tab-btn" data-target="project-3-wrapper">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><path d="M9 11l3 3L22 4"></path><path d="M21 12v7a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2V5a2 2 0 0 1 2-2h11"></path></svg>
      <span>កម្រងសំណួរ ៣៖ វាយតម្លៃសមត្ថភាព (Theory Quiz)</span>
    </button>"""

if old_switch_target in html and "project-3-wrapper" not in html:
    html = html.replace(old_switch_target, new_switch_btn)

# 2. Append Project 3 section before <!-- ==================== IMAGE MODAL ==================== -->
modal_marker = '<!-- ==================== IMAGE MODAL ==================== -->'
if "id=\"project-3-wrapper\"" not in html and modal_marker in html:
    html = html.replace(modal_marker, project_3_html + '\n\n  ' + modal_marker)

with open("d:/Adobe Illustrator/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully added Quiz 3 to index.html!")
