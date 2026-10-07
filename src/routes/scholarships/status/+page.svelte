<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  import {
    checkScholarshipApplicationStatus,
    type ScholarshipApplicationStatusResult
  } from '$lib/api/content';

  let referenceCode = $state('');
  let email = $state('');
  let busy = $state(false);
  let errorMessage = $state('');
  let result = $state<ScholarshipApplicationStatusResult | null>(null);

  const statusCopy: Record<string,string> = {
    submitted: 'Your application has been received and is awaiting review.',
    screening: 'Your application is currently being screened.',
    eligible: 'Your application passed the eligibility stage.',
    shortlisted: 'Your application has been shortlisted for further consideration.',
    approved: 'Your application has been approved. The Foundation will contact you through the official contact details supplied in your application.',
    rejected: 'The application process has concluded for this application.',
    withdrawn: 'This application has been withdrawn.'
  };

  async function check(event: SubmitEvent) {
    event.preventDefault();
    busy = true;
    errorMessage = '';
    result = null;

    try {
      result = await checkScholarshipApplicationStatus(referenceCode, email);
    } catch (error) {
      errorMessage = error instanceof Error ? error.message : 'Unable to check the application.';
    } finally {
      busy = false;
    }
  }
</script>

<svelte:head>
  <title>Check Scholarship Application Status | Queen Tovah</title>
  <meta name="robots" content="noindex,nofollow" />
  <meta
    name="description"
    content="Privately check the current status of a Queen Tovah Cares Foundation International scholarship application."
  />
</svelte:head>

<PageHero
  eyebrow="Private application tracker"
  title="Check your"
  accent="scholarship status."
  copy="Use the reference code issued after submission together with the same email address used on your application."
/>

