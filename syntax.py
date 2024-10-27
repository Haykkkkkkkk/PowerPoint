class SyntaxAnalyseError(Exception):

    def __init__(self, message):
        super().__init__(message)


class StateMachine:
    state = "Start"
    def transition(self, token):
        if StateMachine.state == "Start":
            if token.token_type == "command":
                StateMachine.state = "Command"
            elif token.token_type in ["option", "value"]:
                StateMachine.state = "Error"

        elif StateMachine.state == "Command":
            if token.token_type == "command":
                StateMachine.state = "Command"
            elif token.token_type == "option":
                StateMachine.state = "Option"
            elif token.token_type == "value":
                StateMachine.state = "Error"

        elif StateMachine.state == "Option":
            if token.token_type == "value":
                StateMachine.state = "Value"
            elif token.token_type in ["command", "option"]:
                StateMachine.state = "Error"

        elif StateMachine.state == "Value":
            if token.token_type is None:
                StateMachine.state = "Finished"
            elif token.token_type == "option":
                StateMachine.state = "Option"
            elif token.token_type == "value":
                StateMachine.state = "Error"
            elif token.token_type == "command":
                StateMachine.state = "Error"
        
        return StateMachine.state
    

