import { error } from '@sveltejs/kit';
import type { PageLoad } from './$types';
import {
  getCollection,
  getItem,
  type ActivityUpdate,
  type Partner,
  type PartnerCollaboration
} from '$lib/api/content';

export const load: PageLoad = async ({ fetch, params }) => {
  const [partner, collaborations, activity] = await Promise.all([
    getItem<Partner>(fetch, `partners/${params.slug}/`),
    getCollection<PartnerCollaboration>(
      fetch,
      `partner-collaborations/?partner=${encodeURIComponent(params.slug)}&ordering=display_order,-starts_at`
    ),
    getCollection<ActivityUpdate>(
      fetch,
      `activity-updates/?partner=${encodeURIComponent(params.slug)}&ordering=-occurred_at`
    )
  ]);

  if (!partner) error(404, 'Partner not found');
  return { partner, collaborations, activity };
};
