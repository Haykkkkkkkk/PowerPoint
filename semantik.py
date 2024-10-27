class ArgumentsError(Exception):

    def __init__(self, message):
        super().__init__(message)


class Arguments:
    def __init__(self, args, length) -> None:
        self.args = args
        self.length = length + 1
        self.dict = self.check_args()

    def check_args(self):
        if self.length <= len(self.args):
            return ArgumentsError("Invalid count of args")
        else:
            a = self.list_to_dict()
            return a

    def list_to_dict(self):
        my_dict = {}
        for i in range(0, len(self.args) - 1, 2):
            my_dict[self.args[i]] = self.args[i + 1]
        if len(self.args) % 2 != 0:
            my_dict[self.args[-1]] = None

        return my_dict

    def get_dict(self):
        return self.dict


class Semantik:
    def __init__(self, command):
        self.command = command
        self.existCommands = {
            "add slide": Arguments(command[1:], 2),
            "del slide": Arguments(command[1:], 2),
            "open slide": Arguments(command[1:], 2),
            "add shape": Arguments(command[1:], 0),
            "del shape": Arguments(command[1:], 2),
            
            "exit": Arguments(command[1:], 0),
            'help': Arguments(command[1:], 0),
        }

    def isMatch(self):
        if self.existCommands.get(f"{self.command[0]}") is None:
            print("unmatch")

        else:
            print("match")
            a = self.existCommands[f"{self.command[0]}"].get_dict()
            return self.command[0], a
