import type { Story } from '$lib/api/content';

// Built-in featured story, kept in step with the seeded story in
// backend/core/management/commands/seed_content.py. Used when the content service is unavailable.
export const fallbackStories: Story[] = [
  {
    title: 'Supporting youth unity through the Amawbia August League',
    slug: 'amawbia-august-league-2025',
    excerpt:
      'Queen Tovah Cares Foundation International sponsored the 2025 Amawbia August League football tournament as part of its support for sports, youth engagement and community unity in Anambra.',
    body: '',
    category: 'youth-sports',
    event_date: '2025-08-01',
    hero_image: null,
    hero_alt: '',
    featured: true,
    source_name: 'Independent Newspaper Nigeria',
    source_url: 'https://independent.ng/princess-udoka-menuba-kicks-poverty-out-with-amawbia-football-showdown/',
    published_at: null
  }
];
