import sys

def read_from_file():
  
  fileInput = open(sys.argv[1], "r") # opens the file assuming it is the first argument
  
  x = fileInput.readlines() # reads the file into a list

  for i in range(0,len(x)):
    formatted = x[i].rstrip() # removes the new lines
    x[i] = formatted

  print x # prints for checking

read_from_file() # function call to show it worked :)
