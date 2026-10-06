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


export interface Campaign {
  title: string;
  slug: string;
  summary: string;
  body: string;
  image: string | null;
  image_alt: string;
  goal_amount: string | null;
  current_amount: string;
  currency: string;
  starts_at: string | null;
  ends_at: string | null;
  featured: boolean;
  accepting_support: boolean;
  cta_label: string;
  progress_percent: number | null;
  seo_title?: string;
  seo_description?: string;
  seo_keywords?: string;
}

export interface EventItem {
  title: string;
  slug: string;
  summary: string;
  body: string;
  starts_at: string;
  ends_at: string | null;
  venue_name: string;
  address: string;
  city: string;
  country: string;
  online_url: string;
  registration_url: string;
  image: string | null;
  image_alt: string;
  featured: boolean;
  seo_title?: string;
  seo_description?: string;
  seo_keywords?: string;
}

export interface SiteProfile {
  slug: string;
  display_name: string;
  short_description: string;
  contact_email: string;
  phone: string;
  whatsapp: string;
  office_address: string;
  country: string;
  facebook_url: string;
  instagram_url: string;
  x_url: string;
  linkedin_url: string;
  youtube_url: string;
  donation_url: string;
  volunteer_enabled: boolean;
  newsletter_enabled: boolean;
}

export interface VolunteerPayload {
  name: string;
  email: string;
  phone: string;
  country: string;
  city: string;
  areas_of_interest: string;
  skills: string;
  availability: string;
  message: string;
}

export interface SearchResult {
  type: 'program' | 'story' | 'campaign' | 'event' | 'resource';
  title: string;
  excerpt: string;
  url: string;
}

export async function submitVolunteer(payload: VolunteerPayload): Promise<void> {
  const response = await fetch(`${baseUrl()}/volunteer/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  if (!response.ok) throw new Error('Unable to submit volunteer application.');
}

export async function subscribeNewsletter(email: string, name = ''): Promise<void> {
  const response = await fetch(`${baseUrl()}/newsletter/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ email, name })
  });
  if (!response.ok) throw new Error('Unable to subscribe.');
}

export async function searchSite(fetcher: Fetcher, query: string): Promise<SearchResult[]> {
  const value = query.trim();
  if (value.length < 2) return [];
  try {
    const response = await fetcher(`${baseUrl()}/search/?q=${encodeURIComponent(value)}`);
    if (!response.ok) return [];
    const data = await response.json();
    return data.results ?? [];
  } catch {
    return [];
  }
}


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

export interface Partner {
  title: string;
  slug: string;
  description: string;
  website: string;
  logo: string | null;
  published_at: string | null;
}


export interface ResourceItem {
  title: string;
  slug: string;
  category: 'annual-report' | 'impact-report' | 'policy' | 'press-kit' | 'publication';
  summary: string;
  year: number | null;
  file: string | null;
  external_url: string;
  thumbnail: string | null;
  seo_title?: string;
  seo_description?: string;
  seo_keywords?: string;
  published_at?: string | null;
}

export interface SupportRequestPayload {
  name: string;
  email: string;
  phone: string;
  country: string;
  city: string;
  assistance_type: 'general' | 'education' | 'family' | 'shelter' | 'livelihood' | 'other';
  request_summary: string;
  consent_to_contact: boolean;
}

export async function submitSupportRequest(payload: SupportRequestPayload): Promise<void> {
  const response = await fetch(`${baseUrl()}/request-support/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify(payload)
  });
  if (!response.ok) throw new Error('Unable to submit support request.');
}
