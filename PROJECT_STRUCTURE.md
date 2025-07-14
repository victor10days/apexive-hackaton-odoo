# Project Structure

## Directory Organization

```
apexive-hackaton-odoo/
├── Project Documentation
│   ├── README.md                    # Main project documentation
│   ├── CLAUDE.md                    # Development guide
│   ├── PROJECT_STRUCTURE.md         # This file
│   └── docs/
│       ├── guides/
│       │   ├── DEMO_GUIDE.md        # Demo instructions
│       │   ├── PRESENTATION_STRATEGY.md # Presentation guide
│       │   └── TESTING_COMPLETE.md  # Testing report
│       └── assets/                  # Documentation assets
│
├── Development Environment
│   ├── Makefile                     # Build commands
│   ├── docker-compose.yml           # Container orchestration
│   ├── docker/                      # Docker configuration
│   │   └── requirements.txt         # Python dependencies
│   └── local-data/                  # Local configuration
│       └── odoo.conf               # Odoo configuration
│
├── AI Business Process Optimizer
│   └── extra-addons/
│       └── ai_business_optimizer/   # Main project module
│           ├── __manifest__.py      # Module definition
│           ├── models/              # Business logic
│           │   ├── process_analysis.py
│           │   ├── optimization_recommendation.py
│           │   ├── process_monitor.py
│           │   ├── optimization_engine.py
│           │   └── kpi_tracker.py
│           ├── views/               # User interface
│           │   ├── dashboard_views.xml
│           │   ├── process_analysis_views.xml
│           │   ├── optimization_recommendation_views.xml
│           │   ├── process_monitor_views.xml
│           │   └── menu_views.xml
│           ├── controllers/         # Web API endpoints
│           │   └── main.py
│           ├── wizards/            # User workflows
│           │   ├── process_optimizer_wizard.py
│           │   └── process_optimizer_wizard_views.xml
│           ├── data/               # Configuration data
│           │   ├── process_templates.xml
│           │   ├── optimization_rules.xml
│           │   └── demo_data.xml
│           ├── security/           # Access control
│           │   ├── ir.model.access.csv
│           │   └── security.xml
│           ├── static/             # Frontend assets
│           │   ├── src/
│           │   │   ├── js/dashboard.js
│           │   │   └── css/dashboard.css
│           │   └── description/
│           │       ├── icon.png
│           │       └── index.html
│           └── reports/            # Reporting views
│               └── optimization_report_views.xml
│
├── LLM Integration Modules
│   └── extra-addons/
│       ├── llm/                    # Base LLM functionality
│       ├── llm_anthropic/          # Claude AI integration
│       ├── llm_openai/             # OpenAI GPT integration
│       ├── llm_ollama/             # Local AI models
│       ├── llm_knowledge/          # Knowledge management
│       ├── llm_tools/              # AI tool integrations
│       └── [other LLM modules]/    # Extended AI capabilities
│
├── Odoo Core System
│   └── src/
│       └── odoo/                   # Official Odoo 16.0 source
│           ├── addons/             # Standard Odoo modules
│           ├── odoo/               # Core framework
│           ├── requirements.txt    # Core dependencies
│           └── [core files]        # Framework components
│
└── Development Tools
    └── scripts/
        └── test_module.py          # Module testing script
```

## Key Components

### Documentation Layer
- **README.md**: Project overview and setup instructions
- **CLAUDE.md**: Development guidelines and project context
- **docs/guides/**: Demo and presentation guides

### Main AI Project
- **ai_business_optimizer/**: Core module implementing AI-powered business optimization
- **MVC architecture**: Models, Views, Controllers separation
- **UI Components**: Dashboard, forms, reports
- **AI Integration**: Multi-provider AI analysis with fallback systems

### LLM Ecosystem
- **Modular AI System**: Separate modules for each AI provider
- **Extensible Architecture**: Framework for adding new AI capabilities
- **Knowledge Management**: Document processing and analysis

### Enterprise Foundation
- **Odoo 16.0 Core**: Enterprise ERP framework
- **Standard Modules**: Full ERP capabilities
- **Security**: Role-based access control and data isolation

## Organization Benefits

1. **Clear Purpose**: Each directory has a specific role
2. **Easy Navigation**: Logical hierarchy
3. **Separation of Concerns**: Clean module boundaries
4. **Scalable**: Supports adding new modules and features
5. **Maintainable**: Easy to locate and modify components

## Quick Start Commands

```bash
# Setup and run
make                    # Initial setup
docker compose up -d db # Start database
make run               # Start Odoo

# Access application
# URL: http://127.0.0.1:8069/
# Login: admin / admin
# Install: "AI Business Process Optimizer"

# Run tests
python scripts/test_module.py
```

## File Index

### Root Level Files
- `README.md` - Main project documentation
- `CLAUDE.md` - Development guidelines
- `PROJECT_STRUCTURE.md` - This organization guide
- `Makefile` - Build commands
- `docker-compose.yml` - Container orchestration

### Important Directories
- `docs/guides/` - Presentation materials
- `extra-addons/ai_business_optimizer/` - Main module
- `src/odoo/` - Core Odoo framework
- `scripts/` - Development and testing tools