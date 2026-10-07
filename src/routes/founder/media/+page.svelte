<svelte:head>
  <title>Founder Recognition & Media | Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Verified awards, achievements, media coverage, publications and approved photographs relating to Princess Dr. Jessie Ifeoma Udoka-Menuba."
  />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();

  const featured = data.media.filter((item) => item.featured).slice(0, 3);
  const feed = data.media;

  const labels: Record<string,string> = {
    award: 'Award & recognition',
    achievement: 'Achievement',
    news: 'News coverage',
    interview: 'Interview',
    publication: 'Publication',
    community: 'Community appearance'
  };

  function itemDate(item: (typeof data.media)[number]) {
    const value = item.event_date || item.publication_date;
    if (!value) return 'Public record';
    return new Intl.DateTimeFormat('en', { dateStyle: 'medium' }).format(new Date(value));
  }

  function primaryPhoto(item: (typeof data.media)[number]) {
    return item.photos.find((photo) => photo.is_primary && photo.image_url) ??
      item.photos.find((photo) => photo.image_url) ??
      null;
  }
</script>

<PageHero
  eyebrow="Founder recognition & media"
  title="A public record,"
  accent="not a trophy wall."
  copy="Awards, achievements, coverage and approved photographs are organised here as a source-linked editorial archive. Every item points back to the publication or record that supports it."
/>

