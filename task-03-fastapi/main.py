from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from database import (
    create_table,
    add_student,
    list_student,
    search_student,
    update_student,
    delete_student
)

from validate import validate_student


class StudentCreate(BaseModel):
    name: str
    email: str
    phone: str
    course: str


class StudentUpdate(BaseModel):
    name: str
    email: str
    phone: str
    course: str


class StudentResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str
    course: str


app = FastAPI(
    title="Student Management API",
    description="REST API for managing student records",
    version="1.0.0"
)


create_table()


@app.get(
    "/",
    summary="Home",
    description="Check whether the Student Management API is running."
)
def home():

    return {
        "message": "Student Management API"
    }


# Add Student
@app.post(
    "/students",
    status_code=201,
    summary="Create Student",
    description="Create a new student record."
)
def create_student(student: StudentCreate):

    try:
        validate_student(
            student.name,
            student.email,
            student.phone,
            student.course
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    added = add_student(
        student.name,
        student.email,
        student.phone,
        student.course
    )

    if not added:

        raise HTTPException(
            status_code=400,
            detail="Email already exists"
        )

    return {
        "message": "Student added successfully"
    }


# List Students
@app.get(
    "/students",
    response_model=list[StudentResponse],
    status_code=200,
    summary="Get All Students",
    description="Retrieve all student records."
)
def get_students():

    students = list_student()

    return students


# Search Student
@app.get(
    "/students/{student_id}",
    response_model=StudentResponse,
    status_code=200,
    summary="Get Student",
    description="Retrieve a student by student ID."
)
def get_student(student_id: int):

    student = search_student(student_id)

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    return student


# Update Student
@app.put(
    "/students/{student_id}",
    status_code=200,
    summary="Update Student",
    description="Update an existing student's information."
)
def update_student_api(
    student_id: int,
    student: StudentUpdate
):

    try:
        validate_student(
            student.name,
            student.email,
            student.phone,
            student.course
        )

    except ValueError as error:

        raise HTTPException(
            status_code=400,
            detail=str(error)
        )

    existing_student = search_student(student_id)

    if not existing_student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    update_student(
        student_id,
        student.name,
        student.email,
        student.phone,
        student.course
    )

    return {
        "message": "Student updated successfully"
    }


# Delete Student
@app.delete(
    "/students/{student_id}",
    status_code=200,
    summary="Delete Student",
    description="Delete a student by student ID."
)
def delete_student_api(student_id: int):

    student = search_student(student_id)

    if not student:

        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    delete_student(student_id)

    return {
        "message": "Student deleted successfully"
    }