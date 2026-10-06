import type { LayoutLoad } from './$types';
import { getCollection, type SiteProfile } from '$lib/api/content';

export const load: LayoutLoad = async ({ fetch }) => {
  const profiles = await getCollection<SiteProfile>(fetch, 'site-profile/');
  return { siteProfile: profiles[0] ?? null };
};
