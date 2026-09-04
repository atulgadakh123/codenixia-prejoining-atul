import sqlite3

from database import get_db_connection


# Create Fee Table
def create_fee_table():
    connection = get_db_connection()

    try:
        connection.execute("""
            CREATE TABLE IF NOT EXISTS fees(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                student_id INTEGER NOT NULL,
                total_course_fee REAL NOT NULL,
                registration_fee REAL DEFAULT 0,
                amount_paid REAL DEFAULT 0,
                balance REAL NOT NULL,
                payment_date TEXT,
                installment_number INTEGER NOT NULL,
                payment_status TEXT NOT NULL,

                FOREIGN KEY (student_id) REFERENCES students(id)
            )
        """)

        connection.commit()

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Fee table error: {e}")

    finally:
        connection.close()


# Add Fee
def add_fee(
    student_id,
    total_course_fee,
    registration_fee,
    amount_paid,
    balance,
    payment_date,
    installment_number,
    payment_status
):
    connection = get_db_connection()

    try:

        # Check duplicate installment
        cursor = connection.execute("""
            SELECT id
            FROM fees
            WHERE student_id = ?
            AND installment_number = ?
        """, (
            student_id,
            installment_number
        ))

        existing_installment = cursor.fetchone()

        if existing_installment is not None:
            raise sqlite3.IntegrityError(
                "This installment already exists for this student"
            )

        cursor = connection.execute("""
            INSERT INTO fees(
                student_id,
                total_course_fee,
                registration_fee,
                amount_paid,
                balance,
                payment_date,
                installment_number,
                payment_status
            )
            VALUES(?, ?, ?, ?, ?, ?, ?, ?)
        """, (
            student_id,
            total_course_fee,
            registration_fee,
            amount_paid,
            balance,
            payment_date,
            installment_number,
            payment_status
        ))

        connection.commit()

        return cursor.lastrowid

    except sqlite3.IntegrityError:
        connection.rollback()
        raise

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Add fee error: {e}")

    finally:
        connection.close()


# Payment History
def get_payment_history(student_id):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT *
            FROM fees
            WHERE student_id = ?
            ORDER BY payment_date DESC
        """, (student_id,))

        return cursor.fetchall()

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Payment history error: {e}")

    finally:
        connection.close()


# Calculate Balance
def calculate_balence(student_id):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT
                total_course_fee,
                SUM(registration_fee + amount_paid)
            FROM fees
            WHERE student_id = ?
            GROUP BY total_course_fee
        """, (student_id,))

        fee = cursor.fetchone()

        if fee is None:
            return None

        total_course_fee = fee[0]
        total_paid = fee[1]

        balance = total_course_fee - total_paid

        if balance < 0:
            balance = 0

        return balance

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Balance calculation error: {e}")

    finally:
        connection.close()


# Pending Payments
def get_pending_payments():
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT *
            FROM fees
            WHERE balance > 0
            ORDER BY payment_date DESC
        """)

        return cursor.fetchall()

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Pending payments error: {e}")

    finally:
        connection.close()


# Payment Summary
def get_payment_summary(student_id):
    connection = get_db_connection()

    try:
        cursor = connection.execute("""
            SELECT
                total_course_fee,
                registration_fee,
                amount_paid,
                balance,
                payment_status
            FROM fees
            WHERE student_id = ?
        """, (student_id,))

        fee = cursor.fetchone()

        if fee is None:
            return None

        return fee

    except sqlite3.Error as e:
        connection.rollback()
        raise Exception(f"Payment summary error: {e}")

    finally:
        connection.close()