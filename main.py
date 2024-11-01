from parsing import Parser
from metaClass_Factory import create_command
from slideEditor import SlideEditor
from document import Document
from slide import Slide

if __name__ == "__main__":
    comand_string = "add slide -pos 5"
    command_tuple = Parser(comand_string).parsing()
    document = Document()
    slideEditor = SlideEditor(Document)
    print(type(command_tuple))
    command = create_command(command_tuple)
    command.execute()
    print(command)
