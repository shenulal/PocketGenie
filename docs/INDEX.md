# PocketGenie Documentation Index

Welcome to PocketGenie! This index will help you navigate all available documentation.

## 📚 Getting Started

### For New Users
1. **[QUICKSTART.md](../QUICKSTART.md)** - Get running in 5 minutes
2. **[SETUP_GUIDE.md](./SETUP_GUIDE.md)** - Detailed setup instructions
3. **[README.md](../README.md)** - Project overview and features

### For Developers
1. **[ARCHITECTURE.md](./ARCHITECTURE.md)** - System design and components
2. **[API_DOCUMENTATION.md](./API_DOCUMENTATION.md)** - API reference
3. **[DATABASE_SCHEMA.md](./DATABASE_SCHEMA.md)** - Database design
4. **[CONTRIBUTING.md](./CONTRIBUTING.md)** - How to contribute

## 📖 Documentation Files

### Project Documentation

| File | Purpose | Audience |
|------|---------|----------|
| [PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md) | Complete project overview | Everyone |
| [QUICKSTART.md](../QUICKSTART.md) | Quick start guide | New users |
| [SETUP_GUIDE.md](./SETUP_GUIDE.md) | Installation & setup | Developers |
| [README.md](../README.md) | Main project documentation | Everyone |

### Technical Documentation

| File | Purpose | Audience |
|------|---------|----------|
| [ARCHITECTURE.md](./ARCHITECTURE.md) | System architecture | Developers |
| [API_DOCUMENTATION.md](./API_DOCUMENTATION.md) | API endpoints & examples | Backend developers |
| [DATABASE_SCHEMA.md](./DATABASE_SCHEMA.md) | Database design | Database developers |
| [CONTRIBUTING.md](./CONTRIBUTING.md) | Contribution guidelines | Contributors |

## 🚀 Quick Links

