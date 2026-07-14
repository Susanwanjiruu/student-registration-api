from database import get_connection


def add_student(name, age, email, country, id_number, department):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO students(name, age, email, country, id_number, department) VALUES(?,?,?,?,?,?)',
            (name, age, email, country, id_number, department),
        )


def get_students():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students').fetchall()


def get_student(student_id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM students WHERE id=?', (student_id,)).fetchall()


def update_student(student_id, name, age, email, country, id_number, department):
    with get_connection() as connection:
        connection.execute(
            'UPDATE students SET name=?, age=?, email=?, country=?, id_number=?, department=? WHERE id=?',
            (name, age, email, country, id_number, department, student_id),
        )


def delete_student(student_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM students WHERE id=?', (student_id,))