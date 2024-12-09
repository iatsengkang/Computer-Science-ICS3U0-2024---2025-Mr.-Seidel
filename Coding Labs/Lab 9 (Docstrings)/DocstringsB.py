#----------------------------------------------------------------------
# Name:        Docstrings B
# Purpose:     Creates a movie reccomendation system
#
# Created:     4-Dec-2024
# Updated:     5-Dec-2024
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
    '''
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
    '''
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
    while start != "1" and start != "2" and start != "3":
        start = input("invalid input, please try again\n")
        
    #exits program if 3 is inputted
    if start == "3":
        return database
    
    #adds a movie into the dictionairy if 2 is inputted
    elif start == "2":
        genre = input("what genre of movie do you want to watch?\n")
        
        while len(genre) == 0:
            genre = input("invalid input, please try again\n")
            
        min_rating = input("what is the minimum rating you want your movie to have?\n")        
        while len(min_rating) == 0 or not min_rating.replace(".", "").isdigit() or min_rating.count(".") > 1 or float(min_rating) < 0 or float(min_rating) > 10:
            min_rating = input("invalid input, please try again\n")
            
        print("Current reccomendations:")
        print(", ".join(get_recommendations(database, genre, min_rating)))
        
    #gives reccomendations based on additional inputs
    else:
        title = input("Enter the title of your movie: ")
        while len(title) == 0:
            title = input("invalid input, please try again\n")
            
        genre = input("Enter the genre of your movie: ")
        while len(genre) == 0:
            genre = input("invalid input, please try again\n")
            
        rating = input("Enter the rating of your movie: ")
        while rating == "" or not (rating.replace(".", "")).isdigit() or rating.count(".") > 1 or float(rating) < 0 or float(rating) > 10:
            rating = input("invalid input, please try again\n")
            
        database = add_movie(database, title, genre, rating)
        print("movie successfully added")


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
