import pytest
import random
from faker import Faker
from config.settings import settings
from api.teacher_client import TeacherClient

faker = Faker()

@pytest.fixture(scope="session")
def auth_token():
    client = TeacherClient()
    payload = {
        "username": settings.ADMIN_USERNAME,
        "password": settings.ADMIN_PASSWORD
    }
    response = client.login(payload)
    assert response.status_code == 200, f"Login failed: {response.text}"
    return response.json().get("authToken")

@pytest.fixture(scope="session")
def teacher_client(auth_token):
    return TeacherClient(token=auth_token)

@pytest.fixture
def teacher_payload():
    valid_departments = ["CSE", "BBA", "MBA", "LAW", "PHARMACY", "ENGLISH"]
    designations = ["Assistant Professor", "Lecturer", "Senior Lecturer", "Associate Professor", "Professor"]
    
    return {
        "name": f"{faker.first_name()} {faker.last_name()}",
        "email": faker.unique.email(),
        "department": random.choice(valid_departments),
        "teacherId": faker.unique.random_number(digits=8),
        "designation": random.choice(designations)
    }

@pytest.fixture
def created_teacher(teacher_client, teacher_payload):
    response = teacher_client.create_teacher(teacher_payload)
    assert response.status_code == 201
    teacher_data = response.json()
    yield teacher_data
    # Cleanup
    teacher_client.delete_teacher(teacher_data.get("teacherId"))
