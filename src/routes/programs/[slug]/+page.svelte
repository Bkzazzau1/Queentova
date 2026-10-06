<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();
  const { program } = data;
</script>

<svelte:head>
  <title>{program.seo_title || program.title} | Queen Tovah Cares Foundation International</title>
  <meta name="description" content={program.seo_description || program.summary} />
  {#if program.seo_keywords}<meta name="keywords" content={program.seo_keywords} />{/if}
  <meta property="og:title" content={program.seo_title || program.title} />
  <meta property="og:description" content={program.seo_description || program.summary} />
</svelte:head>

<PageHero
  eyebrow="Foundation program"
  title={program.title}
  copy={program.summary}
/>

<section class="program-detail">
  <div class="container detail-grid">
    <aside>
      <span class="icon">{program.icon === 'heart' ? '♡' : program.icon === 'book' ? '◫' : program.icon === 'spark' ? '✦' : '◉'}</span>
      <p>Managed and published through the Queen Tovah Foundation administration system.</p>
      <a class="btn btn-primary" href="/contact">Enquire about this program</a>
    </aside>
    <div class="body">
      {#if program.body}
        {#each program.body.split('\n\n').filter(Boolean) as paragraph}
          <p>{paragraph}</p>
        {/each}
      {:else}
        <p>{program.summary}</p>
      {/if}
    </div>
  </div>
</section>

<style>
  .program-detail{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .detail-grid{display:grid;grid-template-columns:300px 1fr;gap:80px}
  aside{align-self:start;border:1px solid rgba(80,45,70,.13);border-radius:26px;padding:28px;background:#fff}
  .icon{display:grid;width:64px;height:64px;place-items:center;border:1px solid rgba(166,112,37,.22);border-radius:50%;color:#9d6b25;font-size:1.6rem}
  aside p{margin:28px 0;color:#715f6c;font-size:.86rem}
  aside .btn{width:100%;padding-inline:16px}
  .body{max-width:760px;color:#5f4e5a;font-size:1.06rem;line-height:1.85}
  .body p{margin:0 0 24px}
  @media(max-width:780px){.detail-grid{grid-template-columns:1fr;gap:42px}aside{max-width:420px}}
</style>
