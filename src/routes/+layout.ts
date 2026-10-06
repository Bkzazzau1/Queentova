import type { LayoutLoad } from './$types';
import { getCollection, type Announcement, type SiteProfile } from '$lib/api/content';

export const load: LayoutLoad = async ({ fetch }) => {
  const [profiles, announcements] = await Promise.all([
    getCollection<SiteProfile>(fetch, 'site-profile/'),
    getCollection<Announcement>(fetch, 'announcements/?ordering=-priority')
  ]);

  return {
    siteProfile: profiles[0] ?? null,
    announcement: announcements[0] ?? null
  };
};
