<svelte:head>
  <title>Princess Dr. Jessie Ifeoma Udoka-Menuba | Queen Tovah Cares Foundation International</title>
  <meta
    name="description"
    content="Public profile of Princess Dr. Jessie Ifeoma Udoka-Menuba (née Oliobi), widely reported as Founder/CEO of Queen-Tovah Cares Foundation International, humanitarian, philanthropist and community-development advocate."
  />
  <meta
    name="keywords"
    content="Jessie Ifeoma Udoka-Menuba, Jessie Ifeoma Udoka Menuba, Princess Dr Jessie Udoka-Menuba, Jessie Udoka-Menuba, Queen Tovah Cares Foundation International, Queen-Tovah Foundation, Jessie Joseph"
  />
  <meta property="og:title" content="Princess Dr. Jessie Ifeoma Udoka-Menuba | Queen Tovah Cares Foundation International" />
  <meta
    property="og:description"
    content="Humanitarian, philanthropist and Founder/CEO of Queen-Tovah Cares Foundation International as identified in public reporting."
  />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();

  const fallbackAchievements = [
    {
      year: '2024',
      title: 'Mother General Award',
      copy: 'Ugosimba Women Association, Amawbia honoured Princess Dr. Jessie Ifeoma Udoka-Menuba with its “Mother General” award for leadership and service to vulnerable people.',
      source: 'Anambra State Government',
      href: 'https://anambrastate.gov.ng/ugosimba-women-amawbia-honor-princess-dr-jessie-ifeoma-udoka-menuba-with-prestigious-mother-general-award/'
    },
    {
      year: '2025',
      title: 'Ahaejiejemba1 & Woman of the Decade',
      copy: 'Umuigbo United Assembly Worldwide conferred the titles “Ahaejiejemba1” and “Woman of the Decade” in recognition of leadership, service and support for underprivileged people.',
      source: 'Anambra State Government',
      href: 'https://anambrastate.gov.ng/founder-queen-tovah-cares-foundation-intl-receives-more-accolades-as-umuigbo-united-assembly-honors-her-with-prestigious-awards/'
    },
    {
      year: '2025',
      title: 'NUJ Anambra Philanthropist of the 21st Century',
      copy: 'Public reporting by Anambra State Government lists Jessie Ifeoma Udoka as the 2025 NUJ Anambra “Philanthropist of the 21st Century.”',
      source: 'Anambra State Government',
      href: 'https://anambrastate.gov.ng/tag/awards/'
    },
    {
      year: '2025',
      title: 'Youth empowerment through sport',
      copy: 'She sponsored the 2025 Amawbia August League football tournament, supporting youth engagement, community unity and local development.',
      source: 'Independent Newspaper Nigeria',
      href: 'https://independent.ng/princess-udoka-menuba-kicks-poverty-out-with-amawbia-football-showdown/'
    },
    {
      year: '2026',
      title: 'Ada Di Iche 1 Worldwide',
      copy: 'Umuada Nimo married to Amawbia honoured her with the “Ada Di Iche 1 Worldwide” award for humanitarian work within the community and beyond.',
      source: 'Anambra State Government',
      href: 'https://anambrastate.gov.ng/tag/a-shining-light-princess-jessie-udoka-menuba-honoured-with-ada-di-iche-1-worldwide-award/'
    }
  ];

  const achievements = $derived(data.achievements.length
    ? data.achievements.map((achievement) => ({
        year: String(achievement.year ?? ''),
        title: achievement.title,
        copy: achievement.description,
        source: achievement.source_name || 'Source',
        href: achievement.source_url
      }))
    : fallbackAchievements);

  const founder = $derived(data.founder);
  const mediaPreview = $derived(data.media.slice(0, 4));

  function mediaPhoto(item: (typeof data.media)[number]) {
    return item.photos.find((photo) => photo.is_primary && photo.image_url) ??
      item.photos.find((photo) => photo.image_url) ??
      null;
  }

  const education = [
    'BSc in Nursing',
    'BS in Chaplaincy',
    'MS in General Psychology',
    'Doctorate in Theology (ThD)',
    'PhD in Humanities',
    'PhD in Divinity',
    'Honorary Doctorate of Divinity'
  ];
</script>

<PageHero
  eyebrow="Founder public profile"
  title="Princess Dr. Jessie Ifeoma"
  accent="Udoka-Menuba"
  copy="Public reporting by Anambra State Government and national media repeatedly identifies Princess Dr. Jessie Ifeoma Udoka-Menuba (née Oliobi) as Founder/CEO of Queen-Tovah Cares Foundation International."
