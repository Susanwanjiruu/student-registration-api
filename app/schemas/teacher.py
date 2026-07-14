from pydantic import BaseModel


class Teacher(BaseModel):
    name: str
    id_number: int
    department: str
    email: str
    age: int