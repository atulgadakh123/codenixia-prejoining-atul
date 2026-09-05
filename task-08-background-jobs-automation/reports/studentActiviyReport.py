import json
import os
from datetime import datetime

from database import all_student


def generate_student_activity_report():

    students = all_student()

    report = {
        "report_name": "Student Activity Report",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_students": len(students),
        "students": [dict(student) for student in students]
    }

    os.makedirs("reports/generated", exist_ok=True)

    with open("reports/generated/student_activity_report.json", "w") as file:
        json.dump(report, file, indent=4)

    return "reports/generated/student_activity_report.json"