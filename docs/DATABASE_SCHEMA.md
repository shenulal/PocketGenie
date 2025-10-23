# PocketGenie Database Schema

## Overview

PocketGenie uses a hybrid storage approach:
- **Local Storage**: SQLite/Hive on mobile devices for offline-first functionality
- **Backend Storage**: PostgreSQL for multi-device sync and cloud features
- **Vector Storage**: Milvus for semantic search embeddings

## Local Storage (SQLite/Hive)

### Tasks Table

```sql
CREATE TABLE tasks (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  description TEXT,
  due_date TIMESTAMP,
  priority INTEGER DEFAULT 0,  -- 0=low, 1=medium, 2=high, 3=urgent
  category TEXT,
  tags JSON,  -- List of tags
  completed BOOLEAN DEFAULT FALSE,
  ai_priority_score REAL,
  embedding JSON,  -- Vector embedding for semantic search
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  synced BOOLEAN DEFAULT FALSE
);
```

### Notes Table

```sql
CREATE TABLE notes (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  content TEXT NOT NULL,
  summary TEXT,  -- AI-generated summary
  category TEXT,
  tags JSON,  -- List of tags
  embedding JSON,  -- Vector embedding for semantic search
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  synced BOOLEAN DEFAULT FALSE
);
```

### Settings Table

```sql
CREATE TABLE settings (
  key TEXT PRIMARY KEY,
  value JSON
);
```

## Backend Storage (PostgreSQL)

### Users Table

```sql
CREATE TABLE users (
  id UUID PRIMARY KEY,
  username VARCHAR(100) UNIQUE NOT NULL,
  email VARCHAR(255) UNIQUE NOT NULL,
  hashed_password VARCHAR(255) NOT NULL,
  preferences JSONB,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
```

### Tasks Table (Backend)

```sql
CREATE TABLE tasks (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  description TEXT,
  due_date TIMESTAMP,
  priority INTEGER DEFAULT 0,
  category VARCHAR(100),
  tags TEXT[],
  completed BOOLEAN DEFAULT FALSE,
  ai_priority_score REAL,
  embedding VECTOR(384),  -- Sentence Transformers embedding dimension
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_tasks_user_id ON tasks(user_id);
CREATE INDEX idx_tasks_completed ON tasks(completed);
CREATE INDEX idx_tasks_due_date ON tasks(due_date);
```

### Notes Table (Backend)

```sql
CREATE TABLE notes (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  title VARCHAR(255) NOT NULL,
  content TEXT NOT NULL,
  summary TEXT,
  category VARCHAR(100),
  tags TEXT[],
  embedding VECTOR(384),
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  updated_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_notes_user_id ON notes(user_id);
CREATE INDEX idx_notes_created_at ON notes(created_at);
```

### Device Sync Log Table

```sql
CREATE TABLE device_sync_logs (
  id UUID PRIMARY KEY,
  user_id UUID NOT NULL REFERENCES users(id),
  device_id VARCHAR(255) NOT NULL,
  entity_type VARCHAR(50) NOT NULL,  -- 'task' or 'note'
  entity_id UUID NOT NULL,
  action VARCHAR(50) NOT NULL,  -- 'create', 'update', 'delete'
  synced_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  FOREIGN KEY (user_id) REFERENCES users(id) ON DELETE CASCADE
);

CREATE INDEX idx_sync_logs_user_id ON device_sync_logs(user_id);
CREATE INDEX idx_sync_logs_device_id ON device_sync_logs(device_id);
```

## Vector Storage (Milvus)

### Collections

#### Tasks Collection

```
Collection: tasks_embeddings
Fields:
  - id (VARCHAR, primary key)
  - user_id (VARCHAR)
  - title (VARCHAR)
  - embedding (FLOAT_VECTOR, dimension=384)
  - created_at (INT64, timestamp)
```

#### Notes Collection

```
Collection: notes_embeddings
Fields:
  - id (VARCHAR, primary key)
  - user_id (VARCHAR)
  - title (VARCHAR)
  - embedding (FLOAT_VECTOR, dimension=384)
  - created_at (INT64, timestamp)
```

## Data Types

- **UUID**: Universally unique identifier for backend records
- **TEXT/VARCHAR**: String data
- **TIMESTAMP**: Date and time
- **INTEGER**: Whole numbers
- **REAL/FLOAT**: Decimal numbers
- **BOOLEAN**: True/False
- **JSON/JSONB**: Structured data
- **VECTOR**: High-dimensional vector for embeddings (384 dimensions for all-MiniLM-L6-v2)
- **TEXT[]**: Array of strings

## Relationships

```
Users
  ├── Tasks (1:N)
  ├── Notes (1:N)
  └── DeviceSyncLogs (1:N)

Tasks
  ├── Embeddings (1:1 in Milvus)
  └── DeviceSyncLogs (1:N)

Notes
  ├── Embeddings (1:1 in Milvus)
  └── DeviceSyncLogs (1:N)
```

## Indexing Strategy

- **User ID**: Indexed for fast user-specific queries
- **Completed Status**: Indexed for filtering incomplete tasks
- **Due Date**: Indexed for sorting and filtering by deadline
- **Created At**: Indexed for chronological queries
- **Vector Embeddings**: Indexed in Milvus for semantic search

## Backup & Recovery

- PostgreSQL: Use `pg_dump` for backups
- Milvus: Use Milvus backup utilities
- Local Storage: Automatic backup on device

