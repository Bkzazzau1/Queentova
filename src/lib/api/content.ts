import { dev } from '$app/environment';
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
  program: string | null;
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
  // Local development falls back to the Django dev server. In production the site only calls a
  // backend when PUBLIC_API_BASE_URL is configured; otherwise reads fall back to built-in content
  // and forms report that they are unavailable, instead of calling localhost on visitors' devices.
  const url = env.PUBLIC_API_BASE_URL || (dev ? 'http://localhost:8000/api/v1' : '');
  if (!url) throw new Error('The Foundation content service is not configured.');
  return url.replace(/\/$/, '');
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
  type: 'program' | 'story' | 'campaign' | 'event' | 'scholarship' | 'resource' | 'faq' | 'impact-story' | 'founder-media' | 'activity-update' | 'partner';
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


export interface ScholarshipResultsSummary {
  applications_received: number;
  eligible: number;
  shortlisted: number;
  selected: number;
  max_awards: number | null;
}

export interface Scholarship {
  title: string;
  slug: string;
  summary: string;
  eligibility: string;
  application_instructions: string;
  required_documents: string;
  application_status: 'upcoming' | 'open' | 'closed';
  opens_at: string | null;
  closes_at: string | null;
  application_url: string;
  internal_applications_enabled: boolean;
  internal_applications_open: boolean;
  max_awards: number | null;
  public_results_released: boolean;
  public_results_note: string;
  results_summary: ScholarshipResultsSummary | null;
  published_at: string | null;
}

export interface ScholarshipApplicationReceipt {
  reference_code: string;
  status: string;
  status_label: string;
  scholarship: string;
  submitted_at: string;
}

export interface ScholarshipApplicationStatusResult {
  reference_code: string;
  scholarship: string;
  status: string;
  status_label: string;
  submitted_at: string;
  reviewed_at: string | null;
}

export async function submitScholarshipApplication(
  slug: string,
  formData: FormData
): Promise<ScholarshipApplicationReceipt> {
  const response = await fetch(
    `${baseUrl()}/scholarships/${encodeURIComponent(slug)}/apply/`,
    {
      method: 'POST',
      body: formData
    }
  );

  if (!response.ok) {
    const data = await response.json().catch(() => ({}));
    const message =
      data?.email?.[0] ||
      data?.consent_to_processing?.[0] ||
      data?.declaration_true?.[0] ||
      data?.non_field_errors?.[0] ||
      data?.detail ||
      'Unable to submit the scholarship application.';
    throw new Error(message);
  }

  return await response.json();
}

export async function checkScholarshipApplicationStatus(
  referenceCode: string,
  email: string
): Promise<ScholarshipApplicationStatusResult> {
  const response = await fetch(`${baseUrl()}/scholarship-application-status/`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({
      reference_code: referenceCode,
      email
    })
  });

  if (!response.ok) {
    const data = await response.json().catch(() => ({}));
    throw new Error(data?.detail || 'Application not found.');
  }

  return await response.json();
}

export interface Partner {
  title: string;
  slug: string;
  partner_type: 'corporate' | 'nonprofit' | 'government' | 'education' | 'media' | 'community' | 'professional' | 'other';
  relationship_status: 'strategic' | 'active' | 'project' | 'supporter' | 'completed';
  tagline: string;
  description: string;
  body: string;
  website: string;
  logo: string | null;
  hero_image: string | null;
  hero_alt: string;
  city: string;
  country: string;
  location: string;
  relationship_since: string | null;
  relationship_ended: string | null;
  verified_relationship: boolean;
  reference_url: string;
  featured: boolean;
  seo_title?: string;
  seo_description?: string;
  seo_keywords?: string;
  published_at: string | null;
}

