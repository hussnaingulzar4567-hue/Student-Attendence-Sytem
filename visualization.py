from pathlib import Path
import matplotlib.pyplot as plt
from reports import attendance_statistics

OUTPUT_DIR = Path("outputs")
OUTPUT_DIR.mkdir(exist_ok=True)


def create_attendance_chart(path=None):
    path = Path(path) if path else OUTPUT_DIR / "attendance_chart.png"
    _, report = attendance_statistics()

    names = [row["name"] for row in report]
    percentages = [row["attendance_percentage"] for row in report]

    fig, ax = plt.subplots(figsize=(10, 5.5))
    if names:
        bars = ax.bar(names, percentages)
        ax.bar_label(bars, fmt="%.1f%%", padding=3)
        ax.set_ylim(0, 110)
        ax.tick_params(axis="x", rotation=25)
    else:
        ax.text(0.5, 0.5, "No student attendance data yet",
                ha="center", va="center", transform=ax.transAxes)
        ax.set_xticks([])
        ax.set_yticks([])

    ax.set_title("Student Attendance Percentage")
    ax.set_ylabel("Attendance (%)")
    ax.grid(axis="y", alpha=0.25)
    fig.tight_layout()
    fig.savefig(path, dpi=180, bbox_inches="tight")
    plt.close(fig)
    return path


def create_linkedin_visual(path=None):
    """Create a presentation graphic using Pillow; works in Colab or desktop."""
    from PIL import Image, ImageDraw, ImageFont

    path = Path(path) if path else OUTPUT_DIR / "linkedin_project.png"
    path.parent.mkdir(parents=True, exist_ok=True)

    width, height = 1600, 1000
    image = Image.new("RGB", (width, height), "#F1F5FB")
    draw = ImageDraw.Draw(image)

    def get_font(size, bold=False):
        options = (
            ["/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
             "/usr/share/fonts/truetype/liberation2/LiberationSans-Bold.ttf"]
            if bold else
            ["/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
             "/usr/share/fonts/truetype/liberation2/LiberationSans-Regular.ttf"]
        )
        for font_path in options:
            try:
                return ImageFont.truetype(font_path, size)
            except OSError:
                continue
        return ImageFont.load_default()

    def txt(x, y, s, size=22, color="#172B4D", bold=False):
        draw.text((x, y), s, font=get_font(size, bold), fill=color)

    def card(box, fill="#FFFFFF", outline="#D7E1EF"):
        draw.rounded_rectangle(box, radius=20, fill=fill, outline=outline, width=2)

    draw.rectangle((0, 0, width, 135), fill="#10366A")
    txt(55, 25, "SCHOOL ATTENDANCE MANAGEMENT SYSTEM", 36, "#FFFFFF", True)
    txt(58, 82, "PYTHON PROJECT  |  STUDENT RECORDS  |  ATTENDANCE REPORTS",
        19, "#B9DDFF", True)

    card((40, 170, 520, 570))
    txt(70, 200, "PROJECT OVERVIEW", 25, "#10366A", True)
    overview = [
        "A lightweight Python application",
        "for managing student attendance.",
        "",
        "Features:",
        "• Student registration",
        "• Simulated fingerprint ID",
        "• Daily attendance marking",
        "• CSV data storage",
        "• Attendance statistics",
        "• Report export and chart"
    ]
    yy = 250
    for line in overview:
        txt(72, yy, line, 19, "#263A56", line == "Features:")
        yy += 30

    card((40, 600, 520, 930), "#E5F1FF")
    txt(70, 630, "TECHNOLOGY STACK", 25, "#10366A", True)
    txt(75, 690, "Python — Core logic", 21)
    txt(75, 735, "CSV — Data persistence", 21)
    txt(75, 780, "Matplotlib — Charts", 21)
    txt(75, 825, "Pillow — Portfolio graphic", 21)
    txt(75, 875, "Note: fingerprint ID is simulated.", 16, "#B45309", True)

    card((555, 170, 1560, 570))
    txt(590, 200, "SYSTEM WORKFLOW", 25, "#10366A", True)
    steps = [
        ("01", "Register", "Save student details"),
        ("02", "Verify ID", "Enter simulated fingerprint ID"),
        ("03", "Mark", "Record date and time"),
        ("04", "Report", "View CSV reports and statistics")
    ]
    x_positions = [590, 830, 1070, 1310]
    for x, (num, title, desc) in zip(x_positions, steps):
        draw.rounded_rectangle((x, 270, x+205, 445), radius=16,
                               fill=["#07866B", "#1976D2", "#7045C5", "#F08B32"][int(num)-1])
        txt(x+20, 290, num, 25, "#FFFFFF", True)
        txt(x+20, 335, title, 23, "#FFFFFF", True)
        txt(x+20, 380, desc, 14, "#FFFFFF")
    txt(600, 490, "Organized modules • Reusable functions • CSV persistence",
        19, "#263A56", True)

    card((555, 600, 1560, 930))
    txt(590, 630, "ATTENDANCE ANALYTICS", 25, "#10366A", True)
    _, report = attendance_statistics()
    if report:
        names = [r["name"] for r in report[:6]]
        values = [r["attendance_percentage"] for r in report[:6]]
        max_width = 600
        for i, (name, value) in enumerate(zip(names, values)):
            y = 695 + i*35
            txt(600, y, name[:18], 16)
            bar_x = 820
            draw.rounded_rectangle((bar_x, y, bar_x+max_width, y+20),
                                   radius=7, fill="#DFE7F2")
            fill_width = int(max_width * max(0, min(value, 100)) / 100)
            if fill_width:
                draw.rounded_rectangle((bar_x, y, bar_x+fill_width, y+20),
                                       radius=7, fill="#1976D2")
            txt(bar_x+max_width+15, y-2, f"{value:.1f}%", 15, "#10366A", True)
    else:
        txt(600, 720, "Sample dashboard: register students and mark attendance",
            20, "#61718A")
        txt(600, 770, "to populate your real attendance statistics.", 20, "#61718A")

    draw.rectangle((0, 960, width, height), fill="#10366A")
    txt(250, 972, "PYTHON  +  CSV  +  REPORTS  =  SMARTER ATTENDANCE RECORDS",
        20, "#FFFFFF", True)

    image.save(path, "PNG", optimize=True)
    return path
