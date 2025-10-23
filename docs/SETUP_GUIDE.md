# PocketGenie Setup Guide

## Prerequisites

### System Requirements
- **OS**: Windows, macOS, or Linux
- **RAM**: 4GB minimum (8GB recommended)
- **Disk Space**: 5GB for development environment

### Required Software

1. **Git**
   - Download: https://git-scm.com/
   - Verify: `git --version`

2. **Docker & Docker Compose**
   - Download: https://www.docker.com/products/docker-desktop
   - Verify: `docker --version` and `docker-compose --version`

3. **Flutter SDK** (for mobile development)
   - Download: https://flutter.dev/docs/get-started/install
   - Verify: `flutter --version`

4. **Python 3.9+** (for backend development)
   - Download: https://www.python.org/downloads/
   - Verify: `python --version`

5. **Android Studio** (for Android emulator)
   - Download: https://developer.android.com/studio
   - Or use iOS Simulator on macOS

## Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/yourusername/PocketGenie.git
cd PocketGenie
```

### 2. Backend Setup (Option A: Docker)

```bash
# Start all services with Docker Compose
docker-compose up -d

# Verify services are running
docker-compose ps

# View logs
docker-compose logs -f backend
```

Services will be available at:
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs
- PostgreSQL: localhost:5432
- Redis: localhost:6379
- Milvus: localhost:19530
- MinIO: http://localhost:9000

### 3. Backend Setup (Option B: Local Development)

```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run migrations (if using PostgreSQL)
alembic upgrade head

# Start the server
python -m uvicorn app.main:app --reload
```

Backend will be available at: http://localhost:8000

### 4. Mobile App Setup

```bash
cd mobile

# Get Flutter dependencies
flutter pub get

# Run on emulator/device
flutter run

# Or build for specific platform
flutter run -d android  # Android
flutter run -d ios      # iOS
```

## Configuration

### Backend Configuration

Create `backend/.env` file:

```env
# App
APP_NAME=PocketGenie
DEBUG=True

# Database
DATABASE_URL=sqlite:///./pocketgenie.db
# Or for PostgreSQL:
# DATABASE_URL=postgresql://user:password@localhost:5432/pocketgenie

# AI/LLM
ZEPHYR_API_URL=http://localhost:8001
EMBEDDING_MODEL=sentence-transformers/all-MiniLM-L6-v2

# Milvus
MILVUS_HOST=localhost
MILVUS_PORT=19530

# MinIO
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin

# Redis
REDIS_URL=redis://localhost:6379
```

### Mobile Configuration

Edit `mobile/lib/config/app_config.dart`:

```dart
class AppConfig {
  static const String apiBaseUrl = 'http://localhost:8000/api/v1';
  static const bool enableCloudSync = false;
  static const bool enableVoiceInput = true;
  static const bool enableAISummarization = true;
}
```

## Running Tests

### Backend Tests

```bash
cd backend

# Run all tests
pytest

# Run specific test file
pytest tests/test_tasks.py

# Run with coverage
pytest --cov=app tests/
```

### Mobile Tests

```bash
cd mobile

# Run all tests
flutter test

# Run specific test file
flutter test test/models/task_model_test.dart
```

## Development Workflow

### Backend Development

1. Make changes to backend code
2. Server auto-reloads with `--reload` flag
3. Test changes at http://localhost:8000/docs
4. Run tests: `pytest`

### Mobile Development

1. Make changes to Flutter code
2. Hot reload: Press `r` in terminal
3. Full restart: Press `R` in terminal
4. Test on emulator/device

## Troubleshooting

### Docker Issues

```bash
# Clean up all containers
docker-compose down -v

# Rebuild images
docker-compose build --no-cache

# Start fresh
docker-compose up -d
```

### Backend Issues

```bash
# Clear Python cache
find . -type d -name __pycache__ -exec rm -r {} +

# Reinstall dependencies
pip install --upgrade -r requirements.txt

# Check database
sqlite3 pocketgenie.db ".tables"
```

### Mobile Issues

```bash
# Clean build
flutter clean

# Get dependencies again
flutter pub get

# Run on specific device
flutter devices
flutter run -d <device_id>
```

## Next Steps

1. **Explore API**: Visit http://localhost:8000/docs
2. **Create Tasks**: Use the mobile app to create tasks
3. **Test AI Features**: Create notes to see AI summarization
4. **Semantic Search**: Try searching for tasks/notes
5. **Multi-Device Sync**: Enable cloud sync in settings

## Documentation

- [API Documentation](./API_DOCUMENTATION.md)
- [Database Schema](./DATABASE_SCHEMA.md)
- [Architecture Guide](./ARCHITECTURE.md)
- [Contributing Guide](./CONTRIBUTING.md)

## Support

For issues and questions:
1. Check existing issues on GitHub
2. Create a new issue with detailed description
3. Join our community discussions

## License

MIT License - See LICENSE file for details

