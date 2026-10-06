<svelte:head>
  <title>Programs | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Explore Queen Tovah Cares Foundation International programs in humanitarian support, education, youth empowerment and community development." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';

  let { data } = $props();

  const fallbackPrograms = [
    {
      number:'01',
      title:'Humanitarian Support',
      copy:'Direct assistance for vulnerable people and families, including widows, widowers, indigent people and people experiencing homelessness.',
      slug:'humanitarian-support',
      points:['Family support','Relief and welfare interventions','Support guided by genuine need']
    },
    {
      number:'02',
      title:'Education & Scholarships',
      copy:'Scholarship support designed to keep financial hardship from becoming a permanent barrier to education and personal development.',
      slug:'education-scholarships',
      points:['Scholarship awards','Support for indigent learners','Education-focused opportunity']
    },
    {
      number:'03',
      title:'Youth Empowerment & Sports',
      copy:'Youth-focused initiatives that use sports and constructive engagement to promote unity, participation and healthy community life.',
      slug:'youth-sports',
      points:['Community sports support','Youth engagement','Unity through participation']
    },
    {
      number:'04',
      title:'Human Capital & Community Development',
      copy:'Programs that strengthen people and communities through practical support, capacity building and locally relevant interventions.',
      slug:'community-development',
      points:['Community-led initiatives','Human-capital development','Longer-term empowerment']
    }
  ];

  const programs = data.programs.length
    ? data.programs.map((program, index) => ({
        number: String(index + 1).padStart(2, '0'),
        title: program.title,
        copy: program.summary,
        slug: program.slug,
        points: program.body
          ? program.body.split('\n').map((item) => item.trim()).filter(Boolean)
          : []
      }))
    : fallbackPrograms;
</script>

<PageHero
  eyebrow="Our programs"
  title="From compassion"
  accent="to action."
  copy="Our work combines immediate humanitarian care with education, empowerment and community development so support can create both relief and possibility."
/>

<section class="program-list">
  <div class="container">
    {#each programs as program}
      <article class="program">
        <div class="number">{program.number}</div>
        <div>
          <h2><a href={program.slug ? `/programs/${program.slug}` : '/programs'}>{program.title}</a></h2>
          <p>{program.copy}</p>
        </div>
        {#if program.points.length}
          <ul>
            {#each program.points as point}<li>{point}</li>{/each}
          </ul>
        {:else}
          <div class="managed-note">Managed through the Foundation content system.</div>
        {/if}
      </article>
    {/each}
  </div>
</section>

<section class="principle">
  <div class="container principle-card">
    <p class="eyebrow">One principle</p>
    <h2>Support should meet people where they are — and help them move forward.</h2>
    <a class="btn btn-primary" href="/contact">Discuss a partnership ↗</a>
  </div>
</section>

<style>
  .program-list{padding:100px 0;background:var(--ivory);color:#2a1926}
  .program{display:grid;grid-template-columns:70px minmax(0,1.15fr) minmax(260px,.75fr);gap:34px;border-bottom:1px solid rgba(80,45,70,.14);padding:42px 0}
  .program:first-child{border-top:1px solid rgba(80,45,70,.14)}
  .number{padding-top:7px;color:#a8762c;font-size:.76rem;font-weight:700}
  h2{margin:0;color:#3d2039;font:600 clamp(2rem,4vw,3.25rem)/1 'Cormorant Garamond',Georgia,serif}
  h2 a:hover{color:#8e6020}
  .program p{max-width:650px;margin:14px 0 0;color:#675864}
  ul{margin:8px 0 0;padding:0;list-style:none}
  li{position:relative;border-bottom:1px solid rgba(80,45,70,.08);padding:9px 0 9px 20px;color:#755f70;font-size:.9rem}
  li::before{position:absolute;left:0;color:#a8762c;content:'✦'}
  .managed-note{align-self:start;margin-top:8px;color:#9a887f;font-size:.8rem}
  .principle{padding:90px 0;background:#0a040a}
  .principle-card{border:1px solid rgba(225,189,106,.22);border-radius:32px;padding:54px;background:radial-gradient(circle at 85% 20%,rgba(201,151,63,.14),transparent 24rem),linear-gradient(135deg,rgba(100,25,111,.25),rgba(255,255,255,.02))}
  .principle-card h2{max-width:850px;color:var(--ivory);font-size:clamp(2.5rem,5vw,4.6rem)}
  .principle-card .btn{margin-top:30px}
  @media(max-width:800px){.program{grid-template-columns:44px 1fr}.program ul,.managed-note{grid-column:2}.principle-card{padding:34px 24px}}
</style>
