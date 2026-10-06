<svelte:head>
  <title>{data.query ? `Search: ${data.query}` : 'Search'} | Queen Tovah Cares Foundation International</title>
  <meta name="robots" content="noindex,follow" />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();

  const labels: Record<string, string> = {
    program: 'Program',
    story: 'Story',
    campaign: 'Cause',
    event: 'Event',
    resource: 'Resource',
    faq: 'FAQ'
  };
</script>

<PageHero
  eyebrow="Search the Foundation"
  title="Find the work"
  accent="that matters to you."
  copy="Search across programs, stories, causes and events from one place."
/>

<section class="search">
  <div class="container">
    <form method="GET" action="/search" class="search-box">
      <span aria-hidden="true">⌕</span>
      <input name="q" value={data.query} minlength="2" autocomplete="off" placeholder="Search programs, stories, causes, events…" aria-label="Search the Foundation" />
      <button class="btn btn-primary" type="submit">Search</button>
    </form>

    {#if data.query}
      <div class="result-head">
        <p><strong>{data.results.length}</strong> result{data.results.length === 1 ? '' : 's'} for “{data.query}”</p>
      </div>

      {#if data.results.length}
        <div class="results">
          {#each data.results as result}
            <a href={result.url}>
              <span>{labels[result.type] || result.type}</span>
              <h2>{result.title}</h2>
              <p>{result.excerpt}</p>
              <em>Open ↗</em>
            </a>
          {/each}
        </div>
      {:else}
        <div class="empty">
          <strong>No match found.</strong>
          <p>Try a broader phrase such as “education”, “youth”, “humanitarian” or “community”.</p>
        </div>
      {/if}
    {:else}
      <div class="suggestions">
        <p>Popular areas</p>
        <a href="/search?q=education">Education</a>
        <a href="/search?q=youth">Youth</a>
        <a href="/search?q=humanitarian">Humanitarian</a>
        <a href="/search?q=community">Community</a>
      </div>
    {/if}
  </div>
</section>

<style>
  .search{padding:90px 0 120px;background:var(--ivory);color:#2b1827;min-height:52vh}
  .search-box{display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:12px;max-width:920px;margin:-126px auto 0;position:relative;z-index:3;border:1px solid rgba(225,189,106,.28);border-radius:24px;padding:12px 12px 12px 22px;background:#fff;box-shadow:0 24px 70px rgba(40,15,35,.16)}
  .search-box>span{color:#9b6c29;font-size:1.6rem}
  input{width:100%;border:0;padding:14px 4px;background:transparent;color:#3c2638;font-size:1rem;outline:none}
  .result-head{margin:72px 0 18px;color:#7a6875}.result-head strong{color:#8e6020}
  .results{display:grid;gap:12px}
  .results a{position:relative;display:block;border:1px solid rgba(80,45,70,.11);border-radius:22px;padding:26px 100px 26px 28px;background:#fff;transition:transform .18s ease,border-color .18s ease}
  .results a:hover{transform:translateY(-2px);border-color:rgba(166,112,37,.35)}
  .results span{color:#9b6c29;font-size:.68rem;font-weight:700;letter-spacing:.1em;text-transform:uppercase}
  .results h2{margin:7px 0;color:#43213f;font:600 1.9rem/1 'Cormorant Garamond',Georgia,serif}
  .results p{max-width:740px;margin:0;color:#6d5b68}
  .results em{position:absolute;right:28px;top:50%;transform:translateY(-50%);color:#8e6020;font-size:.8rem;font-style:normal;font-weight:700}
  .empty{margin-top:70px;text-align:center;color:#6d5b68}.empty strong{color:#43213f;font:600 2.2rem/1 'Cormorant Garamond',Georgia,serif}
  .suggestions{display:flex;flex-wrap:wrap;align-items:center;justify-content:center;gap:8px;margin-top:72px}.suggestions p{width:100%;text-align:center;color:#867581}.suggestions a{border:1px solid rgba(80,45,70,.13);border-radius:999px;padding:9px 14px;background:#fff;color:#6b5365;font-size:.82rem}
  @media(max-width:650px){.search-box{grid-template-columns:auto 1fr;margin-top:-112px}.search-box .btn{grid-column:1/-1;width:100%}.results a{padding-right:28px}.results em{position:static;display:block;margin-top:16px;transform:none}}
</style>
