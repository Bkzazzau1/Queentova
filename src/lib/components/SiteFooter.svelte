<script lang="ts">
  import { subscribeNewsletter, type SiteProfile } from '$lib/api/content';

  let { profile = null }: { profile?: SiteProfile | null } = $props();

  let name = '';
  let email = '';
  let busy = false;
  let feedback = '';

  async function subscribe(event: SubmitEvent) {
    event.preventDefault();
    busy = true;
    feedback = '';
    try {
      await subscribeNewsletter(email, name);
      feedback = 'Thank you — you are subscribed.';
      name = '';
      email = '';
    } catch {
      feedback = 'We could not subscribe you right now.';
    } finally {
      busy = false;
    }
  }
</script>

<footer id="contact">
  <div class="container footer-grid">
    <div class="intro">
      <img class="footer-logo" src="/brand/queen-tovah-logo.webp" alt="Queen Tovah Cares Foundation International logo" />
      <h2>{profile?.display_name || 'Queen Tovah Cares Foundation International'}</h2>
      <p>
        {profile?.short_description || 'Compassion with dignity. Opportunity with purpose. A global outlook rooted in service to people and communities.'}
      </p>

      {#if profile?.contact_email || profile?.phone || profile?.office_address}
        <div class="official-contact">
          {#if profile.contact_email}<a href={`mailto:${profile.contact_email}`}>{profile.contact_email}</a>{/if}
          {#if profile.phone}<a href={`tel:${profile.phone}`}>{profile.phone}</a>{/if}
          {#if profile.office_address}<span>{profile.office_address}</span>{/if}
        </div>
      {/if}
    </div>

    <div class="links">
      <p class="label">Explore</p>
      <a href="/about">About the Foundation</a>
      <a href="/programs">Our Programs</a>
      <a href="/causes">Causes</a>
      <a href="/impact">Impact & Accountability</a>
      <a href="/news">Stories</a>
      <a href="/gallery">Gallery</a>
    </div>

    <div class="links">
      <p class="label">Participate</p>
      <a href="/events">Events</a>
      <a href="/scholarships">Scholarships</a>
      <a href="/request-support">Request Support</a>
      <a href="/resources">Reports & Resources</a>
      <a href="/get-involved">Volunteer & Get Involved</a>
      <a href="/donate">Support the Mission</a>
      <a href="/contact">Contact the Foundation</a>
      <a href="/search">Search</a>
    </div>

    <div class="newsletter">
      <p class="label">Foundation updates</p>
      <p class="newsletter-copy">Receive meaningful updates, verified impact stories and opportunities to participate.</p>
      <form onsubmit={subscribe}>
        <input aria-label="Name" bind:value={name} placeholder="Your name" />
        <input aria-label="Email address" required type="email" bind:value={email} placeholder="Email address" />
        <button type="submit" disabled={busy}>{busy ? 'Joining…' : 'Join updates'}</button>
      </form>
      {#if feedback}<small>{feedback}</small>{/if}

      {#if profile?.facebook_url || profile?.instagram_url || profile?.x_url || profile?.linkedin_url || profile?.youtube_url}
        <div class="socials">
          {#if profile.facebook_url}<a href={profile.facebook_url} target="_blank" rel="noreferrer">Facebook</a>{/if}
          {#if profile.instagram_url}<a href={profile.instagram_url} target="_blank" rel="noreferrer">Instagram</a>{/if}
          {#if profile.x_url}<a href={profile.x_url} target="_blank" rel="noreferrer">X</a>{/if}
          {#if profile.linkedin_url}<a href={profile.linkedin_url} target="_blank" rel="noreferrer">LinkedIn</a>{/if}
          {#if profile.youtube_url}<a href={profile.youtube_url} target="_blank" rel="noreferrer">YouTube</a>{/if}
        </div>
      {/if}
    </div>
  </div>

  <div class="container bottom">
    <span>© {new Date().getFullYear()} Queen Tovah Cares Foundation International.</span>
    <em>“It is good to be good.”</em>
  </div>
</footer>

<style>
  footer {
    position: relative;
    overflow: hidden;
    border-top: 1px solid rgba(225, 189, 106, 0.16);
    padding: 76px 0 26px;
    background:
      radial-gradient(circle at 90% 20%, rgba(100, 25, 111, 0.22), transparent 26rem),
      #070307;
  }

  .footer-grid {
    display: grid;
    grid-template-columns: minmax(0, 1.45fr) 0.72fr 0.8fr minmax(250px, 1fr);
    gap: 44px;
  }

  .footer-logo {
    width: 128px;
    border: 1px solid rgba(225, 189, 106, 0.24);
    border-radius: 16px;
    box-shadow: 0 18px 40px rgba(0, 0, 0, 0.24);
  }

  h2 {
    max-width: 500px;
    margin: 20px 0 12px;
    font-family: 'Cormorant Garamond', Georgia, serif;
    color: var(--champagne);
    font-size: clamp(1.9rem, 3vw, 2.8rem);
    font-weight: 600;
    line-height: 1;
  }

  .intro > p,
  .links span,
  .newsletter-copy {
    color: #a998a8;
  }

  .intro > p {
    max-width: 520px;
    margin: 0;
  }

  .official-contact {
    display: grid;
    gap: 6px;
    margin-top: 18px;
    color: #c8b9c7;
    font-size: 0.82rem;
  }

  .official-contact a:hover {
    color: var(--gold-bright);
  }

  .links {
    display: flex;
    flex-direction: column;
    gap: 11px;
    font-size: 0.88rem;
  }

  .label {
    margin: 0 0 6px;
    color: var(--gold-bright);
    font-size: 0.76rem;
    font-weight: 700;
    letter-spacing: 0.1em;
    text-transform: uppercase;
  }

  .links a {
    color: #e5dbe4;
  }

  .links a:hover,
  .socials a:hover {
    color: var(--gold-bright);
  }

  .newsletter-copy {
    margin: 0 0 14px;
    font-size: 0.84rem;
  }

  .newsletter form {
    display: grid;
    gap: 8px;
  }

  .newsletter input {
    width: 100%;
    border: 1px solid rgba(225, 189, 106, 0.15);
    border-radius: 12px;
    padding: 11px 12px;
    background: rgba(255,255,255,0.04);
    color: var(--ivory);
    outline: none;
  }

  .newsletter input:focus {
    border-color: rgba(225, 189, 106, 0.48);
  }

  .newsletter button {
    border-radius: 12px;
    padding: 11px 14px;
    background: linear-gradient(135deg, var(--gold-bright), var(--gold));
    color: #1b0b18;
    font-weight: 800;
    cursor: pointer;
  }

  .newsletter button:disabled {
    cursor: wait;
    opacity: .62;
  }

  .newsletter small {
    display: block;
    margin-top: 8px;
    color: #b9a9b7;
  }

  .socials {
    display: flex;
    flex-wrap: wrap;
    gap: 8px 13px;
    margin-top: 16px;
    font-size: .76rem;
  }

  .socials a {
    color: #c7b9c6;
  }

  .bottom {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    margin-top: 58px;
    border-top: 1px solid rgba(255, 255, 255, 0.08);
    padding-top: 24px;
    color: #8f7f8e;
    font-size: 0.82rem;
  }

  .bottom em {
    color: var(--gold-bright);
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: 1rem;
  }

  @media (max-width: 1060px) {
    .footer-grid {
      grid-template-columns: 1.35fr 1fr 1fr;
    }
    .newsletter {
      grid-column: 1 / -1;
      max-width: 620px;
    }
  }

  @media (max-width: 760px) {
    .footer-grid {
      grid-template-columns: 1fr 1fr;
    }
    .intro,
    .newsletter {
      grid-column: 1 / -1;
    }
  }

  @media (max-width: 520px) {
    .footer-grid {
      grid-template-columns: 1fr;
    }
    .intro,
    .newsletter {
      grid-column: auto;
    }
    .bottom {
      flex-direction: column;
    }
  }
</style>
