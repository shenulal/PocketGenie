# PocketGenie - Quick Reference Card

## ⚡ 5-Minute Quick Start

### Terminal 1: Start Backend
```bash
# Option A: Docker (Easiest)
docker-compose up -d

# Option B: Local Python
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### Terminal 2: Run Mobile App
```bash
cd mobile
flutter pub get
flutter run
```

**That's it! App should launch in 2-5 minutes.**

---

## 🔧 Configuration

### API URL Configuration
Edit `mobile/lib/config/app_config.dart` line 3:

```dart
// Same machine
static const String apiBaseUrl = 'http://localhost:8000/api/v1';

// Android Emulator
static const String apiBaseUrl = 'http://10.0.2.2:8000/api/v1';

// Physical device (replace with your IP)
static const String apiBaseUrl = 'http://192.168.1.100:8000/api/v1';
```

**Find your IP:**
```bash
# Windows
ipconfig

# macOS/Linux
ifconfig
```

---

## 📱 Device Setup

### Android Emulator
```bash
# List devices
flutter devices

# Run on specific device
flutter run -d emulator-5554
```

### Physical Android Device
1. Enable USB Debugging: Settings > Developer Options > USB Debugging
2. Connect via USB
3. Run: `flutter run`

### iOS Simulator
```bash
# Open simulator
open -a Simulator

# Run app
flutter run
```

### Physical iOS Device
1. Connect via USB
2. Trust computer on device
3. Run: `flutter run`

---

## ✅ Testing Checklist

- [ ] Backend running: `curl http://localhost:8000/health`
- [ ] App launches without errors
- [ ] API connection shows as connected in Settings
- [ ] Can create a task
- [ ] Can create a note
- [ ] Can search tasks/notes
- [ ] Can mark task as complete
- [ ] Offline mode works (disable internet, create task, re-enable)

---

## 🐛 Common Issues & Fixes

| Issue | Fix |
|-------|-----|
| "flutter: command not found" | Add Flutter to PATH |
| App can't connect to backend | Check API URL in app_config.dart |
| Port 8000 in use | `kill -9 <PID>` or use different port |
| No devices found | Start emulator or connect physical device |
| Build fails | `flutter clean && flutter pub get` |
| Docker won't start | `docker-compose down -v && docker-compose up -d` |

---

## 📊 Useful Commands

### Backend
```bash
# View logs
docker-compose logs -f backend

# Stop services
docker-compose down

# Run tests
cd backend && pytest

# View API docs
curl http://localhost:8000/docs
```

### Mobile
```bash
# Hot reload (while running)
Press 'r'

# Full restart
Press 'R'

# Build APK
flutter build apk

# Build iOS
flutter build ios

# Clean build
flutter clean && flutter pub get
```

---

## 🎯 Feature Testing

### Create Task
1. Tap Tasks tab
2. Tap + button
3. Fill: Title, Priority, Category
4. Tap Save

### Create Note
1. Tap Notes tab
2. Tap + button
3. Fill: Title, Content
4. Tap Save

### Search
1. Tap Search tab
2. Type query (e.g., "project deadline")
3. View results

### Test Offline
1. Disable internet
2. Create task/note
3. Enable internet
4. Verify sync

---

## 📈 Performance Targets

| Metric | Target |
|--------|--------|
| App Startup | <2 seconds |
| Task Creation | <500ms |
| Search | <500ms |
| Memory | <100MB |

---

## 🔗 Important URLs

| Service | URL |
|---------|-----|
| Backend API | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |
| PostgreSQL | localhost:5432 |
| Redis | localhost:6379 |
| Milvus | localhost:19530 |
| MinIO | http://localhost:9000 |

---

## 📚 Documentation

- **Full Guide**: [MOBILE_TESTING_GUIDE.md](./MOBILE_TESTING_GUIDE.md)
- **Setup Guide**: [docs/SETUP_GUIDE.md](./docs/SETUP_GUIDE.md)
- **API Docs**: [docs/API_DOCUMENTATION.md](./docs/API_DOCUMENTATION.md)
- **Architecture**: [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)

---

## 🚀 Next Steps

1. ✅ Start backend
2. ✅ Run mobile app
3. ✅ Test features
4. ✅ Create tasks/notes
5. ✅ Try search
6. ✅ Test offline mode

---

**Happy testing! 🎉**

