import type { PageLoad } from './$types';
import {
  getCollection,
  getItem,
  type FounderAchievement,
  type FounderProfile
} from '$lib/api/content';

export const load: PageLoad = async ({ fetch }) => ({
  founder: await getItem<FounderProfile>(fetch, 'founders/jessie-ifeoma-udoka-menuba/'),
  achievements: await getCollection<FounderAchievement>(
    fetch,
    'founder-achievements/?ordering=-year'
  )
});
