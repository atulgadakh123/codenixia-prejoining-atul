import sqlite3


def add_student(name, email, phone, course):

    connection = sqlite3.connect("database/student.db")

    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS student (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT NOT NULL,
            phone TEXT,
            course TEXT
        )
    """)

    cursor.execute("""
        INSERT INTO student (name, email, phone, course)
        VALUES (?, ?, ?, ?)
    """, (name, email, phone, course))

    connection.commit()

    connection.close()
    

    print("Student added successfully")




def list_student():
     
    connection=sqlite3.connect("database/student.db")

    cursor=connection.cursor()

    cursor.execute("SELECT * FROM student")

    student= cursor.fetchall()

    connection.close()

    return student





#search Student

def search_student(student_id):
    connection =sqlite3.connect("database/student.db")

    cursor =connection.cursor()

    cursor.execute(
        "SELECT * FROM student WHERE id = ?",
        (student_id,)
    )

    student =cursor.fetchone()

    connection.close() 

    return student




#update student
def update_student(student_id,name,email,phone,course):

    connection =sqlite3.connect("database/student.db")

    cursor=connection.cursor()

    cursor.execute("""
        UPDATE student
        SET name = ?, email = ?,  phone = ?, course = ?
        WHERE id = ?
""",(name,email,phone,course,student_id))

    if cursor.rowcount == 0:
        print("student not found")

    else:
        connection.commit()
        print("Student updated successfully")

    connection.close()

    




def delete_student(student_id):

    connection = sqlite3.connect("database/student.db")

    cursor = connection.cursor()

    cursor.execute(
        "DELETE FROM student WHERE id = ?",
        (student_id,)
    )

    connection.commit()

    connection.close()

    print("Student deleted successfully")    