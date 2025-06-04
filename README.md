# Consultant Connect MVP

## Vision

A platform connecting expert seekers with consultants for advice and services. This MVP focuses on establishing the core connection mechanism.

## Technology Stack

* **Backend:** Python (FastAPI)
* **Frontend:** React (Vite)
* **Database:** PostgreSQL
* **Cloud Provider:** AWS (Targeting services like Fargate/Lambda, RDS, S3)
* **Repository:** GitHub (Public)

## Architecture
```mermaid
graph TD
    subgraph "User Browser"
        Frontend[React SPA]
    end

    subgraph "AWS Cloud"
        API[FastAPI Backend <br/> (e.g., Fargate/Lambda)]
        DB[(PostgreSQL RDS)]
        CDN[CloudFront]
        Assets[S3 Bucket]
    end

    Frontend -- HTTP Requests --> API
    API -- SQL Queries --> DB
    Frontend -- Loads Static Assets --> CDN
    CDN -- Serves Assets From --> Assets
```

## Getting Started

The project uses **Docker Compose** for a hassle-free local setup.

```bash
git clone <repo-url>
cd consultant-connect
docker compose up --build
```

This starts a FastAPI backend, a PostgreSQL database and a Vite dev server. The frontend is available at `http://localhost:3000` and the backend at `http://localhost:8000`. Environment variables can be configured in `.env.example`.

## Core MVP Features

* User Registration/Login (Seeker, Consultant)
* Basic Consultant Profile Management (Create/Edit/View)
* Seeker Discovery (List/Search Consultants, View Profiles)

Additional planning documents can be found in the [docs](docs/) directory, including user personas, customer journey maps and the detailed roadmap.
Detailed deployment instructions for Hetzner are in [docs/DEPLOYMENT_GUIDE.md](docs/DEPLOYMENT_GUIDE.md).
