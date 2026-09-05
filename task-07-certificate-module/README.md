# Task 07 — Certificate Automation

## Overview

This project implements a simple Certificate Automation System using Python and FastAPI.

The system accepts student details, generates a unique certificate ID, stores certificate information in the database, provides certificate verification, and generates a certificate PDF.

## Features

* Accept student details
* Generate unique certificate ID
* Store certificate details in SQLite database
* Verify certificate using certificate ID
* Generate certificate PDF
* REST API using FastAPI
* Error handling for invalid certificate IDs

## Technologies Used

* Python
* FastAPI
* SQLite
* Pydantic
* ReportLab

## Project Structure

```text
task-07-certificate/
│
├── main.py
├── schemas.py
├── certificateRouter.py
├── requirements.txt
│
├── Data/
│   └── certificateDatabase.py
│
└── certificates/
    └── generated PDF files
```

## Installation

Create and activate the virtual environment, then install the required dependencies:

```bash
pip install -r requirements.txt
```

If required, install ReportLab separately:

```bash
pip install reportlab
```

## Run the Application

Start the FastAPI server:

```bash
uvicorn main:app --reload
```

The API documentation is available through Swagger UI.

## API Endpoints

### 1. Generate Certificate

**POST**

```text
/certificate/generate
```

#### Request

```json
{
  "student_id": 1,
  "student_name": "Atul Gadakh",
  "course": "Python"
}
```

#### Response

```json
{
  "message": "Certificate generated successfully",
  "certificate_id": "CERT-0002",
  "student_id": 1,
  "student_name": "Atul Gadakh",
  "course": "Python",
  "issue_date": "2026-09-05"
}
```

### 2. Verify Certificate

**GET**

```text
/certificate/verify/{certificate_id}
```

Example:

```text
/certificate/verify/CERT-0002
```

#### Response

```json
{
  "message": "Certificate is valid",
  "certificate_id": "CERT-0002",
  "student_id": 1,
  "student_name": "Atul Gadakh",
  "course": "Python",
  "issue_date": "2026-09-05"
}
```

If the certificate does not exist:

```json
{
  "detail": "Certificate not found"
}
```

### 3. Generate Certificate PDF

**GET**

```text
/certificate/pdf/{certificate_id}
```

Example:

```text
/certificate/pdf/CERT-0002
```

The generated PDF is saved inside the `certificates` directory.

## Database

The system uses a `certificates` table with the following fields:

| Field          | Description            |
| -------------- | ---------------------- |
| id             | Internal database ID   |
| certificate_id | Unique certificate ID  |
| student_id     | Student ID             |
| student_name   | Student name           |
| course         | Course name            |
| issue_date     | Certificate issue date |

## Certificate ID

Certificate IDs are generated automatically.

Example:

```text
CERT-0001
CERT-0002
CERT-0003
```

## PDF Generation

ReportLab is used to generate certificate PDF files.

Generated files are stored in:

```text
certificates/
```

Example:

```text
certificates/CERT-0002.pdf
```

## Known Limitations

* QR code generation is not implemented yet.
* PDF design is currently simple.
* Certificate verification is based on the certificate ID stored in the database.
* The application currently uses SQLite for database storage.

## What I Learned

* Creating database tables using SQLite
* Separating database logic from API routes
* Generating unique certificate IDs
* Building FastAPI endpoints
* Using Pydantic schemas for request validation
* Implementing certificate verification
* Generating PDF files using ReportLab
* Handling HTTP errors using FastAPI
* Organizing a backend project into separate modules

## Task Status

* Student details: Completed
* Certificate generation: Completed
* Unique certificate ID: Completed
* Database storage: Completed
* Certificate verification: Completed
* PDF generation: Completed
* Testing: Completed

