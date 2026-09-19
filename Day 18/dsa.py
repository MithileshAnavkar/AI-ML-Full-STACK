class Shape:
    def area(self):
        print("Calculating area")


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        print("Circle area:", 3.14 * self.radius * self.radius)


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        print("Rectangle area:", self.length * self.width)


circle = Circle(5)
rectangle = Rectangle(10, 5)

circle.area()
rectangle.area()