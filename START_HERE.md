# 🚀 PocketGenie - START HERE

**Welcome!** This is your entry point to running PocketGenie on your mobile device.

---

## 📱 What You're About to Do

You'll run a complete AI-powered productivity app on your phone with:
- ✅ Task management
- ✅ Note-taking
- ✅ AI summarization
- ✅ Semantic search
- ✅ Offline functionality

**Time Required: 15-30 minutes**

---

## 🎯 Quick Overview

```
Your Computer                    Your Mobile Device
┌─────────────────┐             ┌──────────────────┐
│  Backend API    │◄────────────►│  Flutter App     │
│  (FastAPI)      │             │  (iOS/Android)   │
│  Port 8000      │             │                  │
└─────────────────┘             └──────────────────┘
       ▲
       │
   ┌───┴────────────────┐
   │  Services          │
   ├────────────────────┤
   │ PostgreSQL         │
   │ Redis              │
   │ Milvus (Vector DB) │
   │ MinIO (Storage)    │
   └────────────────────┘
```

---

## 📚 Documentation Files

Choose based on your needs:

| File | Purpose | Time |
|------|---------|------|
| **[MOBILE_TESTING_STEPS.md](./MOBILE_TESTING_STEPS.md)** | **👈 START HERE** - Step-by-step guide | 30 min |
| [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) | Quick commands and fixes | 5 min |
| [MOBILE_TESTING_GUIDE.md](./MOBILE_TESTING_GUIDE.md) | Detailed testing guide | 20 min |
| [QUICKSTART.md](./QUICKSTART.md) | General quick start | 5 min |
| [docs/SETUP_GUIDE.md](./docs/SETUP_GUIDE.md) | Detailed setup | 15 min |

---

## ⚡ Super Quick Start (5 minutes)

If you're experienced with development:

```bash
# Terminal 1: Start backend
docker-compose up -d

# Terminal 2: Run mobile app
cd mobile
flutter pub get
flutter run
```

**Done!** App should launch in 2-5 minutes.

---

## 📋 Step-by-Step (Recommended)

### Step 1: Prerequisites (5 min)
```bash
flutter --version      # Should show 3.0+
dart --version         # Should show 2.17+
git --version          # Should show 2.x+
docker --version       # If using Docker
```

### Step 2: Clone Repository (2 min)
```bash
git clone https://github.com/shenulal/PocketGenie.git
cd PocketGenie
```

### Step 3: Start Backend (5 min)

**Option A: Docker (Easiest)**
```bash
docker-compose up -d
sleep 60
curl http://localhost:8000/health
```

**Option B: Local Python**
```bash
cd backend
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

### Step 4: Setup Mobile (5 min)
```bash
cd mobile
flutter pub get
flutter devices  # Check available devices
```

### Step 5: Configure API (2 min)

Edit `mobile/lib/config/app_config.dart` line 3:

```dart
// For same machine:
static const String apiBaseUrl = 'http://localhost:8000/api/v1';

// For Android Emulator:
static const String apiBaseUrl = 'http://10.0.2.2:8000/api/v1';

