<svelte:head>
  <title>Impact | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="How Queen Tovah Cares Foundation International approaches humanitarian impact, dignity, accountability and community development." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  const steps = [
    ['Listen','Understand the person, family or community need before deciding what support should look like.'],
    ['Respond','Match assistance to the situation with dignity, practicality and compassion.'],
    ['Empower','Where possible, connect immediate support with education, opportunity or longer-term progress.'],
    ['Learn','Review outcomes and use experience to improve future programs and partnerships.']
  ];
</script>

<PageHero
  eyebrow="Our impact"
  title="Impact measured by"
  accent="human progress."
  copy="We are building an impact model that values both immediate relief and the longer journey toward dignity, opportunity and stronger communities."
/>

<section class="approach">
  <div class="container approach-grid">
    <div>
      <p class="eyebrow">Our approach</p>
      <h2 class="section-title">Care that is responsible, not performative.</h2>
      <p class="section-copy">
        We do not publish invented impact numbers. Verified program results, beneficiary counts and
        documented outcomes will be added as the Foundation's reporting records are prepared for the
        website.
      </p>
    </div>
    <div class="steps">
      {#each steps as step, i}
        <article><span>0{i+1}</span><div><h3>{step[0]}</h3><p>{step[1]}</p></div></article>
      {/each}
    </div>
  </div>
</section>

<section class="accountability">
  <div class="container">
    <p class="eyebrow">Accountability</p>
    <div class="account-grid">
      <article><h3>Verified reporting</h3><p>Public impact figures should be traceable to real programs and documented records.</p></article>
      <article><h3>Human dignity</h3><p>Stories and images should respect beneficiaries rather than turn vulnerability into spectacle.</p></article>
      <article><h3>Partnership clarity</h3><p>Collaborations should state what is being supported, why it matters and how success will be understood.</p></article>
    </div>
  </div>
</section>

<style>
  .approach{padding:112px 0;background:#100711}
  .approach-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:84px}
  .steps{border-top:1px solid var(--line)}
  .steps article{display:grid;grid-template-columns:52px 1fr;gap:20px;border-bottom:1px solid var(--line);padding:27px 0}
  .steps span{padding-top:7px;color:var(--gold-deep);font-size:.72rem;font-weight:700}
  .steps h3{margin:0;color:var(--champagne);font:600 1.8rem/1 'Cormorant Garamond',Georgia,serif}
  .steps p{margin:8px 0 0;color:#a897a7}
  .accountability{padding:112px 0;background:var(--cream);color:#2b1827}
  .accountability .eyebrow{color:#8e6020}
  .account-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px;margin-top:34px}
  .account-grid article{border:1px solid rgba(80,45,70,.13);border-radius:24px;padding:30px;background:rgba(255,255,255,.44)}
  .account-grid h3{margin:0;color:#44233f;font:600 1.7rem/1 'Cormorant Garamond',Georgia,serif}
  .account-grid p{margin:14px 0 0;color:#6c5a67}
  @media(max-width:850px){.approach-grid{grid-template-columns:1fr;gap:48px}.account-grid{grid-template-columns:1fr}}
</style>
