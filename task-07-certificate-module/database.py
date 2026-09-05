import sqlite3


def get_db_connection():
    try:
        connection = sqlite3.connect("database/student.db")
        connection.row_factory = sqlite3.Row
        return connection
    except sqlite3.Error as e:
        raise Exception(f"Database connection error: {e}")


# Create Student Table
def create_student_table():
    connection = get_db_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS students(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                phone TEXT,
                course TEXT NOT NULL
            )
        """)
        connection.commit()

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Student table error: {e}")

    finally:
        connection.close()


# Create User Table
def create_user():
    connection = get_db_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS users(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL UNIQUE,
                password TEXT NOT NULL,
                role TEXT NOT NULL
            )
        """)
        connection.commit()

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"User table error: {e}")

    finally:
        connection.close()


# Add User
def add_user(name, email, password, role):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            INSERT INTO users(name, email, password, role)
            VALUES(?, ?, ?, ?)
        """, (name, email, password, role))

        connection.commit()

        return cursor.lastrowid

    except sqlite3.IntegrityError:
        connection.rollback()
        raise

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Add user error: {e}")

    finally:
        connection.close()


# Find User By Email
def get_user_by_email(email):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT * FROM users
            WHERE email = ?
        """, (email,))

        return cursor.fetchone()

    except sqlite3.Error as e:
        raise Exception(f"Find user error: {e}")

    finally:
        connection.close()


# Add Student
def add_student(name, email, phone, course):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            INSERT INTO students(name, email, phone, course)
            VALUES(?, ?, ?, ?)
        """, (name, email, phone, course))

        connection.commit()

        return cursor.lastrowid

    except sqlite3.IntegrityError:
        connection.rollback()
        raise

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Add student error: {e}")

    finally:
        connection.close()


# Get All Students
def all_student():
    connection = get_db_connection()

    try:
        cursor = connection.execute(
            "SELECT * FROM students"
        )

        return cursor.fetchall()

    except sqlite3.Error as e:
        raise Exception(f"Get students error: {e}")

    finally:
        connection.close()


# Search Student
def search_student(student_id):
    connection = get_db_connection()

    try:
        cursor = connection.execute(
            "SELECT * FROM students WHERE id = ?",
            (student_id,)
        )

        return cursor.fetchone()

    except sqlite3.Error as e:
        raise Exception(f"Search student error: {e}")

    finally:
        connection.close()


# Update Student
def update_student(
    student_id,
    name,
    email,
    phone,
    course
):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            UPDATE students
            SET name=?, email=?, phone=?, course=?
            WHERE id=?
        """, (
            name,
            email,
            phone,
            course,
            student_id
        ))

        connection.commit()

        return cursor.rowcount

    except sqlite3.IntegrityError:
        connection.rollback()
        raise

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Update student error: {e}")

    finally:
        connection.close()


# Delete Student
def delete_student(student_id):
    connection = get_db_connection()

    try:
        cursor = connection.execute(
            "DELETE FROM students WHERE id=?",
            (student_id,)
        )

        connection.commit()

        return cursor.rowcount

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Delete student error: {e}")

    finally:
        connection.close()