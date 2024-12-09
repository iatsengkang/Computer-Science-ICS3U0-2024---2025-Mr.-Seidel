#-----------------------------------------------------------------------------
# Name: Grocery
# Purpose: add and removes things from a grocery list
#
# Author:
# Created: 9-Oct-2024
# Updated: 9-Oct-2024
#-----------------------------------------------------------------------------
groceryList = []

# Use while loop to use input() to fill list
item = input()
# Loop should stop when '!' is entered
while item != "!":
    # Items are added only if not already in list
    if item not in groceryList:
        groceryList.append(item)
        item = input()
    else:
        item = input()
    
# Sort and print the list
groceryList.sort()
print(groceryList)

# Print 3rd item, then 3rd LAST item
print(groceryList[2])
print(groceryList[-3])

# Print slice of 4th through 6th item
reverse = groceryList[3:6]
print(reverse)

# Print same slice BACKWARDS
reverse.sort(reverse = True)
print(reverse)

# Remove last item
del groceryList[-1]

# Take input(), remove that item if it exists
remove = input()
for i in range(len(groceryList)):
    if groceryList[i] == remove:
        del groceryList[i]
        break

# Print List
print(groceryList)