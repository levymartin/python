#!/usr/bin/env python3

MENU_PROMPT = "\nEnter 'a' to ad a movie, 'l' to see list of movies, 'f' to find movie by title or 'q' to quit"
movies = []

def add_movie():
    title = input("Enter movies name: ")
    director = input("Enter director name: ")
    year = input("Enter year of release:")

    movies.append({
    "title": title,
    "director": director,
    "year": year
    })

def show_movies():
    for movie in movies:
        print_movie(movie)

def print_movie(movie):
        print(f'Title: {movie["title"]}')
        print(f"Director: {movie['director']}")
        print(f"Release year: {movie['year']}")

def find_movie():
    search_title = input("Enter movie title you are looking for: ")
    for movie in movies:
        if movie["title"] == search_title:
            print_movie(movie)

def menu():
    selection = input(MENU_PROMPT)
    while selection != "q":
        if selection == "a":
            add_ movie()
        elif selection == "l":
            show_movies()
        elif selection == "f":
            find_movie()
        else:
            print("Uknown command.")

        selection = input(MENU_PROMPT)
menu()
