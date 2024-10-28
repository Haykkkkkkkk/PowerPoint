from parsing import Parser
from metaClass_Factory import create_command




if __name__ == "__main__":
    comand_string = "add slide -pos 20"
    command_tuple = Parser(comand_string).parsing()
    print(type(command_tuple))
    command = create_command(command_tuple)
    command.execute()