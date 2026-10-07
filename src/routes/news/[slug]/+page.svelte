<script lang="ts">
  import { page } from '$app/state';
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();
  const { story } = $derived(data);

  const eventDate = $derived(story.event_date
    ? new Intl.DateTimeFormat('en', { dateStyle: 'long' }).format(new Date(story.event_date))
    : '');

  const articleSchema = $derived(
    JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'Article',
      headline: story.title,
      description: story.excerpt,
      url: `${page.url.origin}${page.url.pathname}`,
      ...(story.hero_image ? { image: story.hero_image } : {}),
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
  <title>{story.seo_title || story.title} | Queen Tovah Cares Foundation International</title>
  <meta name="description" content={story.seo_description || story.excerpt} />
  {#if story.seo_keywords}<meta name="keywords" content={story.seo_keywords} />{/if}
  <meta property="og:title" content={story.seo_title || story.title} />
  <meta property="og:description" content={story.seo_description || story.excerpt} />
  {#if story.hero_image}<meta property="og:image" content={story.hero_image} />{/if}
  <meta property="og:type" content="article" />
  {@html `<script type="application/ld+json">${articleSchema}</script>`}
</svelte:head>

<PageHero
  eyebrow={story.category.replace('-', ' ')}
  title={story.title}
  copy={story.excerpt}
/>

<article class="story">
  <div class="container story-shell">
    {#if story.hero_image}
      <img class="hero-image" src={story.hero_image} alt={story.hero_alt || story.title} />
    {/if}

    <div class="meta">
      {#if eventDate}<span>{eventDate}</span>{/if}
      {#if story.source_name}<span>{story.source_name}</span>{/if}
    </div>

    <div class="body">
      {#if story.body}
        {#each story.body.split('\n\n').filter(Boolean) as paragraph}
          <p>{paragraph}</p>
        {/each}
      {:else}
        <p>{story.excerpt}</p>
      {/if}
    </div>

    {#if story.source_url}
      <a class="source" href={story.source_url} target="_blank" rel="noreferrer">
        View published source ↗
      </a>
    {/if}
  </div>
</article>

<style>
  .story{padding:90px 0 120px;background:var(--ivory);color:#2b1827}
  .story-shell{max-width:900px}
  .hero-image{width:100%;max-height:580px;object-fit:cover;border-radius:28px;box-shadow:0 28px 70px rgba(60,30,50,.12)}
  .meta{display:flex;flex-wrap:wrap;gap:10px 24px;margin:28px 0;color:#9a8057;font-size:.78rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase}
  .body{color:#5f4e5a;font-size:1.06rem;line-height:1.85}
  .body p{margin:0 0 24px}
  .source{display:inline-block;margin-top:22px;color:#8e6020;font-size:.86rem;text-decoration:underline;text-underline-offset:4px}
</style>
