from pydantic import BaseModel, EmailStr, Field
from datetime import date

# Student Create
class StudentCreate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=10,
        pattern=r"^[0-9]{10}$"
    )

    course: str = Field(
        min_length=2,
        max_length=15
    )


# Student Response
class StudentResponse(BaseModel):
    id: int
    name: str
    email: EmailStr
    phone: str
    course: str


# Student Update
class StudentUpdate(BaseModel):
    name: str = Field(
        min_length=2,
        max_length=50
    )

    email: EmailStr

    phone: str = Field(
        min_length=10,
        max_length=10,
        pattern=r"^[0-9]{10}$"
    )

    course: str = Field(
        min_length=2,
        max_length=15
    )


# User Registration
class UserCreate(BaseModel):
    name: str = Field(
        min_length=3,
        max_length=50
    )

    email: EmailStr

    password: str = Field(
        min_length=8,
        max_length=72
    )

    role: str


# User Login
class UserLogin(BaseModel):
    email: EmailStr

    password: str


## Payment Create
class paymentCreate(BaseModel):
    student_id: int
    total_course_fee: float
    registration_fee: float = 0
    amount_paid: float
    installment_number: int
    payment_date: date = Field(default_factory=date.today)


#Attedance
class AttendanceCreate(BaseModel):
    student_id: int
    course: str
    batch: str
    status: str
    attendance_date: date = Field(default_factory=date.today)


#certificate
class CertificateCreate(BaseModel):
    student_id: int
    student_name: str
    course: str
