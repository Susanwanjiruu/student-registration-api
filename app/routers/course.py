from fastapi import APIRouter
from schemas.course import Courses
from repositories.course import (
    add_course,
    get_courses,
    get_course,
    update_course,
    delete_course,
)

router = APIRouter(prefix="/courses", tags=["course"])


@router.get("/courses")
def list_courses():
    return get_courses()


@router.get("/courses/{course_id}")
def course_detail(course_id: int):
    return get_course(course_id)


@router.post("/courses")
def create_courses(course: Courses):
    add_course(
        course.course_trainer,
        course.course_name,
        course.department_name,
        course.students_taking_the_course,
        course.code,
    )
    return {"message": "Course registered", "course": course}


@router.put("/courses/{course_id}")
def edit_course(course_id: int, course: Courses):
    update_course(
        course_id,
        course.course_trainer,
        course.course_name,
        course.department_name,
        course.students_taking_the_course,
        course.code,
    )
    return {"message": f"course with ID {course_id} updated successfully", "course": course}


@router.delete("/courses/{course_id}")
def remove_course(course_id: int):
    delete_course(course_id)
    return {"message": f"Course with ID {course_id} deleted successfully"}