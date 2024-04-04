import os
import random
from datetime import datetime


today = datetime.now().date()

day_of_year = (today - datetime(today.year, 1, 1)).days + 1

is_green = random.random() < 0.9

if is_green:
    commit_content = "🟩"
else:
    commit_content = "🟥"

with open("commit.txt", "w") as file:
    file.write(commit_content)

os.system("git add commit.txt")
os.system(f"git commit -m 'Commit on day {day_of_year}'")