<script lang="ts">
  import { page } from '$app/state';
  import '../lib/styles/global.css';
  import SiteHeader from '$lib/components/SiteHeader.svelte';
  import SiteFooter from '$lib/components/SiteFooter.svelte';

  let { children, data } = $props();

  const canonicalUrl = $derived(`${page.url.origin}${page.url.pathname}`);
  const sameAs = $derived(
    [
      data.siteProfile?.facebook_url,
      data.siteProfile?.instagram_url,
      data.siteProfile?.x_url,
      data.siteProfile?.linkedin_url,
      data.siteProfile?.youtube_url
    ].filter(Boolean)
  );

  const organizationSchema = $derived(
    JSON.stringify({
      '@context': 'https://schema.org',
      '@type': 'NGO',
      name: data.siteProfile?.display_name || 'Queen Tovah Cares Foundation International',
      url: page.url.origin,
      logo: `${page.url.origin}/brand/queentova.png`,
      description:
        data.siteProfile?.short_description ||
        'Queen Tovah Cares Foundation International advances humanitarian support, education, youth empowerment and community development.',
      ...(data.siteProfile?.contact_email
        ? { email: data.siteProfile.contact_email }
        : {}),
      ...(data.siteProfile?.phone ? { telephone: data.siteProfile.phone } : {}),
      ...(data.siteProfile?.office_address
        ? {
            address: {
              '@type': 'PostalAddress',
              streetAddress: data.siteProfile.office_address,
              addressCountry: data.siteProfile.country || undefined
            }
          }
        : {}),
      ...(sameAs.length ? { sameAs } : {})
    }).replace(/</g, '\\u003c')
  );
</script>

<svelte:head>
  <link rel="canonical" href={canonicalUrl} />
  <meta property="og:site_name" content="Queen Tovah Cares Foundation International" />
  <meta name="theme-color" content="#160917" />
  {@html `<script type="application/ld+json">${organizationSchema}</script>`}
</svelte:head>

<a class="skip-link" href="#main-content">Skip to main content</a>
<SiteHeader announcement={data.announcement} />
<main id="main-content" tabindex="-1">{@render children()}</main>
<SiteFooter profile={data.siteProfile} />