/>

<section class="identity-note">
  <div class="container note-card">
    <div>
      <p class="eyebrow">Name & discoverability</p>
      <h2>Keeping the public-record name searchable without forcing an unverified name merger.</h2>
    </div>
    <p>
      The Foundation name supplied for this website uses <strong>Princess Dr. Jessie Joseph</strong>.
      Independent public coverage repeatedly uses <strong>Princess Dr. Jessie Ifeoma Udoka-Menuba
      (née Oliobi)</strong> for the Founder/CEO. Until the Foundation formally confirms that both names
      should be treated as the same public identity, this profile keeps the Udoka-Menuba name highly
      visible for search engines while leaving the primary founder naming unchanged elsewhere on the site.
    </p>
  </div>
</section>

<section class="profile">
  <div class="container profile-grid">
    <aside class="portrait-card">
      <div class="portrait-frame">
        {#if founder?.portrait}
          <img src={founder.portrait} alt={founder.portrait_alt || founder.public_record_name || founder.primary_name} />
        {:else}
          <span class="crown">♛</span>
          <strong>{founder?.public_record_name || 'Princess Dr. Jessie Ifeoma Udoka-Menuba'}</strong>
          <small>{founder?.headline || 'Founder / CEO — public record'}</small>
        {/if}
      </div>
      <p>
        Official coverage contains photographs of Dr. Udoka-Menuba. A Foundation-approved portrait will
        replace this panel once the image is cleared for permanent use on the website.
      </p>
      <a
        class="source-link"
        href="https://anambrastate.gov.ng/ugosimba-women-amawbia-honor-princess-dr-jessie-ifeoma-udoka-menuba-with-prestigious-mother-general-award/"
        target="_blank"
        rel="noreferrer"
      >View official coverage with photographs ↗</a>
    </aside>

    <div class="bio">
      <p class="eyebrow">Humanitarian profile</p>
      <h2 class="section-title">A public record centred on service, philanthropy and community development.</h2>
      <p>
        {founder?.biography || 'Princess Dr. Jessie Ifeoma Udoka-Menuba (née Oliobi) is repeatedly described in official public reporting as the Founder and CEO of Queen-Tovah Cares Foundation International. Her work has been associated with support for widows, vulnerable children, indigent people, older people and communities, alongside education, scholarships, youth initiatives and humanitarian assistance.'}
      </p>
      <p>
        Anambra State Government coverage describes the Foundation as having a global outlook and as
        non-political in its humanitarian mission. Independent reporting has also documented her support
        for youth development through the 2025 Amawbia August League football tournament.
      </p>
      <blockquote>“{founder?.motto || 'It is good to be good.'}”</blockquote>
    </div>
  </div>
</section>

<section class="achievements">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">Selected recognition</p>
        <h2 class="section-title">Publicly reported achievements.</h2>
      </div>
      <p class="section-copy">
        These entries are deliberately limited to achievements we could trace to published public sources.
      </p>
    </div>

    <div class="timeline">
      {#each achievements as achievement}
        <article>
          <span class="year">{achievement.year}</span>
          <div>
            <h3>{achievement.title}</h3>
            <p>{achievement.copy}</p>
            <a href={achievement.href} target="_blank" rel="noreferrer">{achievement.source} ↗</a>
          </div>
        </article>
      {/each}
    </div>
  </div>
</section>


<section class="recognition-media">
  <div class="container">
    <div class="section-head">
      <div>
        <p class="eyebrow">Recognition, publications & photographs</p>
        <h2 class="section-title">The founder’s public record as a living media archive.</h2>
      </div>
      <a class="archive-link" href="/founder/media">Open full recognition & media archive ↗</a>
    </div>

    {#if mediaPreview.length}
      <div class="media-grid">
        {#each mediaPreview as item, i}
          {@const photo = mediaPhoto(item)}
          <a class:lead={i === 0} href={`/founder/media/${item.slug}`}>
            <div class="media-visual">
              {#if photo}
                <img src={photo.image_url} alt={photo.alt_text || item.title} loading={i === 0 ? 'eager' : 'lazy'} />
              {:else}
                <span>QT</span>
              {/if}
            </div>
            <div class="media-copy">
              <span>{item.kind.replace('-', ' ')}</span>
              <h3>{item.title}</h3>
              <p>{item.summary}</p>
              <small>{item.source_name} ↗</small>
            </div>
          </a>
        {/each}
      </div>
    {:else}
      <div class="media-empty">
        Verified founder publications will appear here automatically when published through the Foundation archive.
      </div>
    {/if}
  </div>
</section>

<section class="education">
  <div class="container education-grid">
    <div>
      <p class="eyebrow">Academic profile</p>
      <h2 class="section-title">A broad academic and ministerial background.</h2>
      <p class="section-copy">
        A 2025 NUJ Anambra publication and related public profiles list the following qualifications.
        They are presented here as published claims pending receipt of the Foundation’s own credential file.
      </p>
    </div>
    <div class="qualifications">
      {#each education as item}
        <span>{item}</span>
      {/each}
    </div>
  </div>
  <div class="container source-row">
    <a
      href="https://www.odogwublog.com/wp-content/uploads/2025/10/The-WatchDog-Magazine-Of-The-NUJ-Anambra-2025-1.pdf"
      target="_blank"
      rel="noreferrer"
    >View NUJ Anambra profile source ↗</a>
  </div>
</section>

<section class="press">
  <div class="container press-card">
    <div>
      <p class="eyebrow">Press & verification</p>
      <h2>Build the website around records we can defend.</h2>
      <p>
        As more official certificates, photographs, award records and Foundation documents are supplied,
        this profile can expand into a complete verified biography and media archive.
      </p>
    </div>
    <a class="btn btn-primary" href="/contact">Contact the Foundation</a>
  </div>
</section>

<style>
  .identity-note { padding: 72px 0; background: #110711; }
  .note-card {
    display:grid; grid-template-columns:.9fr 1.1fr; gap:60px; align-items:start;
    border:1px solid var(--line); border-radius:28px; padding:42px;
    background:linear-gradient(135deg,rgba(100,25,111,.22),rgba(255,255,255,.02));
  }
  .note-card h2 { margin:0; color:var(--champagne); font:600 clamp(2rem,4vw,3.4rem)/1 'Cormorant Garamond',Georgia,serif; }
  .note-card>p { margin:4px 0 0; color:#b9a9b7; }
  .note-card strong { color:var(--champagne); }

  .profile { padding:112px 0; background:var(--ivory); color:#2b1827; }
  .profile-grid { display:grid; grid-template-columns:.8fr 1.2fr; gap:84px; align-items:center; }
  .portrait-card { border-radius:30px; padding:28px; background:linear-gradient(145deg,#4b1551,#100611); box-shadow:0 30px 80px rgba(53,28,46,.18); }
  .portrait-frame { min-height:500px; display:flex; align-items:center; justify-content:center; flex-direction:column; gap:8px; position:relative; border:1px solid rgba(225,189,106,.35); border-radius:46% 46% 22px 22px; padding:30px; text-align:center; }
  .portrait-frame .crown { position:absolute; top:42px; color:var(--gold-bright); font-size:3.5rem; }
  .portrait-frame img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; border-radius:inherit; }
  .portrait-frame strong { max-width:270px; margin-top:48px; color:var(--champagne); font:600 2rem/1.05 'Cormorant Garamond',Georgia,serif; }
  .portrait-frame small { color:#aa96a8; }
  .portrait-card>p { color:#c5b5c3; font-size:.82rem; }
  .source-link { color:var(--gold-bright); font-size:.82rem; text-decoration:underline; text-underline-offset:3px; }
  .bio .eyebrow { color:#8e6020; }
  .bio .section-title { color:#321c2f; }
  .bio>p:not(.eyebrow) { color:#685764; }
  blockquote { margin:34px 0 0; color:#592b57; font:italic 600 clamp(2rem,4vw,3.2rem)/1 'Cormorant Garamond',Georgia,serif; }

  .achievements { padding:112px 0; background:#090409; }
  .section-head { display:flex; align-items:end; justify-content:space-between; gap:40px; }
  .section-head .section-copy { max-width:470px; margin:0 0 4px; }
  .timeline { margin-top:54px; border-top:1px solid var(--line); }
  .timeline article { display:grid; grid-template-columns:86px 1fr; gap:28px; border-bottom:1px solid var(--line); padding:30px 0; }
  .year { padding-top:7px; color:var(--gold-deep); font-size:.75rem; font-weight:700; }
  .timeline h3 { margin:0; color:var(--champagne); font:600 1.9rem/1 'Cormorant Garamond',Georgia,serif; }
  .timeline p { max-width:780px; margin:10px 0 0; color:#a897a7; }
  .timeline a { display:inline-block; margin-top:12px; color:var(--gold-bright); font-size:.78rem; text-decoration:underline; text-underline-offset:3px; }

  .recognition-media{padding:112px 0;background:var(--ivory);color:#2a1926}
  .recognition-media .eyebrow{color:#8e6020}
  .recognition-media .section-title{color:#341d31}
  .archive-link{color:#8e6020;font-size:.82rem;font-weight:700}
  .media-grid{display:grid;grid-template-columns:1.2fr .8fr;grid-template-rows:240px 240px 240px;gap:14px;margin-top:48px}
  .media-grid>a{display:grid;grid-template-columns:180px 1fr;overflow:hidden;border:1px solid rgba(80,45,70,.12);border-radius:24px;background:#fff}
  .media-grid>a.lead{grid-row:1/4;grid-template-columns:1fr;grid-template-rows:1.1fr .9fr}
  .media-visual{min-height:0;display:grid;place-items:center;background:radial-gradient(circle at 70% 22%,rgba(225,189,106,.18),transparent 13rem),linear-gradient(145deg,#4b1552,#100611);color:var(--gold-bright);font:600 2.7rem/1 'Cormorant Garamond',Georgia,serif}
  .media-visual img{width:100%;height:100%;object-fit:cover}
  .media-copy{padding:22px}
  .media-copy>span{color:#9b6c29;font-size:.66rem;font-weight:800;text-transform:uppercase;letter-spacing:.07em}
  .media-copy h3{margin:10px 0 7px;color:#43213f;font:600 1.55rem/1 'Cormorant Garamond',Georgia,serif}
  .lead .media-copy h3{font-size:2.4rem}
  .media-copy p{margin:0;color:#6d5b68;font-size:.82rem}
  .media-copy small{display:block;margin-top:14px;color:#8e6020}
  .media-empty{margin-top:42px;border:1px dashed rgba(80,45,70,.16);border-radius:20px;padding:30px;color:#6d5b68}
  .education { padding:112px 0; background:var(--cream); color:#2a1926; }
  .education-grid { display:grid; grid-template-columns:.95fr 1.05fr; gap:80px; }
  .education .eyebrow { color:#8e6020; }
  .education .section-title { color:#341d31; }
  .education .section-copy { color:#6d5b68; }
  .qualifications { display:grid; grid-template-columns:1fr 1fr; gap:12px; }
  .qualifications span { border:1px solid rgba(80,45,70,.13); border-radius:18px; padding:18px; background:rgba(255,255,255,.45); color:#5e4b59; font-size:.9rem; }
  .source-row { margin-top:30px; }
  .source-row a { color:#8e6020; font-size:.82rem; text-decoration:underline; text-underline-offset:3px; }

  .press { padding:88px 0; background:#080308; }
  .press-card { display:flex; align-items:end; justify-content:space-between; gap:40px; border:1px solid var(--line); border-radius:30px; padding:50px; background:radial-gradient(circle at 84% 22%,rgba(201,151,63,.13),transparent 22rem),linear-gradient(135deg,rgba(100,25,111,.24),rgba(255,255,255,.02)); }
  .press-card h2 { max-width:800px; margin:0; color:var(--ivory); font:600 clamp(2.4rem,5vw,4.2rem)/.98 'Cormorant Garamond',Georgia,serif; }
  .press-card p:not(.eyebrow) { max-width:740px; color:#ac9baa; }

  @media(max-width:900px){
    .note-card,.profile-grid,.education-grid{grid-template-columns:1fr;gap:44px}
    .media-grid{grid-template-columns:1fr;grid-template-rows:auto}
    .media-grid>a,.media-grid>a.lead{grid-row:auto;grid-template-columns:180px 1fr;grid-template-rows:auto;min-height:220px}
    .section-head,.press-card{align-items:flex-start;flex-direction:column}
  }
  @media(max-width:600px){
    .identity-note,.profile,.achievements,.education{padding:82px 0}
    .note-card,.press-card{padding:30px 24px}
    .portrait-frame{min-height:420px}
    .timeline article{grid-template-columns:52px 1fr}
    .qualifications{grid-template-columns:1fr}
    .media-grid>a,.media-grid>a.lead{grid-template-columns:1fr}
    .media-visual{min-height:220px}
  }
</style>
