# DATA-609: Assignment 03
# Ken Noppinger (knoppin1@umbc.edu)
#
# The Problem:
#
# Write a program that generates 100 random integers between 0 and 9. 
#
# Print them in a 10 by 10 matrix neatly arranged with surrounding asterisks (*):
#
#  ***********************
#  * 5 1 5 6 2 7 8 6 4 2 *
#  * 2 3 7 0 6 9 2 4 2 8 *
#  * 0 0 8 6 4 1 7 2 7 6 *
#  * 0 1 9 0 0 8 5 8 6 8 *
#  * 4 1 0 5 5 7 4 6 4 4 *
#  * 6 0 2 0 1 9 8 2 3 9 *
#  * 4 0 4 8 1 7 6 6 2 1 *
#  * 1 7 6 8 5 4 1 9 6 7 *
#  * 6 4 7 9 9 3 8 2 6 1 *
#  * 9 0 6 4 0 1 0 6 9 9 *
#  ***********************
#
# The Requirements :
#
# - Program and test the solution in both:
#   - Jupyter notebook file
#   - Python script (.py)
# - Upload both files to your GitHub repository
# - Submit the link of your GitHub repo to BB.
# 
# Hints :
# - Use Python standard library random to generate one random number at a time. 
# - Or use NumPy random library to generate 100 random number altogether in one shot.
# - Probably should use nested loop (i.e., a loop within in another loop) since dealing with a 10 x 10 matrix.

import random

# Constants 

# Matrix is 10 x 10
INTEGERS_PER_LINE = 10
INTEGER_LINES = 10

# Range for integers is 0 through 9
MIN_INTEGER = 0
MAX_INTEGER = 9

DOUBLE_ASTERISK = "**"
ASTERISK = "*"

def print_border_line():
    
    """print_border_line - Print a border line of asterisks using the proper length for specified matrix."""
    
    # Print a border prefix
    print(DOUBLE_ASTERISK, end = "")
    
    # Print a line of asterisks
    for i in range(0, INTEGERS_PER_LINE * 2):
        print(ASTERISK, end = "")
        
    # Print a border suffix
    print(ASTERISK, end = '\n')
    
def main():

    # Create a random list of integers within the minimum and maximum integer range to represent the matrix
    random_integer_list = [random.randint(MIN_INTEGER, MAX_INTEGER) for i in range(0, INTEGERS_PER_LINE * INTEGER_LINES)]
    
    # Print top border of the matrix.    
    print_border_line()

    # Execute nested loop to print the matrix
    for i in range(0, INTEGER_LINES):
        
        # Print a border prefix for this line of the matrix.
        print(ASTERISK, end = " ")
        
        # Loop through and print integers for the line.
        for j in range(0, INTEGERS_PER_LINE):
            print(random_integer_list[i * INTEGERS_PER_LINE + j], end = " ")
            
        # Print a border suffix for this line of the matrix.
        print(ASTERISK, end = '\n')
        
    # Print bottom border of the matrix.
    print_border_line()     
    
if __name__ == "__main__":
    main()
