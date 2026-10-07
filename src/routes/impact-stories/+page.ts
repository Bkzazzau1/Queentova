import type { PageLoad } from './$types';
import { getCollection, type ImpactStory } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  stories: await getCollection<ImpactStory>(fetch, 'impact-stories/?ordering=display_order,-published_at')
});
