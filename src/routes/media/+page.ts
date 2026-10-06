import type { PageLoad } from './$types';
import { getCollection, type ResourceItem, type Story } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  stories: await getCollection<Story>(fetch, 'stories/?ordering=-event_date'),
  resources: await getCollection<ResourceItem>(fetch, 'resources/?ordering=display_order')
});
