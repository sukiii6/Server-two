from pathlib import Path
profile_img = Path('profile_image_line.txt').read_text('utf-8').strip()
new_html = """<!DOCTYPE html>
<html lang=\"en\">
<head>
  <meta charset=\"UTF-8\">
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\">
  <title>Suki | Cute Neon Profile</title>
  <style>
    :root {
      color-scheme: dark;
      --bg: #090008;
      --card: rgba(12, 4, 23, 0.92);
      --border: rgba(255, 69, 255, 0.85);
      --accent: #ff65ff;
      --accent-soft: rgba(255, 98, 255, 0.18);
      --text: #f8f1ff;
      --muted: rgba(255, 255, 255, 0.72);
    }
    * {
      margin: 0;
      padding: 0;
      box-sizing: border-box;
      font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, sans-serif;
      color: var(--text);
    }
    html, body {
      min-height: 100%;
      background: radial-gradient(circle at 20% 10%, rgba(255, 123, 255, 0.12), transparent 18%),
                  radial-gradient(circle at 85% 10%, rgba(160, 108, 255, 0.08), transparent 20%),
                  radial-gradient(circle at 50% 120%, rgba(255, 0, 178, 0.08), transparent 16%),
                  linear-gradient(180deg, #090008 0%, #11001b 100%);
      overflow-x: hidden;
    }
    body {
      position: relative;
      min-height: 100vh;
    }
    button, select, textarea {
      font: inherit;
    }
    #background {
      position: fixed;
      inset: 0;
      z-index: 0;
      pointer-events: none;
      overflow: hidden;
    }
    #background canvas {
      width: 100%;
      height: 100%;
      display: block;
    }
    .page {
      position: relative;
      z-index: 1;
      min-height: 100vh;
      display: flex;
      align-items: center;
      justify-content: center;
      padding: 24px;
      transition: opacity 0.35s ease;
    }
    .hidden {
      opacity: 0;
      pointer-events: none;
      position: absolute;
      inset: 0;
    }
    .card {
      width: min(1180px, 100%);
      background: var(--card);
      border: 1px solid rgba(255, 45, 255, 0.24);
      border-radius: 32px;
      box-shadow: 0 0 45px rgba(255, 46, 255, 0.12);
      overflow: hidden;
      position: relative;
      backdrop-filter: blur(18px);
    }
    .card::before {
      content: '';
      position: absolute;
      inset: 0;
      background: linear-gradient(145deg, rgba(255, 255, 255, 0.04), transparent 40%);
      pointer-events: none;
    }
    .hero {
      display: grid;
      grid-template-columns: 260px 1fr;
      gap: 26px;
      align-items: center;
      padding: 36px 36px 24px;
    }
    .hero-left {
      display: flex;
      flex-direction: column;
      gap: 20px;
      align-items: center;
    }
    .profile-picture {
      width: 180px;
      height: 180px;
      border-radius: 50%;
      border: 4px solid rgba(255, 64, 255, 0.9);
      box-shadow: 0 0 42px rgba(255, 84, 255, 0.35);
      object-fit: cover;
      animation: popIn 0.6s ease;
    }
    .hero-left .profile-meta {
      display: grid;
      gap: 12px;
      width: 100%;
    }
    .roles {
      display: flex;
      flex-wrap: wrap;
      gap: 10px;
      justify-content: center;
    }
    .role-pill {
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 90, 255, 0.22);
      border-radius: 999px;
      padding: 10px 14px;
      font-size: 0.88rem;
      letter-spacing: 0.06em;
      text-transform: uppercase;
      color: #fff;
    }
    .hero-right {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }
    .profile-title {
      font-size: clamp(2.4rem, 4vw, 3.5rem);
      font-weight: 800;
      line-height: 0.95;
      background: linear-gradient(135deg, #ff75ff, #d09bff);
      -webkit-background-clip: text;
      color: transparent;
    }
    .badge-row {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
    }
    .badge {
      display: inline-flex;
      align-items: center;
      gap: 8px;
      border-radius: 999px;
      padding: 10px 16px;
      border: 1px solid rgba(255, 105, 255, 0.3);
      background: rgba(255, 255, 255, 0.04);
      font-size: 0.95rem;
      color: #fff;
    }
    .about {
      color: var(--muted);
      line-height: 1.8;
      max-width: 680px;
    }
    .typewriter {
      font-size: 1rem;
      line-height: 1.7;
      letter-spacing: 0.02em;
      color: #ffebff;
      min-height: 3em;
      position: relative;
    }
    .typewriter span {
      border-right: 2px solid rgba(255, 255, 255, 0.85);
      padding-right: 4px;
      animation: blink 1.1s step-end infinite;
    }
    .social-row {
      display: flex;
      flex-wrap: wrap;
      gap: 14px;
      justify-content: center;
    }
    .social-link {
      position: relative;
      width: 58px;
      height: 58px;
      border-radius: 20px;
      display: inline-grid;
      place-items: center;
      background: rgba(255, 255, 255, 0.06);
      border: 1px solid rgba(255, 98, 255, 0.24);
      box-shadow: 0 0 18px rgba(255, 90, 255, 0.18);
      transition: transform 0.22s ease, box-shadow 0.22s ease;
      text-decoration: none;
      color: #fff;
    }
    .social-link:hover {
      transform: translateY(-3px);
      box-shadow: 0 0 28px rgba(255, 100, 255, 0.4);
    }
    .social-link svg {
      width: 28px;
      height: 28px;
    }
    .tooltip {
      position: absolute;
      left: 50%;
      bottom: 110%;
      transform: translateX(-50%);
      padding: 8px 12px;
      border-radius: 999px;
      background: linear-gradient(135deg, #ff7ff7, #ffe2ff);
      color: #2e0034;
      font-size: 0.8rem;
      white-space: nowrap;
      opacity: 0;
      pointer-events: none;
      transition: opacity 0.2s ease, transform 0.2s ease;
      box-shadow: 0 0 16px rgba(255, 105, 255, 0.18);
    }
    .icon-button:hover .tooltip,
    .social-link:hover .tooltip {
      opacity: 1;
      transform: translateX(-50%) translateY(-8px);
    }
    .section {
      padding: 28px 36px 34px;
      border-top: 1px solid rgba(255, 255, 255, 0.06);
    }
    .spotlight {
      display: grid;
      grid-template-columns: 1fr auto;
      gap: 24px;
      align-items: center;
    }
    .spotlight-card {
      position: relative;
      padding: 28px;
      border-radius: 28px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 92, 255, 0.16);
      box-shadow: inset 0 0 22px rgba(255, 70, 255, 0.08);
      overflow: hidden;
    }
    .spotlight-card::before {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at top left, rgba(255, 255, 255, 0.08), transparent 22%);
      pointer-events: none;
    }
    .spotlight-card h2 {
      font-size: 1.35rem;
      margin-bottom: 12px;
    }
    .spotlight-card p {
      color: var(--muted);
      line-height: 1.8;
    }
    .arrow-box {
      width: 96px;
      height: 96px;
      border-radius: 28px;
      border: 1px solid rgba(255, 112, 255, 0.25);
      background: linear-gradient(180deg, rgba(255, 84, 255, 0.18), rgba(255, 255, 255, 0.03));
      display: grid;
      place-items: center;
      cursor: pointer;
      position: relative;
      overflow: hidden;
      transition: transform 0.25s ease, box-shadow 0.25s ease;
      box-shadow: 0 0 28px rgba(255, 90, 255, 0.18);
    }
    .arrow-box:hover {
      transform: translateY(-4px);
      box-shadow: 0 0 36px rgba(255, 90, 255, 0.28);
    }
    .arrow-box::before {
      content: '➜';
      position: absolute;
      font-size: 3.8rem;
      color: rgba(255, 70, 255, 0.18);
      top: 10px;
      left: 16px;
    }
    .arrow-box span {
      position: relative;
      z-index: 1;
      font-size: 2rem;
      color: #ffcdfc;
    }
    .music-panel {
      display: grid;
      grid-template-columns: 1fr 320px;
      gap: 24px;
      align-items: center;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 80, 255, 0.12);
      border-radius: 28px;
      padding: 24px;
      margin-top: 16px;
    }
    .music-info {
      display: flex;
      flex-direction: column;
      gap: 18px;
    }
    .music-info label {
      color: var(--muted);
      letter-spacing: 0.08em;
      text-transform: uppercase;
      font-size: 0.8rem;
    }
    .track-select {
      outline: none;
      width: 100%;
      max-width: 380px;
      border-radius: 20px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      background: rgba(255, 255, 255, 0.06);
      padding: 14px 16px;
      color: #fff;
      appearance: none;
      cursor: pointer;
    }
    .music-controls {
      display: flex;
      gap: 16px;
      align-items: center;
      flex-wrap: wrap;
    }
    .control-button {
      border: none;
      border-radius: 18px;
      background: linear-gradient(135deg, #ff6eff, #cc83ff);
      color: #fff;
      padding: 14px 20px;
      font-weight: 700;
      cursor: pointer;
      box-shadow: 0 12px 28px rgba(255, 80, 255, 0.24);
    }
    .volume-wrap {
      display: flex;
      align-items: center;
      gap: 14px;
      min-width: 220px;
    }
    .volume-slider {
      width: 100%;
      accent-color: #ff62ff;
    }
    .visualizer-wrapper {
      width: 100%;
      min-height: 92px;
      display: grid;
      place-items: center;
    }
    #visualizer {
      width: 100%;
      height: 92px;
      border-radius: 20px;
      background: rgba(0, 0, 0, 0.18);
      border: 1px solid rgba(255, 255, 255, 0.08);
      box-shadow: inset 0 0 22px rgba(255, 255, 255, 0.04);
    }
    .bottom-icons {
      display: flex;
      flex-wrap: wrap;
      justify-content: center;
      gap: 16px;
      padding: 28px 36px 32px;
    }
    .icon-button {
      position: relative;
      width: 70px;
      height: 70px;
      border-radius: 24px;
      border: 1px solid rgba(255, 100, 255, 0.24);
      background: rgba(255, 255, 255, 0.05);
      display: grid;
      place-items: center;
      cursor: pointer;
      transition: transform 0.22s ease, box-shadow 0.22s ease;
      overflow: hidden;
    }
    .icon-button:hover {
      transform: translateY(-4px);
      box-shadow: 0 0 36px rgba(255, 86, 255, 0.3);
    }
    .icon-button svg {
      width: 28px;
      height: 28px;
      color: #fff;
    }
    .icon-button .pulse {
      position: absolute;
      inset: 0;
      border-radius: 24px;
      background: radial-gradient(circle, rgba(255, 97, 255, 0.18), transparent 45%);
      opacity: 0.7;
      animation: pulseGlow 1.8s infinite;
    }
    .icon-button.heart {
      background: linear-gradient(135deg, rgba(255, 83, 255, 0.22), rgba(255, 46, 255, 0.14));
    }
    .icon-button.promo {
      background: linear-gradient(135deg, rgba(154, 95, 255, 0.22), rgba(255, 49, 220, 0.14));
    }
    .icon-button.star {
      background: linear-gradient(135deg, rgba(255, 172, 255, 0.2), rgba(255, 55, 195, 0.14));
    }
    .icon-button .label {
      position: absolute;
      bottom: 10px;
      font-size: 0.72rem;
      color: rgba(255, 255, 255, 0.9);
      text-transform: uppercase;
      letter-spacing: 0.12em;
    }
    .page-title {
      display: inline-flex;
      align-items: center;
      gap: 10px;
      font-size: 0.85rem;
      letter-spacing: 0.16em;
      text-transform: uppercase;
      color: var(--muted);
    }
    .page-title span {
      color: #ffbeff;
    }
    .heart-page {
      display: grid;
      grid-template-columns: 1.1fr 0.9fr;
      gap: 28px;
      padding: 32px;
    }
    .heart-grid {
      display: grid;
      grid-template-columns: repeat(auto-fit, minmax(74px, 1fr));
      gap: 16px;
    }
    .heart-item {
      min-height: 86px;
      border-radius: 26px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(255, 255, 255, 0.03);
      display: grid;
      place-items: center;
      font-size: 1.8rem;
      color: #fff;
      text-shadow: 0 0 10px rgba(255, 255, 255, 0.1);
      animation: pulseHeart 3.2s ease-in-out infinite;
    }
    .heart-item:nth-child(2n) { animation-duration: 2.7s; }
    .heart-item:nth-child(3n) { animation-duration: 3.6s; }
    .custom-box {
      position: relative;
      border-radius: 28px;
      background: rgba(255, 255, 255, 0.04);
      border: 1px solid rgba(255, 96, 255, 0.16);
      padding: 28px;
      overflow: hidden;
    }
    .custom-box::before {
      content: '';
      position: absolute;
      inset: 0;
      background: radial-gradient(circle at top right, rgba(255, 255, 255, 0.08), transparent 24%);
      pointer-events: none;
    }
    .custom-box h3 {
      font-size: 1.35rem;
      margin-bottom: 18px;
    }
    .custom-box textarea {
      width: 100%;
      min-height: 170px;
      resize: vertical;
      border-radius: 22px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      background: rgba(0, 0, 0, 0.28);
      color: #fff;
      padding: 18px;
      line-height: 1.7;
      outline: none;
      font-size: 1rem;
      box-shadow: inset 0 0 16px rgba(255, 80, 255, 0.08);
    }
    .preview-card {
      margin-top: 16px;
      min-height: 208px;
      position: relative;
      border-radius: 24px;
      border: 1px solid rgba(255, 255, 255, 0.1);
      background: rgba(255, 255, 255, 0.03);
      padding: 20px;
      overflow: hidden;
    }
    .preview-card p {
      white-space: pre-wrap;
      line-height: 1.8;
      font-size: 1rem;
      color: #fff;
      position: relative;
      z-index: 1;
    }
    .falling-hearts {
      position: absolute;
      inset: 0;
      pointer-events: none;
      overflow: hidden;
    }
    .falling-hearts span {
      position: absolute;
      font-size: 1.05rem;
      opacity: 0;
      color: #fff;
      filter: drop-shadow(0 0 12px rgba(255, 110, 255, 0.75));
      animation: fall 5.5s linear infinite;
    }
    .back-arrow {
      position: absolute;
      top: 24px;
      left: 24px;
      width: 46px;
      height: 46px;
      border-radius: 16px;
      border: 1px solid rgba(255, 255, 255, 0.12);
      display: grid;
      place-items: center;
      background: rgba(0, 0, 0, 0.45);
      color: #fff;
      cursor: pointer;
      transition: transform 0.2s ease, box-shadow 0.2s ease;
      z-index: 2;
    }
    .back-arrow:hover {
      transform: translateY(-2px);
      box-shadow: 0 0 18px rgba(255, 85, 255, 0.28);
    }
    @keyframes blink {
      0%, 100% { border-color: transparent; }
      50% { border-color: rgba(255, 255, 255, 0.85); }
    }
    @keyframes pulseGlow {
      0%, 100% { transform: scale(1); box-shadow: 0 0 18px rgba(255, 91, 255, 0.22); }
      50% { transform: scale(1.06); box-shadow: 0 0 32px rgba(255, 91, 255, 0.36); }
    }
    @keyframes popIn {
      from { opacity: 0; transform: translateY(16px); }
      to { opacity: 1; transform: translateY(0); }
    }
    @keyframes pulseHeart {
      0%, 100% { transform: scale(1); }
      50% { transform: scale(1.08); }
    }
    @keyframes fall {
      0% { opacity: 0; transform: translateY(-24px); }
      10% { opacity: 1; }
      100% { opacity: 0; transform: translateY(120px); }
    }
    @media (max-width: 980px) {
      .hero { grid-template-columns: 1fr; text-align: center; }
      .hero-left, .hero-right { align-items: center; }
      .music-panel { grid-template-columns: 1fr; }
      .heart-page { grid-template-columns: 1fr; }
      .spotlight { grid-template-columns: 1fr; }
    }
    @media (max-width: 680px) {
      .card { border-radius: 24px; }
      .profile-picture { width: 150px; height: 150px; }
      .hero { padding: 24px 24px 16px; }
      .section { padding: 20px 24px 24px; }
      .bottom-icons { padding: 20px 24px 24px; gap: 12px; }
      .icon-button { width: 60px; height: 60px; border-radius: 20px; }
      .arrow-box { width: 80px; height: 80px; }
      .music-panel { padding: 20px; }
    }
  </style>
</head>
<body>
  <div id=\"background\"><canvas id=\"heart-canvas\"></canvas></div>
  <div class=\"page\" id=\"main-page\">
    <div class=\"card\">
      <div class=\"hero\">
        <div class=\"hero-left\">
          ###PROFILE_IMG###
          <div class=\"profile-meta\">
            <div class=\"page-title\"><span>Roles</span> Owner · MVP · Female · DBD · RE</div>
            <div class=\"roles\">
              <div class=\"role-pill\">Owner</div>
              <div class=\"role-pill\">MVP</div>
              <div class=\"role-pill\">Female</div>
              <div class=\"role-pill\">DBD</div>
              <div class=\"role-pill\">RE</div>
            </div>
          </div>
          <div class=\"social-row\">
            <a href=\"https://www.tiktok.com/@nekirabelle\" target=\"_blank\" class=\"social-link\">
              <svg viewBox=\"0 0 24 24\" fill=\"currentColor\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M20.4 7.2a5.93 5.93 0 0 1-3.7-1.3v8.5a5.9 5.9 0 1 1-5.9-5.9h1.9v2.1a4 4 0 1 0 4 4V7.3a7.9 7.9 0 0 1-2.1-.3v3.9a7.9 7.9 0 1 0 7.9 7.9V7.2z\"/></svg>
              <span class=\"tooltip\">TikTok</span>
            </a>
            <a href=\"https://discord.gg/nyxia\" target=\"_blank\" class=\"social-link\">
              <svg viewBox=\"0 0 24 24\" fill=\"currentColor\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M20.317 4.37a19.791 19.791 0 0 0-4.885-1.515.074.074 0 0 0-.079.037c-.21.375-.444.864-.608 1.25a18.27 18.27 0 0 0-5.487 0 12.64 12.64 0 0 0-.617-1.25.077.077 0 0 0-.079-.037A19.736 19.736 0 0 0 3.677 4.37a.07.07 0 0 0-.032.027C.533 9.046-.32 13.58.099 18.057a.082.082 0 0 0 .031.057 19.9 19.9 0 0 0 5.993 3.03.078.078 0 0 0 .084-.028c.462-.63.874-1.295 1.226-1.994a.076.076 0 0 0-.041-.106 13.107 13.107 0 0 1-1.872-.892.077.077 0 0 1-.008-.128 10.2 10.2 0 0 0 .372-.292.074.074 0 0 1 .077-.01c3.928 1.793 8.18 1.793 12.062 0a.074.074 0 0 1 .078.01c.12.098.246.198.373.292a.077.077 0 0 1-.006.127 12.299 12.299 0 0 1-1.873.892.077.077 0 0 0-.041.107c.36.698.772 1.362 1.225 1.993a.076.076 0 0 0 .084.028 19.839 19.839 0 0 0 6.002-3.03.077.077 0 0 0 .032-.054c.5-5.177-.838-9.674-3.549-13.66a.061.061 0 0 0-.031-.03zM8.02 15.33c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.956-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.956 2.418-2.157 2.418zm7.975 0c-1.183 0-2.157-1.085-2.157-2.419 0-1.333.955-2.419 2.157-2.419 1.21 0 2.176 1.096 2.157 2.42 0 1.333-.946 2.418-2.157 2.418z\"/></svg>
              <span class=\"tooltip\">Discord</span>
            </a>
            <a href=\"https://www.youtube.com/@nekirabelle\" target=\"_blank\" class=\"social-link\">
              <svg viewBox=\"0 0 24 24\" fill=\"currentColor\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M23.498 6.186a3.016 3.016 0 0 0-2.122-2.136C19.505 3.545 12 3.545 12 3.545s-7.505 0-9.377.505A3.017 3.017 0 0 0 .502 6.186C0 8.07 0 12 0 12s0 3.93.502 5.814a3.016 3.016 0 0 0 2.122 2.136c1.871.505 9.376.505 9.376.505s7.505 0 9.377-.505a3.015 3.015 0 0 0 2.122-2.136C24 15.93 24 12 24 12s0-3.93-.502-5.814zM9.545 15.568V8.432L15.818 12l-6.273 3.568z\"/></svg>
              <span class=\"tooltip\">YouTube</span>
            </a>
          </div>
        </div>
        <div class=\"hero-right\">
          <div class=\"profile-title\">NekiraBelle (Suki)</div>
          <div class=\"badge-row\">
            <span class=\"badge\">Owner</span>
            <span class=\"badge\">MVP</span>
            <span class=\"badge\">Female</span>
            <span class=\"badge\">DBD</span>
            <span class=\"badge\">RE</span>
          </div>
          <p class=\"about\">21 // Female // DBD + RE // Nyxia Staff & Content Creator // Discord: zsukiii</p>
          <div class=\"typewriter\"><span id=\"typewriter-text\"></span></div>
        </div>
      </div>
      <div class=\"section spotlight\">
        <div class=\"spotlight-card\">
          <h2>Promo spotlight</h2>
          <p>Promos are now bolder, more animated, and easier to explore. Hit the heart icon to enter the Sebastian page, or open the promo page with the arrow for a deeper glow experience.</p>
        </div>
        <button class=\"arrow-box\" id=\"promo-open-btn\"><span>→</span></button>
      </div>
      <div class=\"section music-panel\">
        <div class=\"music-info\">
          <div class=\"page-title\"><span>Sound</span> Girly playlist + visualizer</div>
          <label for=\"track-select\">Choose a track</label>
          <select id=\"track-select\" class=\"track-select\">
            <option value=\"Foo Fighters - Everlong (Lyrics).mp3\">Foo Fighters - Everlong</option>
          </select>
          <div class=\"music-controls\">
            <button class=\"control-button\" id=\"play-pause-btn\">Play</button>
            <div class=\"volume-wrap\">
              <label for=\"volume-slider\">Volume</label>
              <input id=\"volume-slider\" class=\"volume-slider\" type=\"range\" min=\"0\" max=\"1\" step=\"0.01\" value=\"0.28\" />
            </div>
          </div>
        </div>
        <div class=\"visualizer-wrapper\">
          <canvas id=\"visualizer\"></canvas>
        </div>
      </div>
      <div class=\"bottom-icons\">
        <button class=\"icon-button heart\" id=\"heart-page-btn\">
          <span class=\"pulse\"></span>
          <svg viewBox=\"0 0 24 24\" fill=\"none\" stroke=\"currentColor\" stroke-width=\"2\" stroke-linecap=\"round\" stroke-linejoin=\"round\"><path d=\"M20.84 4.61a5.5 5.5 0 0 0-7.78 0L12 5.67l-1.06-1.06a5.5 5.5 0 1 0-7.78 7.78l1.06 1.06L12 21.23l7.78-7.78 1.06-1.06a5.5 5.5 0 0 0 0-7.78z\"/></svg>
          <span class=\"tooltip\">🌈 I &lt;3 Sebastian</span>
        </button>
        <button class=\"icon-button promo\" id=\"promo-btn\">
          <span class=\"pulse\"></span>
          <svg viewBox=\"0 0 24 24\" fill=\"currentColor\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M12 3l9 18H3L12 3zm0 5.5L7.5 18h9L12 8.5z\"/></svg>
          <span class=\"tooltip\">✨ Open Promo</span>
        </button>
        <button class=\"icon-button star\" id=\"custom-text-btn\">
          <span class=\"pulse\"></span>
          <svg viewBox=\"0 0 24 24\" fill=\"currentColor\" xmlns=\"http://www.w3.org/2000/svg\"><path d=\"M12 2l2.92 6.74L22 9.27l-5 4.87L18.18 22 12 18.56 5.82 22 7 14.14 2 9.27l7.08-0.53L12 2z\"/></svg>
          <span class=\"tooltip\">💜 Edit text</span>
        </button>
      </div>
    </div>
  </div>
  <div class=\"page hidden\" id=\"promo-page\">
    <button class=\"back-arrow\" id=\"promo-back\">←</button>
    <div class=\"card\">
      <div class=\"section\">
        <div class=\"page-title\"><span>Promo</span> Cute campaign page</div>
        <h2 style=\"margin:16px 0 12px; font-size:2.1rem;\">New pink neon promo world</h2>
        <p style=\"color: var(--muted); line-height:1.85; max-width:760px;\">This promo page is designed to feel special and obvious. The button below will show how easy it is to give users a glowing, animated route to your content.</p>
      </div>
      <div class=\"section spotlight\">
        <div class=\"spotlight-card\">
          <h2>Promo power</h2>
          <p>Instead of hidden cards, this section brings a bright banner, animated highlights, and better text separation. The page is fully mobile friendly and keeps the same neon style from the main profile.</p>
          <p style=\"margin-top:16px; color: #ffcdfc;\"><strong>Suggestion:</strong> Add product cards, special launch links, or a limited-time message here.</p>
        </div>
        <div class=\"arrow-box\">
          <span>➤</span>
        </div>
      </div>
      <div class=\"section\">
        <div class=\"page-title\"><span>Links</span> Quick access</div>
        <div style=\"display:grid; gap:14px; margin-top:18px;\">
          <a href=\"https://nyxia.cc/\" target=\"_blank\" style=\"display:block; padding:18px 22px; border-radius:22px; background: rgba(255,255,255,0.04); border:1px solid rgba(255, 72, 255, 0.18); text-decoration:none; color:#fff; box-shadow: inset 0 0 20px rgba(255, 84, 255, 0.06);\">Visit Nyxia Website</a>
          <a href=\"https://discord.gg/nyxia\" target=\"_blank\" style=\"display:block; padding:18px 22px; border-radius:22px; background: rgba(255,255,255,0.04); border:1px solid rgba(255, 72, 255, 0.18); text-decoration:none; color:#fff; box-shadow: inset 0 0 20px rgba(255, 84, 255, 0.06);\">Join Nyxia Discord</a>
        </div>
      </div>
    </div>
  </div>
  <div class=\"page hidden\" id=\"heart-page\">
    <button class=\"back-arrow\" id=\"heart-back\">←</button>
    <div class=\"card\">
      <div class=\"section\">
        <div class=\"page-title\"><span>Heart</span> Sebastian page</div>
        <h2 style=\"margin:16px 0 12px; font-size:2.1rem;\">Cute heart grid with custom text</h2>
        <p style=\"color: var(--muted); line-height:1.85; max-width:760px;\">This page has white heart outlines that pulse, falling hearts in the text preview, and a live custom message box. It is made to feel charming and easy to use.</p>
      </div>
      <div class=\"heart-page\">
        <div>
          <div class=\"page-title\"><span>Grid</span> Heart outlines</div>
          <div class=\"heart-grid\">
            <div class=\"heart-item\" style=\"--i:0\">♡</div>
            <div class=\"heart-item\" style=\"--i:1\">♡</div>
            <div class=\"heart-item\" style=\"--i:2\">♡</div>
            <div class=\"heart-item\" style=\"--i:3\">♡</div>
            <div class=\"heart-item\" style=\"--i:4\">♡</div>
            <div class=\"heart-item\" style=\"--i:5\">♡</div>
            <div class=\"heart-item\" style=\"--i:6\">♡</div>
            <div class=\"heart-item\" style=\"--i:7\">♡</div>
            <div class=\"heart-item\" style=\"--i:8\">♡</div>
            <div class=\"heart-item\" style=\"--i:9\">♡</div>
            <div class=\"heart-item\" style=\"--i:10\">♡</div>
            <div class=\"heart-item\" style=\"--i:11\">♡</div>
            <div class=\"heart-item\" style=\"--i:12\">♡</div>
            <div class=\"heart-item\" style=\"--i:13\">♡</div>
            <div class=\"heart-item\" style=\"--i:14\">♡</div>
            <div class=\"heart-item\" style=\"--i:15\">♡</div>
            <div class=\"heart-item\" style=\"--i:16\">♡</div>
            <div class=\"heart-item\" style=\"--i:17\">♡</div>
          </div>
        </div>
        <div class=\"custom-box\">
          <h3>Write your own message</h3>
          <textarea id=\"custom-text\">I love you, Sebastian 💖</textarea>
          <div class=\"preview-card\">
            <div class=\"falling-hearts\" id=\"falling-hearts\"></div>
            <p id=\"preview-text\">I love you, Sebastian 💖</p>
          </div>
        </div>
      </div>
    </div>
  </div>
  <audio id=\"audio-player\" loop>
    <source src=\"Foo Fighters - Everlong (Lyrics).mp3\" type=\"audio/mp3\">
  </audio>
  <script>
    const pages = {
      main: document.getElementById('main-page'),
      promo: document.getElementById('promo-page'),
      heart: document.getElementById('heart-page')
    };
    function showPage(id) {
      Object.values(pages).forEach(page => page.classList.add('hidden'));
      pages[id].classList.remove('hidden');
    }
    document.getElementById('promo-open-btn').addEventListener('click', () => showPage('promo'));
    document.getElementById('promo-btn').addEventListener('click', () => showPage('promo'));
    document.getElementById('promo-back').addEventListener('click', () => showPage('main'));
    document.getElementById('heart-page-btn').addEventListener('click', () => showPage('heart'));
    document.getElementById('heart-back').addEventListener('click', () => showPage('main'));
    document.getElementById('custom-text-btn').addEventListener('click', () => showPage('heart'));
    const typeTexts = [
      'Sweet streamer energy with neon glow.',
      'Built for PC and mobile with a cute heart grid.',
      'Ready to customize your own promo section.'
    ];
    const typeTarget = document.getElementById('typewriter-text');
    let textIndex = 0;
    let charIndex = 0;
    function typeEffect() {
      const current = typeTexts[textIndex];
      typeTarget.textContent = current.slice(0, charIndex);
      if (charIndex < current.length) {
        charIndex += 1;
        setTimeout(typeEffect, 70);
      } else {
        setTimeout(() => {
          charIndex = 0;
          textIndex = (textIndex + 1) % typeTexts.length;
          typeEffect();
        }, 1800);
      }
    }
    typeEffect();
    const canvas = document.getElementById('heart-canvas');
    const ctx = canvas.getContext('2d');
    let hearts = [];
    function resizeCanvas() {
      canvas.width = window.innerWidth;
      canvas.height = window.innerHeight;
    }
    class Heart {
      constructor() {
        this.reset();
      }
      reset() {
        this.x = Math.random() * canvas.width;
        this.y = Math.random() * canvas.height;
        this.size = 18 + Math.random() * 42;
        this.speed = 0.2 + Math.random() * 0.45;
        this.opacity = 0.08 + Math.random() * 0.18;
        this.hue = 300 + Math.random() * 60;
        this.phase = Math.random() * Math.PI * 2;
      }
      update() {
        this.y -= this.speed;
        this.phase += 0.01;
        if (this.y < -this.size) {
          this.reset();
          this.y = canvas.height + this.size;
        }
      }
      draw() {
        ctx.save();
        ctx.translate(this.x, this.y);
        ctx.rotate(Math.sin(this.phase) * 0.15);
        ctx.font = `${this.size}px serif`;
        ctx.fillStyle = `hsla(${this.hue}, 84%, 77%, ${this.opacity})`;
        ctx.fillText('❤', 0, 0);
        ctx.restore();
      }
    }
    function initHearts() {
      hearts = Array.from({ length: 40 }, () => new Heart());
    }
    function animateHearts() {
      ctx.clearRect(0, 0, canvas.width, canvas.height);
      hearts.forEach(heart => { heart.update(); heart.draw(); });
      requestAnimationFrame(animateHearts);
    }
    window.addEventListener('resize', () => {
      resizeCanvas();
      initHearts();
    });
    resizeCanvas();
    initHearts();
    animateHearts();
    const audio = document.getElementById('audio-player');
    const playButton = document.getElementById('play-pause-btn');
    const volumeSlider = document.getElementById('volume-slider');
    const trackSelect = document.getElementById('track-select');
    const visualizer = document.getElementById('visualizer');
    const audioContext = new (window.AudioContext || window.webkitAudioContext)();
    let analyser;
    let dataArray;
    function createVisualizer() {
      if (!analyser) {
        const source = audioContext.createMediaElementSource(audio);
        analyser = audioContext.createAnalyser();
        analyser.fftSize = 128;
        source.connect(analyser);
        analyser.connect(audioContext.destination);
        dataArray = new Uint8Array(analyser.frequencyBinCount);
      }
      visualizer.width = visualizer.clientWidth * devicePixelRatio;
      visualizer.height = visualizer.clientHeight * devicePixelRatio;
      const vctx = visualizer.getContext('2d');
      vctx.setTransform(devicePixelRatio, 0, 0, devicePixelRatio, 0, 0);
      function draw() {
        requestAnimationFrame(draw);
        analyser.getByteFrequencyData(dataArray);
        vctx.clearRect(0, 0, visualizer.clientWidth, visualizer.clientHeight);
        const barCount = 22;
        const barWidth = visualizer.clientWidth / barCount - 6;
        for (let i = 0; i < barCount; i++) {
          const value = dataArray[i + 10] / 255;
          const barHeight = value * visualizer.clientHeight * 0.95;
          const x = i * (barWidth + 6);
          const y = visualizer.clientHeight - barHeight;
          const hue = 310 + i * 4;
          vctx.fillStyle = `hsl(${hue}, 98%, ${35 + value * 32}%)`;
          vctx.fillRect(x, y, barWidth, barHeight);
          vctx.fillStyle = `rgba(255,255,255,${0.18 + value * 0.24})`;
          vctx.fillRect(x, y - 6, barWidth, 4);
        }
      }
      draw();
    }
    function toggleAudio() {
      if (audio.paused) {
        audioContext.resume();
        audio.play();
        playButton.textContent = 'Pause';
      } else {
        audio.pause();
        playButton.textContent = 'Play';
      }
    }
    playButton.addEventListener('click', toggleAudio);
    volumeSlider.addEventListener('input', event => { audio.volume = event.target.value; });
    trackSelect.addEventListener('change', event => {
      const src = event.target.value;
      audio.pause();
      audio.src = src;
      audio.load();
      if (audioContext.state !== 'suspended') {
        audio.play();
        playButton.textContent = 'Pause';
      }
    });
    audio.addEventListener('play', () => {
      if (!analyser) createVisualizer();
    });
    createVisualizer();
    const customText = document.getElementById('custom-text');
    const previewText = document.getElementById('preview-text');
    const fallingHearts = document.getElementById('falling-hearts');
    function updatePreview() {
      previewText.textContent = customText.value || 'I love you, Sebastian 💖';
    }
    customText.addEventListener('input', updatePreview);
    updatePreview();
    function createFallingHearts() {
      fallingHearts.innerHTML = '';
      for (let i = 0; i < 12; i++) {
        const heart = document.createElement('span');
        heart.textContent = '❣';
        heart.style.left = `${Math.random() * 90}%`;
        heart.style.animationDuration = `${3 + Math.random() * 3}s`;
        heart.style.animationDelay = `${Math.random() * 4}s`;
        heart.style.fontSize = `${13 + Math.random() * 8}px`;
        fallingHearts.appendChild(heart);
      }
    }
    createFallingHearts();
  </script>
</body>
</html>"""
Path('index.html').write_text(new_html.replace('###PROFILE_IMG###', profile_img), encoding='utf-8')
