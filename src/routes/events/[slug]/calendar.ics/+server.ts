import { env } from '$env/dynamic/public';
import { error } from '@sveltejs/kit';
import type { RequestHandler } from './$types';
import type { EventItem } from '$lib/api/content';

function apiBase() {
  return (env.PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1').replace(/\/$/, '');
}

function icsDate(value: string) {
  return new Date(value)
    .toISOString()
    .replace(/[-:]/g, '')
    .replace(/\.\d{3}Z$/, 'Z');
}

function escapeIcs(value: string) {
  return value
    .replace(/\\/g, '\\\\')
    .replace(/\n/g, '\\n')
    .replace(/,/g, '\\,')
    .replace(/;/g, '\\;');
}

export const GET: RequestHandler = async ({ fetch, params, url }) => {
  const response = await fetch(`${apiBase()}/events/${params.slug}/`);
  if (!response.ok) error(404, 'Event not found');

  const event = (await response.json()) as EventItem;
  const start = icsDate(event.starts_at);
  const end = event.ends_at ? icsDate(event.ends_at) : icsDate(new Date(new Date(event.starts_at).getTime() + 60 * 60 * 1000).toISOString());
  const location = [event.venue_name, event.address, event.city, event.country].filter(Boolean).join(', ');
  const eventUrl = `${url.origin}/events/${event.slug}`;

  const body = [
    'BEGIN:VCALENDAR',
    'VERSION:2.0',
    'PRODID:-//Queen Tovah Cares Foundation International//Events//EN',
    'CALSCALE:GREGORIAN',
    'METHOD:PUBLISH',
    'BEGIN:VEVENT',
    `UID:${escapeIcs(event.slug)}@${url.hostname}`,
    `DTSTAMP:${icsDate(new Date().toISOString())}`,
    `DTSTART:${start}`,
    `DTEND:${end}`,
    `SUMMARY:${escapeIcs(event.title)}`,
    `DESCRIPTION:${escapeIcs(event.summary)}`,
    ...(location ? [`LOCATION:${escapeIcs(location)}`] : []),
    `URL:${escapeIcs(eventUrl)}`,
    'END:VEVENT',
    'END:VCALENDAR',
    ''
  ].join('\r\n');

  return new Response(body, {
    headers: {
      'Content-Type': 'text/calendar; charset=utf-8',
      'Content-Disposition': `attachment; filename="${event.slug}.ics"`,
      'Cache-Control': 'public, max-age=900'
    }
  });
};
