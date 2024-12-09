#-----------------------------------------------------------------------------
# Name:        Grade
# Purpose:     provides input based on grade
#
# Author:      Iat Seng
# Created:     1/Oct/2024
# Updated:     1/Oct/2024
#-----------------------------------------------------------------------------

#asks user for their grade, turns it into a integer.
grade = int(input())

#prints "Not Passing." if grade is between 0 and 49, inclusive.
if grade >=0 and grade <= 49:
    print("Not Passing.")
    
#prints "Needs Improvement." if grade is between 50 and 69, inclusive.
elif grade >=50 and grade <= 69:
    print("Needs Improvement.")
    
#prints "Meeting Expectations." if grade is between 70 and 79, inclusive.
elif grade >=70 and grade <= 79:
    print("Meeting Expectations.")
    
#prints "Meeting Expectations." if grade is between 80 and 100, inclusive.
elif grade >=80 and grade <= 100:
    print("Exceeding Expectations.")
    
#prints "Invalid Grade" if all previous checks failed
else:
    print("Invalid Grade")
