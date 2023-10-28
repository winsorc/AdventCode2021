#!/usr/bin/env python3

import re

def main():
 input=readInput()
 print(f"Horizontal Position:", forward_movements())
 print(f"We go down", descent())
 print(f"We go up", ascent())
 print(f"Final depth", (descent()-ascent()))
 
 
  
#Opens file and removes end line characters
def readInput(): 
  file=open("planned_course.txt", "r")
  planned_course=file.read().splitlines()
  return planned_course
  
  
#Sums total of forward movements from input
def forward_movements():
  input = readInput()
  start=0
  forward_numbers = []
  forward_lines = []
  foward_int = []
  for line in input: 
    forward_lines += re.findall("forward [0-9]", line) #Stores all forward entries in list
  for line in forward_lines:
    forward_numbers += (re.findall("[0-9]", line)) #Removes forward string to isolate numbers
  forward_int = [int(i) for i in forward_numbers] #Converts string numbers to int
  forward=sum(forward_int) #Sums all forward movements 
  horizontal_destination=(start+forward)
  return horizontal_destination

def descent():
  input = readInput()
  start_depth = 0
  down_lines=[]
  down_numbers=[]
  down_int=[]
  for line in input:
    down_lines += re.findall("down [0-9]", line)
  for line in down_lines:
    down_numbers += (re.findall("[0-9]", line))
  down_int = [int(i) for i in down_numbers]
  down=sum(down_int) + start_depth
  return down

def ascent():
  input = readInput()
  start_depth = 0
  up_lines=[]
  up_numbers=[]
  up_int=[]
  for line in input:
    up_lines += re.findall("up [0-9]", line)
  for line in up_lines:
    up_numbers += (re.findall("[0-9]", line))
  up_int = [int(i) for i in up_numbers]
  up=sum(up_int) + start_depth
  return up




  
  
if __name__ == "__main__":
  main()