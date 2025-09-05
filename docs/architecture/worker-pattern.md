# Worker Pattern

The MGR API uses Sidekiq workers for background job processing, providing scalable, reliable asynchronous task execution. This document outlines the worker architecture and best practices.

## 🎯 Overview

Workers handle time-consuming operations that shouldn't block the main application thread, such as:

- Data import processing
- Email/SMS notifications
- File processing
- External API integrations
- Batch operations

## 🏗️ Architecture

### Sidekiq Integration

The application uses Sidekiq as the background job processor, which provides:

- **Redis-backed queues**: Reliable job storage and retrieval
- **Multiple queues**: Priority-based job processing
- **Retry mechanisms**: Automatic retry with exponential backoff
- **Monitoring**: Web UI for job monitoring and management
- **Scaling**: Horizontal scaling across multiple processes

### Worker Structure

```ruby
class SomeWorker
  include Sidekiq::Worker
  sidekiq_options retry: 5, queue: 'default'

  def perform(param1, param2)
    # Worker logic here
  end
end
```

## 🔧 Worker Configuration

### Common Options

```ruby
sidekiq_options(
  retry: 5,                    # Number of retry attempts
  queue: 'default',            # Queue name
  backtrace: true,             # Include backtrace in failures
  dead: false,                 # Don't send to dead queue
  unique: :until_executed      # Prevent duplicate jobs
)
```

### Queue Types

| Queue Name | Priority | Purpose |
|------------|----------|---------|
| `critical` | Highest | System-critical operations |
| `user_notifications` | High | User-facing notifications |
| `staff_notifications` | High | Staff notifications |
| `default` | Medium | General background tasks |
| `low_priority` | Low | Batch operations, cleanup |

## 📋 Import System Workers

### ImportProcessorWorker

**Purpose**: Processes CSV imports asynchronously

```ruby
class ImportProcessorWorker
  include Sidekiq::Worker
  sidekiq_options retry: 5, queue: 'default'

  def perform(import_id)
    import = Import.find(import_id)
    business_account = import.business_account

    begin
      case import.import_type
      when 'csv'
        cmd = Imports::ProcessCsvImport.new(
          { import_id: import_id },
          { business_account: business_account }
        )
        success, result = cmd.run

        unless success
          import.mark_as_failed!(result[:error])
        end
      else
        import.mark_as_failed!("Unsupported import type: #{import.import_type}")
      end
    rescue => e
      import.mark_as_failed!(e.message)
      Rails.logger.error "Import processing failed for import #{import_id}: #{e.message}"
      raise e
    end
  end
end
```

**Key Features**:
- Handles different import types
- Comprehensive error handling
- Proper logging and error reporting
- Delegates to command objects for business logic

### Usage Pattern

```ruby
# Enqueue worker
ImportProcessorWorker.perform_async(import.id)

# Enqueue with delay
ImportProcessorWorker.perform_in(5.minutes, import.id)

# Enqueue at specific time
ImportProcessorWorker.perform_at(1.hour.from_now, import.id)
```

## 🔄 Worker Lifecycle

### Job States

1. **Enqueued**: Job added to queue
2. **Processing**: Worker picked up job
3. **Completed**: Job finished successfully
4. **Failed**: Job failed, may retry
5. **Dead**: Job failed permanently after retries

### Retry Logic

```ruby
# Automatic retry with exponential backoff
sidekiq_options retry: 5

# Custom retry logic
sidekiq_retries_exhausted do |msg, ex|
  # Handle permanent failure
  import_id = msg['args'].first
  import = Import.find(import_id)
  import.mark_as_failed!("Processing failed after #{msg['retry_count']} attempts")
end
```

## 🚨 Error Handling

### Error Categories

1. **Transient Errors**: Network issues, temporary service unavailability
2. **Permanent Errors**: Invalid data, missing records
3. **System Errors**: Out of memory, disk space issues

### Error Handling Strategies

```ruby
def perform(import_id)
  begin
    # Main logic
  rescue ActiveRecord::RecordNotFound => e
    # Don't retry for missing records
    Rails.logger.error "Record not found: #{e.message}"
    return
  rescue Net::TimeoutError, Net::OpenTimeout => e
    # Retry for network issues
    Rails.logger.warn "Network timeout: #{e.message}"
    raise e
  rescue => e
    # Log and re-raise for retry
    Rails.logger.error "Unexpected error: #{e.message}"
    raise e
  end
end
```

## 📊 Monitoring & Observability

### Sidekiq Web UI

Access monitoring dashboard at `/sidekiq` (admin only):

- Queue depths and processing rates
- Failed job inspection and retry
- Worker process monitoring
- Historical statistics

### Custom Metrics

