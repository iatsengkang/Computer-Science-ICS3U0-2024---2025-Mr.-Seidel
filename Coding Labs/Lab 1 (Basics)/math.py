#-----------------------------------------------------------------------------
# Name:        Math
# Purpose:     Does math operations
#
# Author:      760087
# Created:     26-Sep-2024
# Updated:     26-Sep-2024
#----------------------------------------------------------------------
#asks user for a number to add 5 to
add = int(input("select a number to add 5 to "))
add = add + 5
print("Your number plus 5 is " + str(add))

#asks user for a number to subtract by 3
sub = int(input("select a number to subtract 3 to "))
sub = sub - 3
print("your number minus 3 is " + str(sub))

#asks user for a number to divide by 2
divide = int(input("select a number to divide by 2 "))
divide = divide / 2
print("your number divided by 2 is " + str(divide))

#asks user for a number to multiply by 10
multiply = int(input("select a number to multiply by 10 "))
multiply = 10 * multiply
print("your number multiplied by 10 is " + str(multiply))

#asks user for a number to cube the number
power = int(input("select a number to find the cube "))
power = power ** 3
print("your number cubed is " + str(power))