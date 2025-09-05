# API Endpoints

This document provides detailed information about all API endpoints in the MGR platform.

## Authentication

All API endpoints require authentication via Bearer token in the Authorization header:

```
Authorization: Bearer your_api_token_here
```

## Base URL

```
https://api.mgr.com/api
```

## Response Format

All API responses follow a consistent JSON format:

### Success Response
```json
{
  "data": { /* response data */ },
  "meta": { /* pagination, etc. */ }
}
```

### Error Response
```json
{
  "errors": [
    {
      "field": "field_name",
      "message": "Error description"
    }
  ]
}
```

## Import Endpoints

### Create Import

Creates a new import record with file attachment.

**Endpoint:** `POST /imports`

**Request Body:**
```json
{
  "name": "Monthly Data Import",
  "description": "Import client and product data for March 2024",
  "import_type": "csv",
  "file_asset_attributes": {
    "file_type": "application/zip",
    "file_size": 1048576,
    "orig_filename": "march_data.zip",
    "key": "file"
  }
}
```

**Response:** `201 Created`
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Monthly Data Import",
  "description": "Import client and product data for March 2024",
  "import_type": "csv",
  "status": "pending",
  "total_records": 0,
  "processed_records": 0,
  "successful_records": 0,
  "failed_records": 0,
  "progress_percentage": 0,
  "success_rate": 0,
  "created_at": "2024-03-15T10:30:00Z",
  "updated_at": "2024-03-15T10:30:00Z",
  "file_asset": {
    "id": "660e8400-e29b-41d4-a716-446655440001",
    "file_type": "application/zip",
    "file_size": 1048576,
    "orig_filename": "march_data.zip",
    "s3_url": "https://s3.amazonaws.com/bucket/path/to/file.zip"
  }
}
```

### Process Import

Initiates background processing of a pending import.

**Endpoint:** `POST /imports/:id/process`

**Parameters:**
- `id` (UUID) - Import ID

**Response:** `200 OK`
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "status": "processing",
  "started_at": "2024-03-15T10:35:00Z",
  "message": "Import processing has been queued"
}
```

**Error Responses:**
- `404 Not Found` - Import not found
- `422 Unprocessable Entity` - Import cannot be processed (wrong status, no file, etc.)
- `403 Forbidden` - Insufficient permissions

### Get Import

Retrieves details about a specific import.

**Endpoint:** `GET /imports/:id`

**Parameters:**
- `id` (UUID) - Import ID

