<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();
  const { event } = data;

  const start = new Date(event.starts_at);
  const date = new Intl.DateTimeFormat('en', { dateStyle:'full' }).format(start);
  const time = new Intl.DateTimeFormat('en', { timeStyle:'short' }).format(start);
  const location = [event.venue_name, event.city, event.country].filter(Boolean).join(' • ');
</script>

<svelte:head>
  <title>{event.seo_title || event.title} | Queen Tovah</title>
  <meta name="description" content={event.seo_description || event.summary} />
  {#if event.seo_keywords}<meta name="keywords" content={event.seo_keywords} />{/if}
  <meta property="og:title" content={event.seo_title || event.title} />
  <meta property="og:description" content={event.seo_description || event.summary} />
  {#if event.image}<meta property="og:image" content={event.image} />{/if}
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
  @media(max-width:850px){.shell{grid-template-columns:1fr}aside{position:static}}
</style>
