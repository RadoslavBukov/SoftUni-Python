from unittest import TestCase, main
from project.bookstore import Bookstore

class TestBookstore(TestCase):

    BOOKS_LIMIT = 5
    NAME = "Book"

    def setUp(self) -> None:
        self.bookstore = Bookstore(self.BOOKS_LIMIT)

# Test Init Method
    def test__bookstore_init__should_create_proper_object(self):
        self.assertEqual(self.BOOKS_LIMIT, self.bookstore.books_limit)
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(0, self.bookstore.total_sold_books)

    def test__bookstore_init_with_0_limit__should_rise_exceptions(self):
        with self.assertRaises(ValueError) as error:
            bookstore = Bookstore(0)
        self.assertEqual(f"Books limit of 0 is not valid", str(error.exception))

    def test__bookstore_init_with__less_than_0_limit__should_rise_exceptions(self):
        with self.assertRaises(ValueError) as error:
            bookstore = Bookstore(-1)
        self.assertEqual(f"Books limit of -1 is not valid", str(error.exception))

# Test Len Method
    def test__len_method_with_empty_dict__should_return_proper_len(self):
        length = len(self.bookstore)
        self.assertEqual(0, length)

    def test__len_method_with_not_empty_dict__should_return_proper_len(self):
        self.bookstore.availability_in_store_by_book_titles["Book"] = 2
        self.bookstore.availability_in_store_by_book_titles["Book2"] = 3
        length = len(self.bookstore)
        self.assertEqual(5, length)

# Test Receive Book Method:
    def test__receive_book_with_no_space__should_raise_exception(self):
        bookstore = Bookstore(1)
        with self.assertRaises(Exception) as error:
            bookstore.receive_book(self.NAME, 2)
        self.assertEqual(f"Books limit is reached. Cannot receive more books!", str(error.exception))

    def test__receive_book_with_enough_space_and_existing_book__should_increase_book_copies(self):
        self.bookstore.receive_book(self.NAME, 2)
        actual_result = self.bookstore.receive_book(self.NAME, 2)
        expected_result = {f"{self.NAME}":4}
        self.assertEqual(expected_result, self.bookstore.availability_in_store_by_book_titles)
        # Without this row - 93% in Judge:
        self.assertEqual(f"4 copies of {self.NAME} are available in the bookstore.", actual_result)

    def test__receive_book_with_enough_space_and_existing_book__should_add_book_copies(self):
        name2 = "Book2"
        self.bookstore.receive_book(self.NAME, 2)
        actual_result = self.bookstore.receive_book(name2, 2)
        expected_result = {f"{self.NAME}":2, f"{name2}":2}
        self.assertEqual(expected_result, self.bookstore.availability_in_store_by_book_titles)
        self.assertEqual(f"2 copies of {name2} are available in the bookstore.", actual_result)

    def test__receive_new_book__should_add_it_and_return_proper_message(self):
        book_copies = 5
        actual_result = self.bookstore.receive_book(self.NAME, book_copies)
        expected_result = f"{book_copies} copies of {self.NAME} are available in the bookstore."
        self.assertEqual(expected_result, actual_result)
        expected_result2 = {f"{self.NAME}": 5}
        self.assertEqual(expected_result2, self.bookstore.availability_in_store_by_book_titles)

# Test Sell Book Method:
    def test__sell_book_not_available_in_store__should_raise_exception(self):
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book(self.NAME, 2)
        self.assertEqual(f"Book {self.NAME} doesn't exist!", str(error.exception))
        self.assertEqual({}, self.bookstore.availability_in_store_by_book_titles)

    def test__sell_existing_book_with_not_enough_copies__should_raise_exception(self):
        book_copies = 5
        self.bookstore.receive_book(self.NAME, book_copies)
        with self.assertRaises(Exception) as error:
            self.bookstore.sell_book(self.NAME, 7)
        self.assertEqual(f"{self.NAME} has not enough copies to sell. Left: {book_copies}", str(error.exception))
        expected_result2 = {f"{self.NAME}": 5}
        self.assertEqual(expected_result2, self.bookstore.availability_in_store_by_book_titles)

    def test__sell_existing_book_and_enough_copies__should_remove_book(self):
        book_copies = 5
        self.bookstore.receive_book(self.NAME, book_copies)
        actual_result = self.bookstore.sell_book(self.NAME, book_copies)
        self.assertEqual(f"Sold {book_copies} copies of {self.NAME}", actual_result)
        length = len(self.bookstore)
        self.assertEqual(0, length)
        self.assertEqual(5, self.bookstore.total_sold_books)
        expected_result2 = {f"{self.NAME}": 0}
        self.assertEqual(expected_result2, self.bookstore.availability_in_store_by_book_titles)

    # Test STR Method:
    def test__str_method_with_no_books_and_no_sell_books__should_return_proper_message(self):
        actual_result = str(self.bookstore)
        expected_result = f"""Total sold books: 0
Current availability: 0"""
        self.assertEqual(expected_result, actual_result)

    def test__str_method_with_sold_out_book__should_return_proper_message(self):
        book_copies = 5
        self.bookstore.receive_book(self.NAME, book_copies)
        self.bookstore.sell_book(self.NAME, book_copies)
        actual_result = str(self.bookstore)
        expected_result = f"""Total sold books: 5
Current availability: 0
 - {self.NAME}: 0 copies"""
        self.assertEqual(expected_result, actual_result)

    def test__str_method_with_couple_of_books__should_return_proper_message(self):
        self.bookstore.receive_book(self.NAME, 1)
        self.bookstore.receive_book("Book2", 2)
        self.bookstore.receive_book("Book3", 1)

        actual_result = str(self.bookstore)
        expected_result = f"""Total sold books: 0
Current availability: 4
 - {self.NAME}: 1 copies
 - Book2: 2 copies
 - Book3: 1 copies"""
        self.assertEqual(expected_result, actual_result)


if __name__ == '__main__':
    main()