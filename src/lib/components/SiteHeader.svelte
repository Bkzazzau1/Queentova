<script lang="ts">
  import { onMount } from 'svelte';
  import type { Announcement } from '$lib/api/content';

  let { announcement = null }: { announcement?: Announcement | null } = $props();
  let open = $state(false);
  let announcementVisible = $state(true);

  onMount(() => {
    if (announcement?.dismissible) {
      announcementVisible = sessionStorage.getItem(`qt-announcement:${announcement.slug}`) !== 'dismissed';
    }
  });

  function dismissAnnouncement() {
    if (!announcement) return;
    announcementVisible = false;
    if (announcement.dismissible) {
      sessionStorage.setItem(`qt-announcement:${announcement.slug}`, 'dismissed');
    }
  }

  const links = [
    { label: 'About', href: '/about' },
    { label: 'Programs', href: '/programs' },
    { label: 'Causes', href: '/causes' },
    { label: 'Stories', href: '/news' },
    { label: 'Events', href: '/events' }
  ];

  const moreLinks = [
    { label: 'Founder', href: '/founder/jessie-ifeoma-udoka-menuba' },
    { label: 'Founder Recognition & Media', href: '/founder/media' },
    { label: 'Impact & Accountability', href: '/impact' },
    { label: 'Activity Journal', href: '/activity' },
    { label: 'Partners & Institutions', href: '/partners' },
    { label: 'Stories of Impact', href: '/impact-stories' },
    { label: 'Governance & Transparency', href: '/governance' },
    { label: 'Scholarships', href: '/scholarships' },
    { label: 'Request Support', href: '/request-support' },
    { label: 'Reports & Resources', href: '/resources' },
    { label: 'Press & Media', href: '/media' },
    { label: 'FAQ', href: '/faq' },
    { label: 'Gallery', href: '/gallery' },
    { label: 'Get Involved', href: '/get-involved' },
    { label: 'Contact', href: '/contact' }
  ];
</script>

