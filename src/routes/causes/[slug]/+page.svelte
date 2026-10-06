<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();
  const { campaign } = data;

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
  @media(max-width:850px){.shell{grid-template-columns:1fr}aside{position:static}}
</style>
