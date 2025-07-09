# Apexive Hackaton Odoo


## What you need to code with AI

1. claude.ai account with claude code ( `npm install -g @anthropic-ai/claude-code`)
2. claudesync (`pip install claudesync`)

## Blogs and videos you should see before the hackaton

1. https://apexive.com/post/the-future-of-software
2. https://www.youtube.com/watch?v=LCEmiRjPEtQ
3. https://www.youtube.com/watch?v=6eBSHbLKuN0
4. https://apexive.com/post/apexive-development-philosophy

## Getting Started with development environment

1. Clone this repository:
   ```bash
   git clone <repository-url>
   cd apexive-hackaton-odoo
   ```

2. Build the project:
   ```bash
   make
   ```
   This command will:
   - Build the Docker images for the Odoo application
   - Install all necessary dependencies
   - Prepare the environment for running the application

3. Start the database:
   ```bash
   docker compose up -d db
   ```

4. Run the project:
   ```bash
   make run
   ```
   
5. Login to Odoo `http://127.0.0.1:8069/` user: `admin` password `admin`
