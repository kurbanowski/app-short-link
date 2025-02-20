# FastAPI Link Shortener

## Overview
This is a simple URL shortening service built using **FastAPI** and **Tortoise-ORM**, with PostgreSQL as the database. The API allows users to submit a URL, receive a shortened link, and be redirected when accessing the short URL.

## Features
- **Shorten URLs**: Generate short URLs for long links.
- **Customizable Length**: Specify the length of the short URL (between 6 and 20 characters).
- **Redirection Support**: Automatically redirects users when they visit a short URL.
- **Database Persistence**: Uses PostgreSQL to store URL mappings.
- **Swagger API Docs**: Interactive API documentation available at `/docs`.
- **Dockerized**: Run the entire service with `docker compose up`.

## Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/kurbanowski/app-short-link
cd app-short-link
```

### 2. Create an Environment File
Set up a `.env` file in the project root with the following content:
```ini
POSTGRES_DB=shortlink
POSTGRES_USER=user
POSTGRES_PASSWORD=password
POSTGRES_HOST=db
POSTGRES_PORT=5432
```

### 3. Build and Run the Project Using Docker
```bash
docker compose up --build
```
This will start the API and the PostgreSQL database.

### 4. Access the API
- **Swagger UI:** [http://localhost:8000/docs](http://localhost:8000/docs)
- **ReDoc UI:** [http://localhost:8000/redoc](http://localhost:8000/redoc)

## API Endpoints

### 1. Shorten a URL
**Endpoint:** `POST /new`

**Request Body:**
```json
{
  "original_url": "https://example.com"
}
```
**Query Parameter:**
- `length`: Optional (default `6`, min `6`, max `20`)

**Response:**
```json
{
  "original_url": "https://example.com",
  "short_url": "http://localhost:8000/abc123"
}
```

### 2. Redirect to Original URL
**Endpoint:** `GET /{short_url}`

If a valid short URL is provided, the API will return a **302 Redirect** to the original URL.


