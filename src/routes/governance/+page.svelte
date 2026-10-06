<svelte:head>
  <title>Governance & Transparency | Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Queen Tovah Cares Foundation International governance, transparency, dignity, accountability and official resources centre."
  />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();

  const governanceResources = data.resources.filter((item) =>
    ['annual-report', 'impact-report', 'policy'].includes(item.category)
  );

  const commitments = [
    ['Dignity before publicity', 'Beneficiaries should never be reduced to promotional material. Public stories and media should respect privacy, consent and human dignity.'],
    ['Verified public claims', 'Impact figures, funding progress, awards and program information should be published only when the Foundation can support the claim.'],
    ['Controlled publishing', 'Website content follows a draft, review and published workflow so unfinished or unapproved information does not automatically become public.'],
    ['Clear giving channels', 'Donation or payment links appear publicly only after an approved Foundation channel has been configured.'],
    ['Private support intake', 'Requests for humanitarian assistance are routed to a private administrative inbox rather than displayed as public beneficiary profiles.'],
    ['Accessible public record', 'Reports, policies and official resources can be published in a dedicated library so partners and communities can find the authoritative version.']
  ];
</script>

<PageHero
  eyebrow="Governance & transparency"
  title="Trust should be"
  accent="designed into the work."
  copy="Our digital platform is structured around controlled publishing, verified public claims, beneficiary dignity and a clear distinction between official Foundation records and third-party coverage."
/>

