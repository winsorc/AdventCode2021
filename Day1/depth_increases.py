#!/usr/bin/env python3

def main():
  numbers = readInput() #assign input list to variable
  print(f"Depth Increases", {depth_increases(numbers)}, "times.")

#Defines function to open input file
def readInput():
  file=open("depth_input.txt", "r")
  depth_input = file.read().splitlines() #removes white space/seperators to isolate number in each line
  depth_input = [ int(i) for i in depth_input ] #converts string number to int for comparison
  #print(depth_input) optional test to confirm int conversion and input accuracy
  return depth_input

#Defines function to calculate number of times depth increases
def depth_increases(numbers):
  numbers = readInput() #assign input list to variable
  prev_num = numbers[0] #initialize previous number position for comparing increases
  count = 0 #initalizes variable to count number of increases
#iterate through each number in input, excluding first number
  for num in numbers[1:]:
    if num > prev_num: #checks if current number is larger than previous number
      count +=1 #increments count
    prev_num = num #Moves current number to previous number
    
  return count
  
  

if __name__ == "__main__":
  main()

      

  


      
      



    
    

