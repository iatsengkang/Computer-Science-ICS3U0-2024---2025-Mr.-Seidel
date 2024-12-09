#----------------------------------------------------------------------
# Name:        Sets test
# Purpose:     testing sets
#
# Created:     11-Apr-2024
# Updated:     24-Apr-2024
#----------------------------------------------------------------------
# Task 1: Creating Sets
your_favorites = {"August: Osage County", "Force of Nature", "The Phantom of the Opera", "Enough Said", "Eternal Sunshine of the Spotless Mind", "Flubber", "Rent"}
person1_favorites = {"The Best of Me", "The Phantom of the Opera", "102 Dalmatians", "Thunderstruck", "August: Osage County", "American Fable", "Flubber"}
person2_favorites = {"Chicken Little", "Alice", "The Dukes of Hazzard", "Rent", "Takers", "Thunderstruck", "Flubber"}
person3_favorites = {"Set It Up", "The Thirteenth Year", "Black Rock", "Enough Said", "Chicken Little", "Flubber", "Vivo"}

# Task 2: Set Operations
print(your_favorites.intersection(person1_favorites, person2_favorites))
print(your_favorites.union(person1_favorites, person2_favorites, person3_favorites))
print(person3_favorites.difference(your_favorites, person1_favorites, person2_favorites))
print(your_favorites.symmetric_difference(person1_favorites))

# Task 3: Set Methods
print(your_favorites.add("Prom"))
print(your_favorites.add("A Glimpse Inside the Mind of Charles Swan III"))

person2_favorites.discard("Alice"))
print(person3_favorites.issubset(your_favorites.union(person1_favorites, person2_favorites, person3_favorites)))
print(len(your_favorites.union(person1_favorites, person2_favorites, person3_favorites)))

# Task 4: Other Set Operations
print(your_favorites.difference_update(person1_favorites))
print(person2_favorites.intersection_update(person3_favorites))
print(your_favorites.isdisjoint(person3_favorites))

# Task 5: Analyzing Preferences

print(your_favorites.intersection(person1_favorites, person2_favorites, person3_favorites))
print(

# Create a set of all unique movies across all favorite sets
# Find movies that are unique to each person's favorites
# Use set operations to answer questions about movie preferences across the group