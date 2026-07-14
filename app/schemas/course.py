from pydantic import BaseModel
class Courses(BaseModel):
    course_trainer:str
    course_name:str
    department_name :str
    students_taking_the_course : int
    code:str