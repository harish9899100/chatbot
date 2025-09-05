# Command Pattern

The MGR API uses the Command Pattern as the primary architectural approach for handling business logic. This pattern provides a consistent, testable, and maintainable way to encapsulate business operations.

## 🎯 Overview

Commands are the core business logic layer that sits between controllers and models. They encapsulate complex operations, handle authorization, validation, and provide a consistent interface for all business actions.

## 🏗️ Structure

### Base Command

All commands inherit from `BaseCommand` which provides:

- **Authorization**: Role-based access control
- **Error Handling**: Consistent error collection and reporting
- **Activity Tracking**: Automatic audit trail creation
- **Return Format**: Standardized success/failure responses

### Command Anatomy

```ruby
module SomeModule
  class SomeCommand < BaseCommand
    def run
      # Main business logic
      # Returns [success_boolean, result_object]
    end

    def authorized_entities
      # Define who can execute this command
      [:system_admin, business_staff: :some_permission]
    end

    def track_activity_name
      # Optional: Define activity type for audit trail
      Activity::SomeAction
    end

    private

    def some_helper_method
      # Private helper methods
    end
  end
end
```

## 🔐 Authorization System

### Permission Types

Commands support multiple authorization patterns:

```ruby
def authorized_entities
  [
    :system_admin,                    # System administrators
    business_staff: :manage_client,   # Staff with specific permission
    user_profile: :self,              # Users acting on themselves
    :public                           # No authorization required
  ]
end
```

### Authorization Flow

1. Command instantiated with `api_user` and `business_account`
2. `authorized_entities` checked against user permissions
3. `BaseCommand::AuthorizationError` raised if unauthorized
4. Command execution proceeds if authorized

## 📊 Return Format

Commands follow a consistent return pattern:

### Success Response
```ruby
[true, result_object]
```

### Failure Response
```ruby
[false, command_object_with_errors]
```

### Usage Example
```ruby
success, result = SomeCommand.new(params, environment).run

if success
  # Handle successful operation
  render json: result
else
  # Handle errors
  render json: { errors: result.errors }, status: 422
end
```

## 🎯 Import System Commands

### 1. Imports::Process

**Purpose**: Orchestrates the import process initiation

```ruby
module Imports
  class Process < BaseCommand
    def run
      import = business_account.imports.find(params[:id])
      
      unless import.can_be_processed?
        add_error(:base, 'Import cannot be processed.')
        return [false, import]
      end

      import.mark_as_processing!
      ImportProcessorWorker.perform_async(import.id)
      
      [true, import]
    end

    def authorized_entities
      [business_staff: :manage_client]
    end

    def track_activity_name
      Activity::ProcessImport
    end
  end
end
```

**Key Features**:
- Validates import can be processed
- Updates import status
- Queues background worker
- Tracks activity for audit trail

### 2. Imports::ProcessCsvImport

**Purpose**: Handles the actual CSV processing logic

```ruby
module Imports
  class ProcessCsvImport < BaseCommand
    BATCH_SIZE = 1000

    def run
      import = business_account.imports.find(params[:import_id])
      
      # Validation
      unless import.file_asset&.s3_url
        import.mark_as_failed!('No file attached to import')
        return [false, { error: 'No file attached to import' }]
      end

      # Processing
      begin
        zip_content = download_zip_file(import.file_asset.s3_url)
        csv_files = extract_and_validate_csv_files(zip_content)
        
        # Process each CSV file
        process_csv_files(csv_files, import)
        
        import.mark_as_completed!
        log_import_activity(import, csv_files)
        
        [true, success_response]
      rescue => e
        import.mark_as_failed!(e.message)
        [false, { error: e.message }]
      end
    end

    def authorized_entities
      [:system_admin, business_staff: :manage_client]
    end
  end
end
```

**Key Features**:
- File validation and processing
- Batch processing for performance
- Progress tracking
- Comprehensive error handling
- Activity logging

## 🧪 Testing Commands

### Test Structure

