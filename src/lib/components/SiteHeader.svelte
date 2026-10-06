<script lang="ts">
  let open = false;

  const links = [
    { label: 'About', href: '/about' },
    { label: 'Founder', href: '/founder/jessie-ifeoma-udoka-menuba' },
    { label: 'Programs', href: '/programs' },
    { label: 'Impact', href: '/impact' },
    { label: 'Stories', href: '/news' },
    { label: 'Gallery', href: '/gallery' },
    { label: 'Contact', href: '/contact' }
  ];
</script>

<header class="site-header">
  <div class="container nav">
    <a class="brand" href="/" aria-label="Queen Tovah Cares Foundation International home">
      <img class="brand-logo" src="/brand/queen-tovah-logo.webp" alt="" />
      <span class="brand-copy">
        <strong>Queen Tovah</strong>
        <small>Cares Foundation International</small>
      </span>
    </a>

    <nav class:open aria-label="Primary navigation">
      {#each links as link}
        <a href={link.href} onclick={() => (open = false)}>{link.label}</a>
      {/each}
      <a class="donate" href="/donate" onclick={() => (open = false)}>Support the mission</a>
    </nav>

    <button
      class="menu"
      type="button"
      aria-label="Toggle navigation"
      aria-expanded={open}
      onclick={() => (open = !open)}
    >
      <span></span>
      <span></span>
    </button>
  </div>
</header>

<style>
  .site-header {
    position: fixed;
    z-index: 40;
    inset: 0 0 auto;
    border-bottom: 1px solid rgba(225, 189, 106, 0.12);
    background: rgba(5, 2, 4, 0.74);
    backdrop-filter: blur(18px);
  }

  .nav {
    display: flex;
    min-height: 84px;
    align-items: center;
    justify-content: space-between;
    gap: 28px;
  }

  .brand {
    display: inline-flex;
    align-items: center;
    gap: 12px;
    min-width: 0;
  }

  .brand-logo {
    width: 58px;
    height: 44px;
    border: 1px solid rgba(225, 189, 106, 0.28);
    border-radius: 12px;
    object-fit: cover;
    box-shadow: 0 8px 24px rgba(0, 0, 0, 0.24);
  }

  .brand-copy {
    display: grid;
    line-height: 1.08;
  }

  .brand-copy strong {
    font-family: 'Cormorant Garamond', Georgia, serif;
    color: var(--champagne);
    font-size: 1.2rem;
    letter-spacing: 0.01em;
  }

  .brand-copy small {
    margin-top: 3px;
    color: #b7a6b6;
    font-size: 0.64rem;
    letter-spacing: 0.08em;
    text-transform: uppercase;
  }

  nav {
    display: flex;
    align-items: center;
    gap: 24px;
  }

  nav > a {
    color: #d8ccd7;
    font-size: 0.88rem;
    font-weight: 600;
    transition: color 160ms ease;
  }

  nav > a:hover {
    color: var(--gold-bright);
  }

  .donate {
    border: 1px solid rgba(225, 189, 106, 0.35);
    border-radius: 999px;
    padding: 10px 16px;
    color: var(--gold-bright);
  }

  .menu {
    display: none;
    width: 46px;
    height: 46px;
    align-items: center;
    justify-content: center;
    flex-direction: column;
    gap: 7px;
    border: 1px solid rgba(225, 189, 106, 0.24);
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.04);
  }

  .menu span {
    width: 18px;
    height: 1px;
    background: var(--champagne);
  }

  @media (max-width: 860px) {
    .menu {
      display: flex;
    }

    nav {
      position: absolute;
      top: calc(100% + 8px);
      right: 14px;
      left: 14px;
      display: none;
      flex-direction: column;
      align-items: stretch;
      gap: 0;
      border: 1px solid rgba(225, 189, 106, 0.18);
      border-radius: 22px;
      padding: 12px;
      background: rgba(17, 5, 18, 0.97);
      box-shadow: var(--shadow);
    }

    nav.open {
      display: flex;
    }

    nav > a {
      padding: 13px 14px;
    }

    .donate {
      margin-top: 4px;
      text-align: center;
    }
  }

  @media (max-width: 480px) {
    .brand-copy small {
      display: none;
    }
  }
</style>
