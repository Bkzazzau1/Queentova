<script lang="ts">
  import PageHero from '$lib/components/PageHero.svelte';
  import {
    submitScholarshipApplication,
    type ScholarshipApplicationReceipt
  } from '$lib/api/content';

  let { data } = $props();
  const { scholarship } = $derived(data);

  let busy = $state(false);
  let errorMessage = $state('');
  let receipt = $state<ScholarshipApplicationReceipt | null>(null);

  async function submit(event: SubmitEvent) {
    event.preventDefault();
    if (busy) return;

    const form = event.currentTarget as HTMLFormElement;
    const formData = new FormData(form);
    formData.set('consent_to_processing', 'true');
    formData.set('declaration_true', 'true');

    busy = true;
    errorMessage = '';

    try {
      receipt = await submitScholarshipApplication(scholarship.slug, formData);
      form.reset();
      window.scrollTo({ top: 0, behavior: 'smooth' });
    } catch (error) {
      errorMessage = error instanceof Error ? error.message : 'Unable to submit your application.';
    } finally {
      busy = false;
    }
  }
</script>

<svelte:head>
  <title>Apply | {scholarship.title} | Queen Tovah Scholarships</title>
  <meta name="robots" content="noindex,nofollow" />
  <meta
    name="description"
    content={`Secure Foundation-managed application for ${scholarship.title}.`}
  />
</svelte:head>

<PageHero
  eyebrow="Private scholarship application"
  title={scholarship.title}
  copy="Submit directly to the Foundation. Your documents, application details, scores and reviewer notes are not published on the public website."
/>

