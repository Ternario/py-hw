# ---------------- Task 1 ---------------------

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def calculate_area(self):
        return self.height * self.width


new_rectangle = Rectangle(4, 5)
print(new_rectangle.calculate_area())


# ---------------- Task 2 ---------------------

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        return f"Student {self.name} is {self.age} year old"


new_student = Student("Andrii", 27)
print(new_student.display_info())
