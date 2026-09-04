# Task 4 – Authentication & Authorization

## Project Overview

This project adds authentication and authorization to the Student Management REST API using FastAPI.

The API provides user registration, password hashing, login with JWT authentication, protected student APIs, and role-based authorization.

## Features

* User Registration
* Password Hashing using bcrypt
* User Login
* JWT Authentication
* Protected APIs
* Role-Based Authorization
* Student CRUD Operations
* Input Validation using Pydantic
* SQLite Database

## Technologies Used

* Python
* FastAPI
* SQLite
* Pydantic
* JWT
* Passlib
* Bcrypt
* Uvicorn

## Project Structure

```text
task-04-authentication/
│
├── database/
│   └── student.db
│
├── main.py
├── database.py
├── schemas.py
├── auth.py
├── requirements.txt
└── README.md
```

## Installation

### 1. Create Virtual Environment

```bash
python -m venv venv
```

### 2. Activate Virtual Environment

Windows:

```bash
venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

## Run the Application

```bash
uvicorn main:app --reload
```

The API will run on:

```text
http://127.0.0.1:8000
```

Swagger API documentation:

```text
http://127.0.0.1:8000/docs
```

## Authentication Flow

### 1. Register User

Endpoint:

```text
POST /register
```

Example:

```json
{
  "name": "User",
  "email": "user@example.com",
  "password": "password123",
  "role": "Student"
}
```

Supported roles:

```text
Admin
Staff
Student
```

### 2. Login

Endpoint:

```text
POST /login
```

Example:

```json
{
  "email": "user@example.com",
  "password": "password123"
}
```

Successful login returns a JWT access token.

```json
{
  "message": "Login successful",
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

### 3. Authorize API

Open Swagger:

```text
/docs
```

Click:

```text
Authorize
```

Paste the JWT token and authorize the API.

## Student API Endpoints

| Method | Endpoint                 | Allowed Roles         |
| ------ | ------------------------ | --------------------- |
| POST   | `/students`              | Admin, Staff          |
| GET    | `/students`              | Admin, Staff, Student |
| GET    | `/students/{student_id}` | Admin, Staff, Student |
| PUT    | `/students/{student_id}` | Admin, Staff          |
| DELETE | `/students/{student_id}` | Admin                 |

## Authorization Testing

### Student

Student can:

* View all students
* View a specific student

Student cannot:

* Create a student
* Update a student
* Delete a student

Unauthorized operation returns:

```text
403 Forbidden
```

### Staff

Staff can:

* Create students
* View students
* Update students

Staff cannot:

* Delete students

Unauthorized operation returns:

```text
403 Forbidden
```

### Admin

Admin can:

* Create students
* View students
* Update students
* Delete students

## Password Security

Passwords are not stored directly in the database.

Passwords are hashed using bcrypt before storing them.

During login, the entered password is verified against the stored password hash.

## JWT Authentication

After successful login, the API generates a JWT access token.

The token contains user information such as:

```json
{
  "sub": "user@example.com",
  "role": "Admin"
}
```

The token is verified before accessing protected APIs.

## Sample Output

Successful login:

```json
{
  "message": "Login successful",
  "access_token": "<JWT_TOKEN>",
  "token_type": "bearer"
}
```

Successful protected API request:

```text
200 OK
```

Unauthorized role:

```text
403 Forbidden
```

Invalid authentication token:

```text
401 Unauthorized
```

## Known Limitations

* The JWT secret key is currently stored directly in the source code.
* Role selection during registration is directly accepted from the request.
* The project is intended for learning and demonstration purposes.

## What I Learned

* Difference between authentication and authorization
* User registration and login
* Password hashing using bcrypt
* JWT token creation and verification
* Protecting FastAPI endpoints
* Role-Based Access Control
* HTTP status codes such as 401 and 403
* Working with SQLite and FastAPI
* API testing using Swagger UI

## Conclusion

This project implements authentication and authorization for the Student Management REST API using FastAPI, JWT, password hashing, and role-based access control.
