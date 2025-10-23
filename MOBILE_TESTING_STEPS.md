# 📱 PocketGenie - Step-by-Step Mobile Testing Guide

Complete walkthrough to run PocketGenie on your mobile device.

---

## 🎯 Overview

This guide will help you:
1. ✅ Setup the backend services
2. ✅ Configure the mobile app
3. ✅ Run the app on your device
4. ✅ Test all features
5. ✅ Troubleshoot issues

**Total Time: 15-30 minutes**

---

## 📋 Prerequisites Checklist

Before starting, verify you have:

```bash
# Check Flutter
flutter --version
# Should show: Flutter 3.0+

# Check Dart
dart --version
# Should show: Dart 2.17+

# Check Git
git --version
# Should show: git version 2.x+

# Check Docker (if using Docker)
docker --version
docker-compose --version

# Check Python (if using local backend)
python --version
# Should show: Python 3.8+
```

If any are missing, install them first.

---

## 🔴 STEP 1: Clone the Repository

**Time: 2 minutes**

```bash
# Clone the project
git clone https://github.com/shenulal/PocketGenie.git

# Navigate to project
cd PocketGenie

# Verify structure
ls -la
```

You should see:
- `backend/` - FastAPI backend
- `mobile/` - Flutter app
- `docs/` - Documentation
- `docker-compose.yml` - Infrastructure
- `README.md` - Project info

---

## 🟠 STEP 2: Start Backend Services

**Time: 5-10 minutes**

### Choose One Option:

#### Option A: Docker (Recommended - Easiest)

**Open Terminal 1:**

```bash
# Navigate to project root
cd PocketGenie

# Start all services
docker-compose up -d

# Wait 30-60 seconds for services to start
echo "Waiting for services..."
sleep 60

# Verify services are running
docker-compose ps

# Check backend health
curl http://localhost:8000/health
```

**Expected output:**
```json
{"status":"ok"}
```

**Services running:**
- Backend API: http://localhost:8000
- PostgreSQL: localhost:5432
- Redis: localhost:6379
- Milvus: localhost:19530
- MinIO: http://localhost:9000

---

#### Option B: Local Python Backend

**Open Terminal 1:**

```bash
# Navigate to backend
cd PocketGenie/backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run backend
python -m uvicorn app.main:app --reload
```

**Expected output:**
```
INFO:     Uvicorn running on http://127.0.0.1:8000
```

**Keep this terminal open** - backend must keep running.

---

## 🟡 STEP 3: Setup Mobile App

**Time: 3-5 minutes**

**Open Terminal 2 (new terminal):**

```bash
# Navigate to mobile directory
cd PocketGenie/mobile

# Get Flutter dependencies
flutter pub get

# This may take 2-5 minutes
# Wait for "Running "flutter pub get"..." to complete
```

**Expected output:**
```
Running "flutter pub get" in mobile...
Running "flutter pub get" in mobile... 2.5s
```

---

## 🟢 STEP 4: Check Available Devices

**Time: 1 minute**

```bash
# List all available devices
flutter devices

# Example output:
# 2 connected devices:
# 
# Android (mobile)    • emulator-5554 • android-x86    • Android 11 (API 30)
# iPhone (mobile)     • iPhone 12     • ios            • iOS 15.0
```

### If No Devices Found:

**Android Emulator:**
1. Open Android Studio
2. Click "AVD Manager"
3. Click "Create Virtual Device"
4. Select device and Android version
5. Click "Start"

**iOS Simulator:**
```bash
# Open iOS simulator
open -a Simulator
```

**Physical Device:**
1. Connect via USB
2. Enable USB Debugging (Android) or Trust Computer (iOS)
3. Run `flutter devices` again

---

## 🔵 STEP 5: Configure API Connection

**Time: 2 minutes**

Edit `mobile/lib/config/app_config.dart`:

