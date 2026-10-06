import type { PageLoad } from './$types';
import { getCollection, type ResourceItem } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  resources: await getCollection<ResourceItem>(fetch, 'resources/?ordering=display_order')
});
