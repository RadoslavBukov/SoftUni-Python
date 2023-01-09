from project.user import User
from project.movie_specification.movie import Movie

class MovieApp:

    def __init__(self):
        self.movies_collection = []
        self.users_collection = []

    def register_user(self, username, age):
        user = self.__find_user_by_name(username)
        if user:
            raise Exception("User already exists!")

        user = User(username, age)
        self.users_collection.append(user)
        return f"{username} registered successfully."

    def upload_movie(self, username, movie: Movie):
        user = self.__find_user_by_name(username)
        if user not in self.users_collection:
            raise Exception("This user does not exist!")
        self.__check_is_owner(user, movie)
        self.__check_movie_is_uploaded(movie)

        self.movies_collection.append(movie)
        user.movie_owned.append(movie)
        return f"{username} successfully added {movie.title} movie."

    def edit_movie(self, username, movie : Movie, **kwargs):
        user = self.__find_user_by_name(username)
        self.__check_movie_is_not_uploaded(movie)
        self.__check_is_owner(user, movie)

       # Variant 1
        movie.title = kwargs.get("title", movie.title)
        movie.year = kwargs.get("year", movie.year)
        movie.age_restriction = kwargs.get("age_restriction", movie.age_restriction)

        # # Same as:
        #  if "title" in kwargs:
        #      movie.title = kwargs["title"]
        #  else:
        #      movie.title = movie.title

        # # Variant 2
        # for key in ["title", "year", "age_restriction"]:
        #     if key not in kwargs:
        #         continue
        #     setattr(movie, key, kwargs[key])

        return f"{username} successfully edited {movie.title} movie."

    def delete_movie(self, username, movie:Movie):
        user = self.__find_user_by_name(username)
        self.__check_movie_is_not_uploaded(movie)
        self.__check_is_owner(user, movie)
        self.movies_collection.remove(movie)
        user.movie_owned.remove(movie)
        return f"{username} successfully delete {movie.title} movie."

    def like_movie(self, username, movie : Movie):
        user = self.__find_user_by_name(username)
        self.__check_is_not_owner(user, movie)
        if movie in user.movie_liked:
            raise Exception(f"{username} already liked the movie {movie.title}!")
        user.movie_liked.append(movie)
        movie.likes += 1
        return f"{username} liked {movie.title} movie."

    def dislike_movie(self, username, movie:Movie):
        user = self.__find_user_by_name(username)
        if movie not in user.movie_liked:
            raise Exception(f"{username} has not liked the movie {movie.title}!")
        user.movie_liked.remove(movie)
        movie.likes -= 1
        return f"{username} disliked {movie.title} movie."

    def display_movies(self):
        if not self.movies_collection:
            return "No movies found."
        sorted_movies = [movie.details() for movie in sorted(self.movies_collection, key=lambda x: (-x.year, x.title))]
        return '\n'.join(sorted_movies)
        # # Variant 2
        # sorted_movies = sorted(self.movies_collection, key=lambda x: (-x.year, x.title))
        # return '\n'.join(movie.details() for movie in sorted_movies)

    def __find_user_by_name(self, username):
        for user in self.users_collection:
            if user.username == username:
                return user

    def __check_is_owner(self, user, movie:Movie):
        if user.username != movie.owner.username:
            raise Exception(f"{user.username} is not the owner of the movie {movie.title}!")
        return True

    def __check_is_not_owner(self, user, movie:Movie):
        if user.username == movie.owner.username:
            raise Exception(f"{user.username} is the owner of the movie {movie.title}!")
        return True

    def __check_movie_is_uploaded(self, movie:Movie):
        if movie in self.movies_collection:
            raise Exception("Movie already added to the collection!")
        return True

    def __check_movie_is_not_uploaded(self, movie:Movie):
        if movie not in self.movies_collection:
            raise Exception(f"The movie {movie.title} is not uploaded!")
        return True

    def __str__(self):
        result = ''
        if not self.users_collection:
            result += "All users: No users.\n"
        else:
            result += "All users: "+', '.join(user.username for user in self.users_collection) + "\n"
        if not self.users_collection:
            result += "All movies: No movies.\n"
        else:
            result += "All users: "+', '.join(movie.title for movie in self.movies_collection)
        return result.strip()