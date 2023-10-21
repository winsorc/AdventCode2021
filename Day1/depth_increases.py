#!/usr/bin/env python3

def main():
  numbers = readInput() #assign input list to variable
  print(f"Depth Increases", {depth_increases(numbers)}, "times.")
  print(f"Depth Window Increases", {depth_windows(numbers)}, "times")

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
#Iterate through each number in input, excluding first number
  for num in numbers[1:]:
    if num > prev_num: #checks if current number is larger than previous number
      count +=1 #increments count
    prev_num = num #Moves current number to previous number
    
  return count
#Defines function to compare depths in sliding window
def depth_windows (numbers):
  numbers = readInput() 
  window_size = 3 
  count  = 0
  total_window=[] #Defines new list to store window depth increases
  for i in range(len(numbers) - window_size + 1): #Iterates input and keeps last number of previous window
    total_window.append((sum(numbers[i: i + window_size]))) #Appends the sum of each window to a new list
  for x in range (1, len(total_window)): 
    if total_window[x - 1] < total_window[x]: #Checks if previous window is smaller
      count+=1 #Counts an increase
  return count  
    
      
    
    
     
     

  

if __name__ == "__main__":
  main()

      

  


      
      



    
    

