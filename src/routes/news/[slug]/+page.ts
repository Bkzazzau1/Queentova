import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getItem, type Story } from '$lib/api/content';
import { fallbackStories } from '$lib/content/stories';

export const load: PageLoad = async ({ fetch, params }) => {
  const story =
    (await getItem<Story>(fetch, `stories/${params.slug}/`)) ??
    fallbackStories.find((item) => item.slug === params.slug) ??
    null;
  if (!story) error(404, 'Story not found');
  return { story };
};
