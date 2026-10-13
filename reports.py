import csv
from pathlib import Path
from attendance_manager import load_attendance
from student_manager import load_students

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def attendance_statistics():
    students = load_students()
    records = load_attendance()
    school_days = {r["date"] for r in records}

    report = []
    total_days = len(school_days)
    for student in students:
        present_dates = {
            r["date"] for r in records
            if r["id"] == student["id"] and r["status"] == "Present"
        }
        present = len(present_dates)
        absent = max(0, total_days - present)
        percentage = (present / total_days * 100) if total_days else 0.0
        report.append({
            "id": student["id"],
            "name": student["name"],
            "class": student["class"],
            "present_days": present,
            "estimated_absent_days": absent,
            "attendance_percentage": round(percentage, 2)
        })
    return total_days, report


def export_attendance_report(path=None):
    path = Path(path) if path else OUTPUT_DIR / "attendance_report.csv"
    records = load_attendance()
    fields = ["id", "name", "class", "date", "time", "status"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(records)
    return path


def export_statistics(path=None):
    path = Path(path) if path else OUTPUT_DIR / "attendance_statistics.csv"
    _, report = attendance_statistics()
    fields = ["id", "name", "class", "present_days",
              "estimated_absent_days", "attendance_percentage"]
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fields)
        writer.writeheader()
        writer.writerows(report)
    return path
