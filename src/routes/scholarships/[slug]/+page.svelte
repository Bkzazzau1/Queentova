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
    <article class="body">
      <section>
        <p class="eyebrow">Eligibility</p>
        {#if scholarship.eligibility}
          {#each scholarship.eligibility.split('\n\n').filter(Boolean) as paragraph}
            <p>{paragraph}</p>
          {/each}
        {:else}
          <p>Detailed eligibility has not yet been published by the Foundation.</p>
        {/if}
      </section>

      {#if scholarship.application_instructions}
        <section>
          <p class="eyebrow">How to apply</p>
          {#each scholarship.application_instructions.split('\n\n').filter(Boolean) as paragraph}
            <p>{paragraph}</p>
          {/each}
        </section>
      {/if}

      {#if scholarship.required_documents}
        <section class="documents">
          <p class="eyebrow">Documents to prepare</p>
          {#each scholarship.required_documents.split('\n').filter(Boolean) as item}
            <div><span>✓</span><p>{item}</p></div>
          {/each}
        </section>
      {/if}

      {#if scholarship.public_results_released && scholarship.results_summary}
        <section class="public-results">
          <div class="result-head">
            <p class="eyebrow">Published aggregate results</p>
            <span>Applicant identities remain private</span>
          </div>

          <div class="result-grid">
            <div><strong>{scholarship.results_summary.applications_received}</strong><span>Applications received</span></div>
            <div><strong>{scholarship.results_summary.eligible}</strong><span>Eligible after review</span></div>
            <div><strong>{scholarship.results_summary.shortlisted}</strong><span>Shortlisted</span></div>
            <div><strong>{scholarship.results_summary.selected}</strong><span>Selected</span></div>
          </div>

          {#if scholarship.public_results_note}<p>{scholarship.public_results_note}</p>{/if}
        </section>
      {/if}
    </article>

    <aside class="card">
      <span class:open={scholarship.application_status === 'open'}>{label}</span>

      {#if scholarship.opens_at}
        <p><strong>Opens</strong>{new Intl.DateTimeFormat('en', { dateStyle:'long' }).format(new Date(scholarship.opens_at))}</p>
      {/if}
      {#if scholarship.closes_at}
        <p><strong>Closes</strong>{new Intl.DateTimeFormat('en', { dateStyle:'long' }).format(new Date(scholarship.closes_at))}</p>
      {/if}
      {#if scholarship.max_awards}
        <p><strong>Planned awards</strong>{scholarship.max_awards}</p>
      {/if}

      {#if scholarship.internal_applications_open}
        <a class="btn btn-primary" href={`/scholarships/${scholarship.slug}/apply`}>
          Apply securely on this website
        </a>
        <a class="status-link" href="/scholarships/status">Already applied? Check status ↗</a>
      {:else if scholarship.application_status === 'open' && scholarship.application_url}
        <a class="btn btn-primary" href={scholarship.application_url} target="_blank" rel="noreferrer">
          Apply through official link ↗
        </a>
      {:else}
        <a class="btn btn-secondary" href="/contact">Scholarship enquiry</a>
      {/if}

      <small>
        Never send fees, identity documents or academic records through an unofficial link claiming to
        represent the Foundation.
      </small>
    </aside>
  </div>
</section>

<section class="privacy">
  <div class="container privacy-card">
    <div>
      <p class="eyebrow">Application privacy</p>
      <h2>Private applications stay private.</h2>
      <p>
        Foundation-managed application documents, reviewer notes and internal scores are not returned
        through the public scholarship pages or status checker.
      </p>
    </div>
    <a class="btn btn-secondary" href="/scholarships/status">Check application status</a>
  </div>
</section>

<style>
  .detail{padding:100px 0 120px;background:var(--ivory);color:#2b1827}
  .shell{display:grid;grid-template-columns:1fr 350px;gap:70px;align-items:start}
  .body{display:grid;gap:54px}
  .body .eyebrow{color:#8e6020}
  .body section>p:not(.eyebrow){max-width:760px;color:#5f4e5a;font-size:1.05rem;line-height:1.8}
  .documents>div{display:flex;gap:12px;max-width:760px;border-top:1px solid rgba(80,45,70,.1);padding:14px 0;color:#5f4e5a}
  .documents>div span{color:#8e6020;font-weight:800}.documents>div p{margin:0}
  .public-results{border:1px solid rgba(80,45,70,.12);border-radius:26px;padding:28px;background:#fff}
  .result-head{display:flex;align-items:center;justify-content:space-between;gap:20px}.result-head .eyebrow{margin:0}.result-head>span{color:#7d6c78;font-size:.72rem}
  .result-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:10px;margin-top:24px}
  .result-grid>div{border:1px solid rgba(80,45,70,.08);border-radius:18px;padding:16px;background:#fbf7f1}
  .result-grid strong{display:block;color:#43213f;font:600 2rem/1 'Cormorant Garamond',Georgia,serif}.result-grid span{display:block;margin-top:5px;color:#7e6d79;font-size:.72rem}
  .public-results>p:last-child{margin:20px 0 0;color:#6d5b68}

  aside{position:sticky;top:116px;border-color:rgba(80,45,70,.13);padding:30px;background:#fff;color:#3d2039}
  aside>span{display:inline-flex;border:1px solid rgba(80,45,70,.12);border-radius:999px;padding:7px 10px;color:#887583;font-size:.7rem;font-weight:700;text-transform:uppercase}
  aside>span.open{border-color:rgba(105,145,101,.28);color:#577451;background:rgba(105,145,101,.07)}
  aside p{display:grid;gap:4px;border-bottom:1px solid rgba(80,45,70,.08);padding:14px 0;color:#665361}
  aside p strong{color:#9a8059;font-size:.7rem;text-transform:uppercase}
  aside .btn{width:100%;margin-top:20px}
  aside small{display:block;margin-top:18px;color:#8d7c88;line-height:1.5}
  .status-link{display:block;margin-top:13px;color:#8e6020;font-size:.76rem;font-weight:700;text-align:center}

  .privacy{padding:88px 0;background:#090409}
  .privacy-card{display:flex;align-items:end;justify-content:space-between;gap:44px;border:1px solid var(--line);border-radius:30px;padding:48px;background:linear-gradient(135deg,rgba(100,25,111,.24),rgba(255,255,255,.02))}
  .privacy-card h2{margin:0;color:var(--ivory);font:600 clamp(2.5rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}.privacy-card p:not(.eyebrow){max-width:720px;color:#ad9daa}.privacy-card .btn{flex-shrink:0}

  @media(max-width:820px){.shell{grid-template-columns:1fr}aside{position:static}.privacy-card{align-items:flex-start;flex-direction:column}.result-grid{grid-template-columns:1fr 1fr}}
  @media(max-width:560px){.result-grid{grid-template-columns:1fr}.result-head{align-items:flex-start;flex-direction:column}}
</style>
