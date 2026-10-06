import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getItem } from '$lib/api/content';
import type { Scholarship } from '../+page';

export const load: PageLoad = async ({ fetch, params }) => {
  const scholarship = await getItem<Scholarship>(fetch, `scholarships/${params.slug}/`);
  if (!scholarship) error(404, 'Scholarship not found');
  return { scholarship };
};
