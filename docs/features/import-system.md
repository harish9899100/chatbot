# Import System

The Import System provides a robust, scalable solution for importing CSV data from ZIP files into the MGR platform. It supports batch processing, progress tracking, and comprehensive error handling.

## 🎯 Overview

The Import System allows business accounts to upload ZIP files containing CSV data that gets processed asynchronously and imported into the system as `ThirdPartyImportedDatum` records for further processing.

### Key Features

- **ZIP File Processing**: Extracts and validates CSV files from uploaded ZIP archives
- **Batch Processing**: Handles large datasets efficiently with configurable batch sizes
- **Progress Tracking**: Real-time progress updates during import processing
- **Error Handling**: Comprehensive error handling with detailed logging
- **Activity Logging**: Full audit trail of import operations
- **File Type Validation**: Only processes predefined CSV file types
- **Asynchronous Processing**: Background processing using Sidekiq workers

## 🏗️ Architecture

### Components

1. **Import Model** (`app/models/import.rb`)
2. **Process Command** (`app/commands/imports/process.rb`)
3. **ProcessCsvImport Command** (`app/commands/imports/process_csv_import.rb`)
4. **ImportProcessorWorker** (`app/workers/import_processor_worker.rb`)
5. **ThirdPartyImportedDatum Model** (for storing imported records)

### Flow Diagram

```
[ZIP Upload] → [Import Created] → [Process Command] → [Worker Queued]
                                                           ↓
[CSV Processing] ← [File Extraction] ← [Background Worker]
        ↓
[Batch Insert] → [Progress Updates] → [Activity Logging] → [Completion]
```

## 📋 Supported File Types

The system supports 22 predefined CSV file types mapped to specific data types:

| CSV File Name | Data Type | Description |
|---------------|-----------|-------------|
| `Clients.csv` | `UserProfile` | Client/user information |
| `Products.csv` | `Product` | Product catalog data |
| `AccountBalances.csv` | `UserAccountBalance` | Account balance records |
| `Locations.csv` | `Location` | Business location data |
| `Trainers.csv` | `BusinessStaff` | Staff/trainer information |
| `Payments.csv` | `UserTransaction` | Payment transactions |
| `Orders.csv` | `Order` | Order/sales data |
| ... | ... | (17 more types) |

## 🚀 Usage

### 1. Creating an Import

```ruby
# Create import with file attachment
import = business_account.imports.create!(
  name: "Monthly Data Import",
  description: "Import client and product data for March 2024",
  import_type: "csv",
  created_by: business_staff
)

# Attach ZIP file
import.file_asset = Asset.create!(
  business_account: business_account,
  assetable: import,
  file_type: "application/zip",
  key: "file",
  orig_filename: "march_data.zip"
)
```

### 2. Processing an Import

```ruby
# Using the Process command
cmd = Imports::Process.new(
  { id: import.id },
  { business_account: business_account, api_user: business_staff }
)

success, result = cmd.run

if success
  # Import queued for background processing
  puts "Import #{result.id} is now processing"
else
  # Handle errors
  puts "Error: #{cmd.errors.full_messages.join(', ')}"
end
```

### 3. Monitoring Progress

```ruby
# Check import status
import.reload

puts "Status: #{import.status}"
puts "Progress: #{import.progress_percentage}%"
puts "Records: #{import.processed_records}/#{import.total_records}"
puts "Success Rate: #{import.success_rate}%"

# Import statuses: pending, processing, completed, failed
```

## 🔧 Configuration

### Batch Size

The system processes records in batches for optimal performance:

```ruby
# In ProcessCsvImport command
BATCH_SIZE = 1000  # Configurable batch size
```

### File Size Limits

Configure maximum file sizes in your application:

```ruby
# Recommended limits
MAX_ZIP_SIZE = 100.megabytes
MAX_CSV_ROWS = 50_000
```

## 📊 Data Flow

### 1. File Upload & Validation

```ruby
# Validation checks
- ZIP file format
- File size limits  
- Required CSV structure
- File name mapping
```

### 2. CSV Processing

```ruby
# For each valid CSV file:
1. Extract from ZIP
2. Parse CSV headers
3. Count total rows
4. Process in batches
5. Insert into ThirdPartyImportedDatum
6. Update progress
```

### 3. Record Structure

```ruby
# ThirdPartyImportedDatum attributes
{
  data_json: { /* Original CSV row data */ },
  data_type: "UserProfile",
  import_source: "csv",
  business_account_id: "uuid",
  source_id: "import_uuid",
  status: "pending",
  created_at: timestamp,
  updated_at: timestamp
}
```

## 🚨 Error Handling

### Common Error Scenarios

1. **No File Attached**
   ```ruby
   # Error: "No file attached to import"
   # Status: failed
   ```

2. **Invalid ZIP Content**
   ```ruby
   # Error: "No valid CSV files found in ZIP"
   # Status: failed
   ```

3. **Processing Errors**
   ```ruby
   # Individual row errors logged
   # Import continues processing
   # Failed records tracked separately
   ```

### Error Recovery

```ruby
# Check for failed imports
failed_imports = business_account.imports.failed

failed_imports.each do |import|
  puts "Import #{import.id}: #{import.error_message}"
  # Option to retry or investigate
end
```

## 📈 Performance Considerations

### Optimization Strategies

1. **Batch Processing**: Large files processed in 1000-record batches
2. **Background Processing**: Async processing prevents UI blocking
3. **Progress Updates**: Efficient progress tracking without excessive DB calls
4. **Memory Management**: Streaming ZIP extraction to minimize memory usage

### Monitoring

```ruby
# Track processing metrics
- Average processing time per record
- Memory usage during large imports
- Failed record patterns
- Peak processing times
```

## 🧪 Testing

The Import System includes comprehensive test coverage:

- **Unit Tests**: Individual component testing
- **Integration Tests**: End-to-end import flow
- **Performance Tests**: Large file processing
- **Error Handling Tests**: Various failure scenarios

### Running Tests

```bash
# Run all import tests
bundle exec rspec spec/commands/imports/

# Run specific test files
bundle exec rspec spec/commands/imports/process_csv_import_spec.rb
bundle exec rspec spec/workers/import_processor_worker_spec.rb
```

## 🔍 Troubleshooting

### Common Issues

1. **Import Stuck in Processing**
   ```ruby
   # Check Sidekiq queue
   # Look for worker errors in logs
   # Verify file accessibility
   ```

2. **Partial Data Import**
   ```ruby
   # Check failed_records count
   # Review error logs
   # Validate CSV format
   ```

3. **Performance Issues**
   ```ruby
   # Monitor batch size
   # Check database performance
   # Review memory usage
   ```

## 📚 Related Documentation

- [Command Pattern](../architecture/command-pattern.md)
- [Worker Pattern](../architecture/worker-pattern.md)
- [Data Import Process](../processes/data-import.md)
- [API Endpoints](../api/endpoints.md)

## 🔄 Future Enhancements

- Support for additional file formats (Excel, JSON)
- Real-time progress WebSocket updates
- Advanced data validation rules
- Automatic data transformation pipelines
- Import scheduling and automation