```ruby
RSpec.describe SomeModule::SomeCommand, type: :command do
  include_context 'user and business'
  
  let(:params) { { id: some_id } }
  let(:environment) { setup_environment({ api_user: business_staff, business_account: business_account }) }
  
  subject(:execute_command!) { do_command(described_class, params, environment) }

  describe '#run' do
    context 'when successful' do
      it 'returns success and result' do
        success, result = execute_command!
        
        expect(success).to be true
        expect(result).to be_a(SomeModel)
      end
    end

    context 'when validation fails' do
      it 'returns failure with errors' do
        result = execute_command!
        
        expect(result).to be_a(described_class)
        expect(result.errors).to be_present
      end
    end
  end

  describe 'authorization' do
    context 'when user lacks permission' do
      it 'raises authorization error' do
        expect { execute_command! }.to raise_error(BaseCommand::AuthorizationError)
      end
    end
  end
end
```

### Testing Best Practices

1. **Use Real Objects**: Prefer fabricators over mocks for models
2. **Test Authorization**: Always test permission scenarios
3. **Test Error Cases**: Cover validation failures and edge cases
4. **Test Activity Tracking**: Verify audit trail creation
5. **Use Contexts**: Group related test scenarios

## 🔄 Command Composition

### Calling Commands from Commands

```ruby
class ParentCommand < BaseCommand
  def run
    # Call another command
    child_cmd = ChildCommand.new(child_params, environment)
    success, result = child_cmd.run
    
    unless success
      add_errors(child_cmd.errors)
      return [false, self]
    end
    
    # Continue with parent logic
    [true, final_result]
  end
end
```

### Nested Command Patterns

```ruby
# For complex workflows
class ComplexWorkflow < BaseCommand
  def run
    steps = [
      -> { validate_input },
      -> { process_data },
      -> { send_notifications },
      -> { update_records }
    ]
    
    steps.each do |step|
      success, result = step.call
      return [false, self] unless success
    end
    
    [true, final_result]
  end
end
```

## 📈 Performance Considerations

### Optimization Strategies

1. **Batch Operations**: Use `insert_all` for bulk database operations
2. **Lazy Loading**: Only load required associations
3. **Background Processing**: Offload heavy work to workers
4. **Caching**: Cache expensive computations
5. **Database Optimization**: Use appropriate indexes and queries

### Memory Management

```ruby
# Process large datasets in chunks
def process_large_dataset(records)
  records.find_in_batches(batch_size: 1000) do |batch|
    process_batch(batch)
  end
end
```

## 🚨 Error Handling

### Error Types

1. **Validation Errors**: Business rule violations
2. **Authorization Errors**: Permission failures
3. **System Errors**: Infrastructure issues
4. **External Service Errors**: Third-party API failures

### Error Handling Patterns

```ruby
def run
  begin
    # Main logic
    [true, result]
  rescue SomeSpecificError => e
    add_error(:base, "Specific error: #{e.message}")
    [false, self]
  rescue => e
    Rails.logger.error "Unexpected error in #{self.class}: #{e.message}"
    add_error(:base, "An unexpected error occurred")
    [false, self]
  end
end
```

## 📚 Best Practices

### Command Design

1. **Single Responsibility**: One command, one business operation
2. **Consistent Interface**: Always return [boolean, object]
3. **Proper Authorization**: Define clear permission requirements
4. **Error Handling**: Comprehensive error collection and logging
5. **Activity Tracking**: Log important business actions

### Code Organization

1. **Namespace by Feature**: Group related commands in modules
2. **Clear Naming**: Command names should describe the action
3. **Helper Methods**: Extract complex logic into private methods
4. **Documentation**: Document complex business rules

### Testing

1. **Comprehensive Coverage**: Test all paths and edge cases
2. **Real Data**: Use fabricators for realistic test scenarios
3. **Authorization Testing**: Verify permission enforcement
4. **Performance Testing**: Test with realistic data volumes

## 🔗 Related Documentation

- [Worker Pattern](./worker-pattern.md)
- [Import System](../features/import-system.md)
- [Testing Guidelines](../development/testing.md)
- [API Error Handling](../api/error-handling.md)
