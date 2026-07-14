from database import get_connection


def add_course(course_trainer, course_name, department_name, students_taking_the_course, code):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO courses (course_trainer, course_name, department_name, students_taking_the_course, code) VALUES (?,?,?,?,?)',
            (course_trainer, course_name, department_name, students_taking_the_course, code)
        )


def get_courses():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses').fetchall()


def get_course(course_id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM courses WHERE course_id=?', (course_id,)).fetchall()


def update_course(course_id, course_trainer, course_name, department_name, students_taking_the_course, code):
    with get_connection() as connection:
        connection.execute(
            'UPDATE courses SET course_trainer=?, course_name=?, department_name=?, students_taking_the_course=?, code=? WHERE course_id=?',
            (course_trainer, course_name, department_name, students_taking_the_course, code, course_id)
        )


def delete_course(course_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM courses WHERE course_id=?', (course_id,))