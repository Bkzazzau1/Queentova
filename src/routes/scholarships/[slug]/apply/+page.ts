import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getItem, type Scholarship } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const scholarship = await getItem<Scholarship>(fetch, `scholarships/${params.slug}/`);
  if (!scholarship) error(404, 'Scholarship not found');
  return { scholarship };
};
