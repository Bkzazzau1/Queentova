<svelte:head>
  <title>Activity Journal | Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Verified field updates, milestones, deliveries and program activity from Queen Tovah Cares Foundation International."
  />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();

  const labels: Record<string,string> = {
    field: 'Field update',
    milestone: 'Milestone',
    delivery: 'Delivery / distribution',
    funding: 'Funding update',
    impact: 'Impact update',
    announcement: 'Announcement'
  };

  const featured = data.updates.find((item) => item.featured) ?? data.updates[0] ?? null;
  const remaining = featured
    ? data.updates.filter((item) => item.slug !== featured.slug)
    : [];

  function updateDate(value: string) {
    return new Intl.DateTimeFormat('en', { dateStyle: 'medium' }).format(new Date(value));
  }

  function primaryMedia(item: (typeof data.updates)[number]) {
    return item.media.find((media) => media.featured && media.url) ??
      item.media.find((media) => media.media_type === 'photo' && media.url) ??
      null;
  }

  function outputText(item: (typeof data.updates)[number]) {
    if (!item.output_value || !item.output_unit) return '';
    const number = Number(item.output_value);
    const value = Number.isFinite(number) ? number.toLocaleString() : item.output_value;
    return `${value} ${item.output_unit}`;
  }
</script>

<PageHero
  eyebrow="Foundation activity journal"
  title="Follow the work"
  accent="as it moves."
  copy="A chronological public record of reviewed field updates, milestones, deliveries and verified results across Foundation programs and causes."
/>

<section class="journal-standard">
  <div class="container standard-grid">
    <div>
      <p class="eyebrow">Built for accountability</p>
      <h2 class="section-title">More useful than a social-media timeline.</h2>
    </div>
    <div class="standards">
      <span><i>01</i>Reviewed before publication</span>
      <span><i>02</i>Linked to a program or cause</span>
      <span><i>03</i>Financial figures require verification</span>
      <span><i>04</i>Outputs show units and context</span>
      <span><i>05</i>Media carries source/credit controls</span>
      <span><i>06</i>Original sources remain traceable</span>
    </div>
  </div>
</section>

