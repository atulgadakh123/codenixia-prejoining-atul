from fastapi import (
    FastAPI,
    HTTPException,
    Depends,
    status
)

from fastapi.security import (
    HTTPBearer,
    HTTPAuthorizationCredentials
)

from database import (
    create_student_table,
    create_user,
    add_student,
    all_student,
    search_student,
    update_student,
    delete_student,
    add_user,
    get_user_by_email
)
from feeDatabase import create_fee_table
from Data.attendance import create_attendace_table
from Data.certificateDatabase import create_certificate_table

from schemas import (
    StudentCreate,
    StudentResponse,
    StudentUpdate,
    UserCreate,
    UserLogin
)

from auth import (
    hash_password,
    verify_password,
    create_access_token,
    verify_access_token
)

from feeRoutes import router as fee_router
from routes.attedenceRouts import router as attendance_router
from routes.certificitRoutes import router as certificite_router

app = FastAPI()
app.include_router(fee_router)
app.include_router(attendance_router)
app.include_router(certificite_router)

security = HTTPBearer()


# Create tables
try:
    create_student_table()
    create_user()
    create_fee_table()
    create_attendace_table()
    create_certificate_table()

except Exception as e:
    print(f"Database initialization error: {e}")


# Get Current User
def get_current_user(
    credentials: HTTPAuthorizationCredentials = Depends(security)
):
    print("CREDENTIALS:", credentials)

    token = credentials.credentials

    print("TOKEN:", token)

    payload = verify_access_token(token)

    print("PAYLOAD:", payload)

    if payload is None:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return payload


# Role Authorization
def require_role(allowed_roles):

    def role_checker(
        current_user=Depends(get_current_user)
    ):
        if current_user["role"] not in allowed_roles:
            raise HTTPException(
                status_code=status.HTTP_403_FORBIDDEN,
                detail="You do not have permission"
            )

        return current_user

    return role_checker


# Home
@app.get("/")
def home():
    return {
        "message": "Task 4 Authentication API"
    }


# Register User
@app.post("/register")
def register_user(user: UserCreate):

    if user.role not in ["Student", "Staff", "Admin"]:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Invalid role"
        )

    try:
        existing_user = get_user_by_email(user.email)

        if existing_user is not None:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Email already exists"
            )

        hashed_password = hash_password(user.password)

        user_id = add_user(
            user.name,
            user.email,
            hashed_password,
            user.role
        )

        return {
            "message": "User registration successful",
            "user_id": user_id,
            "name": user.name,
            "email": user.email,
            "role": user.role
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="User registration failed"
        )


# Login
@app.post("/login")
def user_login(user: UserLogin):

    try:
        existing_user = get_user_by_email(user.email)

        if existing_user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        password_correct = verify_password(
            user.password,
            existing_user["password"]
        )

        if not password_correct:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid email or password"
            )

        token = create_access_token({
            "sub": existing_user["email"],
            "role": existing_user["role"]
        })

        return {
            "message": "Login successful",
            "access_token": token,
            "token_type": "bearer"
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Login failed"
        )


# Add Student
# Admin + Staff
@app.post(
    "/students",
    response_model=StudentResponse,
    status_code=status.HTTP_201_CREATED
)
def create_student(
    student: StudentCreate,
    current_user=Depends(
        require_role(["Admin", "Staff"])
    )
):
    try:
        student_id = add_student(
            student.name,
            student.email,
            student.phone,
            student.course
        )

        new_student = search_student(student_id)

        return dict(new_student)

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Student creation failed"
        )


# Get All Students
# Admin + Staff + Student
@app.get(
    "/students",
    response_model=list[StudentResponse]
)
def get_all_students(
    current_user=Depends(
        require_role(["Admin", "Staff", "Student"])
    )
):
    try:
        students = all_student()

        return [
            dict(student)
            for student in students
        ]

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get students"
        )


# Get Student By ID
# Admin + Staff + Student
@app.get(
    "/students/{student_id}",
    response_model=StudentResponse
)
def get_student(
    student_id: int,
    current_user=Depends(
        require_role(["Admin", "Staff", "Student"])
    )
):
    try:
        student = search_student(student_id)

        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        return dict(student)

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Failed to get student"
        )


# Update Student
# Admin + Staff
@app.put(
    "/students/{student_id}",
    response_model=StudentResponse
)
def update_studentbyid(
    student_id: int,
    student: StudentUpdate,
    current_user=Depends(
        require_role(["Admin", "Staff"])
    )
):
    try:
        existing_student = search_student(student_id)

        if existing_student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        update_student(
            student_id,
            student.name,
            student.email,
            student.phone,
            student.course
        )

        updated_student = search_student(student_id)

        return dict(updated_student)

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Student update failed"
        )


# Delete Student
# Admin only
@app.delete(
    "/students/{student_id}"
)
def delete_studentbyid(
    student_id: int,
    current_user=Depends(
        require_role(["Admin"])
    )
):
    try:
        student = search_student(student_id)

        if student is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Student not found"
            )

        delete_student(student_id)

        return {
            "message": "Student deleted successfully"
        }

    except HTTPException:
        raise

    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Student deletion failed"
        )