### Setup & Installation
- **Docker Setup**: See [SETUP_GUIDE.md](./SETUP_GUIDE.md#docker-setup)
- **Local Backend**: See [SETUP_GUIDE.md](./SETUP_GUIDE.md#local-backend-setup)
- **Mobile App**: See [SETUP_GUIDE.md](./SETUP_GUIDE.md#mobile-app-setup)

### API Reference
- **Tasks Endpoints**: See [API_DOCUMENTATION.md](./API_DOCUMENTATION.md#tasks)
- **Notes Endpoints**: See [API_DOCUMENTATION.md](./API_DOCUMENTATION.md#notes)
- **Search Endpoints**: See [API_DOCUMENTATION.md](./API_DOCUMENTATION.md#search)
- **AI Endpoints**: See [API_DOCUMENTATION.md](./API_DOCUMENTATION.md#ai)

### Architecture
- **System Overview**: See [ARCHITECTURE.md](./ARCHITECTURE.md#system-overview)
- **Component Architecture**: See [ARCHITECTURE.md](./ARCHITECTURE.md#component-architecture)
- **Data Flow**: See [ARCHITECTURE.md](./ARCHITECTURE.md#data-flow)

### Database
- **Local Storage**: See [DATABASE_SCHEMA.md](./DATABASE_SCHEMA.md#local-storage-sqlitehive)
- **Backend Storage**: See [DATABASE_SCHEMA.md](./DATABASE_SCHEMA.md#backend-storage-postgresql)
- **Vector Storage**: See [DATABASE_SCHEMA.md](./DATABASE_SCHEMA.md#vector-storage-milvus)

## 🛠️ Development Guide

### Getting Started with Development
1. Read [SETUP_GUIDE.md](./SETUP_GUIDE.md)
2. Review [ARCHITECTURE.md](./ARCHITECTURE.md)
3. Check [CONTRIBUTING.md](./CONTRIBUTING.md)

### Backend Development
1. Review [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)
2. Check [DATABASE_SCHEMA.md](./DATABASE_SCHEMA.md)
3. See backend code in `backend/app/`

### Mobile Development
1. Review [ARCHITECTURE.md](./ARCHITECTURE.md#mobile-app-flutter)
2. Check mobile code in `mobile/lib/`
3. See [CONTRIBUTING.md](./CONTRIBUTING.md#dartflutter-mobile)

### Testing
- Backend tests: See [SETUP_GUIDE.md](./SETUP_GUIDE.md#running-tests)
- Mobile tests: See [SETUP_GUIDE.md](./SETUP_GUIDE.md#running-tests)
- Contributing tests: See [CONTRIBUTING.md](./CONTRIBUTING.md#testing)

## 📁 Project Structure

```
PocketGenie/
├── backend/                    # FastAPI backend
│   ├── app/
│   │   ├── api/               # API routers
│   │   ├── models/            # Database models
│   │   ├── schemas/           # Validation schemas
│   │   ├── services/          # Business logic
│   │   ├── core/              # Config & database
│   │   └── main.py            # FastAPI app
│   ├── tests/                 # Unit tests
│   ├── requirements.txt        # Dependencies
│   └── Dockerfile             # Docker config
│
├── mobile/                     # Flutter app
│   ├── lib/
│   │   ├── config/            # Configuration
│   │   ├── models/            # Data models
│   │   ├── providers/         # State management
│   │   ├── screens/           # UI screens
│   │   ├── services/          # Services
│   │   ├── widgets/           # UI components
│   │   └── main.dart          # Entry point
│   ├── test/                  # Tests
│   └── pubspec.yaml           # Dependencies
│
├── docs/                       # Documentation
│   ├── SETUP_GUIDE.md         # Setup instructions
│   ├── API_DOCUMENTATION.md   # API reference
│   ├── DATABASE_SCHEMA.md     # Database design
│   ├── ARCHITECTURE.md        # System architecture
│   ├── CONTRIBUTING.md        # Contribution guide
│   ├── PROJECT_SUMMARY.md     # Project overview
│   └── INDEX.md               # This file
│
├── docker-compose.yml         # Docker setup
├── QUICKSTART.md              # Quick start guide
├── README.md                  # Main documentation
├── LICENSE                    # MIT License
└── .gitignore                 # Git ignore rules
```

## 🎯 Common Tasks

### I want to...

#### ...get started quickly
→ Read [QUICKSTART.md](../QUICKSTART.md)

#### ...set up the development environment
→ Follow [SETUP_GUIDE.md](./SETUP_GUIDE.md)

#### ...understand the system architecture
→ Read [ARCHITECTURE.md](./ARCHITECTURE.md)

#### ...use the API
→ Check [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)

#### ...contribute to the project
→ See [CONTRIBUTING.md](./CONTRIBUTING.md)

#### ...understand the database
→ Read [DATABASE_SCHEMA.md](./DATABASE_SCHEMA.md)

#### ...see what's been built
→ Check [PROJECT_SUMMARY.md](./PROJECT_SUMMARY.md)

## 🔍 Search Tips

### By Topic
- **Setup**: QUICKSTART.md, SETUP_GUIDE.md
- **API**: API_DOCUMENTATION.md
- **Database**: DATABASE_SCHEMA.md
- **Architecture**: ARCHITECTURE.md
- **Contributing**: CONTRIBUTING.md

### By Audience
- **New Users**: QUICKSTART.md, README.md
- **Backend Developers**: API_DOCUMENTATION.md, DATABASE_SCHEMA.md
- **Mobile Developers**: ARCHITECTURE.md, CONTRIBUTING.md
- **DevOps**: SETUP_GUIDE.md, docker-compose.yml
- **Contributors**: CONTRIBUTING.md, ARCHITECTURE.md

## 📞 Support & Help

### Getting Help
1. Check relevant documentation
2. Search GitHub issues
3. Create a new issue with details
4. Join GitHub discussions

### Reporting Issues
- See [CONTRIBUTING.md](./CONTRIBUTING.md#issue-reporting)

### Contributing
- See [CONTRIBUTING.md](./CONTRIBUTING.md)

## 📋 Checklist for New Developers

- [ ] Read [QUICKSTART.md](../QUICKSTART.md)
- [ ] Follow [SETUP_GUIDE.md](./SETUP_GUIDE.md)
- [ ] Review [ARCHITECTURE.md](./ARCHITECTURE.md)
- [ ] Check [API_DOCUMENTATION.md](./API_DOCUMENTATION.md)
- [ ] Read [CONTRIBUTING.md](./CONTRIBUTING.md)
- [ ] Explore the codebase
- [ ] Run tests
- [ ] Create your first contribution

## 🎓 Learning Path

### For Backend Developers
1. QUICKSTART.md
2. SETUP_GUIDE.md (Backend section)
3. ARCHITECTURE.md (Backend section)
4. API_DOCUMENTATION.md
5. DATABASE_SCHEMA.md
6. Backend code in `backend/app/`

### For Mobile Developers
1. QUICKSTART.md
2. SETUP_GUIDE.md (Mobile section)
3. ARCHITECTURE.md (Mobile section)
4. Mobile code in `mobile/lib/`
5. CONTRIBUTING.md (Dart/Flutter section)

### For DevOps/Infrastructure
1. SETUP_GUIDE.md
2. docker-compose.yml
3. ARCHITECTURE.md (Deployment section)
4. DATABASE_SCHEMA.md

## 📚 Additional Resources

### External Links
- [Flutter Documentation](https://flutter.dev/docs)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Riverpod Documentation](https://riverpod.dev/)
- [Sentence Transformers](https://www.sbert.net/)

### Tools & Services
- [Docker](https://www.docker.com/)
- [PostgreSQL](https://www.postgresql.org/)
- [Milvus](https://milvus.io/)
- [Redis](https://redis.io/)
- [MinIO](https://min.io/)

## 📝 Document Versions

- **Last Updated**: 2024
- **Project Version**: 0.1.0 (MVP)
- **Status**: Complete and ready for use

## 🤝 Contributing to Documentation

To improve documentation:
1. Fork the repository
2. Make changes to docs
3. Submit a pull request
4. See [CONTRIBUTING.md](./CONTRIBUTING.md)

---

**Happy learning! 🚀**

For questions or suggestions, please open an issue on GitHub.

