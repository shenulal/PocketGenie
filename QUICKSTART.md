# PocketGenie Quick Start

Get PocketGenie running in 5 minutes!

## Prerequisites

- Docker & Docker Compose installed
- Flutter SDK installed (for mobile)
- Git installed

## Option 1: Docker (Recommended for Backend)

### Start All Services

```bash
# Clone the repository
git clone https://github.com/shenulal/PocketGenie.git
cd PocketGenie

# Start all services
docker-compose up -d

# Wait for services to start (30-60 seconds)
docker-compose ps

# Check backend is running
curl http://localhost:8000/health
```

### Access Services

- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs
- **PostgreSQL**: localhost:5432
- **Redis**: localhost:6379
- **Milvus**: localhost:19530
- **MinIO**: http://localhost:9000

## Option 2: Local Backend Development

### Setup Backend

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run server
python -m uvicorn app.main:app --reload
```

Backend will be at: http://localhost:8000

## Setup Mobile App

### Install Flutter Dependencies

```bash
cd mobile
flutter pub get
```

### Run on Emulator/Device

```bash
# List available devices
flutter devices

# Run on default device
flutter run

# Or specify device
flutter run -d <device_id>
```

## Test the App

### 1. Create a Task

```bash
curl -X POST http://localhost:8000/api/v1/tasks \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Buy groceries",
    "priority": 1,
    "category": "shopping"
  }'
```

### 2. Create a Note

```bash
curl -X POST http://localhost:8000/api/v1/notes \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Meeting Notes",
    "content": "Discussed project timeline and deliverables"
  }'
```

### 3. Search

```bash
curl -X POST http://localhost:8000/api/v1/search/semantic \
  -H "Content-Type: application/json" \
  -d '{
    "query": "project deadline",
    "limit": 10
  }'
```

### 4. Summarize

```bash
curl -X POST http://localhost:8000/api/v1/ai/summarize \
  -H "Content-Type: application/json" \
  -d '{
    "content": "Long text to summarize...",
    "max_points": 5
  }'
```

## Using the Mobile App

1. **Home Screen**: View today's tasks and recent notes
2. **Tasks Tab**: Create, view, and manage tasks
3. **Notes Tab**: Create and view notes
4. **Search**: Search tasks and notes semantically
5. **Settings**: Configure app preferences

## Common Commands

### Backend

```bash
# View logs
docker-compose logs -f backend

# Stop services
docker-compose down

# Restart services
docker-compose restart

# Run tests
cd backend && pytest

# View API docs
open http://localhost:8000/docs
```

### Mobile

```bash
# Hot reload
Press 'r' in terminal

# Full restart
Press 'R' in terminal

# Build APK
flutter build apk

# Build iOS
flutter build ios

# Clean build
flutter clean && flutter pub get
```

## Troubleshooting

### Backend won't start

```bash
# Check if port 8000 is in use
lsof -i :8000

# Kill process using port
kill -9 <PID>

# Or use different port
python -m uvicorn app.main:app --port 8001 --reload
```

### Mobile app can't connect to backend

1. Check backend is running: `curl http://localhost:8000/health`
2. Update API URL in `mobile/lib/config/app_config.dart`
3. For Android emulator: Use `10.0.2.2` instead of `localhost`

### Docker services not starting

```bash
# Clean up
docker-compose down -v

# Rebuild
docker-compose build --no-cache

# Start fresh
docker-compose up -d
```

## Next Steps

1. **Read Documentation**: Check `/docs` folder
2. **Explore API**: Visit http://localhost:8000/docs
3. **Create Content**: Add tasks and notes
4. **Test Features**: Try search and summarization
5. **Contribute**: See CONTRIBUTING.md

## Documentation

- [Setup Guide](./docs/SETUP_GUIDE.md) - Detailed setup
- [API Documentation](./docs/API_DOCUMENTATION.md) - API reference
- [Architecture](./docs/ARCHITECTURE.md) - System design
- [Contributing](./docs/CONTRIBUTING.md) - How to contribute

## Support

- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **Docs**: `/docs` folder

## What's Next?

- [ ] Create your first task
- [ ] Add a note and see AI summary
- [ ] Try semantic search
- [ ] Explore API documentation
- [ ] Contribute to the project

---

**Enjoy using PocketGenie! 🚀**

For detailed setup instructions, see [SETUP_GUIDE.md](./docs/SETUP_GUIDE.md)

