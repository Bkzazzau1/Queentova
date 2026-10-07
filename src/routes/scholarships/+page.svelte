<svelte:head>
  <title>Scholarships | Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Explore verified scholarship opportunities and Foundation-managed applications from Queen Tovah Cares Foundation International."
  />
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
    <div class="toolbar">
      <div>
        <p class="eyebrow">Verified opportunities</p>
        <h2>Apply through the official Foundation channel.</h2>
      </div>
      <a href="/scholarships/status">Check an application status ↗</a>
    </div>

    {#if data.scholarships.length}
      <div class="grid">
        {#each data.scholarships as scholarship}
          <article>
            <div class="top">
              <span class:open={scholarship.application_status === 'open'}>
                {labels[scholarship.application_status]}
              </span>
              {#if scholarship.internal_applications_enabled}
                <span class="channel">Foundation managed</span>
              {:else if scholarship.application_url}
                <span class="channel">Official external link</span>
              {/if}
            </div>

            <h2><a href={`/scholarships/${scholarship.slug}`}>{scholarship.title}</a></h2>
            <p>{scholarship.summary}</p>

            {#if scholarship.public_results_released && scholarship.results_summary}
              <div class="results">
                <span><strong>{scholarship.results_summary.selected}</strong> selected</span>
                <span><strong>{scholarship.results_summary.shortlisted}</strong> shortlisted</span>
              </div>
            {/if}

            <div class="bottom">
              <div>
                {#if scholarship.closes_at}
                  <small>Closes {new Intl.DateTimeFormat('en', { dateStyle:'medium' }).format(new Date(scholarship.closes_at))}</small>
                {:else}
                  <small>Foundation-managed opportunity</small>
                {/if}
                {#if scholarship.max_awards}<small>{scholarship.max_awards} award{scholarship.max_awards === 1 ? '' : 's'} planned</small>{/if}
              </div>
              <a href={`/scholarships/${scholarship.slug}`}>View details ↗</a>
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
    <div>
      <p class="eyebrow">Application safety</p>
      <h2>Applications and private documents stay separate from public scholarship pages.</h2>
    </div>
    <div>
      <p>
        Every application receives a private reference code. Scores, reviewer notes and uploaded
        documents are kept confidential and never shown publicly.
      </p>
      <a href="/scholarships/status">Track an application securely ↗</a>
    </div>
  </div>
</section>

<style>
  .scholarships{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .toolbar{display:flex;align-items:end;justify-content:space-between;gap:40px;margin-bottom:44px}
  .toolbar .eyebrow{color:#8e6020}.toolbar h2{max-width:760px;margin:0;color:#3f213a;font:600 clamp(2.3rem,5vw,3.8rem)/.98 'Cormorant Garamond',Georgia,serif}
  .toolbar>a{color:#8e6020;font-size:.8rem;font-weight:700}
  .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
  article{min-height:360px;display:flex;flex-direction:column;border:1px solid rgba(80,45,70,.13);border-radius:26px;padding:28px;background:#fff}
  .top,.bottom{display:flex;align-items:center;justify-content:space-between;gap:14px}
  .top>span{border:1px solid rgba(80,45,70,.12);border-radius:999px;padding:7px 10px;color:#887583;font-size:.67rem;font-weight:700;text-transform:uppercase;letter-spacing:.05em}
  .top>span.open{border-color:rgba(105,145,101,.28);color:#577451;background:rgba(105,145,101,.07)}
  .top .channel{border-color:rgba(166,112,37,.2);color:#916323;background:#fff9ef}
  article h2{margin:64px 0 12px;color:#44223f;font:600 clamp(2rem,4vw,3rem)/.98 'Cormorant Garamond',Georgia,serif}
  article h2 a:hover{color:#8e6020}
  article>p{margin:0;color:#6d5b68}
  .results{display:flex;gap:10px;margin-top:22px}.results span{border:1px solid rgba(80,45,70,.09);border-radius:14px;padding:10px 12px;color:#7d6b78;font-size:.74rem}.results strong{color:#8e6020}
  .bottom{margin-top:auto;border-top:1px solid rgba(80,45,70,.09);padding-top:20px}
  .bottom>div{display:grid;gap:4px}.bottom small{color:#8c7a87}.bottom a{color:#8e6020;font-size:.78rem;font-weight:700}
  .empty{max-width:760px;margin:auto;padding:64px;background:#fff;border-color:rgba(80,45,70,.12);text-align:center}
  .empty>span{color:#9b6c29;font-size:.72rem;font-weight:700;text-transform:uppercase;letter-spacing:.07em}
  .empty h2{margin:22px 0 12px;color:#44223f;font:600 2.5rem/1 'Cormorant Garamond',Georgia,serif}.empty p{color:#6d5b68}
  .safety{padding:88px 0;background:#0a040a}
  .safety-grid{display:grid;grid-template-columns:1fr .85fr;gap:70px;align-items:end}
  .safety-grid h2{margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .safety-grid>div:last-child p{color:#ad9daa}.safety-grid a{display:inline-block;margin-top:14px;color:var(--gold-bright);font-size:.8rem;font-weight:700}
  @media(max-width:780px){.grid,.safety-grid{grid-template-columns:1fr}.safety-grid{gap:28px}.toolbar{align-items:flex-start;flex-direction:column}}
</style>
