from Screen import Screen
from UIElements import Button, Image
import pygame as pg
from threading import Thread
import random
import time

class StrumPatternGame(Screen):
    METRONOME_TIMING = 4
    IMAGE_CHANGE_PERIOD = 4
    PATTERNS_COUNT = 1
    current_pattern = 0

    def __init__(self) -> None:
        super().__init__("Chord Game", (0, 15, 0))
        self.elements = [
            Image(self.WINDOW_SIZE / 4, self.WINDOW_SIZE / 5, self.WINDOW_SIZE / 2, self.WINDOW_SIZE / 2, f"P{self.current_pattern}"),
            Button(self.WINDOW_SIZE / 4, self.WINDOW_SIZE / 8 * 5.5, self.WINDOW_SIZE / 2, self.WINDOW_SIZE / 8, "Back", self.end)
        ]
        self.metronome = pg.mixer.Sound("metronome.wav")

    def start(self) -> None:
        Thread(target=self.play_game).start()
        super().start()

    def play_game(self) -> None:
        time_counter = 0
        while self.running:
            time.sleep(self.METRONOME_TIMING)
            time_counter += self.METRONOME_TIMING

            self.metronome.play()

            if time_counter > self.IMAGE_CHANGE_PERIOD:
                time_counter = 0
                self.change_image(previous=self.current_pattern)
     
    def change_image(self, previous) -> None:
        new_pattern_num = random.randint(0, self.PATTERNS_COUNT - 1)

        while new_pattern_num == previous: 
            new_pattern_num = random.randint(0, self.PATTERNS_COUNT - 1)

        self.elements[0].set_image(f"P{new_pattern_num}")