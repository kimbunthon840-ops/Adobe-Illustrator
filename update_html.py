# -*- coding: utf-8 -*-
import io

project_2_html = """
  <!-- ==================== PROJECT 2: BUSINESS CARD WRAPPER ==================== -->
  <div class="project-section-wrapper" id="project-2-wrapper">

    <!-- HERO SECTION 2 -->
    <section class="hero hero-theme-cyan" id="hero-2">
      <div class="hero-container">
        <div class="hero-left">
          <div class="hero-tag" style="background: rgba(2, 132, 199, 0.25); border-color: rgba(56, 189, 248, 0.5); color: #bae6fd;">
            <svg width="14" height="14" viewBox="0 0 24 24" fill="currentColor">
              <polygon points="12 2 15.09 8.26 22 9.27 17 14.14 18.18 21.02 12 17.77 5.82 21.02 7 14.14 2 9.27 8.91 8.26 12 2"></polygon>
            </svg>
            វិញ្ញាសាអនុវត្តជាក់ស្តែងទី២ • Adobe Illustrator
          </div>
          <h2 class="hero-title">គម្រោងប្រតិបត្តិ២៖ <span>ការរចនានាមប័ណ្ណ</span></h2>
          <p class="hero-subtitle">
            មគ្គុទ្ទេសក៍ពេញលេញសម្រាប់រចនានាមប័ណ្ណសងខាង (Front &amp; Back) ទំហំស្តង់ដារ <strong>85mm &times; 50mm (Bleed 3mm)</strong>, ការបញ្ចូល Logo ពីកិច្ចការទី១, ការកំណត់ 2 Spot Colors / CMYK / RGB, ការរៀបប្លង់ព្រីន <strong>Imposition ១០ សន្លឹកលើ A4</strong> និងការពង្រីកព្រីនខ្នាតធំមិនលើសពី 200mm។
          </p>

          <div class="hero-badges">
            <div class="hero-badge-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#7dd3fc" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
              ពេលវេលា៖ <strong>១ ម៉ោង ៣០ នាទី</strong>
            </div>
            <div class="hero-badge-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#7dd3fc" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
              ទំហំ៖ <strong>85 &times; 50 mm (Bleed 3mm)</strong>
            </div>
            <div class="hero-badge-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#7dd3fc" stroke-width="2"><path d="M12 2l3.09 6.26L22 9.27l-5 4.87 1.18 6.88L12 17.77l-6.18 3.25L7 14.14 2 9.27l6.91-1.01L12 2z"></path></svg>
              ពណ៌៖ <strong>2 Spot Colors (No Tints/Gradients)</strong>
            </div>
            <div class="hero-badge-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#7dd3fc" stroke-width="2"><rect x="2" y="2" width="20" height="20" rx="2"></rect><line x1="8" y1="2" x2="8" y2="22"></line><line x1="16" y1="2" x2="16" y2="22"></line></svg>
              Imposition: <strong>១០ នាមប័ណ្ណ / A4</strong>
            </div>
            <div class="hero-badge-item">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="#7dd3fc" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
              Formats: <strong>PDF, PNG, AI</strong>
            </div>
          </div>

          <div class="hero-actions">
            <a href="#tutorial-steps-2" class="btn-primary btn-cyan">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><polygon points="5 3 19 12 5 21 5 3"></polygon></svg>
              រៀនជំហានរចនានាមប័ណ្ណ (Start Tutorial)
            </a>
            <a href="#exam-brief-2" class="btn-secondary">
              <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><circle cx="12" cy="12" r="10"></circle><line x1="12" y1="16" x2="12" y2="12"></line></svg>
              ពិនិត្យលក្ខខណ្ឌវិញ្ញាសា (Exam Brief)
            </a>
          </div>
        </div>

        <div class="hero-right">
          <div class="hero-preview-card" style="max-width: 460px;">
            <span class="card-label" style="background: #0284c7;">Vector Business Card</span>
            <div style="width: 100%; aspect-ratio: 1.7/1; overflow: hidden; border-radius: 8px;">
              <object data="card-preview.svg" type="image/svg+xml" width="100%" height="100%"></object>
            </div>
            <p style="font-size: 0.85rem; color: #64748b; margin-top: 0.75rem; font-weight: 600;">
              ម៉ូដែលនាមប័ណ្ណ Front &amp; Back សម្រេច ១០០%
            </p>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 1: EXAM 2 BRIEF BREAKDOWN -->
    <section class="container" id="exam-brief-2">
      <div class="section-header">
        <span class="section-tag" style="color: #0284c7;">PROJECT 2 SPECIFICATIONS</span>
        <h3 class="section-title">វិភាគសំណួរ និងលក្ខខណ្ឌបច្ចេកទេសនៃគម្រោងទី២ (នាមប័ណ្ណ)</h3>
        <p class="section-subtitle">
          ដកស្រង់លម្អិតចេញពីសន្លឹកវិញ្ញាសាជាក់ស្តែងទី២ រួមទាំងលក្ខខណ្ឌព្រីនមុនបោះពុម្ព (Pre-Press &amp; Imposition)។
        </p>
      </div>

      <div class="exam-breakdown-grid">
        <!-- Original Sheet Scan -->
        <div class="card">
          <h4 class="card-title">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2"><rect x="3" y="3" width="18" height="18" rx="2"></rect><circle cx="8.5" cy="8.5" r="1.5"></circle><polyline points="21 15 16 10 5 21"></polyline></svg>
            រូបភាពសន្លឹកវិញ្ញាសាទី២ (Original Exam Sheet 2)
          </h4>
          <div class="exam-image-box" title="Click to open full-screen view">
            <img src="exam-sample-2.jpg" alt="Business Card Exam Sheet">
            <div class="image-overlay-pill">
              <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><circle cx="11" cy="11" r="8"></circle><line x1="21" y1="21" x2="16.65" y2="16.65"></line></svg>
              ចុចដើម្បីពង្រីកមើលច្បាស់ (Click to Zoom)
            </div>
          </div>
          <p style="font-size: 0.82rem; color: #64748b; margin-top: 0.85rem; text-align: center;">
            រយៈពេលអនុវត្ត៖ <strong>១ ម៉ោង ៣០ នាទី (90 Minutes)</strong> ក្នុងកម្មវិធី Adobe Illustrator
          </p>
        </div>

        <!-- Explanations of All 12 Rules -->
        <div class="card">
          <h4 class="card-title">
            <svg width="22" height="22" viewBox="0 0 24 24" fill="none" stroke="#0284c7" stroke-width="2"><path d="M14 2H6a2 2 0 0 0-2 2v16a2 2 0 0 0 2 2h12a2 2 0 0 0 2-2V8z"></path><polyline points="14 2 14 8 20 8"></polyline></svg>
            ការបកស្រាយលក្ខខណ្ឌទាំង ១២ ចំណុចនៃវិញ្ញាសាទី២
          </h4>

          <ul class="rules-list">
            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">1</div>
              <div class="rule-content">
                <h4>នាមប័ណ្ណសងខាង (Front &amp; Back) និងព័ត៌មានលម្អិត</h4>
                <p>ត្រូវរចនានាមប័ណ្ណសងខាងដោយផ្ទាល់ ដោយក្នុងនោះត្រូវមាន៖ ឈ្មោះ (<strong>ហ៊ាន សុខា</strong>), តួនាទី (<strong>អ្នកគ្រប់គ្រងទូទៅ</strong>), លេខទូរសព្ទ, គេហទំព័រ, អ៊ីមែល និងទីតាំង (Address) អមដោយរូបតំណាង Icon និង QR Code។</p>
              </div>
            </li>

            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">2</div>
              <div class="rule-content">
                <h4>យកនិមិត្តសញ្ញានៃកិច្ចការទីមួយមកប្រើក្នុងនាមប័ណ្ណ</h4>
                <p>ត្រូវយក Logo <strong>"សាលាបង្រៀនភេសជ្ជៈ (BAVERAGE SCHOOL)"</strong> ដែលបានគូសក្នុងកិច្ចការទី១ មកដាក់បញ្ចូលក្នុងនាមប័ណ្ណទាំងសងខាង។</p>
              </div>
            </li>

            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">3</div>
              <div class="rule-content">
                <h4>ទំហំនាមប័ណ្ណ៖ 85mm &times; 50mm</h4>
                <p>នេះជាខ្នាតស្តង់ដារកាត់សម្រេច (Finished Trim Size)។</p>
              </div>
            </li>

            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">4</div>
              <div class="rule-content">
                <h4>Bleed: 3mm</h4>
                <p>ត្រូវកំណត់ Bleed <strong>3mm ជុំវិញ</strong> ទាំងបួនជ្រុង (Top, Bottom, Left, Right) ដើម្បីកុំឲ្យកាត់ឆ្វៀលសពេលកាត់ក្រដាស (Canvas សរុប 91 &times; 56 mm)។</p>
              </div>
            </li>

            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">5</div>
              <div class="rule-content">
                <h4>2 Spot Color, CMYK, RGB with NO tints or gradients</h4>
                <p>ត្រូវកំណត់ពណ៌ជា <strong>២ ពណ៌សុទ្ធ (2 Solid Inks)</strong>៖ ពណ៌ខៀវស្រស់ (Cyan/Cerulean) និងពណ៌ខៀវចាស់/ធ្យូង (Charcoal Navy)។ <strong>ហាមដាច់ខាត</strong> ការប្រើ Gradient ឬ Tint %។</p>
                <span class="badge-tag" style="background: #e0f2fe; color: #0369a1;">2 Spot Colors • 100% Solid</span>
              </div>
            </li>

            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">6</div>
              <div class="rule-content">
                <h4>ICC profile: Coated GRACoL 2006 &amp; sRGB</h4>
                <p>Coated GRACoL 2006 (ISO 12647-2:2004) សម្រាប់ Spot &amp; CMYK និង sRGB សម្រាប់ RGB Color។</p>
              </div>
            </li>

            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">7</div>
              <div class="rule-content">
                <h4>រក្សាទុកជាប្រភេទឯកសារ PDF, PNG, AI</h4>
                <p>ត្រូវ Export ឯកសារទាំង ៣ ប្រភេទនេះឲ្យបានគ្រប់ចំនួន។</p>
              </div>
            </li>

            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">8</div>
              <div class="rule-content">
                <h4>សម្លាប់ Font (Create Outline) លើអក្សរទាំងអស់</h4>
                <p>ចុច <code>Ctrl + Shift + O</code> លើ Text ទាំងអស់ដើម្បីបម្លែងជា Vector Curves មិនឲ្យបាត់ Font។</p>
              </div>
            </li>

            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">9</div>
              <div class="rule-content">
                <h4>រៀបនាមប័ណ្ណលើក្រដាស A4 ចំនួន ១០ នាមប័ណ្ណ (10-Up Imposition)</h4>
                <p>រៀបចំ layout លើក្រដាស A4 ជា ២ ជួរឈរ &times; ៥ ជួរដេក (2 Columns &times; 5 Rows) = ១០ នាមប័ណ្ណ អមដោយ Crop Marks សម្រាប់កាត់។</p>
              </div>
            </li>

            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">10</div>
              <div class="rule-content">
                <h4>បោះពុម្ពចេញក្រៅរួចកាត់បំបែកទៅជានាមប័ណ្ណ ១០ សន្លឹក</h4>
                <p>ព្រីនចេញមកក្រៅ និងកាត់តាមបន្ទាត់ Crop Marks ឲ្យចេញជានាមប័ណ្ណ ១០ សន្លឹកដាច់ៗពីគ្នា។</p>
              </div>
            </li>

            <li class="rule-item" style="border-left-color: #0284c7;">
              <div class="rule-num" style="background: #0284c7;">11</div>
              <div class="rule-content">
                <h4>បោះពុម្ពនាមប័ណ្ណ ១ សន្លឹកលើ A4 ប្រវែងជួរដេក &le; 200 mm</h4>
                <p>ពង្រីកនាមប័ណ្ណតែ ១ សន្លឹកដាក់ចំកណ្តាលក្រដាស A4 ដោយកំណត់ប្រវែងទទឹងដេក (Width) <strong>មិនលើសពី 200 mm</strong> (ឧ. 195 mm &times; 114.7 mm) សម្រាប់ដាក់តាំងបង្ហាញ (Proofing Display)។</p>
              </div>
            </li>
          </ul>
        </div>
      </div>
    </section>

    <!-- SECTION 2: VISUAL EXPLORER FOR CARD & IMPOSITION -->
    <section class="container" id="visual-explorer-2">
      <div class="section-header">
        <span class="section-tag" style="color: #0284c7;">PRE-PRESS BLUEPRINTS</span>
        <h3 class="section-title">ប្លង់វ៉ិចទ័រនាមប័ណ្ណ និងប្លង់រៀបពុម្ពលើ A4 (Vector Explorer)</h3>
        <p class="section-subtitle">
          ពិនិត្យមើលប្លង់នាមប័ណ្ណសងខាង (Front &amp; Back) និងប្លង់ Imposition ១០ សន្លឹកលើក្រដាស A4
        </p>
      </div>

      <div class="explorer-card">
        <div style="display: grid; grid-template-columns: 1fr; gap: 2rem;">
          <div>
            <h4 style="font-size: 1.1rem; color: #1e293b; font-weight: 800; margin-bottom: 0.75rem;">
              ១. គំរូប្លង់នាមប័ណ្ណសងខាង (Front &amp; Back Architecture with Bleed &amp; Crop Marks)
            </h4>
            <div style="width: 100%; max-width: 950px; margin: 0 auto; background: #f8fafc; border-radius: 12px; padding: 1rem; border: 1px solid #cbd5e1;">
              <object data="card-preview.svg" type="image/svg+xml" width="100%" height="100%"></object>
            </div>
          </div>

          <div style="margin-top: 1.5rem;">
            <h4 style="font-size: 1.1rem; color: #1e293b; font-weight: 800; margin-bottom: 0.75rem;">
              ២. ប្លង់រៀបពុម្ព ១០ សន្លឹកលើក្រដាស A4 (A4 Pre-Press Imposition Sheet — 2 &times; 5 Grid)
            </h4>
            <div style="width: 100%; max-width: 600px; margin: 0 auto; background: #f8fafc; border-radius: 12px; padding: 1rem; border: 1px solid #cbd5e1;">
              <object data="imposition-preview.svg" type="image/svg+xml" width="100%" height="100%"></object>
            </div>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 3: COLOR SYSTEM FOR PROJECT 2 -->
    <section class="container" id="color-specs-2">
      <div class="section-header">
        <span class="section-tag" style="color: #0284c7;">COLOR MANAGEMENT</span>
        <h3 class="section-title">ប្រព័ន្ធពណ៌នៃនាមប័ណ្ណ (2 Spot Colors System)</h3>
        <p class="section-subtitle">
          ប្រើប្រាស់ ២ ពណ៌សុទ្ធ (Solid Colors) គ្មាន Gradient និងគ្មាន Tint ឡើយ
        </p>
      </div>

      <div class="color-specs-grid">
        <!-- Color 1: Process Cyan -->
        <div class="color-card">
          <div class="color-swatch-banner swatch-cyan">
            <div>
              <div class="swatch-title">Process Cyan / Blue</div>
              <div style="font-size: 0.8rem; opacity: 0.9;">ពណ៌ខៀវស្រស់ (បដាឈ្មោះ &amp; រាងធរណីមាត្រ)</div>
            </div>
            <span class="swatch-badge">Spot 1</span>
          </div>
          <div class="color-details-body">
            <table class="code-table">
              <tr>
                <td class="label">Pantone (Spot):</td>
                <td class="val">PANTONE Process Cyan C <button class="copy-btn" data-code="PANTONE Process Cyan C">Copy</button></td>
              </tr>
              <tr>
                <td class="label">CMYK Mode:</td>
                <td class="val">C: 100% &nbsp; M: 25% &nbsp; Y: 0% &nbsp; K: 0% <button class="copy-btn" data-code="C:100 M:25 Y:0 K:0">Copy</button></td>
              </tr>
              <tr>
                <td class="label">RGB Mode:</td>
                <td class="val">R: 0 &nbsp; G: 143 &nbsp; B: 213 <button class="copy-btn" data-code="rgb(0, 143, 213)">Copy</button></td>
              </tr>
              <tr>
                <td class="label">HEX Code:</td>
                <td class="val">#008FD5 <button class="copy-btn" data-code="#008FD5">Copy</button></td>
              </tr>
              <tr>
                <td class="label">Rule Status:</td>
                <td class="val" style="color: var(--accent-green);">100% Solid (No Gradient/No Tint)</td>
              </tr>
            </table>
          </div>
        </div>

        <!-- Color 2: Dark Charcoal Navy -->
        <div class="color-card">
          <div class="color-swatch-banner swatch-charcoal">
            <div>
              <div class="swatch-title">Dark Charcoal Navy</div>
              <div style="font-size: 0.8rem; opacity: 0.9;">ពណ៌ខៀវក្រម៉ៅធ្យូង (Chevron &amp; Flaps)</div>
            </div>
            <span class="swatch-badge">Spot 2</span>
          </div>
          <div class="color-details-body">
            <table class="code-table">
              <tr>
                <td class="label">Pantone (Spot):</td>
                <td class="val">PANTONE 289 C <button class="copy-btn" data-code="PANTONE 289 C">Copy</button></td>
              </tr>
              <tr>
                <td class="label">CMYK Mode:</td>
                <td class="val">C: 90% &nbsp; M: 75% &nbsp; Y: 45% &nbsp; K: 55% <button class="copy-btn" data-code="C:90 M:75 Y:45 K:55">Copy</button></td>
              </tr>
              <tr>
                <td class="label">RGB Mode:</td>
                <td class="val">R: 26 &nbsp; G: 43 &nbsp; B: 73 <button class="copy-btn" data-code="rgb(26, 43, 73)">Copy</button></td>
              </tr>
              <tr>
                <td class="label">HEX Code:</td>
                <td class="val">#1A2B49 <button class="copy-btn" data-code="#1A2B49">Copy</button></td>
              </tr>
              <tr>
                <td class="label">Rule Status:</td>
                <td class="val" style="color: var(--accent-green);">100% Solid (No Gradient/No Tint)</td>
              </tr>
            </table>
          </div>
        </div>
      </div>
    </section>

    <!-- SECTION 4: STEP-BY-STEP TUTORIAL FOR BUSINESS CARD -->
    <section class="container" id="tutorial-steps-2">
      <div class="section-header">
        <span class="section-tag" style="color: #0284c7;">STEP-BY-STEP WORKFLOW</span>
        <h3 class="section-title">ជំហានអនុវត្តរចនានាមប័ណ្ណ និងប្លង់ព្រីន (Business Card Tutorial)</h3>
        <p class="section-subtitle">
          អនុវត្តតាម ១០ ជំហានបច្ចេកទេសនេះ ដើម្បីសម្រេចកិច្ចការទី២ ឲ្យបានពិន្ទុពេញ ១០០%
        </p>
      </div>

      <div class="steps-wrapper" style="max-width: 950px; margin: 0 auto;">

        <!-- Step 1 -->
        <article class="step-card">
          <div class="step-header">
            <div>
              <span class="step-phase" style="color: #0284c7;">ជំហានទី ១ • បង្កើត ARTBOARDS</span>
              <h4 class="step-heading">បង្កើតឯកសារនាមប័ណ្ណ 85 &times; 50 mm ជាមួយ Bleed 3mm (2 Artboards)</h4>
            </div>
            <span class="step-tools-badge">Ctrl + N</span>
          </div>
          <div class="step-body">
            <ul class="step-actions-list">
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">A</span>
                <div class="action-text">ចុច <strong>File &gt; New</strong> (<kbd>Ctrl</kbd> + <kbd>N</kbd>) &gt; ដាក់ឈ្មោះ <code>Business-Card-Design</code>។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">B</span>
                <div class="action-text">កំណត់ <strong>Width: 85 mm</strong>, <strong>Height: 50 mm</strong>, <strong>Units: Millimeters</strong>។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">C</span>
                <div class="action-text">ដាក់ចំនួន <strong>Number of Artboards: 2</strong> (Artboard 1: ខាងមុខ Front, Artboard 2: ខាងក្រោយ Back)។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">D</span>
                <div class="action-text">កំណត់ <strong>Bleed: 3 mm</strong> លើគ្រប់ជ្រុង (Top: 3mm, Bottom: 3mm, Left: 3mm, Right: 3mm)។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">E</span>
                <div class="action-text">Color Mode: <strong>CMYK Color</strong>, Raster Effects: <strong>High (300 ppi)</strong> រួចចុច Create។</div>
              </li>
            </ul>
          </div>
        </article>

        <!-- Step 2 -->
        <article class="step-card">
          <div class="step-header">
            <div>
              <span class="step-phase" style="color: #0284c7;">ជំហានទី ២ • SAFE MARGIN GUIDES</span>
              <h4 class="step-heading">បង្កើតបន្ទាត់សុវត្ថិភាព Safe Area (3mm ខាងក្នុង)</h4>
            </div>
            <span class="step-tools-badge">Guides &amp; Offset Path</span>
          </div>
          <div class="step-body">
            <p>ដើម្បីកុំឲ្យអក្សរ ឬ Icon ត្រូវកន្ត្រៃកាត់ចំពេលកាត់ក្រដាស ត្រូវបង្កើត Safe Margin 3mm ខាងក្នុង Trim line៖</p>
            <ul class="step-actions-list">
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">A</span>
                <div class="action-text">ប្រើ Rectangle Tool (<kbd>M</kbd>) គូសចតុកោណកែងទំហំ 85 &times; 50 mm តម្រឹមចំកណ្តាល Artboard។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">B</span>
                <div class="action-text">ចូល <strong>Object &gt; Path &gt; Offset Path...</strong> វាយតម្លៃ <strong>-3 mm</strong> &gt; ចុចស្តាំជ្រើសរើស <strong>Make Guides</strong> (<kbd>Ctrl</kbd> + <kbd>5</kbd>)។</div>
              </li>
            </ul>
          </div>
        </article>

        <!-- Step 3 -->
        <article class="step-card">
          <div class="step-header">
            <div>
              <span class="step-phase" style="color: #0284c7;">ជំហានទី ៣ • ផ្ទៃខាងមុខ (FRONT SIDE)</span>
              <h4 class="step-heading">គូសបដាឈ្មោះ (Cyan Banner) និងបន្ទាត់ឆ្នូតខាងលើ</h4>
            </div>
            <span class="step-tools-badge">Pen Tool (P)</span>
          </div>
          <div class="step-body">
            <ul class="step-actions-list">
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">A</span>
                <div class="action-text">ប្រើ <strong>Pen Tool</strong> គូសរាងពហុកោណកាត់ជ្រុងបញ្ឆិតនៅផ្នែកខាងលើឆ្វេង Fill ពណ៌ខៀវ Cyan (<code>#008FD5</code>) ដោយទាញឲ្យហៀរចេញដល់បន្ទាត់ក្រហម Bleed 3mm ខាងលើ និងខាងឆ្វេង។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">B</span>
                <div class="action-text">គូសបន្ទាត់ឆ្នូតផ្តេកតូចមួយបន្តពីគែមជ្រុងបញ្ឆិតនោះកាត់ទៅដល់គែមស្តាំ Stroke ពណ៌ Cyan 2pt។</div>
              </li>
            </ul>
          </div>
        </article>

        <!-- Step 4 -->
        <article class="step-card">
          <div class="step-header">
            <div>
              <span class="step-phase" style="color: #0284c7;">ជំហានទី ៤ • TYPOGRAPHY &amp; ព័ត៌មានទំនាក់ទំនង</span>
              <h4 class="step-heading">វាយឈ្មោះ តួនាទី លេខទូរសព្ទ អ៊ីមែល គេហទំព័រ និងអាសយដ្ឋាន</h4>
            </div>
            <span class="step-tools-badge">Type Tool (T)</span>
          </div>
          <div class="step-body">
            <ul class="step-actions-list">
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">A</span>
                <div class="action-text"><strong>ឈ្មោះ៖</strong> វាយអក្សរខ្មែរ <strong>"ហ៊ាន សុខា"</strong> (Font ក្បាលមូល ឬ Muol Light, ទំហំ 14pt, ពណ៌ស) ដាក់លើបដាខៀវ។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">B</span>
                <div class="action-text"><strong>តួនាទី៖</strong> វាយ <strong>"អ្នកគ្រប់គ្រងទូទៅ"</strong> (ទំហំ 8pt, ពណ៌សស្រាល)។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">C</span>
                <div class="action-text"><strong>ព័ត៌មានទំនាក់ទំនង៖</strong> វាយលេខទូរសព្ទ <code>+123 456 789 000</code>, អ៊ីមែល <code>yourgmail@name.com</code>, និងទីតាំង <code>123 your street name / your city, Country</code> ដាក់ពណ៌ប្រផេះក្រម៉ៅ (Font ស្អាតស្មើ 7pt)។</div>
              </li>
            </ul>
          </div>
        </article>

        <!-- Step 5 -->
        <article class="step-card">
          <div class="step-header">
            <div>
              <span class="step-phase" style="color: #0284c7;">ជំហានទី ៥ • ICONS &amp; QR CODE</span>
              <h4 class="step-heading">គូស Vector Icons ទាំង ៣ និង QR Code</h4>
            </div>
            <span class="step-tools-badge">Shape Tools</span>
          </div>
          <div class="step-body">
            <ul class="step-actions-list">
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">A</span>
                <div class="action-text">គូសកូនប្រអប់ការ៉េជ្រុងមូលពណ៌ Cyan ទំហំ <code>3.5 mm &times; 3.5 mm</code> ចំនួន ៣ &gt; គូស Icon ទូរសព្ទ, សំបុត្រ Email, និង Location Pin ពណ៌សដាក់ចំកណ្តាលប្រអប់នីមួយៗ។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">B</span>
                <div class="action-text">គូសក្រឡា QR Code វ៉ិចទ័រទំហំ <code>9 mm &times; 9 mm</code> ដោយមានប្រអប់ការ៉េ ៣ នៅជ្រុង ដាក់នៅជិតផ្នែកព័ត៌មានទំនាក់ទំនង។</div>
              </li>
            </ul>
          </div>
        </article>

        <!-- Step 6 -->
        <article class="step-card">
          <div class="step-header">
            <div>
              <span class="step-phase" style="color: #0284c7;">ជំហានទី ៦ • រូបរាងធរណីមាត្រ (ORIGAMI RIBBON FOLD)</span>
              <h4 class="step-heading">គូសផ្ទាំងធរណីមាត្របត់ពត់ (Geometric Fold) ខាងស្តាំ</h4>
            </div>
            <span class="step-tools-badge">Pen Tool &amp; Polygon</span>
          </div>
          <div class="step-body">
            <p>រូបរាងធរណីមាត្រនៅផ្នែកកណ្តាលស្តាំជាការផ្គុំគ្នានៃរាងពហុកោណបញ្ឆិត ២ ស្រទាប់៖</p>
            <ul class="step-actions-list">
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">A</span>
                <div class="action-text"><strong>ស្រទាប់លើ (Top Chevron):</strong> ប្រើ Pen Tool គូសរាង Chevron បញ្ឆិតពីគែមលើចុះមក Fill ពណ៌ខៀវក្រម៉ៅធ្យូង Dark Charcoal Navy (<code>#1A2B49</code>)។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">B</span>
                <div class="action-text"><strong>ស្រទាប់កណ្តាល (Diamond Fold):</strong> គូសរាងពេជ្របញ្ឆិតនៅកណ្តាលបន្តគ្នា Fill ពណ៌ខៀវស្រស់ Cyan (<code>#008FD5</code>)។</div>
              </li>
            </ul>
          </div>
        </article>

        <!-- Step 7 -->
        <article class="step-card">
          <div class="step-header">
            <div>
              <span class="step-phase" style="color: #0284c7;">ជំហានទី ៧ • ដាក់ LOGO ពីគម្រោងទី១</span>
              <h4 class="step-heading">បញ្ចូលនិមិត្តសញ្ញា "សាលាបង្រៀនភេសជ្ជៈ" ចូលក្នុងនាមប័ណ្ណ</h4>
            </div>
            <span class="step-tools-badge">Copy &amp; Scale</span>
          </div>
          <div class="step-body">
            <ul class="step-actions-list">
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">A</span>
                <div class="action-text">បើក File <code>Logo-CMYK.ai</code> (ពីគម្រោងទី១) &gt; Select Logo ទាំងអស់ &gt; ចុច <kbd>Ctrl</kbd> + <kbd>C</kbd> (Copy)។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">B</span>
                <div class="action-text">ត្រឡប់មកផ្ទាំងនាមប័ណ្ណ &gt; ចុច <kbd>Ctrl</kbd> + <kbd>V</kbd> (Paste) &gt; ចុច <kbd>Shift</kbd> ទាញបង្រួមសមាមាត្រឲ្យនៅទំហំអង្កត់ផ្ចិតប្រហែល <strong>18 mm</strong> ដាក់នៅផ្នែកខាងលើស្តាំនៃផ្ទៃខាងមុខ។</div>
              </li>
            </ul>
          </div>
        </article>

        <!-- Step 8 -->
        <article class="step-card">
          <div class="step-header">
            <div>
              <span class="step-phase" style="color: #0284c7;">ជំហានទី ៨ • ផ្ទៃខាងក្រោយ (BACK SIDE)</span>
              <h4 class="step-heading">រចនាផ្ទៃខាងក្រោយ (Artboard 2) ជាមួយ Logo ធំចំកណ្តាល</h4>
            </div>
            <span class="step-tools-badge">Artboard 2</span>
          </div>
          <div class="step-body">
            <ul class="step-actions-list">
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">A</span>
                <div class="action-text"><strong>ផ្ទាំងខាងលើ៖</strong> គូសរាងត្រីកោណបញ្ឆិតធំគ្របពីគែមលើចុះមកជិតកណ្តាល Fill ពណ៌ Dark Charcoal Navy (<code>#1A2B49</code>) ដោយទាញឲ្យហៀរចេញដល់ Bleed 3mm។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">B</span>
                <div class="action-text"><strong>ផ្ទាំងខាងក្រោម៖</strong> គូសរាងត្រីកោណបញ្ឆិតធំពីគែមក្រោមកាត់ឡើងលើ Fill ពណ៌ Cyan (<code>#008FD5</code>) ហៀរចេញដល់ Bleed 3mm។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">C</span>
                <div class="action-text"><strong>Logo ចំកណ្តាល៖</strong> គូសរង្វង់មូលពណ៌សមួយនៅចំកណ្តាលផ្ទាំងកាត់ &gt; ដាក់ Logo "សាលាបង្រៀនភេសជ្ជៈ" ទំហំធំល្មម (24mm) ក្នុងរង្វង់សនោះ អមដោយពាក្យស្លោក <em>"PROFESSIONAL BARISTA &amp; DRINKS ACADEMY"</em>។</div>
              </li>
            </ul>
          </div>
        </article>

        <!-- Step 9 -->
        <article class="step-card">
          <div class="step-header">
            <div>
              <span class="step-phase" style="color: #0284c7;">ជំហានទី ៩ • CREATE OUTLINE &amp; SAVING</span>
              <h4 class="step-heading">សម្លាប់ Font និងរក្សាទុកជា PDF, PNG, AI</h4>
            </div>
            <span class="step-tools-badge">Ctrl + Shift + O</span>
          </div>
          <div class="step-body">
            <ul class="step-actions-list">
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">A</span>
                <div class="action-text"><strong>Create Outline:</strong> ចុច <kbd>Ctrl</kbd> + <kbd>A</kbd> &gt; ចុច <kbd>Ctrl</kbd> + <kbd>Shift</kbd> + <kbd>O</kbd> (Type &gt; Create Outlines) លើ Artboards ទាំងពីរ។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">B</span>
                <div class="action-text"><strong>Save AI:</strong> ចូល File &gt; Save As &gt; ដាក់ឈ្មោះ <code>Business-Card.ai</code>។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">C</span>
                <div class="action-text"><strong>Save PDF:</strong> File &gt; Save As &gt; Adobe PDF &gt; Marks and Bleeds: ធិកយក <em>Use Document Bleed Settings (3mm)</em> និង <em>Trim Marks</em> &gt; Save <code>Business-Card.pdf</code>។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">D</span>
                <div class="action-text"><strong>Export PNG:</strong> File &gt; Export &gt; Export As... &gt; Format: PNG &gt; ធិកយក <em>Use Artboards</em> &gt; Resolution: High (300 ppi)។</div>
              </li>
            </ul>
          </div>
        </article>

        <!-- Step 10 -->
        <article class="step-card">
          <div class="step-header">
            <div>
              <span class="step-phase" style="color: #0284c7;">ជំហានទី ១០ • PRE-PRESS IMPOSITION &amp; 200MM PROOF</span>
              <h4 class="step-heading">រៀប ១០ នាមប័ណ្ណលើ A4 និងពង្រីកព្រីនមិនលើសពី 200mm</h4>
            </div>
            <span class="step-tools-badge">A4 Imposition Layout</span>
          </div>
          <div class="step-body">
            <p>នេះជាលក្ខខណ្ឌវិញ្ញាសាសំខាន់បំផុតផ្នែកបោះពុម្ព (Pre-Press &amp; Finishing)៖</p>
            <ul class="step-actions-list">
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">A</span>
                <div class="action-text"><strong>រៀប ១០ នាមប័ណ្ណលើ A4 (10-Up Imposition):</strong><br>
                1. បង្កើត Document ថ្មីទំហំ <strong>A4 (210 &times; 297 mm)</strong>។<br>
                2. Copy នាមប័ណ្ណសម្រេច (85 &times; 50 mm) មកដាក់លើ A4។<br>
                3. តម្រៀបជា <strong>២ ជួរឈរ &times; ៥ ជួរដេក (2 Columns &times; 5 Rows) = ១០ សន្លឹក</strong> (ទំហំសរុបនៃ Grid គឺ 170mm ទទឹង &times; 250mm កម្ពស់ ដែលស្ថិតក្នុងទំហំ A4 210&times;297mm យ៉ាងស្អាត ដោយសល់គែមសងខាង 20mm និងលើក្រោម 23.5mm)។<br>
                4. Select នាមប័ណ្ណទាំងអស់ រួចចូល <strong>Object &gt; Create Trim Marks</strong> ដើម្បីបង្កើតបន្ទាត់ Crop Marks សម្រាប់កាត់។<br>
                5. Save ជា PDF សម្រាប់ព្រីន និងកាត់បំបែកជា ១០ សន្លឹក។</div>
              </li>
              <li class="step-action-item">
                <span class="action-bullet" style="background: #e0f2fe; color: #0284c7;">B</span>
                <div class="action-text"><strong>បោះពុម្ពនាមប័ណ្ណ ១ សន្លឹកលើ A4 មិនលើសពី 200mm (Enlarged Proof):</strong><br>
                1. បង្កើត Document A4 មួយទៀត។<br>
                2. ដាក់នាមប័ណ្ណ ១ សន្លឹកចំកណ្តាល Artboard។<br>
                3. បើក Transform Panel (<kbd>Shift</kbd> + <kbd>F8</kbd>) &gt; ធិកចាក់សោ Constrain Proportions &gt; វាយតម្លៃ <strong>Width: 195 mm</strong> (តិចជាង 200mm បន្តិចតាមលក្ខខណ្ឌមិនឲ្យលើស 200mm) &rarr; Height នឹងឡើងដល់ 114.7 mm ដោយស្វ័យប្រវត្តិ។<br>
                4. តម្រឹមចំកណ្តាល Artboard Center រួច Save ជា PDF។</div>
              </li>
            </ul>
          </div>
        </article>

      </div>
    </section>

    <!-- SECTION 5: CHECKLIST FOR PROJECT 2 -->
    <section class="container" id="checklist-2">
      <div class="section-header">
        <span class="section-tag" style="color: #0284c7;">EXAM READINESS</span>
        <h3 class="section-title">តារាងផ្ទៀងផ្ទាត់លក្ខខណ្ឌគម្រោងទី២ (Business Card Checklist)</h3>
        <p class="section-subtitle">
          ផ្ទៀងផ្ទាត់គ្រប់ចំណុចទាំងអស់មុនពេល Submit ការងារទៅគណៈកម្មការ
        </p>
      </div>

      <div class="checklist-card">
        <div class="checklist-header">
          <div>
            <h4 style="font-size: 1.15rem; color: #1e293b; font-weight: 800;">កម្រិតត្រៀមខ្លួនសម្រាប់គម្រោងទី២ (Full Score 100 Pts)</h4>
            <span style="font-size: 0.85rem; color: var(--text-muted);" class="checked-count">0 / 12 Requirements</span>
          </div>
          <div style="font-weight: 800; font-size: 1.25rem; color: #0284c7;" class="progress-percent">0% Ready</div>
        </div>

        <div class="progress-track">
          <div class="progress-fill" style="background: linear-gradient(90deg, #0284c7 0%, #16a34a 100%);"></div>
        </div>

        <div class="checklist-items">
          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>1. នាមប័ណ្ណសងខាង (Front &amp; Back)</h5>
              <p>មានរចនាទាំងផ្ទៃខាងមុខ និងផ្ទៃខាងក្រោយពេញលេញ។</p>
            </div>
            <span class="checklist-points">10 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>2. ព័ត៌មានគ្រប់ជ្រុងជ្រោយ</h5>
              <p>មានឈ្មោះ (ហ៊ាន សុខា), តួនាទី (អ្នកគ្រប់គ្រងទូទៅ), លេខទូរសព្ទ, គេហទំព័រ, អ៊ីមែល និងទីតាំង។</p>
            </div>
            <span class="checklist-points">10 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>3. ដាក់ Logo ពីកិច្ចការទីមួយ</h5>
              <p>បានបញ្ចូល Logo សាលាបង្រៀនភេសជ្ជៈ ពីកិច្ចការទី១ ចូលក្នុងនាមប័ណ្ណ។</p>
            </div>
            <span class="checklist-points">10 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>4. ទំហំត្រឹមត្រូវ 85mm &times; 50mm</h5>
              <p>ខ្នាតកាត់សម្រេចគឺ 85mm ទទឹង &times; 50mm កម្ពស់។</p>
            </div>
            <span class="checklist-points">10 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>5. Bleed 3mm ជុំវិញ</h5>
              <p>បានកំណត់ Bleed 3mm គ្រប់ជ្រុងទាំងបួន និងទាញ background ហៀរដល់បន្ទាត់ក្រហម Bleed។</p>
            </div>
            <span class="checklist-points">10 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>6. 2 Spot Colors (No Tints or Gradients)</h5>
              <p>កំណត់ 2 Spot Colors (Cyan &amp; Charcoal Navy) 100% Solid គ្មាន Tint % ឬ Gradient ឡើយ។</p>
            </div>
            <span class="checklist-points">10 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>7. ICC Profile: Coated GRACoL 2006 &amp; sRGB</h5>
              <p>បានកំណត់ Profile ក្នុង Color Settings ត្រឹមត្រូវតាមស្ដង់ដារ ISO 12647-2:2004។</p>
            </div>
            <span class="checklist-points">5 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>8. សម្លាប់ Font (Create Outline) លើអក្សរទាំងអស់</h5>
              <p>បានចុច Ctrl + Shift + O បម្លែងអក្សរទាំងអស់ទៅជា Vector Paths។</p>
            </div>
            <span class="checklist-points">10 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>9. រក្សាទុកឯកសារគ្រប់ទម្រង់ (PDF, PNG, AI)</h5>
              <p>បាន Export File ជា PDF, PNG, និង AI គ្រប់ចំនួន។</p>
            </div>
            <span class="checklist-points">5 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>10. រៀបនាមប័ណ្ណ ១០ សន្លឹកលើក្រដាស A4 (Imposition)</h5>
              <p>បានរៀបចំ 10 Cards លើ A4 (2 &times; 5 Grid) អមដោយ Crop Marks សម្រាប់កាត់។</p>
            </div>
            <span class="checklist-points">10 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>11. ព្រីន និងកាត់បំបែកជា ១០ សន្លឹក</h5>
              <p>បានបោះពុម្ព និងកាត់តាមបន្ទាត់ Trim Marks ចេញជានាមប័ណ្ណ ១០ សន្លឹកស្អាតស្មើគ្នា។</p>
            </div>
            <span class="checklist-points">5 Pts</span>
          </div>

          <div class="checklist-row">
            <input type="checkbox" class="checklist-checkbox">
            <div class="checklist-label">
              <h5>12. ពង្រីកព្រីន ១ សន្លឹកលើ A4 មិនលើស 200mm</h5>
              <p>បានរៀបចំពង្រីកនាមប័ណ្ណ ១ សន្លឹកលើ A4 ដោយប្រវែងជួរដេក (Width) &le; 200 mm។</p>
            </div>
            <span class="checklist-points">5 Pts</span>
          </div>
        </div>
      </div>
    </section>

  </div>
  <!-- ==================== END PROJECT 2 ==================== -->
"""

