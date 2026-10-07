<script lang="ts">
  // Shows only the crowned QT emblem from the single brand image by cropping it with CSS.
  let { class: className = '', label = '' }: { class?: string; label?: string } = $props();
</script>

<span
  class={`brand-crest ${className}`}
  role={label ? 'img' : undefined}
  aria-label={label || undefined}
  aria-hidden={label ? undefined : 'true'}
></span>

<style>
  .brand-crest {
    display: block;
    width: 100%;
    aspect-ratio: 742 / 662;
    background-image: url('/brand/queentova.png');
    background-repeat: no-repeat;
    /* Crest occupies x 414–1156, y 10–672 of the 1536×1024 artwork. */
    background-size: 207% auto;
    background-position: 52.14% 2.76%;
  }
</style>
