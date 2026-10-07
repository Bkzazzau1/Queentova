import type { Program } from '$lib/api/content';

// Built-in program content, kept in step with backend/core/management/commands/seed_content.py.
// Used whenever the Foundation content service is unavailable (for example, a website-only deploy).
export const fallbackPrograms: (Program & { points: string[] })[] = [
  {
    title: 'Humanitarian Support',
    slug: 'humanitarian-support',
    summary:
      'Global outreach for the downtrodden and less privileged, including widows and widowers, indigent people, the homeless and families facing hardship.',
    body: [
      'Official Anambra State Government coverage describes Queen Tovah Cares Foundation International as a foundation "with global outreach that looks toward the plights of the downtrodden, the less privileged and is not politically motivated".',
      'Its humanitarian mission includes helping widows and widowers, indigent people and the homeless, including financial help to families facing hardship.',
      'The Founder has made clear that this philanthropy is not limited to Anambra or Amawbia, but extends to any part of Nigeria and the world.'
    ].join('\n\n'),
    icon: 'heart',
    featured: true,
    points: ['Widows, widowers and indigent families', 'Support for the homeless', 'Financial help to families']
  },
  {
    title: 'Education & Scholarships',
    slug: 'education-scholarships',
    summary:
      'Scholarship awards for indigent people, so that financial hardship does not become a permanent barrier to education.',
    body: [
      'The Foundation sponsors scholarship awards for indigent people, opening doors to learning for those whose potential should not be limited by circumstance.',
      "Education is part of the Foundation's wider investment in human capital: helping people build the knowledge and confidence to shape stronger futures for themselves and their communities."
    ].join('\n\n'),
    icon: 'book',
    featured: true,
    points: ['Scholarship awards', 'Support for indigent learners', 'Education-focused opportunity']
  },
  {
    title: 'Youth Empowerment & Sports',
    slug: 'youth-sports',
    summary:
      'Using sport to promote unity and engage young people, including sponsorship of the 2025 Amawbia August League football tournament in Anambra State.',
    body: [
      'The Foundation uses sport to bring young people together, encourage constructive engagement and strengthen community bonds.',
      'In 2025 it sponsored the Amawbia August League football tournament to promote sports and unite youths in Anambra State.'
    ].join('\n\n'),
    icon: 'spark',
    featured: true,
    points: ['2025 Amawbia August League', 'Youth engagement', 'Unity through sport']
  },
  {
    title: 'Human Capital & Community Development',
    slug: 'community-development',
    summary:
      'Recognised for work in human capital and community development, investing in people as the foundation of stronger communities.',
    body: [
      'The Foundation has been recognised for its work in human capital and community development, investing in people as the foundation of stronger communities.',
      'Its support is shaped around real local needs and guided by the Founder\'s principles: "It is good to be good" and "God is my strength".'
    ].join('\n\n'),
    icon: 'people',
    featured: true,
    points: ['Human-capital development', 'Community-led initiatives', 'Longer-term empowerment']
  }
];
