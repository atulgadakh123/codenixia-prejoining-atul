import sqlite3


def create_table():

    connection = sqlite3.connect("database/student.db")

    cursor = connection.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        phone TEXT,
        course TEXT
    )
""")

    connection.commit()

    connection.close()


# Add Student
def add_student(name, email, phone, course):

    connection = sqlite3.connect("database/student.db")

    cursor = connection.cursor()

    try:
        cursor.execute("""
            INSERT INTO student (name, email, phone, course)
            VALUES (?, ?, ?, ?)
        """, (name, email, phone, course))

        connection.commit()

    except sqlite3.IntegrityError:
        connection.close()
        return False

    connection.close()

    return True


# List Students
def list_student():

    connection = sqlite3.connect("database/student.db")

    cursor = connection.cursor()

    cursor.execute("SELECT * FROM student")

    students = cursor.fetchall()

    connection.close()

    return [
        {
            "id": student[0],
            "name": student[1],
            "email": student[2],
            "phone": student[3],
            "course": student[4]
        }
        for student in students
    ]


# Search Student
def search_student(student_id):

    connection = sqlite3.connect("database/student.db")

    cursor = connection.cursor()

    cursor.execute(
        "SELECT * FROM student WHERE id = ?",
        (student_id,)
    )

    student = cursor.fetchone()

    connection.close()

    if student:

        return {
            "id": student[0],
            "name": student[1],
            "email": student[2],
            "phone": student[3],
            "course": student[4]
        }

    return None


# Update Student
def update_student(
    student_id,
    name,
    email,
    phone,
    course
):

    connection = sqlite3.connect("database/student.db")

    cursor = connection.cursor()

    cursor.execute("""
        UPDATE student
        SET name = ?, email = ?, phone = ?, course = ?
        WHERE id = ?
    """, (
        name,
        email,
        phone,
        course,
        student_id
    ))

    connection.commit()

    rows_updated = cursor.rowcount

    connection.close()

    return rows_updated


# Delete Student
def delete_student(student_id):

    connection = sqlite3.connect("database/student.db")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM student WHERE id = ?",
        (student_id,)
    )

    connection.commit()

    rows_deleted = cursor.rowcount

    connection.close()

    return rows_deleted