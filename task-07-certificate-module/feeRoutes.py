from fastapi import APIRouter, HTTPException

from database import search_student

from feeDatabase import (
    add_fee,
    get_payment_history,
    calculate_balence,
    get_payment_summary,
    get_pending_payments
)

from schemas import paymentCreate


router = APIRouter(prefix="/fees", tags=["Fees"])


# Add Payment
@router.post("/payment")
def add_payment(payment: paymentCreate):

    if payment.amount_paid < 0:
        raise HTTPException(
            status_code=400,
            detail="Amount paid cannot be negative"
        )

    if payment.registration_fee < 0:
        raise HTTPException(
            status_code=400,
            detail="Registration fee cannot be negative"
        )

    if payment.total_course_fee <= 0:
        raise HTTPException(
            status_code=400,
            detail="Total course fee must be greater than 0"
        )

    if payment.installment_number <= 0:
        raise HTTPException(
            status_code=400,
            detail="Installment number must be greater than 0"
        )

    # Check student
    student = search_student(payment.student_id)

    if student is None:
        raise HTTPException(
            status_code=404,
            detail="Student not found"
        )

    # Total amount paid
    total_paid = payment.registration_fee + payment.amount_paid

    # Prevent overpayment
    if total_paid > payment.total_course_fee:
        raise HTTPException(
            status_code=400,
            detail="Total payment cannot exceed course fee"
        )

    # Calculate balance
    balance = payment.total_course_fee - total_paid

    # Calculate payment status
    if balance <= 0:
        payment_status = "paid"
    else:
        payment_status = "pending"

    # Add fee
    fee_id = add_fee(
        payment.student_id,
        payment.total_course_fee,
        payment.registration_fee,
        payment.amount_paid,
        balance,
        payment.payment_date,
        payment.installment_number,
        payment_status
    )

    return {
        "message": "Payment added successfully",
        "fee_id": fee_id,
        "balance": balance,
        "payment_status": payment_status
    }


# Get Payment History
@router.get("/{student_id}/history")
def payment_history(student_id: int):

    history = get_payment_history(student_id)

    if not history:
        return {
            "message": "No payment history found",
            "student_id": student_id,
            "payment_history": []
        }

    return {
        "student_id": student_id,
        "payment_history": history
    }


# Calculate Balance
@router.get("/{student_id}/balance")
def student_balance(student_id: int):

    balance = calculate_balence(student_id)

    if balance is None:
        return {
            "message": "Fee record not found",
            "student_id": student_id
        }

    return {
        "student_id": student_id,
        "balance": balance
    }


# Payment Summary
@router.get("/{student_id}/summary")
def payment_summary(student_id: int):

    summary = get_payment_summary(student_id)

    if summary is None:
        return {
            "message": "Fee record not found",
            "student_id": student_id
        }

    return {
        "student_id": student_id,
        "payment_summary": summary
    }


# Pending Payment
@router.get("/pending")
def pending_payments():

    payments = get_pending_payments()

    return {
        "pending_payments": payments
    }