from Screen import Screen
from UIElements import Button, Label

class StrumPatternGame(Screen):
    def __init__(self) -> None:
        super().__init__("Chord Game")
        self.elements = [
            Button(self.WINDOW_SIZE / 4, self.WINDOW_SIZE / 8 * 5.5, self.WINDOW_SIZE / 2, self.WINDOW_SIZE / 8, "Back", self.end)
        ]