<section class="activity-feed">
  <div class="container">
    {#if featured}
      {@const media = primaryMedia(featured)}
      <a class="featured-update" href={`/activity/${featured.slug}`}>
        <div class="featured-visual">
          {#if media}
            <img src={media.url} alt={media.alt_text || featured.title} />
          {:else}
            <div class="placeholder"><span>QT</span><small>{labels[featured.kind] || 'Activity update'}</small></div>
          {/if}
          <span class="badge">{labels[featured.kind] || featured.kind}</span>
        </div>
        <div class="featured-copy">
          <div class="meta">
            <span>{updateDate(featured.occurred_at)}</span>
            {#if featured.location_label}<span>{featured.location_label}</span>{/if}
          </div>
          <h2>{featured.title}</h2>
          <p>{featured.summary}</p>

          <div class="linkage">
            {#if featured.campaign_title}<span>Cause: {featured.campaign_title}</span>{/if}
            {#if featured.program_title}<span>Program: {featured.program_title}</span>{/if}
          </div>

          <div class="facts">
            {#if outputText(featured)}
              <div><strong>{outputText(featured)}</strong><span>{featured.output_note || 'Reported output'}</span></div>
            {/if}
            {#if featured.expenditure_amount && featured.expenditure_verified}
              <div><strong>{featured.expenditure_currency} {Number(featured.expenditure_amount).toLocaleString()}</strong><span>Verified expenditure</span></div>
            {/if}
          </div>

          <em>Open update ↗</em>
        </div>
      </a>

      {#if remaining.length}
        <div class="timeline">
          {#each remaining as item}
            {@const itemMedia = primaryMedia(item)}
            <article>
              <div class="date">
                <strong>{new Intl.DateTimeFormat('en',{day:'2-digit'}).format(new Date(item.occurred_at))}</strong>
                <span>{new Intl.DateTimeFormat('en',{month:'short',year:'numeric'}).format(new Date(item.occurred_at))}</span>
              </div>

              {#if itemMedia}
                <a class="thumb" href={`/activity/${item.slug}`}>
                  <img src={itemMedia.url} alt={itemMedia.alt_text || item.title} loading="lazy" />
                </a>
              {/if}

              <div class="update-copy">
                <div class="topline">
                  <span>{labels[item.kind] || item.kind}</span>
                  {#if item.expenditure_amount && item.expenditure_verified}<span class="verified">Verified finance</span>{/if}
                </div>
                <h3><a href={`/activity/${item.slug}`}>{item.title}</a></h3>
                <p>{item.summary}</p>
                <div class="context">
                  {#if item.campaign_title}<span>{item.campaign_title}</span>{/if}
                  {#if item.program_title}<span>{item.program_title}</span>{/if}
                  {#if item.location_label}<span>{item.location_label}</span>{/if}
                </div>
                <a class="read" href={`/activity/${item.slug}`}>Read update ↗</a>
              </div>
            </article>
          {/each}
        </div>
      {/if}
    {:else}
      <div class="empty card">
        <span>QT</span>
        <h2>Reviewed activity updates will appear here.</h2>
        <p>
          The journal intentionally does not invent field activity, spending figures or impact numbers.
          Administrators can publish verified updates as Foundation work progresses.
        </p>
      </div>
    {/if}
  </div>
</section>

<section class="journal-note">
  <div class="container note-card">
    <div>
      <p class="eyebrow">A living public record</p>
      <h2>Campaign pages can now show what happened after the announcement.</h2>
      <p>
        Updates can carry media, field milestones, reported outputs and verified financial figures,
        giving supporters a clearer view of implementation rather than only the original appeal.
      </p>
    </div>
    <a class="btn btn-secondary" href="/causes">Explore causes</a>
  </div>
</section>

<style>
  .journal-standard{padding:92px 0;background:var(--ivory);color:#2b1827}
  .standard-grid{display:grid;grid-template-columns:.82fr 1.18fr;gap:76px}
  .journal-standard .eyebrow{color:#8e6020}.journal-standard .section-title{color:#351e32}
  .standards{display:grid;grid-template-columns:1fr 1fr;border-top:1px solid rgba(80,45,70,.13)}
  .standards span{display:flex;gap:14px;align-items:center;border-bottom:1px solid rgba(80,45,70,.13);padding:17px 0;color:#5f4e5a;font-size:.86rem}
  .standards span:nth-child(odd){padding-right:20px}.standards span:nth-child(even){border-left:1px solid rgba(80,45,70,.13);padding-left:20px}
  .standards i{color:#9b6c29;font-size:.66rem;font-style:normal;font-weight:800}

  .activity-feed{padding:112px 0 120px;background:#090409}
  .featured-update{display:grid;grid-template-columns:1.05fr .95fr;overflow:hidden;border:1px solid rgba(225,189,106,.18);border-radius:32px;background:#100711}
  .featured-visual{position:relative;min-height:560px}
  .featured-visual img{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
  .placeholder{height:100%;display:grid;place-items:center;align-content:center;gap:10px;background:radial-gradient(circle at 65% 24%,rgba(225,189,106,.17),transparent 18rem),linear-gradient(145deg,#4b1552,#110712);color:var(--gold-bright)}
  .placeholder span{font:600 5.5rem/1 'Cormorant Garamond',Georgia,serif}.placeholder small{color:#aa9aa8;text-transform:uppercase;letter-spacing:.08em}
  .badge{position:absolute;top:22px;left:22px;border:1px solid rgba(255,255,255,.18);border-radius:999px;padding:8px 11px;background:rgba(8,3,8,.62);backdrop-filter:blur(8px);color:var(--champagne);font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em}
  .featured-copy{display:flex;justify-content:center;flex-direction:column;padding:48px}
  .meta,.linkage,.context{display:flex;flex-wrap:wrap;gap:8px 16px;color:#9c8999;font-size:.72rem}
  .featured-copy h2{margin:18px 0 12px;color:var(--ivory);font:600 clamp(2.8rem,5vw,4.8rem)/.94 'Cormorant Garamond',Georgia,serif}
  .featured-copy>p{color:#b7a7b5}.linkage{margin-top:18px;color:var(--gold-deep)}
  .facts{display:grid;grid-template-columns:1fr 1fr;gap:10px;margin-top:26px}
  .facts div{border:1px solid rgba(225,189,106,.14);border-radius:16px;padding:15px;background:rgba(255,255,255,.025)}
  .facts strong{display:block;color:var(--champagne);font:600 1.55rem/1 'Cormorant Garamond',Georgia,serif}.facts span{display:block;margin-top:5px;color:#978596;font-size:.7rem}
  .featured-copy em{margin-top:28px;color:var(--gold-bright);font-size:.8rem;font-style:normal;font-weight:800}

  .timeline{margin-top:40px;border-top:1px solid var(--line)}
  .timeline article{display:grid;grid-template-columns:90px 220px 1fr;gap:28px;align-items:start;border-bottom:1px solid var(--line);padding:28px 0}
  .date{display:grid;gap:3px;padding-top:4px}.date strong{color:var(--champagne);font:600 2rem/1 'Cormorant Garamond',Georgia,serif}.date span{color:#8c7a8a;font-size:.68rem}
  .thumb{height:160px;overflow:hidden;border-radius:18px;background:#1a0b1b}.thumb img{width:100%;height:100%;object-fit:cover}
  .topline{display:flex;flex-wrap:wrap;gap:8px 12px}.topline>span{color:var(--gold-deep);font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em}.topline .verified{border:1px solid rgba(85,120,80,.25);border-radius:999px;padding:4px 7px;color:#9ab493}
  .update-copy h3{margin:10px 0 8px;color:var(--champagne);font:600 2rem/1 'Cormorant Garamond',Georgia,serif}.update-copy h3 a:hover{color:var(--gold-bright)}
  .update-copy>p{max-width:760px;margin:0;color:#aa9aa8}.context{margin-top:12px}.read{display:inline-block;margin-top:16px;color:var(--gold-bright);font-size:.75rem;font-weight:800}

  .empty{max-width:760px;margin:auto;border-color:rgba(225,189,106,.16);padding:64px;background:rgba(255,255,255,.035);text-align:center}.empty>span{color:var(--gold-bright);font:600 4rem/1 'Cormorant Garamond',Georgia,serif}.empty h2{margin:24px 0 10px;color:var(--ivory);font:600 2.5rem/1 'Cormorant Garamond',Georgia,serif}.empty p{color:#aa9aa8}

  .journal-note{padding:88px 0;background:var(--cream);color:#2b1827}.note-card{display:flex;align-items:end;justify-content:space-between;gap:44px;border:1px solid rgba(80,45,70,.12);border-radius:30px;padding:46px;background:#fff}.note-card .eyebrow{color:#8e6020}.note-card h2{max-width:820px;margin:0;color:#43213f;font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}.note-card p:not(.eyebrow){max-width:760px;color:#6d5b68}.note-card .btn{flex-shrink:0;border-color:rgba(80,45,70,.2);color:#4c3548}

  @media(max-width:900px){.standard-grid,.featured-update{grid-template-columns:1fr}.featured-visual{min-height:420px}.timeline article{grid-template-columns:70px 1fr}.timeline .thumb{grid-column:2}.note-card{align-items:flex-start;flex-direction:column}}
  @media(max-width:620px){.standards{grid-template-columns:1fr}.standards span:nth-child(odd),.standards span:nth-child(even){border-left:0;padding:15px 0}.featured-copy{padding:34px 24px}.facts{grid-template-columns:1fr}.timeline article{grid-template-columns:1fr}.timeline .thumb{grid-column:auto}.date{grid-template-columns:auto 1fr;align-items:end;gap:8px}}
</style>
