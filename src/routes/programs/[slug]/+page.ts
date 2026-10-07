import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getCollection, getItem, type ActivityUpdate, type GalleryItem, type Program } from '$lib/api/content';
import { fallbackPrograms } from '$lib/content/programs';

export const load: PageLoad = async ({ fetch, params }) => {
  const slug = encodeURIComponent(params.slug);
  const [apiProgram, updates, gallery] = await Promise.all([
    getItem<Program>(fetch, `programs/${params.slug}/`),
    getCollection<ActivityUpdate>(fetch, `activity-updates/?program=${slug}&ordering=-occurred_at`),
    getCollection<GalleryItem>(fetch, `gallery/?program=${slug}&ordering=display_order`)
  ]);

  const program = apiProgram ?? fallbackPrograms.find((item) => item.slug === params.slug) ?? null;
  if (!program) error(404, 'Program not found');
  return { program, updates, gallery };
};
