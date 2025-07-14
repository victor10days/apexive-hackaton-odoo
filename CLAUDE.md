# CLAUDE.md

This file provides comprehensive guidance to Claude Code (claude.ai/code) when working with the AI Business Process Optimizer for Odoo project.

## Project Overview

This is an Odoo 16.0 development environment for the Apexive Hackathon featuring the AI Business Process Optimizer. The project uses a containerized setup with Docker Compose and includes a complete Odoo installation with advanced AI integration capabilities for business process analysis and optimization.

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

# Start Qdrant vector database
docker compose up -d qdrant
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
- `extra-addons/ai_business_optimizer/` - Main AI Business Process Optimizer module
- `local-data/` - Local data directory for Odoo configuration and storage
- `docker/` - Docker configuration files

### Key Components
- **Odoo Version**: 16.0
- **Database**: PostgreSQL 17 with pgvector extension
- **Cache**: Redis 7
- **Vector DB**: Qdrant (for AI/ML features)
- **Python**: 3.10 virtual environment
- **AI Integration**: Anthropic Claude + OpenAI GPT + Fallback systems

### AI Business Process Optimizer Module
- **Models**: Process Analysis, Optimization Recommendations, Process Monitors, KPI Trackers
- **Views**: Dashboard, Analysis Forms, Kanban Boards, Reports
- **Controllers**: Web API endpoints for real-time data
- **Wizards**: Process optimization workflows
- **Security**: Role-based access control with audit trails

### Addon Management
- Custom addons are managed as git submodules in `extra-addons/.src/`
- Symlinks are created in `extra-addons/` pointing to the actual addon directories
- Use `make modules` to update submodules and recreate symlinks

## Environment Variables
Configure in `.env`:
- `ODOO_VERSION=16.0`
- `ODOO_DATABASE=apexive-hackaton`
- `ODOO_IMAGE_VERSION=1.0`
- `ODOO_IMAGE=odoo`

## Database Connection
- Host: localhost
- User: odoo
- Password: odoo
- Database: apexive-hackaton

## AI Integration Setup

### Required API Keys
Configure AI provider credentials in Odoo:
1. Navigate to **Settings → Technical → Parameters → System Parameters**
2. Add parameters:
   - `anthropic.api_key` - Your Anthropic Claude API key
   - `openai.api_key` - Your OpenAI API key

### AI Provider Configuration
The system supports multiple AI providers:
- **Anthropic Claude**: Primary AI provider for process analysis
- **OpenAI GPT**: Secondary AI provider for recommendations
- **Hybrid Mode**: Combines both providers for enhanced accuracy
- **Fallback System**: Rule-based analysis when AI services unavailable

## Development Workflow

### Standard Development Process
1. Start with `make` for initial setup
2. Use `docker compose up -d db` to start database
3. Run `make run` for development server
4. Access Odoo at http://127.0.0.1:8069/
5. Use `make upgrade` when adding/updating modules

### AI Module Development
1. **Install Base Dependencies**:
   ```bash
   # Install AI Business Process Optimizer
   # Apps → Search "AI Business Process Optimizer" → Install
   ```

2. **Configure AI Providers**:
   - Set up API keys in system parameters
   - Test AI connectivity in module settings
   - Configure fallback thresholds

3. **Development Testing**:
   ```bash
   # Run module tests
   python scripts/test_module.py
   
   # Test AI integration
   # Navigate to AI Business Optimizer → Configuration → Test AI Connection
   ```

## Docker Services
- `db`: PostgreSQL with pgvector extension
- `redis`: Redis cache for session management
- `odoo`: Odoo application server
- `qdrant`: Vector database for AI features and knowledge management

## Module Structure

### Core Models
- `ProcessAnalysis`: Business process analysis records
- `OptimizationRecommendation`: AI-generated optimization suggestions
- `ProcessMonitor`: Real-time process monitoring
- `KPITracker`: Key Performance Indicator tracking
- `OptimizationEngine`: AI processing engine

### View Components
- `Dashboard`: Real-time KPI dashboard with live updates
- `Analysis Forms`: Process analysis creation and results
- `Kanban Boards`: Recommendation management workflow
- `Reports`: Optimization impact reporting

### Security Implementation
- **Access Control**: Role-based permissions (User, Manager, Admin)
- **Data Isolation**: Company-level data separation
- **API Security**: Encrypted AI provider communications
- **Audit Trails**: Complete activity tracking

## Testing Procedures

### Module Validation
```bash
# Complete module test suite
python scripts/test_module.py

# Expected results:
# - Module Structure Test: PASSED
# - Python Syntax Test: PASSED
# - XML Validity Test: PASSED
# - Manifest File Test: PASSED
# - Model Structure Test: PASSED
```

### AI Integration Testing
1. **Test AI Connectivity**:
   - Navigate to AI Business Optimizer → Configuration
   - Run "Test AI Connection" wizard
   - Verify both Claude and OpenAI respond

2. **Process Analysis Testing**:
   - Create sample analysis with demo data
   - Verify AI-generated insights
   - Check recommendation generation

3. **Real-time Monitoring**:
   - Configure process monitors
   - Test threshold alerts
   - Verify KPI calculations

## Performance Optimization

### Development Environment
The main development workflow uses the local Python environment rather than containers for faster development cycles.

### AI Response Optimization
- **Caching**: AI responses cached for 24 hours
- **Batch Processing**: Multiple analyses processed together
- **Fallback Systems**: Rule-based analysis for high availability
- **Async Processing**: Background AI processing for large datasets

### Database Performance
- **Indexes**: Optimized for process analysis queries
- **Partitioning**: Large datasets partitioned by date
- **Caching**: Redis cache for frequently accessed data

## Debugging and Troubleshooting

### Common Issues
1. **AI Service Unavailable**:
   - Check API key configuration
   - Verify network connectivity
   - System falls back to rule-based analysis

2. **Module Installation Errors**:
   - Ensure all dependencies installed
   - Check module manifest syntax
   - Verify file permissions

3. **Performance Issues**:
   - Monitor database query performance
   - Check Redis cache utilization
   - Review AI response times

### Development Tools
- **Logging**: Comprehensive logging for AI operations
- **Debug Mode**: Detailed error reporting
- **Profiling**: Performance monitoring tools
- **Testing**: Automated test suite validation

## Production Deployment

### Pre-deployment Checklist
- [ ] All tests passing (5/5)
- [ ] AI providers configured
- [ ] Database optimized
- [ ] Security configured
- [ ] Backup procedures tested

### Performance Monitoring
- **KPI Tracking**: Real-time performance metrics
- **Error Monitoring**: AI service failure detection
- **Resource Usage**: Database and memory monitoring
- **User Analytics**: Feature usage tracking

## Documentation Standards

### Code Documentation
- **Models**: Comprehensive docstrings
- **Views**: Clear field descriptions
- **Controllers**: API endpoint documentation
- **Wizards**: User workflow guidance

### User Documentation
- **README.md**: Complete project overview
- **DEMO_GUIDE.md**: Demonstration instructions
- **PRESENTATION_GUIDE.md**: Presentation materials
- **TESTING_COMPLETE.md**: Validation results

The main development workflow uses the local Python environment rather than containers for faster development cycles.