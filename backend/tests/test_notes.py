"""
Tests for notes API
"""

import pytest


def test_create_note(client):
    """Test creating a note"""
    response = client.post(
        "/api/v1/notes/",
        json={
            "title": "Test Note",
            "content": "This is a test note with some content.",
            "category": "personal",
            "tags": ["test"],
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Test Note"
    assert data["content"] == "This is a test note with some content."
    assert data["category"] == "personal"
    assert "id" in data


def test_list_notes(client):
    """Test listing notes"""
    # Create a note first
    client.post(
        "/api/v1/notes/",
        json={
            "title": "Note 1",
            "content": "Content 1",
        },
    )

    response = client.get("/api/v1/notes/")
    assert response.status_code == 200
    data = response.json()
    assert len(data) > 0
    assert data[0]["title"] == "Note 1"


def test_get_note(client):
    """Test getting a specific note"""
    # Create a note first
    create_response = client.post(
        "/api/v1/notes/",
        json={
            "title": "Test Note",
            "content": "Test content",
        },
    )
    note_id = create_response.json()["id"]

    response = client.get(f"/api/v1/notes/{note_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == note_id
    assert data["title"] == "Test Note"


def test_update_note(client):
    """Test updating a note"""
    # Create a note first
    create_response = client.post(
        "/api/v1/notes/",
        json={
            "title": "Original Title",
            "content": "Original content",
        },
    )
    note_id = create_response.json()["id"]

    # Update the note
    response = client.put(
        f"/api/v1/notes/{note_id}",
        json={
            "title": "Updated Title",
            "content": "Updated content",
        },
    )
    assert response.status_code == 200
    data = response.json()
    assert data["title"] == "Updated Title"
    assert data["content"] == "Updated content"


def test_delete_note(client):
    """Test deleting a note"""
    # Create a note first
    create_response = client.post(
        "/api/v1/notes/",
        json={
            "title": "Note to Delete",
            "content": "Content to delete",
        },
    )
    note_id = create_response.json()["id"]

    # Delete the note
    response = client.delete(f"/api/v1/notes/{note_id}")
    assert response.status_code == 200

    # Verify it's deleted
    get_response = client.get(f"/api/v1/notes/{note_id}")
    assert get_response.status_code == 404

