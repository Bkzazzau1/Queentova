import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getItem, type ImpactStory } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const story = await getItem<ImpactStory>(fetch, `impact-stories/${params.slug}/`);
  if (!story) error(404, 'Impact story not found');
  return { story };
};
