<script lang="ts">
  import { page } from '$app/state';
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();
  const { partner, collaborations, activity } = data;

  const typeLabels: Record<string,string> = {
    corporate: 'Corporate',
    nonprofit: 'Nonprofit / NGO',
    government: 'Government / public institution',
    education: 'Education / research',
    media: 'Media',
    community: 'Community organisation',
    professional: 'Professional body',
    other: 'Partner institution'
  };

  const statusLabels: Record<string,string> = {
    strategic: 'Strategic partner',
    active: 'Active partner',
    project: 'Project partner',
    supporter: 'Supporter / sponsor',
    completed: 'Completed collaboration'
  };

  const collaborationLabels: Record<string,string> = {
    planned: 'Planned',
    active: 'Active',
    completed: 'Completed',
    ongoing: 'Ongoing'
  };

  const organizationSchema = $derived(
    JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'Organization',
      name: partner.title,
      ...(partner.website ? { url: partner.website } : {}),
      ...(partner.logo ? { logo: partner.logo } : {}),
      description: partner.tagline || partner.description,
      ...(partner.location
        ? {
            address: {
              '@type': 'PostalAddress',
              addressLocality: partner.city || undefined,
              addressCountry: partner.country || undefined
            }
          }
        : {}),
      memberOf: {
        '@type': 'NGO',
        name: 'Queen Tovah Cares Foundation International',
        url: page.url.origin
      }
    }).replace(/</g, '\\u003c')
  );
</script>

