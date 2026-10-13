# School Attendance Management System

A beginner-friendly Python project for registering students, marking attendance, saving data in CSV files, exporting reports, and creating attendance charts and a LinkedIn portfolio image.

## Features
- Register students with unique IDs
- Simulated fingerprint ID lookup (not real biometric scanning)
- Mark one attendance record per student per day
- View student and attendance records
- Estimate attendance statistics from recorded attendance dates
- Export CSV reports
- Generate an attendance chart and LinkedIn project visualization

## Project files
- `attendance_system.py`: main menu and application entry point
- `student_manager.py`: student registration and CSV loading
- `attendance_manager.py`: attendance logic
- `reports.py`: statistics and report export
- `visualization.py`: chart and LinkedIn image creation
- `requirements.txt`: external dependencies

## Run locally (Windows, macOS, or Linux)
1. Install Python 3.10 or newer.
2. Open a terminal in this project folder.
3. Install dependencies:
   ```bash
   python -m pip install -r requirements.txt
   ```
4. Start the application:
   ```bash
   python attendance_system.py
   ```
5. Choose menu option 1 to register students, then option 2 to mark attendance.

The `students.csv` and `attendance.csv` files are created when records are saved. Generated files are placed in `outputs/`.

## Run in Google Colab
This is a terminal-input Python project, so it can run in Colab cells:
```python
!pip install -r requirements.txt
!python attendance_system.py
```
Use the interactive prompts in the cell output. To create the LinkedIn graphic without running the menu:
```python
from visualization import create_linkedin_visual
display(create_linkedin_visual())
```
If the project files are not in the Colab session, upload and extract the project ZIP first.

## Attendance statistics note
The program estimates absences using the dates present in `attendance.csv`. It does not know official school holidays or days when school was closed, so this is an estimate rather than an official attendance register.

## LinkedIn portfolio image
Select menu option 8 or run `create_linkedin_visual()` to create `outputs/linkedin_project.png`. The visualization uses real statistics if records exist; otherwise it shows a clearly illustrative empty-state dashboard.

## Limitations
- Fingerprint verification is simulated using a text ID.
- No real biometric device is connected.
- CSV files are intended for a small learning project, not a multi-user production system.
