<svelte:head>
  <title>Get Involved | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Volunteer, partner and stay connected with Queen Tovah Cares Foundation International." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  import { submitVolunteer, subscribeNewsletter, type VolunteerPayload } from '$lib/api/content';

  let volunteer: VolunteerPayload = {
    name: '',
    email: '',
    phone: '',
    country: '',
    city: '',
    areas_of_interest: '',
    skills: '',
    availability: '',
    message: ''
  };

  let volunteerBusy = false;
  let volunteerMessage = '';
  let volunteerSuccess = false;

  let newsletterName = '';
  let newsletterEmail = '';
  let newsletterBusy = false;
  let newsletterMessage = '';

  async function sendVolunteer(event: SubmitEvent) {
    event.preventDefault();
    volunteerBusy = true;
    volunteerMessage = '';
    volunteerSuccess = false;
    try {
      await submitVolunteer(volunteer);
      volunteerSuccess = true;
      volunteerMessage = 'Thank you. Your volunteer interest has been received for review.';
      volunteer = {
        name: '', email: '', phone: '', country: '', city: '',
        areas_of_interest: '', skills: '', availability: '', message: ''
      };
    } catch {
      volunteerMessage = 'We could not submit your application. Please try again.';
    } finally {
      volunteerBusy = false;
    }
  }

  async function joinNewsletter(event: SubmitEvent) {
    event.preventDefault();
    newsletterBusy = true;
    newsletterMessage = '';
    try {
      await subscribeNewsletter(newsletterEmail, newsletterName);
      newsletterMessage = 'You are subscribed. Thank you for staying close to the mission.';
      newsletterEmail = '';
      newsletterName = '';
    } catch {
      newsletterMessage = 'Subscription could not be completed. Please try again.';
    } finally {
      newsletterBusy = false;
    }
  }

  const pathways = [
    ['Volunteer', 'Offer your time, professional skills or community knowledge where they can create meaningful value.'],
    ['Partner', 'Organizations can collaborate on education, humanitarian support, youth and community programs.'],
    ['Sponsor', 'Support a verified campaign, scholarship, event or outreach initiative through approved Foundation channels.'],
    ['Amplify', 'Help responsible, verified Foundation stories reach people who can contribute, collaborate or benefit.']
  ];
</script>

<PageHero
  eyebrow="Get involved"
  title="There is more than one"
  accent="way to do good."
  copy="Volunteer your skills, build a partnership, support a verified cause or simply stay connected to work that matters."
/>

