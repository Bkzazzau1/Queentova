# Queen Tovah Cares Foundation International

Official public website for **Queen Tovah Cares Foundation International**.

## Architecture

### Public website
- SvelteKit
- Svelte 5
- TypeScript
- Responsive SEO-friendly public pages
- Typed content API integration
- Dynamic sitemap and robots.txt

### Foundation administration
- Django 5
- Django REST Framework
- PostgreSQL
- Django Admin
- Draft → Review → Published workflow
- Media uploads
- Contact enquiry inbox
- Published-content-only public API
- API throttling for public submissions

## Brand direction

The visual system is derived from the official Queen Tovah logo:

- Ink: `#050204`
- Deep plum: `#2B0D2F`
- Royal purple: `#48144D`
- Purple: `#64196F`
- Antique gold: `#8B6223`
- Gold: `#C9973F`
- Bright gold: `#E1BD6A`
- Champagne: `#F0DDAD`
- Ivory: `#FFFAF2`

The site is designed to feel premium, humanitarian, international and dignified rather than like a generic NGO template.

## Managed content

Foundation administrators can manage:

- Programs
- Stories / news
- Gallery images and video links
- Founder profile
- Founder achievements and awards
- Verified impact metrics
- Scholarships
- Partners
- Contact enquiries
- SEO title, description, keywords and Open Graph images

Only records with **Published** status are exposed through the public API.

## Local development

Copy the environment template:

```bash
cp .env.example .env
```

Start PostgreSQL:

```bash
docker compose up -d postgres
```

Set up the backend:

```bash
cd backend
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py seed_content
python manage.py createsuperuser
python manage.py runserver
```

In another terminal, run the SvelteKit website:

```bash
npm install
npm run dev
```

The default development API is:

```
http://localhost:8000/api/v1
```

The Django administration is:

```
http://localhost:8000/admin/
```

## Public API

- `GET /api/v1/programs/`
- `GET /api/v1/stories/`
- `GET /api/v1/gallery/`
- `GET /api/v1/founders/`
- `GET /api/v1/founder-achievements/`
- `GET /api/v1/impact/`
- `GET /api/v1/scholarships/`
- `GET /api/v1/partners/`
- `POST /api/v1/contact/`
- `GET /api/health/`

## CI

GitHub Actions verifies both sides of the platform:

- Svelte type checks
- Svelte production build
- Django system checks
- migration consistency
- migrations
- backend API tests

## Current priorities

1. Add a Foundation-approved founder portrait and official project photography.
2. Confirm the Foundation's official public email, phone number and office details.
3. Configure production PostgreSQL and persistent media/cloud storage.
4. Add verified impact records, stories and gallery items through the admin.
5. Connect approved donation/payment channels.
6. Deploy the SvelteKit frontend and Django API behind the production domain.

### Guiding principle

> It is good to be good.