with open("d:/Adobe Illustrator/index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Insert Project Switcher Bar right after </header>
switch_bar_html = """
  <!-- ==================== PROJECT SWITCHER BAR ==================== -->
  <div class="project-switch-bar">
    <button class="proj-tab-btn active gold-theme" data-target="project-1-wrapper">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><circle cx="12" cy="12" r="10"></circle><polyline points="12 6 12 12 16 14"></polyline></svg>
      <span>គម្រោង ១៖ ការរចនានិមិត្តសញ្ញា (Logo Design)</span>
    </button>
    <button class="proj-tab-btn" data-target="project-2-wrapper">
      <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2"><rect x="3" y="3" width="18" height="18" rx="2"></rect><line x1="3" y1="9" x2="21" y2="9"></line><line x1="9" y1="21" x2="9" y2="9"></line></svg>
      <span>គម្រោង ២៖ ការរចនានាមប័ណ្ណ (Business Card)</span>
    </button>
  </div>
"""

header_end = "</header>"
if header_end in html and "project-switch-bar" not in html:
    html = html.replace(header_end, header_end + "\n" + switch_bar_html)

# 2. Wrap Project 1 sections in <div class="project-section-wrapper active" id="project-1-wrapper">
if "id=\"project-1-wrapper\"" not in html:
    hero_start = '<section class="hero" id="hero">'
    html = html.replace(hero_start, '<div class="project-section-wrapper active" id="project-1-wrapper">\n' + hero_start)
    
    modal_start = '<!-- ==================== IMAGE MODAL ==================== -->'
    html = html.replace(modal_start, '</div><!-- END PROJECT 1 -->\n\n' + project_2_html + '\n\n' + modal_start)

with open("d:/Adobe Illustrator/index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Successfully updated index.html with Project 2!")