**Response:** `200 OK`
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Monthly Data Import",
  "description": "Import client and product data for March 2024",
  "import_type": "csv",
  "status": "completed",
  "total_records": 5000,
  "processed_records": 5000,
  "successful_records": 4995,
  "failed_records": 5,
  "progress_percentage": 100.0,
  "success_rate": 99.9,
  "started_at": "2024-03-15T10:35:00Z",
  "completed_at": "2024-03-15T10:37:30Z",
  "created_at": "2024-03-15T10:30:00Z",
  "updated_at": "2024-03-15T10:37:30Z",
  "error_message": null,
  "file_asset": {
    "id": "660e8400-e29b-41d4-a716-446655440001",
    "file_type": "application/zip",
    "file_size": 1048576,
    "orig_filename": "march_data.zip"
  }
}
```

### List Imports

Retrieves a paginated list of imports for the current business account.

**Endpoint:** `GET /imports`

**Query Parameters:**
- `status` (string, optional) - Filter by status: `pending`, `processing`, `completed`, `failed`
- `page` (integer, optional) - Page number (default: 1)
- `per_page` (integer, optional) - Results per page (default: 20, max: 100)
- `sort` (string, optional) - Sort field: `created_at`, `updated_at`, `name` (default: `created_at`)
- `order` (string, optional) - Sort order: `asc`, `desc` (default: `desc`)

**Response:** `200 OK`
```json
{
  "imports": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "name": "Monthly Data Import",
      "status": "completed",
      "total_records": 5000,
      "successful_records": 4995,
      "failed_records": 5,
      "progress_percentage": 100.0,
      "success_rate": 99.9,
      "created_at": "2024-03-15T10:30:00Z",
      "updated_at": "2024-03-15T10:37:30Z"
    }
  ],
  "pagination": {
    "current_page": 1,
    "total_pages": 3,
    "total_count": 25,
    "per_page": 20
  }
}
```

### Update Import

Updates import metadata (only allowed for pending imports).

**Endpoint:** `PUT /imports/:id`

**Parameters:**
- `id` (UUID) - Import ID

**Request Body:**
```json
{
  "name": "Updated Import Name",
  "description": "Updated description"
}
```

**Response:** `200 OK`
```json
{
  "id": "550e8400-e29b-41d4-a716-446655440000",
  "name": "Updated Import Name",
  "description": "Updated description",
  "status": "pending",
  "updated_at": "2024-03-15T10:45:00Z"
}
```

### Delete Import

Deletes an import (only allowed for pending or failed imports).

**Endpoint:** `DELETE /imports/:id`

**Parameters:**
- `id` (UUID) - Import ID

**Response:** `204 No Content`

## Third Party Imported Data Endpoints

### List Imported Data

Retrieves a paginated list of imported data records with filtering and search capabilities.

**Endpoint:** `GET /third_party_imported_data`

**Query Parameters:**
- `data_type` (string, optional) - Filter by data type (Location, UserProfile, Product, etc.)
- `status` (string, optional) - Filter by status: `pending`, `importing`, `imported`, `failed`, `skipped`
- `import_source` (string, optional) - Filter by import source: `csv`, `api`, etc.
- `source_id` (UUID, optional) - Filter by source import ID
- `search` (string, optional) - Search within data_json content
- `created_after` (datetime, optional) - Filter records created after this date
- `created_before` (datetime, optional) - Filter records created before this date
- `page` (integer, optional) - Page number (default: 1)
- `per_page` (integer, optional) - Results per page (default: 20, max: 100)
- `sort` (string, optional) - Sort field: `created_at`, `updated_at`, `data_type`, `status`
- `order` (string, optional) - Sort order: `asc`, `desc` (default: `desc`)

**Response:** `200 OK`
```json
{
  "data": [
    {
      "id": "550e8400-e29b-41d4-a716-446655440000",
      "data_type": "UserProfile",
      "status": "pending",
      "import_source": "csv",
      "source_id": "import-uuid",
      "data_json": {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com"
      },
      "data_preview": {
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com"
      },
      "status_label": "Pending",
      "created_at": "2024-03-15T10:30:00Z",
      "updated_at": "2024-03-15T10:30:00Z"
    }
  ],
  "pagination": {
    "curr_page": 1,
    "next_page": 2,
    "prev_page": null,
    "max_page": 5,
    "total_count": 100,
    "per_page": 20
  },
  "summary": {
    "total_records": 100,
    "by_status": {
      "pending": 80,
      "imported": 15,
      "failed": 5
    },
    "by_data_type": {
      "UserProfile": 50,
      "Product": 30,
      "Location": 20
    },
    "by_import_source": {
      "csv": 100
    }
  }
}
```

### Get Imported Data Record

Retrieves details about a specific imported data record.

**Endpoint:** `GET /third_party_imported_data/:id`

**Parameters:**
- `id` (UUID) - Record ID

**Response:** `200 OK`
```json
{
  "data": {
    "id": "550e8400-e29b-41d4-a716-446655440000",
    "data_type": "UserProfile",
    "status": "pending",
    "import_source": "csv",
    "source_id": "import-uuid",
    "data_json": {
      "first_name": "John",
      "last_name": "Doe",
      "email": "john@example.com",
      "phone": "+15551234567",
      "address": "123 Main St"
    },
    "location": {
      "id": "location-uuid",
      "name": "Main Location"
    },
    "linked_to": null,
    "created_at": "2024-03-15T10:30:00Z",
    "updated_at": "2024-03-15T10:30:00Z"
  }
}
```

### Delete Imported Data Record

Deletes a specific imported data record (only allowed for pending, skipped, or failed records).

**Endpoint:** `DELETE /third_party_imported_data/:id`

**Parameters:**
- `id` (UUID) - Record ID

**Response:** `204 No Content`

**Error Responses:**
- `422 Unprocessable Entity` - Cannot delete imported or importing records

### Bulk Delete Imported Data

Deletes multiple imported data records at once.

**Endpoint:** `DELETE /third_party_imported_data/bulk_destroy`

**Request Body:**
```json
{
  "ids": [
    "550e8400-e29b-41d4-a716-446655440000",
    "660e8400-e29b-41d4-a716-446655440001"
  ]
}
```

**Response:** `200 OK`
```json
{
  "message": "Successfully deleted 2 records",
  "deleted_count": 2
}
```

### Import Data to Models

Initiates the process of importing data from ThirdPartyImportedDatum records into actual application models.

**Endpoint:** `POST /third_party_imported_data/import_data`

**Request Body:**
```json
{
  "data_type": "UserProfile",
  "import_all": true
}
```

**Or for specific records:**
```json
{
  "data_type": "UserProfile",
  "record_ids": [
    "550e8400-e29b-41d4-a716-446655440000",
    "660e8400-e29b-41d4-a716-446655440001"
  ]
}
```

**Response:** `200 OK`
```json
{
  "message": "Importing all UserProfile records is in progress",
  "job_id": "worker-job-id"
}
```

**Error Responses:**
- `422 Unprocessable Entity` - Prerequisites not met, invalid data type, or records already imported

### Get Data Types

Retrieves available data types with their import status and prerequisites.

**Endpoint:** `GET /third_party_imported_data/data_types`

**Response:** `200 OK`
```json
{
  "data_types": [
    {
      "name": "Location",
      "display_name": "Location",
      "import_order": 0,
      "can_import": true,
      "prerequisite_status": "ready",
      "statuses": {
        "pending": 5,
        "imported": 0,
        "failed": 0,
        "importing": 0,
        "skipped": 0
      },
      "total_records": 5
    },
    {
      "name": "UserProfile",
      "display_name": "User Profile",
      "import_order": 1,
      "can_import": false,
      "prerequisite_status": "waiting_for: Location",
      "statuses": {
        "pending": 50,
        "imported": 0,
        "failed": 0,
        "importing": 0,
        "skipped": 0
      },
      "total_records": 50
    }
  ],
  "import_order": [
    "Location",
    "UserProfile",
    "UserNote",
    "UserProfileNotificationPreference",
    "BusinessStaff",
    "Product",
    "UserAccountBalance",
    "Order",
    "PackageInstance",
    "ResourceOffering",
    "ResourceReservation"
  ]
}
```

### Get Summary

Retrieves comprehensive summary of all imported data.

**Endpoint:** `GET /third_party_imported_data/summary`

**Response:** `200 OK`
```json
{
  "summary": {
    "overview": {
      "total_records": 500,
      "pending_records": 400,
      "imported_records": 80,
      "failed_records": 15,
      "skipped_records": 5,
      "importing_records": 0,
      "unique_data_types": 8,
      "latest_import": "2024-03-15T10:30:00Z"
    },
    "by_data_type": {
      "UserProfile": {
        "statuses": {
          "pending": 200,
          "imported": 50,
          "failed": 10
        },
        "total": 260,
        "import_order": 1
      }
    },
    "by_status": {
      "pending": 400,
      "imported": 80,
      "failed": 15,
      "skipped": 5
    },
    "by_import_source": {
      "csv": 500
    },
    "recent_activity": [
      {
        "data_type": "UserProfile",
        "status": "imported",
        "created_at": "2024-03-15T10:30:00Z"
      }
    ],
    "import_readiness": {
      "ready_to_import": ["Location"],
      "blocked_types": [
        {
          "name": "UserProfile",
          "reason": "waiting_for: Location"
        }
      ],
      "next_recommended": "Location"
    }
  }
}
```

## Import Status Values

| Status | Description |
|--------|-------------|
| `pending` | Import created but not yet processing |
| `processing` | Import is currently being processed in background |
| `completed` | Import finished successfully |
| `failed` | Import failed due to an error |

## Supported CSV File Types

The import system supports the following CSV file types:

| File Name | Data Type | Description |
|-----------|-----------|-------------|
| `Clients.csv` | `UserProfile` | Client/customer information |
| `Products.csv` | `Product` | Product catalog data |
| `AccountBalances.csv` | `UserAccountBalance` | Account balance records |
| `Locations.csv` | `Location` | Business location data |
| `Trainers.csv` | `BusinessStaff` | Staff/trainer information |
| `Payments.csv` | `UserTransaction` | Payment transaction records |
| `Orders.csv` | `Order` | Sales/order data |
| `AppointmentNotes.csv` | `UserNote` | Appointment notes |
| `ClientAutopayContracts.csv` | `RecurringPackageInstance` | Recurring contracts |
| `ClientNotifications.csv` | `UserNotification` | User notifications |
| `ClientPricingOptions.csv` | `Product` | Pricing options |
| `ClientRelationships.csv` | `UserProfile` | Client relationships |
| `ClientSales.csv` | `Order` | Sales records |
| `ClientTypes.csv` | `UserProfile` | Client type classifications |
| `ContactLogs.csv` | `UserProfile` | Contact history |
| `GiftCardBalances.csv` | `GiftCardInstance` | Gift card balances |
| `Indexes.csv` | `UserProfile` | Index data |
| `Notes - Redacted.csv` | `UserNote` | Redacted notes |
| `Referrers.csv` | `UserProfile` | Referrer information |
| `ReservationData.csv` | `ResourceReservation` | Reservation records |
| `RewardPoints.csv` | `UserProfile` | Reward point data |
| `VisitData.csv` | `ResourceReservation` | Visit records |
| `VisitPaymentLinking.csv` | `PackageInstance` | Visit payment links |

## Error Codes

### Import-Specific Errors

| Code | Message | Description |
|------|---------|-------------|
| `IMPORT_001` | No file attached to import | Import record has no file asset |
| `IMPORT_002` | No valid CSV files found in ZIP | ZIP contains no supported CSV files |
| `IMPORT_003` | Import cannot be processed | Import status or state prevents processing |
| `IMPORT_004` | Unsupported import type | Import type is not supported |
| `IMPORT_005` | File download failed | Unable to download file from S3 |
| `IMPORT_006` | CSV parsing error | Error parsing CSV file content |
| `IMPORT_007` | Batch insert failed | Database insertion error |

### General API Errors

| Code | Status | Description |
|------|--------|-------------|
| `AUTH_001` | 401 | Invalid or missing authentication token |
| `AUTH_002` | 403 | Insufficient permissions for operation |
| `VALIDATION_001` | 422 | Request validation failed |
| `NOT_FOUND_001` | 404 | Requested resource not found |
| `RATE_LIMIT_001` | 429 | Rate limit exceeded |
| `SERVER_ERROR_001` | 500 | Internal server error |

## Rate Limiting

API requests are rate limited per business account:

- **Standard endpoints**: 1000 requests per hour
- **Import processing**: 10 concurrent imports per business account
- **File uploads**: 100MB per file, 1GB total per hour

Rate limit headers are included in all responses:

```
X-RateLimit-Limit: 1000
X-RateLimit-Remaining: 999
X-RateLimit-Reset: 1640995200
```

## Webhooks

The API supports webhooks for real-time notifications of import status changes:

### Import Status Changed

Triggered when an import status changes (processing → completed/failed).

**Payload:**
```json
{
  "event": "import.status_changed",
  "data": {
    "import_id": "550e8400-e29b-41d4-a716-446655440000",
    "status": "completed",
    "previous_status": "processing",
    "total_records": 5000,
    "successful_records": 4995,
    "failed_records": 5,
    "completed_at": "2024-03-15T10:37:30Z"
  },
  "timestamp": "2024-03-15T10:37:30Z"
}
```

## SDK Examples

### cURL

```bash
# Create import
curl -X POST https://api.mgr.com/api/imports \
  -H "Authorization: Bearer your_token" \
  -H "Content-Type: application/json" \
  -d '{
    "name": "Test Import",
    "import_type": "csv",
    "file_asset_attributes": {
      "file_type": "application/zip",
      "file_size": 1024,
      "orig_filename": "test.zip",
      "key": "file"
    }
  }'

# Process import
curl -X POST https://api.mgr.com/api/imports/550e8400-e29b-41d4-a716-446655440000/process \
  -H "Authorization: Bearer your_token"

# Check status
curl https://api.mgr.com/api/imports/550e8400-e29b-41d4-a716-446655440000 \
  -H "Authorization: Bearer your_token"
```

### JavaScript

```javascript
const API_BASE = 'https://api.mgr.com/api';
const token = 'your_token_here';

// Create import
const createImport = async (importData) => {
  const response = await fetch(`${API_BASE}/imports`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(importData)
  });
  return response.json();
};

// Process import
const processImport = async (importId) => {
  const response = await fetch(`${API_BASE}/imports/${importId}/process`, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  return response.json();
};

// Monitor progress
const checkImportStatus = async (importId) => {
  const response = await fetch(`${API_BASE}/imports/${importId}`, {
    headers: {
      'Authorization': `Bearer ${token}`
    }
  });
  return response.json();
};
```
