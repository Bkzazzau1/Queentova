<svelte:head>
  <title>Press & Media Centre | Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Official press resources, Foundation stories, media information and verified materials from Queen Tovah Cares Foundation International."
  />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();

  const pressResources = data.resources.filter((item) =>
    ['press-kit', 'annual-report', 'impact-report', 'publication'].includes(item.category)
  );
  const stories = data.stories.slice(0, 6);
  const founderMedia = data.founderMedia.slice(0, 4);

  function founderPhoto(item: (typeof data.founderMedia)[number]) {
    return item.photos.find((photo) => photo.is_primary && photo.image_url) ??
      item.photos.find((photo) => photo.image_url) ??
      null;
  }
</script>

<PageHero
  eyebrow="Press & media centre"
  title="Use the"
  accent="official record."
  copy="A single place for journalists, partners and researchers to find verified Foundation stories, reports, public resources and official contact channels."
/>

<section class="media-intro">
  <div class="container intro-grid">
    <div>
      <p class="eyebrow">For media professionals</p>
      <h2 class="section-title">Accuracy matters before amplification.</h2>
    </div>
    <div class="intro-copy">
      <p>
        Use this website as the reference point for official Foundation material. Where a story cites
        third-party coverage, the source is clearly identified. Foundation-owned reports and media
        resources are separated into the official resource library.
      </p>
      <div class="quick-actions">
        <a href="/founder/jessie-ifeoma-udoka-menuba">Founder public profile ↗</a>
        <a href="/resources">Reports & resources ↗</a>
        <a href="/governance">Governance & transparency ↗</a>
      </div>
    </div>
  </div>
</section>

