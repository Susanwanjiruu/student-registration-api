from pydantic import BaseModel


class Student(BaseModel):
    name: str
    department: str
    email: str
    country: str
    id_number: int
    age:int