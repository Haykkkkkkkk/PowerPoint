class Slide:

    def __init__(self, pos) -> None:
        self.pos = pos
        self.shapes = []

    def __repr__(self) -> str:
        return f" Slide(Index: {self.pos}\n       Shapes:{self.shapes}\n"