{#if featured.length}
<section class="featured">
  <div class="container">
    <div class="featured-grid">
      {#each featured as item, i}
        {@const photo = primaryPhoto(item)}
        <a class:lead={i === 0} href={`/founder/media/${item.slug}`}>
          {#if photo}
            <img src={photo.image_url} alt={photo.alt_text || item.title} />
          {/if}
          <div class="shade"></div>
          <div class="content">
            <div class="meta">
              <span>{labels[item.kind] || item.kind}</span>
              <span>{itemDate(item)}</span>
            </div>
            <h2>{item.title}</h2>
            <p>{item.summary}</p>
            <em>View record ↗</em>
          </div>
        </a>
      {/each}
    </div>
  </div>
</section>
{/if}

<section class="feed">
  <div class="container feed-grid">
    <aside>
      <p class="eyebrow">Media archive</p>
      <h2>Recognition with evidence attached.</h2>
      <p>
        Publication links stay visible beside each record. Source photographs appear only after the
        Foundation confirms that the image may be reused, or uploads its own approved copy.
      </p>
      <a href="/founder/jessie-ifeoma-udoka-menuba">Founder profile ←</a>
    </aside>

    <div class="timeline">
      {#if feed.length}
        {#each feed as item}
          {@const photo = primaryPhoto(item)}
          <article>
            <div class="date">{itemDate(item)}</div>
            <div class="record">
              <div class="record-top">
                <span>{labels[item.kind] || item.kind}</span>
                {#if item.verified_source}<span class="verified">Verified source</span>{/if}
              </div>

              {#if photo}
                <a class="thumb" href={`/founder/media/${item.slug}`}>
                  <img src={photo.image_url} alt={photo.alt_text || item.title} loading="lazy" />
                </a>
              {/if}

              <h3><a href={`/founder/media/${item.slug}`}>{item.title}</a></h3>
              <p>{item.summary}</p>

              <div class="record-meta">
                {#if item.award_title}<span><strong>Award</strong>{item.award_title}</span>{/if}
                {#if item.awarding_body}<span><strong>By</strong>{item.awarding_body}</span>{/if}
                {#if item.location}<span><strong>Location</strong>{item.location}</span>{/if}
              </div>

              <div class="actions">
                <a href={`/founder/media/${item.slug}`}>Open archive item ↗</a>
                <a href={item.source_url} target="_blank" rel="noreferrer">Read original publication ↗</a>
              </div>
            </div>
          </article>
        {/each}
      {:else}
        <div class="empty">
          Verified founder media records will appear here after publication through the Foundation admin.
        </div>
      {/if}
    </div>
  </div>
</section>

<section class="archive-note">
  <div class="container note">
    <div>
      <p class="eyebrow">Photo & publication integrity</p>
      <h2>Source discovery does not equal permission to republish.</h2>
      <p>
        The system can collect candidate photographs from approved publication domains for internal review,
        but those images remain private until reuse is explicitly approved.
      </p>
    </div>
    <a class="btn btn-secondary" href="/media">Press & Media Centre</a>
  </div>
</section>

<style>
  .featured{padding:96px 0;background:#0a040a}
  .featured-grid{display:grid;grid-template-columns:1.25fr .75fr;grid-template-rows:260px 260px;gap:16px}
  .featured-grid>a{position:relative;isolation:isolate;overflow:hidden;border:1px solid rgba(225,189,106,.16);border-radius:28px;background:radial-gradient(circle at 70% 20%,rgba(225,189,106,.17),transparent 18rem),linear-gradient(145deg,#4b1552,#100611)}
  .featured-grid>a.lead{grid-row:1 / 3}
  .featured-grid img{position:absolute;z-index:-2;inset:0;width:100%;height:100%;object-fit:cover}
  .shade{position:absolute;z-index:-1;inset:0;background:linear-gradient(0deg,rgba(7,2,7,.94),rgba(7,2,7,.12) 72%)}
  .content{position:absolute;right:28px;bottom:28px;left:28px}
  .meta{display:flex;gap:9px 18px;flex-wrap:wrap;color:var(--gold-bright);font-size:.66rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
  .content h2{margin:10px 0 8px;color:var(--ivory);font:600 1.9rem/1 'Cormorant Garamond',Georgia,serif}
  .lead .content h2{font-size:clamp(2.8rem,5vw,4.8rem)}
  .content p{max-width:680px;margin:0;color:#c2b4c0;font-size:.84rem}
  .content em{display:inline-block;margin-top:17px;color:var(--gold-bright);font-size:.76rem;font-style:normal;font-weight:800}

  .feed{padding:110px 0 120px;background:var(--ivory);color:#2b1827}
  .feed-grid{display:grid;grid-template-columns:290px 1fr;gap:72px;align-items:start}
  aside{position:sticky;top:124px}
  aside .eyebrow{color:#8e6020}
  aside h2{margin:0;color:#43213f;font:600 2.8rem/1 'Cormorant Garamond',Georgia,serif}
  aside p{color:#6d5b68}
  aside a{display:inline-block;margin-top:10px;color:#8e6020;font-size:.8rem;font-weight:700}

  .timeline{border-top:1px solid rgba(80,45,70,.14)}
  .timeline article{display:grid;grid-template-columns:130px 1fr;gap:26px;border-bottom:1px solid rgba(80,45,70,.14);padding:32px 0}
  .date{padding-top:5px;color:#9a8059;font-size:.72rem;font-weight:700}
  .record-top{display:flex;flex-wrap:wrap;gap:8px 12px;align-items:center}
  .record-top>span{color:#9b6c29;font-size:.66rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
  .record-top .verified{border:1px solid rgba(80,115,75,.25);border-radius:999px;padding:5px 8px;background:rgba(80,115,75,.07);color:#587252}
  .thumb{display:block;overflow:hidden;height:280px;margin:18px 0 22px;border-radius:24px}
  .thumb img{width:100%;height:100%;object-fit:cover}
  .record h3{margin:14px 0 8px;color:#43213f;font:600 clamp(2rem,4vw,3rem)/.98 'Cormorant Garamond',Georgia,serif}
  .record h3 a:hover{color:#8e6020}
  .record>p{max-width:760px;margin:0;color:#6d5b68}
  .record-meta{display:flex;flex-wrap:wrap;gap:10px 24px;margin-top:18px;color:#796875;font-size:.76rem}
  .record-meta span{display:flex;gap:6px}.record-meta strong{color:#9b6c29;font-size:.67rem;text-transform:uppercase}
  .actions{display:flex;flex-wrap:wrap;gap:9px 20px;margin-top:22px}
  .actions a{color:#8e6020;font-size:.78rem;font-weight:700}
  .empty{border:1px dashed rgba(80,45,70,.16);border-radius:20px;padding:32px;color:#6d5b68}

  .archive-note{padding:88px 0;background:#080308}
  .note{display:flex;align-items:end;justify-content:space-between;gap:44px;border:1px solid var(--line);border-radius:30px;padding:48px;background:linear-gradient(135deg,rgba(100,25,111,.24),rgba(255,255,255,.02))}
  .note h2{max-width:780px;margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .note p:not(.eyebrow){max-width:760px;color:#ad9daa}
  .note .btn{flex-shrink:0}

  @media(max-width:900px){
    .featured-grid{grid-template-columns:1fr;grid-template-rows:auto}
    .featured-grid>a,.featured-grid>a.lead{grid-row:auto;min-height:390px}
    .feed-grid{grid-template-columns:1fr;gap:42px}
    aside{position:static}
    .note{align-items:flex-start;flex-direction:column}
  }
  @media(max-width:620px){
    .timeline article{grid-template-columns:1fr;gap:8px}
    .thumb{height:230px}
  }
</style>
