import type { PageLoad } from './$types';
import { getCollection, type Partner } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  partners: await getCollection<Partner>(
    fetch,
    'partners/?ordering=display_order,relationship_since,title'
  )
});
