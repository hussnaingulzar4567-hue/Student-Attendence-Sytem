# Optional Google Colab helper:
# Upload the project ZIP to Colab, then run:
# !unzip -o School_Attendance_System.zip
# %cd School_Attendance_System
# !pip install -r requirements.txt

from visualization import create_linkedin_visual
from IPython.display import display

image_path = create_linkedin_visual()
display(__import__("PIL").Image.open(image_path))
print("Image saved to:", image_path)
