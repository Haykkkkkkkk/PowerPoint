from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
 
    def draw(self):
        return f"Drawing a circle with radius {self.radius}"


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def draw(self):
        return f"Drawing a rectangle with width {self.width} and height {self.height}"


class ColorDecorator(Shape):
    def __init__(self, shape, color):
        self.shape = shape
        self.color = color

    def draw(self):
        return f"{self.shape.draw()} with color {self.color}"


class BorderSizeDecorator(Shape):
    def __init__(self, shape, size):
        self.shape = shape
        self.size = size

    def draw(self):
        return f"{self.shape.draw()} with size {self.size}"


class BorderStyleDecorator(Shape):
    def __init__(self, shape, border_style):
        self.shape = shape
        self.border_style = border_style

    def draw(self):
        return f"{self.shape.draw()} with border style '{self.border_style}'"


circle = Circle(radius=5)
circle_with_color = ColorDecorator(circle, color="red")


rectangle = Rectangle(width=4, height=6)
rectangle_with_border = BorderStyleDecorator(rectangle, border_style="solid")
rectangle_with_all = BorderSizeDecorator(rectangle_with_border, size = 2)


print(circle_with_color.draw())
print(rectangle_with_all.draw())
