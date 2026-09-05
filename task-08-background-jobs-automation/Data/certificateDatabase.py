import sqlite3

from database import get_db_connection


# Create certificate table
def create_certificate_table():
    connection = get_db_connection()

    connection.execute("""
        CREATE TABLE IF NOT EXISTS certificates (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            certificate_id TEXT UNIQUE NOT NULL,
            student_id INTEGER NOT NULL,
            student_name TEXT NOT NULL,
            course TEXT NOT NULL,
            issue_date TEXT NOT NULL
        )
    """)

    connection.commit()
    connection.close()


# Insert certificate into database
def add_certificate(
    certificate_id,
    student_id,
    student_name,
    course,
    issue_date
):
    connection = get_db_connection()

    connection.execute("""
        INSERT INTO certificates
        (certificate_id, student_id, student_name, course, issue_date)
        VALUES (?, ?, ?, ?, ?)
    """, (
        certificate_id,
        student_id,
        student_name,
        course,
        issue_date
    ))

    connection.commit()
    connection.close()


# Generate unique certificate ID
def generate_certificate_id():
    connection = get_db_connection()

    cursor = connection.execute(
        "SELECT id FROM certificates ORDER BY id DESC LIMIT 1"
    )

    result = cursor.fetchone()

    connection.close()

    if result is None:
        next_id = 1
    else:
        next_id = result[0] + 1

    return f"CERT-{next_id:04d}"


# Get certificate by certificate ID
def get_certificate(certificate_id):
    connection = get_db_connection()

    cursor = connection.execute(
        """
        SELECT
            certificate_id,
            student_id,
            student_name,
            course,
            issue_date
        FROM certificates
        WHERE certificate_id = ?
        """,
        (certificate_id,)
    )

    certificate = cursor.fetchone()

    connection.close()

    return certificate