```bash
# Open the file
# Windows: Use Notepad or VS Code
# macOS/Linux: Use nano or VS Code
nano mobile/lib/config/app_config.dart
```

**Find line 3:**
```dart
static const String apiBaseUrl = 'http://localhost:8000/api/v1';
```

### Choose Configuration Based on Your Setup:

**Same Machine (Backend on same computer):**
```dart
static const String apiBaseUrl = 'http://localhost:8000/api/v1';
```

**Android Emulator:**
```dart
static const String apiBaseUrl = 'http://10.0.2.2:8000/api/v1';
```

**Physical Device (Replace with your IP):**
```bash
# Find your computer's IP:
# Windows:
ipconfig
# Look for "IPv4 Address" (e.g., 192.168.1.100)

# macOS/Linux:
ifconfig
# Look for "inet" address
```

Then update:
```dart
static const String apiBaseUrl = 'http://192.168.1.100:8000/api/v1';
// Replace 192.168.1.100 with your actual IP
```

**Save the file.**

---

## 🟣 STEP 6: Run the App

**Time: 2-5 minutes (first run takes longer)**

**In Terminal 2:**

```bash
# Make sure you're in mobile directory
cd PocketGenie/mobile

# Run the app
flutter run

# Or specify device
flutter run -d emulator-5554
```

**Wait for build to complete:**
```
Launching lib/main.dart on Android SDK built for x86 in debug mode...
...
Running "flutter pub get" in mobile...
...
Building APK...
...
✓ Built build/app/outputs/flutter-app.apk
Installing and launching...
```

**App should launch on your device!** 🎉

---

## ✅ STEP 7: Verify Backend Connection

**Time: 1 minute**

1. **Open the app** on your device
2. **Tap Settings** (bottom right)
3. **Look for API Status:**
   - ✅ Connected - Backend is working
   - ❌ Disconnected - Check configuration

If disconnected:
- Verify backend is running: `curl http://localhost:8000/health`
- Check API URL in `app_config.dart`
- Verify firewall allows port 8000

---

## 🧪 STEP 8: Test Features

**Time: 10 minutes**

### Test 1: Create a Task

1. Tap **Tasks** tab (bottom navigation)
2. Tap **+** button (floating action button)
3. Fill in:
   - **Title**: "Buy groceries"
   - **Priority**: Select "High"
   - **Category**: "Shopping"
4. Tap **Save**
5. ✅ Task should appear in list

### Test 2: Create a Note

1. Tap **Notes** tab
2. Tap **+** button
3. Fill in:
   - **Title**: "Meeting Notes"
   - **Content**: "Discussed project timeline and deliverables"
4. Tap **Save**
5. ✅ Note should appear in list

### Test 3: Search

1. Tap **Search** tab
2. Type: "project"
3. Tap search button
4. ✅ Should see matching tasks and notes

### Test 4: Mark Task Complete

1. Go to **Tasks** tab
2. Tap on a task
3. Tap **Mark Complete** button
4. ✅ Task should show as completed

### Test 5: Edit Task

1. Go to **Tasks** tab
2. Tap on a task
3. Tap **Edit** button
4. Change title to "Updated Task"
5. Tap **Save**
6. ✅ Task should update

### Test 6: Delete Task

1. Go to **Tasks** tab
2. Tap on a task
3. Tap **Delete** button
4. Confirm deletion
5. ✅ Task should disappear

### Test 7: Offline Mode

1. **Disable internet** on your device
2. Create a new task: "Offline Task"
3. ✅ Task should save locally
4. **Re-enable internet**
5. ✅ Task should sync to backend

### Test 8: AI Summarization (if enabled)

1. Go to **Notes** tab
2. Tap on a note
3. Look for **AI Summary** section
4. ✅ Summary should appear (if backend supports)

---

## 📊 Testing Checklist

Mark off as you complete each test:

