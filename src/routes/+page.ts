import type { PageLoad } from './$types';
import {
  getCollection,
  type Campaign,
  type EventItem,
  type Partner,
  type Program,
  type Scholarship,
  type Story
} from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  programs: await getCollection<Program>(fetch, 'programs/?ordering=display_order'),
  stories: await getCollection<Story>(fetch, 'stories/?ordering=-event_date'),
  campaigns: await getCollection<Campaign>(fetch, 'campaigns/?ordering=display_order'),
  events: await getCollection<EventItem>(fetch, 'events/?ordering=starts_at'),
  scholarships: await getCollection<Scholarship>(fetch, 'scholarships/?ordering=-opens_at'),
  partners: await getCollection<Partner>(fetch, 'partners/?ordering=display_order')
});
