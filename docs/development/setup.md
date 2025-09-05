# Development Setup Guide

This guide will help you set up the MGR API development environment on your local machine.

## Prerequisites

### Required Software

- **Ruby**: 3.0.0 or higher
- **Rails**: 7.0.0 or higher  
- **PostgreSQL**: 12.0 or higher
- **Redis**: 6.0 or higher (for Sidekiq)
- **Node.js**: 16.0 or higher (for asset compilation)
- **Git**: Latest version

### Optional Tools

- **Docker**: For containerized development
- **pgAdmin**: PostgreSQL administration
- **Redis CLI**: Redis debugging
- **Postman**: API testing

## Installation

### 1. Clone Repository

```bash
git clone https://github.com/your-org/mgr-api.git
cd mgr-api
```

### 2. Install Dependencies

```bash
# Install Ruby gems
bundle install

# Install Node.js packages
npm install
```

### 3. Database Setup

```bash
# Create databases
rails db:create

# Run migrations
rails db:migrate

# Seed development data
rails db:seed
```

### 4. Environment Configuration

Copy the example environment file and configure:

```bash
cp .env.example .env
```

Edit `.env` with your local settings:

```bash
# Database
DATABASE_URL=postgresql://username:password@localhost/mgr_api_development

# Redis
REDIS_URL=redis://localhost:6379/0

# AWS S3 (for file uploads)
AWS_ACCESS_KEY_ID=your_access_key
AWS_SECRET_ACCESS_KEY=your_secret_key
AWS_BUCKET_NAME=mgr-api-development
AWS_REGION=us-west-2

# Email (optional for development)
SMTP_HOST=localhost
SMTP_PORT=1025

# Application
SECRET_KEY_BASE=your_secret_key_base
RAILS_ENV=development
```

### 5. Start Services

#### Option A: Manual Start

```bash
# Terminal 1: Rails server
rails server

# Terminal 2: Sidekiq worker
bundle exec sidekiq

# Terminal 3: Redis (if not running as service)
redis-server
```

#### Option B: Using Foreman

```bash
# Install foreman
gem install foreman

# Start all services
foreman start
```

#### Option C: Docker Compose

```bash
# Build and start containers
docker-compose up --build

# Run migrations in container
docker-compose exec web rails db:migrate
```

## Development Workflow

### Running Tests

```bash
# Run all tests
bundle exec rspec

# Run specific test file
bundle exec rspec spec/commands/imports/process_spec.rb

# Run tests with coverage
COVERAGE=true bundle exec rspec

# Run tests in parallel
bundle exec parallel_rspec spec/
```

### Code Quality

```bash
# Run RuboCop linter
bundle exec rubocop

# Auto-fix RuboCop issues
bundle exec rubocop -a

# Run security audit
bundle exec brakeman

# Check for outdated gems
bundle outdated
```

### Database Operations

```bash
# Create migration
rails generate migration AddFieldToModel field:type

# Run migrations
rails db:migrate

# Rollback migration
rails db:rollback

# Reset database
rails db:reset

# Generate seed data
rails db:seed
```

### Console Access

```bash
# Rails console
rails console

# Sidekiq console
bundle exec sidekiq -e development

# Database console
rails dbconsole
```

## Project Structure

```
mgr-api/
├── app/
│   ├── commands/           # Business logic commands
│   │   ├── imports/        # Import-related commands
│   │   └── ...
│   ├── controllers/        # API controllers
│   ├── models/            # ActiveRecord models
│   ├── workers/           # Sidekiq background workers
│   └── serializers/       # JSON serializers
├── config/
│   ├── environments/      # Environment configurations
│   ├── initializers/      # Application initializers
│   └── routes.rb         # API routes
├── db/
│   ├── migrate/          # Database migrations
│   └── seeds.rb          # Seed data
├── docs/                 # Documentation
├── spec/                 # Test files
│   ├── commands/         # Command tests
│   ├── controllers/      # Controller tests
│   ├── models/          # Model tests
│   ├── workers/         # Worker tests
│   └── support/         # Test support files
└── lib/                 # Custom libraries
```

## Key Development Patterns

### Command Pattern