```
Basic Functionality
- [ ] App launches without errors
- [ ] Backend connection shows as connected
- [ ] Can create a task
- [ ] Can create a note
- [ ] Can view task list
- [ ] Can view note list

Task Management
- [ ] Create task with all fields
- [ ] Edit task
- [ ] Delete task
- [ ] Mark task as complete
- [ ] Filter tasks by category
- [ ] Filter tasks by priority

Note Management
- [ ] Create note
- [ ] Edit note
- [ ] Delete note
- [ ] View note details
- [ ] AI summary appears

Search
- [ ] Search for tasks
- [ ] Search for notes
- [ ] Search returns relevant results
- [ ] Can filter search results

Offline Features
- [ ] Create task without internet
- [ ] Create note without internet
- [ ] Data persists locally
- [ ] Data syncs when online

UI/UX
- [ ] App is responsive
- [ ] Navigation works smoothly
- [ ] Buttons are clickable
- [ ] Forms validate input
- [ ] Error messages are clear
```

---

## 🐛 Troubleshooting

### Problem: "flutter: command not found"

**Solution:**
```bash
# Add Flutter to PATH
# Windows: Add C:\path\to\flutter\bin to PATH environment variable
# macOS/Linux: Add to ~/.bashrc or ~/.zshrc:
export PATH="$PATH:/path/to/flutter/bin"

# Reload shell
source ~/.bashrc  # or ~/.zshrc
```

---

### Problem: App can't connect to backend

**Check 1: Backend is running**
```bash
curl http://localhost:8000/health
# Should return: {"status":"ok"}
```

**Check 2: Correct API URL**
```bash
# Edit mobile/lib/config/app_config.dart
# Verify line 3 has correct URL
```

**Check 3: Firewall**
- Windows: Check Windows Defender Firewall
- macOS: Check System Preferences > Security & Privacy
- Ensure port 8000 is allowed

---

### Problem: "No devices found"

**Solution:**
```bash
# Start Android Emulator from Android Studio
# Or connect physical device via USB
# Then run:
flutter devices
```

---

### Problem: Build fails with dependency errors

**Solution:**
```bash
# Clean and rebuild
flutter clean
flutter pub get
flutter run
```

---

### Problem: Port 8000 already in use

**Solution:**
```bash
# Find process using port
# Windows:
netstat -ano | findstr :8000

# macOS/Linux:
lsof -i :8000

# Kill process (replace PID)
# Windows:
taskkill /PID 1234 /F

# macOS/Linux:
kill -9 1234

# Or use different port:
python -m uvicorn app.main:app --port 8001 --reload
# Then update app_config.dart to use port 8001
```

---

### Problem: Docker services not starting

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

## 🎯 Success Indicators

You've successfully completed testing when:

✅ App launches without errors
✅ Backend connection shows as connected
✅ Can create and view tasks
✅ Can create and view notes
✅ Search returns results
✅ Offline mode works
✅ All UI elements are responsive

---

## 📚 Next Steps

1. **Explore Code**: Review `mobile/lib/` and `backend/app/`
2. **Read Documentation**: Check `/docs` folder
3. **Report Issues**: Create GitHub issues for bugs
4. **Contribute**: See [CONTRIBUTING.md](./docs/CONTRIBUTING.md)
5. **Customize**: Modify app for your needs

---

## 📞 Support

- **Full Guide**: [MOBILE_TESTING_GUIDE.md](./MOBILE_TESTING_GUIDE.md)
- **Quick Reference**: [QUICK_REFERENCE.md](./QUICK_REFERENCE.md)
- **Setup Guide**: [docs/SETUP_GUIDE.md](./docs/SETUP_GUIDE.md)
- **API Docs**: [docs/API_DOCUMENTATION.md](./docs/API_DOCUMENTATION.md)

---

## 🎉 Congratulations!

You've successfully set up and tested PocketGenie on your mobile device! 🚀

**Enjoy using PocketGenie!**

