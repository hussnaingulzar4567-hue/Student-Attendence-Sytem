import csv
from datetime import datetime
from pathlib import Path
from student_manager import load_students

ATTENDANCE_FILE = Path("attendance.csv")
ATTENDANCE_FIELDS = ["id", "name", "class", "date", "time", "status"]


def load_attendance():
    if not ATTENDANCE_FILE.exists() or ATTENDANCE_FILE.stat().st_size == 0:
        return []
    with ATTENDANCE_FILE.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def mark_attendance(fingerprint, now=None):
    fingerprint = fingerprint.strip()
    student = next(
        (s for s in load_students() if s["fingerprint"] == fingerprint),
        None
    )
    if student is None:
        raise ValueError("Fingerprint ID not recognized.")

    now = now or datetime.now()
    date_text = now.strftime("%Y-%m-%d")
    time_text = now.strftime("%H:%M:%S")
    records = load_attendance()

    if any(r["id"] == student["id"] and r["date"] == date_text
           for r in records):
        raise ValueError("Attendance is already marked for this student today.")

    new_file = not ATTENDANCE_FILE.exists() or ATTENDANCE_FILE.stat().st_size == 0
    with ATTENDANCE_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=ATTENDANCE_FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow({
            "id": student["id"],
            "name": student["name"],
            "class": student["class"],
            "date": date_text,
            "time": time_text,
            "status": "Present"
        })

    return {"id": student["id"], "name": student["name"],
            "class": student["class"], "date": date_text,
            "time": time_text, "status": "Present"}
