from Screen import Screen
from UIElements import Button
import pygame as pg

class StrumPatternGame(Screen):
    def __init__(self) -> None:
        super().__init__("Chord Game", (0, 15, 0))
        self.elements = [
            Button(self.WINDOW_SIZE / 4, self.WINDOW_SIZE / 8 * 5.5, self.WINDOW_SIZE / 2, self.WINDOW_SIZE / 8, "Back", self.end)
        ]
        self.metronome = pg.mixer.Sound("metronome.wav")