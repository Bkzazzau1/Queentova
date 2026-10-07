<script lang="ts">
  import type { GalleryItem } from '$lib/api/content';

  let { items, programTitle }: { items: GalleryItem[]; programTitle: string } = $props();

  const photos = $derived(items.filter((item) => item.media_type === 'image' && item.image));
  const videos = $derived(items.filter((item) => item.media_type === 'video' && item.video_url));

  let dialog = $state<HTMLDialogElement>();
  let current = $state(0);

  function open(index: number) {
    current = index;
    dialog?.showModal();
  }

  function step(delta: number) {
    current = (current + delta + photos.length) % photos.length;
  }

  function onKeydown(event: KeyboardEvent) {
    if (event.key === 'ArrowRight') step(1);
    if (event.key === 'ArrowLeft') step(-1);
  }

  function formatDate(value: string | null) {
    return value ? new Intl.DateTimeFormat('en', { dateStyle: 'medium' }).format(new Date(value)) : '';
  }
</script>

<section class="program-gallery">
  <div class="container">
    <div class="head">
      <div>
        <p class="eyebrow">Gallery</p>
        <h2>Our work in {programTitle}.</h2>
      </div>
      {#if photos.length || videos.length}
        <span class="count">{photos.length + videos.length} {photos.length + videos.length === 1 ? 'item' : 'items'}</span>
      {/if}
    </div>

    {#if photos.length || videos.length}
      <div class="grid">
        {#each photos as item, i (item.slug)}
          <button type="button" class="tile" class:feature={i === 0 && photos.length > 2} onclick={() => open(i)}>
            <img src={item.image} alt={item.alt_text || item.title} loading="lazy" />
            <span class="tile-copy">
              <strong>{item.title}</strong>
              {#if item.event_date}<small>{formatDate(item.event_date)}</small>{/if}
            </span>
          </button>
        {/each}

        {#each videos as item (item.slug)}
          <a class="tile video" href={item.video_url} target="_blank" rel="noreferrer">
            {#if item.image}<img src={item.image} alt={item.alt_text || item.title} loading="lazy" />{/if}
            <span class="play" aria-hidden="true">▶</span>
            <span class="tile-copy">
              <strong>{item.title}</strong>
              <small>Watch video ↗</small>
            </span>
          </a>
        {/each}
      </div>
    {:else}
      <div class="empty">
        <span aria-hidden="true">✦</span>
        <p>Photographs from this program will be shared here soon.</p>
      </div>
    {/if}
  </div>
</section>

{#if photos.length}
  <dialog bind:this={dialog} onkeydown={onKeydown} onclick={(e) => e.target === dialog && dialog?.close()} aria-label="Program photo viewer">
    {#if photos[current]}
      <figure>
        <img src={photos[current].image} alt={photos[current].alt_text || photos[current].title} />
        <figcaption>
          <strong>{photos[current].title}</strong>
          {#if photos[current].caption}<span>{photos[current].caption}</span>{/if}
          <small>{current + 1} / {photos.length}{photos[current].event_date ? ` · ${formatDate(photos[current].event_date)}` : ''}</small>
        </figcaption>
      </figure>
    {/if}
    <button type="button" class="close" aria-label="Close" onclick={() => dialog?.close()}>×</button>
    {#if photos.length > 1}
      <button type="button" class="nav prev" aria-label="Previous photo" onclick={() => step(-1)}>‹</button>
      <button type="button" class="nav next" aria-label="Next photo" onclick={() => step(1)}>›</button>
    {/if}
  </dialog>
{/if}

<style>
  .program-gallery { padding: 96px 0 110px; background: #fff; color: #2b1827; }
  .head { display: flex; align-items: end; justify-content: space-between; gap: 32px; }
  .head h2 { margin: 0; color: #2b1827; font: 600 clamp(2.4rem, 5vw, 3.8rem)/1 'Cormorant Garamond', Georgia, serif; }
  .count { color: #9a6d2b; font-size: .78rem; font-weight: 700; letter-spacing: .06em; text-transform: uppercase; }

  .grid { display: grid; grid-template-columns: repeat(3, 1fr); grid-auto-rows: 240px; gap: 14px; margin-top: 42px; }
  .tile { position: relative; overflow: hidden; display: block; border: 0; border-radius: 22px; padding: 0; background: linear-gradient(145deg, #4b1551, #150817); cursor: pointer; text-align: left; }
  .tile.feature { grid-column: span 2; grid-row: span 2; }
  .tile img { width: 100%; height: 100%; object-fit: cover; object-position: 50% 22%; transition: transform .5s ease; }
  .tile::after { position: absolute; inset: 0; background: linear-gradient(0deg, rgba(10, 4, 10, .78), transparent 55%); content: ''; }
  .tile:hover img, .tile:focus-visible img { transform: scale(1.04); }
  .tile-copy { position: absolute; z-index: 1; right: 18px; bottom: 16px; left: 18px; display: grid; gap: 3px; }
  .tile-copy strong { color: var(--champagne); font: 600 1.35rem/1.05 'Cormorant Garamond', Georgia, serif; }
  .tile-copy small { color: #d9c9d6; font-size: .74rem; }
  .play { position: absolute; z-index: 1; top: 50%; left: 50%; display: grid; width: 58px; height: 58px; place-items: center; border: 1px solid rgba(225, 189, 106, .6); border-radius: 50%; background: rgba(10, 4, 10, .55); color: var(--gold-bright); transform: translate(-50%, -60%); }

  .empty { display: flex; align-items: center; gap: 16px; margin-top: 36px; border: 1px dashed rgba(139, 98, 35, .3); border-radius: 22px; padding: 28px; background: #fffaf2; color: #6e5c69; }
  .empty span { color: #b08433; font-size: 1.4rem; }
  .empty p { margin: 0; }

  dialog { width: min(1100px, 94vw); max-height: 94vh; border: 0; padding: 0; background: transparent; overflow: visible; }
  dialog::backdrop { background: rgba(8, 3, 8, .9); }
  figure { margin: 0; display: grid; gap: 14px; }
  figure img { width: 100%; max-height: 78vh; object-fit: contain; border-radius: 14px; }
  figcaption { display: grid; gap: 4px; color: #e9dce6; text-align: center; }
  figcaption strong { color: var(--champagne); font: 600 1.5rem/1.1 'Cormorant Garamond', Georgia, serif; }
  figcaption small { color: #a998a8; }
  .close, .nav { position: absolute; display: grid; width: 46px; height: 46px; place-items: center; border: 1px solid rgba(225, 189, 106, .4); border-radius: 50%; background: rgba(10, 4, 10, .7); color: var(--gold-bright); font-size: 1.6rem; cursor: pointer; }
  .close { top: -10px; right: -10px; }
  .nav { top: 40%; }
  .prev { left: -62px; }
  .next { right: -62px; }

  @media (max-width: 860px) {
    .grid { grid-template-columns: 1fr 1fr; grid-auto-rows: 200px; }
    .prev { left: 6px; }
    .next { right: 6px; }
    .close { top: 6px; right: 6px; }
  }
  @media (max-width: 520px) {
    .head { flex-direction: column; align-items: flex-start; gap: 10px; }
    .grid { grid-template-columns: 1fr; }
    .tile.feature { grid-column: span 1; grid-row: span 1; }
  }
</style>
