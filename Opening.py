from fileinput import filename
import os, time

os.system("cls")

filenames = ["hangman0.txt", "hangman1.txt", "hangman2.txt", "hangman3.txt"]
frames = []

for name in filenames:
    with open(name, "r", encoding="utf8") as f:
        frames.append(f.readlines())

for i in range(8):
    for frame in frames:
        print("".join(frame))
        time.sleep(0.5)
        os.system("cls")
