from unittest import TestCase, main
from student.project.student import Student

class TestStudent(TestCase):
    NAME = "Username"

    def setUp(self) -> None:
        self.student = Student(self.NAME)

# Test Init Method
    def test__student_init_without_courses__should_create_obj_without_courses(self):
        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test__student_init_wit_courses__should_create_obj_with_courses(self):
        course_name = "Python OOP"
        courses = {course_name: ['note1', 'note2']}

        student = Student(self.NAME, courses)

        self.assertEqual(self.NAME, self.student.name)
        self.assertEqual(courses, student.courses)

# Test Enroll Method
    def test__student_enroll__when_course_is_already_enrolled__should_update_course_notes(self):
        course_name = "Python"
        courses = {course_name: ['note1', 'note2']}

        student = Student(self.NAME, courses)

        result = student.enroll(course_name, ['note3', 'note4'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note1', 'note2', 'note3', 'note4'], student.courses[course_name])

    def test__student_enroll__without_course_notes__should_update_course_notes(self):
        course_name = "Python"
        course_notes = ['note1', 'note2']

        result = self.student.enroll(course_name, course_notes)

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test__student_enroll__without_course_notes_Y__should_update_course_notes(self):
        course_name = "Python"
        course_notes = ['note1', 'note2']

        result = self.student.enroll(course_name, course_notes, "Y")

        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test__student_enroll__without_course_notes_when_invalid_add_course__should_add_course(self):
        course_name = "Python"
        course_notes = ['note1', 'note2']

        result = self.student.enroll(course_name, course_notes, "N")

        self.assertEqual("Course has been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])

# Test Add Notes Method
    def test__add_notes_with_not_existing_course__should_raise_error(self):
        with self.assertRaises(Exception) as error:
            self.student.add_notes("Python", "Note3")
        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

    def test__add_notes_with_existing_course__should_append_notes(self):
        course_name = "Python"
        courses = {course_name: ['note1', 'note2']}
        student = Student(self.NAME, courses)

        result = student.add_notes(course_name, 'note3')

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['note1', 'note2', 'note3'], student.courses[course_name])

    def test__leave_course_that_not_exist__should_rise_exception(self):
        self.student.enroll("Python", [])

        with self.assertRaises(Exception) as error:
            self.student.leave_course("Python OOP")
        self.assertEqual("Cannot remove course. Course not found.", str(error.exception))

    def test__leave_course_that_exist__should_remove_course(self):
        course_name = "Python"
        student = Student(self.NAME, {course_name: []})

        result = student.leave_course(course_name)
        self.assertEqual("Course has been removed", result)
        self.assertTrue(course_name not in student.courses)

if __name__ == '__main__':
    main()