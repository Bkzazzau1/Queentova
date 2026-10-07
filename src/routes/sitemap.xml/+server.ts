import { env } from '$env/dynamic/public';
import type { RequestHandler } from './$types';

const staticRoutes = [
  '/',
  '/about',
  '/founder/jessie-ifeoma-udoka-menuba',
  '/founder/media',
  '/activity',
  '/programs',
  '/causes',
  '/impact',
  '/impact-stories',
  '/governance',
  '/news',
  '/events',
  '/scholarships',
  '/request-support',
  '/resources',
  '/media',
  '/faq',
  '/gallery',
  '/get-involved',
  '/donate',
  '/contact'
];

function apiBase() {
  return (env.PUBLIC_API_BASE_URL || 'http://localhost:8000/api/v1').replace(/\/$/, '');
}

async function dynamicRoutes(fetcher: typeof fetch, endpoint: string, prefix: string) {
  try {
    const response = await fetcher(`${apiBase()}/${endpoint}/?page_size=100`);
    if (!response.ok) return [];
    const data = await response.json();
    const items = Array.isArray(data) ? data : (data.results ?? []);
    return items
      .filter((item: { slug?: string }) => Boolean(item.slug))
      .map((item: { slug: string }) => `${prefix}/${item.slug}`);
  } catch {
    return [];
  }
}

export const GET: RequestHandler = async ({ url, fetch }) => {
  const dynamic = (
    await Promise.all([
      dynamicRoutes(fetch, 'programs', '/programs'),
      dynamicRoutes(fetch, 'stories', '/news'),
      dynamicRoutes(fetch, 'impact-stories', '/impact-stories'),
      dynamicRoutes(fetch, 'founder-media', '/founder/media'),
      dynamicRoutes(fetch, 'activity-updates', '/activity'),
      dynamicRoutes(fetch, 'campaigns', '/causes'),
      dynamicRoutes(fetch, 'events', '/events'),
      dynamicRoutes(fetch, 'scholarships', '/scholarships'),
      dynamicRoutes(fetch, 'resources', '/resources')
    ])
  ).flat();

  const routes = [...new Set([...staticRoutes, ...dynamic])];
  const today = new Date().toISOString().slice(0, 10);

  const body = `<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
${routes
  .map(
    (route) => `  <url>
    <loc>${url.origin}${route}</loc>
    <lastmod>${today}</lastmod>
    <changefreq>${route === '/' ? 'weekly' : 'monthly'}</changefreq>
    <priority>${route === '/' ? '1.0' : route.startsWith('/founder/') ? '0.9' : '0.8'}</priority>
  </url>`
  )
  .join('\n')}
</urlset>`;

  return new Response(body, {
    headers: {
      'Content-Type': 'application/xml; charset=utf-8',
      'Cache-Control': 'public, max-age=3600'
    }
  });
};