```ruby
# Track processing metrics
def perform(import_id)
  start_time = Time.current
  
  begin
    # Process import
    process_import(import_id)
    
    # Record success metrics
    duration = Time.current - start_time
    StatsD.timing('import.processing_time', duration)
    StatsD.increment('import.success')
  rescue => e
    StatsD.increment('import.failure')
    raise e
  end
end
```

### Logging

```ruby
# Structured logging
Rails.logger.info({
  event: 'import_processing_started',
  import_id: import_id,
  worker: self.class.name,
  queue: self.class.sidekiq_options_hash['queue']
}.to_json)
```

## 🧪 Testing Workers

### Test Structure

```ruby
RSpec.describe ImportProcessorWorker, type: :worker do
  include_context 'user and business'

  let(:import) { Fabricate(:import_with_file, business_account: business_account) }
  let(:worker) { described_class.new }

  describe '#perform' do
    context 'when import type is csv' do
      let(:mock_command) { instance_double(Imports::ProcessCsvImport) }

      before do
        allow(Imports::ProcessCsvImport).to receive(:new).and_return(mock_command)
      end

      context 'when processing succeeds' do
        before do
          allow(mock_command).to receive(:run).and_return([true, { message: 'Success' }])
        end

        it 'calls the ProcessCsvImport command' do
          worker.perform(import.id)

          expect(Imports::ProcessCsvImport).to have_received(:new).with(
            { import_id: import.id },
            { business_account: business_account }
          )
        end
      end
    end
  end
end
```

### Testing Best Practices

1. **Mock External Dependencies**: Don't make real API calls or file operations
2. **Test Error Scenarios**: Verify error handling and retry logic
3. **Use Real Models**: Test with actual database records when possible
4. **Verify Side Effects**: Check that expected state changes occur

## 🔧 Performance Optimization

### Memory Management

```ruby
# Process large datasets in chunks
def perform(large_dataset_id)
  Dataset.find(large_dataset_id).records.find_in_batches(batch_size: 1000) do |batch|
    process_batch(batch)
    GC.start # Force garbage collection between batches
  end
end
```

### Database Optimization

```ruby
# Use bulk operations
def process_records(records)
  # Instead of individual saves
  records.each(&:save!)
  
  # Use bulk insert
  Record.insert_all(records.map(&:attributes))
end
```

### Connection Management

```ruby
# Ensure database connections are returned to pool
def perform(id)
  ActiveRecord::Base.connection_pool.with_connection do
    # Database operations
  end
end
```

## 🚀 Deployment Considerations

### Worker Scaling

```yaml
# docker-compose.yml
sidekiq:
  image: app:latest
  command: bundle exec sidekiq
  environment:
    - RAILS_ENV=production
  deploy:
    replicas: 3  # Scale based on load
```

### Queue Configuration

```ruby
# config/initializers/sidekiq.rb
Sidekiq.configure_server do |config|
  config.redis = { url: ENV['REDIS_URL'] }
  
  # Configure queues with weights
  config.queues = {
    'critical' => 10,
    'user_notifications' => 5,
    'default' => 3,
    'low_priority' => 1
  }
end
```

### Monitoring Setup

```ruby
# config/routes.rb
require 'sidekiq/web'

Rails.application.routes.draw do
  # Protect Sidekiq web interface
  authenticate :admin_user do
    mount Sidekiq::Web => '/sidekiq'
  end
end
```

## 📋 Best Practices

### Worker Design

1. **Keep Workers Simple**: Delegate complex logic to service objects or commands
2. **Idempotent Operations**: Workers should be safe to run multiple times
3. **Fail Fast**: Validate inputs early and fail quickly for invalid data
4. **Proper Error Handling**: Distinguish between retryable and permanent errors

### Job Parameters

1. **Use IDs, Not Objects**: Pass record IDs, not ActiveRecord objects
2. **Keep Parameters Simple**: Use basic data types (strings, numbers, arrays)
3. **Validate Parameters**: Check that required records exist

### Error Recovery

1. **Graceful Degradation**: Handle partial failures appropriately
2. **Dead Letter Queues**: Monitor and handle permanently failed jobs
3. **Alerting**: Set up alerts for high failure rates

## 📚 Related Documentation

- [Command Pattern](./command-pattern.md)
- [Import System](../features/import-system.md)
- [Data Import Process](../processes/data-import.md)
- [Deployment Guide](../development/deployment.md)

## 🔗 External Resources

- [Sidekiq Documentation](https://github.com/mperham/sidekiq)
- [Redis Configuration](https://redis.io/documentation)
- [Background Job Best Practices](https://github.com/mperham/sidekiq/wiki/Best-Practices)
