#----------------------------------------------------------------------
# Name:        Dictionairys
# Purpose:     testing dictionairy functions
#
# Created:     24-Oct-2024
# Updated:     25-Oct-2024
#----------------------------------------------------------------------
# Task 1: Creating Dictionaries
your_favorites = {
"Dragon Blade": "Action",
"Cedar Rapids": "Comedy",
"My Fair Lady": "Drama",
"Ender's Game": "Sci-Fi",
"Hard Eight": "Thriller"
}
person1_favorites = {
"Cedar Rapids": 2011,
"Freedomland": 2006,
"Get Hard": 2015,
"The Thing": 1982,
"The Favourite": 2018
}
person2_favorites = {
"My Fair Lady": "George Cukor",
"Hard Eight": "Paul Thomas Anderson",
"Darby and the Dead": "Silas Howard",
"Jett Jackson: The Movie": "Shawn Levy",
"The Last King of Scotland": "Kevin Macdonald"
}
person3_favorites = {
"Dragon Blade": 5.9,
"Ender's Game": 6.6,
"Get Hard": 6.0,
"Europa": 7.5,
"Freeheld": 6.7
}
# Task 2: Accessing Dictionary Elements
# Use dictionary key access to print required information

#print(your_favorites["Dragon Blade"])
#print(your_favorites["Hard Eight"])
length = 1
for movie, favs in your_favorites.items():
    if length == 1:
        print(your_favorites[movie])
    if length == len(your_favorites):
        print(your_favorites[movie])
        break
    length += 1
print(person1_favorites["Get Hard"])
print(person2_favorites["My Fair Lady"])
print(person2_favorites["Hard Eight"])
print(person2_favorites["Darby and the Dead"])

# Use the 'in' operator to check for a movie's presence
if "Ender's Game" in person3_favorites:
    print("There is Ender's Game")
else:
    print("There is no Ender's Game")

# Task 3: Dictionaries in Lists
all_favorites = [your_favorites, person1_favorites, person2_favorites, person3_favorites]

# Access the third dictionary in the list, then get its second item
print(all_favorites[2]["Hard Eight"])

# Use a loop to count occurrences of specific movies across all dictionaries
count = 0
check = input("check for a movie\n")
for i in all_favorites:
    for movie in i:
        if movie == check:
            count += 1
print(count)

# Task 4: Dictionary Methods

# Use the keys() method to get all movies from your_favorites
for i in your_favorites.keys():
    print(i)
# Use the values() method to get all ratings from person3_favorites
for i in person3_favorites.values():
    print(i)
# Use the items() method to get and print all movie-director pairs from person2_favorites
for movies, keys in person2_favorites.items():
    print(str(movies) + ": " + str(keys))
            

