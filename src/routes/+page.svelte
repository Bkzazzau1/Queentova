<svelte:head>
  <title>Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Queen Tovah Cares Foundation International advances humanitarian support, education, youth empowerment and community development with a global outlook."
  />
  <meta property="og:title" content="Queen Tovah Cares Foundation International" />
  <meta
    property="og:description"
    content="Compassion with dignity. Opportunity with purpose. It is good to be good."
  />
</svelte:head>

<script lang="ts">
  const programs = [
    {
      number: '01',
      title: 'Humanitarian Support',
      copy: 'Practical care for vulnerable people and families, with dignity at the centre of every intervention.',
      icon: 'heart'
    },
    {
      number: '02',
      title: 'Education & Scholarships',
      copy: 'Opening doors to learning for indigent students and people whose potential should not be limited by circumstance.',
      icon: 'book'
    },
    {
      number: '03',
      title: 'Youth & Sports',
      copy: 'Using sport, mentorship and shared experiences to bring young people together and strengthen communities.',
      icon: 'spark'
    },
    {
      number: '04',
      title: 'Community Development',
      copy: 'Supporting human capital and community-led progress through initiatives designed around real local needs.',
      icon: 'people'
    }
  ];

  const principles = [
    ['Global outlook', 'Service is not confined by geography; compassion should reach wherever it is genuinely needed.'],
    ['Human dignity', 'People are never reduced to statistics. Respect, care and humanity guide the work.'],
    ['Non-political service', 'The mission is humanitarian and community-focused, not driven by partisan interests.'],
    ['Opportunity', 'Support should not only relieve immediate hardship; it should help people move forward.']
  ];
</script>

<section class="hero">
  <div class="hero-orb orb-one"></div>
  <div class="hero-orb orb-two"></div>

  <div class="container hero-grid">
    <div class="hero-copy">
      <p class="eyebrow">Compassion • Dignity • Opportunity</p>
      <h1 class="display">
        Goodness that <span class="gold-text">reaches beyond</span> borders.
      </h1>
      <p class="lead">
        Queen Tovah Cares Foundation International serves vulnerable people and communities through
        humanitarian support, education, empowerment and purposeful community development.
      </p>

      <div class="hero-actions">
        <a class="btn btn-primary" href="#programs">Explore our mission <span>↗</span></a>
        <a class="btn btn-secondary" href="#founder">Meet the founder</a>
      </div>

      <div class="hero-note">
        <span class="mini-mark">QT</span>
        <div>
          <strong>Our guiding principle</strong>
          <p>“It is good to be good.”</p>
        </div>
      </div>
    </div>

    <div class="identity card" aria-label="Queen Tovah brand identity">
      <div class="identity-glow"></div>
      <div class="crown" aria-hidden="true">♛</div>
      <div class="monogram">
        <span>Q</span>
        <span class="t">T</span>
        <div class="globe">
          <i></i><i></i><i></i>
        </div>
      </div>
      <p class="identity-name">Queen Tovah</p>
      <p class="identity-sub">Cares Foundation International</p>
      <p class="motto">It is good to be good.</p>
      <span class="logo-note">Official logo artwork will sit here in production.</span>
    </div>
  </div>

  <div class="container trust-strip">
    <span>Humanitarian care</span>
    <span>Education</span>
    <span>Youth empowerment</span>
    <span>Community development</span>
    <span>Global outreach</span>
  </div>
</section>

<section class="about" id="about">
  <div class="container about-grid">
    <div>
      <p class="eyebrow">Who we are</p>
      <h2 class="section-title">Care should restore hope, dignity and possibility.</h2>
    </div>
    <div class="about-copy">
      <p>
        Queen Tovah Cares Foundation International is a philanthropic foundation founded by
        <strong>Princess Dr. Jessie Joseph</strong>. Its work is centred on people who are too often
        overlooked: widows and widowers, indigent families, the homeless, young people and communities
        needing meaningful support.
      </p>
      <p>
        The Foundation combines direct humanitarian assistance with longer-term investment in human
        potential — from scholarships and education to sports, youth engagement and community
        development.
      </p>
    </div>
  </div>
</section>