{#if pressResources.length}
<section class="press-resources">
  <div class="container">
    <div class="section-head">
      <div><p class="eyebrow">Press resources</p><h2 class="section-title">Download the approved material.</h2></div>
      <a href="/resources">All resources ↗</a>
    </div>
    <div class="resource-grid">
      {#each pressResources.slice(0, 6) as item}
        <a href={`/resources/${item.slug}`}>
          <span>{item.year || item.category.replace('-', ' ')}</span>
          <h3>{item.title}</h3>
          <p>{item.summary}</p>
          <em>Open resource ↗</em>
        </a>
      {/each}
    </div>
  </div>
</section>
{/if}


{#if founderMedia.length}
<section class="founder-media">
  <div class="container">
    <div class="section-head founder-media-head">
      <div>
        <p class="eyebrow">Founder recognition & media</p>
        <h2 class="section-title">Awards, coverage and publication records.</h2>
      </div>
      <a href="/founder/media">Open founder media archive ↗</a>
    </div>

    <div class="founder-media-grid">
      {#each founderMedia as item, i}
        {@const photo = founderPhoto(item)}
        <a class:lead-founder={i === 0} href={`/founder/media/${item.slug}`}>
          <div class="founder-visual">
            {#if photo}
              <img src={photo.image_url} alt={photo.alt_text || item.title} loading="lazy" />
            {:else}
              <span>QT</span>
            {/if}
          </div>
          <div class="founder-copy">
            <span>{item.kind.replace('-', ' ')}</span>
            <h3>{item.title}</h3>
            <p>{item.summary}</p>
            <small>{item.source_name} ↗</small>
          </div>
        </a>
      {/each}
    </div>
  </div>
</section>
{/if}

<section class="coverage">
  <div class="container">
    <div class="section-head">
      <div><p class="eyebrow">Latest stories</p><h2 class="section-title">Published activity & coverage.</h2></div>
      <a href="/news">All stories ↗</a>
    </div>

    {#if stories.length}
      <div class="story-grid">
        {#each stories as story, i}
          <a class:featured={i === 0} href={`/news/${story.slug}`}>
            <div class="visual">
              {#if story.hero_image}<img src={story.hero_image} alt={story.hero_alt || story.title} loading="lazy" />{:else}<span>QT</span>{/if}
            </div>
            <div class="body">
              <span>{story.category.replace('-', ' ')}</span>
              <h3>{story.title}</h3>
              <p>{story.excerpt}</p>
            </div>
          </a>
        {/each}
      </div>
    {:else}
      <div class="empty">Published Foundation stories will appear here automatically.</div>
    {/if}
  </div>
</section>

<section class="media-contact">
  <div class="container contact-card">
    <div>
      <p class="eyebrow">Media enquiries</p>
      <h2>Need confirmation, an interview or approved material?</h2>
      <p>
        Use the Foundation contact route and select <strong>Media</strong>. This keeps requests inside
        the official enquiry system.
      </p>
    </div>
    <a class="btn btn-primary" href="/contact">Send a media enquiry ↗</a>
  </div>
</section>

<style>
  .media-intro{padding:110px 0;background:var(--ivory);color:#2b1827}
  .intro-grid{display:grid;grid-template-columns:1fr .9fr;gap:82px}
  .media-intro .eyebrow,.coverage .eyebrow{color:#8e6020}
  .media-intro .section-title{color:#351e32}
  .intro-copy>p{margin:35px 0 0;color:#6d5b68}
  .quick-actions{display:flex;flex-wrap:wrap;gap:8px 18px;margin-top:28px}
  .quick-actions a{color:#8e6020;font-size:.8rem;font-weight:700}

  .press-resources{padding:110px 0;background:#0d060e}
  .section-head{display:flex;align-items:end;justify-content:space-between;gap:40px}
  .section-head>a{color:var(--gold-bright);font-size:.8rem;font-weight:700}
  .resource-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:14px;margin-top:46px}
  .resource-grid a{min-height:270px;display:flex;flex-direction:column;border:1px solid rgba(225,189,106,.15);border-radius:22px;padding:24px;background:rgba(255,255,255,.03)}
  .resource-grid span{color:var(--gold-deep);font-size:.68rem;font-weight:800;text-transform:uppercase}
  .resource-grid h3{margin:54px 0 9px;color:var(--champagne);font:600 1.7rem/1 'Cormorant Garamond',Georgia,serif}
  .resource-grid p{margin:0;color:#a998a8;font-size:.84rem}
  .resource-grid em{margin-top:auto;padding-top:18px;color:var(--gold-bright);font-size:.75rem;font-style:normal;font-weight:700}

  .founder-media{padding:110px 0;background:var(--ivory);color:#2b1827}
  .founder-media .eyebrow{color:#8e6020}
  .founder-media .section-title{color:#351e32}
  .founder-media-head>a{color:#8e6020}
  .founder-media-grid{display:grid;grid-template-columns:1.2fr .8fr;grid-template-rows:230px 230px 230px;gap:14px;margin-top:46px}
  .founder-media-grid>a{display:grid;grid-template-columns:180px 1fr;overflow:hidden;border:1px solid rgba(80,45,70,.12);border-radius:24px;background:#fff}
  .founder-media-grid>a.lead-founder{grid-row:1/4;grid-template-columns:1fr;grid-template-rows:1.1fr .9fr}
  .founder-visual{display:grid;place-items:center;min-height:0;background:linear-gradient(145deg,#4c1553,#150817);color:var(--gold-bright);font:600 2.6rem/1 'Cormorant Garamond',Georgia,serif}
  .founder-visual img{width:100%;height:100%;object-fit:cover}
  .founder-copy{padding:20px}
  .founder-copy>span{color:#9b6c29;font-size:.66rem;font-weight:800;text-transform:uppercase}
  .founder-copy h3{margin:9px 0 8px;color:#43213f;font:600 1.55rem/1 'Cormorant Garamond',Georgia,serif}
  .lead-founder .founder-copy h3{font-size:2.4rem}
  .founder-copy p{margin:0;color:#6d5b68;font-size:.82rem}
  .founder-copy small{display:block;margin-top:14px;color:#8e6020}
  .coverage{padding:112px 0;background:var(--cream);color:#2b1827}
  .coverage .section-title{color:#351e32}
  .coverage .section-head>a{color:#8e6020}
  .story-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:46px}
  .story-grid>a{overflow:hidden;border:1px solid rgba(80,45,70,.12);border-radius:24px;background:#fff}
  .story-grid>a.featured{grid-column:span 2}
  .visual{height:220px;display:grid;place-items:center;background:linear-gradient(145deg,#4c1553,#150817);color:var(--gold-bright);font:600 2.5rem/1 'Cormorant Garamond',Georgia,serif}
  .featured .visual{height:300px}
  .visual img{width:100%;height:100%;object-fit:cover}
  .body{padding:22px}
  .body>span{color:#9b6c29;font-size:.68rem;font-weight:800;text-transform:uppercase}
  .body h3{margin:10px 0 8px;color:#43213f;font:600 1.8rem/1 'Cormorant Garamond',Georgia,serif}
  .body p{margin:0;color:#6d5b68;font-size:.84rem}
  .empty{margin-top:42px;border:1px dashed rgba(80,45,70,.18);border-radius:20px;padding:30px;color:#6d5b68}

  .media-contact{padding:88px 0;background:#080308}
  .contact-card{display:flex;align-items:end;justify-content:space-between;gap:44px;border:1px solid var(--line);border-radius:30px;padding:48px;background:linear-gradient(135deg,rgba(100,25,111,.25),rgba(255,255,255,.02))}
  .contact-card h2{max-width:790px;margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .contact-card p:not(.eyebrow){max-width:720px;color:#ad9daa}

  @media(max-width:880px){.intro-grid{grid-template-columns:1fr;gap:38px}.resource-grid,.story-grid{grid-template-columns:1fr 1fr}.founder-media-grid{grid-template-columns:1fr;grid-template-rows:auto}.founder-media-grid>a,.founder-media-grid>a.lead-founder{grid-row:auto;grid-template-columns:180px 1fr;grid-template-rows:auto;min-height:220px}.contact-card{align-items:flex-start;flex-direction:column}}
  @media(max-width:600px){.resource-grid,.story-grid{grid-template-columns:1fr}.story-grid>a.featured{grid-column:auto}.founder-media-grid>a,.founder-media-grid>a.lead-founder{grid-template-columns:1fr}.founder-visual{min-height:220px}.section-head{align-items:flex-start;flex-direction:column}}
</style>
