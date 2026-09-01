#Student Management System

##Description

    The Student Management System is a Python-based application for managing student records using SQLite.

    The application allows users to add, list, search, update, and delete student records.


#Features
    Add a new student
    List all students
    Search student by ID
    View student details
    Update student information
    Delete a student
    Validate student information
    Handle validation errors
    Store student data in SQLite database
    Technologies Used
    Python
    SQLite
    Object-Oriented Programming (OOP)
    SQL

##Project Structure
    task-02-student-management/
    │
    ├── database/
    │   └── student.db
    │
    ├── main.py
    ├── student.py
    ├── database.py
    ├── validate.py
    └── README.md

##File Description
    main.py — Main application and menu system.
    student.py — Contains the Student class.
    database.py — Handles SQLite database operations.
    validate.py — Handles student data validation.
    database/student.db — SQLite database file.
    README.md — Project documentation.


##Database

    The application uses SQLite to store student records.

##The student table contains:

    id
    name
    email
    phone
    course

##How to Run
    1. Activate the virtual environment
    venv\Scripts\activate
    2. Run the application
    python main.py


##Application Menu
--- Student Management System ---
    1. Add Student
    2. List Students
    3. Search Student
    4. Update Student
    5. Delete Student
    6. Exit


##Validation

    The application validates:

    Name should not be empty.
    Email should not be empty.
    Email should contain @.
    Phone should not be empty.
    Phone should contain only numbers.
    Phone should be exactly 10 digits.
    Course should not be empty.


##Sample Input
    Enter your choice: 1
    Enter name: Atul
    Enter email: atul@gmail.com
    Enter phone: 9876543210
    Enter course: Python
    Sample Output
    Student added successfully


#Error Handling

    The application uses exception handling to handle validation errors and display meaningful error messages to the user.

#Example:

    Error:
    Invalid email
    Phone must contain only numbers
    Known Limitations
    The application currently uses a command-line interface.
    Authentication and authorization are not implemented.
    The application uses SQLite as the database.


##What I Learned

    Through this project, I learned:

##Object-Oriented Programming in Python
    Classes and objects
    SQLite database integration
    SQL CRUD operations
    Database connection handling
    Data validation
    Exception handling
    Building a menu-driven application
    Organizing Python project files