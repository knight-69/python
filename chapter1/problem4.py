# use chatgpt for problem 4 
import os

# Function to print the contents of a directory
def print_directory_contents(directory):
    try:
        # Get the list of files and directories in the specified directory
        contents = os.listdir(directory)
        
        # Print each item in the directory
        for item in contents:
            print(item)
    except Exception as e:
        print(f"Error: {e}")


