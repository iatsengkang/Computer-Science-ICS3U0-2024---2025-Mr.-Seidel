#----------------------------------------------------------------------
# Name:        Exceptions B
# Purpose:     Creates a movie reccomendation system
#
# Created:     11-Dec-2024
# Updated:     12-Dec-2024
#----------------------------------------------------------------------

#makes default movie dictionairy
def create_movie_database():
    '''
    creats the default movie dictionairy

    Parameters
    ----------

    Returns
    -------
    dict
        default movie dictionairy
    '''
    return {
        "Movie1": ("action", 9.3),
        "Movie2": ("fantasy", 9.2),
        "Movie3": ("thriller", 9.1),
        "Movie4": ("horror", 9.0),
        "Movie5": ("slice of life", 8.9)
    } #these are examples, fill in with your own information

#function that adds a movie to the movie dictionairy
def add_movie(database, title, genre, rating):
    '''
    adds a movie to the database

    Parameters
    ----------
    dabatase : dict
        dictionairy of all movies
    title : str
        inputted title
    genre : str
        inputted genre
    rating : float not > 10 and not < 0

    Returns
    -------
    database
        updated dictionairy of the movies
        
    Raises
    ------
    TypeError
        If rating is not an int or float
    ValueError
        If rating larger than 10 or less than 0
    Exception
        If the function goes awry
    '''
    if not isinstance(rating, (float, int)):
        raise TypeError("rating expected to be a int or float")
    if rating > 10 or rating < 0:
        raise TypeError("rating expected to be in between 0 and 10")

    database[title] = (genre.lower(), float(rating))
    return database


#gets recommendations besed on given inputs
def get_recommendations(database, genre, min_rating):
    '''
    gives movie recomendations to user based on genre and minimum rating

    Parameters
    ----------
    dabatase : dict
        dictionairy of all movies
    genre : str
        inputted genre required
    min_rating : float not > 10 and not < 0

    Returns
    -------
    rec
        list of all movies that match the requirements

    Raises
    ------
    TypeError
        If min_rating is not an int or float
    ValueError
        If min_rating is larger than 10 or smaller than 0
    Exception
        If the function goes awry
    '''
    if not isinstance(min_rating, (float, int)):
        raise TypeError("min_rating expected to be a int or float")
    if float(min_rating) > 10 or float(min_rating) < 0:
        raise TypeError("min_rating expected to be in between 0 and 10")
    rec = []
    for movie in database:
        if database[movie][0] == genre.lower() and database[movie][1] >= float(min_rating):
            rec.append(movie.lower())
    return rec


# runs a different command based on user's input. Checks for validity
def run_menu(database):
    '''
    main menu

    Parameters
    ----------
    dabatase : dict
        dictionairy of all movies

    Returns
    -------
    database
        list of all movies
    '''
    run_program = True
    while run_program == True:

        start = input("input 1 to add a new movie to the database \ninput 2 to get movie recommendations \ninput 3 to exit the program\n")
        while start not in ["1", "2", "3"]:
            start = input("invalid input, please try again\n")

        #exits program if 3 is inputted, returns the database
        if start == "3":
            return database

        #adds a movie into the dictionairy if 2 is inputted, checks for errors
        elif start == "2":
            genre = input("what genre of movie do you want to watch?\n")

            min_rating = input("what is the minimum rating you want your movie to have?\n")    

            try:
                recommendations = get_recommendations(database, genre, min_rating)
                print("Current reccomendations:")
                print(", ".join(recommendations))
            except (ValueError, TypeError):
                print("minimum rating must be between 0 and 10")
                continue
            except Exception as e:
                print(f"unexpected error: {e}")
                break

        #gives reccomendations based on additional inputs, checks for errors
        else:
            title = input("Enter the title of your movie: ")

            genre = input("Enter the genre of your movie: ")

            rating = input("Enter the rating of your movie: ")
            try:
                database = add_movie(database, title, genre, rating)
                print("movie successfully added")
            except (ValueError, TypeError):
                print("rating must be between 0 and 10")
                continue
            except Exception as e:
                print(f"unexpected error: {e}")
                break

#begins the program
def main():
    '''
    gives movie recomendations to user based on genre and minimum rating

    Parameters
    ----------

    Returns
    -------
    databse
        list of all movies
    '''
    movie_db = create_movie_database()
    run_menu(movie_db)

main()
