<svelte:head>
  <title>Stories | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="News and stories from Queen Tovah Cares Foundation International." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();

  const fallbackStory = {
    slug: 'amawbia-august-league-2025',
    title: 'Supporting youth unity through the Amawbia August League.',
    excerpt: 'Queen Tovah Cares Foundation International sponsored the 2025 Amawbia August League football tournament as part of its support for sports, youth engagement and community unity in Anambra.',
    category: 'Youth & Sports',
    event_date: '2025-08-01',
    hero_image: null,
    hero_alt: '',
    source_name: '',
    source_url: ''
  };

  const featured = $derived(data.stories.find((story) => story.featured) ?? data.stories[0] ?? fallbackStory);
  const year = $derived(featured.event_date ? featured.event_date.slice(0, 4) : 'Foundation');
  const category = $derived(featured.category
    .split('-')
    .map((part) => part.charAt(0).toUpperCase() + part.slice(1))
    .join(' '));
</script>

<PageHero
  eyebrow="News & stories"
  title="Stories of service,"
  accent="care and community."
  copy="Verified Foundation activities, partnerships, humanitarian interventions and community stories are published here through our editorial content system."
/>

<section class="stories">
  <div class="container">
    <article class="featured">
      <div
        class="visual"
        class:has-image={Boolean(featured.hero_image)}
        style={featured.hero_image ? `background-image: linear-gradient(0deg, rgba(14,5,15,.58), rgba(14,5,15,.14)), url('${featured.hero_image}')` : undefined}
      >
        <span>{year}</span><strong>{category}</strong>
      </div>
      <div class="copy">
        <p class="eyebrow">Featured activity</p>
        <h2><a href={`/news/${featured.slug}`}>{featured.title}</a></h2>
        <p>{featured.excerpt}</p>
        {#if featured.source_url}
          <a class="source" href={featured.source_url} target="_blank" rel="noreferrer">
            {featured.source_name || 'Source'} ↗
          </a>
        {:else}
          <span class="status">Additional verified stories and official photography are added through the Foundation admin.</span>
        {/if}
      </div>
    </article>

    {#if data.stories.length > 1}
      <div class="story-grid">
        {#each data.stories.filter((story) => story.slug !== featured.slug) as story}
          <article class="story-card">
            <span>{story.event_date?.slice(0,4) ?? 'Story'}</span>
            <h3><a href={`/news/${story.slug}`}>{story.title}</a></h3>
            <p>{story.excerpt}</p>
            {#if story.source_url}<a href={story.source_url} target="_blank" rel="noreferrer">Read source ↗</a>{/if}
          </article>
        {/each}
      </div>
    {/if}

    <div class="coming">
      <p class="eyebrow">Editorial standard</p>
      <h3>Only reviewed and published Foundation stories appear publicly.</h3>
      <p>Drafts remain private inside the admin until they complete the review and publication workflow.</p>
    </div>
  </div>
</section>

<style>
  .stories{padding:110px 0;background:var(--ivory);color:#2a1926}
  .featured{display:grid;grid-template-columns:.95fr 1.05fr;overflow:hidden;border:1px solid rgba(80,45,70,.14);border-radius:32px;background:#fffaf2;box-shadow:0 24px 60px rgba(60,30,50,.08)}
  .visual{min-height:470px;display:flex;align-items:flex-start;justify-content:flex-end;flex-direction:column;padding:38px;background:radial-gradient(circle at 65% 30%,rgba(225,189,106,.34),transparent 24%),linear-gradient(145deg,#5d1965,#140816);background-position:center;background-size:cover;color:var(--champagne)}
  .visual.has-image{background-position:center;background-size:cover}
  .visual span{color:var(--gold-bright);font-size:.78rem;font-weight:700;letter-spacing:.14em}
  .visual strong{margin-top:6px;font:600 2.6rem/1 'Cormorant Garamond',Georgia,serif}
  .copy{padding:58px}
  .copy .eyebrow{color:#8e6020}
  h2{margin:0;color:#40213c;font:600 clamp(2.4rem,5vw,4.4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .copy>p:not(.eyebrow){margin:24px 0 0;color:#695966}
  .copy h2 a:hover,.story-card h3 a:hover{color:#8e6020}
  .status,.source{display:block;margin-top:30px;border-top:1px solid rgba(80,45,70,.12);padding-top:20px;color:#9a825b;font-size:.8rem}
  .source{text-decoration:underline;text-underline-offset:3px}
  .story-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:34px}
  .story-card{border:1px solid rgba(80,45,70,.12);border-radius:22px;padding:24px;background:rgba(255,255,255,.45)}
  .story-card>span{color:#9a6d2b;font-size:.72rem;font-weight:700}
  .story-card h3{margin:28px 0 10px;color:#43213f;font:600 1.7rem/1 'Cormorant Garamond',Georgia,serif}
  .story-card p{color:#6f5e6a;font-size:.88rem}
  .story-card a{color:#8e6020;font-size:.78rem;text-decoration:underline;text-underline-offset:3px}
  .coming{max-width:760px;margin:80px auto 0;text-align:center}
  .coming .eyebrow{justify-content:center;color:#8e6020}
  .coming h3{margin:0;color:#43213f;font:600 2.4rem/1 'Cormorant Garamond',Georgia,serif}
  .coming p{color:#6f5e6a}
  @media(max-width:900px){.story-grid{grid-template-columns:1fr 1fr}}
  @media(max-width:820px){.featured{grid-template-columns:1fr}.visual{min-height:340px}.copy{padding:34px 26px}}
  @media(max-width:580px){.story-grid{grid-template-columns:1fr}}
</style>
