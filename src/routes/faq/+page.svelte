<svelte:head>
  <title>Frequently Asked Questions | Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Answers to common questions about Queen Tovah Cares Foundation International, giving, humanitarian support, scholarships, volunteering and partnerships."
  />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();
  let category = 'all';

  const categories = [
    ['all', 'All questions'],
    ['general', 'General'],
    ['support', 'Requesting support'],
    ['giving', 'Giving & causes'],
    ['scholarship', 'Scholarships'],
    ['volunteer', 'Volunteering'],
    ['partnership', 'Partnerships']
  ] as const;
</script>

<PageHero
  eyebrow="Help centre"
  title="Clear answers build"
  accent="better trust."
  copy="Browse published answers about the Foundation, its programs, support process, giving, scholarships, volunteering and partnerships."
/>

<section class="faq">
  <div class="container">
    <div class="category-bar" aria-label="FAQ categories">
      {#each categories as item}
        <button
          type="button"
          class:active={category === item[0]}
          onclick={() => (category = item[0])}
        >
          {item[1]}
        </button>
      {/each}
    </div>

    {#if data.faqs.length}
      <div class="faq-grid">
        <aside>
          <p class="eyebrow">Need something else?</p>
          <h2>Find the right path.</h2>
          <p>For a personal enquiry, use Contact. For humanitarian assistance, use the private Request Support flow.</p>
          <div class="aside-actions">
            <a href="/contact">Contact the Foundation ↗</a>
            <a href="/request-support">Request support privately ↗</a>
          </div>
        </aside>

        <div class="questions">
          {#each data.faqs.filter((item) => category === 'all' || item.category === category) as item}
            <details id={item.slug}>
              <summary>
                <span>{item.question}</span>
                <i aria-hidden="true">+</i>
              </summary>
              <div class="answer">
                {#each item.answer.split('\n\n').filter(Boolean) as paragraph}
                  <p>{paragraph}</p>
                {/each}
              </div>
            </details>
          {/each}
        </div>
      </div>
    {:else}
      <div class="empty card">
        <span>QT</span>
        <h2>Published answers will appear here.</h2>
        <p>The Foundation can manage frequently asked questions in the admin without editing website code.</p>
        <a class="btn btn-primary" href="/contact">Ask the Foundation</a>
      </div>
    {/if}
  </div>
</section>

<section class="trust">
  <div class="container trust-shell">
    <div>
      <p class="eyebrow">Still unsure?</p>
      <h2>Do not rely on unofficial payment links, scholarship forms or social-media claims.</h2>
    </div>
    <p>Use the Foundation website as the reference point for published causes, opportunities, application links and official contact channels.</p>
  </div>
</section>

<style>
  .faq{padding:92px 0 120px;background:var(--ivory);color:#2b1827}
  .category-bar{display:flex;flex-wrap:wrap;gap:8px;margin-bottom:54px}
  .category-bar button{border:1px solid rgba(80,45,70,.13);border-radius:999px;padding:9px 14px;background:#fff;color:#705f6c;cursor:pointer;font-size:.78rem;font-weight:700}
  .category-bar button.active{border-color:#9c6c28;background:#44213f;color:var(--champagne)}
  .faq-grid{display:grid;grid-template-columns:300px 1fr;gap:70px;align-items:start}
  aside{position:sticky;top:132px}
  aside .eyebrow{color:#8e6020}
  aside h2{margin:0;color:#43213f;font:600 2.8rem/1 'Cormorant Garamond',Georgia,serif}
  aside>p:not(.eyebrow){color:#6d5b68}
  .aside-actions{display:grid;gap:8px;margin-top:24px}
  .aside-actions a{color:#8e6020;font-size:.8rem;font-weight:700}
  .questions{border-top:1px solid rgba(80,45,70,.13)}
  details{border-bottom:1px solid rgba(80,45,70,.13)}
  summary{display:flex;align-items:center;justify-content:space-between;gap:28px;padding:25px 0;cursor:pointer;list-style:none;color:#41223d;font:600 1.55rem/1.08 'Cormorant Garamond',Georgia,serif}
  summary::-webkit-details-marker{display:none}
  summary i{display:grid;width:34px;height:34px;flex-shrink:0;place-items:center;border:1px solid rgba(166,112,37,.22);border-radius:50%;color:#9b6c29;font:normal 400 1.2rem/1 Manrope,sans-serif;transition:transform .18s ease}
  details[open] summary i{transform:rotate(45deg)}
  .answer{padding:0 56px 24px 0;color:#665561;line-height:1.75}
  .answer p{margin:0 0 14px}
  .empty{max-width:760px;margin:auto;padding:64px;text-align:center;background:#fff;border-color:rgba(80,45,70,.12)}
  .empty>span{display:grid;width:60px;height:60px;place-items:center;margin:auto;border:1px solid rgba(166,112,37,.28);border-radius:50%;color:#8e6020;font:600 1.3rem/1 'Cormorant Garamond',Georgia,serif}
  .empty h2{margin:24px 0 10px;color:#43213f;font:600 2.3rem/1 'Cormorant Garamond',Georgia,serif}
  .empty p{color:#6d5b68}.empty .btn{margin-top:18px}
  .trust{padding:88px 0;background:#0a040a}
  .trust-shell{display:grid;grid-template-columns:1fr .85fr;gap:70px;align-items:end}
  .trust-shell h2{margin:0;color:var(--ivory);font:600 clamp(2.3rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .trust-shell>p{color:#ad9daa}
  @media(max-width:820px){.faq-grid,.trust-shell{grid-template-columns:1fr;gap:42px}aside{position:static}}
</style>
