class Question:
    # The arrow next to params is a function annotation
    # ref: https://peps.python.org/pep-0484/
    def __init__(self, text, answer) -> None:
        self.text = text
        self.answer = answer
