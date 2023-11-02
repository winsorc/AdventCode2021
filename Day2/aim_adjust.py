#! usr/bin/env python 3
file = open("planned_course.txt", "r")
lines = file.readlines()

position = 0
depth = 0
aim = 0

for line in lines:
    step, number = line.split()

    if step == "forward":
        position += int(number)
        depth += aim * int(number)
    elif step == "down":
        aim += int(number)
    elif step  == "up":
        aim -= int(number)

print(depth * position)