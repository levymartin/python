#!/usr/bin/env python3

print("Hello, this is computer quiz.")
playing = input("Do you want to play quiz game? ")

if playing.lower() != "yes":
    quit()

print("Okay! Lets play :)!")
score = 0
answer = input("What does CPU stands for? ")
if answer == "central processing unit":
    print("Correct!")
    score += 1 # score = score + 1
else:
    print("Incorrect!")

answer = input("What does RAM stands for? ")
if answer == "random processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does GPU stands for? ")
if answer == "graphics processing unit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

answer = input("What does ASIC stands for? ")
if answer == "application specific integrated circuit":
    print("Correct!")
    score += 1
else:
    print("Incorrect!")

print("You got " + str(score) + " questions correct! Congratulations!")
print("You got " + str((score / 4) * 100) + "%.")
