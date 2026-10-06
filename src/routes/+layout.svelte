<script lang="ts">
  import '../lib/styles/global.css';
  import SiteHeader from '$lib/components/SiteHeader.svelte';
  import SiteFooter from '$lib/components/SiteFooter.svelte';

  let { children, data } = $props();
</script>

<a class="skip-link" href="#main-content">Skip to main content</a>
<SiteHeader />
<main id="main-content" tabindex="-1">{@render children()}</main>
<SiteFooter profile={data.siteProfile} />
