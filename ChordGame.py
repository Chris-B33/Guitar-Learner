import pygame as pg
from Screen import Screen
from UIElements import Button, Image
from threading import Thread
import random
import time

class ChordGame(Screen):
    METRONOME_TIMING = 1
    IMAGE_CHANGE_PERIOD = 2
    CHORDS = ["Am", "C", "Em", "E", "G"]
    current_chord = "C"

    def __init__(self) -> None:
        super().__init__("Chord Game")
        self.elements = [
            Image(self.WINDOW_SIZE / 4, self.WINDOW_SIZE / 5, self.WINDOW_SIZE / 2, self.WINDOW_SIZE / 2, self.current_chord),
            Button(self.WINDOW_SIZE / 3, self.WINDOW_SIZE / 4 * 3, self.WINDOW_SIZE / 3, self.WINDOW_SIZE / 8, "Back", self.end)
        ]
        self.metronome = pg.mixer.Sound("metronome.wav")

    def start(self):
        Thread(target=self.play_game).start()
        super().start()

    def play_game(self):
        time_counter = 0
        while self.running:
            time.sleep(self.METRONOME_TIMING)
            time_counter += self.METRONOME_TIMING

            self.metronome.play()

            if time_counter > self.IMAGE_CHANGE_PERIOD:
                time_counter = 0
                self.change_image(previous=self.current_chord)
    
    def change_image(self, previous):
        new_chord = self.CHORDS[random.randint(0, len(self.CHORDS) - 1)]

        while new_chord == previous: 
            new_chord = self.CHORDS[random.randint(0, len(self.CHORDS) - 1)]

        self.elements[0].set_image(new_chord)
