from functions import add_movie, display_movies, save_movies, load_movies

movie_list = []

while True:
    print("\n1. Add Movie")
    print("2. Display Movies")
    print("3. Save Movies")
    print("4. Load Movies")
    print("5. Exit")

    choice = input("Select an option: ")

    if choice == "1" or choice == "Add Movie":
        movie_list = add_movie(movie_list)
    elif choice == "2":
        display_movies(movie_list)
    elif choice == "3":
        filename = input("Provide filename (without extension): ")
        save_movies(movie_list, filename + ".txt")
    elif choice == "4":
        filename = input("Provide filename to read (without extension): ")
        movie_list = load_movies(filename + ".txt")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option!")