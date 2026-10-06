import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import { getItem, type EventItem } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const event = await getItem<EventItem>(fetch, `events/${params.slug}/`);
  if (!event) error(404, 'Event not found');
  return { event };
};
