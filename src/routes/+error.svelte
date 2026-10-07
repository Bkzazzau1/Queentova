<script lang="ts">
  import { page } from '$app/state';

  const isNotFound = page.status === 404;
</script>

<svelte:head>
  <title>{isNotFound ? 'Page not found' : 'Something went wrong'} | Queen Tovah</title>
  <meta name="robots" content="noindex,follow" />
</svelte:head>

<section class="error-page">
  <div class="orb"></div>
  <div class="container error-shell">
    <img src="/brand/queen-tovah-logo-full.webp" width="840" height="560" alt="Queen Tovah Cares Foundation International" />
    <p class="eyebrow">{page.status}</p>
    <h1>{isNotFound ? 'This page has moved beyond our path.' : 'Something interrupted the journey.'}</h1>
    <p>
      {isNotFound
        ? 'The page you were looking for may have moved, changed or not yet been published.'
        : 'The website encountered an unexpected problem. You can return home or continue through our main sections.'}
    </p>
    <div class="actions">
      <a class="btn btn-primary" href="/">Return home</a>
      <a class="btn btn-secondary" href="/search">Search the Foundation</a>
    </div>
    <div class="quick">
      <a href="/programs">Programs</a>
      <a href="/causes">Causes</a>
      <a href="/news">Stories</a>
      <a href="/get-involved">Get involved</a>
    </div>
  </div>
</section>

<style>
  .error-page{position:relative;isolation:isolate;overflow:hidden;min-height:100svh;display:grid;align-items:center;padding:130px 0 80px;background:radial-gradient(circle at 75% 28%,rgba(201,151,63,.14),transparent 26rem),radial-gradient(circle at 15% 75%,rgba(100,25,111,.24),transparent 30rem),#080308}
  .orb{position:absolute;z-index:-1;right:-140px;top:120px;width:460px;height:460px;border:1px solid rgba(225,189,106,.14);border-radius:50%}
  .error-shell{max-width:820px;text-align:center}
  img{display:block;width:190px;height:auto;margin:0 auto 24px}
  .eyebrow{justify-content:center}
  h1{margin:0;color:var(--ivory);font:600 clamp(3rem,7vw,6rem)/.92 'Cormorant Garamond',Georgia,serif;letter-spacing:-.04em}
  .error-shell>p:not(.eyebrow){max-width:650px;margin:26px auto 0;color:#b9a9b7}
  .actions{display:flex;justify-content:center;flex-wrap:wrap;gap:10px;margin-top:34px}
  .quick{display:flex;justify-content:center;flex-wrap:wrap;gap:8px 20px;margin-top:54px;border-top:1px solid rgba(225,189,106,.12);padding-top:24px}
  .quick a{color:#a998a8;font-size:.8rem}.quick a:hover{color:var(--gold-bright)}
</style>
