import type { PageLoad } from './$types';
import { getCollection, type ImpactMetric } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  metrics: await getCollection<ImpactMetric>(fetch, 'impact/?ordering=display_order')
});
