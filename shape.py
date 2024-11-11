from item import Item
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, item :Item):
        self.index = item.index
        self.type = item.type
        self.geometry = item.geometry
        self.color = getattr(item, 'color', None)
        self.z_index = getattr(item, 'z_index', None)
    
    @abstractmethod
    def draw(self):
        """Abstract method that must be implemented in subclasses."""
        pass
    
    def __str__(self):
        return f"{self.__class__.__name__} (Type: {self.type}, Index: {self.index}, Geometry: {self.geometry}, Color: {self.color}, Z-Index: {self.z_index})"


class ShapeFactory:
    @staticmethod
    def create_shape(item):
        # Determine class name based on item.type
        class_name = f"{item.type.capitalize()}Shape"
        
        # Check and create the dynamic class
        if item.type.lower() == "square":
            shape_class = SquareShape
        elif item.type.lower() == "circle":
            shape_class = CircleShape
        else:
            raise ValueError(f"Unknown shape type: {item.type}")
        
        return shape_class(item)


class SquareShape(Shape):
    def draw(self):
        # Implementation of the draw method for a square
        print(f"Drawing a square with geometry {self.geometry}, color {self.color}, and z-index {self.z_index}")


class CircleShape(Shape):
    def draw(self):
        # Implementation of the draw method for a circle
        print(f"Drawing a circle with geometry {self.geometry}, color {self.color}, and z-index {self.z_index}")



item1 = Item(type="Square", index=1, geometry=(10, 10))
item1.setColor("red")
item1.setZ_index(5)

shape1 = ShapeFactory.create_shape(item1)
shape1.draw() 