from database import get_connection
def create_table():
    with get_connection() as connection:
       
        connection.execute('''CREATE TABLE IF NOT EXISTS courses(
                           course_id INTEGER PRIMARY KEY AUTOINCREMENT,
                           course_trainer TEXT NOT NULL,
                           course_name TEXT NOT NULL,
                           department_name TEXT NOT NULL,
                           students_taking_the_course INTEGER NOT NULL,
                           code TEXT NOT NULL
                           )''')
        