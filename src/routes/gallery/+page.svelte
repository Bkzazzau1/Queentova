<svelte:head>
  <title>Gallery | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Official photo and video gallery for Queen Tovah Cares Foundation International." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();
  const categories=['Humanitarian Outreach','Education & Scholarships','Youth & Sports','Community Development','Foundation Events','Partnerships'];
</script>

<PageHero
  eyebrow="Gallery"
  title="The mission,"
  accent="documented with dignity."
  copy="Official photography and video from Foundation activities. Stock images are never presented as Foundation work."
/>

<section class="gallery">
  <div class="container">
    <div class="grid">
      {#if data.gallery.length}
        {#each data.gallery as item, i}
          <article class:wide={i===0 || i % 6 === 5} class:with-media={Boolean(item.image)}>
            {#if item.image}
              <img src={item.image} alt={item.alt_text || item.title} loading="lazy" />
            {/if}
            <span>0{i+1}</span>
            <div>
              <p>{item.title}</p>
              <small>{item.caption || item.category || 'Foundation media'}</small>
              {#if item.media_type === 'video' && item.video_url}
                <a href={item.video_url} target="_blank" rel="noreferrer">Watch video ↗</a>
              {/if}
            </div>
          </article>
        {/each}
      {:else}
        {#each categories as category, i}
          <article class:wide={i===0 || i===5}>
            <span>0{i+1}</span>
            <div><p>{category}</p><small>Official media coming soon</small></div>
          </article>
        {/each}
      {/if}
    </div>
  </div>
</section>

<style>
  .gallery{padding:100px 0 120px;background:#0a040a}
  .grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px}
  article{position:relative;isolation:isolate;overflow:hidden;min-height:290px;display:flex;justify-content:space-between;flex-direction:column;border:1px solid rgba(225,189,106,.18);border-radius:26px;padding:24px;background:radial-gradient(circle at 72% 25%,rgba(225,189,106,.12),transparent 14rem),linear-gradient(145deg,rgba(100,25,111,.28),rgba(255,255,255,.018))}
  article.with-media::after{position:absolute;z-index:-1;inset:0;background:linear-gradient(0deg,rgba(8,3,8,.86),rgba(8,3,8,.12) 68%);content:''}
  article img{position:absolute;z-index:-2;inset:0;width:100%;height:100%;object-fit:cover}
  article.wide{grid-column:span 2}
  article span{color:var(--gold-bright);font-size:.72rem;font-weight:700}
  article p{margin:0;color:var(--champagne);font:600 2rem/1 'Cormorant Garamond',Georgia,serif}
  article small{display:block;margin-top:8px;color:#b8a9b6}
  article a{display:inline-block;margin-top:10px;color:var(--gold-bright);font-size:.78rem;text-decoration:underline;text-underline-offset:3px}
  @media(max-width:780px){.grid{grid-template-columns:1fr 1fr}article.wide{grid-column:span 1}}
  @media(max-width:520px){.grid{grid-template-columns:1fr}}
</style>
