<svelte:head>
  <title>Support the Mission | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Support Queen Tovah Cares Foundation International through verified humanitarian causes, sponsorship and partnerships." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();

  const profile = $derived(data.siteProfile);
  const openCauses = $derived(data.campaigns.filter((campaign) => campaign.accepting_support).slice(0, 3));
</script>

<PageHero
  eyebrow="Support the mission"
  title="Help goodness"
  accent="travel further."
  copy="Support can take many forms — verified giving, sponsorship, institutional partnership, professional expertise or community collaboration."
/>

<section class="support">
  <div class="container support-grid">
    <article>
      <span>01</span>
      <h2>Give</h2>
      <p>Support verified humanitarian, education and community causes through an approved Foundation channel.</p>
      {#if profile?.donation_url}<a href={profile.donation_url} target="_blank" rel="noreferrer">Official giving channel ↗</a>{:else}<a href="/causes">View verified causes ↗</a>{/if}
    </article>
    <article><span>02</span><h2>Sponsor</h2><p>Back a scholarship, youth activity, humanitarian intervention or community-focused program.</p><a href="/contact">Discuss sponsorship ↗</a></article>
    <article><span>03</span><h2>Partner</h2><p>Organizations and institutions can collaborate where shared resources can create stronger outcomes.</p><a href="/get-involved">Partnership pathways ↗</a></article>
  </div>
</section>

{#if openCauses.length}
<section class="active-causes">
  <div class="container">
    <div class="heading">
      <div><p class="eyebrow">Open causes</p><h2 class="section-title">Choose a verified cause.</h2></div>
      <a href="/causes">View all causes ↗</a>
    </div>
    <div class="cause-grid">
      {#each openCauses as campaign}
        <a href={`/causes/${campaign.slug}`}>
          <span>{campaign.progress_percent !== null ? `${campaign.progress_percent}% of verified goal` : 'Foundation cause'}</span>
          <h3>{campaign.title}</h3>
          <p>{campaign.summary}</p>
        </a>
      {/each}
    </div>
  </div>
</section>
{/if}

<section class="notice">
  <div class="container notice-card">
    <div>
      <p class="eyebrow">Giving safely</p>
      <h2>We will never publish unverified payment details.</h2>
      <p>
        {profile?.donation_url
          ? 'The official giving button on this page is controlled from the Foundation administration profile.'
          : 'No public payment gateway has been approved in the Foundation profile yet. Never send money to an account claiming to represent the Foundation unless it is confirmed here.'}
      </p>
    </div>
    {#if profile?.donation_url}
      <a class="btn btn-primary" href={profile.donation_url} target="_blank" rel="noreferrer">Use official giving channel ↗</a>
    {:else}
      <a class="btn btn-primary" href="/contact">Contact the Foundation ↗</a>
    {/if}
  </div>
</section>

<style>
  .support{padding:110px 0;background:var(--ivory);color:#2a1926}
  .support-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
  .support article{min-height:350px;display:flex;flex-direction:column;border:1px solid rgba(80,45,70,.14);border-radius:26px;padding:30px;background:rgba(255,255,255,.58)}
  .support article>span{color:#9d6b25;font-size:.74rem;font-weight:700}
  .support article h2{margin:96px 0 10px;color:#452341;font:600 2.5rem/1 'Cormorant Garamond',Georgia,serif}
  .support article p{margin:0;color:#6d5b68}
  .support article a{margin-top:auto;padding-top:28px;color:#8e6020;font-size:.8rem;font-weight:700}
  .active-causes{padding:100px 0;background:var(--cream);color:#2a1926}
  .heading{display:flex;align-items:end;justify-content:space-between;gap:30px}.heading .eyebrow{color:#8e6020}.heading .section-title{color:#3c2238}.heading>a{color:#8e6020;font-size:.8rem;font-weight:700}
  .cause-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px;margin-top:44px}
  .cause-grid a{min-height:260px;display:flex;flex-direction:column;border:1px solid rgba(80,45,70,.12);border-radius:24px;padding:25px;background:#fff}
  .cause-grid span{color:#9d6b25;font-size:.7rem;font-weight:700;text-transform:uppercase}.cause-grid h3{margin:60px 0 10px;color:#43213f;font:600 1.8rem/1 'Cormorant Garamond',Georgia,serif}.cause-grid p{margin:0;color:#6d5b68;font-size:.88rem}
  .notice{padding:90px 0;background:#090409}
  .notice-card{display:flex;align-items:flex-end;justify-content:space-between;gap:44px;border:1px solid var(--line);border-radius:30px;padding:50px;background:linear-gradient(135deg,rgba(100,25,111,.22),rgba(255,255,255,.02))}
  .notice-card h2{max-width:760px;margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4.1rem)/.98 'Cormorant Garamond',Georgia,serif}
  .notice-card p:not(.eyebrow){max-width:700px;color:#ae9ead}
  @media(max-width:820px){.support-grid,.cause-grid{grid-template-columns:1fr}.notice-card,.heading{align-items:flex-start;flex-direction:column}.support article{min-height:270px}.support article h2{margin-top:62px}}
</style>
