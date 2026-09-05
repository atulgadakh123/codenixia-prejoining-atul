import sqlite3

from database import get_db_connection, search_student


#create Attedence

def create_attendace_table():
    connection = get_db_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS attendance(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                course TEXT NOT NULL,
                batch TEXT NOT NULL,
                attendance_date DATE NOT NULL,
                status TEXT NOT NULL
            )
        """)
        connection.commit()

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Attendance table error: {e}")

    finally:
        connection.close()

# Add Attendance
def add_attendance(student_id, course, batch, attendance_date, status):
    connection = get_db_connection()

    student = search_student(student_id)

    if student is None:
        raise Exception("Student not found")
    try:
        cursor = connection.execute("""
            INSERT INTO attendance(
                student_id,
                course,
                batch,
                attendance_date,
                status
            )
            VALUES(?, ?, ?, ?, ?)
        """, (
            student_id,
            course,
            batch,
            attendance_date,
            status
        ))

        connection.commit()

        return cursor.lastrowid

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Add attendance error: {e}")

    finally:
        connection.close()

# Get All Attendance
def get_all_attendance():
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT * FROM attendance
        """)

        return cursor.fetchall()

    except sqlite3.Error as e:
        raise Exception(f"Get attendance error: {e}")

    finally:
        connection.close()


 # Get Student Attendance
def get_student_attendance(student_id):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT *
            FROM attendance
            WHERE student_id = ?
            ORDER BY attendance_date
        """, (student_id,))

        return cursor.fetchall()

    except sqlite3.Error as e:
        raise Exception(f"Get student attendance error: {e}")

    finally:
        connection.close()

# Get Daily Attendance
def get_daily_attendance(attendance_date):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT *
            FROM attendance
            WHERE attendance_date = ?
            ORDER BY student_id
        """, (attendance_date,))

        return cursor.fetchall()

    except sqlite3.Error as e:
        raise Exception(f"Get daily attendance error: {e}")

    finally:
        connection.close()

        # Get Batch Attendance
def get_batch_attendance(batch):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT *
            FROM attendance
            WHERE batch = ?
            ORDER BY attendance_date, student_id
        """, (batch,))

        return cursor.fetchall()

    except sqlite3.Error as e:
        raise Exception(f"Get batch attendance error: {e}")

    finally:
        connection.close()

# Calculate Student Attendance Percentage
def calculate_attendance_percentage(student_id):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT
                COUNT(*) AS total_days,
                SUM(CASE WHEN status = 'Present' THEN 1 ELSE 0 END) AS present_days
            FROM attendance
            WHERE student_id = ?
        """, (student_id,))

        result = cursor.fetchone()

        total_days = result["total_days"]
        present_days = result["present_days"] or 0

        if total_days == 0:
            return 0

        return (present_days / total_days) * 100

    except sqlite3.Error as e:
        raise Exception(f"Attendance percentage error: {e}")

    finally:
        connection.close()


# Get Students Below Attendance Threshold
def get_students_below_threshold(threshold=75):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT
                student_id,
                COUNT(*) AS total_days,
                SUM(
                    CASE
                        WHEN status = 'Present' THEN 1
                        ELSE 0
                    END
                ) AS present_days
            FROM attendance
            GROUP BY student_id
            HAVING (present_days * 100.0 / total_days) < ?
        """, (threshold,))

        return cursor.fetchall()

    except sqlite3.Error as e:
        raise Exception(
            f"Attendance threshold error: {e}"
        )

    finally:
        connection.close()


# Get Student Attendance Report
def get_student_attendance_report(student_id):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT
                student_id,
                course,
                batch,
                attendance_date,
                status
            FROM attendance
            WHERE student_id = ?
            ORDER BY attendance_date
        """, (student_id,))

        return cursor.fetchall()

    except sqlite3.Error as e:
        raise Exception(
            f"Student attendance report error: {e}"
        )

    finally:
        connection.close()