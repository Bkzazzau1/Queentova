import type { PageLoad } from './$types';
import { getCollection, type EventItem } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  events: await getCollection<EventItem>(fetch, 'events/?ordering=starts_at')
});
