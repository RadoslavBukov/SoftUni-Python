from unittest import TestCase, main
from project.movie import Movie

class TestMovie(TestCase):

    NAME = "Movie"
    YEAR = 2000
    RATING = 5.0
    ACTOR_NAME = "Actor"

    OLDEST_MOVIE_YEAR = 1887

    def setUp(self) -> None:
        self.movie = Movie(self.NAME, self.YEAR, self.RATING)

# Test Init Method
    def test__movie_init__should_create_proper_object(self):
        self.assertEqual(self.NAME, self.movie.name)
        self.assertEqual(self.YEAR, self.movie.year)
        self.assertEqual(self.RATING, self.movie.rating)
        self.assertEqual([], self.movie.actors)

    def test__movie_init_with_wrong_name__should_rise_exceptions(self):
        with self.assertRaises(ValueError) as error:
            movie = Movie("", self.YEAR, self.RATING)
        self.assertEqual(f"Name cannot be an empty string!", str(error.exception))

    def test__movie_init_with_wrong_year__should_rise_exceptions(self):
        with self.assertRaises(ValueError) as error:
            movie = Movie(self.NAME, self.OLDEST_MOVIE_YEAR-1, self.RATING)
        self.assertEqual("Year is not valid!", str(error.exception))

# Test Add Actor Method
    def test__movie_add_actor_with_no_existing_actor__should_add_actor(self):
        self.movie.add_actor(self.ACTOR_NAME)
        self.assertEqual(f"['{self.ACTOR_NAME}']", str(self.movie.actors))

    def test__movie_add_actor_with_existing_actor__should_return_error_massage(self):
        self.movie.add_actor(self.ACTOR_NAME)
        message = self.movie.add_actor(self.ACTOR_NAME)
        self.assertEqual(f"{self.ACTOR_NAME} is already added in the list of actors!", message)
        self.assertEqual(f"['{self.ACTOR_NAME}']", str(self.movie.actors))

# Test GT Method
    def test__movie_gt_method_with_rating_greater_than_other__should_return_proper_message(self):
        other_movie_name = "Other"
        other_movie = Movie(other_movie_name, self.YEAR, self.RATING-1)
        self.assertGreater(self.movie, other_movie)
        message = self.movie > other_movie
        self.assertEqual(f'"{self.movie.name}" is better than "{other_movie.name}"', message)

    def test__movie_gt_method_with_rating_less_than_other__should_return_proper_message(self):
        other_movie_name = "Other"
        other_movie = Movie(other_movie_name, self.YEAR, self.RATING+1)
        self.assertGreater(self.movie, other_movie)
        message = other_movie > self.movie
        self.assertEqual(f'"{other_movie.name}" is better than "{self.movie.name}"', message)

    def test__movie_gt_method_with_rating_equal_with_other__should_return_proper_message(self):
        other_movie_name = "Other"
        other_movie = Movie(other_movie_name, self.YEAR, self.RATING)
        message = self.movie > other_movie
        self.assertEqual(f'"{other_movie.name}" is better than "{self.movie.name}"', message)


# Test repr Method
    def test__movie_repr_method__should_return_correct_string(self):
        self.movie.add_actor(self.ACTOR_NAME)
        expected_str = f"Name: {self.NAME}\n" \
               f"Year of Release: {self.YEAR}\n" \
               f"Rating: {self.RATING:.2f}\n" \
               f"Cast: {self.ACTOR_NAME}"
        actual_result = self.movie.__repr__()
        self.assertEqual(expected_str, actual_result)

if __name__ == '__main__':
    main()