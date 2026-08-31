# Task 01 - Python Data Processing

## Objective
 Build a Python application that processes student data from a CSV file.

# Features
-read student data from csv
-Validate student record
-Detect missing fields
-Validate email addresses
-validate marks
-Separates valid and invalid records
-Generate error report
-Generate summary

# project structer


task-01-python-data-processor/
│
├── data/
│   └── students.csv
│
├── output/
│   ├── valid_students.csv
│   ├── invalid_students.csv
│   └── error_report.csv
│
├── src/
│   └── main.py
│
├── README.md
└── requirements.txt

## Requirements

- Python 3.x

## Setup

1. Clone the repository.
2. Open the project folder.
3. Make sure Python is installed.
4. Run the application:

python src/main.py

# Input
data /students.csv
Student Name
Email
College
Course
Marks
Phone
Attendance

# output
output/valid_students.csv
output/invalid_students.csv
output/error_report.csv

## Validation Rules

- Student Name must not be empty.
- Email must not be empty and must contain `@` and `.`.
- College must not be empty.
- Course must not be empty.
- Phone must not be empty.
- Attendance must not be empty.
- Marks must not be empty and must be between 0 and 100.

## Known Limitations
- Email validation uses a basic format check.
- Phone number format is not validated.
- The application processes CSV input only.

## What I Learned

- Reading CSV files using Python
- Working with lists and dictionaries
- Using functions and validation logic
- Handling exceptions using try/except
- Separating valid and invalid records
- Generating CSV reports
- Using Git for version control