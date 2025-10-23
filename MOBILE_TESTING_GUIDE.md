# PocketGenie - Mobile Testing Guide

Complete step-by-step guide to run and test PocketGenie on your mobile device.

---

## 📋 Prerequisites

Before starting, ensure you have:

### Required Software
- [ ] **Flutter SDK** (3.0+) - [Download](https://flutter.dev/docs/get-started/install)
- [ ] **Android Studio** or **Xcode** (for iOS)
- [ ] **Git** installed
- [ ] **Docker & Docker Compose** (for backend)
- [ ] **Python 3.8+** (for backend)

### Hardware
- [ ] Physical Android/iOS device OR emulator/simulator
- [ ] USB cable (for physical device)
- [ ] Computer with 8GB+ RAM

### Verify Installation
```bash
# Check Flutter
flutter --version

# Check Dart
dart --version

# Check Android/iOS setup
flutter doctor
```

---

## 🚀 Step 1: Clone the Repository

```bash
# Clone the project
git clone https://github.com/shenulal/PocketGenie.git
cd PocketGenie

# Verify structure
ls -la
# You should see: backend/, mobile/, docs/, docker-compose.yml, etc.
```

---

## 🔧 Step 2: Start the Backend Services

You have two options:

### Option A: Docker (Recommended - Easiest)

```bash
# Start all services
docker-compose up -d

# Wait 30-60 seconds for services to start
sleep 60

# Verify services are running
docker-compose ps

# Check backend health
curl http://localhost:8000/health
# Expected response: {"status":"ok"}
```

**Services started:**
- Backend API: http://localhost:8000
- PostgreSQL: localhost:5432
- Redis: localhost:6379
- Milvus: localhost:19530
- MinIO: http://localhost:9000

### Option B: Local Backend (Manual Setup)

```bash
# Navigate to backend
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run backend server
python -m uvicorn app.main:app --reload

# Backend will be at: http://localhost:8000
```

**Keep this terminal open** - the backend needs to keep running.

---

## 📱 Step 3: Setup Mobile App

### 3.1 Navigate to Mobile Directory

```bash
# Open new terminal/command prompt
cd PocketGenie/mobile
```

### 3.2 Install Flutter Dependencies

```bash
# Get all dependencies
flutter pub get

# This may take 2-5 minutes
```

### 3.3 Check Available Devices

```bash
# List all connected devices and emulators
flutter devices

# Example output:
# 2 connected devices:
# 
# Android (mobile)    • emulator-5554 • android-x86    • Android 11 (API 30)
# iPhone (mobile)     • iPhone 12     • ios            • iOS 15.0
```

---

## 📲 Step 4: Configure API Connection

### For Physical Device or Emulator on Same Network

**Option 1: Using localhost (Same Machine)**

If running backend on same machine:

```bash
# Edit mobile/lib/config/app_config.dart
# Line 3 should be:
static const String apiBaseUrl = 'http://localhost:8000/api/v1';
```

**For Android Emulator**, use special IP:
```dart
// For Android Emulator, use:
static const String apiBaseUrl = 'http://10.0.2.2:8000/api/v1';
```

**Option 2: Using Your Computer's IP Address**

Find your computer's IP:
```bash
# Windows
ipconfig
# Look for "IPv4 Address" (e.g., 192.168.x.x)

# macOS/Linux
ifconfig
# Look for "inet" address
```

Update the config:
```dart
// In mobile/lib/config/app_config.dart, line 3:
static const String apiBaseUrl = 'http://192.168.x.x:8000/api/v1';
// Replace 192.168.x.x with your actual IP
```

---

## ▶️ Step 5: Run on Mobile Device

### 5.1 Connect Physical Device (Optional)

**Android:**
```bash
# Enable USB Debugging on your Android phone
# Settings > Developer Options > USB Debugging

# Connect via USB
# Verify connection:
flutter devices
```

**iOS:**
```bash
# Connect via USB
# Trust the computer on your iPhone
# Verify connection:
flutter devices
```

### 5.2 Run the App

```bash
# Run on default device
flutter run

# Or specify device
flutter run -d <device_id>

# Example:
flutter run -d emulator-5554
```

**Wait for app to build and launch** (first build takes 2-5 minutes)

---

## ✅ Step 6: Test the App

### 6.1 Verify Backend Connection

1. Open the app on your device
2. Go to **Settings** screen
3. You should see:
   - API Status: Connected ✅
   - Backend URL: http://localhost:8000/api/v1 (or your IP)

### 6.2 Create a Task

1. Tap **Tasks** tab
2. Tap **+** button (floating action button)
3. Fill in:
   - **Title**: "Buy groceries"
   - **Priority**: High
   - **Category**: Shopping
4. Tap **Save**
5. Verify task appears in list

### 6.3 Create a Note

1. Tap **Notes** tab
2. Tap **+** button
3. Fill in:
   - **Title**: "Meeting Notes"
   - **Content**: "Discussed project timeline and deliverables"
4. Tap **Save**
5. Verify note appears in list

### 6.4 Test AI Summarization

1. Go to **Notes** tab
2. Tap on a note
3. Look for **AI Summary** section
4. If summary appears, AI integration is working ✅

### 6.5 Test Semantic Search

1. Tap **Search** tab
2. Type: "project deadline"
3. Tap search button
4. Verify results appear from tasks and notes

### 6.6 Test Offline Functionality

1. **Disable internet** on your device
2. Create a new task
3. Task should save locally ✅
4. **Re-enable internet**
5. Task should sync to backend

---

## 🧪 Step 7: Run Backend Tests (Optional)

```bash
# Navigate to backend
cd backend

# Activate virtual environment (if not already)
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Run tests
pytest

# Run with verbose output
pytest -v

# Run specific test file
pytest tests/test_tasks.py -v
```

---

## 🐛 Troubleshooting

### Issue: "flutter: command not found"

**Solution:**
```bash
# Add Flutter to PATH
# Windows: Add C:\path\to\flutter\bin to PATH
# macOS/Linux: Add to ~/.bashrc or ~/.zshrc:
export PATH="$PATH:/path/to/flutter/bin"

# Verify
flutter --version
```

### Issue: App can't connect to backend

**Check 1: Backend is running**
```bash
# Test backend
curl http://localhost:8000/health
# Should return: {"status":"ok"}
```

**Check 2: Correct API URL**
```bash
# Edit mobile/lib/config/app_config.dart
# For Android Emulator: http://10.0.2.2:8000/api/v1
# For Physical Device: http://YOUR_IP:8000/api/v1
# For Same Machine: http://localhost:8000/api/v1
```

**Check 3: Firewall**
```bash
# Ensure port 8000 is not blocked by firewall
# Windows: Check Windows Defender Firewall
# macOS: Check System Preferences > Security & Privacy
```

### Issue: "No devices found"

**Solution:**
```bash
# List devices
flutter devices

# If no devices:
# 1. Start Android Emulator from Android Studio
# 2. Or connect physical device via USB
# 3. Enable USB Debugging (Android)
# 4. Trust computer (iOS)
```

### Issue: Build fails with dependency errors

**Solution:**
```bash
# Clean and rebuild
flutter clean
flutter pub get
flutter run
```

### Issue: Port 8000 already in use

**Solution:**
```bash
# Find process using port 8000
# Windows:
netstat -ano | findstr :8000

# macOS/Linux:
lsof -i :8000

# Kill process (get PID from above)
# Windows:
taskkill /PID <PID> /F

# macOS/Linux:
kill -9 <PID>

# Or use different port:
python -m uvicorn app.main:app --port 8001 --reload
# Then update app_config.dart to use port 8001
```

### Issue: Docker services not starting

**Solution:**
```bash
# Check Docker is running
docker ps

# Clean up and restart
docker-compose down -v
docker-compose up -d

# Check logs
docker-compose logs backend
```

---

## 📊 Testing Checklist

Use this checklist to verify all features work:

### Basic Functionality
- [ ] App launches without errors
- [ ] Backend connection shows as connected
- [ ] Can create a task
- [ ] Can create a note
- [ ] Can view task list
- [ ] Can view note list

### Task Management
- [ ] Create task with all fields
- [ ] Edit task
- [ ] Delete task
- [ ] Mark task as complete
- [ ] Filter tasks by category
- [ ] Filter tasks by priority

### Note Management
- [ ] Create note
- [ ] Edit note
- [ ] Delete note
- [ ] View note details
- [ ] AI summary appears (if backend supports)

### Search
- [ ] Search for tasks
- [ ] Search for notes
- [ ] Search returns relevant results
- [ ] Can filter search results

### Offline Features
- [ ] Create task without internet
- [ ] Create note without internet
- [ ] Data persists locally
- [ ] Data syncs when online

### UI/UX
- [ ] App is responsive
- [ ] Navigation works smoothly
- [ ] Buttons are clickable
- [ ] Forms validate input
- [ ] Error messages are clear

---

## 🎯 Common Testing Scenarios

### Scenario 1: Full Feature Test (15 minutes)

```
1. Create 3 tasks with different priorities
2. Create 2 notes with content
3. Search for a task
4. Mark a task as complete
5. Edit a note
6. Delete a task
7. Verify all changes persist
```

### Scenario 2: Offline Test (10 minutes)

```
1. Disable internet on device
2. Create a task
3. Create a note
4. Verify they appear in lists
5. Enable internet
6. Verify data syncs to backend
```

### Scenario 3: Performance Test (5 minutes)

```
1. Create 20 tasks
2. Create 10 notes
3. Measure app responsiveness
4. Test search performance
5. Check memory usage
```

---

## 📈 Performance Metrics to Monitor

While testing, monitor these metrics:

| Metric | Expected | Tool |
|--------|----------|------|
| App Startup | <2 seconds | Device timer |
| Task Creation | <500ms | Network tab |
| Search Response | <500ms | Network tab |
| Memory Usage | <100MB | Device settings |
| Battery Impact | Minimal | Device battery |

---

## 🔍 Debugging Tips

### Enable Debug Logging

```dart
// In mobile/lib/services/api_service.dart
// Uncomment debug logging to see API calls
```

### View Network Requests

```bash
# In terminal where flutter run is active:
# Press 'w' to show widget tree
# Press 'L' to show layers
# Press 'P' to show performance overlay
```

### Check Device Logs

```bash
# Android
adb logcat

# iOS
xcrun simctl spawn booted log stream --predicate 'process == "Runner"'
```

---

## 📚 Next Steps After Testing

1. **Report Issues**: Create GitHub issues for any bugs found
2. **Contribute**: See [CONTRIBUTING.md](./docs/CONTRIBUTING.md)
3. **Explore Code**: Review backend and mobile code
4. **Customize**: Modify app for your needs
5. **Deploy**: Build APK/IPA for distribution

---

## 📞 Support

- **Documentation**: See `/docs` folder
- **Issues**: GitHub Issues
- **Discussions**: GitHub Discussions
- **API Docs**: http://localhost:8000/docs

---

## 🎉 Success!

If you've completed all steps and the app is running on your device, congratulations! 🎊

You now have a fully functional AI-powered productivity assistant running locally!

---

**Happy testing! 🚀**

