from project.movie_app import MovieApp
from project.movie_specification.fantasy import Fantasy
from project.movie_specification.action import Action
from project.movie_specification.thriller import Thriller

movie_app = MovieApp()
print(movie_app)
print(movie_app.register_user('Martin', 24))
user = movie_app.users_collection[0]
movie = Action('Die Hard', 1988, user, 18)
print(movie_app.upload_movie('Martin', movie))
print(movie_app.movies_collection[0].title)
print(movie_app.register_user('Alexandra', 25))
user2 = movie_app.users_collection[1]
print(movie_app.register_user('Lachko', 75))
user3 = movie_app.users_collection[2]
movie2 = Action('Free Guy', 2021, user2, 16)
movie3 = Thriller('Titanic', 2000, user, 17)
print(movie_app.upload_movie('Martin', movie3))
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.edit_movie('Alexandra', movie2, age_restriction=12))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.like_movie('Alexandra', movie))
print(movie_app.like_movie('Alexandra', movie3))
print(movie_app.like_movie('Lachko', movie3))
print(movie_app.dislike_movie('Martin', movie2))
print(movie_app.like_movie('Martin', movie2))
print(movie_app.delete_movie('Alexandra', movie2))
movie2 = Fantasy('The Lord of the Rings', 2003, user2, 14)
print(movie_app.upload_movie('Alexandra', movie2))
print(movie_app.display_movies())
print(movie_app)
print(movie.likes)
print(movie2.likes)
print(movie3.likes)
print(movie.details())
print(movie2.details())
print(movie3.details())