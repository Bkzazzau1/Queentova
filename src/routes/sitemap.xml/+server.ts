import type { RequestHandler } from './$types';

const routes = [
  '/',
  '/about',
  '/founder/jessie-ifeoma-udoka-menuba',
  '/programs',
  '/impact',
  '/news',
  '/gallery',
  '/donate',
  '/contact'
];

export const GET: RequestHandler = ({ url }) => {
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
