import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getItem, type FounderMediaItem } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const item = await getItem<FounderMediaItem>(fetch, `founder-media/${params.slug}/`);
  if (!item) error(404, 'Founder media record not found');
  return { item };
};
