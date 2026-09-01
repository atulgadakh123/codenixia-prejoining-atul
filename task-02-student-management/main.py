from student import Student
from database import (
    add_student,
    list_student,
    search_student,
    update_student,
    delete_student
)
from validate import validate_student


while True:

    print("\n--- Student Management System ---")
    print("1. Add Student")
    print("2. List Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = input("Enter your choice: ")


    # Add Student
    if choice == "1":

        name = input("Enter name: ")
        email = input("Enter email: ")
        phone = input("Enter phone: ")
        course = input("Enter course: ")

        try:

            validate_student(
                name,
                email,
                phone,
                course
            )

            student = Student(
                name,
                email,
                phone,
                course
            )

            add_student(
                student.name,
                student.email,
                student.phone,
                student.course
            )

        except ValueError as error:

            print("Error:")
            print(error)


    # List Students
    elif choice == "2":

        students = list_student()

        for student in students:

            print(
                "ID:", student[0],
                "| Name:", student[1],
                "| Email:", student[2],
                "| Phone:", student[3],
                "| Course:", student[4]
            )


    # Search Student
    elif choice == "3":

        student_id = int(
            input("Enter student ID to search: ")
        )

        student = search_student(student_id)

        if student:

            student_obj = Student(
                student[1],
                student[2],
                student[3],
                student[4],
                student[0]
            )

            student_obj.display_details()

        else:

            print("Student not found")


    # Update Student
    elif choice == "4":

        student_id = int(
            input("Enter student ID to update: ")
        )

        student = search_student(student_id)

        if not student:

            print("Student not found")

        else:

            name = input("Enter new name: ")
            email = input("Enter new email: ")
            phone = input("Enter new phone: ")
            course = input("Enter new course: ")

            try:

                validate_student(
                    name,
                    email,
                    phone,
                    course
                )

                update_student(
                    student_id,
                    name,
                    email,
                    phone,
                    course
                )

            except ValueError as error:

                print("Error:")
                print(error)


    # Delete Student
    elif choice == "5":

        student_id = int(
            input("Enter student ID to delete: ")
        )

        student = search_student(student_id)

        if not student:

            print("Student not found")

        else:

            delete_student(student_id)


    # Exit
    elif choice == "6":

        print("Thank you!")

        break


    else:

        print("Invalid choice")