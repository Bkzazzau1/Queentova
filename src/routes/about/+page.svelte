<svelte:head>
  <title>About | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Learn about Queen Tovah Cares Foundation International and its founder. Public coverage identifies Princess Dr. Jessie Ifeoma Udoka-Menuba (née Oliobi) as Founder/CEO." />
  <meta name="keywords" content="Jessie Ifeoma Udoka-Menuba, Jessie Udoka-Menuba, Jessie Joseph, Queen Tovah Cares Foundation International, Queen-Tovah Foundation" />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
</script>

<PageHero
  eyebrow="About the Foundation"
  title="Compassion with"
  accent="purpose."
  copy="Queen Tovah Cares Foundation International is a philanthropic foundation serving vulnerable people and communities through humanitarian care, education, youth empowerment and community development."
/>

<section class="story">
  <div class="container story-grid">
    <div>
      <p class="eyebrow">Our identity</p>
      <h2 class="section-title">Humanity first. Dignity always.</h2>
    </div>
    <div class="prose">
      <p>
        The Foundation was established with a global outlook toward the plight of the downtrodden and
        less privileged. Its humanitarian focus includes widows and widowers, indigent people, families
        facing hardship and people without stable shelter.
      </p>
      <p>
        Its work goes beyond immediate relief. Education, scholarships, youth engagement, sports and
        human-capital development are part of a wider commitment to help individuals and communities
        build stronger futures.
      </p>
      <p>
        The Foundation is non-political in its humanitarian mission. Service is guided by need,
        compassion and the conviction that goodness should not be limited by geography.
      </p>
    </div>
  </div>
</section>

<section class="values">
  <div class="container">
    <p class="eyebrow">What guides us</p>
    <div class="value-grid">
      <article><span>01</span><h3>Compassion</h3><p>We respond to real human need with care, empathy and practical support.</p></article>
      <article><span>02</span><h3>Dignity</h3><p>Every person deserves to be treated with respect, not reduced to a circumstance.</p></article>
      <article><span>03</span><h3>Opportunity</h3><p>Education and empowerment help support become a pathway toward lasting progress.</p></article>
      <article><span>04</span><h3>Global outlook</h3><p>Our concern extends beyond one town, state or country wherever meaningful help can reach.</p></article>
    </div>
  </div>
</section>

<section class="founder" id="founder">
  <div class="container founder-grid">
    <div class="portrait">
      <div class="portrait-inner">
        <span class="crown">♛</span>
        <p>Founder portrait</p>
      </div>
    </div>
    <div>
      <p class="eyebrow">Founder</p>
      <h2 class="section-title">Princess Dr. Jessie Joseph</h2>
      <p class="reported-name">Official public reporting repeatedly identifies the Founder/CEO as <a href="/founder/jessie-ifeoma-udoka-menuba">Princess Dr. Jessie Ifeoma Udoka-Menuba (née Oliobi)</a>.</p>
      <p class="founder-copy">
        Princess Dr. Jessie Joseph founded Queen Tovah Cares Foundation International around a
        conviction that philanthropy should reach people wherever need exists. Her vision combines
        direct humanitarian support with investment in education, youth, families and community life.
      </p>
      <blockquote>“It is good to be good.”</blockquote>
      <p class="faith">God is my strength.</p>
    </div>
  </div>
</section>

<style>
  .story, .values, .founder { padding: 112px 0; }
  .story { background: var(--ivory); color: #2a1926; }
  .story .eyebrow, .founder .eyebrow { color: #8e6020; }
  .story-grid { display:grid; grid-template-columns:1fr .92fr; gap:86px; }
  .story .section-title, .founder .section-title { color:#2b1827; }
  .prose { color:#655561; font-size:1.03rem; }
  .prose p { margin:0 0 22px; }
  .values { background:#0b050b; }
  .value-grid { display:grid; grid-template-columns:repeat(4,1fr); gap:16px; margin-top:42px; }
  .value-grid article { min-height:250px; border:1px solid var(--line); border-radius:24px; padding:26px; background:rgba(255,255,255,.025); }
  .value-grid span { color:var(--gold-deep); font-size:.72rem; font-weight:700; }
  .value-grid h3 { margin:62px 0 10px; color:var(--champagne); font:600 1.7rem/1 'Cormorant Garamond',Georgia,serif; }
  .value-grid p { margin:0; color:#a897a7; font-size:.9rem; }
  .founder { background:#f7efe2; color:#33232f; }
  .founder-grid { display:grid; grid-template-columns:.8fr 1.2fr; align-items:center; gap:80px; }
  .portrait { min-height:520px; border-radius:30px; padding:28px; background:linear-gradient(145deg,#4b1551,#100611); box-shadow:0 26px 70px rgba(60,30,50,.2); }
  .portrait-inner { height:100%; min-height:464px; display:grid; place-items:center; position:relative; border:1px solid rgba(225,189,106,.35); border-radius:45% 45% 18px 18px; color:#bdaebc; text-align:center; }
  .portrait-inner p { max-width:220px; }
  .crown { position:absolute; top:42px; color:var(--gold-bright); font-size:3.5rem; }
  .reported-name { margin:18px 0 0; color:#8e6020; font-size:.9rem; }
  .reported-name a { text-decoration:underline; text-underline-offset:3px; }
  .founder-copy { max-width:700px; margin:26px 0 0; color:#695966; }
  blockquote { margin:34px 0 0; color:#592b57; font:italic 600 clamp(2rem,4vw,3.2rem)/1 'Cormorant Garamond',Georgia,serif; }
  .faith { color:#8e6020; font-size:.78rem; font-weight:700; letter-spacing:.12em; text-transform:uppercase; }
  @media(max-width:900px){.story-grid,.founder-grid{grid-template-columns:1fr;gap:44px}.value-grid{grid-template-columns:1fr 1fr}}
  @media(max-width:600px){.story,.values,.founder{padding:82px 0}.value-grid{grid-template-columns:1fr}.portrait{min-height:430px}.portrait-inner{min-height:374px}}
</style>
