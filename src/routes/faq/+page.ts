import type { PageLoad } from './$types';
import { getCollection, type FAQItem } from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  faqs: await getCollection<FAQItem>(fetch, 'faqs/?ordering=display_order')
});
