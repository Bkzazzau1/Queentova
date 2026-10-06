import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getItem, type Campaign } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const campaign = await getItem<Campaign>(fetch, `campaigns/${params.slug}/`);
  if (!campaign) error(404, 'Cause not found');
  return { campaign };
};
