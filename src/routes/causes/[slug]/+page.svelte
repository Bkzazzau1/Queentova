<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();
  const { campaign, updates } = $derived(data);

  const updateLabels: Record<string,string> = {
    field: 'Field update',
    milestone: 'Milestone',
    delivery: 'Delivery / distribution',
    funding: 'Funding update',
    impact: 'Impact update',
    announcement: 'Announcement'
  };

  function money(value: string | null) {
    if (!value) return '';
    const number = Number(value);
    if (!Number.isFinite(number)) return value;
    try {
      return new Intl.NumberFormat('en', {
        style: 'currency',
        currency: campaign.currency,
        maximumFractionDigits: 0
      }).format(number);
    } catch {
      return `${campaign.currency} ${number.toLocaleString()}`;
    }
  }
</script>

<svelte:head>
  <title>{campaign.seo_title || campaign.title} | Queen Tovah</title>
  <meta name="description" content={campaign.seo_description || campaign.summary} />
  {#if campaign.seo_keywords}<meta name="keywords" content={campaign.seo_keywords} />{/if}
  <meta property="og:title" content={campaign.seo_title || campaign.title} />
  <meta property="og:description" content={campaign.seo_description || campaign.summary} />
  {#if campaign.image}<meta property="og:image" content={campaign.image} />{/if}
</svelte:head>

<PageHero eyebrow="Foundation cause" title={campaign.title} copy={campaign.summary} />

<section class="detail">
  <div class="container shell">
    <div class="main">
      {#if campaign.image}
        <img class="hero-image" src={campaign.image} alt={campaign.image_alt || campaign.title} />
      {/if}
      <div class="body">
        {#if campaign.body}
          {#each campaign.body.split('\n\n').filter(Boolean) as paragraph}<p>{paragraph}</p>{/each}
        {:else}
          <p>{campaign.summary}</p>
        {/if}
      </div>
    </div>

    <aside class="card">
      <p class="eyebrow">Cause status</p>
      {#if campaign.goal_amount && campaign.progress_percent !== null}
        <strong class="raised">{money(campaign.current_amount)}</strong>
        <span class="goal">raised toward {money(campaign.goal_amount)}</span>
        <div class="bar"><span style={`width:${campaign.progress_percent}%`}></span></div>
        <small>{campaign.progress_percent}% of verified goal</small>
      {:else}
        <h2>Support without invented numbers.</h2>
        <p>Funding progress will appear here only when the Foundation publishes a verified target and amount.</p>
      {/if}

      {#if campaign.accepting_support}
        <a class="btn btn-primary" href="/donate">{campaign.cta_label || 'Support this cause'}</a>
      {:else}
        <a class="btn btn-secondary" href="/contact">Ask about this cause</a>
      {/if}
    </aside>
  </div>
</section>

{#if updates.length}
<section class="journal">
  <div class="container">
    <div class="journal-head">
      <div>
        <p class="eyebrow">Implementation journal</p>
        <h2>What happened after this cause was published.</h2>
      </div>
      <a href="/activity">Open full activity journal ↗</a>
    </div>

    <div class="updates">
      {#each updates.slice(0, 4) as update}
        <a href={`/activity/${update.slug}`}>
          <div class="update-meta">
            <span>{updateLabels[update.kind] || update.kind}</span>
            <span>{new Intl.DateTimeFormat('en',{dateStyle:'medium'}).format(new Date(update.occurred_at))}</span>
          </div>
          <h3>{update.title}</h3>
          <p>{update.summary}</p>
          <div class="update-facts">
            {#if update.output_value && update.output_unit}
              <span>{Number(update.output_value).toLocaleString()} {update.output_unit}</span>
            {/if}
            {#if update.expenditure_amount && update.expenditure_verified}
              <span>Verified expenditure</span>
            {/if}
            {#if update.location_label}<span>{update.location_label}</span>{/if}
          </div>
        </a>
      {/each}
    </div>
  </div>
</section>
{/if}


<style>
  .detail{padding:100px 0 120px;background:var(--ivory);color:#2b1827}
  .shell{display:grid;grid-template-columns:minmax(0,1fr) 350px;gap:56px;align-items:start}
  .hero-image{width:100%;max-height:620px;object-fit:cover;border-radius:30px;box-shadow:0 28px 70px rgba(60,30,50,.12)}
  .body{max-width:780px;margin-top:34px;color:#5f4e5a;font-size:1.06rem;line-height:1.85}
  .body p{margin:0 0 24px}
  aside{position:sticky;top:116px;border-color:rgba(80,45,70,.13);padding:30px;background:#fff;color:#3d2039;box-shadow:0 24px 60px rgba(60,30,50,.08)}
  aside .eyebrow{color:#8e6020}
  .raised{display:block;color:#4c2948;font:600 3.1rem/1 'Cormorant Garamond',Georgia,serif}
  .goal{display:block;margin-top:5px;color:#887986;font-size:.8rem}
  .bar{height:8px;overflow:hidden;margin-top:24px;border-radius:99px;background:#eadfce}
  .bar span{display:block;height:100%;background:linear-gradient(90deg,#8b6223,#e1bd6a)}
  aside small{display:block;margin-top:8px;color:#8d7c88}
  aside h2{margin:0;color:#44223f;font:600 2rem/1 'Cormorant Garamond',Georgia,serif}
  aside p{color:#6d5b68;font-size:.9rem}
  aside .btn{width:100%;margin-top:26px}
  .journal{padding:96px 0 110px;background:#0a040a}
  .journal-head{display:flex;align-items:end;justify-content:space-between;gap:40px}
  .journal-head .eyebrow{color:var(--gold-bright)}
  .journal-head h2{max-width:780px;margin:0;color:var(--ivory);font:600 clamp(2.5rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .journal-head>a{color:var(--gold-bright);font-size:.8rem;font-weight:700}
  .updates{display:grid;grid-template-columns:repeat(2,1fr);gap:14px;margin-top:42px}
  .updates>a{min-height:260px;display:flex;flex-direction:column;border:1px solid rgba(225,189,106,.15);border-radius:24px;padding:24px;background:rgba(255,255,255,.035)}
  .update-meta,.update-facts{display:flex;flex-wrap:wrap;gap:8px 14px;color:#9d8b9a;font-size:.68rem}
  .update-meta span:first-child{color:var(--gold-deep);font-weight:800;text-transform:uppercase;letter-spacing:.06em}
  .updates h3{margin:58px 0 10px;color:var(--champagne);font:600 1.9rem/1 'Cormorant Garamond',Georgia,serif}
  .updates p{margin:0;color:#aa9aa8;font-size:.85rem}
  .update-facts{margin-top:auto;padding-top:20px;color:#c0afbc}
  @media(max-width:850px){.shell{grid-template-columns:1fr}aside{position:static}.journal-head{align-items:flex-start;flex-direction:column}.updates{grid-template-columns:1fr}}
</style>
