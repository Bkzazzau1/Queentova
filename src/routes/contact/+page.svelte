<svelte:head>
  <title>Contact | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Contact Queen Tovah Cares Foundation International for humanitarian, partnership, scholarship and community enquiries." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  import { submitContact, type ContactPayload } from '$lib/api/content';

  let form: ContactPayload = {
    name: '',
    email: '',
    enquiry_type: 'general',
    message: ''
  };
  let submitting = false;
  let feedback = '';
  let succeeded = false;

  async function sendMessage(event: SubmitEvent) {
    event.preventDefault();
    submitting = true;
    feedback = '';
    succeeded = false;

    try {
      await submitContact(form);
      succeeded = true;
      feedback = 'Thank you. Your message has been received by the Foundation.';
      form = { name: '', email: '', enquiry_type: 'general', message: '' };
    } catch {
      feedback = 'We could not send your message. Please try again shortly.';
    } finally {
      submitting = false;
    }
  }
</script>

<PageHero
  eyebrow="Contact"
  title="Start a conversation"
  accent="that can do good."
  copy="For humanitarian enquiries, partnerships, sponsorship, scholarship matters and community initiatives, send a message directly to the Foundation team."
/>

<section class="contact">
  <div class="container contact-grid">
    <div class="contact-copy">
      <p class="eyebrow">Get in touch</p>
      <h2 class="section-title">Partnership begins with a clear purpose.</h2>
      <p>
        The website now routes enquiries into the Foundation administration system. Official public
        telephone, email and office details can be added here after Foundation confirmation.
      </p>
      <div class="topics">
        <span>Humanitarian support</span><span>Scholarships</span><span>Partnerships</span><span>Youth & sports</span><span>Community programs</span>
      </div>
    </div>

    <form class="card" onsubmit={sendMessage}>
      <label>Name<input name="name" required maxlength="160" placeholder="Your name" bind:value={form.name} /></label>
      <label>Email<input name="email" required type="email" placeholder="you@example.com" bind:value={form.email} /></label>
      <label>Enquiry type
        <select name="type" bind:value={form.enquiry_type}>
          <option value="general">General enquiry</option>
          <option value="partnership">Partnership</option>
          <option value="humanitarian">Humanitarian support</option>
          <option value="scholarship">Scholarship</option>
          <option value="media">Media</option>
        </select>
      </label>
      <label>Message<textarea name="message" required rows="6" maxlength="6000" placeholder="How can we help?" bind:value={form.message}></textarea></label>
      <button type="submit" class="btn btn-primary" disabled={submitting}>
        {submitting ? 'Sending…' : 'Send message'}
      </button>
      {#if feedback}
        <p class:success={succeeded} class="feedback" role="status">{feedback}</p>
      {:else}
        <small>Messages are stored securely for authorised Foundation administrators to review.</small>
      {/if}
    </form>
  </div>
</section>

<style>
  .contact{padding:110px 0;background:var(--ivory);color:#2a1926}
  .contact-grid{display:grid;grid-template-columns:.9fr 1.1fr;gap:80px}
  .contact-copy .eyebrow{color:#8e6020}
  .contact-copy .section-title{color:#341d31}
  .contact-copy>p:not(.eyebrow){max-width:600px;color:#6d5b68}
  .topics{display:flex;flex-wrap:wrap;gap:8px;margin-top:30px}
  .topics span{border:1px solid rgba(80,45,70,.15);border-radius:999px;padding:8px 13px;color:#705e6b;font-size:.78rem}
  form{display:grid;gap:18px;border-color:rgba(80,45,70,.13);padding:34px;background:#fff;color:#42243d;box-shadow:0 26px 70px rgba(60,30,50,.08)}
  label{display:grid;gap:8px;font-size:.78rem;font-weight:700;letter-spacing:.05em;text-transform:uppercase}
  input,select,textarea{width:100%;border:1px solid rgba(80,45,70,.14);border-radius:14px;padding:13px 14px;background:#fbf7f1;color:#35212f;outline:none;text-transform:none;letter-spacing:0}
  input:focus,select:focus,textarea:focus{border-color:#b78335}
  form .btn{width:fit-content}
  form .btn:disabled{cursor:wait;opacity:.65}
  form small{color:#8e7b88}
  .feedback{margin:0;color:#9a5b4c;font-size:.85rem}
  .feedback.success{color:#527052}
  @media(max-width:850px){.contact-grid{grid-template-columns:1fr;gap:46px}}
</style>
