"""
Tests for tasks API
"""

import pytest
from datetime import datetime, timedelta


def test_create_task(client):
    """Test creating a task"""
    response = client.post(
        "/api/v1/tasks/",
        json={
            "title": "Test Task",
            "description": "Test Description",
            "priority": 1,
            "category": "work",
            "tags": ["urgent"],
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Task"
    assert data["description"] == "Test Description"
    assert data["priority"] == 1
    assert data["category"] == "work"
    assert "id" in data


def test_list_tasks(client):
    """Test listing tasks"""
    # Create a task first
    client.post(
        "/api/v1/tasks/",
        json={
            "title": "Task 1",
            "priority": 0,
        },
    )

    response = client.get("/api/v1/tasks/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["title"] == "Task 1"


def test_get_task(client):
    """Test getting a specific task"""
    # Create a task first
    create_response = client.post(
        "/api/v1/tasks/",
        json={
            "title": "Test Task",
            "priority": 1,
        },
    )
    task_id = create_response.json()["id"]

    response = client.get(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == task_id
    assert data["title"] == "Test Task"


def test_update_task(client):
    """Test updating a task"""
    # Create a task first
    create_response = client.post(
        "/api/v1/tasks/",
        json={
            "title": "Original Title",
            "priority": 0,
        },
    )
    task_id = create_response.json()["id"]

    # Update the task
    response = client.put(
        f"/api/v1/tasks/{task_id}",
        json={
            "title": "Updated Title",
            "priority": 2,
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["priority"] == 2


def test_delete_task(client):
    """Test deleting a task"""
    # Create a task first
    create_response = client.post(
        "/api/v1/tasks/",
        json={
            "title": "Task to Delete",
            "priority": 0,
        },
    )
    task_id = create_response.json()["id"]

    # Delete the task
    response = client.delete(f"/api/v1/tasks/{task_id}")
    assert response.status_code == 200

    # Verify it's deleted
    get_response = client.get(f"/api/v1/tasks/{task_id}")
    assert get_response.status_code == 404


def test_complete_task(client):
    """Test completing a task"""
    # Create a task first
    create_response = client.post(
        "/api/v1/tasks/",
        json={
            "title": "Task to Complete",
            "priority": 0,
        },
    )
    task_id = create_response.json()["id"]

    # Complete the task
    response = client.post(f"/api/v1/tasks/{task_id}/complete")
    assert response.status_code == 200
    data = response.json()
    assert data["completed"] is True

