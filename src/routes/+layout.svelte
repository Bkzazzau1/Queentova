<script lang="ts">
  import '../lib/styles/global.css';
  import SiteHeader from '$lib/components/SiteHeader.svelte';
  import SiteFooter from '$lib/components/SiteFooter.svelte';

  let { children } = $props();
</script>

<SiteHeader />
<main>{@render children()}</main>
<SiteFooter />
