#-----------------------------------------------------------------------------
# Name:        tupples
# Purpose:     Does tupple operations
#
# Author:      760087
# Created:     17-Oct-2024
# Updated:     17-Oct-2024
#----------------------------------------------------------------------
# Task 1: Creating Tuples
your_favorites = ("Harry Potter and the Chamber of Secrets", "Hotel Mumbai", "Jumping Ship", "Collateral Damage", "Bones and All")
person1_favorites = ("Batman: Soul of the Dragon", "Blade Runner 2049", "Wish Dragon", "Stir of Echoes", "Jumping Ship")
person2_favorites = ("In the Earth", "Concrete Cowboy", "Wish Dragon", "Jumping Ship", "Gunpowder Milkshake")
person3_favorites = ("Whip It", "Nightbooks", "Harry Potter and the Chamber of Secrets", "Stir of Echoes", "Blade Runner 2049")

# Task 2: Accessing Tuple Elements
print(your_favorites[0])
print(your_favorites[-1])
print(person1_favorites[2])
print(person2_favorites[0:3])
if "Nightbooks" in person3_favorites:
    print("Nightbooks is my favorite movie")
else:
    print("Nightbooks is not my favorite movie")
    
# Task 3: Tuple Unpacking
movie_info = ("The Best Man Holiday", 1969, "cool dude")
title, year, director = movie_info
print(f'{title} was directed by {director} in {year}.')

# Task 4: Tuples in Lists
all_favorites = [your_favorites, person1_favorites, person2_favorites, person3_favorites]
print(all_favorites[2][1])
movie_check = input("check for a movie: ")
movie_num = 0
for i in all_favorites:
    for movie in i:
        if movie == movie_check:
            movie_num += 1
print(movie_num)

# Task 5: Tuple Methods
movie_check2 = input("check for another movie: ")
print(your_favorites.index(movie_check2))
movie_num2 = 0
for movie in person1_favorites:
    if movie == movie_check2:
        movie_num2 += 1
print(movie_num2)