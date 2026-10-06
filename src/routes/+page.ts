import type { PageLoad } from './$types';
import { getCollection, type Program, type Story } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  programs: await getCollection<Program>(fetch, 'programs/?ordering=display_order'),
  stories: await getCollection<Story>(fetch, 'stories/?ordering=-event_date')
});
