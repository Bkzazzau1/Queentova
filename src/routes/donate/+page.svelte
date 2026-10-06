<svelte:head>
  <title>Support the Mission | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Support Queen Tovah Cares Foundation International through humanitarian partnerships, sponsorship and giving." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
</script>

<PageHero
  eyebrow="Support the mission"
  title="Help goodness"
  accent="travel further."
  copy="Support can take many forms — giving, sponsorship, institutional partnership, professional expertise or community collaboration."
/>

<section class="support">
  <div class="container support-grid">
    <article><span>01</span><h2>Give</h2><p>Support humanitarian, education and community programs. Verified payment channels will be connected before public launch.</p></article>
    <article><span>02</span><h2>Sponsor</h2><p>Back a scholarship, youth activity, humanitarian intervention or community-focused program.</p></article>
    <article><span>03</span><h2>Partner</h2><p>Organizations and institutions can collaborate on initiatives where shared resources can create stronger outcomes.</p></article>
  </div>
</section>

<section class="notice">
  <div class="container notice-card">
    <div>
      <p class="eyebrow">Giving safely</p>
      <h2>We will never publish unverified payment details.</h2>
      <p>Official donation accounts and payment gateways will appear here only after Foundation approval and verification.</p>
    </div>
    <a class="btn btn-primary" href="/contact">Contact the Foundation ↗</a>
  </div>
</section>

<style>
  .support{padding:110px 0;background:var(--ivory);color:#2a1926}
  .support-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:18px}
  article{min-height:330px;border:1px solid rgba(80,45,70,.14);border-radius:26px;padding:30px;background:rgba(255,255,255,.48)}
  article span{color:#9d6b25;font-size:.74rem;font-weight:700}
  article h2{margin:100px 0 10px;color:#452341;font:600 2.5rem/1 'Cormorant Garamond',Georgia,serif}
  article p{margin:0;color:#6d5b68}
  .notice{padding:90px 0;background:#090409}
  .notice-card{display:flex;align-items:flex-end;justify-content:space-between;gap:44px;border:1px solid var(--line);border-radius:30px;padding:50px;background:linear-gradient(135deg,rgba(100,25,111,.22),rgba(255,255,255,.02))}
  .notice-card h2{max-width:760px;margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4.1rem)/.98 'Cormorant Garamond',Georgia,serif}
  .notice-card p:not(.eyebrow){max-width:700px;color:#ae9ead}
  @media(max-width:820px){.support-grid{grid-template-columns:1fr}.notice-card{align-items:flex-start;flex-direction:column}article{min-height:260px}article h2{margin-top:62px}}
</style>
