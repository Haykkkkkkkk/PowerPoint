class TokenizerError(Exception):

    def __init__(self, message):
        super().__init__(message)


class Token:
    def __init__(self, token_type, value):
        self.token_type = token_type  # 'command', 'option', 'value'
        self.value = value

    def __repr__(self):
        return f"Token(type='{self.token_type}', value='{self.value}')"


class CommandTokenizer:

    _start_comander = True

    def __init__(self):
        self.tokens = None

    def tokenize_command(self, word):
        if CommandTokenizer._start_comander:
            if word.isalpha():
                return Token("command", word)

        if word.startswith('-') and word[1:].isalpha():
            CommandTokenizer._start_comander = False
            return Token("option", word[1:])
        elif word.isalpha() or word.isdigit():
            CommandTokenizer._start_comander = False
            return Token("value", word)
        else:
            raise TokenizerError("TokenizerError: Unknown Token format")
