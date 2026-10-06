import type { PageLoad } from './$types';
import { getCollection } from '$lib/api/content';

export interface Scholarship {
  title: string;
  slug: string;
  summary: string;
  eligibility: string;
  application_status: 'upcoming' | 'open' | 'closed';
  opens_at: string | null;
  closes_at: string | null;
  application_url: string;
  published_at: string | null;
}

export const load: PageLoad = async ({ fetch }) => ({
  scholarships: await getCollection<Scholarship>(fetch, 'scholarships/?ordering=-opens_at')
});
