import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getCollection, getItem, type ActivityUpdate, type GalleryItem, type Program } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const slug = encodeURIComponent(params.slug);
  const [program, updates, gallery] = await Promise.all([
    getItem<Program>(fetch, `programs/${params.slug}/`),
    getCollection<ActivityUpdate>(fetch, `activity-updates/?program=${slug}&ordering=-occurred_at`),
    getCollection<GalleryItem>(fetch, `gallery/?program=${slug}&ordering=display_order`)
  ]);

  if (!program) error(404, 'Program not found');
  return { program, updates, gallery };
};
