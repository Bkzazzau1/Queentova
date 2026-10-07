<svelte:head>
  <title>Stories of Impact | Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Human stories from Queen Tovah Cares Foundation International, published only with consent and privacy review."
  />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();

  const featured = $derived(data.stories.find((story) => story.featured) ?? data.stories[0] ?? null);
  const remaining = $derived(featured
    ? data.stories.filter((story) => story.slug !== featured.slug)
    : []);

  const labels: Record<string, string> = {
    humanitarian: 'Humanitarian support',
    education: 'Education & scholarships',
    youth: 'Youth & sports',
    community: 'Community development',
    livelihood: 'Livelihood & empowerment',
    other: 'Foundation impact'
  };
</script>

<PageHero
  eyebrow="Stories of impact"
  title="Human stories,"
  accent="shared with dignity."
  copy="Every story on this page is published only after consent and privacy review. Identity, photographs and quotations are shown only to the extent approved for public use."
/>

<section class="consent-standard">
  <div class="container standard-grid">
    <div>
      <p class="eyebrow">Our publishing standard</p>
      <h2 class="section-title">A person is never content first.</h2>
    </div>
    <div class="standards">
      <span><i>01</i>Story consent required</span>
      <span><i>02</i>Separate photo consent</span>
      <span><i>03</i>Separate quote consent</span>
      <span><i>04</i>Guardian consent for minors</span>
      <span><i>05</i>Consent can be withdrawn</span>
      <span><i>06</i>Privacy review before publication</span>
    </div>
  </div>
</section>