<section class="apply">
  <div class="container">
    {#if receipt}
      <div class="receipt card">
        <span class="success">Application received</span>
        <h2>Keep your reference code safe.</h2>
        <div class="reference">{receipt.reference_code}</div>
        <p>
          Your application for <strong>{receipt.scholarship}</strong> has been received with status
          <strong>{receipt.status_label}</strong>.
        </p>
        <div class="receipt-actions">
          <a class="btn btn-primary" href="/scholarships/status">Check application status</a>
          <a class="btn btn-secondary" href={`/scholarships/${scholarship.slug}`}>Back to scholarship</a>
        </div>
        <small>
          The Foundation will never ask you to post your reference code, identity document or academic
          records publicly.
        </small>
      </div>
    {:else if scholarship.internal_applications_open}
      <div class="apply-grid">
        <aside class="card">
          <p class="eyebrow">Before you submit</p>
          <h2>Prepare one complete application.</h2>
          <p>
            Only one application is accepted per email address for this scholarship. Review your
            details carefully before submitting.
          </p>

          {#if scholarship.closes_at}
            <div class="deadline">
              <span>Applications close</span>
              <strong>{new Intl.DateTimeFormat('en',{dateStyle:'long'}).format(new Date(scholarship.closes_at))}</strong>
            </div>
          {/if}

          {#if scholarship.required_documents}
            <div class="prepare">
              <span>Published document guidance</span>
              {#each scholarship.required_documents.split('\n').filter(Boolean) as item}
                <p>✓ {item}</p>
              {/each}
            </div>
          {/if}

          <div class="privacy-note">
            <strong>Private by design</strong>
            <p>
              Uploaded files are stored as application records and are not exposed by public
              scholarship APIs or the public status checker.
            </p>
          </div>
        </aside>

        <form class="application-form" onsubmit={submit}>
          <fieldset>
            <legend>01 — Applicant details</legend>
            <div class="two">
              <label>
                <span>First name *</span>
                <input name="first_name" autocomplete="given-name" required maxlength="100" />
              </label>
              <label>
                <span>Last name *</span>
                <input name="last_name" autocomplete="family-name" required maxlength="100" />
              </label>
            </div>
            <div class="two">
              <label>
                <span>Email *</span>
                <input name="email" type="email" autocomplete="email" required />
              </label>
              <label>
                <span>Phone</span>
                <input name="phone" autocomplete="tel" maxlength="40" />
              </label>
            </div>
            <div class="two">
              <label>
                <span>Country *</span>
                <input name="country" autocomplete="country-name" required maxlength="120" />
              </label>
              <label>
                <span>City</span>
                <input name="city" autocomplete="address-level2" maxlength="120" />
              </label>
            </div>
          </fieldset>

          <fieldset>
            <legend>02 — Academic context</legend>
            <label>
              <span>Institution</span>
              <input name="institution" maxlength="220" />
            </label>
            <div class="two">
              <label>
                <span>Course / area of study</span>
                <input name="course_of_study" maxlength="220" />
              </label>
              <label>
                <span>Current level / class</span>
                <input name="current_level" maxlength="120" />
              </label>
            </div>
            <label>
              <span>Academic summary</span>
              <textarea
                name="academic_summary"
                rows="4"
                placeholder="Briefly describe your academic standing, relevant results or achievements."
              ></textarea>
            </label>
          </fieldset>

          <fieldset>
            <legend>03 — Your case for support</legend>
            <label>
              <span>Financial need statement *</span>
              <textarea
                name="financial_need_statement"
                rows="6"
                required
                placeholder="Explain the financial circumstances affecting your education."
              ></textarea>
            </label>
            <label>
              <span>Personal statement *</span>
              <textarea
                name="personal_statement"
                rows="7"
                required
                placeholder="Explain your goals, why this opportunity matters and how you hope to use your education."
              ></textarea>
            </label>
          </fieldset>

          <fieldset>
            <legend>04 — Private documents</legend>
            <p class="field-note">PDF, JPG or PNG. Maximum 8 MB per file. Upload only documents relevant to this application.</p>
            <div class="file-grid">
              <label class="file">
                <span>Academic record / transcript</span>
                <input name="academic_document" type="file" accept=".pdf,.jpg,.jpeg,.png" />
              </label>
              <label class="file">
                <span>Identity document</span>
                <input name="identity_document" type="file" accept=".pdf,.jpg,.jpeg,.png" />
              </label>
              <label class="file">
                <span>Admission / enrolment evidence</span>
                <input name="admission_document" type="file" accept=".pdf,.jpg,.jpeg,.png" />
              </label>
              <label class="file">
                <span>Recommendation</span>
                <input name="recommendation_document" type="file" accept=".pdf,.jpg,.jpeg,.png" />
              </label>
              <label class="file">
                <span>Other supporting document</span>
                <input name="supporting_document" type="file" accept=".pdf,.jpg,.jpeg,.png" />
              </label>
            </div>
          </fieldset>

          <fieldset>
            <legend>05 — Consent & declaration</legend>
            <label class="check">
              <input name="consent_to_processing" type="checkbox" required />
              <span>
                I consent to the Foundation processing the information and documents in this application
                for scholarship assessment and administration.
              </span>
            </label>
            <label class="check">
              <input name="declaration_true" type="checkbox" required />
              <span>
                I confirm that the information supplied is accurate to the best of my knowledge.
              </span>
            </label>
          </fieldset>

          {#if errorMessage}<div class="error" role="alert">{errorMessage}</div>{/if}

          <button class="btn btn-primary submit" type="submit" disabled={busy}>
            {busy ? 'Submitting securely…' : 'Submit scholarship application'}
          </button>
          <small class="submit-note">
            After submission you will receive a reference code. Save it; you will need it together with
            your email to check your application status.
          </small>
        </form>
      </div>
    {:else}
      <div class="closed card">
        <span>Applications are not open</span>
        <h2>This Foundation-managed form is currently unavailable.</h2>
        <p>Return to the scholarship page for the current application status and official channel.</p>
        <a class="btn btn-primary" href={`/scholarships/${scholarship.slug}`}>Scholarship details</a>
      </div>
    {/if}
  </div>
</section>

<style>
  .apply{padding:105px 0 120px;background:var(--ivory);color:#2b1827}
  .apply-grid{display:grid;grid-template-columns:330px minmax(0,1fr);gap:56px;align-items:start}
  aside{position:sticky;top:118px;border-color:rgba(80,45,70,.13);padding:28px;background:#fff;color:#3d2039}
  aside .eyebrow{color:#8e6020}aside h2{margin:8px 0 12px;color:#43213f;font:600 2.2rem/1 'Cormorant Garamond',Georgia,serif}aside>p{color:#6d5b68}
  .deadline,.prepare,.privacy-note{margin-top:24px;border-top:1px solid rgba(80,45,70,.1);padding-top:18px}.deadline span,.prepare>span{display:block;color:#9a8059;font-size:.68rem;font-weight:800;text-transform:uppercase}.deadline strong{display:block;margin-top:6px;color:#4a3346}.prepare p{margin:9px 0;color:#6d5b68;font-size:.78rem}
  .privacy-note{border:1px solid rgba(90,130,85,.16);border-radius:16px;padding:16px;background:#f6faf4}.privacy-note strong{color:#587252}.privacy-note p{margin:6px 0 0;color:#6b7967;font-size:.77rem}

  .application-form{display:grid;gap:18px}
  fieldset{display:grid;gap:18px;border:1px solid rgba(80,45,70,.12);border-radius:24px;padding:28px;background:#fff}
  legend{padding:0 9px;color:#8e6020;font-size:.72rem;font-weight:800;letter-spacing:.07em;text-transform:uppercase}
  label{display:grid;gap:7px}label>span{color:#5d4b58;font-size:.78rem;font-weight:700}
  .two{display:grid;grid-template-columns:1fr 1fr;gap:14px}
  input,textarea{width:100%;border:1px solid rgba(80,45,70,.14);border-radius:12px;padding:12px 13px;background:#fdfbf8;color:#382334;outline:none;font:inherit}
  input:focus,textarea:focus{border-color:rgba(166,112,37,.55);box-shadow:0 0 0 3px rgba(166,112,37,.08)}
  textarea{resize:vertical}
  .field-note{margin:0;color:#806f7b;font-size:.78rem}
  .file-grid{display:grid;grid-template-columns:1fr 1fr;gap:12px}.file{border:1px dashed rgba(80,45,70,.16);border-radius:16px;padding:14px;background:#fbf8f3}.file input{border:0;padding:8px 0;background:transparent;font-size:.76rem}
  .check{grid-template-columns:auto 1fr;align-items:start;gap:10px}.check input{width:18px;height:18px;margin-top:2px}.check span{font-weight:500;line-height:1.55}
  .error{border:1px solid rgba(150,65,65,.22);border-radius:14px;padding:13px 15px;background:#fff5f5;color:#8a3f3f;font-size:.82rem}
  .submit{justify-self:start;min-width:280px}.submit-note{max-width:720px;color:#806f7b;line-height:1.5}

  .receipt,.closed{max-width:800px;margin:auto;border-color:rgba(80,45,70,.12);padding:58px;background:#fff;text-align:center}
  .success,.closed>span{display:inline-flex;border:1px solid rgba(85,120,80,.22);border-radius:999px;padding:7px 10px;background:#f6faf4;color:#587252;font-size:.68rem;font-weight:800;text-transform:uppercase}
  .receipt h2,.closed h2{margin:25px 0 12px;color:#43213f;font:600 2.8rem/1 'Cormorant Garamond',Georgia,serif}
  .reference{display:inline-block;margin:14px 0;border:1px solid rgba(166,112,37,.24);border-radius:16px;padding:15px 20px;background:#fff9ef;color:#8e6020;font:700 1.5rem/1.1 Manrope,sans-serif;letter-spacing:.08em}
  .receipt p,.closed p{max-width:620px;margin:10px auto;color:#6d5b68}.receipt-actions{display:flex;flex-wrap:wrap;justify-content:center;gap:10px;margin-top:26px}.receipt small{display:block;max-width:620px;margin:22px auto 0;color:#887784}
  .closed .btn{margin-top:22px}

  @media(max-width:900px){.apply-grid{grid-template-columns:1fr}aside{position:static;max-width:620px}}
  @media(max-width:620px){.two,.file-grid{grid-template-columns:1fr}fieldset{padding:22px 18px}.receipt,.closed{padding:42px 22px}.submit{width:100%;min-width:0}}
</style>
