<svelte:head>
  <title>Reports & Resources | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Official Queen Tovah Cares Foundation International reports, policies, publications and media resources." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  let { data } = $props();

  const labels: Record<string,string> = {
    'annual-report': 'Annual report',
    'impact-report': 'Impact report',
    'policy': 'Policy',
    'press-kit': 'Press kit',
    'publication': 'Publication'
  };
</script>

<PageHero
  eyebrow="Reports & resources"
  title="Transparency should be"
  accent="easy to find."
  copy="Official reports, policies, publications and media resources are published here through the Foundation's review workflow."
/>

<section class="resources">
  <div class="container">
    {#if data.resources.length}
      <div class="resource-grid">
        {#each data.resources as item}
          <article>
            <div class="thumb">
              {#if item.thumbnail}<img src={item.thumbnail} alt="" loading="lazy" />{:else}<span>QT</span>{/if}
            </div>
            <div class="body">
              <div class="meta"><span>{labels[item.category] || item.category}</span>{#if item.year}<span>{item.year}</span>{/if}</div>
              <h2>{item.title}</h2>
              <p>{item.summary}</p>
              <a href={`/resources/${item.slug}`}>View resource ↗</a>
              {#if !item.file && !item.external_url}<span class="pending">Document publication pending</span>{/if}
            </div>
          </article>
        {/each}
      </div>
    {:else}
      <div class="empty card">
        <span>QT</span>
        <h2>Official publications will appear here.</h2>
        <p>Administrators can publish annual reports, impact reports, policies, press kits and other resources without changing website code.</p>
      </div>
    {/if}
  </div>
</section>

<section class="trust">
  <div class="container trust-grid">
    <div><p class="eyebrow">A public record</p><h2>Documents should remain accessible, attributable and current.</h2></div>
    <p>The resource library separates approved Foundation material from third-party coverage, helping partners, donors, journalists and communities find the official record.</p>
  </div>
</section>

<style>
  .resources{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .resource-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:18px}
  article{display:grid;grid-template-columns:160px 1fr;overflow:hidden;border:1px solid rgba(80,45,70,.12);border-radius:26px;background:#fff}
  .thumb{min-height:260px;display:grid;place-items:center;background:radial-gradient(circle at 65% 24%,rgba(225,189,106,.25),transparent 10rem),linear-gradient(145deg,#4c1553,#150817);color:var(--gold-bright);font:600 2.8rem/1 'Cormorant Garamond',Georgia,serif}
  .thumb img{width:100%;height:100%;object-fit:cover}
  .body{padding:26px}
  .meta{display:flex;justify-content:space-between;gap:12px;color:#9b6c29;font-size:.68rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
  h2{margin:38px 0 10px;color:#43213f;font:600 2rem/1 'Cormorant Garamond',Georgia,serif}
  .body p{color:#6d5b68;font-size:.88rem}
  .body a,.pending{display:inline-block;margin-top:18px;color:#8e6020;font-size:.78rem;font-weight:700}.pending{color:#9a8995}
  .empty{max-width:760px;margin:auto;padding:64px;text-align:center;background:#fff;border-color:rgba(80,45,70,.12)}
  .empty>span{display:grid;width:60px;height:60px;place-items:center;margin:auto;border:1px solid rgba(166,112,37,.28);border-radius:50%;color:#8e6020;font:600 1.3rem/1 'Cormorant Garamond',Georgia,serif}
  .empty h2{margin:24px 0 10px}.empty p{color:#6d5b68}
  .trust{padding:88px 0;background:#0a040a}
  .trust-grid{display:grid;grid-template-columns:1fr .9fr;gap:72px;align-items:end}.trust-grid h2{margin:0;color:var(--ivory);font:600 clamp(2.3rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}.trust-grid>p{color:#ae9ead}
  @media(max-width:900px){.resource-grid,.trust-grid{grid-template-columns:1fr}}
  @media(max-width:560px){article{grid-template-columns:1fr}.thumb{min-height:190px}}
</style>
