<svelte:head>
  <title>Request Support | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Send a private humanitarian support request to Queen Tovah Cares Foundation International." />
  <meta name="robots" content="index,follow" />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  import { submitSupportRequest, type SupportRequestPayload } from '$lib/api/content';

  let form: SupportRequestPayload = {
    name: '',
    email: '',
    phone: '',
    country: '',
    city: '',
    assistance_type: 'general',
    request_summary: '',
    consent_to_contact: false
  };

  let busy = false;
  let feedback = '';
  let success = false;

  async function submit(event: SubmitEvent) {
    event.preventDefault();
    busy = true;
    feedback = '';
    success = false;
    try {
      await submitSupportRequest(form);
      success = true;
      feedback = 'Your request has been received privately for Foundation review.';
      form = {
        name: '', email: '', phone: '', country: '', city: '',
        assistance_type: 'general', request_summary: '', consent_to_contact: false
      };
    } catch {
      feedback = 'We could not submit your request. Check that you provided a contact method and consent, then try again.';
    } finally {
      busy = false;
    }
  }
</script>

<PageHero
  eyebrow="Request humanitarian support"
  title="Asking for help should"
  accent="still preserve dignity."
  copy="This private intake sends your request to authorised Foundation administrators. It is not published on the website."
/>

<section class="support-request">
  <div class="container request-grid">
    <div class="guidance">
      <p class="eyebrow">Before you submit</p>
      <h2 class="section-title">Tell us only what is necessary.</h2>
      <p>
        This first-stage form is intentionally simple. Do not upload identity documents, bank details,
        medical records or other highly sensitive documents here. If follow-up is appropriate, the Foundation
        can request necessary information through an approved private channel.
      </p>
      <div class="principles">
        <span>Private review</span>
        <span>No public beneficiary profile</span>
        <span>No guarantee of assistance</span>
        <span>Need-based assessment</span>
      </div>
    </div>

    <form class="card" onsubmit={submit}>
      <div class="two">
        <label>Full name<input required maxlength="180" bind:value={form.name} placeholder="Your name" /></label>
        <label>Country<input required maxlength="120" bind:value={form.country} placeholder="Country" /></label>
      </div>

      <div class="two">
        <label>Email<input type="email" bind:value={form.email} placeholder="Email address" /></label>
        <label>Phone<input bind:value={form.phone} placeholder="Phone number" /></label>
      </div>

      <div class="two">
        <label>City<input maxlength="120" bind:value={form.city} placeholder="City" /></label>
        <label>Type of support
          <select bind:value={form.assistance_type}>
            <option value="general">General humanitarian support</option>
            <option value="education">Education</option>
            <option value="family">Family support</option>
            <option value="shelter">Shelter / housing</option>
            <option value="livelihood">Livelihood / empowerment</option>
            <option value="other">Other</option>
          </select>
        </label>
      </div>

      <label>Briefly explain the situation
        <textarea required rows="7" maxlength="5000" bind:value={form.request_summary} placeholder="Explain the need clearly and briefly."></textarea>
      </label>

      <label class="consent">
        <input type="checkbox" bind:checked={form.consent_to_contact} required />
        <span>I consent to Queen Tovah Cares Foundation International contacting me about this request.</span>
      </label>

      <button class="btn btn-primary" type="submit" disabled={busy}>{busy ? 'Submitting privately…' : 'Submit private request'}</button>

      {#if feedback}<p class:success class="feedback" class:success={success} role="status">{feedback}</p>{/if}
      <small>At least one contact method — email or phone — is required for follow-up.</small>
    </form>
  </div>
</section>

<section class="emergency">
  <div class="container">
    <p><strong>Important:</strong> This website is not an emergency-response service. For immediate danger or urgent medical emergencies, contact the appropriate local emergency service.</p>
  </div>
</section>

<style>
  .support-request{padding:110px 0;background:var(--ivory);color:#2b1827}
  .request-grid{display:grid;grid-template-columns:.82fr 1.18fr;gap:78px}
  .guidance .eyebrow{color:#8e6020}.guidance .section-title{color:#341d31}.guidance>p:not(.eyebrow){color:#6d5b68}
  .principles{display:flex;flex-wrap:wrap;gap:8px;margin-top:30px}.principles span{border:1px solid rgba(80,45,70,.13);border-radius:999px;padding:8px 12px;background:#fff;color:#705f6c;font-size:.73rem}
  form{display:grid;gap:17px;border-color:rgba(80,45,70,.13);padding:34px;background:#fff;color:#42243d;box-shadow:0 26px 70px rgba(60,30,50,.08)}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  label{display:grid;gap:8px;font-size:.75rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase}
  input,select,textarea{width:100%;border:1px solid rgba(80,45,70,.14);border-radius:14px;padding:13px 14px;background:#fbf7f1;color:#35212f;outline:none;text-transform:none;letter-spacing:0}
  input:focus,select:focus,textarea:focus{border-color:#b78335}
  .consent{grid-template-columns:auto 1fr;align-items:start;text-transform:none;letter-spacing:0;font-weight:500;line-height:1.45}.consent input{width:18px;height:18px;margin-top:1px}
  form .btn{width:fit-content}button:disabled{opacity:.62;cursor:wait}
  .feedback{margin:0;color:#9a5b4c;font-size:.84rem}.feedback.success{color:#527052}form small{color:#8d7b88}
  .emergency{padding:28px 0;background:#120713;color:#b7a7b5}.emergency p{margin:0;font-size:.83rem}.emergency strong{color:var(--gold-bright)}
  @media(max-width:880px){.request-grid{grid-template-columns:1fr;gap:44px}}
  @media(max-width:600px){.two{grid-template-columns:1fr}form{padding:28px 22px}}
</style>
