import type { PageLoad } from './$types';
import { searchSite } from '$lib/api/content';

export const load: PageLoad = async ({ fetch, url }) => {
  const query = url.searchParams.get('q')?.trim() ?? '';
  return {
    query,
    results: query.length >= 2 ? await searchSite(fetch, query) : []
  };
};
