import json
import os
from datetime import datetime

from feeDatabase import get_pending_payments


def generate_pending_fee_report():

    payments = get_pending_payments()

    report = {
        "report_name": "Pending Fee Report",
        "generated_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "total_pending": len(payments),
        "payments": [dict(payment) for payment in payments]
    }

    os.makedirs("reports/generated", exist_ok=True)

    with open("reports/generated/pending_fee_report.json", "w") as file:
        json.dump(report, file, indent=4, default=str)

    return "reports/generated/pending_fee_report.json"