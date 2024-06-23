from UIElements import Button
import pygame as pg

class Screen:
    WINDOW_SIZE: int = 600

    def __init__(self, title, color: tuple) -> None:
        pg.init()
        self.screen = pg.display.set_mode([self.WINDOW_SIZE, self.WINDOW_SIZE])
        pg.display.set_caption(title)
        self.elements = []
        self.running = True
        self.bg_color = color

    def end(self) -> None:
        self.running = False

    def start(self) -> None:
        while self.running:
            self.screen.fill(self.bg_color)

            for event in pg.event.get():
                if event.type == pg.QUIT:
                    self.running = False

                if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
                    for elem in self.elements:
                        if type(elem) != Button:
                            continue

                        if elem.rect.collidepoint(event.pos):
                            elem.on_click(event)

            for elem in self.elements:
                elem.draw()
                self.screen.blit(elem.surface, (elem.rect.x, elem.rect.y))
               
            pg.display.flip()