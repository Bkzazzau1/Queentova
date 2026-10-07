<script lang="ts">
  let {
    eyebrow,
    title,
    copy,
    accent = ''
  }: { eyebrow: string; title: string; copy: string; accent?: string } = $props();
</script>

<section class="page-hero">
  <div class="orb"></div>
  <div class="container hero-inner">
    <div>
      <p class="eyebrow">{eyebrow}</p>
      <h1>{title} {#if accent}<span>{accent}</span>{/if}</h1>
      <p class="copy">{copy}</p>
    </div>
    <img src="/brand/queen-tovah-crest.webp" alt="" aria-hidden="true" width="520" height="419" />
  </div>
</section>

<style>
  .page-hero {
    position: relative;
    isolation: isolate;
    overflow: hidden;
    padding: 170px 0 92px;
    border-bottom: 1px solid rgba(225, 189, 106, 0.14);
    background:
      radial-gradient(circle at 78% 34%, rgba(201, 151, 63, 0.16), transparent 24rem),
      radial-gradient(circle at 14% 4%, rgba(100, 25, 111, 0.22), transparent 25rem),
      #080308;
  }

  .orb {
    position: absolute;
    z-index: -1;
    top: 80px;
    right: -90px;
    width: 420px;
    height: 420px;
    border: 1px solid rgba(225, 189, 106, 0.13);
    border-radius: 50%;
    box-shadow: inset 0 0 100px rgba(100, 25, 111, 0.1);
  }

  .hero-inner {
    display: grid;
    grid-template-columns: minmax(0, 1fr) 280px;
    align-items: center;
    gap: 72px;
  }

  h1 {
    max-width: 860px;
    margin: 0;
    font-family: 'Cormorant Garamond', Georgia, serif;
    font-size: clamp(3.4rem, 7vw, 6.6rem);
    font-weight: 600;
    line-height: 0.92;
    letter-spacing: -0.045em;
  }

  h1 span {
    color: var(--gold-bright);
  }

  .copy {
    max-width: 720px;
    margin: 28px 0 0;
    color: #cfbfce;
    font-size: 1.05rem;
  }

  img {
    width: 100%;
    height: auto;
    filter: drop-shadow(0 20px 40px rgba(201, 151, 63, 0.16));
  }

  @media (max-width: 820px) {
    .page-hero {
      padding-top: 140px;
    }

    .hero-inner {
      grid-template-columns: 1fr;
      gap: 38px;
    }

    img {
      width: min(200px, 56vw);
    }
  }
</style>
