# Task 08 — Background Jobs & Automation

## Objective

Create an automated reporting system that generates:

* Pending Fee Report
* Attendance Report
* Student Activity Report

## Features

* Generate all reports manually
* Generate reports automatically using Python Scheduler
* Generate reports using FastAPI Background Tasks
* Save generated reports as JSON files

## Project Structure

```text
task-08-background-jobs-automation/
│
├── reports/
│   ├── pendingFeeReport.py
│   ├── attendanceReport.py
│   ├── studentActiviyReport.py
│   ├── report_generator.py
│   ├── reportScheduler.py
│   └── generated/
│
├── database.py
├── feeDatabase.py
├── attendanceDatabase.py
├── main.py
└── README.md
```

## Reports

### 1. Pending Fee Report

Gets pending fee records from the existing fee database and generates a JSON report.

### 2. Attendance Report

Gets attendance records from the existing attendance database and generates a JSON report.

### 3. Student Activity Report

Gets student records from the existing student database and generates a JSON report.

## Manual Report Generation

Run:

```powershell
python -m reports.reportScheduler
```

This generates all three reports.

## Automatic Scheduling

The system can generate reports automatically at a scheduled time using the Python `schedule` library.

## FastAPI Background Task

Reports can also be generated through:

```text
POST /reports/generate
```

The report generation runs as a background task.

## Generated Reports

Reports are saved inside:

```text
reports/generated/
```

## Dependencies

```text
fastapi
uvicorn
schedule
```

Install dependencies:

```powershell
pip install -r requirements.txt
```

## What I Learned

* Python scheduling
* Background tasks
* Basic automation
* Report generation
* Working with existing database data
* JSON file generation
* FastAPI background processing

## Known Limitations

* Scheduler must be running for scheduled jobs to execute.
* Reports are currently saved as JSON files.
* Task queue systems are not implemented; only their basic concept is understood.