<section class="pathways">
  <div class="container">
    <div class="path-grid">
      {#each pathways as item, i}
        <article>
          <span>0{i + 1}</span>
          <h2>{item[0]}</h2>
          <p>{item[1]}</p>
        </article>
      {/each}
    </div>
  </div>
</section>

<section class="volunteer">
  <div class="container volunteer-grid">
    <div class="intro">
      <p class="eyebrow">Volunteer with us</p>
      <h2 class="section-title">Bring something useful to the mission.</h2>
      <p>
        Tell us where you can contribute. Applications are reviewed inside the Foundation administration
        system and are never published on the public website.
      </p>
      <div class="privacy">
        <span>Private submission</span>
        <span>Human review</span>
        <span>No automatic public profile</span>
      </div>
    </div>

    <form class="card" onsubmit={sendVolunteer}>
      <div class="two">
        <label>Name<input required maxlength="180" bind:value={volunteer.name} placeholder="Full name" /></label>
        <label>Email<input required type="email" bind:value={volunteer.email} placeholder="you@example.com" /></label>
      </div>
      <div class="two">
        <label>Phone<input bind:value={volunteer.phone} placeholder="+..." /></label>
        <label>Country<input bind:value={volunteer.country} placeholder="Country" /></label>
      </div>
      <div class="two">
        <label>City<input bind:value={volunteer.city} placeholder="City" /></label>
        <label>Availability<input bind:value={volunteer.availability} placeholder="Weekends, remote, etc." /></label>
      </div>
      <label>Area of interest
        <select required bind:value={volunteer.areas_of_interest}>
          <option value="" disabled>Select an area</option>
          <option>Humanitarian outreach</option>
          <option>Education & scholarships</option>
          <option>Youth & sports</option>
          <option>Community development</option>
          <option>Health & wellbeing</option>
          <option>Media & communications</option>
          <option>Professional / technical support</option>
        </select>
      </label>
      <label>Skills<textarea rows="3" bind:value={volunteer.skills} placeholder="Tell us what you can contribute"></textarea></label>
      <label>Message<textarea rows="4" bind:value={volunteer.message} placeholder="Anything else the Foundation should know?"></textarea></label>
      <button class="btn btn-primary" type="submit" disabled={volunteerBusy}>
        {volunteerBusy ? 'Submitting…' : 'Submit volunteer interest'}
      </button>
      {#if volunteerMessage}<p class:success={volunteerSuccess} class="feedback" role="status">{volunteerMessage}</p>{/if}
    </form>
  </div>
</section>

<section class="newsletter">
  <div class="container newsletter-card">
    <div>
      <p class="eyebrow">Stay close to the mission</p>
      <h2>Receive meaningful Foundation updates, not noise.</h2>
      <p>News, verified impact stories, events and opportunities to take part.</p>
    </div>
    <form onsubmit={joinNewsletter}>
      <input aria-label="Your name" bind:value={newsletterName} placeholder="Your name" />
      <input aria-label="Your email" required type="email" bind:value={newsletterEmail} placeholder="Email address" />
      <button class="btn btn-primary" type="submit" disabled={newsletterBusy}>{newsletterBusy ? 'Joining…' : 'Join updates'}</button>
      {#if newsletterMessage}<small>{newsletterMessage}</small>{/if}
    </form>
  </div>
</section>

<style>
  .pathways{padding:96px 0;background:var(--ivory);color:#2b1827}
  .path-grid{display:grid;grid-template-columns:repeat(4,1fr);gap:15px}
  .path-grid article{min-height:280px;border:1px solid rgba(80,45,70,.13);border-radius:24px;padding:26px;background:#fff}
  .path-grid span{color:#9b6b27;font-size:.72rem;font-weight:700}
  .path-grid h2{margin:82px 0 10px;color:#452341;font:600 2rem/1 'Cormorant Garamond',Georgia,serif}
  .path-grid p{margin:0;color:#6d5b68;font-size:.89rem}
  .volunteer{padding:112px 0;background:#100711}
  .volunteer-grid{display:grid;grid-template-columns:.82fr 1.18fr;gap:76px}
  .intro{padding-top:20px}
  .intro>p:not(.eyebrow){max-width:560px;color:#b3a3b1}
  .privacy{display:flex;flex-wrap:wrap;gap:8px;margin-top:30px}
  .privacy span{border:1px solid rgba(225,189,106,.16);border-radius:999px;padding:8px 12px;color:#a996a8;font-size:.72rem}
  .volunteer form{display:grid;gap:17px;border-color:rgba(225,189,106,.18);padding:34px;background:rgba(255,255,255,.04)}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  label{display:grid;gap:8px;color:#d8ccd7;font-size:.75rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase}
  input,select,textarea{width:100%;border:1px solid rgba(225,189,106,.16);border-radius:14px;padding:13px 14px;background:rgba(255,255,255,.05);color:var(--ivory);outline:none;text-transform:none;letter-spacing:0}
  select option{color:#241321}
  input:focus,select:focus,textarea:focus{border-color:rgba(225,189,106,.55)}
  form .btn{width:fit-content}
  button:disabled{opacity:.62;cursor:wait}
  .feedback{margin:0;color:#e09b8d;font-size:.84rem}.feedback.success{color:#a8c4a8}
  .newsletter{padding:88px 0;background:#080308}
  .newsletter-card{display:grid;grid-template-columns:1fr .9fr;gap:70px;align-items:center;border:1px solid var(--line);border-radius:32px;padding:52px;background:radial-gradient(circle at 86% 20%,rgba(225,189,106,.14),transparent 22rem),linear-gradient(135deg,rgba(100,25,111,.25),rgba(255,255,255,.02))}
  .newsletter-card h2{max-width:690px;margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}
  .newsletter-card p:not(.eyebrow){color:#ae9ead}
  .newsletter form{display:grid;grid-template-columns:1fr 1fr;gap:10px}
  .newsletter form .btn{grid-column:1/-1;width:100%}
  .newsletter form small{grid-column:1/-1;color:#b8a8b6}
  @media(max-width:920px){.path-grid{grid-template-columns:1fr 1fr}.volunteer-grid,.newsletter-card{grid-template-columns:1fr}.newsletter-card{gap:36px}}
  @media(max-width:600px){.path-grid{grid-template-columns:1fr}.two,.newsletter form{grid-template-columns:1fr}.path-grid article{min-height:230px}.path-grid h2{margin-top:54px}.newsletter-card{padding:34px 24px}}
</style>