<section class="programs" id="programs">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">What we do</p>
        <h2 class="section-title">Purpose translated into action.</h2>
      </div>
      <p class="section-copy">
        Our programs are designed around a simple idea: meaningful support should meet immediate needs
        while creating pathways toward a stronger future.
      </p>
    </div>

    <div class="program-grid">
      {#each programs as program}
        <article class="program-card card">
          <div class="program-top">
            <span class="program-number">{program.number}</span>
            <span class="program-arrow">↗</span>
          </div>
          <div class="program-icon" aria-hidden="true">
            {#if program.icon === 'heart'}
              ♡
            {:else if program.icon === 'book'}
              ◫
            {:else if program.icon === 'spark'}
              ✦
            {:else}
              ◉
            {/if}
          </div>
          <h3>{program.title}</h3>
          <p>{program.copy}</p>
        </article>
      {/each}
    </div>
  </div>
</section>

<section class="impact" id="impact">
  <div class="container impact-shell">
    <div class="impact-copy">
      <p class="eyebrow">How we serve</p>
      <h2 class="section-title">Human-first by design.</h2>
      <p class="section-copy">
        The Foundation's identity is not built around charity as a transaction. It is built around
        service, inclusion, empowerment and the belief that every act of good can multiply.
      </p>
    </div>

    <div class="principles">
      {#each principles as principle, index}
        <article>
          <span>0{index + 1}</span>
          <div>
            <h3>{principle[0]}</h3>
            <p>{principle[1]}</p>
          </div>
        </article>
      {/each}
    </div>
  </div>
</section>

<section class="founder" id="founder">
  <div class="container founder-grid">
    <div class="founder-portrait card">
      <div class="portrait-frame">
        <div class="portrait-crown">♛</div>
        <span>Founder portrait</span>
      </div>
      <p>Princess Dr. Jessie Joseph</p>
    </div>

    <div class="founder-copy">
      <p class="eyebrow">Founder & vision</p>
      <h2 class="section-title">A conviction that goodness should travel.</h2>
      <p>
        Princess Dr. Jessie Joseph founded Queen Tovah Cares Foundation International with a vision of
        philanthropy that is not limited to one community or one country. The Foundation's outlook is
        global, while its work remains personal: helping people, families and communities where support
        can make a real difference.
      </p>

      <blockquote>
        <span>“</span>
        <p>It is good to be good.</p>
      </blockquote>

      <p class="strength">God is my strength.</p>
    </div>
  </div>
</section>

<section class="cta">
  <div class="container cta-card">
    <div>
      <p class="eyebrow">Stand with the mission</p>
      <h2>Good grows when people choose to participate.</h2>
    </div>
    <div class="cta-actions">
      <a class="btn btn-primary" href="mailto:info@queentovah.org">Partner with us</a>
      <a class="btn btn-secondary" href="#programs">Explore programs</a>
    </div>
  </div>
</section>

<style>
  .hero {
    position: relative;
    isolation: isolate;
    overflow: hidden;
    min-height: 100svh;
    padding: 172px 0 46px;
  }

  .hero::before {
    position: absolute;
    z-index: -3;
    inset: 0;
    background:
      linear-gradient(90deg, rgba(5, 2, 4, 0.96) 0%, rgba(5, 2, 4, 0.84) 48%, rgba(34, 10, 37, 0.74) 100%),
      radial-gradient(circle at 76% 42%, rgba(201, 151, 63, 0.14), transparent 28rem);
    content: '';
  }

  .hero-orb {
    position: absolute;
    z-index: -2;
    border-radius: 50%;
    filter: blur(30px);
    pointer-events: none;
  }

  .orb-one {
    top: 7%;
    right: 6%;
    width: 520px;
    height: 520px;
    border: 1px solid rgba(225, 189, 106, 0.2);
    box-shadow:
      0 0 120px rgba(201, 151, 63, 0.11),
      inset 0 0 120px rgba(100, 25, 111, 0.16);
  }

  .orb-two {
    bottom: 2%;
    left: -14%;
    width: 420px;
    height: 420px;
    background: rgba(100, 25, 111, 0.13);
  }

  .hero-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.15fr) minmax(360px, 0.85fr);
    align-items: center;
    gap: 70px;
  }

  .lead {
    max-width: 690px;
    margin: 30px 0 0;
    color: #d8ccd7;
    font-size: clamp(1rem, 1.4vw, 1.16rem);
  }

  .hero-actions {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    margin-top: 34px;
  }

  .hero-note {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-top: 44px;
    color: #cbbdca;
  }

  .mini-mark {
    display: grid;
    width: 42px;
    height: 42px;
    place-items: center;
    border: 1px solid rgba(225, 189, 106, 0.36);
    border-radius: 50%;
    color: var(--gold-bright);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-weight: 700;
  }

  .hero-note strong {
    display: block;
    color: #9d8f9c;
    font-size: 0.72rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  .hero-note p {
    margin: 2px 0 0;
    color: var(--champagne);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.26rem;
    font-style: italic;
  }

  .identity {
    position: relative;
    overflow: hidden;
    min-height: 560px;
    display: flex;
    align-items: center;
    flex-direction: column;
    justify-content: center;
    padding: 36px;
    border-color: rgba(225, 189, 106, 0.32);
    background:
      radial-gradient(circle at 50% 30%, rgba(225, 189, 106, 0.16), transparent 28%),
      radial-gradient(circle at 55% 52%, rgba(100, 25, 111, 0.4), transparent 42%),
      linear-gradient(145deg, rgba(57, 16, 62, 0.82), rgba(6, 2, 6, 0.94));
    box-shadow:
      0 36px 100px rgba(0, 0, 0, 0.38),
      inset 0 1px 0 rgba(255, 255, 255, 0.07);
  }

  .identity::before,
  .identity::after {
    position: absolute;
    border: 1px solid rgba(225, 189, 106, 0.12);
    border-radius: 50%;
    content: '';
  }

  .identity::before {
    width: 410px;
    height: 410px;
  }

  .identity::after {
    width: 310px;
    height: 310px;
  }

  .identity-glow {
    position: absolute;
    inset: auto 12% -12%;
    height: 180px;
    border-radius: 50%;
    background: rgba(201, 151, 63, 0.16);
    filter: blur(50px);
  }

  .crown {
    position: relative;
    z-index: 2;
    margin-bottom: -8px;
    color: var(--gold-bright);
    font-size: 3.1rem;
    filter: drop-shadow(0 6px 14px rgba(201, 151, 63, 0.22));
  }

  .monogram {
    position: relative;
    z-index: 1;
    width: 230px;
    height: 210px;
    color: transparent;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 13rem;
    font-weight: 700;
    line-height: 0.8;
    -webkit-text-stroke: 2px var(--gold-bright);
  }

  .monogram > span:first-child {
    position: absolute;
    left: -4px;
    top: 10px;
  }

  .monogram .t {
    position: absolute;
    top: 22px;
    right: 8px;
    color: rgba(100, 25, 111, 0.7);
    -webkit-text-stroke: 1px var(--gold-bright);
  }

  .globe {
    position: absolute;
    top: 74px;
    left: 43px;
    width: 88px;
    height: 88px;
    border: 1px solid rgba(240, 221, 173, 0.85);
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.04);
  }

  .globe::before,
  .globe::after,
  .globe i {
    position: absolute;
    border: 1px solid rgba(240, 221, 173, 0.44);
    border-radius: 50%;
    content: '';
  }

  .globe::before {
    inset: 7px 26px;
  }

  .globe::after {
    inset: 26px 7px;
  }

  .globe i:nth-child(1) {
    inset: 0 42px;
    border-radius: 0;
    border-width: 0 1px 0 0;
  }

  .globe i:nth-child(2) {
    inset: 42px 0;
    border-radius: 0;
    border-width: 1px 0 0;
  }

  .identity-name {
    position: relative;
    z-index: 1;
    margin: 0;
    color: var(--champagne);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 2.25rem;
    font-weight: 600;
    letter-spacing: 0.07em;
    text-transform: uppercase;
  }

  .identity-sub {
    position: relative;
    z-index: 1;
    margin: 4px 0 0;
    color: var(--gold-bright);
    font-size: 0.7rem;
    font-weight: 700;
    letter-spacing: 0.15em;
    text-align: center;
    text-transform: uppercase;
  }

  .motto {
    position: relative;
    z-index: 1;
    margin: 18px 0 0;
    color: #c7a1c9;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.2rem;
    font-style: italic;
  }

  .logo-note {
    position: absolute;
    right: 22px;
    bottom: 18px;
    left: 22px;
    color: #716170;
    font-size: 0.65rem;
    text-align: center;
  }

  .trust-strip {
    display: flex;
    flex-wrap: wrap;
    justify-content: center;
    gap: 8px 28px;
    margin-top: 70px;
    border-top: 1px solid rgba(225, 189, 106, 0.14);
    padding-top: 24px;
    color: #8f7f8e;
    font-size: 0.74rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  .trust-strip span:not(:last-child)::after {
    margin-left: 28px;
    color: var(--gold-deep);
    content: '•';
  }

  .about {
    padding: 126px 0;
    background: var(--cream);
    color: #23151f;
  }

  .about .eyebrow {
    color: #8e6020;
  }

  .about-grid {
    display: grid;
    grid-template-columns: minmax(0, 1fr) minmax(0, 0.85fr);
    gap: 90px;
  }

  .about .section-title {
    color: #2b1827;
  }

  .about-copy {
    padding-top: 34px;
    color: #5e4d59;
    font-size: 1.04rem;
  }

  .about-copy p {
    margin: 0 0 20px;
  }

  .about-copy strong {
    color: #3e203b;
  }

  .programs {
    padding: 126px 0;
    background:
      radial-gradient(circle at 90% 20%, rgba(100, 25, 111, 0.17), transparent 32rem),
      #090409;
  }

  .section-head {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 40px;
  }

  .section-head .section-copy {
    margin: 0 0 5px;
    max-width: 480px;
  }

  .program-grid {
    display: grid;
    grid-template-columns: repeat(4, 1fr);
    gap: 16px;
    margin-top: 64px;
  }

  .program-card {
    min-height: 360px;
    padding: 24px;
    transition: transform 180ms ease, border-color 180ms ease, background 180ms ease;
  }

  .program-card:hover {
    transform: translateY(-6px);
    border-color: rgba(225, 189, 106, 0.42);
    background:
      linear-gradient(145deg, rgba(100, 25, 111, 0.22), rgba(255, 255, 255, 0.018)),
      rgba(28, 9, 28, 0.72);
  }

  .program-top {
    display: flex;
    align-items: center;
    justify-content: space-between;
  }

  .program-number,
  .program-arrow {
    color: #897788;
    font-size: 0.72rem;
  }

  .program-arrow {
    color: var(--gold-bright);
    font-size: 1rem;
  }

  .program-icon {
    display: grid;
    width: 60px;
    height: 60px;
    place-items: center;
    margin-top: 72px;
    border: 1px solid rgba(225, 189, 106, 0.24);
    border-radius: 50%;
    background: rgba(201, 151, 63, 0.05);
    color: var(--gold-bright);
    font-size: 1.6rem;
  }

  .program-card h3 {
    margin: 24px 0 10px;
    color: #f3e8f1;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.65rem;
    font-weight: 600;
    line-height: 1.04;
  }

  .program-card p {
    margin: 0;
    color: #a897a7;
    font-size: 0.88rem;
  }

  .impact {
    padding: 126px 0;
    background: #120713;
  }

  .impact-shell {
    display: grid;
    grid-template-columns: minmax(0, 0.9fr) minmax(0, 1.1fr);
    gap: 80px;
    align-items: start;
  }

  .impact-copy {
    position: sticky;
    top: 130px;
  }

  .principles {
    border-top: 1px solid rgba(225, 189, 106, 0.16);
  }

  .principles article {
    display: grid;
    grid-template-columns: 54px 1fr;
    gap: 20px;
    border-bottom: 1px solid rgba(225, 189, 106, 0.13);
    padding: 28px 0;
  }

  .principles article > span {
    padding-top: 6px;
    color: var(--gold-deep);
    font-size: 0.7rem;
    font-weight: 700;
  }

  .principles h3 {
    margin: 0;
    color: var(--champagne);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.8rem;
    font-weight: 600;
  }

  .principles p {
    margin: 7px 0 0;
    color: #a897a7;
    font-size: 0.92rem;
  }

  .founder {
    padding: 126px 0;
    background: var(--ivory);
    color: #2a1926;
  }

  .founder .eyebrow {
    color: #8e6020;
  }

  .founder-grid {
    display: grid;
    grid-template-columns: minmax(320px, 0.85fr) minmax(0, 1.15fr);
    align-items: center;
    gap: 88px;
  }

  .founder-portrait {
    position: relative;
    overflow: hidden;
    min-height: 560px;
    border-color: rgba(139, 98, 35, 0.22);
    background:
      radial-gradient(circle at 52% 33%, rgba(225, 189, 106, 0.42), transparent 22%),
      linear-gradient(145deg, #3f1746, #160917);
    box-shadow: 0 30px 80px rgba(53, 28, 46, 0.22);
  }

  .portrait-frame {
    position: absolute;
    inset: 34px 34px 84px;
    display: grid;
    place-items: center;
    border: 1px solid rgba(225, 189, 106, 0.38);
    border-radius: 46% 46% 18px 18px;
    color: rgba(240, 221, 173, 0.66);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.1rem;
  }

  .portrait-crown {
    position: absolute;
    top: 38px;
    color: var(--gold-bright);
    font-size: 3.6rem;
  }

  .founder-portrait > p {
    position: absolute;
    right: 0;
    bottom: 26px;
    left: 0;
    margin: 0;
    color: var(--champagne);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.75rem;
    text-align: center;
  }

  .founder-copy .section-title {
    color: #2b1827;
  }

  .founder-copy > p:not(.eyebrow):not(.strength) {
    margin: 28px 0 0;
    color: #665561;
    font-size: 1.02rem;
  }

  blockquote {
    position: relative;
    margin: 38px 0 0;
    border-left: 1px solid #bc8b3b;
    padding: 8px 0 8px 34px;
  }

  blockquote > span {
    position: absolute;
    top: -18px;
    left: 26px;
    color: rgba(188, 139, 59, 0.2);
    font-family: Georgia, serif;
    font-size: 6rem;
  }

  blockquote p {
    position: relative;
    margin: 0;
    color: #50254f;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(2rem, 4vw, 3.2rem);
    font-style: italic;
  }

  .strength {
    margin: 16px 0 0;
    color: #8e6020;
    font-size: 0.78rem;
    font-weight: 700;
    letter-spacing: 0.12em;
    text-transform: uppercase;
  }

  .cta {
    padding: 82px 0;
    background: #080308;
  }

  .cta-card {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 40px;
    border: 1px solid rgba(225, 189, 106, 0.24);
    border-radius: 32px;
    padding: 54px;
    background:
      radial-gradient(circle at 85% 25%, rgba(225, 189, 106, 0.14), transparent 22rem),
      linear-gradient(135deg, rgba(100, 25, 111, 0.28), rgba(255, 255, 255, 0.03));
  }

  .cta-card h2 {
    max-width: 690px;
    margin: 0;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(2.5rem, 5vw, 4.5rem);
    font-weight: 600;
    line-height: 0.98;
  }

  .cta-actions {
    display: flex;
    flex-shrink: 0;
    gap: 10px;
  }

  @media (max-width: 1020px) {
    .hero-grid,
    .about-grid,
    .impact-shell,
    .founder-grid {
      grid-template-columns: 1fr;
    }

    .hero-grid {
      gap: 46px;
    }

    .identity {
      min-height: 500px;
    }

    .about-grid,
    .founder-grid {
      gap: 44px;
    }

    .about-copy {
      padding-top: 0;
    }

    .program-grid {
      grid-template-columns: repeat(2, 1fr);
    }

    .impact-copy {
      position: static;
    }

    .founder-portrait {
      min-height: 500px;
    }

    .cta-card {
      align-items: flex-start;
      flex-direction: column;
    }
  }

  @media (max-width: 700px) {
    .hero {
      padding-top: 136px;
    }

    .identity {
      min-height: 450px;
      padding: 24px;
    }

    .monogram {
      transform: scale(0.88);
    }

    .trust-strip {
      justify-content: flex-start;
    }

    .trust-strip span::after {
      display: none;
    }

    .about,
    .programs,
    .impact,
    .founder {
      padding: 88px 0;
    }

    .section-head {
      align-items: flex-start;
      flex-direction: column;
    }

    .section-head .section-copy {
      margin: 0;
    }

    .program-grid {
      grid-template-columns: 1fr;
    }

    .program-card {
      min-height: 320px;
    }

    .program-icon {
      margin-top: 44px;
    }

    .founder-portrait {
      min-height: 430px;
    }

    .cta-card {
      padding: 34px 24px;
    }

    .cta-actions {
      width: 100%;
      flex-direction: column;
    }

    .cta-actions .btn {
      width: 100%;
    }
  }
</style>
