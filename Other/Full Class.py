##+-----------------------------------------------------------------------
##
## Python Homework Assignments - (c) 2024 Chris Londal.  All Rights Reserved.
##
## File:        Full Class.py
##
## Description:
##
##   All Homeworks & All Problems in one document
##
## History:     Jan-19-2024     cfl429bc        Created
##              Month-Day-Year  cfl429bc        Editted
##
##------------------------------------------------------------------------
name = input("What is your name? ")
print(f"Hello {name} this is Chris Londal's entire set of homework assignments for CSCI1101.")
assignment = input("Which assignment would you like to run? ")
while not assignment == "STOP":
    assignment_num = int(assignment)
    problem = input("Which problem would you like to run? (a or b) ")

    if assignment_num == 0:
        print("Hello World!")

    if assignment_num == 1:
        if problem == "a" or problem == "A":
            yards = input("Enter number of yards: ")
            yards = int(yards)

            feet = input("Enter number of feet: ")
            feet = int(feet)

            inches = input("Enter number of inches: ")
            inches = int(inches)

            total = (yards * 3 * 12) + (feet * 12) + (inches)
            total = str(total)

            print("Total number of inches = " + total)
            
        if problem == "b" or problem == "B":
            from math import floor

            total = input("Enter number of inches: ")
            total = int(total)

            yards = total / 36
            yards = floor(yards)

            total = total - (yards * 36)
            yards = str(yards)

            feet = total / 12
            feet = floor(feet)

            total = total - (feet * 12)
            feet = str(feet)

            inches = total
            inches = str(inches)

            print("Number of yards = " + yards)
            print("Number of feet = " + feet)
            print("Number of inches = " + inches)

    if assignment_num == 2:
        print("This assignment has not been completed yet")

    if assignment_num == 3:
        print("This assignment has not been completed yet")

    if assignment_num == 4:
        print("This assignment has not been completed yet")

    assignment = input("Which assignment would you like to run next? (type STOP to stop) ")
print("Thank you come again!")
