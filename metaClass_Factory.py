from Editor import Editor
from slide import Slide
from item import Item
import sys

class CommandMeta(type):
    _commands = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)

        if name != "Command":  # Register only specific command classes, not the base Command
            cls._commands[name.lower()] = new_class
        return new_class

    @classmethod
    # Method to retrieve the command class by its name
    def get_command_class(cls, command_name):
        return cls._commands.get(command_name.lower())


class Command(metaclass=CommandMeta):
    def __init__(self, **kwargs):
        self.params = kwargs  # Save command parameters as a dictionary

    def execute(self):
        raise NotImplementedError(
            "This method should be overridden by subclasses")


# Dynamic creation of the AddSlide class
class AddSlide(Command):
    def execute(self):
        pos = self.params.get("pos")
        print(f"Executing AddSlide with pos={pos}")
        Editor().add_slide(Slide(pos))
        
 

class DelSlide(Command):
    def execute(self):
        pos = self.params.get("pos")
        print(f"Executing DelSLide with pos={pos}")
        Editor().del_slide(pos)
        



class OpenSlide(Command):
    def execute(self):
        pos = self.params.get("pos")
        print(f"Executing OPenSlide with pos={pos}")


class AddShape(Command):
    def execute(self):
        type = self.params.get("type")
        item = Item(type)
        if not self.params.get("x") is None:
            item.setX(self.params["x"])
        
        if not self.params.get("y") is None:
            item.setY(self.params["y"])
        
        if not self.params.get("color") is None:
            item.setColor(self.params["color"])
            
        print(self.params)
        print(f"Executing AddShape with geo : {item.geometry}, type = {item.type}, color : {item.color}")
        

        
class Exit(Command):
    def execute(self):
        print(f"Executing Exit")
        sys.exit()


class PrintDocument(Command):
    def execute(self):
        print("execute PrintDocument")
        Editor().print_document()


class PrintAllShapes(Command):
    def execute(self):
        print("execute print all shapes")
    
    
class Help(Command):
    def execute(self):
        help_text = """
        Available commands:
        - add slide  -pos <slide_index>         : Add a new slide with the given index.
        - del slide  -pos <slide_index>         : Delete the slide with the given ID.
        - open slide -pos <slide_index>        : Open a slide for editing.
        - add shape square -x <value> -y <value> -side <value> : Add a square shape with given coordinates and side length.
        - add shape circle -x <value> -y <value> -r <value>   : Add a circle shape with given coordinates and radius.
        - add shape rectangle <x> <y> <width> <height> : Add a rectangle shape with given coordinates and dimensions.
        - add shape triangle <x> <y> <width> <height>  : Add a triangle shape with given coordinates and dimensions.
        - del shape <shape_index>         : Delete the shape with the given ID from the current slide.
        - print all shapes             : Print all shapes in the currently opened slide.
        - print document               : Print the entire document structure.
        - help                         : Show this help message.
        - exit                         : Exit the program.
        """
        print(help_text)

# Factory function to create commands


def create_command(command_tuple):
    command_name, args = command_tuple
    command_class = CommandMeta.get_command_class(     # Retrieve the command class through the metaclass
        command_name.replace(" ", ""))

    if not command_class:
        raise ValueError(f"Unknown command: {command_name}")

    # Pass parameters to the command constructor
    return command_class(**{k: int(v) if v.isdigit() else v for k, v in args.items()})
