# Contributing to PocketGenie

Thank you for your interest in contributing to PocketGenie! This document provides guidelines and instructions for contributing.

## Code of Conduct

- Be respectful and inclusive
- Provide constructive feedback
- Focus on the code, not the person
- Help others learn and grow

## Getting Started

1. Fork the repository
2. Clone your fork: `git clone https://github.com/yourusername/PocketGenie.git`
3. Create a feature branch: `git checkout -b feature/your-feature-name`
4. Make your changes
5. Commit with clear messages: `git commit -m "Add feature: description"`
6. Push to your fork: `git push origin feature/your-feature-name`
7. Create a Pull Request

## Development Setup

See [SETUP_GUIDE.md](./SETUP_GUIDE.md) for detailed setup instructions.

## Coding Standards

### Python (Backend)

- Follow PEP 8 style guide
- Use type hints
- Write docstrings for functions and classes
- Use meaningful variable names
- Keep functions small and focused

Example:
```python
def create_task(db: Session, task: TaskCreate) -> Task:
    """
    Create a new task.
    
    Args:
        db: Database session
        task: Task creation schema
        
    Returns:
        Created task object
    """
    db_task = Task(**task.dict())
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task
```

### Dart/Flutter (Mobile)

- Follow Dart style guide
- Use meaningful widget names
- Add comments for complex logic
- Use const constructors where possible
- Keep widgets focused and reusable

Example:
```dart
class TaskCard extends ConsumerWidget {
  final TaskModel task;

  const TaskCard({Key? key, required this.task}) : super(key: key);

  @override
  Widget build(BuildContext context, WidgetRef ref) {
    // Implementation
  }
}
```

## Testing

### Backend Tests

```bash
cd backend
pytest tests/
```

Write tests for:
- API endpoints
- Service methods
- Database operations
- Edge cases

Example:
```python
def test_create_task(client):
    response = client.post(
        "/api/v1/tasks/",
        json={"title": "Test Task", "priority": 1}
    )
    assert response.status_code == 200
    assert response.json()["title"] == "Test Task"
```

### Mobile Tests

```bash
cd mobile
flutter test
```

Write tests for:
- Models
- Providers
- Services
- Widgets

Example:
```dart
void main() {
  test('TaskModel copyWith works correctly', () {
    final task = TaskModel(id: '1', title: 'Test');
    final updated = task.copyWith(title: 'Updated');
    expect(updated.title, 'Updated');
    expect(updated.id, '1');
  });
}
```

## Commit Messages

Use clear, descriptive commit messages:

```
feat: Add semantic search functionality
fix: Resolve task completion bug
docs: Update API documentation
refactor: Simplify embedding service
test: Add tests for task prioritization
chore: Update dependencies
```

Format: `<type>: <description>`

Types:
- `feat`: New feature
- `fix`: Bug fix
- `docs`: Documentation
- `refactor`: Code refactoring
- `test`: Tests
- `chore`: Maintenance

## Pull Request Process

1. **Before submitting**:
   - Run tests: `pytest` (backend) or `flutter test` (mobile)
   - Check code style
   - Update documentation if needed
   - Ensure no merge conflicts

2. **PR Description**:
   - Clear title describing the change
   - Description of what changed and why
   - Link to related issues
   - Screenshots for UI changes

3. **Review Process**:
   - At least one approval required
   - Address feedback and comments
   - Keep commits clean and organized
   - Rebase if needed

4. **Merging**:
   - Squash commits if appropriate
   - Delete feature branch after merge
   - Update related issues

## Issue Reporting

When reporting issues:

1. **Check existing issues** first
2. **Provide details**:
   - OS and version
   - Steps to reproduce
   - Expected vs actual behavior
   - Error messages/logs
   - Screenshots if applicable

3. **Use issue templates** if available

Example:
```
**Describe the bug**
Tasks are not syncing to backend

**Steps to reproduce**
1. Create a task
2. Go offline
3. Go online
4. Task doesn't appear on backend

**Expected behavior**
Task should sync automatically

**Environment**
- OS: Windows 11
- Flutter: 3.10.0
- Backend: Running locally
```

## Feature Requests

When suggesting features:

1. **Describe the feature** clearly
2. **Explain the use case** and benefits
3. **Provide examples** if possible
4. **Consider alternatives** you've thought of

## Documentation

- Update README.md for major changes
- Add docstrings to new functions
- Update API documentation for new endpoints
- Add comments for complex logic
- Keep docs in sync with code

## Areas for Contribution

### High Priority
- [ ] Voice input implementation
- [ ] Multi-device sync
- [ ] Advanced AI features
- [ ] Performance optimization
- [ ] Mobile UI improvements

### Medium Priority
- [ ] Export functionality (PDF, CSV)
- [ ] Calendar integration
- [ ] Notification improvements
- [ ] Search enhancements
- [ ] Settings UI

### Low Priority
- [ ] Documentation improvements
- [ ] Code refactoring
- [ ] Test coverage
- [ ] UI polish
- [ ] Accessibility improvements

## Questions?

- Open a discussion on GitHub
- Check existing documentation
- Ask in issues or PRs
- Join our community

## License

By contributing, you agree that your contributions will be licensed under the MIT License.

## Recognition

Contributors will be recognized in:
- README.md contributors section
- Release notes
- GitHub contributors page

Thank you for contributing to PocketGenie! 🎉

