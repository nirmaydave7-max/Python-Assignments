file=open("my_playlist.txt","w")
file.write("song 1")
file.write("song 2")
file.write("song 3")
file.write("song 4")
file.write("song 5")
file.close()
file=open("my_playlist.txt","r")
content=file.read()
a=content.upper()
print(a)
import csv
file=open("CLASSWORK/python_assignment/ipl match.csv","r")
lines=file.readlines()
file.close()
header=lines[0].strip().split(",")
winner_index=header.index("winner")
for line in lines[1:]:
    row=line.strip().split(",")
    print(row[winner_index])
import json

file = open("user_profile.json", "r")

data = json.load(file)

file.close()

print("Username:", data["username"])
print("Followers:", data["followers"])
from pathlib import Path
if Path("zomato_order.json").exists():
    print("file found")
else:
    print("file not found")

