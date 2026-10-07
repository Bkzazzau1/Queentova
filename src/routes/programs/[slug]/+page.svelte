<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();
  const { program, updates } = data;

  const updateLabels: Record<string,string> = {
    field: 'Field update',
    milestone: 'Milestone',
    delivery: 'Delivery / distribution',
    funding: 'Funding update',
    impact: 'Impact update',
    announcement: 'Announcement'
  };
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

{#if updates.length}
<section class="program-journal">
  <div class="container">
    <div class="journal-head">
      <div>
        <p class="eyebrow">Program activity</p>
        <h2>Recent work from this program.</h2>
      </div>
      <a href="/activity">Foundation activity journal ↗</a>
    </div>

    <div class="journal-list">
      {#each updates.slice(0, 5) as update}
        <a href={`/activity/${update.slug}`}>
          <div class="date">
            <strong>{new Intl.DateTimeFormat('en',{day:'2-digit'}).format(new Date(update.occurred_at))}</strong>
            <span>{new Intl.DateTimeFormat('en',{month:'short',year:'numeric'}).format(new Date(update.occurred_at))}</span>
          </div>
          <div>
            <span class="kind">{updateLabels[update.kind] || update.kind}</span>
            <h3>{update.title}</h3>
            <p>{update.summary}</p>
          </div>
          <em>↗</em>
        </a>
      {/each}
    </div>
  </div>
</section>
{/if}


<style>
  .program-detail{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .detail-grid{display:grid;grid-template-columns:300px 1fr;gap:80px}
  aside{align-self:start;border:1px solid rgba(80,45,70,.13);border-radius:26px;padding:28px;background:#fff}
  .icon{display:grid;width:64px;height:64px;place-items:center;border:1px solid rgba(166,112,37,.22);border-radius:50%;color:#9d6b25;font-size:1.6rem}
  aside p{margin:28px 0;color:#715f6c;font-size:.86rem}
  aside .btn{width:100%;padding-inline:16px}
  .body{max-width:760px;color:#5f4e5a;font-size:1.06rem;line-height:1.85}
  .body p{margin:0 0 24px}
  .program-journal{padding:96px 0 110px;background:#0a040a}
  .journal-head{display:flex;align-items:end;justify-content:space-between;gap:40px}
  .journal-head .eyebrow{color:var(--gold-bright)}
  .journal-head h2{margin:0;color:var(--ivory);font:600 clamp(2.5rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .journal-head>a{color:var(--gold-bright);font-size:.8rem;font-weight:700}
  .journal-list{margin-top:42px;border-top:1px solid var(--line)}
  .journal-list>a{display:grid;grid-template-columns:88px 1fr auto;gap:24px;align-items:center;border-bottom:1px solid var(--line);padding:22px 0}
  .date{display:grid;gap:2px}.date strong{color:var(--champagne);font:600 2rem/1 'Cormorant Garamond',Georgia,serif}.date span{color:#887788;font-size:.67rem}
  .kind{color:var(--gold-deep);font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em}
  .journal-list h3{margin:7px 0 6px;color:var(--champagne);font:600 1.8rem/1 'Cormorant Garamond',Georgia,serif}
  .journal-list p{margin:0;color:#aa9aa8;font-size:.84rem}.journal-list em{color:var(--gold-bright);font-style:normal}
  @media(max-width:780px){.detail-grid{grid-template-columns:1fr;gap:42px}aside{max-width:420px}.journal-head{align-items:flex-start;flex-direction:column}.journal-list>a{grid-template-columns:70px 1fr}.journal-list em{display:none}}
</style>
