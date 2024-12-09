#-----------------------------------------------------------------------------
# Name:        Adding
# Purpose:     Prints the sum all numbers between begin and end inclusive
# Author:      760087
# Created:     2-Oct-2024
# Updated:     2-Oct-2024
#----------------------------------------------------------------------

#asks user for 2 inputs; begin and end
begin = int(input())
end = int(input())

#prints error if begin is larger than end
if begin > end:
    print("Error.")

#prints the sum all numbers between begin and end inclusive
else:
    for i in range (begin, end):
        begin += end
        end = end - 1
    print(begin)
