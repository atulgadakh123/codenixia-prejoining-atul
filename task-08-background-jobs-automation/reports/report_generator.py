from reports.pendingFeeReport import generate_pending_fee_report
from reports.attendanceReport import generate_attendance_report
from reports.studentActiviyReport import generate_student_activity_report


def generate_all_reports():

    pending_fee = generate_pending_fee_report()
    attendance = generate_attendance_report()
    student_activity = generate_student_activity_report()

    return {
        "pending_fee_report": pending_fee,
        "attendance_report": attendance,
        "student_activity_report": student_activity
    }