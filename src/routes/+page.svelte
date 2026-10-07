<svelte:head>
  <title>Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Queen Tovah Cares Foundation International advances humanitarian support, education, youth empowerment and community development with a global outlook."
  />
  <meta property="og:title" content="Queen Tovah Cares Foundation International" />
  <meta name="keywords" content="Queen Tovah Cares Foundation International, Jessie Ifeoma Udoka-Menuba, Jessie Udoka-Menuba, Princess Dr Jessie Joseph, Queen Tovah Foundation" />
  <meta
    property="og:description"
    content="Compassion with dignity. Opportunity with purpose. It is good to be good."
  />
</svelte:head>

<script lang="ts">
  let { data } = $props();

  const fallbackPrograms = [
    {
      number: '01',
      slug: 'humanitarian-support',
      title: 'Humanitarian Support',
      copy: 'Practical care for vulnerable people and families, with dignity at the centre of every intervention.',
      icon: 'heart'
    },
    {
      number: '02',
      slug: 'education-scholarships',
      title: 'Education & Scholarships',
      copy: 'Opening doors to learning for indigent students and people whose potential should not be limited by circumstance.',
      icon: 'book'
    },
    {
      number: '03',
      slug: 'youth-sports',
      title: 'Youth & Sports',
      copy: 'Using sport, mentorship and shared experiences to bring young people together and strengthen communities.',
      icon: 'spark'
    },
    {
      number: '04',
      slug: 'community-development',
      title: 'Community Development',
      copy: 'Supporting human capital and community-led progress through initiatives designed around real local needs.',
      icon: 'people'
    }
  ];

  const programs = $derived(data.programs.length
    ? data.programs.slice(0, 4).map((program, index) => ({
        number: String(index + 1).padStart(2, '0'),
        slug: program.slug,
        title: program.title,
        copy: program.summary,
        icon: program.icon || 'people'
      }))
    : fallbackPrograms);

  const featuredCampaign = $derived(data.campaigns.find((campaign) => campaign.featured) ?? data.campaigns[0] ?? null);
  const nextEvent = $derived(data.events[0] ?? null);
  const featuredScholarship = $derived(data.scholarships.find((item) => item.application_status === 'open') ?? data.scholarships[0] ?? null);
  const latestStories = $derived(data.stories.slice(0, 3));
  const visiblePartners = $derived(data.partners.slice(0, 6));
  const homepageSpotlights = $derived(data.spotlights.slice(0, 2));

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
        <a class="btn btn-primary" href="/programs">Explore our mission <span>↗</span></a>
        <a class="btn btn-secondary" href="/about#founder">Meet the founder</a>
      </div>

      <div class="hero-note">
        <span class="mini-mark">QT</span>
        <div>
          <strong>Our guiding principle</strong>
          <p>“It is good to be good.”</p>
        </div>
      </div>
    </div>

    <div class="identity card" aria-label="Queen Tovah Cares Foundation International">
      <div class="identity-glow"></div>
      <img
        class="official-logo"
        src="/brand/queentova.png"
        alt="Queen Tovah Cares Foundation International logo"
        width="1536"
        height="1024"
      />
      <div class="identity-caption">
        <span>Global humanitarian service</span>
      </div>
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


