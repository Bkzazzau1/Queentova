import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getItem, type Program } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const program = await getItem<Program>(fetch, `programs/${params.slug}/`);
  if (!program) error(404, 'Program not found');
  return { program };
};
