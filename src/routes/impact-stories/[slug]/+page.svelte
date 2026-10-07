<script lang="ts">
  import { page } from '$app/state';
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();
  const { story } = $derived(data);

  const labels: Record<string, string> = {
    humanitarian: 'Humanitarian support',
    education: 'Education & scholarships',
    youth: 'Youth & sports',
    community: 'Community development',
    livelihood: 'Livelihood & empowerment',
    other: 'Foundation impact'
  };

  const articleSchema = $derived(
    JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'Article',
      headline: story.title,
      description: story.excerpt,
      url: `${page.url.origin}${page.url.pathname}`,
      ...(story.image ? { image: story.image } : {}),
      ...(story.published_at ? { datePublished: story.published_at } : {}),
      publisher: {
        '@type': 'NGO',
        name: 'Queen Tovah Cares Foundation International',
        logo: {
          '@type': 'ImageObject',
          url: `${page.url.origin}/brand/queentova.png`
        }
      }
    }).replace(/</g, '\\u003c')
  );
</script>

<svelte:head>
  <title>{story.seo_title || story.title} | Queen Tovah Stories of Impact</title>
  <meta name="description" content={story.seo_description || story.excerpt} />
  {#if story.seo_keywords}<meta name="keywords" content={story.seo_keywords} />{/if}
  <meta property="og:title" content={story.seo_title || story.title} />
  <meta property="og:description" content={story.seo_description || story.excerpt} />
  {#if story.image}<meta property="og:image" content={story.image} />{/if}
  <meta property="og:type" content="article" />
  {@html `<script type="application/ld+json">${articleSchema}</script>`}
</svelte:head>

<PageHero
  eyebrow={labels[story.program_area] || 'Story of impact'}
  title={story.title}
  copy={story.excerpt}
/>

<section class="story-detail">
  <div class="container story-shell">
    <aside class="identity card">
      <div class="identity-visual">
        {#if story.image}
          <img src={story.image} alt={story.image_alt || story.title} />
        {:else}
          <span>QT</span>
          <small>No public photograph</small>
        {/if}
      </div>

      <div class="identity-copy">
        <span class="consent">Shared with consent</span>
        <h2>{story.public_name}</h2>
        {#if story.location_label}<p>{story.location_label}</p>{/if}
        {#if story.age_group !== 'not-stated'}<p>{story.age_group.replace('-', ' ')}</p>{/if}
      </div>
    </aside>

    <article>
      <div class="privacy-note">
        <span>Privacy standard</span>
        <p>
          Only the identity details, image and quotations approved for public use are displayed on this page.
          Internal consent records are never exposed through the public website.
        </p>
      </div>

      <div class="body">
        {#each story.body.split('\n\n').filter(Boolean) as paragraph}
          <p>{paragraph}</p>
        {/each}
      </div>

      {#if story.quote}
        <blockquote>
          <p>“{story.quote}”</p>
          <cite>{story.quote_attribution || story.public_name}</cite>
        </blockquote>
      {/if}

      <div class="story-footer">
        <a href="/impact-stories">← All stories of impact</a>
        <a href="/impact">Impact & accountability ↗</a>
      </div>
    </article>
  </div>
</section>

<section class="consent-reminder">
  <div class="container consent-card">
    <div>
      <p class="eyebrow">Dignity remains part of the story</p>
      <h2>Consent can be withdrawn.</h2>
      <p>
        The Foundation's publishing controls are designed so a story can be removed from public view
        when consent is withdrawn.
      </p>
    </div>
    <a class="btn btn-secondary" href="/governance">Read our governance approach</a>
  </div>
</section>

<style>
  .story-detail{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .story-shell{display:grid;grid-template-columns:330px minmax(0,1fr);gap:72px;align-items:start}
  .identity{position:sticky;top:122px;overflow:hidden;border-color:rgba(80,45,70,.13);background:#fff;color:#3d2039}
  .identity-visual{height:360px;display:grid;place-items:center;background:radial-gradient(circle at 60% 26%,rgba(225,189,106,.2),transparent 13rem),linear-gradient(145deg,#4c1553,#150817);color:var(--gold-bright)}
  .identity-visual img{width:100%;height:100%;object-fit:cover}
  .identity-visual>span{font:600 4rem/1 'Cormorant Garamond',Georgia,serif}
  .identity-visual>small{position:absolute;margin-top:90px;color:#b09fac;text-transform:uppercase;letter-spacing:.07em;font-size:.65rem}
  .identity-copy{padding:22px}
  .consent{display:inline-block;border:1px solid rgba(91,130,86,.25);border-radius:999px;padding:6px 9px;background:rgba(91,130,86,.07);color:#587252;font-size:.64rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em}
  .identity-copy h2{margin:18px 0 6px;color:#43213f;font:600 2rem/1 'Cormorant Garamond',Georgia,serif}
  .identity-copy p{margin:4px 0;color:#806f7b;font-size:.78rem;text-transform:capitalize}
  .privacy-note{border:1px solid rgba(166,112,37,.18);border-radius:18px;padding:18px 20px;background:#fff9ef}
  .privacy-note span{color:#9b6c29;font-size:.68rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em}
  .privacy-note p{margin:7px 0 0;color:#6b5966;font-size:.84rem}
  .body{margin-top:38px;color:#5f4e5a;font-size:1.07rem;line-height:1.9}
  .body p{margin:0 0 26px}
  blockquote{margin:44px 0;border-left:3px solid #b27d30;padding:12px 0 12px 26px}
  blockquote p{margin:0;color:#4b2a46;font:italic 600 clamp(2rem,4vw,3.2rem)/1.08 'Cormorant Garamond',Georgia,serif}
  blockquote cite{display:block;margin-top:12px;color:#8b7685;font-size:.76rem;font-style:normal}
  .story-footer{display:flex;justify-content:space-between;gap:20px;border-top:1px solid rgba(80,45,70,.12);padding-top:24px}
  .story-footer a{color:#8e6020;font-size:.8rem;font-weight:700}
  .consent-reminder{padding:88px 0;background:#0a040a}
  .consent-card{display:flex;align-items:end;justify-content:space-between;gap:44px;border:1px solid var(--line);border-radius:30px;padding:48px;background:linear-gradient(135deg,rgba(100,25,111,.24),rgba(255,255,255,.02))}
  .consent-card h2{margin:0;color:var(--ivory);font:600 clamp(2.5rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .consent-card p:not(.eyebrow){max-width:720px;color:#ad9daa}
  @media(max-width:860px){.story-shell{grid-template-columns:1fr}.identity{position:static;max-width:460px}.consent-card{align-items:flex-start;flex-direction:column}}
</style>
