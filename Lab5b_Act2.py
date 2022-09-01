# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Name:         Caleb Lewis
# Section:      521
# Assignment:   Lab 2b
# Date:         10 04 2021
#

# Prompt the user for a stress value
x0 = float(input("Enter the strain: "))
# If the value is not in the range of the graph, print an error message and end the program, otherwise continue
if(x0<0 or x0>.27):
    print("Strain is undefined in that region")
# Find the two nearest points on the graph to the left and right of the user’s input using a series of if-else statements
# Set x1, y1, x2, and y2 to the values of those points
else:
    if(x0<=.01):
        x1 = 0
        y1 = 0
        x2 = .01
        y2 = 43
    elif(x0<=.06):
        x1 = .01
        y1 = 43
        x2 = .06
        y2 = 43.5
    elif(x0<=.18):
        x1 = .06
        y1 = 43.5
        x2 = .18
        y2 = 60
    else:
        x1 = .18
        y1 = 60
        x2 = .27
        y2 = 51
# Plug the values into the linear interpolation equation
    y0 = ((y2-y1)/(x2-x1))*(x0-x1)+y1
# Print y0
    print("The stress is approximately {:.1f}".format(y0))




