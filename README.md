<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>CloudCoin — Time-Based Digital Currency</title>
<link href="https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Mono:ital,wght@0,300;0,400;1,300&family=DM+Sans:ital,wght@0,300;0,400;0,500;1,300&display=swap" rel="stylesheet">
<style>
  :root {
    --sky: #0ea5e9;
    --sky-light: #38bdf8;
    --sky-dark: #0369a1;
    --cloud: #e0f2fe;
    --cloud2: #bae6fd;
    --ink: #0c1a2e;
    --ink2: #1e3a5f;
    --mist: #f0f9ff;
    --gold: #f59e0b;
    --gold-light: #fde68a;
    --mint: #10b981;
    --coral: #f43f5e;
    --white: #ffffff;
    --glass: rgba(255,255,255,0.6);
    --radius: 16px;
  }

  *, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

  html { scroll-behavior: smooth; }

  body {
    font-family: 'DM Sans', sans-serif;
    background: var(--ink);
    color: var(--white);
    overflow-x: hidden;
    line-height: 1.7;
  }

  /* ── HERO ── */
  .hero {
    min-height: 100vh;
    background:
      radial-gradient(ellipse 80% 60% at 50% -10%, rgba(14,165,233,0.45) 0%, transparent 70%),
      radial-gradient(ellipse 60% 40% at 80% 110%, rgba(16,185,129,0.2) 0%, transparent 60%),
      linear-gradient(160deg, #0c1a2e 0%, #0f2744 50%, #0c1a2e 100%);
    display: flex;
    flex-direction: column;
    align-items: center;
    justify-content: center;
    text-align: center;
    padding: 80px 24px 60px;
    position: relative;
    overflow: hidden;
  }

  .hero::before {
    content: '';
    position: absolute;
    inset: 0;
    background-image:
      radial-gradient(circle 1px at 20% 30%, rgba(56,189,248,0.5) 0%, transparent 1px),
      radial-gradient(circle 1px at 75% 20%, rgba(56,189,248,0.4) 0%, transparent 1px),
      radial-gradient(circle 1.5px at 40% 70%, rgba(56,189,248,0.3) 0%, transparent 1.5px),
      radial-gradient(circle 1px at 90% 55%, rgba(16,185,129,0.4) 0%, transparent 1px),
      radial-gradient(circle 1px at 10% 80%, rgba(56,189,248,0.3) 0%, transparent 1px),
      radial-gradient(circle 2px at 60% 15%, rgba(245,158,11,0.3) 0%, transparent 2px),
      radial-gradient(circle 1px at 85% 85%, rgba(56,189,248,0.4) 0%, transparent 1px);
    pointer-events: none;
  }

  .coin-float {
    width: 120px;
    height: 120px;
    border-radius: 50%;
    background: conic-gradient(from 0deg, #f59e0b, #fde68a, #f59e0b, #d97706, #f59e0b);
    box-shadow:
      0 0 60px rgba(245,158,11,0.5),
      0 0 120px rgba(245,158,11,0.2),
      inset 0 2px 8px rgba(255,255,255,0.4),
      inset 0 -2px 8px rgba(180,120,0,0.4);
    display: flex;
    align-items: center;
    justify-content: center;
    font-family: 'Syne', sans-serif;
    font-size: 2.4rem;
    font-weight: 800;
    color: #7c3500;
    margin-bottom: 32px;
    animation: float 4s ease-in-out infinite, spin-slow 20s linear infinite;
    position: relative;
    z-index: 1;
    text-shadow: 0 1px 2px rgba(255,255,255,0.3);
  }

  @keyframes float {
    0%, 100% { transform: translateY(0px); }
    50% { transform: translateY(-18px); }
  }

  @keyframes spin-slow {
    from { filter: hue-rotate(0deg) drop-shadow(0 0 24px rgba(245,158,11,0.6)); }
    to { filter: hue-rotate(360deg) drop-shadow(0 0 24px rgba(245,158,11,0.6)); }
  }

  .badge {
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: rgba(14,165,233,0.15);
    border: 1px solid rgba(14,165,233,0.35);
    border-radius: 100px;
    padding: 6px 16px;
    font-family: 'DM Mono', monospace;
    font-size: 0.72rem;
    letter-spacing: 0.12em;
    color: var(--sky-light);
    text-transform: uppercase;
    margin-bottom: 20px;
    backdrop-filter: blur(8px);
    position: relative;
    z-index: 1;
  }

  .hero h1 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(3rem, 9vw, 7rem);
    font-weight: 800;
    line-height: 1;
    letter-spacing: -0.02em;
    background: linear-gradient(135deg, #ffffff 0%, #bae6fd 40%, #38bdf8 100%);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    background-clip: text;
    margin-bottom: 16px;
    position: relative;
    z-index: 1;
  }

  .hero-sub {
    font-size: clamp(1rem, 2vw, 1.2rem);
    color: rgba(186,230,253,0.75);
    max-width: 520px;
    margin: 0 auto 44px;
    font-weight: 300;
    position: relative;
    z-index: 1;
  }

  .hero-stats {
    display: flex;
    gap: 32px;
    flex-wrap: wrap;
    justify-content: center;
    position: relative;
    z-index: 1;
  }

  .stat-pill {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    backdrop-filter: blur(12px);
    border-radius: 12px;
    padding: 14px 24px;
    text-align: center;
    transition: transform 0.2s, border-color 0.2s;
  }

  .stat-pill:hover {
    transform: translateY(-4px);
    border-color: rgba(14,165,233,0.4);
  }

  .stat-pill .num {
    font-family: 'Syne', sans-serif;
    font-size: 1.6rem;
    font-weight: 800;
    color: var(--sky-light);
    line-height: 1;
  }

  .stat-pill .label {
    font-size: 0.7rem;
    letter-spacing: 0.1em;
    text-transform: uppercase;
    color: rgba(186,230,253,0.6);
    margin-top: 4px;
    font-family: 'DM Mono', monospace;
  }

  /* ── MAIN CONTENT ── */
  .container {
    max-width: 960px;
    margin: 0 auto;
    padding: 0 24px;
  }

  section {
    padding: 80px 0;
  }

  .section-label {
    font-family: 'DM Mono', monospace;
    font-size: 0.68rem;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--sky);
    margin-bottom: 12px;
    display: flex;
    align-items: center;
    gap: 10px;
  }

  .section-label::after {
    content: '';
    flex: 1;
    max-width: 60px;
    height: 1px;
    background: var(--sky);
    opacity: 0.4;
  }

  h2 {
    font-family: 'Syne', sans-serif;
    font-size: clamp(1.8rem, 4vw, 2.8rem);
    font-weight: 700;
    line-height: 1.15;
    margin-bottom: 20px;
    color: var(--white);
  }

  /* ── PROBLEM / SOLUTION SPLIT ── */
  .split-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 20px;
    margin-top: 40px;
  }

  @media (max-width: 640px) { .split-grid { grid-template-columns: 1fr; } }

  .card {
    border-radius: var(--radius);
    padding: 28px;
    position: relative;
    overflow: hidden;
    transition: transform 0.2s;
  }

  .card:hover { transform: translateY(-4px); }

  .card-problem {
    background: linear-gradient(135deg, rgba(244,63,94,0.12) 0%, rgba(244,63,94,0.04) 100%);
    border: 1px solid rgba(244,63,94,0.25);
  }

  .card-solution {
    background: linear-gradient(135deg, rgba(16,185,129,0.12) 0%, rgba(16,185,129,0.04) 100%);
    border: 1px solid rgba(16,185,129,0.25);
  }

  .card h3 {
    font-family: 'Syne', sans-serif;
    font-size: 1.1rem;
    font-weight: 700;
    margin-bottom: 16px;
    display: flex;
    align-items: center;
    gap: 8px;
  }

  .card-problem h3 { color: #fb7185; }
  .card-solution h3 { color: #34d399; }

  .card ul { list-style: none; }
  .card ul li {
    font-size: 0.9rem;
    color: rgba(255,255,255,0.7);
    padding: 6px 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
    display: flex;
    gap: 10px;
    align-items: flex-start;
  }

  .card ul li::before { flex-shrink: 0; margin-top: 2px; }
  .card-problem ul li::before { content: '↘'; color: #fb7185; }
  .card-solution ul li::before { content: '↗'; color: #34d399; }

  /* ── WORKFLOW ── */
  .workflow {
    background: linear-gradient(135deg, rgba(14,165,233,0.08) 0%, rgba(3,105,161,0.05) 100%);
    border: 1px solid rgba(14,165,233,0.15);
    border-radius: 20px;
    padding: 48px 40px;
    margin-top: 40px;
    position: relative;
    overflow: hidden;
  }

  .workflow::before {
    content: '';
    position: absolute;
    top: -40px; right: -40px;
    width: 200px; height: 200px;
    border-radius: 50%;
    background: radial-gradient(circle, rgba(14,165,233,0.15), transparent 70%);
  }

  .flow-steps {
    display: flex;
    align-items: center;
    gap: 8px;
    flex-wrap: wrap;
    justify-content: center;
    margin-top: 16px;
  }

  .flow-step {
    background: rgba(255,255,255,0.06);
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: 12px;
    padding: 16px 20px;
    text-align: center;
    min-width: 120px;
    transition: all 0.2s;
  }

  .flow-step:hover {
    background: rgba(14,165,233,0.15);
    border-color: rgba(14,165,233,0.4);
    transform: translateY(-3px);
  }

  .flow-step .icon { font-size: 1.6rem; margin-bottom: 6px; }
  .flow-step .step-num {
    font-family: 'DM Mono', monospace;
    font-size: 0.6rem;
    letter-spacing: 0.15em;
    color: var(--sky);
    text-transform: uppercase;
    margin-bottom: 4px;
  }
  .flow-step .step-label {
    font-size: 0.78rem;
    font-weight: 500;
    color: rgba(255,255,255,0.85);
  }

  .flow-arrow {
    color: rgba(14,165,233,0.5);
    font-size: 1.2rem;
    flex-shrink: 0;
  }

  .equation {
    display: flex;
    align-items: center;
    justify-content: center;
    gap: 20px;
    margin: 32px 0 24px;
    flex-wrap: wrap;
  }

  .eq-part {
    font-family: 'Syne', sans-serif;
    font-size: clamp(1.2rem, 3vw, 1.8rem);
    font-weight: 700;
    padding: 12px 24px;
    border-radius: 12px;
  }

  .eq-time {
    background: rgba(14,165,233,0.2);
    border: 2px solid rgba(14,165,233,0.4);
    color: var(--sky-light);
  }

  .eq-equals {
    color: rgba(255,255,255,0.4);
    font-size: 1.6rem;
  }

  .eq-coin {
    background: rgba(245,158,11,0.2);
    border: 2px solid rgba(245,158,11,0.4);
    color: var(--gold);
  }

  /* ── FEATURES GRID ── */
  .features-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
    gap: 20px;
    margin-top: 40px;
  }

  .feature-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: var(--radius);
    padding: 28px;
    transition: all 0.2s;
    position: relative;
    overflow: hidden;
  }

  .feature-card::after {
    content: '';
    position: absolute;
    bottom: 0; left: 0; right: 0;
    height: 2px;
    background: var(--accent-color, var(--sky));
    transform: scaleX(0);
    transition: transform 0.3s;
    transform-origin: left;
  }

  .feature-card:hover::after { transform: scaleX(1); }
  .feature-card:hover {
    background: rgba(255,255,255,0.05);
    border-color: rgba(255,255,255,0.15);
    transform: translateY(-4px);
  }

  .feature-icon {
    width: 44px;
    height: 44px;
    border-radius: 12px;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.3rem;
    margin-bottom: 16px;
  }

  .feature-card h4 {
    font-family: 'Syne', sans-serif;
    font-size: 1rem;
    font-weight: 700;
    margin-bottom: 10px;
    color: var(--white);
  }

  .feature-card p {
    font-size: 0.85rem;
    color: rgba(255,255,255,0.55);
    line-height: 1.6;
  }

  /* ── TECH STACK ── */
  .tech-section {
    background: linear-gradient(135deg, rgba(255,255,255,0.03), rgba(255,255,255,0.01));
    border: 1px solid rgba(255,255,255,0.08);
    border-radius: 20px;
    padding: 40px;
    margin-top: 40px;
  }

  .tech-row {
    display: flex;
    align-items: center;
    gap: 16px;
    padding: 14px 0;
    border-bottom: 1px solid rgba(255,255,255,0.06);
  }

  .tech-row:last-child { border-bottom: none; }

  .tech-layer {
    font-family: 'DM Mono', monospace;
    font-size: 0.7rem;
    letter-spacing: 0.12em;
    text-transform: uppercase;
    color: rgba(255,255,255,0.35);
    width: 80px;
    flex-shrink: 0;
  }

  .tech-tags {
    display: flex;
    flex-wrap: wrap;
    gap: 8px;
  }

  .tech-tag {
    background: rgba(14,165,233,0.12);
    border: 1px solid rgba(14,165,233,0.25);
    border-radius: 8px;
    padding: 4px 12px;
    font-family: 'DM Mono', monospace;
    font-size: 0.75rem;
    color: var(--sky-light);
  }

  /* ── SETUP BLOCK ── */
  .code-block {
    background: #0a1628;
    border: 1px solid rgba(14,165,233,0.2);
    border-radius: var(--radius);
    padding: 28px;
    margin-top: 28px;
    position: relative;
    overflow: hidden;
  }

  .code-block::before {
    content: '● ● ●';
    display: block;
    font-size: 0.7rem;
    color: rgba(255,255,255,0.2);
    margin-bottom: 16px;
    letter-spacing: 6px;
  }

  .code-block pre {
    font-family: 'DM Mono', monospace;
    font-size: 0.82rem;
    line-height: 1.9;
    color: rgba(186,230,253,0.85);
    overflow-x: auto;
  }

  .code-block .comment { color: rgba(148,163,184,0.5); font-style: italic; }
  .code-block .cmd { color: #7dd3fc; }
  .code-block .arg { color: #a5f3fc; }
  .code-block .url { color: #6ee7b7; }

  /* ── ROADMAP ── */
  .roadmap {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 16px;
    margin-top: 40px;
  }

  .roadmap-item {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: var(--radius);
    padding: 24px;
    transition: all 0.2s;
  }

  .roadmap-item:hover {
    transform: translateY(-4px);
    border-color: rgba(14,165,233,0.3);
    background: rgba(14,165,233,0.06);
  }

  .roadmap-item .ri-icon { font-size: 1.8rem; margin-bottom: 12px; }
  .roadmap-item h4 {
    font-family: 'Syne', sans-serif;
    font-size: 0.95rem;
    font-weight: 700;
    color: var(--white);
    margin-bottom: 6px;
  }
  .roadmap-item p { font-size: 0.8rem; color: rgba(255,255,255,0.45); }

  /* ── TEAM ── */
  .team-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(180px, 1fr));
    gap: 16px;
    margin-top: 40px;
  }

  .team-card {
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: var(--radius);
    padding: 24px 20px;
    text-align: center;
    transition: all 0.2s;
  }

  .team-card:hover {
    transform: translateY(-4px);
    border-color: rgba(245,158,11,0.3);
    background: rgba(245,158,11,0.05);
  }

  .avatar {
    width: 56px;
    height: 56px;
    border-radius: 50%;
    margin: 0 auto 12px;
    font-family: 'Syne', sans-serif;
    font-weight: 800;
    font-size: 1.2rem;
    display: flex;
    align-items: center;
    justify-content: center;
    position: relative;
  }

  .avatar::after {
    content: '';
    position: absolute;
    inset: -3px;
    border-radius: 50%;
    background: conic-gradient(from 0deg, #f59e0b, #38bdf8, #10b981, #f59e0b);
    z-index: -1;
    opacity: 0.7;
  }

  .team-card .name {
    font-family: 'Syne', sans-serif;
    font-size: 0.9rem;
    font-weight: 700;
    color: var(--white);
  }

  .team-card .role {
    font-size: 0.72rem;
    color: rgba(255,255,255,0.4);
    font-family: 'DM Mono', monospace;
    margin-top: 4px;
    letter-spacing: 0.05em;
  }

  /* ── DIVIDER ── */
  .divider {
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(14,165,233,0.3), transparent);
    margin: 0 24px;
  }

  /* ── FOOTER ── */
  footer {
    text-align: center;
    padding: 60px 24px;
    position: relative;
  }

  footer::before {
    content: '';
    display: block;
    height: 1px;
    background: linear-gradient(90deg, transparent, rgba(14,165,233,0.3), transparent);
    margin-bottom: 48px;
  }

  footer p {
    font-size: 0.8rem;
    color: rgba(255,255,255,0.25);
    font-family: 'DM Mono', monospace;
  }

  .conclusion-box {
    background: linear-gradient(135deg, rgba(14,165,233,0.1) 0%, rgba(16,185,129,0.08) 100%);
    border: 1px solid rgba(14,165,233,0.2);
    border-radius: 20px;
    padding: 48px;
    text-align: center;
    margin-top: 60px;
  }

  .conclusion-box h2 {
    font-size: clamp(1.5rem, 3.5vw, 2.2rem);
    margin-bottom: 16px;
  }

  .conclusion-box p {
    color: rgba(186,230,253,0.7);
    max-width: 600px;
    margin: 0 auto;
    font-size: 1.05rem;
  }

  /* testing items */
  .test-grid {
    display: flex;
    gap: 16px;
    flex-wrap: wrap;
    margin-top: 32px;
  }

  .test-pill {
    display: flex;
    align-items: center;
    gap: 10px;
    background: rgba(16,185,129,0.1);
    border: 1px solid rgba(16,185,129,0.25);
    border-radius: 12px;
    padding: 12px 20px;
    flex: 1;
    min-width: 200px;
  }

  .test-pill .ti { font-size: 1.3rem; }
  .test-pill .tl {
    font-size: 0.85rem;
    font-weight: 500;
    color: rgba(255,255,255,0.8);
  }

  .test-pill .ts {
    font-size: 0.7rem;
    color: #34d399;
    font-family: 'DM Mono', monospace;
    letter-spacing: 0.08em;
  }

  /* results */
  .result-list {
    display: flex;
    flex-direction: column;
    gap: 12px;
    margin-top: 32px;
  }

  .result-item {
    display: flex;
    align-items: center;
    gap: 14px;
    padding: 14px 20px;
    background: rgba(255,255,255,0.03);
    border: 1px solid rgba(255,255,255,0.07);
    border-radius: 12px;
    transition: all 0.2s;
  }

  .result-item:hover { background: rgba(255,255,255,0.06); }
  .result-item::before { content: '✦'; color: var(--gold); font-size: 0.8rem; flex-shrink: 0; }
  .result-item span { font-size: 0.9rem; color: rgba(255,255,255,0.75); }

  /* references */
  .ref-list {
    display: flex;
    flex-direction: column;
    gap: 10px;
    margin-top: 32px;
  }

  .ref-item {
    display: flex;
    align-items: flex-start;
    gap: 12px;
    padding: 12px 18px;
    background: rgba(255,255,255,0.02);
    border-radius: 10px;
    font-size: 0.85rem;
    color: rgba(255,255,255,0.55);
  }

  .ref-item::before { content: '↗'; color: var(--sky); flex-shrink: 0; }
</style>
</head>
<body>

<!-- ═══════════════ HERO ═══════════════ -->
<section class="hero">
  <div class="coin-float">☁</div>
  <div class="badge">⏱ Open Source · Community Project</div>
  <h1>CloudCoin</h1>
  <p class="hero-sub">A time-based digital currency system that transforms volunteer hours into measurable, redeemable value — building stronger communities, one hour at a time.</p>
  <div class="hero-stats">
    <div class="stat-pill">
      <div class="num">1:1</div>
      <div class="label">Hour to Coin</div>
    </div>
    <div class="stat-pill">
      <div class="num">100%</div>
      <div class="label">Transparent</div>
    </div>
    <div class="stat-pill">
      <div class="num">∞</div>
      <div class="label">Scalable</div>
    </div>
    <div class="stat-pill">
      <div class="num">NGO</div>
      <div class="label">Ready</div>
    </div>
  </div>
</section>

<div class="container">

  <!-- ═══════════════ OVERVIEW ═══════════════ -->
  <section>
    <div class="section-label">01 · Overview</div>
    <h2>What is CloudCoin?</h2>
    <p style="color:rgba(255,255,255,0.6); max-width:640px; font-size:1.05rem;">
      CloudCoin is a web-based platform that converts verified volunteer time into digital currency. It provides NGOs, institutions, and community organisations with a fair, traceable, and motivating reward infrastructure.
    </p>

    <div class="equation">
      <div class="eq-part eq-time">⏱ 1 Hour of Service</div>
      <div class="eq-equals">=</div>
      <div class="eq-part eq-coin">☁ 1 CloudCoin</div>
    </div>

    <div class="split-grid">
      <div class="card card-problem">
        <h3>⚠️ The Problem</h3>
        <ul>
          <li>No recognition or tangible incentives for volunteers</li>
          <li>Volunteer hours go untracked and unverified</li>
          <li>Poor transparency makes systems untrustworthy</li>
          <li>Low motivation leads to declining participation</li>
          <li>No scalable framework for NGOs to manage rewards</li>
        </ul>
      </div>
      <div class="card card-solution">
        <h3>✅ The Solution</h3>
        <ul>
          <li>Every hour earns a verified CloudCoin</li>
          <li>Admin-verified activity logs create accountability</li>
          <li>Digital wallet offers full transaction transparency</li>
          <li>Coins redeemable for rewards, boosting motivation</li>
          <li>Scalable architecture suitable for any organisation</li>
        </ul>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══════════════ WORKFLOW ═══════════════ -->
  <section>
    <div class="section-label">02 · How It Works</div>
    <h2>Five-Step Workflow</h2>

    <div class="workflow">
      <div class="flow-steps">
        <div class="flow-step">
          <div class="icon">📋</div>
          <div class="step-num">Step 01</div>
          <div class="step-label">Register &<br>Login</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-step">
          <div class="icon">🤝</div>
          <div class="step-num">Step 02</div>
          <div class="step-label">Perform<br>Service</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-step">
          <div class="icon">🛡️</div>
          <div class="step-num">Step 03</div>
          <div class="step-label">Admin<br>Verification</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-step">
          <div class="icon">☁️</div>
          <div class="step-num">Step 04</div>
          <div class="step-label">Coins<br>Credited</div>
        </div>
        <div class="flow-arrow">→</div>
        <div class="flow-step">
          <div class="icon">🎁</div>
          <div class="step-num">Step 05</div>
          <div class="step-label">Redeem<br>Rewards</div>
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══════════════ FEATURES ═══════════════ -->
  <section>
    <div class="section-label">03 · Features</div>
    <h2>Core Modules</h2>

    <div class="features-grid">
      <div class="feature-card" style="--accent-color: #38bdf8;">
        <div class="feature-icon" style="background:rgba(56,189,248,0.15);">👤</div>
        <h4>User Module</h4>
        <p>Secure registration and login, personal wallet dashboard, complete transaction history, and a seamless coin redemption flow.</p>
      </div>
      <div class="feature-card" style="--accent-color: #f59e0b;">
        <div class="feature-icon" style="background:rgba(245,158,11,0.15);">🛠️</div>
        <h4>Admin Module</h4>
        <p>Verify volunteer hours with evidence, credit CloudCoins instantly, and manage all users and service records from one panel.</p>
      </div>
      <div class="feature-card" style="--accent-color: #10b981;">
        <div class="feature-icon" style="background:rgba(16,185,129,0.15);">💰</div>
        <h4>Wallet System</h4>
        <p>Tamper-evident CloudCoin storage, immutable transaction logs, and automatic deduction during redemption with audit trails.</p>
      </div>
      <div class="feature-card" style="--accent-color: #f43f5e;">
        <div class="feature-icon" style="background:rgba(244,63,94,0.15);">📊</div>
        <h4>Analytics &amp; Reporting</h4>
        <p>Track volunteer engagement trends, generate service reports for NGOs, and export verified hour certificates digitally.</p>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══════════════ TECH STACK ═══════════════ -->
  <section>
    <div class="section-label">04 · Tech Stack</div>
    <h2>Built With</h2>

    <div class="tech-section">
      <div class="tech-row">
        <span class="tech-layer">Frontend</span>
        <div class="tech-tags">
          <span class="tech-tag">HTML5</span>
          <span class="tech-tag">CSS3</span>
          <span class="tech-tag">JavaScript</span>
        </div>
      </div>
      <div class="tech-row">
        <span class="tech-layer">Backend</span>
        <div class="tech-tags">
          <span class="tech-tag">Python</span>
          <span class="tech-tag">Flask</span>
        </div>
      </div>
      <div class="tech-row">
        <span class="tech-layer">Database</span>
        <div class="tech-tags">
          <span class="tech-tag">MySQL</span>
          <span class="tech-tag">SQLite</span>
        </div>
      </div>
      <div class="tech-row">
        <span class="tech-layer">Tooling</span>
        <div class="tech-tags">
          <span class="tech-tag">VS Code</span>
          <span class="tech-tag">GitHub</span>
          <span class="tech-tag">XAMPP</span>
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══════════════ SETUP ═══════════════ -->
  <section>
    <div class="section-label">05 · Setup</div>
    <h2>Quick Start</h2>
    <p style="color:rgba(255,255,255,0.55); margin-bottom:8px; font-size:0.9rem;">Get CloudCoin running locally in under two minutes.</p>

    <div class="code-block">
      <pre><span class="comment"># 1 · Clone the repository</span>
<span class="cmd">git clone</span> <span class="arg">https://github.com/your-username/cloudcoin.git</span>

<span class="comment"># 2 · Enter the project directory</span>
<span class="cmd">cd</span> <span class="arg">cloudcoin</span>

<span class="comment"># 3 · Install Python dependencies</span>
<span class="cmd">pip install</span> <span class="arg">-r requirements.txt</span>

<span class="comment"># 4 · Launch the Flask development server</span>
<span class="cmd">python</span> <span class="arg">app.py</span>

<span class="comment"># 5 · Open in your browser</span>
<span class="url">http://127.0.0.1:5000/</span></pre>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══════════════ TESTING ═══════════════ -->
  <section>
    <div class="section-label">06 · Testing</div>
    <h2>Quality Assurance</h2>

    <div class="test-grid">
      <div class="test-pill">
        <span class="ti">🔬</span>
        <div>
          <div class="tl">Unit Testing</div>
          <div class="ts">✔ Passed — All individual modules</div>
        </div>
      </div>
      <div class="test-pill">
        <span class="ti">🔗</span>
        <div>
          <div class="tl">Integration Testing</div>
          <div class="ts">✔ Passed — Module interaction verified</div>
        </div>
      </div>
      <div class="test-pill">
        <span class="ti">🖥️</span>
        <div>
          <div class="tl">System Testing</div>
          <div class="ts">✔ Passed — Full workflow validated</div>
        </div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══════════════ RESULTS ═══════════════ -->
  <section>
    <div class="section-label">07 · Results</div>
    <h2>Impact &amp; Outcomes</h2>

    <div class="result-list">
      <div class="result-item"><span>Measurable increase in volunteer engagement and retention rates</span></div>
      <div class="result-item"><span>Fully transparent, auditable reward mechanism trusted by NGOs</span></div>
      <div class="result-item"><span>Efficient, real-time tracking and verification of service hours</span></div>
      <div class="result-item"><span>Scalable architecture deployable by any institution or community</span></div>
      <div class="result-item"><span>High usability scores — users reported clarity and ease of use</span></div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══════════════ ROADMAP ═══════════════ -->
  <section>
    <div class="section-label">08 · Roadmap</div>
    <h2>What's Next</h2>

    <div class="roadmap">
      <div class="roadmap-item">
        <div class="ri-icon">📱</div>
        <h4>Mobile App</h4>
        <p>Native Android &amp; iOS apps for on-the-go service logging and wallet access.</p>
      </div>
      <div class="roadmap-item">
        <div class="ri-icon">🔗</div>
        <h4>Blockchain Layer</h4>
        <p>Immutable, decentralised ledger for tamper-proof coin issuance and verification.</p>
      </div>
      <div class="roadmap-item">
        <div class="ri-icon">🏛️</div>
        <h4>NGO Integration</h4>
        <p>Official partnerships and APIs for government bodies and registered NGOs.</p>
      </div>
      <div class="roadmap-item">
        <div class="ri-icon">🛒</div>
        <h4>Marketplace</h4>
        <p>A curated catalogue where CloudCoins unlock services, certificates, and perks.</p>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══════════════ TEAM ═══════════════ -->
  <section>
    <div class="section-label">09 · Contributors</div>
    <h2>The Team</h2>

    <div class="team-grid">
      <div class="team-card">
        <div class="avatar" style="background:linear-gradient(135deg,#0ea5e9,#6366f1);">ST</div>
        <div class="name">Shravani T</div>
        <div class="role">Contributor</div>
      </div>
      <div class="team-card">
        <div class="avatar" style="background:linear-gradient(135deg,#f59e0b,#f43f5e);">RR</div>
        <div class="name">Rakshitha R</div>
        <div class="role">Contributor</div>
      </div>
      <div class="team-card">
        <div class="avatar" style="background:linear-gradient(135deg,#10b981,#0ea5e9);">SI</div>
        <div class="name">Soumya Ishwar Kambar</div>
        <div class="role">Contributor</div>
      </div>
      <div class="team-card">
        <div class="avatar" style="background:linear-gradient(135deg,#8b5cf6,#ec4899);">MR</div>
        <div class="name">Manjula R</div>
        <div class="role">Contributor</div>
      </div>
    </div>
  </section>

  <div class="divider"></div>

  <!-- ═══════════════ REFERENCES ═══════════════ -->
  <section>
    <div class="section-label">10 · References</div>
    <h2>Further Reading</h2>

    <div class="ref-list">
      <div class="ref-item">IEEE Papers on Time Banking Systems</div>
      <div class="ref-item">Flask Official Documentation — flask.palletsprojects.com</div>
      <div class="ref-item">MySQL Reference Manual — dev.mysql.com/doc</div>
      <div class="ref-item">Research on Volunteer Reward Systems &amp; Behavioural Incentives</div>
    </div>
  </section>

  <!-- ═══════════════ CONCLUSION ═══════════════ -->
  <div class="conclusion-box">
    <h2>Time has value. Now it shows. ☁</h2>
    <p>CloudCoin transforms volunteering into a measurable and rewarding experience. By assigning real value to time, it builds a fair, motivating, and scalable ecosystem for social contribution — one verified hour at a time.</p>
  </div>

</div>

<!-- ═══════════════ FOOTER ═══════════════ -->
<footer>
  <p>CloudCoin · Time-Based Digital Currency for Volunteers · Open Source</p>
  <p style="margin-top:8px;">Made with ♥ for community builders everywhere</p>
</footer>

</body>
</html>