<section class="status-page">
  <div class="container status-grid">
    <div class="explain">
      <p class="eyebrow">What this checker shows</p>
      <h2>Only the status — not your private review file.</h2>
      <p>
        The public checker does not expose your uploaded documents, eligibility score, reviewer notes,
        internal assessment or other applicants.
      </p>

      <div class="steps">
        <div><span>01</span><p>Enter your Queen Tovah application reference.</p></div>
        <div><span>02</span><p>Use the exact email address submitted with the application.</p></div>
        <div><span>03</span><p>See the current high-level review status.</p></div>
      </div>
    </div>

    <div class="checker card">
      <form onsubmit={check}>
        <label>
          <span>Application reference</span>
          <input
            bind:value={referenceCode}
            required
            autocomplete="off"
            placeholder="QT-XXXXXXXXXX"
            maxlength="20"
          />
        </label>

        <label>
          <span>Application email</span>
          <input
            bind:value={email}
            required
            type="email"
            autocomplete="email"
            placeholder="you@example.com"
          />
        </label>

        {#if errorMessage}<div class="error" role="alert">{errorMessage}</div>{/if}

        <button class="btn btn-primary" type="submit" disabled={busy}>
          {busy ? 'Checking…' : 'Check application'}
        </button>
      </form>

      {#if result}
        <div class="result">
          <span class:approved={result.status === 'approved'}>{result.status_label}</span>
          <h3>{result.scholarship}</h3>
          <div class="reference">{result.reference_code}</div>
          <p>{statusCopy[result.status] || 'Your application status has been updated.'}</p>

          <dl>
            <div>
              <dt>Submitted</dt>
              <dd>{new Intl.DateTimeFormat('en',{dateStyle:'medium'}).format(new Date(result.submitted_at))}</dd>
            </div>
            {#if result.reviewed_at}
              <div>
                <dt>Last reviewed</dt>
                <dd>{new Intl.DateTimeFormat('en',{dateStyle:'medium'}).format(new Date(result.reviewed_at))}</dd>
              </div>
            {/if}
          </dl>
        </div>
      {/if}
    </div>
  </div>
</section>

<section class="security">
  <div class="container security-card">
    <div>
      <p class="eyebrow">Protect your application</p>
      <h2>Do not post your reference code or documents publicly.</h2>
      <p>
        If someone contacts you claiming to represent the Foundation, use the official website contact
        route before sharing additional information or making any payment.
      </p>
    </div>
    <a class="btn btn-secondary" href="/contact">Official contact route</a>
  </div>
</section>

<style>
  .status-page{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .status-grid{display:grid;grid-template-columns:.8fr 1.2fr;gap:72px;align-items:start}
  .explain .eyebrow{color:#8e6020}.explain h2{margin:0;color:#43213f;font:600 clamp(2.5rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}.explain>p:not(.eyebrow){color:#6d5b68}
  .steps{margin-top:34px;border-top:1px solid rgba(80,45,70,.12)}.steps>div{display:grid;grid-template-columns:44px 1fr;gap:14px;border-bottom:1px solid rgba(80,45,70,.12);padding:15px 0}.steps span{color:#9b6c29;font-size:.68rem;font-weight:800}.steps p{margin:0;color:#5f4e5a;font-size:.86rem}

  .checker{border-color:rgba(80,45,70,.13);padding:30px;background:#fff;color:#3d2039}
  form{display:grid;gap:16px}label{display:grid;gap:7px}label span{color:#5d4b58;font-size:.78rem;font-weight:700}
  input{width:100%;border:1px solid rgba(80,45,70,.14);border-radius:12px;padding:13px;background:#fdfbf8;color:#382334;outline:none;font:inherit;text-transform:none}
  input:focus{border-color:rgba(166,112,37,.55);box-shadow:0 0 0 3px rgba(166,112,37,.08)}
  form .btn{justify-self:start;min-width:210px}
  .error{border:1px solid rgba(150,65,65,.22);border-radius:12px;padding:12px 14px;background:#fff5f5;color:#8a3f3f;font-size:.8rem}

  .result{margin-top:28px;border-top:1px solid rgba(80,45,70,.1);padding-top:26px}
  .result>span{display:inline-flex;border:1px solid rgba(166,112,37,.22);border-radius:999px;padding:7px 10px;background:#fff9ef;color:#8e6020;font-size:.67rem;font-weight:800;text-transform:uppercase}
  .result>span.approved{border-color:rgba(85,120,80,.24);background:#f6faf4;color:#587252}
  .result h3{margin:18px 0 10px;color:#43213f;font:600 2.2rem/1 'Cormorant Garamond',Georgia,serif}
  .reference{display:inline-block;border-radius:10px;padding:8px 10px;background:#f5efe7;color:#7b5c31;font-size:.78rem;font-weight:800;letter-spacing:.06em}
  .result>p{color:#6d5b68}
  dl{margin:20px 0 0}dl div{display:flex;justify-content:space-between;gap:18px;border-top:1px solid rgba(80,45,70,.08);padding:12px 0}dt{color:#9a8059;font-size:.68rem;font-weight:800;text-transform:uppercase}dd{margin:0;color:#5d4b58;font-size:.8rem}

  .security{padding:88px 0;background:#090409}.security-card{display:flex;align-items:end;justify-content:space-between;gap:44px;border:1px solid var(--line);border-radius:30px;padding:48px;background:linear-gradient(135deg,rgba(100,25,111,.24),rgba(255,255,255,.02))}
  .security-card h2{max-width:800px;margin:0;color:var(--ivory);font:600 clamp(2.4rem,5vw,4rem)/.98 'Cormorant Garamond',Georgia,serif}.security-card p:not(.eyebrow){max-width:720px;color:#ad9daa}.security-card .btn{flex-shrink:0}
  @media(max-width:840px){.status-grid{grid-template-columns:1fr}.security-card{align-items:flex-start;flex-direction:column}}
  @media(max-width:560px){.checker{padding:22px}.security-card{padding:34px 24px}form .btn{width:100%;min-width:0}}
</style>
