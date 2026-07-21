import math
print(math.sqrt(9))
print(math.factorial(24))
print(math.radians(180))

import os

files = os.listdir()

print("Image files in the current directory:")

for file in files:
    if file.endswith(".jpg") or file.endswith(".png"):
        print(file)

from datetime import datetime

date = input("Enter a date (YYYY-MM-DD): ")

try:
    user_date = datetime.strptime(date, "%Y-%m-%d")
    print("Day of the week:", user_date.strftime("%A"))
except ValueError:
    print("Invalid date format. Please enter the date as YYYY-MM-DD.")

from insta_utils import format_follower_count

print(format_follower_count(1500))
print(format_follower_count(2500000))
print(format_follower_count(34000))