<svelte:head>
  <title>Gallery | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Official photo and video gallery for Queen Tovah Cares Foundation International." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  const categories=['Humanitarian Outreach','Education & Scholarships','Youth & Sports','Community Development','Foundation Events','Partnerships'];
</script>

<PageHero
  eyebrow="Gallery"
  title="The mission,"
  accent="documented with dignity."
  copy="Official Foundation photography and video will live here. Until approved media is supplied, we are keeping the gallery intentionally free of stock or invented imagery."
/>

<section class="gallery">
  <div class="container">
    <div class="grid">
      {#each categories as category, i}
        <article class:wide={i===0 || i===5}>
          <span>0{i+1}</span>
          <div><p>{category}</p><small>Official media coming soon</small></div>
        </article>
      {/each}
    </div>
  </div>
</section>

<style>
  .gallery{padding:100px 0 120px;background:#0a040a}
  .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
  article{min-height:290px;display:flex;justify-content:space-between;flex-direction:column;border:1px solid rgba(225,189,106,.18);border-radius:26px;padding:24px;background:radial-gradient(circle at 72% 25%,rgba(225,189,106,.12),transparent 14rem),linear-gradient(145deg,rgba(100,25,111,.28),rgba(255,255,255,.018))}
  article.wide{grid-column:span 2}
  article span{color:var(--gold-deep);font-size:.72rem;font-weight:700}
  article p{margin:0;color:var(--champagne);font:600 2rem/1 'Cormorant Garamond',Georgia,serif}
  article small{display:block;margin-top:8px;color:#8f7f8e}
  @media(max-width:780px){.grid{grid-template-columns:1fr 1fr}article.wide{grid-column:span 1}}
  @media(max-width:520px){.grid{grid-template-columns:1fr}}
</style>
