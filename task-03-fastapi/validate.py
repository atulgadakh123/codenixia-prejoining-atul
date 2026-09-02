def validate_student(name, email, phone, course):

    errors = []

    if not name.strip():
        errors.append("Name cannot be empty")

    if not email.strip():
        errors.append("Email cannot be empty")
    elif "@" not in email:
        errors.append("Invalid email")

    if not phone.strip():
        errors.append("Phone cannot be empty")
    elif not phone.isdigit():
        errors.append("Phone must contain only numbers")
    elif len(phone) != 10:
        errors.append("Phone must be exactly 10 digits")

    if not course.strip():
        errors.append("Course cannot be empty")

    if errors:
        raise ValueError("\n".join(errors))

    return True