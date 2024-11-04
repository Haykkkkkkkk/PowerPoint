from syntax import StateMachine, SyntaxAnalyseError
from Lexical_analysis import Token, TokenizerError, CommandTokenizer
from semantik import Semantik



class Parser:
    def __init__(self, command_string) -> None:
        self.command_string = command_string

    def parsing(self):
        command = []
        tokenizer = CommandTokenizer()
        sm = StateMachine()
        for word in self.command_string.split():
            token = tokenizer.tokenize_command(word)
            sm.transition(token)
            print(token)
            if StateMachine.state == "Error":
                raise SyntaxAnalyseError("Error")
            command.append(token)
        real_command = self.get_command(command)
        CommandTokenizer._start_comander = True
        StateMachine.state = "Start"
        return Semantik(real_command).isMatch()

    def get_command(self, command):
        co = ""
        for t in command:
            if t.token_type == "command":
                co = co + t.value + " "
        real_command = []
        real_command.append(co.strip())

        for t in command:
            if not t.token_type == "command":
                real_command.append(t.value)
        return real_command



