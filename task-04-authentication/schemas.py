from pydantic import BaseModel, EmailStr, Field


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