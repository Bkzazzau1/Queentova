<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();
  const { scholarship } = data;

  const label = scholarship.application_status === 'open'
    ? 'Applications open'
    : scholarship.application_status === 'upcoming'
      ? 'Upcoming opportunity'
      : 'Applications closed';
</script>

<svelte:head>
  <title>{scholarship.title} | Queen Tovah Scholarships</title>
  <meta name="description" content={scholarship.summary} />
</svelte:head>

<PageHero eyebrow="Scholarship opportunity" title={scholarship.title} copy={scholarship.summary} />

<section class="detail">
  <div class="container shell">
    <div class="body">
      <p class="eyebrow">Eligibility</p>
      {#if scholarship.eligibility}
        {#each scholarship.eligibility.split('\n\n').filter(Boolean) as paragraph}<p>{paragraph}</p>{/each}
      {:else}
        <p>Detailed eligibility has not yet been published by the Foundation.</p>
      {/if}
    </div>
    <aside class="card">
      <span class:open={scholarship.application_status === 'open'}>{label}</span>
      {#if scholarship.opens_at}<p><strong>Opens</strong>{new Intl.DateTimeFormat('en', { dateStyle:'long' }).format(new Date(scholarship.opens_at))}</p>{/if}
      {#if scholarship.closes_at}<p><strong>Closes</strong>{new Intl.DateTimeFormat('en', { dateStyle:'long' }).format(new Date(scholarship.closes_at))}</p>{/if}
      {#if scholarship.application_status === 'open' && scholarship.application_url}
        <a class="btn btn-primary" href={scholarship.application_url} target="_blank" rel="noreferrer">Apply through official link ↗</a>
      {:else}
        <a class="btn btn-secondary" href="/contact">Scholarship enquiry</a>
      {/if}
      <small>Never pay through an unverified link claiming to represent this Foundation.</small>
    </aside>
  </div>
</section>

<style>
  .detail{padding:100px 0 120px;background:var(--ivory);color:#2b1827}
  .shell{display:grid;grid-template-columns:1fr 350px;gap:70px;align-items:start}
  .body .eyebrow{color:#8e6020}
  .body>p:not(.eyebrow){max-width:760px;color:#5f4e5a;font-size:1.05rem;line-height:1.8}
  aside{position:sticky;top:116px;border-color:rgba(80,45,70,.13);padding:30px;background:#fff;color:#3d2039}
  aside>span{display:inline-flex;border:1px solid rgba(80,45,70,.12);border-radius:999px;padding:7px 10px;color:#887583;font-size:.7rem;font-weight:700;text-transform:uppercase}
  aside>span.open{border-color:rgba(105,145,101,.28);color:#577451;background:rgba(105,145,101,.07)}
  aside p{display:grid;gap:4px;border-bottom:1px solid rgba(80,45,70,.08);padding:14px 0;color:#665361}
  aside p strong{color:#9a8059;font-size:.7rem;text-transform:uppercase}
  aside .btn{width:100%;margin-top:20px}
  aside small{display:block;margin-top:18px;color:#8d7c88;line-height:1.5}
  @media(max-width:820px){.shell{grid-template-columns:1fr}aside{position:static}}
</style>
