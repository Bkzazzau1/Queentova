import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getCollection, getItem, type ActivityUpdate, type Program } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const [program, updates] = await Promise.all([
    getItem<Program>(fetch, `programs/${params.slug}/`),
    getCollection<ActivityUpdate>(
      fetch,
      `activity-updates/?program=${encodeURIComponent(params.slug)}&ordering=-occurred_at`
    )
  ]);

  if (!program) error(404, 'Program not found');
  return { program, updates };
};
