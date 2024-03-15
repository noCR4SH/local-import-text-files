def add_movie(movie_list):
    movie_name = input("Enter the movie name: ")
    movie_list.append(movie_name)
    print(f"Movie '{movie_name}' added!")
    return movie_list

def display_movies(movie_list):
    if not movie_list:
        print("The movie list is empty!")
    else:
        print("Favorite Movies:")
        for movie in movie_list:
            print(f"- {movie}")

def save_movies(movie_list, filename):
    try:
        with open(filename, 'w') as file:
            for movie in movie_list:
                file.write(movie + '\n')
        print("Movies saved succesfully!")
    except Exception as e:
        print(f"Error saving movies: {e}")

def load_movies(filename):
    try:
        with open(filename, 'r') as file:

            """
            movie_list = []
            for line in file.readlines():
                movie_list.append(line.strip())
            """

            movie_list = [line.strip() for line in file.readlines()]
        print("Movies loaded successfully!")
        return movie_list
    except Exception as e:
        print(f"Error loading movies: {e}")
        return []