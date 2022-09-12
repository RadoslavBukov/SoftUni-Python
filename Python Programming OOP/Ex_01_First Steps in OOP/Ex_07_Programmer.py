"""
Test Code	                                                                    Output
programmer = Programmer("John", "Java", 50)                                     John does not know Python
print(programmer.watch_course("Python Masterclass", "Python", 84))              John already knows Java
print(programmer.change_language("Java", 30))                                   John needs 50 more skills
print(programmer.change_language("Python", 100))                                John watched Java: zero to hero
print(programmer.watch_course("Java: zero to hero", "Java", 50))                John switched from Java to Python
print(programmer.change_language("Python", 100))                                John watched Python Masterclass
print(programmer.watch_course("Python Masterclass", "Python", 84))
"""
class Programmer:

    def __init__(self, name, language, skills):
       self.name = name
       self.language = language
       self.skills = skills

    def watch_course(self, course_name, language, skills_earned):
        # if self.language != language:
        #     return f"{self.name} does not know {language}"
        # else:
        #     self.skills += skills_earned
        #     return f"{self.name} watched {course_name}"
        if self.language != language:
            return f"{self.name} does not know {language}"
        self.skills += skills_earned
        return f"{self.name} watched {course_name}"


    def change_language(self, new_language, skills_needed):
        # if self.skills < skills_needed:
        #     return f"{self.name} needs {skills_needed-self.skills} more skills"
        # else:
        #     if self.language == new_language:
        #         return f"{self.name} already knows {new_language}"
        #     else:
        #         previous_language = self.language
        #         self.language = new_language
        #         return f"{self.name} switched from {previous_language} to {new_language}"
        if self.language == new_language:
            return f"{self.name} already knows {new_language}"
        if self.skills < skills_needed:
            return f"{self.name} needs {skills_needed-self.skills} more skills"

        previous_language = self.language
        self.language = new_language
        return f"{self.name} switched from {previous_language} to {new_language}"


programmer = Programmer("John", "Java", 50)
print(programmer.watch_course("Python Masterclass", "Python", 84))
print(programmer.change_language("Java", 30))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Java: zero to hero", "Java", 50))
print(programmer.change_language("Python", 100))
print(programmer.watch_course("Python Masterclass", "Python", 84))
