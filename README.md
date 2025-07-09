# Apexive Hackaton Odoo

## Getting Started

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