<header class="site-header">
  {#if announcement && announcementVisible}
    <div class="announcement" class:urgent={announcement.kind === 'urgent'} class:appeal={announcement.kind === 'appeal'}>
      <div class="container announcement-inner">
        <div class="announcement-copy">
          <span>{announcement.kind}</span>
          <strong>{announcement.title}</strong>
          <p>{announcement.message}</p>
        </div>
        <div class="announcement-actions">
          {#if announcement.link_url}
            <a href={announcement.link_url}>{announcement.link_label || 'Learn more'} ↗</a>
          {/if}
          {#if announcement.dismissible}
            <button type="button" aria-label="Dismiss announcement" onclick={dismissAnnouncement}>×</button>
          {/if}
        </div>
      </div>
    </div>
  {/if}

  <div class="container nav">
    <a class="brand" href="/" aria-label="Queen Tovah Cares Foundation International home">
      <img class="brand-logo" src="/brand/queen-tovah-crest.webp" alt="" width="260" height="196" />
      <span class="brand-copy">
        <strong>Queen Tovah</strong>
        <small>Cares Foundation International</small>
      </span>
    </a>

    <nav class:open aria-label="Primary navigation">
      {#each links as link}
        <a href={link.href} onclick={() => (open = false)}>{link.label}</a>
      {/each}

      <details class="more">
        <summary>More <span>⌄</span></summary>
        <div class="more-menu">
          {#each moreLinks as link}
            <a href={link.href} onclick={() => (open = false)}>{link.label}</a>
          {/each}
        </div>
      </details>

      <a class="search-link" href="/search" aria-label="Search the Foundation" onclick={() => (open = false)}>⌕</a>
      <a class="donate" href="/donate" onclick={() => (open = false)}>Support the mission</a>
    </nav>

    <div class="mobile-actions">
      <a class="mobile-search" href="/search" aria-label="Search">⌕</a>
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
  </div>
</header>

<style>
  .site-header {
    position: fixed;
    z-index: 40;
    inset: 0 0 auto;
    border-bottom: 1px solid rgba(225, 189, 106, 0.12);
    background: rgba(5, 2, 4, 0.76);
    backdrop-filter: blur(20px);
  }

  .announcement {
    border-bottom: 1px solid rgba(225, 189, 106, 0.15);
    background: linear-gradient(90deg, rgba(76,21,83,.94), rgba(31,8,33,.96));
  }

  .announcement.appeal {
    background: linear-gradient(90deg, rgba(89,47,18,.94), rgba(39,18,9,.96));
  }

  .announcement.urgent {
    background: linear-gradient(90deg, rgba(98,30,35,.96), rgba(45,12,17,.97));
  }

  .announcement-inner {
    min-height: 43px;
    display: flex;
    align-items: center;
    justify-content: space-between;
    gap: 18px;
    padding-block: 7px;
  }

  .announcement-copy {
    display: flex;
    min-width: 0;
    align-items: center;
    gap: 10px;
  }

  .announcement-copy > span {
    flex-shrink: 0;
    border: 1px solid rgba(225,189,106,.3);
    border-radius: 999px;
    padding: 3px 7px;
    color: var(--gold-bright);
    font-size: .58rem;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  .announcement-copy strong {
    flex-shrink: 0;
    color: var(--champagne);
    font-size: .78rem;
  }

  .announcement-copy p {
    overflow: hidden;
    margin: 0;
    color: #cbbdca;
    font-size: .76rem;
    text-overflow: ellipsis;
    white-space: nowrap;
  }

  .announcement-actions {
    display: flex;
    flex-shrink: 0;
    align-items: center;
    gap: 12px;
  }

  .announcement-actions a {
    color: var(--gold-bright);
    font-size: .72rem;
    font-weight: 700;
  }

  .announcement-actions button {
    display: grid;
    width: 28px;
    height: 28px;
    place-items: center;
    border-radius: 50%;
    background: rgba(255,255,255,.07);
    color: #d8ccd7;
    cursor: pointer;
    font-size: 1rem;
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
    width: auto;
    height: 52px;
    flex-shrink: 0;
    filter: drop-shadow(0 4px 12px rgba(201, 151, 63, 0.18));
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
    gap: 20px;
  }

  nav > a,
  summary {
    color: #d8ccd7;
    font-size: 0.84rem;
    font-weight: 600;
    transition: color 160ms ease;
  }

  nav > a:hover,
  summary:hover {
    color: var(--gold-bright);
  }

  .more {
    position: relative;
  }

  summary {
    display: flex;
    align-items: center;
    gap: 4px;
    list-style: none;
    cursor: pointer;
  }

  summary::-webkit-details-marker {
    display: none;
  }

  summary span {
    color: #8e7c8c;
    font-size: .72rem;
  }

  .more-menu {
    position: absolute;
    top: calc(100% + 22px);
    right: -18px;
    width: 235px;
    display: grid;
    gap: 2px;
    border: 1px solid rgba(225,189,106,.18);
    border-radius: 18px;
    padding: 10px;
    background: rgba(16,5,17,.98);
    box-shadow: 0 24px 65px rgba(0,0,0,.38);
  }

  .more-menu::before {
    position: absolute;
    top: -22px;
    right: 0;
    left: 0;
    height: 22px;
    content: '';
  }

  .more-menu a {
    border-radius: 10px;
    padding: 10px 11px;
    color: #d8ccd7;
    font-size: .82rem;
  }

  .more-menu a:hover {
    background: rgba(255,255,255,.05);
    color: var(--gold-bright);
  }

  .search-link,
  .mobile-search {
    display: grid;
    place-items: center;
    width: 38px;
    height: 38px;
    border: 1px solid rgba(225, 189, 106, 0.18);
    border-radius: 50%;
    font-size: 1.2rem;
  }

  .donate {
    border: 1px solid rgba(225, 189, 106, 0.35);
    border-radius: 999px;
    padding: 10px 16px;
    color: var(--gold-bright);
    white-space: nowrap;
  }

  .mobile-actions {
    display: none;
    align-items: center;
    gap: 8px;
  }

  .mobile-search {
    color: var(--champagne);
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

  @media (max-width: 1060px) {
    .announcement-copy strong {
      display: none;
    }

    .announcement-copy p {
      max-width: 58vw;
    }

    .mobile-actions {
      display: flex;
    }

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
      max-height: calc(100vh - 112px);
      overflow-y: auto;
      border: 1px solid rgba(225, 189, 106, 0.18);
      border-radius: 22px;
      padding: 12px;
      background: rgba(17, 5, 18, 0.98);
      box-shadow: var(--shadow);
    }

    nav.open {
      display: flex;
    }

    nav > a,
    summary {
      padding: 13px 14px;
    }

    nav .search-link {
      display: none;
    }

    .more-menu {
      position: static;
      width: auto;
      margin: 0 8px 8px;
      border-color: rgba(225,189,106,.1);
      background: rgba(255,255,255,.025);
      box-shadow: none;
    }

    .more-menu::before {
      display: none;
    }

    .donate {
      margin-top: 5px;
      text-align: center;
    }
  }

  @media (max-width: 480px) {
    .announcement-copy > span {
      display: none;
    }

    .announcement-copy p {
      max-width: 62vw;
    }

    .announcement-actions a {
      display: none;
    }

    .brand-copy small {
      display: none;
    }

    .brand-logo {
      height: 44px;
    }
  }
</style>
