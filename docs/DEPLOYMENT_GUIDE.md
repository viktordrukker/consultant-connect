# Hetzner Deployment Guide

This document explains how to deploy the Consultant Connect stack to a single Hetzner VM using GitHub Actions.

## Server setup
1. Install Docker and the compose plugin:
   ```bash
   sudo apt update
   sudo apt install docker.io docker-compose-plugin -y
   sudo usermod -aG docker $USER
   ```
   Log out and back in so your user can run Docker.
2. Clone the repository:
   ```bash
   sudo mkdir -p /opt/consultant-connect
   sudo chown $USER /opt/consultant-connect
   git clone <repository-url> /opt/consultant-connect
   ```
3. Add an `.env` file under `/opt/consultant-connect` if you need to override database credentials or other environment variables.
4. (Optional) Configure a reverse proxy such as Caddy or Nginx to expose ports 80/443 and route requests to the `frontend` (port 3000) and `backend` (port 8000) containers.

## GitHub secrets
Define the following repository secrets so the workflow can connect to the server:
- `SSH_HOST` – the server IP or hostname
- `SSH_USER` – the SSH username
- `SSH_KEY` – a private key with access to the server

## Manual deployment
You can deploy manually by running:
```bash
cd /opt/consultant-connect
docker compose up -d --build
```

## Automated deployment
A GitHub Actions workflow (`.github/workflows/deploy.yml`) is provided. Every push to `main` triggers the workflow, which:
1. Builds the frontend and checks the backend.
2. Connects to the server via SSH.
3. Pulls the latest code and runs `docker compose up -d --build`.

This keeps the Hetzner instance up to date with the latest version of the application.