{#if homepageSpotlights.length}
<section class="curated-spotlights" aria-label="Featured Foundation updates">
  <div class="container">
    <div class="spotlight-heading">
      <div>
        <p class="eyebrow">Selected by the Foundation</p>
        <h2 class="section-title">What deserves your attention now.</h2>
      </div>
      <p>
        This area is curated from the Foundation administration system and can be scheduled without
        changing the website code.
      </p>
    </div>

    <div class:single={homepageSpotlights.length === 1} class="spotlight-grid">
      {#each homepageSpotlights as spotlight, index}
        <article class:primary={index === 0} class:with-image={Boolean(spotlight.image)} class:campaign={spotlight.style === 'campaign'} class:opportunity={spotlight.style === 'opportunity'}>
          {#if spotlight.image}
            <img src={spotlight.image} alt={spotlight.image_alt || spotlight.title} loading={index === 0 ? 'eager' : 'lazy'} />
          {/if}
          <div class="spotlight-shade"></div>
          <div class="spotlight-content">
            <span>{spotlight.eyebrow || (spotlight.style === 'impact' ? 'Impact' : spotlight.style === 'campaign' ? 'Featured cause' : spotlight.style === 'opportunity' ? 'Opportunity' : 'Featured')}</span>
            <h3>{spotlight.title}</h3>
            <p>{spotlight.summary}</p>
            <div class="spotlight-actions">
              <a class="spotlight-primary" href={spotlight.link_url}>{spotlight.link_label || 'Explore'} ↗</a>
              {#if spotlight.secondary_url && spotlight.secondary_label}
                <a class="spotlight-secondary" href={spotlight.secondary_url}>{spotlight.secondary_label}</a>
              {/if}
            </div>
          </div>
        </article>
      {/each}
    </div>
  </div>
</section>
{/if}

<section class="about" id="about">
  <div class="container about-grid">
    <div>
      <p class="eyebrow">Who we are</p>
      <h2 class="section-title">Care should restore hope, dignity and possibility.</h2>
    </div>
    <div class="about-copy">
      <p>
        Queen Tovah Cares Foundation International is a philanthropic foundation founded by
        <strong>Princess Dr. Jessie Joseph</strong>. Official public coverage of the Foundation also identifies
        <strong>Princess Dr. Jessie Ifeoma Udoka-Menuba (née Oliobi)</strong> as Founder/CEO. Until the
        Foundation formally confirms how these names should be presented together, the website keeps
        the public-record name visible for discoverability without replacing the primary founder name
        supplied for the site. Its work is centred on people who are too often
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
        <a class="program-card card" href={`/programs/${program.slug}`}>
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
        </a>
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

<section class="mission-live">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">The mission, live</p>
        <h2 class="section-title">More ways to take part.</h2>
      </div>
      <p class="section-copy">Causes, events and opportunities to stand with the Foundation's work.</p>
    </div>

    <div class="live-grid">
      {#if featuredCampaign}
        <a class="live-card campaign-card" href={`/causes/${featuredCampaign.slug}`}>
          <span class="live-label">Featured cause</span>
          <div>
            <h3>{featuredCampaign.title}</h3>
            <p>{featuredCampaign.summary}</p>
          </div>
          <span class="live-action">Explore cause ↗</span>
        </a>
      {:else}
        <a class="live-card campaign-card" href="/donate">
          <span class="live-label">Support the mission</span>
          <div>
            <h3>Help goodness travel further.</h3>
            <p>Give, sponsor or partner with the Foundation through verified channels.</p>
          </div>
          <span class="live-action">Ways to support ↗</span>
        </a>
      {/if}

      {#if nextEvent}
        <a class="live-card event-card" href={`/events/${nextEvent.slug}`}>
          <span class="live-label">Foundation event</span>
          <div>
            <small>{new Intl.DateTimeFormat('en', { dateStyle:'medium' }).format(new Date(nextEvent.starts_at))}</small>
            <h3>{nextEvent.title}</h3>
            <p>{nextEvent.city || nextEvent.country || nextEvent.summary}</p>
          </div>
          <span class="live-action">Event details ↗</span>
        </a>
      {:else}
        <a class="live-card" href="/request-support">
          <span class="live-label">Request support</span>
          <div>
            <h3>Reach out when help is needed.</h3>
            <p>Individuals, families and communities can ask the Foundation for humanitarian support.</p>
          </div>
          <span class="live-action">Request support ↗</span>
        </a>
      {/if}

      {#if featuredScholarship}
        <a class="live-card scholarship-card" href={`/scholarships/${featuredScholarship.slug}`}>
          <span class="live-label">{featuredScholarship.application_status === 'open' ? 'Applications open' : 'Scholarship'}</span>
          <div>
            <h3>{featuredScholarship.title}</h3>
            <p>{featuredScholarship.summary}</p>
          </div>
          <span class="live-action">View opportunity ↗</span>
        </a>
      {:else}
        <a class="live-card scholarship-card" href="/scholarships">
          <span class="live-label">Education</span>
          <div>
            <h3>Scholarships that open doors.</h3>
            <p>See how the Foundation supports indigent students and announces new opportunities.</p>
          </div>
          <span class="live-action">Explore scholarships ↗</span>
        </a>
      {/if}

      <a class="live-card involved-card" href="/get-involved">
        <span class="live-label">Participate</span>
        <div>
          <h3>Bring your time, skills or partnership.</h3>
          <p>Volunteer, collaborate or stay connected to work that matters.</p>
        </div>
        <span class="live-action">Get involved ↗</span>
      </a>
    </div>
  </div>
</section>

{#if latestStories.length}
<section class="latest-stories">
  <div class="container">
    <div class="section-head stories-head">
      <div>
        <p class="eyebrow">Stories & updates</p>
        <h2 class="section-title">The work behind the words.</h2>
      </div>
      <a class="view-all" href="/news">View all stories ↗</a>
    </div>

    <div class="story-preview-grid">
      {#each latestStories as story, index}
        <a class:lead-story={index === 0} class="story-preview" href={`/news/${story.slug}`}>
          {#if story.hero_image}<img src={story.hero_image} alt={story.hero_alt || story.title} loading="lazy" />{/if}
          <div class="story-shade"></div>
          <div class="story-info">
            <span>{story.category.replace('-', ' ')}</span>
            <h3>{story.title}</h3>
            <p>{story.excerpt}</p>
          </div>
        </a>
      {/each}
    </div>
  </div>
</section>
{/if}

{#if visiblePartners.length}
<section class="partners">
  <div class="container">
    <div class="partner-head">
      <div>
        <p class="eyebrow">Verified collaboration</p>
        <h2>Institutions connected to the mission.</h2>
      </div>
      <a href="/partners">View partner directory ↗</a>
    </div>
    <div class="partner-row">
      {#each visiblePartners as partner}
        <a href={`/partners/${partner.slug}`} aria-label={`View verified partner profile for ${partner.title}`}>
          {#if partner.logo}
            <img src={partner.logo} alt={partner.title} />
          {:else}
            <span>{partner.title}</span>
          {/if}
          <small>✓ Verified</small>
        </a>
      {/each}
    </div>
  </div>
</section>
{/if}

<section class="founder" id="founder">
  <div class="container founder-grid">
    <div class="founder-portrait card">
      <div class="portrait-frame">
        <img
          class="portrait-photo"
          src="/brand/queen.png"
          alt="Princess Dr. Jessie Joseph, Founder of Queen Tovah Cares Foundation International"
          width="941"
          height="1671"
          loading="lazy"
        />
      </div>
      <p>Princess Dr. Jessie Joseph</p>
    </div>

    <div class="founder-copy">
      <p class="eyebrow">Founder & vision</p>
      <h2 class="section-title">A conviction that goodness should travel.</h2>
      <p class="public-name">Publicly reported as <a href="/founder/jessie-ifeoma-udoka-menuba">Princess Dr. Jessie Ifeoma Udoka-Menuba (née Oliobi)</a>, Founder/CEO of Queen-Tovah Cares Foundation International.</p>
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
      <a class="btn btn-primary" href="/contact">Partner with us</a>
      <a class="btn btn-secondary" href="/programs">Explore programs</a>
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
    border-color: rgba(225, 189, 106, 0.55);
    background:
      radial-gradient(circle at 50% 42%, #fffaf2 0%, #fbf1dc 46%, #efdcb0 100%);
    box-shadow:
      0 36px 100px rgba(0, 0, 0, 0.45),
      0 0 0 6px rgba(225, 189, 106, 0.08),
      inset 0 1px 0 rgba(255, 255, 255, 0.6);
  }

  .identity::before,
  .identity::after {
    position: absolute;
    border: 1px solid rgba(139, 98, 35, 0.16);
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
    background: rgba(201, 151, 63, 0.22);
    filter: blur(50px);
  }

  .official-logo {
    position: relative;
    z-index: 2;
    width: min(100%, 400px);
    height: auto;
  }

  .identity-caption {
    position: relative;
    z-index: 2;
    display: grid;
    gap: 4px;
    margin-top: 24px;
    text-align: center;
  }

  .identity-caption span {
    color: #8b6223;
    font-size: 0.72rem;
    font-weight: 700;
    letter-spacing: 0.13em;
    text-transform: uppercase;
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


  .curated-spotlights {
    padding: 92px 0;
    background: #0a040a;
  }

  .spotlight-heading {
    display: grid;
    grid-template-columns: 1fr .72fr;
    align-items: end;
    gap: 70px;
    margin-bottom: 42px;
  }

  .spotlight-heading .section-title {
    max-width: 780px;
  }

  .spotlight-heading > p {
    margin: 0 0 6px;
    color: #aa9aa8;
  }

  .spotlight-grid {
    display: grid;
    grid-template-columns: 1.35fr .85fr;
    min-height: 520px;
    gap: 16px;
  }

  .spotlight-grid.single {
    grid-template-columns: 1fr;
  }

  .spotlight-grid article {
    position: relative;
    isolation: isolate;
    overflow: hidden;
    min-height: 520px;
    display: flex;
    align-items: flex-end;
    border: 1px solid rgba(225, 189, 106, .18);
    border-radius: 30px;
    padding: 34px;
    background:
      radial-gradient(circle at 72% 20%, rgba(225, 189, 106, .17), transparent 18rem),
      linear-gradient(145deg, #4d1554, #100611);
    box-shadow: 0 28px 70px rgba(0, 0, 0, .22);
  }

  .spotlight-grid article:not(.primary) {
    min-height: 520px;
    background:
      radial-gradient(circle at 72% 20%, rgba(225, 189, 106, .10), transparent 16rem),
      linear-gradient(145deg, #29102d, #0e060f);
  }

  .spotlight-grid article.campaign {
    background:
      radial-gradient(circle at 78% 18%, rgba(225, 189, 106, .20), transparent 18rem),
      linear-gradient(145deg, #5a2d13, #170a08);
  }

  .spotlight-grid article.opportunity {
    background:
      radial-gradient(circle at 80% 18%, rgba(225, 189, 106, .18), transparent 17rem),
      linear-gradient(145deg, #39143f, #0c0812);
  }

  .spotlight-grid article img {
    position: absolute;
    z-index: -3;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .spotlight-shade {
    position: absolute;
    z-index: -2;
    inset: 0;
    background: linear-gradient(0deg, rgba(7, 2, 7, .94), rgba(7, 2, 7, .14) 72%);
  }

  .spotlight-grid article:not(.with-image) .spotlight-shade {
    background: linear-gradient(0deg, rgba(7, 2, 7, .52), transparent 72%);
  }

  .spotlight-content {
    max-width: 720px;
  }

  .spotlight-content > span {
    display: inline-block;
    margin-bottom: 12px;
    color: var(--gold-bright);
    font-size: .68rem;
    font-weight: 800;
    letter-spacing: .11em;
    text-transform: uppercase;
  }

  .spotlight-content h3 {
    margin: 0;
    color: var(--ivory);
    font: 600 clamp(2.4rem, 4.8vw, 4.4rem)/.94 'Cormorant Garamond', Georgia, serif;
    letter-spacing: -.025em;
  }

  .spotlight-grid article:not(.primary) .spotlight-content h3 {
    font-size: clamp(2.1rem, 3.6vw, 3.15rem);
  }

  .spotlight-content p {
    max-width: 650px;
    margin: 16px 0 0;
    color: #c7bac5;
  }

  .spotlight-actions {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 12px 20px;
    margin-top: 25px;
  }

  .spotlight-primary {
    border-radius: 999px;
    padding: 10px 15px;
    background: linear-gradient(135deg, var(--gold-bright), var(--gold));
    color: #180b17;
    font-size: .78rem;
    font-weight: 800;
  }

  .spotlight-secondary {
    color: var(--champagne);
    font-size: .78rem;
    font-weight: 700;
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


  .mission-live {
    padding: 126px 0;
    background: var(--ivory);
    color: #2a1926;
  }

  .mission-live .eyebrow,
  .latest-stories .eyebrow,
  .partners .eyebrow {
    color: #8e6020;
  }

  .mission-live .section-title {
    color: #321c2f;
  }

  .mission-live .section-copy {
    color: #6d5b68;
  }

  .live-grid {
    display: grid;
    grid-template-columns: repeat(2, 1fr);
    gap: 16px;
    margin-top: 54px;
  }

  .live-card {
    position: relative;
    overflow: hidden;
    min-height: 330px;
    display: flex;
    justify-content: space-between;
    flex-direction: column;
    border: 1px solid rgba(80,45,70,.13);
    border-radius: 28px;
    padding: 28px;
    background: #fff;
    transition: transform .2s ease, box-shadow .2s ease;
  }

  .live-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 22px 55px rgba(55,26,49,.1);
  }

  .campaign-card,
  .involved-card {
    background:
      radial-gradient(circle at 84% 15%, rgba(225,189,106,.16), transparent 18rem),
      linear-gradient(145deg, #4c1553, #150817);
    color: var(--ivory);
  }

  .live-label {
    width: fit-content;
    border: 1px solid rgba(139,98,35,.2);
    border-radius: 999px;
    padding: 7px 10px;
    color: #9a6d2b;
    font-size: .68rem;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .campaign-card .live-label,
  .involved-card .live-label {
    border-color: rgba(225,189,106,.25);
    color: var(--gold-bright);
  }

  .live-card h3 {
    max-width: 620px;
    margin: 0;
    color: #43213f;
    font: 600 clamp(2rem,4vw,3.15rem)/.98 'Cormorant Garamond', Georgia, serif;
  }

  .campaign-card h3,
  .involved-card h3 {
    color: var(--champagne);
  }

  .live-card p {
    max-width: 620px;
    margin: 12px 0 0;
    color: #6e5c69;
  }

  .campaign-card p,
  .involved-card p {
    color: #b6a5b4;
  }

  .live-card small {
    display: block;
    margin-bottom: 7px;
    color: #9a6d2b;
    font-size: .75rem;
    font-weight: 700;
  }

  .live-action {
    color: #8e6020;
    font-size: .78rem;
    font-weight: 800;
  }

  .campaign-card .live-action,
  .involved-card .live-action {
    color: var(--gold-bright);
  }

  .latest-stories {
    padding: 126px 0;
    background: #090409;
  }

  .stories-head {
    align-items: end;
  }

  .view-all {
    color: var(--gold-bright);
    font-size: .82rem;
    font-weight: 700;
  }

  .story-preview-grid {
    display: grid;
    grid-template-columns: 1.3fr .85fr;
    grid-template-rows: 260px 260px;
    gap: 16px;
    margin-top: 54px;
  }

  .story-preview {
    position: relative;
    isolation: isolate;
    overflow: hidden;
    border: 1px solid rgba(225,189,106,.16);
    border-radius: 26px;
    background: linear-gradient(145deg,#4c1553,#150817);
  }

  .story-preview.lead-story {
    grid-row: 1 / 3;
  }

  .story-preview img {
    position: absolute;
    z-index: -2;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
  }

  .story-shade {
    position: absolute;
    z-index: -1;
    inset: 0;
    background: linear-gradient(0deg, rgba(7,2,7,.94), rgba(7,2,7,.12) 70%);
  }

  .story-info {
    position: absolute;
    right: 26px;
    bottom: 26px;
    left: 26px;
  }

  .story-info > span {
    color: var(--gold-bright);
    font-size: .68rem;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .story-info h3 {
    margin: 7px 0 8px;
    color: var(--ivory);
    font: 600 1.8rem/1 'Cormorant Garamond', Georgia, serif;
  }

  .lead-story .story-info h3 {
    font-size: clamp(2.4rem,4vw,3.6rem);
  }

  .story-info p {
    max-width: 650px;
    margin: 0;
    color: #c5b8c3;
    font-size: .84rem;
  }

  .partners {
    padding: 62px 0;
    border-top: 1px solid rgba(80,45,70,.1);
    background: var(--cream);
    color: #2b1827;
  }

  .partner-head {
    display: flex;
    align-items: end;
    justify-content: space-between;
    gap: 34px;
  }

  .partner-head h2 {
    margin: 0;
    color: #3c2238;
    font: 600 clamp(2rem,4vw,3.1rem)/.98 'Cormorant Garamond', Georgia, serif;
  }

  .partner-head > a {
    color: #8e6020;
    font-size: .8rem;
    font-weight: 700;
  }

  .partner-row {
    display: grid;
    grid-template-columns: repeat(6, 1fr);
    gap: 12px;
    margin-top: 20px;
  }

  .partner-row a {
    position: relative;
    min-height: 96px;
    display: grid;
    place-items: center;
    border: 1px solid rgba(80,45,70,.1);
    border-radius: 16px;
    padding: 14px;
    background: rgba(255,255,255,.5);
    color: #6d5b68;
    font-size: .78rem;
    font-weight: 700;
    text-align: center;
  }

  .partner-row img {
    max-width: 100%;
    max-height: 46px;
    object-fit: contain;
  }

  .partner-row small {
    position: absolute;
    right: 8px;
    bottom: 7px;
    color: #668060;
    font-size: .58rem;
    font-weight: 800;
    letter-spacing: .04em;
    text-transform: uppercase;
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
    overflow: hidden;
    color: rgba(240, 221, 173, 0.66);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1.1rem;
  }

  .portrait-photo {
    position: absolute;
    inset: 0;
    width: 100%;
    height: 100%;
    object-fit: cover;
    object-position: 50% 12%;
    border-radius: inherit;
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

  .public-name {
    margin: 18px 0 0;
    color: #8e6020;
    font-size: 0.88rem;
  }

  .public-name a {
    text-decoration: underline;
    text-underline-offset: 3px;
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

    .partner-row {
      grid-template-columns: repeat(3, 1fr);
    }

    .partner-head {
      align-items: flex-start;
      flex-direction: column;
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

    .live-grid,
    .story-preview-grid {
      grid-template-columns: 1fr;
      grid-template-rows: auto;
    }

    .story-preview,
    .story-preview.lead-story {
      grid-row: auto;
      min-height: 330px;
    }

    .partner-row {
      grid-template-columns: repeat(2, 1fr);
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
