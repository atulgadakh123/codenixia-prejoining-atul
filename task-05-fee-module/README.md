# Task 05 — Fee & Installment Management

## Overview

This project extends the Student Management API with a Fee Management Module using Python, FastAPI, and SQLite.

The module manages course fees, registration fees, installments, payments, balances, and payment status.

## Features

* Store total course fee
* Store registration fee
* Manage installments
* Store amount paid
* Calculate balance
* Store payment date
* Track payment status
* Validate student before adding payment
* Prevent negative payments
* Prevent overpayment
* Prevent duplicate installment numbers for the same student
* Maintain payment history
* View pending payments
* Generate payment summary

## Technologies

* Python
* FastAPI
* SQLite
* Pydantic
* REST API

## Project Structure

```text
task-05-fee-management/
│
├── main.py
├── database.py
├── feeDatabase.py
├── feeRoutes.py
├── schemas.py
├── requirements.txt
└── README.md
```

## APIs

### 1. Add Payment

**POST**

```text
/fees/payment
```

Example request:

```json
{
  "student_id": 3,
  "total_course_fee": 50000,
  "registration_fee": 5000,
  "amount_paid": 10000,
  "installment_number": 1,
  "payment_date": "2026-09-04"
}
```

Example response:

json
{
  "message": "Payment added successfully",
  "fee_id": 4,
  "balance": 35000,
  "payment_status": "pending"
}


### 2. View Payment History

**GET**

text
/fees/{student_id}/history


Example:

```text
/fees/3/history
```

Returns all payment records for the student.

### 3. Calculate Balance

**GET**

```text
/fees/{student_id}/balance
```

Example:

```text
/fees/3/balance
```

Example response:

```json
{
  "student_id": 3,
  "balance": 35000
}
```

### 4. View Pending Payments

**GET**

```text
/fees/pending
```

Returns payment records where the balance is greater than zero.

### 5. Payment Summary

**GET**

```text
/fees/{student_id}/summary
```

Example:

```text
/fees/3/summary
```

Example response:

```json
{
  "student_id": 3,
  "payment_summary": {
    "total_course_fee": 50000,
    "registration_fee": 5000,
    "amount_paid": 10000,
    "balance": 35000,
    "payment_status": "pending"
  }
}
```

## Fee Calculation

The balance is calculated as:

```text
Balance = Total Course Fee - Total Paid
```

Where:

```text
Total Paid = Registration Fee + Amount Paid
```

For multiple installments, the balance calculation considers the payments recorded for the student.

## Validation

The API validates:

* Student must exist
* Amount paid cannot be negative
* Registration fee cannot be negative
* Total course fee must be greater than zero
* Installment number must be greater than zero
* Total payment cannot exceed course fee
* Duplicate installment numbers are not allowed for the same student

## Database Relationship

The `fees` table is connected to the `students` table using `student_id`.

```text
students
   │
   │ student_id
   ↓
 fees
```

A student can have multiple fee/payment records.

## Transactions and Data Integrity

Database operations use transactions with:

* `commit()` for successful operations
* `rollback()` when an error occurs
* Foreign key relationship between students and fees
* Duplicate installment validation

## How to Run

Create and activate the virtual environment:

```bash
python -m venv venv
```

Activate on Windows:

```bash
venv\Scripts\activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the FastAPI application:

```bash
uvicorn main:app --reload
```

Open Swagger documentation:

```text
http://127.0.0.1:8000/docs
```

## Task 5 Requirements Covered

| Requirement            | Status |
| ---------------------- | ------ |
| Total course fee       | ✅     |
| Registration fee       | ✅      |
| Installments           | ✅      |
| Amount paid            | ✅      |
| Balance                | ✅      |
| Payment date           | ✅      |
| Payment status         | ✅      |
| Add payment API        | ✅      |
| Payment history API    | ✅      |
| Calculate balance API  | ✅      |
| Pending payments API   | ✅      |
| Payment summary API    | ✅      |
| Database relationships | ✅      |
| Transactions           | ✅      |
| Business logic         | ✅      |
| Data integrity         | ✅      |
| Financial calculations | ✅      |
| API design             | ✅      |
