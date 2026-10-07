<script lang="ts">
  import { page } from '$app/state';
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();
  const { event } = $derived(data);

  const start = $derived(new Date(event.starts_at));
  const date = $derived(new Intl.DateTimeFormat('en', { dateStyle:'full' }).format(start));
  const time = $derived(new Intl.DateTimeFormat('en', { timeStyle:'short' }).format(start));
  const location = $derived([event.venue_name, event.city, event.country].filter(Boolean).join(' • '));

  const eventSchema = $derived(
    JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'Event',
      name: event.title,
      description: event.summary,
      startDate: event.starts_at,
      ...(event.ends_at ? { endDate: event.ends_at } : {}),
      url: `${page.url.origin}${page.url.pathname}`,
      ...(event.image ? { image: [event.image] } : {}),
      ...(event.venue_name || event.address || event.city || event.country
        ? {
            location: {
              '@type': 'Place',
              name: event.venue_name || event.city || 'Queen Tovah Foundation event',
              address: {
                '@type': 'PostalAddress',
                streetAddress: event.address || undefined,
                addressLocality: event.city || undefined,
                addressCountry: event.country || undefined
              }
            }
          }
        : {}),
      organizer: {
        '@type': 'NGO',
        name: 'Queen Tovah Cares Foundation International',
        url: page.url.origin
      }
    }).replace(/</g, '\\u003c')
  );
</script>

<svelte:head>
  <title>{event.seo_title || event.title} | Queen Tovah</title>
  <meta name="description" content={event.seo_description || event.summary} />
  {#if event.seo_keywords}<meta name="keywords" content={event.seo_keywords} />{/if}
  <meta property="og:title" content={event.seo_title || event.title} />
  <meta property="og:description" content={event.seo_description || event.summary} />
  {#if event.image}<meta property="og:image" content={event.image} />{/if}
  {@html `<script type="application/ld+json">${eventSchema}</script>`}
</svelte:head>

<PageHero eyebrow="Foundation event" title={event.title} copy={event.summary} />

<section class="event-detail">
  <div class="container shell">
    <div class="main">
      {#if event.image}<img class="hero-image" src={event.image} alt={event.image_alt || event.title} />{/if}
      <div class="body">
        {#if event.body}
          {#each event.body.split('\n\n').filter(Boolean) as paragraph}<p>{paragraph}</p>{/each}
        {:else}<p>{event.summary}</p>{/if}
      </div>
    </div>

    <aside class="card">
      <p class="eyebrow">Event details</p>
      <dl>
        <div><dt>Date</dt><dd>{date}</dd></div>
        <div><dt>Time</dt><dd>{time}</dd></div>
        {#if location}<div><dt>Location</dt><dd>{location}</dd></div>{/if}
        {#if event.address}<div><dt>Address</dt><dd>{event.address}</dd></div>{/if}
      </dl>
      {#if event.registration_url}
        <a class="btn btn-primary" href={event.registration_url} target="_blank" rel="noreferrer">Register ↗</a>
      {:else if event.online_url}
        <a class="btn btn-primary" href={event.online_url} target="_blank" rel="noreferrer">Join online ↗</a>
      {:else}
        <a class="btn btn-secondary" href="/contact">Ask about this event</a>
      {/if}
      <a class="calendar-link" href={`/events/${event.slug}/calendar.ics`}>＋ Add to calendar</a>
      {#if event.address}
        <a
          class="directions-link"
          href={`https://www.google.com/maps/search/?api=1&query=${encodeURIComponent([event.venue_name,event.address,event.city,event.country].filter(Boolean).join(', '))}`}
          target="_blank"
          rel="noreferrer"
        >Get directions ↗</a>
      {/if}
    </aside>
  </div>
</section>

<style>
  .event-detail{padding:100px 0 120px;background:var(--ivory);color:#2b1827}
  .shell{display:grid;grid-template-columns:minmax(0,1fr) 350px;gap:56px;align-items:start}
  .hero-image{width:100%;max-height:620px;object-fit:cover;border-radius:30px;box-shadow:0 28px 70px rgba(60,30,50,.12)}
  .body{max-width:780px;margin-top:34px;color:#5f4e5a;font-size:1.06rem;line-height:1.85}
  aside{position:sticky;top:116px;border-color:rgba(80,45,70,.13);padding:30px;background:#fff;color:#3d2039}
  aside .eyebrow{color:#8e6020}
  dl{display:grid;gap:0;margin:0}
  dl div{border-bottom:1px solid rgba(80,45,70,.1);padding:16px 0}
  dt{color:#9a8059;font-size:.7rem;font-weight:700;letter-spacing:.08em;text-transform:uppercase}
  dd{margin:5px 0 0;color:#4b3547;font-size:.9rem}
  aside .btn{width:100%;margin-top:26px}
  .calendar-link,.directions-link{display:block;margin-top:13px;color:#8e6020;font-size:.78rem;font-weight:700;text-align:center}
  .directions-link{margin-top:8px;color:#745e6e}
  @media(max-width:850px){.shell{grid-template-columns:1fr}aside{position:static}}
</style>
