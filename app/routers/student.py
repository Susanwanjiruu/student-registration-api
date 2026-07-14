from fastapi import APIRouter
from schemas.student import Student
from repositories.student import (
    add_student,
    get_students,
    get_student,
    update_student,
    delete_student,
)

router = APIRouter(prefix="/students", tags=["students"])


@router.get("")
def student_detail(id: int):
    student = get_student(id)
    return student


@router.get("/all")
def student_list():
    students = get_students()
    return students


@router.post("")
def register_student(student: Student):
    add_student(student.name, student.age, student.email, student.country, student.id_number, student.department)
    return {"message": "student registered", "student": student}


@router.put("/{id}")
def edit_student(id: int, student: Student):
    update_student(id, student.name, student.age, student.email, student.country, student.id_number, student.department)
    return {"message": f"Student with ID {id} updated successfully", "student": student}


@router.delete("/{id}")
def remove_student(id: int):
    delete_student(id)
    return {"message": f"Student with ID {id} deleted successfully"}