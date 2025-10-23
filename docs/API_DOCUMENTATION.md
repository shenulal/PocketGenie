# PocketGenie API Documentation

## Base URL

```
http://localhost:8000/api/v1
```

## Authentication

Currently, the API uses no authentication (development mode). For production, implement JWT authentication.

## Response Format

All responses are in JSON format.

### Success Response

```json
{
  "id": "uuid",
  "title": "Task Title",
  "created_at": "2024-01-01T00:00:00Z",
  ...
}
```

### Error Response

```json
{
  "detail": "Error message"
}
```

## Endpoints

### Tasks

#### Create Task

```
POST /tasks
Content-Type: application/json

{
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "priority": 1,
  "category": "shopping",
  "tags": ["urgent"],
  "due_date": "2024-01-15T10:00:00Z"
}

Response: 200 OK
{
  "id": "uuid",
  "title": "Buy groceries",
  "description": "Milk, eggs, bread",
  "priority": 1,
  "category": "shopping",
  "tags": ["urgent"],
  "due_date": "2024-01-15T10:00:00Z",
  "completed": false,
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### List Tasks

```
GET /tasks?skip=0&limit=10&completed=false&category=work

Response: 200 OK
[
  {
    "id": "uuid",
    "title": "Task 1",
    ...
  },
  ...
]
```

#### Get Task

```
GET /tasks/{task_id}

Response: 200 OK
{
  "id": "uuid",
  "title": "Task 1",
  ...
}
```

#### Update Task

```
PUT /tasks/{task_id}
Content-Type: application/json

{
  "title": "Updated title",
  "priority": 2,
  "completed": true
}

Response: 200 OK
{
  "id": "uuid",
  "title": "Updated title",
  ...
}
```

#### Delete Task

```
DELETE /tasks/{task_id}

Response: 200 OK
{
  "message": "Task deleted successfully"
}
```

#### Complete Task

```
POST /tasks/{task_id}/complete

Response: 200 OK
{
  "id": "uuid",
  "completed": true,
  ...
}
```

### Notes

#### Create Note

```
POST /notes
Content-Type: application/json

{
  "title": "Meeting Notes",
  "content": "Discussed project timeline and deliverables",
  "category": "work",
  "tags": ["meeting"]
}

Response: 200 OK
{
  "id": "uuid",
  "title": "Meeting Notes",
  "content": "Discussed project timeline and deliverables",
  "summary": "AI-generated summary...",
  "category": "work",
  "tags": ["meeting"],
  "created_at": "2024-01-01T00:00:00Z",
  "updated_at": "2024-01-01T00:00:00Z"
}
```

#### List Notes

```
GET /notes?skip=0&limit=10&category=work

Response: 200 OK
[
  {
    "id": "uuid",
    "title": "Note 1",
    ...
  },
  ...
]
```

#### Get Note

```
GET /notes/{note_id}

Response: 200 OK
{
  "id": "uuid",
  "title": "Note 1",
  ...
}
```

#### Update Note

```
PUT /notes/{note_id}
Content-Type: application/json

{
  "title": "Updated title",
  "content": "Updated content"
}

Response: 200 OK
{
  "id": "uuid",
  "title": "Updated title",
  ...
}
```

#### Delete Note

```
DELETE /notes/{note_id}

Response: 200 OK
{
  "message": "Note deleted successfully"
}
```

### Search

#### Semantic Search

```
POST /search/semantic
Content-Type: application/json

{
  "query": "project deadline",
  "entity_type": "all",
  "limit": 10
}

Response: 200 OK
{
  "query": "project deadline",
  "results": [
    {
      "entity_type": "task",
      "entity_id": "uuid",
      "title": "Complete project",
      "similarity_score": 0.95,
      "content": "Finish the project by Friday"
    },
    ...
  ]
}
```

### AI

#### Summarize Content

```
POST /ai/summarize
Content-Type: application/json

{
  "content": "Long text to summarize...",
  "max_points": 5
}

Response: 200 OK
{
  "summary": "Summary paragraph...",
  "bullet_points": [
    "Key point 1",
    "Key point 2",
    "Key point 3"
  ]
}
```

#### Prioritize Tasks

```
POST /ai/prioritize
Content-Type: application/json

{
  "tasks": [
    {
      "id": "uuid",
      "title": "Task 1",
      "due_date": "2024-01-15T10:00:00Z",
      "priority": 1,
      ...
    },
    ...
  ]
}

Response: 200 OK
{
  "prioritized_tasks": [
    {
      "id": "uuid",
      "title": "Task 1",
      ...
    },
    ...
  ],
  "next_best_action": {
    "id": "uuid",
    "title": "Most urgent task",
    ...
  },
  "reasoning": "AI reasoning for prioritization..."
}
```

## Status Codes

- `200 OK`: Successful request
- `201 Created`: Resource created
- `400 Bad Request`: Invalid request
- `404 Not Found`: Resource not found
- `500 Internal Server Error`: Server error

## Rate Limiting

Currently no rate limiting. Implement in production.

## Pagination

Use `skip` and `limit` parameters for pagination:
- `skip`: Number of items to skip (default: 0)
- `limit`: Number of items to return (default: 10, max: 100)

