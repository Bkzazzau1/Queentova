<script lang="ts">
  let {
    title,
    text = ''
  }: {
    title: string;
    text?: string;
  } = $props();

  let copied = $state(false);

  async function copyLink() {
    if (typeof window === 'undefined') return;
    try {
      await navigator.clipboard.writeText(window.location.href);
      copied = true;
      window.setTimeout(() => (copied = false), 1800);
    } catch {
      copied = false;
    }
  }

  async function share() {
    if (typeof window === 'undefined') return;

    if (navigator.share) {
      try {
        await navigator.share({
          title,
          text,
          url: window.location.href
        });
        return;
      } catch {
        return;
      }
    }

    await copyLink();
  }
</script>

<div class="share" aria-label="Share this page">
  <span>Share</span>
  <button type="button" onclick={share}>↗ Share</button>
  <button type="button" onclick={copyLink}>{copied ? '✓ Copied' : '⧉ Copy link'}</button>
</div>

<style>
  .share {
    display: flex;
    flex-wrap: wrap;
    align-items: center;
    gap: 8px;
    margin-top: 30px;
  }

  .share > span {
    margin-right: 3px;
    color: #9a8059;
    font-size: .68rem;
    font-weight: 800;
    letter-spacing: .08em;
    text-transform: uppercase;
  }

  button {
    border: 1px solid rgba(80,45,70,.13);
    border-radius: 999px;
    padding: 8px 12px;
    background: transparent;
    color: #745e6e;
    cursor: pointer;
    font-size: .76rem;
    font-weight: 700;
    transition: border-color .16s ease, color .16s ease, background .16s ease;
  }

  button:hover {
    border-color: rgba(166,112,37,.35);
    background: rgba(166,112,37,.05);
    color: #8e6020;
  }
</style>