Business logic is encapsulated in command objects:

```ruby
# app/commands/some_module/some_command.rb
module SomeModule
  class SomeCommand < BaseCommand
    def run
      # Business logic here
      [success_boolean, result_object]
    end

    def authorized_entities
      [business_staff: :some_permission]
    end
  end
end
```

### Worker Pattern

Background jobs use Sidekiq workers:

```ruby
# app/workers/some_worker.rb
class SomeWorker
  include Sidekiq::Worker
  sidekiq_options retry: 5, queue: 'default'

  def perform(param1, param2)
    # Background job logic
  end
end
```

### Testing Patterns

Tests follow RSpec conventions:

```ruby
# spec/commands/some_module/some_command_spec.rb
RSpec.describe SomeModule::SomeCommand, type: :command do
  include_context 'user and business'
  
  let(:params) { { id: some_id } }
  let(:environment) { setup_environment({ api_user: business_staff }) }
  
  subject(:execute_command!) { do_command(described_class, params, environment) }

  describe '#run' do
    it 'executes successfully' do
      success, result = execute_command!
      expect(success).to be true
    end
  end
end
```

## Debugging

### Rails Debugging

```ruby
# Add to code for debugging
binding.pry          # Pry debugger
debugger            # Built-in debugger
puts "Debug: #{var}" # Simple output
```

### Sidekiq Debugging

```bash
# Monitor Sidekiq web UI
open http://localhost:4567/sidekiq

# Check Redis queues
redis-cli
> LLEN queue:default
> LRANGE queue:default 0 -1
```

### Database Debugging

```sql
-- Check active connections
SELECT * FROM pg_stat_activity;

-- Monitor slow queries
SELECT query, mean_time, calls 
FROM pg_stat_statements 
ORDER BY mean_time DESC;
```

## Common Issues

### Database Connection Issues

```bash
# Check PostgreSQL status
brew services list | grep postgresql

# Restart PostgreSQL
brew services restart postgresql

# Check database exists
psql -l | grep mgr_api
```

### Redis Connection Issues

```bash
# Check Redis status
redis-cli ping

# Restart Redis
brew services restart redis

# Clear Redis data
redis-cli FLUSHALL
```

### Asset Issues

```bash
# Precompile assets
rails assets:precompile

# Clear asset cache
rails assets:clobber
```

### Gem Issues

```bash
# Update bundler
gem update bundler

# Clean bundle
bundle clean --force

# Reinstall gems
rm Gemfile.lock
bundle install
```

## Performance Monitoring

### Development Tools

```ruby
# Add to Gemfile for development
gem 'bullet'              # N+1 query detection
gem 'rack-mini-profiler'  # Request profiling
gem 'memory_profiler'     # Memory usage analysis
```

### Monitoring Endpoints

```bash
# Health check
curl http://localhost:3000/health

# Sidekiq stats
curl http://localhost:3000/sidekiq/stats

# Database stats
rails runner "puts ActiveRecord::Base.connection.execute('SELECT version()').first"
```

## Deployment Preparation

### Environment Check

```bash
# Check environment variables
rails runner "puts ENV.keys.sort"

# Validate configuration
rails runner "Rails.application.config_for(:database)"

# Test external services
rails runner "Redis.current.ping"
```

### Security Check

```bash
# Run security audit
bundle exec brakeman

# Check for secrets in code
git secrets --scan

# Validate SSL certificates
openssl s_client -connect api.mgr.com:443
```

## Getting Help

### Documentation

- [Architecture Overview](../architecture/system-overview.md)
- [Command Pattern](../architecture/command-pattern.md)
- [Import System](../features/import-system.md)
- [API Endpoints](../api/endpoints.md)

### Resources

- **Rails Guides**: https://guides.rubyonrails.org/
- **Sidekiq Documentation**: https://github.com/mperham/sidekiq
- **RSpec Documentation**: https://rspec.info/
- **PostgreSQL Documentation**: https://www.postgresql.org/docs/

### Team Communication

- **Slack**: #mgr-api-dev
- **GitHub Issues**: For bug reports and feature requests
- **Code Reviews**: All changes require PR review
- **Daily Standups**: 9:00 AM PST
