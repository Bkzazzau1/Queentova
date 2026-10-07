import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getCollection, getItem, type ActivityUpdate, type Campaign } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const [campaign, updates] = await Promise.all([
    getItem<Campaign>(fetch, `campaigns/${params.slug}/`),
    getCollection<ActivityUpdate>(
      fetch,
      `activity-updates/?campaign=${encodeURIComponent(params.slug)}&ordering=-occurred_at`
    )
  ]);

  if (!campaign) error(404, 'Cause not found');
  return { campaign, updates };
};
