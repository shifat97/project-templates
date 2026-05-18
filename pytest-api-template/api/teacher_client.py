from typing import Any, Dict, Optional
from api.base_client import BaseClient

class TeacherClient(BaseClient):
    def __init__(self, token: Optional[str] = None):
        super().__init__()
        if token:
            self.session.headers.update({"Authorization": f"Bearer {token}"})

    def login(self, payload: Dict[str, Any]):
        return self.post("/login", json=payload)

    def create_teacher(self, payload: Dict[str, Any]):
        return self.post("/api/teacher", json=payload)

    def get_all_teachers(self):
        return self.get("/api/teacher")

    def get_teacher_by_id(self, teacher_id: str):
        return self.get(f"/api/teacher/{teacher_id}")

    def update_teacher(self, teacher_id: str, payload: Dict[str, Any]):
        return self.put(f"/api/teacher/{teacher_id}", json=payload)

    def delete_teacher(self, teacher_id: str):
        return self.delete(f"/api/teacher/{teacher_id}")

    def get_filtered_teachers(self, filter_type: str, filter_value: str):
        return self.get("/api/teacher", params={filter_type: filter_value})
