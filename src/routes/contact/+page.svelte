<svelte:head>
  <title>Contact | Queen Tovah Cares Foundation International</title>
  <meta name="description" content="Contact Queen Tovah Cares Foundation International for humanitarian, partnership, scholarship and community enquiries." />
</svelte:head>

<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
</script>

<PageHero
  eyebrow="Contact"
  title="Start a conversation"
  accent="that can do good."
  copy="For humanitarian enquiries, partnerships, sponsorship, scholarship matters and community initiatives, use the appropriate Foundation contact channel once published."
/>

<section class="contact">
  <div class="container contact-grid">
    <div class="contact-copy">
      <p class="eyebrow">Get in touch</p>
      <h2 class="section-title">Partnership begins with a clear purpose.</h2>
      <p>
        The official email address, telephone number and public office details will be added after
        confirmation. We are intentionally not placing guessed contact information on the website.
      </p>
      <div class="topics">
        <span>Humanitarian support</span><span>Scholarships</span><span>Partnerships</span><span>Youth & sports</span><span>Community programs</span>
      </div>
    </div>

    <form class="card" onsubmit={(event) => event.preventDefault()}>
      <label>Name<input name="name" placeholder="Your name" /></label>
      <label>Email<input name="email" type="email" placeholder="you@example.com" /></label>
      <label>Enquiry type
        <select name="type">
          <option>General enquiry</option>
          <option>Partnership</option>
          <option>Humanitarian support</option>
          <option>Scholarship</option>
          <option>Media</option>
        </select>
      </label>
      <label>Message<textarea name="message" rows="6" placeholder="How can we help?"></textarea></label>
      <button type="button" class="btn btn-primary">Contact form activates at launch</button>
      <small>No information is submitted yet; backend delivery will be connected before launch.</small>
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
  form small{color:#8e7b88}
  @media(max-width:850px){.contact-grid{grid-template-columns:1fr;gap:46px}}
</style>
