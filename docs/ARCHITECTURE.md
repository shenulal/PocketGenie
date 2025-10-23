# PocketGenie Architecture

## System Overview

```
┌─────────────────────────────────────────────────────────────┐
│                    Mobile App (Flutter)                      │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  UI Layer (Screens, Widgets)                         │   │
│  │  - HomeScreen, TasksScreen, NotesScreen, etc.       │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  State Management (Riverpod)                         │   │
│  │  - TasksProvider, NotesProvider                      │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Services Layer                                      │   │
│  │  - ApiService, StorageService                        │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Local Storage (Hive + SQLite)                       │   │
│  │  - Tasks, Notes, Settings                            │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
                            ↓ HTTP/REST
┌─────────────────────────────────────────────────────────────┐
│                  Backend API (FastAPI)                       │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  API Layer (Routers)                                 │   │
│  │  - /tasks, /notes, /search, /ai                      │   │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Service Layer                                       │   │
│  │  - TaskService, NoteService, SearchService, AIService│  │
│  └──────────────────────────────────────────────────────┘   │
│  ┌──────────────────────────────────────────────────────┐   │
│  │  Data Layer (SQLAlchemy ORM)                         │   │
│  │  - Models: Task, Note, User, DeviceSyncLog           │   │
│  └──────────────────────────────────────────────────────┘   │
└─────────────────────────────────────────────────────────────┘
         ↓                    ↓                    ↓
    ┌─────────┐          ┌─────────┐         ┌──────────┐
    │PostgreSQL│          │ Milvus  │         │  MinIO   │
    │Database  │          │ Vector  │         │ Storage  │
    │          │          │   DB    │         │          │
    └─────────┘          └─────────┘         └──────────┘
```

## Component Architecture

### Mobile App (Flutter)

#### Presentation Layer
- **Screens**: HomeScreen, TasksScreen, NotesScreen, SearchScreen, SettingsScreen
- **Widgets**: TaskCard, NoteCard, custom UI components
- **Navigation**: GoRouter for app navigation

#### State Management (Riverpod)
- **Providers**: TasksProvider, NotesProvider
- **Notifiers**: TasksNotifier, NotesNotifier
- Manages app state and side effects

#### Services Layer
- **ApiService**: HTTP client for backend communication
- **StorageService**: Local storage operations (Hive/SQLite)
- **NotificationService**: Push notifications

#### Models
- **TaskModel**: Task data structure with Hive adapter
- **NoteModel**: Note data structure with Hive adapter

### Backend API (FastAPI)

#### API Layer (Routers)
- **tasks.py**: Task CRUD endpoints
- **notes.py**: Note CRUD endpoints
- **search.py**: Semantic search endpoints
- **ai.py**: AI/LLM endpoints

#### Service Layer
- **TaskService**: Task business logic
- **NoteService**: Note business logic
- **SearchService**: Semantic search logic
- **AIService**: LLM integration and task prioritization
- **EmbeddingService**: Vector embedding generation

#### Data Layer
- **Models**: SQLAlchemy ORM models
- **Database**: PostgreSQL connection and session management
- **Schemas**: Pydantic validation schemas

## Data Flow

### Creating a Task

```
Mobile App
  ↓
User enters task details
  ↓
TasksProvider.addTask()
  ↓
StorageService.saveTask() → Local Hive storage
  ↓
ApiService.createTask() → Backend API
  ↓
Backend: TaskService.create_task()
  ↓
EmbeddingService.get_embedding() → Generate vector
  ↓
Save to PostgreSQL + Milvus
  ↓
Return response to mobile
  ↓
Update local storage with synced status
```

### Semantic Search

```
Mobile App
  ↓
User enters search query
  ↓
ApiService.semanticSearch()
  ↓
Backend: SearchService.semantic_search()
  ↓
EmbeddingService.get_embedding(query)
  ↓
Query Milvus for similar embeddings
  ↓
Calculate similarity scores
  ↓
Return ranked results
  ↓
Display in SearchScreen
```

### AI Summarization

```
Mobile App
  ↓
User creates note with content
  ↓
NoteService.create_note()
  ↓
ApiService.createNote()
  ↓
Backend: NoteService.create_note()
  ↓
AIService.summarize(content)
  ↓
Call Z.ai LLM server
  ↓
Parse response into summary + bullet points
  ↓
Save to PostgreSQL
  ↓
Return to mobile with summary
  ↓
Display in NoteCard
```

## Technology Stack Details

### Frontend (Mobile)
- **Flutter**: Cross-platform UI framework
- **Riverpod**: State management and dependency injection
- **Hive**: Local key-value storage
- **SQLite**: Relational local storage
- **Dio**: HTTP client
- **GoRouter**: Navigation

### Backend
- **FastAPI**: Modern Python web framework
- **SQLAlchemy**: ORM for database operations
- **Pydantic**: Data validation
- **Sentence Transformers**: Embedding generation
- **Requests**: HTTP client for LLM calls

### Infrastructure
- **PostgreSQL**: Primary database
- **Milvus**: Vector database for semantic search
- **Redis**: Caching and task queue
- **MinIO**: S3-compatible object storage
- **Docker**: Containerization

### AI/ML
- **Z.ai**: Open-source LLM for summarization and prioritization
- **Sentence Transformers**: all-MiniLM-L6-v2 for embeddings (384 dimensions)
- **Celery**: Async task processing (optional)

## Offline-First Architecture

1. **Local Storage**: All data stored locally on device
2. **Sync Queue**: Changes queued for sync when online
3. **Conflict Resolution**: Last-write-wins strategy
4. **Background Sync**: Automatic sync when connection available

## Security Considerations

### Current (Development)
- No authentication
- No encryption
- SQLite local storage

### Production Recommendations
- JWT authentication
- HTTPS/TLS encryption
- Encrypted local storage
- Rate limiting
- Input validation
- CORS configuration
- Database backups

## Scalability

### Horizontal Scaling
- Stateless FastAPI servers behind load balancer
- PostgreSQL read replicas
- Milvus cluster for vector search
- Redis cluster for caching

### Vertical Scaling
- Increase server resources
- Database optimization
- Caching strategies
- Query optimization

## Performance Optimization

1. **Embeddings**: Pre-computed and cached
2. **Search**: Indexed vector search in Milvus
3. **Pagination**: Limit results per request
4. **Caching**: Redis for frequently accessed data
5. **Async Operations**: Background tasks with Celery

## Deployment Architecture

```
┌─────────────────────────────────────────┐
│         Load Balancer (Nginx)           │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│    FastAPI Instances (Multiple)         │
│  - Auto-scaling based on load           │
└─────────────────────────────────────────┘
              ↓
┌─────────────────────────────────────────┐
│    PostgreSQL (Primary + Replicas)      │
│    Redis Cluster                        │
│    Milvus Cluster                       │
│    MinIO Cluster                        │
└─────────────────────────────────────────┘
```

## Future Enhancements

1. **Real-time Sync**: WebSocket for live updates
2. **Collaborative Features**: Shared tasks/notes
3. **Advanced Analytics**: Usage insights
4. **Mobile Offline AI**: On-device embeddings and summarization
5. **Voice Commands**: Voice-to-text task creation
6. **Calendar Integration**: Sync with calendar apps
7. **Third-party Integrations**: Slack, Teams, etc.

