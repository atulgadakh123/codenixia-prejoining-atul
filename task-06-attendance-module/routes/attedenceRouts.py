from fastapi import APIRouter, HTTPException
from schemas  import AttendanceCreate
from Data.attendance import (
    add_attendance,
    get_all_attendance,
    get_student_attendance,
    get_daily_attendance,
    get_batch_attendance,
    calculate_attendance_percentage,
    get_students_below_threshold
)


router = APIRouter(
    prefix="/attendance",
    tags=["Attendance"]
)


# Add Attendance
@router.post("/")
def create_attendance(attendance: AttendanceCreate):
    try:
        attendance_id = add_attendance(
            attendance.student_id,
            attendance.course,
            attendance.batch,
            attendance.attendance_date,
            attendance.status
        )

        return {
            "message": "Attendance added successfully",
            "attendance_id": attendance_id
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# Get All Attendance
@router.get("/")
def get_attendance():
    try:
        records = get_all_attendance()

        return [dict(record) for record in records]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# Student-wise Attendance
@router.get("/student/{student_id}")
def get_student_attendance_route(student_id: int):
    try:
        records = get_student_attendance(student_id)

        return [dict(record) for record in records]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# Daily Attendance
@router.get("/daily/{attendance_date}")
def get_daily_attendance_route(attendance_date: str):
    try:
        records = get_daily_attendance(attendance_date)

        return [dict(record) for record in records]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# Batch-wise Attendance
@router.get("/batch/{batch}")
def get_batch_attendance_route(batch: str):
    try:
        records = get_batch_attendance(batch)

        return [dict(record) for record in records]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# Student Attendance Percentage
@router.get("/student/{student_id}/percentage")
def get_attendance_percentage(student_id: int):
    try:
        percentage = calculate_attendance_percentage(student_id)

        return {
            "student_id": student_id,
            "attendance_percentage": round(percentage, 2)
        }

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )


# Students Below Attendance Threshold
@router.get("/below-threshold")
def get_below_threshold():
    try:
        records = get_students_below_threshold(75)

        return [dict(record) for record in records]

    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=str(e)
        )