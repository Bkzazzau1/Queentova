import type { PageLoad } from './$types';
import { getCollection, type ImpactMetric, type ImpactStory } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  metrics: await getCollection<ImpactMetric>(fetch, 'impact/?ordering=display_order'),
  stories: await getCollection<ImpactStory>(fetch, 'impact-stories/?ordering=display_order,-published_at')
});
