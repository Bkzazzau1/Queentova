<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();
  const { resource } = data;

  const labels: Record<string,string> = {
    'annual-report': 'Annual report',
    'impact-report': 'Impact report',
    'policy': 'Policy',
    'press-kit': 'Press kit',
    'publication': 'Publication'
  };
</script>

<svelte:head>
  <title>{resource.seo_title || resource.title} | Queen Tovah</title>
  <meta name="description" content={resource.seo_description || resource.summary} />
  {#if resource.seo_keywords}<meta name="keywords" content={resource.seo_keywords} />{/if}
  <meta property="og:title" content={resource.seo_title || resource.title} />
  <meta property="og:description" content={resource.seo_description || resource.summary} />
</svelte:head>

<PageHero
  eyebrow={labels[resource.category] || 'Foundation resource'}
  title={resource.title}
  copy={resource.summary || 'Official Foundation resource.'}
/>

<section class="detail">
  <div class="container shell">
    <div class="document">
      {#if resource.thumbnail}
        <img src={resource.thumbnail} alt="" />
      {:else}
        <div class="placeholder"><span>QT</span><small>{labels[resource.category] || 'Resource'}</small></div>
      {/if}
    </div>
    <div class="copy">
      <p class="eyebrow">Official resource</p>
      <h2 class="section-title">{resource.title}</h2>
      {#if resource.year}<p class="year">{resource.year}</p>{/if}
      <p>{resource.summary || 'This item has been published through the Foundation administration system.'}</p>
      <div class="actions">
        {#if resource.file}<a class="btn btn-primary" href={resource.file} target="_blank" rel="noreferrer">Open document ↗</a>{/if}
        {#if resource.external_url}<a class="btn btn-secondary dark" href={resource.external_url} target="_blank" rel="noreferrer">Open external resource ↗</a>{/if}
        <a class="back" href="/resources">← Back to resources</a>
      </div>
    </div>
  </div>
</section>

<style>
  .detail{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .shell{display:grid;grid-template-columns:.75fr 1.25fr;gap:76px;align-items:center}
  .document{overflow:hidden;min-height:500px;border:1px solid rgba(80,45,70,.12);border-radius:30px;background:#fff;box-shadow:0 30px 75px rgba(60,30,50,.1)}
  .document img{width:100%;height:100%;min-height:500px;object-fit:cover}
  .placeholder{min-height:500px;display:flex;align-items:center;justify-content:center;flex-direction:column;gap:12px;background:radial-gradient(circle at 60% 25%,rgba(225,189,106,.27),transparent 15rem),linear-gradient(145deg,#4c1553,#150817);color:var(--gold-bright)}
  .placeholder span{font:600 5rem/1 'Cormorant Garamond',Georgia,serif}.placeholder small{color:#b8a9b6;text-transform:uppercase;letter-spacing:.1em}
  .copy .eyebrow{color:#8e6020}.copy .section-title{color:#351f32}.copy>p:not(.eyebrow):not(.year){max-width:700px;color:#6d5b68;font-size:1.02rem}.year{color:#9b6c29;font-weight:700}
  .actions{display:flex;flex-wrap:wrap;align-items:center;gap:10px;margin-top:30px}.dark{border-color:rgba(80,45,70,.2);color:#4b3547;background:transparent}.back{width:100%;margin-top:14px;color:#8e6020;font-size:.8rem;font-weight:700}
  @media(max-width:820px){.shell{grid-template-columns:1fr}.document,.document img,.placeholder{min-height:360px}}
</style>
