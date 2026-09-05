import schedule
import time

from reports.report_generator import generate_all_reports
#print(generate_all_reports())

def run_reports():
    generate_all_reports()
    print("All reports generated successfully")


schedule.every().day.at("14:30").do(run_reports)


while True:
    schedule.run_pending()
    time.sleep(1)