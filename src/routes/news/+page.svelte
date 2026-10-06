<svelte:head>
  <title>Stories | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="News and stories from Queen Tovah Cares Foundation International." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
</script>

<PageHero
  eyebrow="News & stories"
  title="Stories of service,"
  accent="care and community."
  copy="This is where verified Foundation activities, partnerships, humanitarian interventions and community stories will be published."
/>

<section class="stories">
  <div class="container">
    <article class="featured">
      <div class="visual"><span>2025</span><strong>Youth & Sports</strong></div>
      <div class="copy">
        <p class="eyebrow">Featured activity</p>
        <h2>Supporting youth unity through the Amawbia August League.</h2>
        <p>
          Queen Tovah Cares Foundation International sponsored the 2025 Amawbia August League football
          tournament as part of its support for sports, youth engagement and community unity in Anambra.
        </p>
        <span class="status">Full story and official event photography to be added.</span>
      </div>
    </article>

    <div class="coming">
      <p class="eyebrow">Editorial standard</p>
      <h3>Only verified Foundation stories will be published.</h3>
      <p>As official records and photography are supplied, this section will grow into a searchable news and impact archive.</p>
    </div>
  </div>
</section>

<style>
  .stories{padding:110px 0;background:var(--ivory);color:#2a1926}
  .featured{display:grid;grid-template-columns:.95fr 1.05fr;overflow:hidden;border:1px solid rgba(80,45,70,.14);border-radius:32px;background:#fffaf2;box-shadow:0 24px 60px rgba(60,30,50,.08)}
  .visual{min-height:470px;display:flex;align-items:flex-start;justify-content:flex-end;flex-direction:column;padding:38px;background:radial-gradient(circle at 65% 30%,rgba(225,189,106,.34),transparent 24%),linear-gradient(145deg,#5d1965,#140816);color:var(--champagne)}
  .visual span{color:var(--gold-bright);font-size:.78rem;font-weight:700;letter-spacing:.14em}
  .visual strong{margin-top:6px;font:600 2.6rem/1 'Cormorant Garamond',Georgia,serif}
  .copy{padding:58px}
  .copy .eyebrow{color:#8e6020}
  h2{margin:0;color:#40213c;font:600 clamp(2.4rem,5vw,4.4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .copy>p:not(.eyebrow){margin:24px 0 0;color:#695966}
  .status{display:block;margin-top:30px;border-top:1px solid rgba(80,45,70,.12);padding-top:20px;color:#9a825b;font-size:.8rem}
  .coming{max-width:760px;margin:80px auto 0;text-align:center}
  .coming .eyebrow{justify-content:center;color:#8e6020}
  .coming h3{margin:0;color:#43213f;font:600 2.4rem/1 'Cormorant Garamond',Georgia,serif}
  .coming p{color:#6f5e6a}
  @media(max-width:820px){.featured{grid-template-columns:1fr}.visual{min-height:340px}.copy{padding:34px 26px}}
</style>
