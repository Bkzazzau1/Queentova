<svelte:head>
  <title>Scholarships | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Explore verified scholarship opportunities from Queen Tovah Cares Foundation International." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();

  const labels = {
    open: 'Applications open',
    upcoming: 'Upcoming',
    closed: 'Closed'
  } as const;
</script>

<PageHero
  eyebrow="Education & opportunity"
  title="Potential should not be"
  accent="priced out of possibility."
  copy="Scholarship opportunities are published here only after the Foundation confirms eligibility, timelines and the official application channel."
/>

<section class="scholarships">
  <div class="container">
    {#if data.scholarships.length}
      <div class="grid">
        {#each data.scholarships as scholarship}
          <article>
            <div class="top">
              <span class:open={scholarship.application_status === 'open'}>
                {labels[scholarship.application_status]}
              </span>
              <span class="arrow">↗</span>
            </div>
            <h2><a href={`/scholarships/${scholarship.slug}`}>{scholarship.title}</a></h2>
            <p>{scholarship.summary}</p>
            <div class="bottom">
              {#if scholarship.closes_at}
                <small>Closes {new Intl.DateTimeFormat('en', { dateStyle:'medium' }).format(new Date(scholarship.closes_at))}</small>
              {:else}
                <small>Foundation-managed opportunity</small>
              {/if}
              <a href={`/scholarships/${scholarship.slug}`}>View details</a>
            </div>
          </article>
        {/each}
      </div>
    {:else}
      <div class="empty card">
        <span>Education remains part of the mission.</span>
        <h2>No scholarship application is publicly open right now.</h2>
        <p>Approved opportunities will appear here with verified eligibility and application information.</p>
      </div>
    {/if}
  </div>
</section>

<section class="safety">
  <div class="container safety-grid">
    <div><p class="eyebrow">Application safety</p><h2>Trust only scholarship links published on this website.</h2></div>
    <p>Queen Tovah scholarship records can include a single official application URL. If no link is published, the Foundation has not opened online applications through this platform.</p>
  </div>
</section>

<style>
  .scholarships{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
  article{min-height:330px;display:flex;flex-direction:column;border:1px solid rgba(80,45,70,.13);border-radius:26px;padding:28px;background:#fff}
  .top,.bottom{display:flex;align-items:center;justify-content:space-between;gap:20px}
  .top>span:first-child{border:1px solid rgba(80,45,70,.12);border-radius:999px;padding:7px 10px;color:#887583;font-size:.69rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em}
  .top>span.open{border-color:rgba(105,145,101,.28);color:#577451;background:rgba(105,145,101,.07)}
  .arrow{color:#9b6c29}
  h2{margin:72px 0 12px;color:#44223f;font:600 clamp(2rem,4vw,3rem)/.98 'Cormorant Garamond',Georgia,serif}
  h2 a:hover{color:#8e6020}
  article>p{margin:0;color:#6d5b68}
  .bottom{margin-top:auto;border-top:1px solid rgba(80,45,70,.09);padding-top:20px}
  .bottom small{color:#8c7a87}.bottom a{color:#8e6020;font-size:.78rem;font-weight:700}
  .empty{max-width:760px;margin:auto;padding:64px;background:#fff;border-color:rgba(80,45,70,.12);text-align:center}
  .empty>span{color:#9b6c29;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em}
  .empty h2{margin:22px 0 12px}.empty p{color:#6d5b68}
  .safety{padding:88px 0;background:#0a040a}
  .safety-grid{display:grid;grid-template-columns:1fr .85fr;gap:70px;align-items:end}
  .safety-grid h2{margin:0;color:var(--ivory)}
  .safety-grid>p{color:#ad9daa}
  @media(max-width:780px){.grid,.safety-grid{grid-template-columns:1fr}.safety-grid{gap:28px}}
</style>
