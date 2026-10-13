from student_manager import register_student, load_students
from attendance_manager import mark_attendance, load_attendance
from reports import attendance_statistics, export_attendance_report, export_statistics
from visualization import create_attendance_chart, create_linkedin_visual


def show_students():
    students = load_students()
    print("\n--- REGISTERED STUDENTS ---")
    if not students:
        print("No students registered yet.")
        return
    for s in students:
        print(f'{s["id"]} | {s["name"]} | {s["class"]}')


def show_attendance():
    records = load_attendance()
    print("\n--- ATTENDANCE REPORT ---")
    if not records:
        print("No attendance records yet.")
        return
    for r in records:
        print(f'{r["date"]} {r["time"]} | {r["id"]} | {r["name"]} | {r["class"]} | {r["status"]}')


def show_statistics():
    total_days, report = attendance_statistics()
    print(f"\nRecorded dates: {total_days}")
    if not report:
        print("No students registered.")
        return
    print("\nID | Student | Present | Estimated absent | Attendance")
    print("-" * 65)
    for r in report:
        print(f'{r["id"]} | {r["name"]} | {r["present_days"]} | '
              f'{r["estimated_absent_days"]} | {r["attendance_percentage"]:.2f}%')
    print("\nAbsences are estimates based only on dates present in the attendance file.")


def main():
    while True:
        print("\n" + "=" * 52)
        print(" SCHOOL ATTENDANCE MANAGEMENT SYSTEM")
        print("=" * 52)
        print("1. Register student")
        print("2. Mark attendance (simulated fingerprint ID)")
        print("3. View students")
        print("4. View attendance report")
        print("5. View attendance statistics")
        print("6. Export CSV reports")
        print("7. Create attendance chart")
        print("8. Create LinkedIn project image")
        print("9. Exit")

        choice = input("Choose (1-9): ").strip()
        try:
            if choice == "1":
                print("\n--- Student Registration ---")
                result = register_student(
                    input("Student ID: "),
                    input("Student name: "),
                    input("Class: "),
                    input("Simulated fingerprint ID: ")
                )
                print("Registered:", result["name"])
            elif choice == "2":
                result = mark_attendance(input("Enter simulated fingerprint ID: "))
                print(f'Attendance marked: {result["name"]} | {result["date"]} {result["time"]}')
            elif choice == "3":
                show_students()
            elif choice == "4":
                show_attendance()
            elif choice == "5":
                show_statistics()
            elif choice == "6":
                print("Exported:", export_attendance_report())
                print("Exported:", export_statistics())
            elif choice == "7":
                print("Chart saved:", create_attendance_chart())
            elif choice == "8":
                print("LinkedIn image saved:", create_linkedin_visual())
            elif choice == "9":
                print("Thank you for using the system.")
                break
            else:
                print("Please enter a number from 1 to 9.")
        except (ValueError, OSError) as exc:
            print("Error:", exc)


if __name__ == "__main__":
    main()
