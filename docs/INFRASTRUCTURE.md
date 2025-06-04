# Infrastructure Plan

This document outlines the low‑cost environments for development,
staging and production. The aim is to keep the footprint minimal
while allowing the team to iterate quickly.

## Development
- **Local**: Run services via Docker Compose. A container for the FastAPI backend, another for PostgreSQL, and one for the React/Vite dev server.
- **Database**: Local Postgres volume to persist data.
- **Secrets**: `.env` file with local credentials.

## Staging
- **Hosting**: AWS using the lowest tier that supports our stack.
- **Backend**: ECS Fargate or a small EC2 instance running the FastAPI container.
- **Database**: PostgreSQL RDS in the free tier, single availability zone.
- **Static Assets**: S3 bucket served via CloudFront.
- **CI/CD**: GitHub Actions builds Docker images and deploys to ECS on every push to the `main` branch.

## Production
- **Backend**: ECS Fargate with auto‑scaling rules. Start with minimal CPU/RAM and scale up as traffic grows.
- **Database**: PostgreSQL RDS with automated backups. Begin with the smallest instance class.
- **Caching**: Use AWS ElastiCache if performance demands it.
- **Monitoring**: CloudWatch metrics and alerts for API errors, latency and resource usage.
- **Cost Control**: Review AWS usage monthly and clean up unused resources.

This setup allows rapid iteration with minimal upfront cost and the option to scale as the platform gains traction.
