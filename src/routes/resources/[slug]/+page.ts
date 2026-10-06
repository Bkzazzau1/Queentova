import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getItem, type ResourceItem } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const resource = await getItem<ResourceItem>(fetch, `resources/${params.slug}/`);
  if (!resource) error(404, 'Resource not found');
  return { resource };
};
