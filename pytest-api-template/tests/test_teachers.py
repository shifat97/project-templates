import pytest

from models.teacher import Teacher

class TestTeachers:
    def test_create_teacher_success(self, teacher_client, teacher_payload):
        response = teacher_client.create_teacher(teacher_payload)
        
        assert response.status_code == 201
        
        # Validate response with Pydantic model
        teacher = Teacher(**response.json())
        assert teacher.name == teacher_payload["name"]
        assert teacher.email == teacher_payload["email"]
        
        # Cleanup
        teacher_client.delete_teacher(teacher.teacherId)

    def test_get_all_teachers(self, teacher_client):
        response = teacher_client.get_all_teachers()
        
        assert response.status_code == 200
        assert isinstance(response.json(), list)

    def test_get_teacher_by_id(self, teacher_client, created_teacher):
        teacher_id = created_teacher["teacherId"]
        response = teacher_client.get_teacher_by_id(teacher_id)
        
        assert response.status_code == 200
        assert response.json()["teacherId"] == teacher_id

    def test_update_teacher(self, teacher_client, created_teacher):
        teacher_id = created_teacher["teacherId"]
        update_payload = {"name": "Updated Name"}
        
        # In a real app, you might need to send the full payload or partial
        # Assuming partial update is supported via PUT or PATCH
        response = teacher_client.update_teacher(teacher_id, update_payload)
        
        assert response.status_code == 200
        assert response.json()["name"] == "Updated Name"

    def test_delete_teacher(self, teacher_client, teacher_payload):
        # Create a teacher specifically to delete it
        create_res = teacher_client.create_teacher(teacher_payload)
        teacher_id = create_res.json()["teacherId"]
        
        delete_res = teacher_client.delete_teacher(teacher_id)
        assert delete_res.status_code == 200 # or 204 depending on API
        
        # Verify deletion
        get_res = teacher_client.get_teacher_by_id(teacher_id)
        assert get_res.status_code == 404
