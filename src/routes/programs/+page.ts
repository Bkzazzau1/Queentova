import type { PageLoad } from './$types';
import { getCollection, type Program } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  programs: await getCollection<Program>(fetch, 'programs/?ordering=display_order')
});
