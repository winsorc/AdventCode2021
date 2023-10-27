#!/usr/bin/env python3

import re

def main():
 input=readInput()
 print(f"Total Forward Movements:", forward_movements())
 
  
#Opens file and removes end line characters
def readInput(): 
  file=open("planned_course.txt", "r")
  planned_course=file.read().splitlines()
  return planned_course
  
  
#Sums total of forward movements from input
def forward_movements():
  input = readInput()
  forward_numbers = []
  forward_lines = []
  foward_int = []
  for line in input: 
    forward_lines += re.findall("forward [0-9]", line) #Stores all forward entries in list
    for line in forward_lines:
      forward_numbers += (re.findall("[0-9]", line)) #Removes forward string to isolate numbers
  forward_int = [int(i) for i in forward_numbers] #Converts string numbers to int
  forward=sum(forward_int) #Sums all forward movements
  return forward

  
  
if __name__ == "__main__":
  main()