export interface PartnerCollaboration {
  title: string;
  slug: string;
  summary: string;
  body: string;
  collaboration_status: 'planned' | 'active' | 'completed' | 'ongoing';
  partner_slug: string;
  partner_title: string;
  program_slug: string | null;
  program_title: string | null;
  campaign_slug: string | null;
  campaign_title: string | null;
  starts_at: string | null;
  ends_at: string | null;
  location_label: string;
  featured: boolean;
  verified_record: boolean;
  source_url: string;
  seo_title?: string;
  seo_description?: string;
  seo_keywords?: string;
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


export interface Announcement {
  title: string;
  slug: string;
  message: string;
  kind: 'info' | 'event' | 'opportunity' | 'appeal' | 'urgent';
  link_label: string;
  link_url: string;
  starts_at: string | null;
  ends_at: string | null;
  dismissible: boolean;
  priority: number;
  published_at: string | null;
}

export interface FAQItem {
  question: string;
  slug: string;
  answer: string;
  category: 'general' | 'support' | 'giving' | 'scholarship' | 'volunteer' | 'partnership';
  featured: boolean;
  display_order: number;
  published_at: string | null;
}


export interface HomepageSpotlight {
  eyebrow: string;
  title: string;
  slug: string;
  summary: string;
  image: string | null;
  image_alt: string;
  link_label: string;
  link_url: string;
  secondary_label: string;
  secondary_url: string;
  style: 'editorial' | 'impact' | 'campaign' | 'opportunity';
  starts_at: string | null;
  ends_at: string | null;
  priority: number;
  display_order: number;
  published_at: string | null;
}


export interface ImpactStory {
  title: string;
  slug: string;
  excerpt: string;
  body: string;
  program_area: 'humanitarian' | 'education' | 'youth' | 'community' | 'livelihood' | 'other';
  public_name: string;
  age_group: 'not-stated' | 'child' | 'youth' | 'adult' | 'older-adult';
  location_label: string;
  image: string | null;
  image_alt: string;
  quote: string;
  quote_attribution: string;
  featured: boolean;
  shared_with_consent: boolean;
  seo_title?: string;
  seo_description?: string;
  seo_keywords?: string;
  published_at: string | null;
}


export interface FounderMediaPhoto {
  image_url: string | null;
  alt_text: string;
  caption: string;
  credit: string;
  source_url: string;
  is_primary: boolean;
  display_order: number;
}

export interface FounderMediaItem {
  title: string;
  slug: string;
  kind: 'award' | 'achievement' | 'news' | 'interview' | 'publication' | 'community';
  summary: string;
  body: string;
  event_date: string | null;
  publication_date: string | null;
  source_name: string;
  source_url: string;
  source_domain: string;
  source_reference: string;
  award_title: string;
  awarding_body: string;
  location: string;
  featured: boolean;
  verified_source: boolean;
  photos: FounderMediaPhoto[];
  seo_title?: string;
  seo_description?: string;
  seo_keywords?: string;
  published_at: string | null;
}


export interface ActivityUpdateMedia {
  media_type: 'photo' | 'document';
  url: string | null;
  alt_text: string;
  caption: string;
  credit: string;
  source_url: string;
  featured: boolean;
  display_order: number;
}

export interface ActivityUpdate {
  title: string;
  slug: string;
  kind: 'field' | 'milestone' | 'delivery' | 'funding' | 'impact' | 'announcement';
  summary: string;
  body: string;
  occurred_at: string;
  location_label: string;
  featured: boolean;
  video_url: string;
  campaign_slug: string | null;
  campaign_title: string | null;
  program_slug: string | null;
  program_title: string | null;
  partners: Partner[];
  expenditure_amount: string | null;
  expenditure_currency: string;
  expenditure_note: string;
  expenditure_verified: boolean;
  output_value: string | null;
  output_unit: string;
  output_note: string;
  verification_note: string;
  source_reference: string;
  source_url: string;
  media: ActivityUpdateMedia[];
  seo_title?: string;
  seo_description?: string;
  seo_keywords?: string;
  published_at: string | null;
}
