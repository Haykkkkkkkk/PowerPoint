from parsing import Parser


class CommandMeta(type):
    _commands = {}

    def __new__(cls, name, bases, attrs):
        new_class = super().__new__(cls, name, bases, attrs)
        
        if name != "Command": # Register only specific command classes, not the base Command
            cls._commands[name.lower()] = new_class
        return new_class

    @classmethod
    def get_command_class(cls, command_name):  # Method to retrieve the command class by its name
        return cls._commands.get(command_name.lower())


class Command(metaclass=CommandMeta):
    def __init__(self, **kwargs):
        self.params = kwargs # Save command parameters as a dictionary

    def execute(self):
        raise NotImplementedError(
            "This method should be overridden by subclasses")


# Dynamic creation of the AddSlide class
class AddSlide(Command):
    def execute(self):
        pos = self.params.get("pos")
        print(f"Executing AddSlide with pos={pos}")

class DelSlide(Command):
    def execute(self):
        pos = self.params.get("pos")
        print(f"Executing DelSLide with pos={pos}")
        
class OpenSlide(Command):
    def execute(self):
        pos = self.params.get("pos")
        print(f"Executing OPenSlide with pos={pos}")


# Factory function to create commands
def create_command(command_tuple):
    command_name, args = command_tuple
    command_class = CommandMeta.get_command_class(     # Retrieve the command class through the metaclass
        command_name.replace(" ", ""))

    if not command_class:
        raise ValueError(f"Unknown command: {command_name}")

    # Pass parameters to the command constructor
    return command_class(**{k: int(v) if v.isdigit() else v for k, v in args.items()})




if __name__ == "__main__":
    comand_string = "open slide -pos 5"
    command_tuple = Parser(comand_string).parsing()
    print(type(command_tuple))
    command = create_command(command_tuple)
    command.execute()