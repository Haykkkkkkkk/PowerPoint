
class Semantik:
    def __init__(self, command):
        self.command = command
        self.existCommands = {
            "add slide": True,
            "del slide": True,
            "open slide": True,
            "add shape": True,
            "del shape": True,
            "print document": True,
            "exit": True,
            'help': True,
        }

    def isMatch(self):
        if self.existCommands.get(f"{self.command[0]}") is None:
            return ("unmatch")
        else:
            print("match")
            input_list = self.command[1:]
            result_dict = {input_list[i]: input_list[i + 1] for i in range(0, len(input_list), 2)}
            return self.command[0], result_dict
