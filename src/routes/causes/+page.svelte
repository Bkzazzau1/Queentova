<svelte:head>
  <title>Causes | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Explore verified Queen Tovah Cares Foundation International humanitarian causes and campaigns." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();

  function money(value: string | null, currency: string) {
    if (!value) return '';
    const number = Number(value);
    if (!Number.isFinite(number)) return value;
    try {
      return new Intl.NumberFormat('en', {
        style: 'currency',
        currency,
        maximumFractionDigits: 0
      }).format(number);
    } catch {
      return `${currency} ${number.toLocaleString()}`;
    }
  }
</script>

<PageHero
  eyebrow="Causes & campaigns"
  title="Give where"
  accent="good can grow."
  copy="Every published cause on this page is managed through the Foundation's review workflow. Funding figures appear only when verified by the Foundation."
/>

<section class="causes">
  <div class="container">
    {#if data.campaigns.length}
      <div class="grid">
        {#each data.campaigns as campaign, i}
          <article class:featured={campaign.featured || i === 0}>
            <div class="media">
              {#if campaign.image}
                <img src={campaign.image} alt={campaign.image_alt || campaign.title} loading="lazy" />
              {:else}
                <div class="placeholder"><span>QT</span></div>
              {/if}
              <span class="badge">{campaign.accepting_support ? 'Open for support' : 'Foundation cause'}</span>
            </div>
            <div class="body">
              <h2><a href={`/causes/${campaign.slug}`}>{campaign.title}</a></h2>
              <p>{campaign.summary}</p>

              {#if campaign.goal_amount && campaign.progress_percent !== null}
                <div class="progress" aria-label={`${campaign.progress_percent}% of campaign goal`}>
                  <div class="bar"><span style={`width:${campaign.progress_percent}%`}></span></div>
                  <div class="numbers">
                    <strong>{money(campaign.current_amount, campaign.currency)}</strong>
                    <span>of {money(campaign.goal_amount, campaign.currency)}</span>
                  </div>
                </div>
              {/if}

              <a class="learn" href={`/causes/${campaign.slug}`}>View cause ↗</a>
            </div>
          </article>
        {/each}
      </div>
    {:else}
      <div class="empty card">
        <span class="mark">QT</span>
        <h2>Verified causes will appear here.</h2>
        <p>New causes are announced here once they are confirmed by the Foundation.</p>
      </div>
    {/if}
  </div>
</section>

<section class="trust">
  <div class="container trust-card">
    <div>
      <p class="eyebrow">Giving with confidence</p>
      <h2>Support information is published only after internal verification.</h2>
    </div>
    <a class="btn btn-secondary" href="/impact">See our accountability approach</a>
  </div>
</section>

<style>
  .causes{padding:105px 0;background:var(--ivory);color:#2b1827}
  .grid{display:grid;grid-template-columns:repeat(2,1fr);gap:20px}
  article{overflow:hidden;border:1px solid rgba(80,45,70,.13);border-radius:28px;background:#fff;box-shadow:0 20px 55px rgba(60,30,50,.06)}
  article.featured{grid-column:span 2;display:grid;grid-template-columns:1.05fr .95fr}
  .media{position:relative;min-height:320px;background:radial-gradient(circle at 68% 26%,rgba(225,189,106,.34),transparent 15rem),linear-gradient(145deg,#5c1a64,#140816)}
  article.featured .media{min-height:470px}
  .media img{width:100%;height:100%;object-fit:cover;position:absolute;inset:0}
  .placeholder{height:100%;display:grid;place-items:center;color:var(--gold-bright);font:600 4rem/1 'Cormorant Garamond',Georgia,serif}
  .badge{position:absolute;top:20px;left:20px;border:1px solid rgba(255,255,255,.22);border-radius:999px;padding:7px 11px;background:rgba(12,5,13,.56);backdrop-filter:blur(8px);color:var(--champagne);font-size:.7rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase}
  .body{padding:30px}
  article.featured .body{display:flex;justify-content:center;flex-direction:column;padding:48px}
  h2{margin:0;color:#3f213b;font:600 clamp(2rem,4vw,3.4rem)/.98 'Cormorant Garamond',Georgia,serif}
  h2 a:hover{color:#8e6020}
  .body>p{color:#6b5a67}
  .progress{margin-top:24px}
  .bar{height:7px;overflow:hidden;border-radius:99px;background:#eadfce}
  .bar span{display:block;height:100%;border-radius:inherit;background:linear-gradient(90deg,#8b6223,#e1bd6a)}
  .numbers{display:flex;justify-content:space-between;gap:20px;margin-top:9px;font-size:.78rem}
  .numbers strong{color:#6b4320}.numbers span{color:#8c7b86}
  .learn{display:inline-block;margin-top:24px;color:#8e6020;font-size:.82rem;font-weight:700}
  .empty{max-width:760px;margin:auto;padding:70px;text-align:center;background:#fff;border-color:rgba(80,45,70,.12)}
  .mark{display:grid;width:62px;height:62px;place-items:center;margin:auto;border:1px solid rgba(166,112,37,.3);border-radius:50%;color:#8e6020;font:600 1.4rem/1 'Cormorant Garamond',Georgia,serif}
  .empty h2{margin-top:26px}.empty p{color:#6b5a67}
  .trust{padding:86px 0;background:#090409}
  .trust-card{display:flex;align-items:end;justify-content:space-between;gap:40px;border:1px solid var(--line);border-radius:30px;padding:46px;background:linear-gradient(135deg,rgba(100,25,111,.25),rgba(255,255,255,.02))}
  .trust-card h2{max-width:760px;color:var(--ivory)}
  @media(max-width:850px){.grid{grid-template-columns:1fr}article.featured{grid-column:auto;display:block}.trust-card{align-items:flex-start;flex-direction:column}}
  @media(max-width:560px){.causes{padding:82px 0}.body,article.featured .body{padding:26px}.empty{padding:42px 24px}}
</style>
