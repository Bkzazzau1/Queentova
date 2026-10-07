import type { PageLoad } from './$types';
import { getCollection, type ActivityUpdate } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  updates: await getCollection<ActivityUpdate>(
    fetch,
    'activity-updates/?ordering=-occurred_at,-published_at'
  )
});
