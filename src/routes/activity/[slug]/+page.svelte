<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();
  const { update } = $derived(data);

  const labels: Record<string,string> = {
    field: 'Field update',
    milestone: 'Milestone',
    delivery: 'Delivery / distribution',
    funding: 'Funding update',
    impact: 'Impact update',
    announcement: 'Announcement'
  };

  const photos = $derived(update.media.filter((item) => item.media_type === 'photo' && item.url));
  const documents = $derived(update.media.filter((item) => item.media_type === 'document' && item.url));

  function money(value: string) {
    const number = Number(value);
    if (!Number.isFinite(number)) return `${update.expenditure_currency} ${value}`;
    try {
      return new Intl.NumberFormat('en', {
        style: 'currency',
        currency: update.expenditure_currency,
        maximumFractionDigits: 0
      }).format(number);
    } catch {
      return `${update.expenditure_currency} ${number.toLocaleString()}`;
    }
  }

  function outputText() {
    if (!update.output_value || !update.output_unit) return '';
    const number = Number(update.output_value);
    return `${Number.isFinite(number) ? number.toLocaleString() : update.output_value} ${update.output_unit}`;
  }
</script>

<svelte:head>
  <title>{update.seo_title || update.title} | Queen Tovah Activity Journal</title>
  <meta name="description" content={update.seo_description || update.summary} />
  {#if update.seo_keywords}<meta name="keywords" content={update.seo_keywords} />{/if}
  <meta property="og:title" content={update.seo_title || update.title} />
  <meta property="og:description" content={update.seo_description || update.summary} />
  {#if photos[0]?.url}<meta property="og:image" content={photos[0].url} />{/if}
</svelte:head>

<PageHero
  eyebrow={labels[update.kind] || 'Foundation activity'}
  title={update.title}
  copy={update.summary}
/>

<section class="detail">
  <div class="container detail-grid">
    <article>
      {#if photos.length}
        <div class="gallery" class:single={photos.length === 1}>
          {#each photos as photo, i}
            <figure class:primary={photo.featured || i === 0}>
              <img src={photo.url} alt={photo.alt_text || update.title} />
              {#if photo.caption || photo.credit}
                <figcaption>
                  {#if photo.caption}<span>{photo.caption}</span>{/if}
                  {#if photo.credit}<small>Photo: {photo.credit}</small>{/if}
                </figcaption>
              {/if}
            </figure>
          {/each}
        </div>
      {/if}

      <div class="story-body">
        {#if update.body}
          {#each update.body.split('\n\n').filter(Boolean) as paragraph}<p>{paragraph}</p>{/each}
        {:else}
          <p>{update.summary}</p>
        {/if}
      </div>

      {#if update.video_url}
        <div class="video-card">
          <span>Video evidence / update</span>
          <a href={update.video_url} target="_blank" rel="noreferrer">Open published video ↗</a>
        </div>
      {/if}

      {#if documents.length}
        <div class="documents">
          <h2>Related documents</h2>
          {#each documents as document}
            <a href={document.url} target="_blank" rel="noreferrer">
              <span>{document.caption || document.alt_text || 'Activity document'}</span>
              <em>Open ↗</em>
            </a>
          {/each}
        </div>
      {/if}

      {#if update.source_url}
        <div class="source">
          <span>Supporting source</span>
          <a href={update.source_url} target="_blank" rel="noreferrer">{update.source_reference || 'Open source record'} ↗</a>
        </div>
      {/if}
    </article>

    <aside class="card">
      <p class="eyebrow">Update record</p>
      <dl>
        <div><dt>Date</dt><dd>{new Intl.DateTimeFormat('en',{dateStyle:'long'}).format(new Date(update.occurred_at))}</dd></div>
        {#if update.location_label}<div><dt>Location</dt><dd>{update.location_label}</dd></div>{/if}
        {#if update.campaign_title}<div><dt>Cause</dt><dd><a href={`/causes/${update.campaign_slug}`}>{update.campaign_title}</a></dd></div>{/if}
        {#if update.program_title}<div><dt>Program</dt><dd><a href={`/programs/${update.program_slug}`}>{update.program_title}</a></dd></div>{/if}
        {#if update.partners.length}
          <div class="partner-record">
            <dt>Partner{update.partners.length === 1 ? '' : 's'}</dt>
            <dd>
              {#each update.partners as partner, i}
                <a href={`/partners/${partner.slug}`}>{partner.title}</a>{i < update.partners.length - 1 ? ', ' : ''}
              {/each}
            </dd>
          </div>
        {/if}
      </dl>

      {#if outputText()}
        <div class="metric">
          <span>Reported output</span>
          <strong>{outputText()}</strong>
          {#if update.output_note}<p>{update.output_note}</p>{/if}
        </div>
      {/if}

      {#if update.expenditure_amount && update.expenditure_verified}
        <div class="metric finance">
          <span>Verified expenditure</span>
          <strong>{money(update.expenditure_amount)}</strong>
          {#if update.expenditure_note}<p>{update.expenditure_note}</p>{/if}
          {#if update.verification_note}<small>{update.verification_note}</small>{/if}
        </div>
      {/if}

      <a class="back" href="/activity">← Activity journal</a>
    </aside>
  </div>
</section>

<section class="verification">
  <div class="container verification-card">
    <div>
      <p class="eyebrow">Verification rule</p>
      <h2>Financial figures cannot publish as verified until the record passes validation.</h2>
      <p>
        This separates ordinary field updates from financial claims and helps the Foundation keep
        accountability information defensible.
      </p>
    </div>
    <a class="btn btn-secondary" href="/governance">Governance & transparency</a>
  </div>
</section>

<style>
  .detail{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .detail-grid{display:grid;grid-template-columns:minmax(0,1fr) 350px;gap:58px;align-items:start}
  .gallery{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}.gallery.single{grid-template-columns:1fr}
  figure{overflow:hidden;margin:0;border-radius:24px;background:#eee5d9}figure.primary{grid-column:1/-1}figure img{width:100%;height:320px;object-fit:cover}figure.primary img{height:min(620px,65vw)}
  figcaption{display:flex;justify-content:space-between;gap:14px;padding:12px 14px;color:#6d5b68;font-size:.76rem}figcaption small{color:#9a8059}
  .story-body{max-width:800px;margin-top:40px;color:#5f4e5a;font-size:1.06rem;line-height:1.88}.story-body p{margin:0 0 25px}
  .video-card,.source{display:flex;align-items:center;justify-content:space-between;gap:20px;margin-top:30px;border:1px solid rgba(80,45,70,.12);border-radius:18px;padding:18px 20px;background:#fff}.video-card span,.source span{color:#8d7b88;font-size:.74rem}.video-card a,.source a{color:#8e6020;font-size:.8rem;font-weight:700}
  .documents{margin-top:42px}.documents h2{color:#43213f;font:600 2.2rem/1 'Cormorant Garamond',Georgia,serif}.documents a{display:flex;justify-content:space-between;gap:20px;border-top:1px solid rgba(80,45,70,.12);padding:15px 0;color:#5f4e5a}.documents em{color:#8e6020;font-size:.78rem;font-style:normal;font-weight:700}
  aside{position:sticky;top:120px;border-color:rgba(80,45,70,.13);padding:28px;background:#fff;color:#3d2039}aside .eyebrow{color:#8e6020}
  dl{margin:0}dl div{border-bottom:1px solid rgba(80,45,70,.09);padding:14px 0}dt{color:#9a8059;font-size:.67rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em}dd{margin:5px 0 0;color:#4b3547;font-size:.88rem}dd a{color:#8e6020}
  .metric{margin-top:24px;border:1px solid rgba(80,45,70,.1);border-radius:18px;padding:18px;background:#fbf7f0}.metric span{color:#9a8059;font-size:.67rem;font-weight:800;text-transform:uppercase}.metric strong{display:block;margin-top:7px;color:#43213f;font:600 2rem/1 'Cormorant Garamond',Georgia,serif}.metric p,.metric small{display:block;margin:7px 0 0;color:#766571;font-size:.76rem}.metric.finance{border-color:rgba(85,120,80,.18);background:#f6faf4}
  .back{display:block;margin-top:24px;color:#8e6020;font-size:.78rem;font-weight:700;text-align:center}
  .verification{padding:88px 0;background:#090409}.verification-card{display:flex;align-items:end;justify-content:space-between;gap:44px;border:1px solid var(--line);border-radius:30px;padding:48px;background:linear-gradient(135deg,rgba(100,25,111,.24),rgba(255,255,255,.02))}.verification-card h2{max-width:820px;margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}.verification-card p:not(.eyebrow){max-width:740px;color:#ad9daa}.verification-card .btn{flex-shrink:0}
  @media(max-width:860px){.detail-grid{grid-template-columns:1fr}aside{position:static}.verification-card{align-items:flex-start;flex-direction:column}}
  @media(max-width:620px){.gallery{grid-template-columns:1fr}figure.primary{grid-column:auto}figure img,figure.primary img{height:300px}.video-card,.source{align-items:flex-start;flex-direction:column}}
</style>
