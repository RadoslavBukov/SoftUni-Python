from unittest import TestCase, main
from mammal.project.mammal import Mammal

class TestMammal(TestCase):
    NAME = "Name"
    MAMMAL_TYPE = "TYPE"
    SOUND = "SOUND"
    KINGDOM = "animals"

    def setUp(self) -> None:
        self.mammal = Mammal(self.NAME, self.MAMMAL_TYPE, self.SOUND)

    def test__mammal_init__should_create_proper_obj(self):

        self.assertEqual(self.NAME, self.mammal.name)
        self.assertEqual(self.MAMMAL_TYPE, self.mammal.type)
        self.assertEqual(self.SOUND, self.mammal.sound)
        self.assertEqual(self.KINGDOM, self.mammal._Mammal__kingdom)

    def test__mammal_make_sound__should_return_proper_sound(self):
        expected_result = f"{self.NAME} makes {self.SOUND}"
        actual_result = self.mammal.make_sound()

        self.assertEqual(expected_result, actual_result)

    def test__mammal_get_kingdom__should_return_proper_kingdom(self):
        expected_result = "animals"
        actual_result = self.mammal.get_kingdom()

        self.assertEqual(expected_result, actual_result)

    def test__mammal_info__should_return_proper_info(self):
        expected_result = f"{self.NAME} is of type {self.mammal.type}"
        actual_result = self.mammal.info()
        self.assertEqual(expected_result, actual_result)

if __name__ == '__main__':
    main()