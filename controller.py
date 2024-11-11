from parsing import Parser
from metaClass_Factory import create_command


class Controller:
    def __init__(self) -> None:
        pass

    def run(self):
        while True:
            comand_string = input("Input command : ")
            command_tuple = Parser(comand_string).parsing()
            print(command_tuple)
            command = create_command(command_tuple)
            command.execute()
