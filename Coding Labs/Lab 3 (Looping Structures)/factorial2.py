#-----------------------------------------------------------------------------
# Name:        factorial
# Purpose:     finds the factorial of a positive number
# Author:      760087
# Created:     2-Oct-2024
# Updated:     3-Oct-2024
#----------------------------------------------------------------------

#asks user for factorial 
factorial = int(input())
run = factorial

#prints error if factorial is less than 0
if factorial < 0:
    print("Error.")
    
#prints 1 if factorial is 0
elif factorial == 0:
    print("1")
    
#prints the factorial of the input
else:
    while run > 0:
        run = run - 1
        if run > 0:
            factorial = factorial * run
    print(factorial)