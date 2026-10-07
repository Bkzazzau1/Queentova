import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getItem, type ActivityUpdate } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const update = await getItem<ActivityUpdate>(fetch, `activity-updates/${params.slug}/`);
  if (!update) error(404, 'Activity update not found');
  return { update };
};
