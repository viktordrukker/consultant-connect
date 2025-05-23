# Consultant Connect MVP

## Vision

A platform connecting expert seekers with consultants for advice and services. This MVP focuses on establishing the core connection mechanism.

## Technology Stack

*   **Backend:** Python (FastAPI)
*   **Frontend:** React (Vite)
*   **Database:** PostgreSQL
*   **Cloud Provider:** AWS (Targeting services like Fargate/Lambda, RDS, S3)
*   **Repository:** GitHub (Public)

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

## Getting Started (Initial Placeholder)

*(Instructions on how to set up the development environment will be added here later)*

## Core MVP Features

*   User Registration/Login (Seeker, Consultant)
*   Basic Consultant Profile Management (Create/Edit/View)
*   Seeker Discovery (List/Search Consultants, View Profiles)
*   "Request Contact" functionality (Seeker expresses interest in a Consultant)
