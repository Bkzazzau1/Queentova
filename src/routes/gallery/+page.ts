import type { PageLoad } from './$types';
import { getCollection, type GalleryItem } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  gallery: await getCollection<GalleryItem>(fetch, 'gallery/?ordering=display_order')
});
