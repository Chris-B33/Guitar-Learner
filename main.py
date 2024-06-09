import pygame as pg
from ChordGame import ChordGame
from StrumPatternGame import StrumPatternGame
from UIElements import Button, Label

class GuitarLearner:
    WINDOW_SIZE: int = 400

    def __init__(self) -> None:
        pg.init()
        self.screen = pg.display.set_mode([self.WINDOW_SIZE, self.WINDOW_SIZE])
        pg.display.set_caption('Guitar Learner')
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

    def start(self) -> None:
        running = True 
        while running:
            self.screen.fill((155, 255, 155))

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    running = False

                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    for elem in self.elements:
                        elem.on_click(event)

            for elem in self.elements:
                pg.draw.rect(elem.surface, 0, elem.rect)
                elem.surface.blit(elem.text, elem.text.get_rect(center=(elem.surface.get_width()/2, elem.surface.get_height()/2)))
                self.screen.blit(elem.surface, (elem.rect.x, elem.rect.y))
               
            pg.display.flip()

if __name__ == "__main__":
    gl = GuitarLearner()
    gl.start()