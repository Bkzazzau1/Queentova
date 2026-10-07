<svelte:head>
  <title>Partners & Institutions | Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Verified partners, institutions and collaboration relationships of Queen Tovah Cares Foundation International."
  />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();

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

  const featured = $derived(data.partners.filter((item) => item.featured).slice(0, 3));
  const partners = $derived(data.partners);
</script>

<PageHero
  eyebrow="Partners & institutions"
  title="Collaboration should have"
  accent="a public record."
  copy="This directory contains only relationships that the Foundation has verified for public display. Each profile can show what was done together, the programs involved and the activity connected to the partnership."
/>

{#if featured.length}
<section class="featured">
  <div class="container">
    <div class="featured-grid">
      {#each featured as partner, i}
        <a class:lead={i === 0} href={`/partners/${partner.slug}`}>
          <div class="visual">
            {#if partner.hero_image}
              <img src={partner.hero_image} alt={partner.hero_alt || partner.title} />
            {:else if partner.logo}
              <img class="logo-visual" src={partner.logo} alt={partner.title} />
            {:else}
              <span>QT ×</span>
            {/if}
          </div>
          <div class="copy">
            <div class="meta">
              <span>{typeLabels[partner.partner_type] || partner.partner_type}</span>
              <span class="verified">Verified relationship</span>
            </div>
            <h2>{partner.title}</h2>
            <p>{partner.tagline || partner.description}</p>
            <em>{statusLabels[partner.relationship_status] || partner.relationship_status} ↗</em>
          </div>
        </a>
      {/each}
    </div>
  </div>
</section>
{/if}

<section class="directory">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">Verified directory</p>
        <h2 class="section-title">Institutions connected to the work.</h2>
      </div>
      <p class="section-copy">
        A logo alone is not treated as proof of partnership. Public profiles appear only after the
        relationship has been confirmed in the Foundation administration system.
      </p>
    </div>

    {#if partners.length}
      <div class="partner-grid">
        {#each partners as partner}
          <a href={`/partners/${partner.slug}`}>
            <div class="logo-wrap">
              {#if partner.logo}
                <img src={partner.logo} alt={partner.title} loading="lazy" />
              {:else}
                <span>{partner.title.slice(0,2).toUpperCase()}</span>
              {/if}
            </div>
            <div class="body">
              <div class="top">
                <span>{typeLabels[partner.partner_type] || partner.partner_type}</span>
                <span class="check">✓ Verified</span>
              </div>
              <h3>{partner.title}</h3>
              <p>{partner.tagline || partner.description || 'Verified Foundation relationship.'}</p>
              <div class="bottom">
                <span>{statusLabels[partner.relationship_status] || partner.relationship_status}</span>
                {#if partner.location}<span>{partner.location}</span>{/if}
              </div>
            </div>
          </a>
        {/each}
      </div>
    {:else}
      <div class="empty card">
        <span>QT</span>
        <h2>No institution is displayed until the relationship is verified.</h2>
        <p>
          Administrators can prepare partner profiles privately, but they remain off the public website
          until relationship verification and publication are complete.
        </p>
        <a class="btn btn-primary" href="/contact">Discuss a partnership</a>
      </div>
    {/if}
  </div>
</section>

<section class="principle">
  <div class="container principle-card">
    <div>
      <p class="eyebrow">Partnership integrity</p>
      <h2>We distinguish collaboration from association.</h2>
      <p>
        Media coverage, event attendance or a shared photograph does not automatically make an
        organisation a Foundation partner. The public directory is intentionally stricter.
      </p>
    </div>
    <a class="btn btn-secondary" href="/governance">Governance & transparency</a>
  </div>
</section>

<style>
  .featured{padding:96px 0;background:#0a040a}
  .featured-grid{display:grid;grid-template-columns:1.2fr .8fr;grid-template-rows:260px 260px;gap:16px}
  .featured-grid>a{display:grid;grid-template-columns:200px 1fr;overflow:hidden;border:1px solid rgba(225,189,106,.16);border-radius:28px;background:rgba(255,255,255,.035)}
  .featured-grid>a.lead{grid-row:1/3;grid-template-columns:1fr;grid-template-rows:1.08fr .92fr}
  .visual{display:grid;place-items:center;overflow:hidden;background:radial-gradient(circle at 70% 22%,rgba(225,189,106,.15),transparent 16rem),linear-gradient(145deg,#4b1552,#100611);color:var(--gold-bright);font:600 2.4rem/1 'Cormorant Garamond',Georgia,serif}
  .visual img{width:100%;height:100%;object-fit:cover}.visual img.logo-visual{width:65%;height:65%;object-fit:contain}
  .copy{padding:25px}
  .meta{display:flex;flex-wrap:wrap;gap:8px 12px;color:var(--gold-deep);font-size:.66rem;font-weight:800;text-transform:uppercase;letter-spacing:.06em}
  .meta .verified{border:1px solid rgba(90,130,85,.25);border-radius:999px;padding:4px 7px;color:#9db898}
  .copy h2{margin:13px 0 9px;color:var(--champagne);font:600 1.9rem/1 'Cormorant Garamond',Georgia,serif}
  .lead .copy h2{font-size:clamp(2.7rem,5vw,4.4rem)}
  .copy p{margin:0;color:#aa9aa8;font-size:.84rem}.copy em{display:inline-block;margin-top:16px;color:var(--gold-bright);font-size:.75rem;font-style:normal;font-weight:800}

  .directory{padding:112px 0 120px;background:var(--ivory);color:#2b1827}
  .directory .eyebrow{color:#8e6020}.directory .section-title{color:#351e32}.directory .section-copy{color:#6d5b68}
  .partner-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:48px}
  .partner-grid>a{overflow:hidden;border:1px solid rgba(80,45,70,.12);border-radius:24px;background:#fff;transition:transform .18s ease,box-shadow .18s ease}
  .partner-grid>a:hover{transform:translateY(-3px);box-shadow:0 22px 55px rgba(55,26,49,.09)}
  .logo-wrap{height:170px;display:grid;place-items:center;border-bottom:1px solid rgba(80,45,70,.08);background:#fbf7f1}
  .logo-wrap img{max-width:72%;max-height:92px;object-fit:contain}.logo-wrap span{display:grid;width:70px;height:70px;place-items:center;border:1px solid rgba(166,112,37,.25);border-radius:50%;color:#8e6020;font:600 1.7rem/1 'Cormorant Garamond',Georgia,serif}
  .body{padding:22px}.top,.bottom{display:flex;flex-wrap:wrap;justify-content:space-between;gap:8px 12px;color:#9b6c29;font-size:.65rem;font-weight:800;text-transform:uppercase;letter-spacing:.05em}.top .check{color:#587252}
  .body h3{margin:22px 0 8px;color:#43213f;font:600 2rem/1 'Cormorant Garamond',Georgia,serif}.body p{margin:0;color:#6d5b68;font-size:.86rem}.bottom{margin-top:24px;border-top:1px solid rgba(80,45,70,.08);padding-top:15px;color:#8d7c88;text-transform:none;letter-spacing:0;font-weight:600}
  .empty{max-width:780px;margin:50px auto 0;padding:64px;background:#fff;border-color:rgba(80,45,70,.12);text-align:center}.empty>span{color:#8e6020;font:600 4rem/1 'Cormorant Garamond',Georgia,serif}.empty h2{margin:22px 0 10px;color:#43213f;font:600 2.5rem/1 'Cormorant Garamond',Georgia,serif}.empty p{color:#6d5b68}.empty .btn{margin-top:20px}

  .principle{padding:88px 0;background:#080308}.principle-card{display:flex;align-items:end;justify-content:space-between;gap:44px;border:1px solid var(--line);border-radius:30px;padding:48px;background:linear-gradient(135deg,rgba(100,25,111,.24),rgba(255,255,255,.02))}.principle-card h2{max-width:780px;margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}.principle-card p:not(.eyebrow){max-width:730px;color:#ad9daa}.principle-card .btn{flex-shrink:0}

  @media(max-width:900px){.featured-grid{grid-template-columns:1fr;grid-template-rows:auto}.featured-grid>a,.featured-grid>a.lead{grid-row:auto;grid-template-columns:180px 1fr;grid-template-rows:auto;min-height:230px}.partner-grid{grid-template-columns:1fr 1fr}.principle-card{align-items:flex-start;flex-direction:column}}
  @media(max-width:620px){.featured-grid>a,.featured-grid>a.lead{grid-template-columns:1fr}.visual{min-height:220px}.partner-grid{grid-template-columns:1fr}}
</style>
