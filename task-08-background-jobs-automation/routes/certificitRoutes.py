from fastapi import APIRouter, HTTPException
from datetime import date
from fastapi.responses import FileResponse
from reportlab.pdfgen import canvas
import os

from schemas import CertificateCreate

from Data.certificateDatabase import (
    add_certificate,
    generate_certificate_id,
    get_certificate
)


router = APIRouter(
    prefix="/certificate",
    tags=["Certificate"]
)


# Generate Certificate
@router.post("/generate")
def generate_certificate(certificate: CertificateCreate):

    certificate_id = generate_certificate_id()
    issue_date = str(date.today())

    add_certificate(
        certificate_id,
        certificate.student_id,
        certificate.student_name,
        certificate.course,
        issue_date
    )

    return {
        "message": "Certificate generated successfully",
        "certificate_id": certificate_id,
        "student_id": certificate.student_id,
        "student_name": certificate.student_name,
        "course": certificate.course,
        "issue_date": issue_date
    }


# Verify Certificate
@router.get("/pdf/{certificate_id}")
def generate_certificate_pdf(certificate_id: str):

    certificate = get_certificate(certificate_id)

    if certificate is None:
        raise HTTPException(
            status_code=404,
            detail="Certificate not found"
        )

    certificate_id = certificate[0]
    student_id = certificate[1]
    student_name = certificate[2]
    course = certificate[3]
    issue_date = certificate[4]

    os.makedirs("certificates", exist_ok=True)

    file_path = f"certificates/{certificate_id}.pdf"

    pdf = canvas.Canvas(file_path)

    pdf.setTitle("Certificate")

    pdf.setFont("Helvetica-Bold", 24)
    pdf.drawCentredString(
        300,
        750,
        "CERTIFICATE OF COMPLETION"
    )

    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(
        300,
        680,
        "This certificate is proudly presented to"
    )

    pdf.setFont("Helvetica-Bold", 20)
    pdf.drawCentredString(
        300,
        630,
        student_name
    )

    pdf.setFont("Helvetica", 14)
    pdf.drawCentredString(
        300,
        580,
        f"for successfully completing the {course} course"
    )

    pdf.setFont("Helvetica", 12)
    pdf.drawString(
        100,
        500,
        f"Student ID: {student_id}"
    )

    pdf.drawString(
        100,
        470,
        f"Certificate ID: {certificate_id}"
    )

    pdf.drawString(
        100,
        440,
        f"Issue Date: {issue_date}"
    )

    pdf.save()

    return FileResponse(
        path=file_path,
        media_type="application/pdf",
        filename=f"{certificate_id}.pdf"
    )