<svelte:head>
  <title>{partner.seo_title || partner.title} | Queen Tovah Partners</title>
  <meta name="description" content={partner.seo_description || partner.tagline || partner.description} />
  {#if partner.seo_keywords}<meta name="keywords" content={partner.seo_keywords} />{/if}
  <meta property="og:title" content={partner.seo_title || partner.title} />
  <meta property="og:description" content={partner.seo_description || partner.tagline || partner.description} />
  {#if partner.hero_image}<meta property="og:image" content={partner.hero_image} />{:else if partner.logo}<meta property="og:image" content={partner.logo} />{/if}
  {@html `<script type="application/ld+json">${organizationSchema}</script>`}
</svelte:head>

<PageHero
  eyebrow={typeLabels[partner.partner_type] || 'Verified partner'}
  title={partner.title}
  copy={partner.tagline || partner.description}
/>

<section class="profile">
  <div class="container profile-grid">
    <aside class="identity card">
      <div class="logo-wrap">
        {#if partner.logo}
          <img src={partner.logo} alt={partner.title} />
        {:else}
          <span>{partner.title.slice(0,2).toUpperCase()}</span>
        {/if}
      </div>

      <span class="verified">✓ Verified relationship</span>
      <h2>{statusLabels[partner.relationship_status] || partner.relationship_status}</h2>

      <dl>
        {#if partner.relationship_since}
          <div><dt>Relationship since</dt><dd>{new Intl.DateTimeFormat('en',{dateStyle:'medium'}).format(new Date(partner.relationship_since))}</dd></div>
        {/if}
        {#if partner.relationship_ended}
          <div><dt>Completed</dt><dd>{new Intl.DateTimeFormat('en',{dateStyle:'medium'}).format(new Date(partner.relationship_ended))}</dd></div>
        {/if}
        {#if partner.location}<div><dt>Location</dt><dd>{partner.location}</dd></div>{/if}
      </dl>

      {#if partner.website}
        <a class="btn btn-primary" href={partner.website} target="_blank" rel="noreferrer">Visit institution website ↗</a>
      {/if}
      {#if partner.reference_url}
        <a class="reference" href={partner.reference_url} target="_blank" rel="noreferrer">Open public relationship reference ↗</a>
      {/if}
    </aside>

    <article>
      {#if partner.hero_image}
        <img class="hero-image" src={partner.hero_image} alt={partner.hero_alt || partner.title} />
      {/if}

      <div class="body">
        {#if partner.body}
          {#each partner.body.split('\n\n').filter(Boolean) as paragraph}<p>{paragraph}</p>{/each}
        {:else if partner.description}
          <p>{partner.description}</p>
        {:else}
          <p>This verified profile records an approved Foundation relationship with {partner.title}.</p>
        {/if}
      </div>
    </article>
  </div>
</section>

{#if collaborations.length}
<section class="collaborations">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">Collaboration history</p>
        <h2 class="section-title">What we have done together.</h2>
      </div>
      <p class="section-copy">Only verified collaboration records are displayed here.</p>
    </div>

    <div class="collaboration-grid">
      {#each collaborations as item}
        <article class:featured={item.featured}>
          <div class="top">
            <span>{collaborationLabels[item.collaboration_status] || item.collaboration_status}</span>
            <span class="check">✓ Verified</span>
          </div>
          <h3>{item.title}</h3>
          <p>{item.summary}</p>

          <div class="links">
            {#if item.program_slug}<a href={`/programs/${item.program_slug}`}>Program: {item.program_title} ↗</a>{/if}
            {#if item.campaign_slug}<a href={`/causes/${item.campaign_slug}`}>Cause: {item.campaign_title} ↗</a>{/if}
            {#if item.source_url}<a href={item.source_url} target="_blank" rel="noreferrer">Supporting source ↗</a>{/if}
          </div>

          <div class="dates">
            {#if item.starts_at}<span>From {new Intl.DateTimeFormat('en',{dateStyle:'medium'}).format(new Date(item.starts_at))}</span>{/if}
            {#if item.ends_at}<span>to {new Intl.DateTimeFormat('en',{dateStyle:'medium'}).format(new Date(item.ends_at))}</span>{/if}
            {#if item.location_label}<span>{item.location_label}</span>{/if}
          </div>
        </article>
      {/each}
    </div>
  </div>
</section>
{/if}

{#if activity.length}
<section class="activity">
  <div class="container">
    <div class="activity-head">
      <div>
        <p class="eyebrow">Related activity</p>
        <h2 class="section-title">See the work connected to this relationship.</h2>
      </div>
      <a href="/activity">Full activity journal ↗</a>
    </div>

    <div class="activity-list">
      {#each activity.slice(0, 6) as update}
        <a href={`/activity/${update.slug}`}>
          <span>{new Intl.DateTimeFormat('en',{dateStyle:'medium'}).format(new Date(update.occurred_at))}</span>
          <div>
            <small>{update.kind.replace('-', ' ')}</small>
            <h3>{update.title}</h3>
            <p>{update.summary}</p>
          </div>
          <em>↗</em>
        </a>
      {/each}
    </div>
  </div>
</section>
{/if}

<section class="partner-cta">
  <div class="container cta-card">
    <div>
      <p class="eyebrow">Build something useful together</p>
      <h2>Interested in working with the Foundation?</h2>
      <p>Institutional enquiries are routed through the Foundation contact system for review.</p>
    </div>
    <a class="btn btn-primary" href="/contact">Discuss a partnership ↗</a>
  </div>
</section>

<style>
  .profile{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .profile-grid{display:grid;grid-template-columns:330px minmax(0,1fr);gap:64px;align-items:start}
  .identity{position:sticky;top:120px;border-color:rgba(80,45,70,.13);padding:28px;background:#fff;color:#3d2039}
  .logo-wrap{height:190px;display:grid;place-items:center;border:1px solid rgba(80,45,70,.08);border-radius:20px;background:#fbf7f1}
  .logo-wrap img{max-width:75%;max-height:110px;object-fit:contain}.logo-wrap span{color:#8e6020;font:600 3rem/1 'Cormorant Garamond',Georgia,serif}
  .verified{display:inline-flex;margin-top:22px;border:1px solid rgba(85,120,80,.25);border-radius:999px;padding:6px 9px;background:rgba(85,120,80,.07);color:#587252;font-size:.66rem;font-weight:800;text-transform:uppercase}
  .identity h2{margin:16px 0;color:#43213f;font:600 2rem/1 'Cormorant Garamond',Georgia,serif}
  dl{margin:0}dl div{border-bottom:1px solid rgba(80,45,70,.08);padding:12px 0}dt{color:#9a8059;font-size:.66rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em}dd{margin:5px 0 0;color:#5d4b58;font-size:.84rem}
  .identity .btn{width:100%;margin-top:22px}.reference{display:block;margin-top:14px;color:#8e6020;font-size:.76rem;font-weight:700;text-align:center}
  .hero-image{width:100%;max-height:580px;object-fit:cover;border-radius:30px;box-shadow:0 28px 70px rgba(60,30,50,.12)}
  .body{max-width:820px;margin-top:36px;color:#5f4e5a;font-size:1.06rem;line-height:1.88}.body p{margin:0 0 25px}

  .collaborations{padding:110px 0;background:#0a040a}
  .collaboration-grid{display:grid;grid-template-columns:repeat(2,1fr);gap:16px;margin-top:46px}
  .collaboration-grid article{min-height:320px;display:flex;flex-direction:column;border:1px solid rgba(225,189,106,.14);border-radius:24px;padding:26px;background:rgba(255,255,255,.035)}
  .collaboration-grid article.featured{background:radial-gradient(circle at 80% 18%,rgba(225,189,106,.12),transparent 17rem),linear-gradient(145deg,rgba(77,21,84,.5),rgba(255,255,255,.025))}
  .top{display:flex;justify-content:space-between;gap:12px;color:var(--gold-deep);font-size:.66rem;font-weight:800;text-transform:uppercase}.top .check{color:#9db898}
  .collaboration-grid h3{margin:58px 0 10px;color:var(--champagne);font:600 2rem/1 'Cormorant Garamond',Georgia,serif}.collaboration-grid p{margin:0;color:#aa9aa8}
  .links{display:flex;flex-wrap:wrap;gap:8px 16px;margin-top:auto;padding-top:24px}.links a{color:var(--gold-bright);font-size:.75rem;font-weight:700}
  .dates{display:flex;flex-wrap:wrap;gap:7px 15px;margin-top:14px;border-top:1px solid var(--line);padding-top:14px;color:#8f7d8d;font-size:.7rem}

  .activity{padding:110px 0;background:var(--cream);color:#2b1827}
  .activity .eyebrow{color:#8e6020}.activity .section-title{color:#351e32}
  .activity-head{display:flex;align-items:end;justify-content:space-between;gap:40px}.activity-head>a{color:#8e6020;font-size:.8rem;font-weight:700}
  .activity-list{margin-top:42px;border-top:1px solid rgba(80,45,70,.12)}
  .activity-list>a{display:grid;grid-template-columns:145px 1fr auto;gap:24px;align-items:center;border-bottom:1px solid rgba(80,45,70,.12);padding:22px 0}.activity-list>a>span{color:#9a8059;font-size:.72rem}
  .activity-list small{color:#9b6c29;font-size:.65rem;font-weight:800;text-transform:uppercase}.activity-list h3{margin:6px 0;color:#43213f;font:600 1.8rem/1 'Cormorant Garamond',Georgia,serif}.activity-list p{margin:0;color:#6d5b68;font-size:.84rem}.activity-list em{color:#8e6020;font-style:normal}

  .partner-cta{padding:88px 0;background:#080308}.cta-card{display:flex;align-items:end;justify-content:space-between;gap:44px;border:1px solid var(--line);border-radius:30px;padding:48px;background:linear-gradient(135deg,rgba(100,25,111,.24),rgba(255,255,255,.02))}.cta-card h2{max-width:780px;margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}.cta-card p:not(.eyebrow){color:#ad9daa}.cta-card .btn{flex-shrink:0}

  @media(max-width:880px){.profile-grid{grid-template-columns:1fr}.identity{position:static;max-width:460px}.collaboration-grid{grid-template-columns:1fr}.activity-head,.cta-card{align-items:flex-start;flex-direction:column}}
  @media(max-width:620px){.activity-list>a{grid-template-columns:1fr;gap:8px}.activity-list em{display:none}}
</style>
