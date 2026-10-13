import csv
from pathlib import Path

STUDENT_FILE = Path("students.csv")
STUDENT_FIELDS = ["id", "name", "class", "fingerprint"]


def load_students():
    if not STUDENT_FILE.exists() or STUDENT_FILE.stat().st_size == 0:
        return []
    with STUDENT_FILE.open("r", newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f))


def register_student(student_id, name, student_class, fingerprint):
    student_id, name = student_id.strip(), name.strip()
    student_class, fingerprint = student_class.strip(), fingerprint.strip()

    if not all([student_id, name, student_class, fingerprint]):
        raise ValueError("All fields are required.")

    students = load_students()
    if any(s["id"] == student_id for s in students):
        raise ValueError("Student ID already exists.")
    if any(s["fingerprint"] == fingerprint for s in students):
        raise ValueError("Fingerprint ID already exists.")

    new_file = not STUDENT_FILE.exists() or STUDENT_FILE.stat().st_size == 0
    with STUDENT_FILE.open("a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=STUDENT_FIELDS)
        if new_file:
            writer.writeheader()
        writer.writerow({
            "id": student_id,
            "name": name,
            "class": student_class,
            "fingerprint": fingerprint
        })
    return {"id": student_id, "name": name,
            "class": student_class, "fingerprint": fingerprint}
