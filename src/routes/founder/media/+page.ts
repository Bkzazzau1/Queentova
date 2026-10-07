import type { PageLoad } from './$types';
import { getCollection, type FounderMediaItem } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  media: await getCollection<FounderMediaItem>(
    fetch,
    'founder-media/?ordering=display_order,-event_date,-publication_date'
  )
});