// For physical device (replace with your IP):
static const String apiBaseUrl = 'http://192.168.1.100:8000/api/v1';
```

### Step 6: Run App (2-5 min)
```bash
flutter run
```

### Step 7: Test Features (5 min)
- Create a task
- Create a note
- Try search
- Test offline mode

---

## 🎯 What to Test

Once the app is running:

### ✅ Basic Tests
1. **Create Task**: Tap Tasks → + → Fill form → Save
2. **Create Note**: Tap Notes → + → Fill form → Save
3. **Search**: Tap Search → Type query → View results
4. **Offline**: Disable internet → Create task → Re-enable → Verify sync

### ✅ Advanced Tests
1. **Edit Task**: Tap task → Edit → Change title → Save
2. **Delete Task**: Tap task → Delete → Confirm
3. **Mark Complete**: Tap task → Mark Complete
4. **AI Summary**: View note → Check AI summary section

---

## 🐛 Common Issues

| Issue | Fix |
|-------|-----|
| "flutter: command not found" | Add Flutter to PATH |
| App can't connect | Check API URL in app_config.dart |
| Port 8000 in use | Kill process or use different port |
| No devices | Start emulator or connect physical device |
| Build fails | `flutter clean && flutter pub get` |

**See [QUICK_REFERENCE.md](./QUICK_REFERENCE.md) for more fixes.**

---

## 📱 Device Options

### Android Emulator (Easiest)
1. Open Android Studio
2. Click AVD Manager
3. Create/Start virtual device
4. Run `flutter run`

### iOS Simulator (macOS only)
```bash
open -a Simulator
flutter run
```

### Physical Device
1. Connect via USB
2. Enable USB Debugging (Android) or Trust (iOS)
3. Run `flutter run`

---

## 🔗 Important URLs

Once running:

| Service | URL |
|---------|-----|
| Backend API | http://localhost:8000 |
| API Docs | http://localhost:8000/docs |
| PostgreSQL | localhost:5432 |
| Redis | localhost:6379 |

---

## 📊 Expected Performance

| Action | Time |
|--------|------|
| App startup | <2 seconds |
| Create task | <500ms |
| Search | <500ms |
| Offline sync | <1 second |

---

## ✨ Features You'll Test

- ✅ **Task Management**: Create, edit, delete, complete tasks
- ✅ **Note-Taking**: Create and manage notes
- ✅ **AI Features**: Summarization and prioritization
- ✅ **Semantic Search**: Natural language search
- ✅ **Offline Mode**: Full functionality without internet
- ✅ **Sync**: Automatic sync when online
- ✅ **UI**: Material Design 3 with dark mode

---

## 🎓 Learning Path

1. **Get it running** (this guide)
2. **Test features** (MOBILE_TESTING_STEPS.md)
3. **Explore code** (backend/app/, mobile/lib/)
4. **Read architecture** (docs/ARCHITECTURE.md)
5. **Contribute** (docs/CONTRIBUTING.md)

---

## 📞 Need Help?

1. **Quick answers**: [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)
2. **Detailed guide**: [MOBILE_TESTING_STEPS.md](./MOBILE_TESTING_STEPS.md)
3. **Full documentation**: [docs/](./docs/)
4. **API reference**: [docs/API_DOCUMENTATION.md](./docs/API_DOCUMENTATION.md)

---

## 🚀 Ready to Start?

### Choose Your Path:

**👉 I want step-by-step instructions**
→ Read [MOBILE_TESTING_STEPS.md](./MOBILE_TESTING_STEPS.md)

**👉 I want quick commands**
→ Read [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)

**👉 I want detailed information**
→ Read [MOBILE_TESTING_GUIDE.md](./MOBILE_TESTING_GUIDE.md)

**👉 I'm experienced, just give me the basics**
→ See "Super Quick Start" above

---

## ✅ Success Checklist

You're done when:
- [ ] Backend is running
- [ ] Mobile app launches
- [ ] Can create tasks
- [ ] Can create notes
- [ ] Search works
- [ ] Offline mode works
- [ ] All features are responsive

---

## 🎉 Next Steps

After testing:
1. Explore the code
2. Read the documentation
3. Report any issues
4. Contribute improvements
5. Customize for your needs

---

## 📄 Quick Links

- **Main Docs**: [README.md](./README.md)
- **Setup Guide**: [docs/SETUP_GUIDE.md](./docs/SETUP_GUIDE.md)
- **API Docs**: [docs/API_DOCUMENTATION.md](./docs/API_DOCUMENTATION.md)
- **Architecture**: [docs/ARCHITECTURE.md](./docs/ARCHITECTURE.md)
- **Contributing**: [docs/CONTRIBUTING.md](./docs/CONTRIBUTING.md)

---

## 🎯 TL;DR

```bash
# Terminal 1
docker-compose up -d

# Terminal 2
cd mobile && flutter pub get && flutter run

# Then test in the app!
```

---

**Happy testing! 🚀**

**👉 Next: Read [MOBILE_TESTING_STEPS.md](./MOBILE_TESTING_STEPS.md)**

