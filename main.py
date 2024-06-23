from ChordGame import ChordGame
from StrumPatternGame import StrumPatternGame
from UIElements import Button, Label
from Screen import Screen
import pygame as pg

class GuitarLearner(Screen):
    WINDOW_SIZE: int = 600

    def __init__(self) -> None:
        super().__init__("Guitar Learner", (155, 255, 155))
        self.elements = [
            Label(self.WINDOW_SIZE / 10 * 1.5, self.WINDOW_SIZE / 4, self.WINDOW_SIZE / 10 * 7, self.WINDOW_SIZE / 16 * 2.5, "Guitar Learner"),
            Button(self.WINDOW_SIZE / 4, self.WINDOW_SIZE / 2, self.WINDOW_SIZE / 2, self.WINDOW_SIZE / 8, "Chord Game", self.start_chord_game),
            Button(self.WINDOW_SIZE / 4, self.WINDOW_SIZE / 8 * 5.5, self.WINDOW_SIZE / 2, self.WINDOW_SIZE / 8, "Strum Pattern Game", self.start_strum_pattern_game)
        ]

    def start_chord_game(self) -> None:
        cg = ChordGame()
        cg.start()

    def start_strum_pattern_game(self) -> None:
        sp = StrumPatternGame()
        sp.start()

if __name__ == "__main__":
    gl = GuitarLearner()
    gl.start()