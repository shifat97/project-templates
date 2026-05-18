from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class Teacher(BaseModel):
    name: str
    email: EmailStr
    department: str
    teacherId: int
    designation: str
    id: Optional[str] = Field(None, alias="_id")

    class Config:
        populate_by_name = True
