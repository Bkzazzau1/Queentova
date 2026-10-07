<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();
  const { item } = $derived(data);

  const label: Record<string,string> = {
    award: 'Award & recognition',
    achievement: 'Achievement',
    news: 'News coverage',
    interview: 'Interview',
    publication: 'Publication',
    community: 'Community appearance'
  };

  const displayDate = $derived(item.event_date || item.publication_date);
</script>

<svelte:head>
  <title>{item.seo_title || item.title} | Founder Media | Queen Tovah</title>
  <meta name="description" content={item.seo_description || item.summary} />
  {#if item.seo_keywords}<meta name="keywords" content={item.seo_keywords} />{/if}
  <meta property="og:title" content={item.seo_title || item.title} />
  <meta property="og:description" content={item.seo_description || item.summary} />
  {#if item.photos[0]?.image_url}<meta property="og:image" content={item.photos[0].image_url} />{/if}
</svelte:head>

<PageHero
  eyebrow={label[item.kind] || 'Founder media'}
  title={item.title}
  copy={item.summary}
/>

<section class="record">
  <div class="container record-grid">
    <article>
      {#if item.photos.length}
        <div class="gallery" class:single={item.photos.length === 1}>
          {#each item.photos as photo, i}
            {#if photo.image_url}
              <figure class:primary={photo.is_primary || i === 0}>
                <img src={photo.image_url} alt={photo.alt_text || item.title} />
                {#if photo.caption || photo.credit}
                  <figcaption>
                    {#if photo.caption}<span>{photo.caption}</span>{/if}
                    {#if photo.credit}<small>Photo: {photo.credit}</small>{/if}
                  </figcaption>
                {/if}
              </figure>
            {/if}
          {/each}
        </div>
      {:else}
        <div class="no-photo">
          <span>QT</span>
          <h2>No source photograph has been cleared for reuse yet.</h2>
          <p>The publication link remains available below so visitors can view the original reporting and its photographs at source.</p>
        </div>
      {/if}

      {#if item.body}
        <div class="body">
          {#each item.body.split('\n\n').filter(Boolean) as paragraph}
            <p>{paragraph}</p>
          {/each}
        </div>
      {/if}
    </article>

    <aside class="card">
      <p class="eyebrow">Record details</p>
      <dl>
        {#if displayDate}
          <div><dt>Date</dt><dd>{new Intl.DateTimeFormat('en',{dateStyle:'long'}).format(new Date(displayDate))}</dd></div>
        {/if}
        {#if item.award_title}<div><dt>Recognition</dt><dd>{item.award_title}</dd></div>{/if}
        {#if item.awarding_body}<div><dt>Awarding body</dt><dd>{item.awarding_body}</dd></div>{/if}
        {#if item.location}<div><dt>Location</dt><dd>{item.location}</dd></div>{/if}
        <div><dt>Published by</dt><dd>{item.source_name}</dd></div>
        {#if item.verified_source}<div><dt>Source status</dt><dd class="verified">Verified publication link</dd></div>{/if}
      </dl>

      <a class="btn btn-primary" href={item.source_url} target="_blank" rel="noreferrer">
        Open original publication ↗
      </a>
      <a class="archive-back" href="/founder/media">← Founder media archive</a>
    </aside>
  </div>
</section>

<style>
  .record{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .record-grid{display:grid;grid-template-columns:minmax(0,1fr) 350px;gap:56px;align-items:start}
  .gallery{display:grid;grid-template-columns:repeat(2,1fr);gap:14px}
  .gallery.single{grid-template-columns:1fr}
  figure{overflow:hidden;margin:0;border-radius:24px;background:#f2eadf}
  figure.primary{grid-column:1/-1}
  figure img{width:100%;height:330px;object-fit:cover}
  figure.primary img{height:min(620px,65vw)}
  figcaption{display:flex;justify-content:space-between;gap:16px;padding:12px 15px;color:#6d5b68;font-size:.76rem}
  figcaption small{color:#9a8059}
  .no-photo{min-height:450px;display:flex;align-items:center;justify-content:center;flex-direction:column;border:1px dashed rgba(80,45,70,.15);border-radius:28px;padding:48px;text-align:center;background:#fff}
  .no-photo>span{color:#9b6c29;font:600 4rem/1 'Cormorant Garamond',Georgia,serif}
  .no-photo h2{max-width:620px;margin:24px 0 10px;color:#43213f;font:600 2.4rem/1 'Cormorant Garamond',Georgia,serif}
  .no-photo p{max-width:600px;margin:0;color:#6d5b68}
  .body{max-width:800px;margin-top:42px;color:#5f4e5a;font-size:1.05rem;line-height:1.85}
  aside{position:sticky;top:120px;border-color:rgba(80,45,70,.13);padding:28px;background:#fff;color:#3d2039}
  aside .eyebrow{color:#8e6020}
  dl{margin:0}
  dl div{border-bottom:1px solid rgba(80,45,70,.09);padding:14px 0}
  dt{color:#9a8059;font-size:.68rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
  dd{margin:5px 0 0;color:#4b3547;font-size:.88rem}
  dd.verified{color:#587252}
  aside .btn{width:100%;margin-top:24px}
  .archive-back{display:block;margin-top:16px;color:#8e6020;font-size:.78rem;font-weight:700;text-align:center}
  @media(max-width:860px){.record-grid{grid-template-columns:1fr}aside{position:static}}
  @media(max-width:620px){.gallery{grid-template-columns:1fr}figure.primary{grid-column:auto}figure img,figure.primary img{height:300px}figcaption{flex-direction:column}}
</style>
