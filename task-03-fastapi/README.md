# Student Management System REST API

## Project Description

The Student Management System REST API is a RESTful web API built using Python and FastAPI. It allows users to create, retrieve, update, and delete student records.

The API uses SQLite as the database and Pydantic for request and response validation.

## Technologies Used

* Python
* FastAPI
* Pydantic
* SQLite
* Uvicorn

## Project Structure

```text
task-03-fastapi/
│
├── main.py
├── database.py
├── student.py
├── validate.py
├── requirements.txt
├── README.md
│
└── database/
    └── student.db
```

## Features

* Create a new student
* Get all students
* Get a student by ID
* Update student information
* Delete a student
* Request validation
* Response models
* Duplicate email prevention
* Error handling
* HTTP status codes
* Automatic API documentation using Swagger UI

## Installation / Setup

### 1. Create a Virtual Environment

```bash
python -m venv venv
```

### 2. Activate the Virtual Environment

For Windows PowerShell:

```bash
venv\Scripts\Activate.ps1
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

Start the FastAPI server using Uvicorn:

```bash
uvicorn main:app --reload
```

The API will run at:

```text
http://127.0.0.1:8000
```

## API Endpoints

| Method | Endpoint                 | Description          |
| ------ | ------------------------ | -------------------- |
| POST   | `/students`              | Create a new student |
| GET    | `/students`              | Get all students     |
| GET    | `/students/{student_id}` | Get a student by ID  |
| PUT    | `/students/{student_id}` | Update a student     |
| DELETE | `/students/{student_id}` | Delete a student     |

## API Documentation

FastAPI automatically provides interactive API documentation using Swagger UI.

Open:

```text
http://127.0.0.1:8000/docs
```

From Swagger UI, all API endpoints can be tested directly.

## Sample Request & Response

### Create Student

**POST `/students`**

Request:

```json
{
    "name": "Atul",
    "email": "atul@gmail.com",
    "phone": "9876543210",
    "course": "Python"
}
```

Successful Response:

```json
{
    "message": "Student added successfully"
}
```

Status Code:

```text
201 Created
```

### Get All Students

**GET `/students`**

Response:

```json
[
    {
        "id": 1,
        "name": "Atul",
        "email": "atul@gmail.com",
        "phone": "9876543210",
        "course": "Python"
    }
]
```

### Get Student by ID

**GET `/students/1`**

Response:

```json
{
    "id": 1,
    "name": "Atul",
    "email": "atul@gmail.com",
    "phone": "9876543210",
    "course": "Python"
}
```

### Update Student

**PUT `/students/1`**

Request:

```json
{
    "name": "Atul Gadakh",
    "email": "atul@gmail.com",
    "phone": "9876543210",
    "course": "FastAPI"
}
```

Successful Response:

```json
{
    "message": "Student updated successfully"
}
```

### Delete Student

**DELETE `/students/1`**

Successful Response:

```json
{
    "message": "Student deleted successfully"
}
```

## Error Examples

### Duplicate Email

If an email that already exists is submitted:

```json
{
    "detail": "Email already exists"
}
```

Status Code:

```text
400 Bad Request
```

### Student Not Found

If a student ID does not exist:

```json
{
    "detail": "Student not found"
}
```

Status Code:

```text
404 Not Found
```

### Validation Error

If invalid student data is submitted:

```json
{
    "detail": "Invalid student data"
}
```

Status Code:

```text
400 Bad Request
```

## HTTP Status Codes

| Status Code          | Description                               |
| -------------------- | ----------------------------------------- |
| 200 OK               | Request completed successfully            |
| 201 Created          | Student successfully created              |
| 400 Bad Request      | Invalid data or duplicate email           |
| 404 Not Found        | Student does not exist                    |
| 422 Validation Error | FastAPI/Pydantic request validation error |

## Sample Input / Output

### Sample Input

```json
{
    "name": "Rahul",
    "email": "rahul@gmail.com",
    "phone": "9876543210",
    "course": "Python"
}
```

### Sample Output

```json
{
    "message": "Student added successfully"
}
```

## Known Limitations

* The application uses SQLite as a local database.
* Authentication and authorization are not implemented.
* The API does not use a production database server.
* The API currently supports basic student CRUD operations only.

## What I Learned
 How REST APIs work
 How to build APIs using FastAPI
 How to use Pydantic models for request and response validation
 How to connect FastAPI with SQLite
 How to implement CRUD operations
 How to use HTTP status codes
 How to handle API errors
 How to test APIs using Swagger UI
 How to document a REST API

