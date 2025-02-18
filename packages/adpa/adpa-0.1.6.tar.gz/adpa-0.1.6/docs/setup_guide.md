# ADPA Setup Guide

Version 0.7.0

## Prerequisites

- Python 3.8+
- PostgreSQL 13+
- Git

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/ADPA.git
cd ADPA
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Set up environment variables:
Create a `.env` file in the root directory with:
```env
POSTGRES_URI=postgresql://username:password@localhost:5432/adpa
OPENAI_API_KEY=your_openai_key
GEMINI_API_KEY=your_gemini_key
GROQ_API_KEY=your_groq_key
```

## Step-by-Step Setup

### 1. Clone the Repository

```bash
# Clone ADPA repository
git clone https://github.com/achimdehnert/ADPA.git
cd ADPA

# If you have a specific branch
git checkout your-branch-name
```

### 2. Python Environment Setup

```bash
# Create a virtual environment
python -m venv .venv

# Activate the virtual environment
# On Windows:
.venv\Scripts\activate
# On Unix or MacOS:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Database Setup

#### Option 1: Local PostgreSQL

```bash
# Install PostgreSQL (if not already installed)
# On Windows: Download from https://www.postgresql.org/download/windows/
# On Ubuntu:
sudo apt-get update
sudo apt-get install postgresql postgresql-contrib

# Create a new database
createdb adpa_db  # Or your preferred database name

# Set environment variables
export POSTGRES_HOST=localhost
export POSTGRES_PORT=5432
export POSTGRES_USER=your_username
export POSTGRES_PASSWORD=your_password
export POSTGRES_DATABASE=adpa_db
export POSTGRES_URI=postgresql://your_username:your_password@localhost:5432/adpa_db
```

#### Option 2: Remote PostgreSQL (e.g., AWS RDS)

```bash
# Set environment variables for your remote database
export POSTGRES_HOST=your-host.region.rds.amazonaws.com
export POSTGRES_PORT=5432
export POSTGRES_USER=your_username
export POSTGRES_PASSWORD=your_password
export POSTGRES_DATABASE=your_database
export POSTGRES_URI=postgresql://your_username:your_password@your-host.region.rds.amazonaws.com:5432/your_database
```

### 4. Initialize Database

```bash
# Create database schema
python scripts/create_schema.py

# Seed initial data
python scripts/seed_data.py

# Verify setup
python scripts/test_db.py
python scripts/test_repositories.py
```

### 5. API Keys Setup

Create a `.env` file in the project root:

```bash
# Required API Keys
OPENAI_API_KEY=your_openai_key
ANTHROPIC_API_KEY=your_anthropic_key
AZURE_API_KEY=your_azure_key
GOOGLE_API_KEY=your_google_key
TAVILY_API_KEY=your_tavily_key
YOUTUBE_API_KEY=your_youtube_key
NEWS_API_KEY=your_news_key

# Database Configuration
POSTGRES_HOST=your_host
POSTGRES_PORT=5432
POSTGRES_USER=your_username
POSTGRES_PASSWORD=your_password
POSTGRES_DATABASE=your_database
POSTGRES_URI=postgresql://user:password@host:port/database
```

### 6. Start the Application

```bash
# Start the Streamlit app
streamlit run streamlit_app/Home.py
```

## Database Setup

### PostgreSQL Installation
1. Install PostgreSQL 14 or higher
2. Create ADPA database
3. Configure connection settings in `.env`

### AI Components Setup
1. Install required packages:
```bash
pip install psycopg3 numpy
```

2. Configure environment:
```env
POSTGRES_URI=postgresql://user:password@localhost:5432/adpa
```

3. Initialize components:
```python
# Initialize repositories
team_repo = TeamRepository()
agent_repo = AgentRepository()
task_repo = TaskRepository()

# Initialize monitoring
dashboard = MonitoringDashboard()

# Initialize query optimizer
optimizer = QueryOptimizer()
```

### Monitoring Setup
1. Configure system metrics collection
2. Set up alert thresholds
3. Configure dashboard access

## Directory Structure

```
ADPA/
├── adpa/                   # Main package directory
│   ├── agents/            # Agent implementations
│   ├── database/          # Database models and repositories
│   ├── research/          # Research capabilities
│   └── utils/             # Utility functions
├── docs/                  # Documentation
├── scripts/               # Utility scripts
├── streamlit_app/         # Streamlit interface
└── tests/                 # Test suite
```

## Common Issues

### Database Connection Issues

1. **Connection Refused**
   - Check if PostgreSQL is running
   - Verify port number
   - Check firewall settings

2. **Authentication Failed**
   - Verify username and password
   - Check database permissions

3. **Database Not Found**
   - Ensure database exists
   - Check database name in connection string

### API Key Issues

1. **Invalid API Key**
   - Verify key format
   - Check if key is active
   - Ensure key has required permissions

2. **Rate Limiting**
   - Implement retry logic
   - Check API usage limits
   - Consider upgrading API plan

## Maintenance

### Database Maintenance

```bash
# Backup database
pg_dump -U your_username -d your_database > backup.sql

# Restore database
psql -U your_username -d your_database < backup.sql

# Reset database
python scripts/create_schema.py --reset
python scripts/seed_data.py
```

### Environment Updates

```bash
# Update dependencies
pip install -r requirements.txt --upgrade

# Update database schema
python scripts/migrate_to_postgres.py
```

## Next Steps

1. Read the [Session Management](session.md) guide
2. Check the [API Documentation](api.md)
3. Review the [Architecture Overview](architecture.md)
4. Follow the [Development Guide](development.md)

## Search Tools Configuration

ADPA uses several external APIs to provide comprehensive search functionality. You'll need to set up API keys for the services you want to use:

1. **Tavily API Key** (Web Search)
   - Sign up at [Tavily](https://tavily.com)
   - Get your API key from the dashboard
   - Set environment variable: `TAVILY_API_KEY`

2. **YouTube API Key** (Video Search)
   - Go to [Google Cloud Console](https://console.cloud.google.com)
   - Create a project and enable YouTube Data API
   - Create credentials and get your API key
   - Set environment variable: `YOUTUBE_API_KEY`

3. **News API Key** (News Search)
   - Sign up at [News API](https://newsapi.org)
   - Get your API key
   - Set environment variable: `NEWS_API_KEY`

Note: arXiv search doesn't require an API key.

### Setting Environment Variables

#### Windows
```powershell
setx TAVILY_API_KEY "your_key_here"
setx YOUTUBE_API_KEY "your_key_here"
setx NEWS_API_KEY "your_key_here"
```

#### Linux/Mac
```bash
export TAVILY_API_KEY="your_key_here"
export YOUTUBE_API_KEY="your_key_here"
export NEWS_API_KEY="your_key_here"
```

Or add to your `.bashrc` or `.zshrc`:
```bash
# ADPA API Keys
export TAVILY_API_KEY="your_key_here"
export YOUTUBE_API_KEY="your_key_here"
export NEWS_API_KEY="your_key_here"
```

## Support

For issues and questions:
1. Check the [documentation](docs/)
2. Search existing GitHub issues
3. Create a new issue if needed
