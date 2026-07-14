from fastapi import APIRouter
from schemas.teacher import Teacher
from repositories.teacher import (
    add_teacher,
    get_teachers,
    get_teacher,
    update_teacher,
    delete_teacher,
)

router = APIRouter(prefix="/teacher", tags=["teacher"])


@router.get("")
def list_teachers():
    return get_teachers()


@router.get("/{teacher_id}")
def teacher_detail(teacher_id: int):
    return get_teacher(teacher_id)


@router.post("")
def register_teacher(teacher: Teacher):
    add_teacher(teacher.name, teacher.id_number, teacher.department, teacher.email, teacher.age)
    return teacher


@router.put("/{teacher_id}")
def edit_teacher(teacher_id: int, teacher: Teacher):
    update_teacher(teacher_id, teacher.name, teacher.id_number, teacher.department, teacher.email, teacher.age)
    return {"message": f"Teacher with ID {teacher_id} updated successfully", "teacher": teacher}


@router.delete("/{teacher_id}")
def remove_teacher(teacher_id: int):
    """
    Deletes a teacher from the temporary database by their ID.
    """
    delete_teacher(teacher_id)
    return {"message": f"Teacher with ID {teacher_id} deleted successfully"}

