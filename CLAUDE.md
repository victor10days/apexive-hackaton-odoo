# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This is an Odoo 16.0 development environment for the Apexive Hackathon. The project uses a containerized setup with Docker Compose and includes a complete Odoo installation with custom addons support.

## Essential Commands

### Initial Setup
```bash
# Clone and setup the project
make
```
This command builds Docker images, installs dependencies, and prepares the environment.

### Database Management
```bash
# Start PostgreSQL database
docker compose up -d db

# Start Redis (if needed)
docker compose up -d redis
```

### Running Odoo
```bash
# Run Odoo in development mode (recommended)
make run
```
This starts Odoo with the development server at http://127.0.0.1:8069/
- Default login: admin/admin
- Uses local Python virtual environment
- Connects to localhost database

```bash
# Run Odoo in Docker container (alternative)
make up
```

### Development Commands
```bash
# Initialize development environment
make init-dev

# Upgrade all modules
make upgrade

# Build Docker image
make build

# Clean modules and submodules
make clean
```

## Architecture

### Directory Structure
- `src/odoo/` - Core Odoo source code (cloned from official repo)
- `extra-addons/` - Custom addons directory with symlinks to submodules
- `local-data/` - Local data directory for Odoo configuration and storage
- `docker/` - Docker configuration files

### Key Components
- **Odoo Version**: 16.0
- **Database**: PostgreSQL 17 with pgvector extension
- **Cache**: Redis 7
- **Vector DB**: Qdrant (for AI/ML features)
- **Python**: 3.10 virtual environment

### Addon Management
- Custom addons are managed as git submodules in `extra-addons/.src/`
- Symlinks are created in `extra-addons/` pointing to the actual addon directories
- Use `make modules` to update submodules and recreate symlinks

## Environment Variables
Configure in `.env`:
- `ODOO_VERSION=16.0`
- `ODOO_DATABASE=apexive-hackaton`
- `ODOO_IMAGE_VERSION=1.0`

## Database Connection
- Host: localhost
- User: odoo
- Password: odoo
- Database: apexive-hackaton

## Development Workflow
1. Start with `make` for initial setup
2. Use `docker compose up -d db` to start database
3. Run `make run` for development server
4. Access Odoo at http://127.0.0.1:8069/
5. Use `make upgrade` when adding/updating modules

## Docker Services
- `db`: PostgreSQL with pgvector
- `redis`: Redis cache
- `odoo`: Odoo application server
- `qdrant`: Vector database for AI features

The main development workflow uses the local Python environment rather than containers for faster development cycles.