import json
import os
from datetime import datetime

from Data.attendance import get_all_attendance


def generate_attendance_report():

    attendance = get_all_attendance()

    report = {
        "report_name": "Attendance Report",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_records": len(attendance),
        "attendance": [dict(row) for row in attendance]
    }

    os.makedirs("reports/generated", exist_ok=True)

    with open("reports/generated/attendance_report.json", "w") as file:
        json.dump(report, file, indent=4, default=str)

    return "reports/generated/attendance_report.json"