import { env } from '$env/dynamic/public';

type Fetcher = (input: RequestInfo | URL, init?: RequestInit) => Promise<Response>;

export interface Program {
  title: string;
  slug: string;
  summary: string;
  body: string;
  icon: string;
  featured: boolean;
  seo_title?: string;
  seo_description?: string;
  seo_keywords?: string;
  published_at?: string | null;
}

export interface Story {
  title: string;
  slug: string;
  excerpt: string;
  body: string;
  category: string;
  event_date: string | null;
  hero_image: string | null;
  hero_alt: string;
  featured: boolean;
  source_name: string;
  source_url: string;
  seo_title?: string;
  seo_description?: string;
  seo_keywords?: string;
  published_at?: string | null;
}

export interface GalleryItem {
  title: string;
  slug: string;
  media_type: 'image' | 'video';
  image: string | null;
  video_url: string;
  alt_text: string;
  caption: string;
  category: string;
  event_date: string | null;
}

export interface ImpactMetric {
  title: string;
  slug: string;
  value: string;
  unit: string;
  period: string;
  verification_note: string;
  source_reference: string;
}

export interface FounderProfile {
  title: string;
  slug: string;
  primary_name: string;
  public_record_name: string;
  maiden_name: string;
  headline: string;
  biography: string;
  motto: string;
  faith_line: string;
  portrait: string | null;
  portrait_alt: string;
  seo_title: string;
  seo_description: string;
}

export interface FounderAchievement {
  title: string;
  slug: string;
  year: number | null;
  description: string;
  source_name: string;
  source_url: string;
}

export interface ContactPayload {
  name: string;
  email: string;
  enquiry_type: 'general' | 'partnership' | 'humanitarian' | 'scholarship' | 'media';
  message: string;
}

function baseUrl() {
  return (env.PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1').replace(/\/$/, '');
}

export async function getCollection<T>(
  fetcher: Fetcher,
  path: string
): Promise<T[]> {
  try {
    const response = await fetcher(`${baseUrl()}/${path.replace(/^\//, '')}`);
    if (!response.ok) return [];
    const data = await response.json();
    return Array.isArray(data) ? data : (data.results ?? []);
  } catch {
    return [];
  }
}

export async function getItem<T>(
  fetcher: Fetcher,
  path: string
): Promise<T | null> {
  try {
    const response = await fetcher(`${baseUrl()}/${path.replace(/^\//, '')}`);
    if (!response.ok) return null;
    return await response.json();
  } catch {
    return null;
  }
}

export async function submitContact(payload: ContactPayload): Promise<void> {
  const response = await fetch(`${baseUrl()}/contact/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });

  if (!response.ok) {
    throw new Error('Unable to submit your message.');
  }
}
