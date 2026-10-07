<svelte:head>
  <title>Events | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Explore Queen Tovah Cares Foundation International events, outreach activities and community programs." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();

  const now = new Date();
  const upcoming = $derived(data.events.filter((event) => new Date(event.starts_at) >= now));
  const past = $derived(data.events.filter((event) => new Date(event.starts_at) < now).reverse());

  function parts(value: string) {
    const d = new Date(value);
    return {
      day: new Intl.DateTimeFormat('en', { day: '2-digit' }).format(d),
      month: new Intl.DateTimeFormat('en', { month: 'short' }).format(d),
      time: new Intl.DateTimeFormat('en', { hour: 'numeric', minute: '2-digit' }).format(d)
    };
  }
</script>

<PageHero
  eyebrow="Events & outreach"
  title="Where service"
  accent="meets community."
  copy="Upcoming Foundation events, outreach activities and community programs appear here after they are reviewed and published."
/>

<section class="events">
  <div class="container">
    <div class="heading">
      <div>
        <p class="eyebrow">Upcoming</p>
        <h2 class="section-title">Join us where it matters.</h2>
      </div>
      <a href="/get-involved">Volunteer with the Foundation ↗</a>
    </div>

    {#if upcoming.length}
      <div class="event-list">
        {#each upcoming as event}
          {@const date = parts(event.starts_at)}
          <article>
            <div class="date"><strong>{date.day}</strong><span>{date.month}</span></div>
            <div class="event-copy">
              <div class="meta">{date.time}{event.city ? ` • ${event.city}` : ''}{event.country ? `, ${event.country}` : ''}</div>
              <h3><a href={`/events/${event.slug}`}>{event.title}</a></h3>
              <p>{event.summary}</p>
              <a class="view" href={`/events/${event.slug}`}>Event details ↗</a>
            </div>
            <div class="visual">
              {#if event.image}<img src={event.image} alt={event.image_alt || event.title} loading="lazy" />{:else}<span>QT</span>{/if}
            </div>
          </article>
        {/each}
      </div>
    {:else}
      <div class="empty card">
        <h3>No public event is scheduled yet.</h3>
        <p>Upcoming Foundation events will be announced here.</p>
      </div>
    {/if}

    {#if past.length}
      <div class="past">
        <p class="eyebrow">Past events</p>
        <div class="past-grid">
          {#each past.slice(0,6) as event}
            <a href={`/events/${event.slug}`}>
              <span>{new Intl.DateTimeFormat('en', { month:'short', year:'numeric' }).format(new Date(event.starts_at))}</span>
              <strong>{event.title}</strong>
              <small>{event.city || event.country || 'Foundation event'}</small>
            </a>
          {/each}
        </div>
      </div>
    {/if}
  </div>
</section>

<style>
  .events{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .heading{display:flex;align-items:end;justify-content:space-between;gap:40px}
  .heading .eyebrow{color:#8e6020}
  .heading .section-title{color:#351e32}
  .heading>a{color:#8e6020;font-size:.82rem;font-weight:700}
  .event-list{margin-top:52px;border-top:1px solid rgba(80,45,70,.14)}
  article{display:grid;grid-template-columns:92px 1fr 250px;gap:32px;align-items:center;border-bottom:1px solid rgba(80,45,70,.14);padding:30px 0}
  .date{display:grid;place-items:center;width:72px;height:82px;border:1px solid rgba(166,112,37,.25);border-radius:20px;background:#fff}
  .date strong{color:#4b2946;font:600 2rem/1 'Cormorant Garamond',Georgia,serif}
  .date span{color:#9b6c29;font-size:.72rem;font-weight:700;text-transform:uppercase}
  .meta{color:#9b8059;font-size:.75rem;font-weight:700;text-transform:uppercase;letter-spacing:.04em}
  h3{margin:7px 0 8px;color:#40213b;font:600 2rem/1 'Cormorant Garamond',Georgia,serif}
  h3 a:hover{color:#8e6020}
  .event-copy p{max-width:680px;margin:0;color:#6c5a67}
  .view{display:inline-block;margin-top:14px;color:#8e6020;font-size:.78rem;font-weight:700}
  .visual{height:150px;overflow:hidden;border-radius:22px;background:linear-gradient(145deg,#5c1a64,#140816);display:grid;place-items:center;color:var(--gold-bright);font:600 2.5rem/1 'Cormorant Garamond',Georgia,serif}
  .visual img{width:100%;height:100%;object-fit:cover}
  .empty{margin-top:50px;padding:44px;background:#fff;border-color:rgba(80,45,70,.12);color:#4a2a45}
  .empty h3{margin:0}.empty p{color:#6d5b68}
  .past{margin-top:90px}
  .past .eyebrow{color:#8e6020}
  .past-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px}
  .past-grid a{display:grid;gap:8px;border:1px solid rgba(80,45,70,.12);border-radius:20px;padding:22px;background:#fff}
  .past-grid span{color:#9b6c29;font-size:.72rem;font-weight:700;text-transform:uppercase}
  .past-grid strong{color:#43233f;font:600 1.45rem/1.05 'Cormorant Garamond',Georgia,serif}
  .past-grid small{color:#8a7986}
  @media(max-width:860px){article{grid-template-columns:78px 1fr}.visual{display:none}.past-grid{grid-template-columns:1fr 1fr}}
  @media(max-width:620px){.heading{align-items:flex-start;flex-direction:column}.past-grid{grid-template-columns:1fr}article{grid-template-columns:58px 1fr;gap:18px}.date{width:54px;height:68px}.date strong{font-size:1.6rem}}
</style>
