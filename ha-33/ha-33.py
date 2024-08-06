# ---------------- Task 1 ---------------------
class Employee:
    company = "First Company"

    def __init__(self, name, position):
        self.name = name
        self.position = position

    @classmethod
    def set_company(cls, com_name):
        cls.company = com_name

    def get_info(self):
        return f"Name: {self.name}, Pasition: {self.position}, Company: {self.company}"


employee1 = Employee("John", "Manager")
print(employee1.get_info())
Employee.set_company("Other Company")
employe2 = Employee("Alice", "Developer")
print(employe2.get_info())

# ---------------- Task 2 ---------------------

from abc import ABC, abstractmethod


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return (self.width + self.height) * 2


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

    def perimeter(self):
        return 2 * 3.14 * self.radius


rectangle = Rectangle(5, 3)
circle = Circle(2)

print(f"Rectangle area: {rectangle.area()}")
print(f"Rectangle perimeter: {rectangle.perimeter()}")
print(f"Circle area: {circle.area()}")
print(f"Circle perimeter: {circle.perimeter()}")