<section class="commitments">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">Digital governance</p>
        <h2 class="section-title">Principles behind the platform.</h2>
      </div>
      <p class="section-copy">
        These standards describe how the website is designed to handle public information. Formal
        Foundation policies will be published in the resources library once approved.
      </p>
    </div>

    <div class="commitment-grid">
      {#each commitments as item, i}
        <article>
          <span>0{i + 1}</span>
          <h3>{item[0]}</h3>
          <p>{item[1]}</p>
        </article>
      {/each}
    </div>
  </div>
</section>

<section class="workflow">
  <div class="container workflow-grid">
    <div>
      <p class="eyebrow">Publishing control</p>
      <h2 class="section-title">Draft. Review. Publish.</h2>
      <p class="section-copy">
        Public content is separated from work in progress. Administrators can prepare material, move it
        into review and publish only when it is ready.
      </p>
    </div>
    <div class="flow">
      <div><span>01</span><strong>Draft</strong><p>Prepare content privately.</p></div>
      <i>→</i>
      <div><span>02</span><strong>Review</strong><p>Check accuracy and presentation.</p></div>
      <i>→</i>
      <div><span>03</span><strong>Published</strong><p>Expose approved material publicly.</p></div>
    </div>
  </div>
</section>

<section class="resources">
  <div class="container">
    <div class="resource-head">
      <div>
        <p class="eyebrow">Official record</p>
        <h2 class="section-title">Reports & policies.</h2>
      </div>
      <a href="/resources">Open full resource library ↗</a>
    </div>

    {#if governanceResources.length}
      <div class="resource-grid">
        {#each governanceResources.slice(0, 6) as item}
          <a href={`/resources/${item.slug}`}>
            <span>{item.year || 'Official'}</span>
            <h3>{item.title}</h3>
            <p>{item.summary}</p>
            <em>View resource ↗</em>
          </a>
        {/each}
      </div>
    {:else}
      <div class="empty">
        <p>No formal governance document has been published through the website yet.</p>
        <span>This section will populate automatically when approved policies or reports are released.</span>
      </div>
    {/if}
  </div>
</section>

<section class="trust-cta">
  <div class="container cta-card">
    <div>
      <p class="eyebrow">Questions about the Foundation?</p>
      <h2>Ask through an official channel.</h2>
    </div>
    <div class="actions">
      <a class="btn btn-primary" href="/contact">Contact the Foundation</a>
      <a class="btn btn-secondary" href="/faq">Read FAQs</a>
    </div>
  </div>
</section>

<style>
  .commitments{padding:112px 0;background:var(--ivory);color:#2b1827}
  .commitments .eyebrow,.resources .eyebrow{color:#8e6020}
  .commitments .section-title,.resources .section-title{color:#351e32}
  .commitments .section-copy{color:#6d5b68}
  .commitment-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:16px;margin-top:54px}
  .commitment-grid article{min-height:300px;border:1px solid rgba(80,45,70,.12);border-radius:24px;padding:26px;background:#fff}
  .commitment-grid span{color:#9b6c29;font-size:.7rem;font-weight:800}
  .commitment-grid h3{margin:72px 0 10px;color:#43213f;font:600 1.8rem/1 'Cormorant Garamond',Georgia,serif}
  .commitment-grid p{margin:0;color:#6d5b68;font-size:.88rem}

  .workflow{padding:110px 0;background:#100711}
  .workflow-grid{display:grid;grid-template-columns:.85fr 1.15fr;gap:80px;align-items:center}
  .flow{display:grid;grid-template-columns:1fr auto 1fr auto 1fr;align-items:center;gap:12px}
  .flow>div{min-height:190px;border:1px solid rgba(225,189,106,.16);border-radius:22px;padding:22px;background:rgba(255,255,255,.035)}
  .flow>div span{color:var(--gold-deep);font-size:.7rem;font-weight:800}
  .flow>div strong{display:block;margin-top:52px;color:var(--champagne);font:600 1.6rem/1 'Cormorant Garamond',Georgia,serif}
  .flow>div p{margin:6px 0 0;color:#a998a8;font-size:.8rem}
  .flow>i{color:var(--gold-deep);font-style:normal}

  .resources{padding:112px 0;background:var(--cream);color:#2b1827}
  .resource-head{display:flex;align-items:end;justify-content:space-between;gap:40px}
  .resource-head>a{color:#8e6020;font-size:.8rem;font-weight:700}
  .resource-grid{display:grid;grid-template-columns:repeat(3,1fr);gap:15px;margin-top:46px}
  .resource-grid a{min-height:270px;display:flex;flex-direction:column;border:1px solid rgba(80,45,70,.12);border-radius:22px;padding:24px;background:#fff}
  .resource-grid span{color:#9b6c29;font-size:.7rem;font-weight:800;text-transform:uppercase}
  .resource-grid h3{margin:54px 0 10px;color:#43213f;font:600 1.7rem/1 'Cormorant Garamond',Georgia,serif}
  .resource-grid p{margin:0;color:#6d5b68;font-size:.85rem}
  .resource-grid em{margin-top:auto;padding-top:20px;color:#8e6020;font-size:.75rem;font-style:normal;font-weight:700}
  .empty{margin-top:42px;border:1px dashed rgba(80,45,70,.18);border-radius:22px;padding:32px;color:#6d5b68}
  .empty p{margin:0;color:#4c3548;font-weight:700}.empty span{display:block;margin-top:5px;font-size:.84rem}

  .trust-cta{padding:86px 0;background:#080308}
  .cta-card{display:flex;align-items:end;justify-content:space-between;gap:40px;border:1px solid var(--line);border-radius:30px;padding:48px;background:linear-gradient(135deg,rgba(100,25,111,.25),rgba(255,255,255,.02))}
  .cta-card h2{margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .actions{display:flex;flex-wrap:wrap;gap:10px;flex-shrink:0}

  @media(max-width:900px){.commitment-grid,.resource-grid{grid-template-columns:1fr 1fr}.workflow-grid{grid-template-columns:1fr}.flow{grid-template-columns:1fr}.flow>i{transform:rotate(90deg);text-align:center}.cta-card,.resource-head{align-items:flex-start;flex-direction:column}}
  @media(max-width:600px){.commitment-grid,.resource-grid{grid-template-columns:1fr}.commitment-grid article{min-height:240px}.commitment-grid h3{margin-top:48px}.cta-card{padding:32px 24px}}
</style>
