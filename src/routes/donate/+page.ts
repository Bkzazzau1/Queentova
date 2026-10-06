import type { PageLoad } from './$types';
import { getCollection, type Campaign } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  campaigns: await getCollection<Campaign>(fetch, 'campaigns/?ordering=display_order')
});
