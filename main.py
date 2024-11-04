from parsing import Parser
from metaClass_Factory import create_command


if __name__ == "__main__":
    while True:
        
        comand_string = input("Input command : ")
        command_tuple = Parser(comand_string).parsing()
        print(command_tuple)
        command = create_command(command_tuple)
        command.execute()
    
