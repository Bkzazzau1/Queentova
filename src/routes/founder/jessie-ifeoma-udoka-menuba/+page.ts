import type { PageLoad } from './$types';
import {
  getCollection,
  getItem,
  type FounderAchievement,
  type FounderMediaItem,
  type FounderProfile
} from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  founder: await getItem<FounderProfile>(fetch, 'founders/jessie-ifeoma-udoka-menuba/'),
  achievements: await getCollection<FounderAchievement>(
    fetch,
    'founder-achievements/?ordering=-year'
  ),
  media: await getCollection<FounderMediaItem>(
    fetch,
    'founder-media/?ordering=display_order,-event_date,-publication_date'
  )
});