<section class="stories">
  <div class="container">
    {#if featured}
      <article class="featured">
        <div class="featured-media">
          {#if featured.image}
            <img src={featured.image} alt={featured.image_alt || featured.title} />
          {:else}
            <div class="protected-visual">
              <span>QT</span>
              <small>Identity protected by design</small>
            </div>
          {/if}
          <div class="consent-badge">Shared with consent</div>
        </div>

        <div class="featured-copy">
          <span class="category">{labels[featured.program_area] || 'Impact story'}</span>
          <h2><a href={`/impact-stories/${featured.slug}`}>{featured.title}</a></h2>
          <p>{featured.excerpt}</p>

          <div class="identity-row">
            <span>{featured.public_name}</span>
            {#if featured.location_label}<span>{featured.location_label}</span>{/if}
          </div>

          {#if featured.quote}
            <blockquote>
              <p>“{featured.quote}”</p>
              <cite>{featured.quote_attribution || featured.public_name}</cite>
            </blockquote>
          {/if}

          <a class="read" href={`/impact-stories/${featured.slug}`}>Read this story ↗</a>
        </div>
      </article>

      {#if remaining.length}
        <div class="story-grid">
          {#each remaining as story}
            <a href={`/impact-stories/${story.slug}`}>
              <div class="media">
                {#if story.image}
                  <img src={story.image} alt={story.image_alt || story.title} loading="lazy" />
                {:else}
                  <div class="protected-small"><span>QT</span></div>
                {/if}
              </div>
              <div class="body">
                <span>{labels[story.program_area] || 'Impact story'}</span>
                <h3>{story.title}</h3>
                <p>{story.excerpt}</p>
                <small>{story.public_name}{story.location_label ? ` • ${story.location_label}` : ''}</small>
              </div>
            </a>
          {/each}
        </div>
      {/if}
    {:else}
      <div class="empty card">
        <span class="mark">QT</span>
        <h2>No beneficiary story is published until consent is complete.</h2>
        <p>
          This page intentionally stays empty rather than filling the website with invented testimonials
          or stories that have not passed the Foundation's consent and privacy review.
        </p>
        <a class="btn btn-primary" href="/impact">Explore verified impact reporting</a>
      </div>
    {/if}
  </div>
</section>

<section class="privacy">
  <div class="container privacy-card">
    <div>
      <p class="eyebrow">Consent is not permanent ownership</p>
      <h2>A person can withdraw permission to share their story.</h2>
      <p>
        When consent is withdrawn in the Foundation administration system, the story is removed from the
        public impact-story API and unpublished from this website.
      </p>
    </div>
    <a class="btn btn-secondary" href="/governance">Governance & transparency</a>
  </div>
</section>

<style>
  .consent-standard{padding:92px 0;background:var(--ivory);color:#2b1827}
  .standard-grid{display:grid;grid-template-columns:.82fr 1.18fr;gap:78px;align-items:start}
  .consent-standard .eyebrow{color:#8e6020}
  .consent-standard .section-title{color:#351e32}
  .standards{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid rgba(80,45,70,.13)}
  .standards span{display:flex;align-items:center;gap:14px;border-bottom:1px solid rgba(80,45,70,.13);padding:18px 0;color:#5f4e5a;font-size:.88rem}
  .standards span:nth-child(odd){padding-right:22px}
  .standards span:nth-child(even){border-left:1px solid rgba(80,45,70,.13);padding-left:22px}
  .standards i{color:#9b6c29;font-size:.68rem;font-style:normal;font-weight:800}

  .stories{padding:112px 0 120px;background:#0a040a}
  .featured{display:grid;grid-template-columns:1.05fr .95fr;overflow:hidden;border:1px solid rgba(225,189,106,.18);border-radius:32px;background:#100711}
  .featured-media{position:relative;min-height:600px}
  .featured-media img{width:100%;height:100%;object-fit:cover;position:absolute;inset:0}
  .protected-visual{height:100%;min-height:600px;display:grid;place-items:center;align-content:center;gap:12px;background:radial-gradient(circle at 60% 28%,rgba(225,189,106,.17),transparent 19rem),linear-gradient(145deg,#4b1552,#110712)}
  .protected-visual span{color:var(--gold-bright);font:600 6rem/1 'Cormorant Garamond',Georgia,serif}
  .protected-visual small{color:#aa9aa8;text-transform:uppercase;letter-spacing:.09em}
  .consent-badge{position:absolute;top:22px;left:22px;border:1px solid rgba(255,255,255,.2);border-radius:999px;padding:8px 12px;background:rgba(7,2,7,.62);backdrop-filter:blur(9px);color:var(--champagne);font-size:.67rem;font-weight:800;letter-spacing:.06em;text-transform:uppercase}
  .featured-copy{padding:52px}
  .category{color:var(--gold-bright);font-size:.68rem;font-weight:800;letter-spacing:.08em;text-transform:uppercase}
  .featured-copy h2{margin:18px 0 14px;color:var(--ivory);font:600 clamp(2.7rem,5vw,4.8rem)/.94 'Cormorant Garamond',Georgia,serif}
  .featured-copy h2 a:hover{color:var(--gold-bright)}
  .featured-copy>p{color:#b8a9b6}
  .identity-row{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:24px;color:#998797;font-size:.76rem;text-transform:uppercase;letter-spacing:.05em}
  blockquote{margin:34px 0 0;border-left:2px solid var(--gold-deep);padding-left:20px}
  blockquote p{margin:0;color:var(--champagne);font:italic 600 1.6rem/1.2 'Cormorant Garamond',Georgia,serif}
  blockquote cite{display:block;margin-top:9px;color:#9d8d9a;font-size:.72rem;font-style:normal}
  .read{display:inline-block;margin-top:34px;color:var(--gold-bright);font-size:.8rem;font-weight:800}

  .story-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:24px}
  .story-grid>a{overflow:hidden;border:1px solid rgba(225,189,106,.14);border-radius:24px;background:rgba(255,255,255,.035)}
  .media{height:240px;background:linear-gradient(145deg,#4b1552,#110712)}
  .media img{width:100%;height:100%;object-fit:cover}
  .protected-small{height:100%;display:grid;place-items:center;color:var(--gold-bright);font:600 3rem/1 'Cormorant Garamond',Georgia,serif}
  .body{padding:23px}
  .body>span{color:var(--gold-deep);font-size:.66rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em}
  .body h3{margin:12px 0 9px;color:var(--champagne);font:600 1.75rem/1 'Cormorant Garamond',Georgia,serif}
  .body p{margin:0;color:#aa9aa8;font-size:.84rem}
  .body small{display:block;margin-top:18px;color:#897886}

  .empty{max-width:780px;margin:auto;border-color:rgba(225,189,106,.18);padding:68px;background:rgba(255,255,255,.035);text-align:center}
  .mark{display:grid;width:66px;height:66px;place-items:center;margin:auto;border:1px solid rgba(225,189,106,.28);border-radius:50%;color:var(--gold-bright);font:600 1.4rem/1 'Cormorant Garamond',Georgia,serif}
  .empty h2{margin:28px 0 12px;color:var(--ivory);font:600 2.6rem/1 'Cormorant Garamond',Georgia,serif}
  .empty p{max-width:650px;margin:0 auto;color:#aa9aa8}
  .empty .btn{margin-top:28px}

  .privacy{padding:88px 0;background:var(--cream);color:#2b1827}
  .privacy-card{display:flex;align-items:end;justify-content:space-between;gap:48px;border:1px solid rgba(80,45,70,.12);border-radius:30px;padding:46px;background:#fff}
  .privacy-card .eyebrow{color:#8e6020}
  .privacy-card h2{max-width:800px;margin:0;color:#40213b;font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .privacy-card p:not(.eyebrow){max-width:720px;color:#6d5b68}
  .privacy-card .btn{flex-shrink:0;border-color:rgba(80,45,70,.2);color:#4c3548}

  @media(max-width:900px){
    .standard-grid,.featured{grid-template-columns:1fr}
    .featured-media,.protected-visual{min-height:420px}
    .story-grid{grid-template-columns:1fr 1fr}
    .privacy-card{align-items:flex-start;flex-direction:column}
  }
  @media(max-width:620px){
    .standards{grid-template-columns:1fr}
    .standards span:nth-child(odd),.standards span:nth-child(even){border-left:0;padding:16px 0}
    .story-grid{grid-template-columns:1fr}
    .featured-copy{padding:34px 24px}
    .empty{padding:46px 24px}
  }
</style>
