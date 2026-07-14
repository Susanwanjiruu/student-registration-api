from database import get_connection


def add_teacher(name, id_number, department, email, age):
    with get_connection() as connection:
        connection.execute(
            'INSERT INTO teachers (name,id_number,department,email,age) VALUES (?,?,?,?,?)',
            (name, id_number, department, email, age)
        )


def get_teachers():
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers').fetchall()


def get_teacher(teacher_id):
    with get_connection() as connection:
        return connection.execute('SELECT * FROM teachers WHERE teacher_id=?', (teacher_id,)).fetchall()


def update_teacher(teacher_id, name, id_number, department, email, age):
    with get_connection() as connection:
        connection.execute(
            'UPDATE teachers SET name=?, id_number=?, department=?, email=?, age=? WHERE teacher_id=?',
            (name, id_number, department, email, age, teacher_id)
        )


def delete_teacher(teacher_id):
    with get_connection() as connection:
        connection.execute('DELETE FROM teachers WHERE teacher_id=?', (teacher_id,))
    
