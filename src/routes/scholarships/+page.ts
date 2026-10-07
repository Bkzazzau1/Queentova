import type { PageLoad } from './$types';
import { getCollection, type Scholarship } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  scholarships: await getCollection<Scholarship>(fetch, 'scholarships/?ordering=-opens_at')
});
