import pygame as pg
from UIElements import Button

class Screen:
    WINDOW_SIZE: int = 600

    def __init__(self, title) -> None:
        pg.init()
        self.screen = pg.display.set_mode([self.WINDOW_SIZE, self.WINDOW_SIZE])
        pg.display.set_caption(title)
        self.elements = []
        self.running = True

    def end(self):
        self.running = False

    def start(self) -> None:
        while self.running:
            self.screen.fill((155, 255, 155))

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
                pg.draw.rect(elem.surface, 0, elem.rect)
                elem.surface.blit(elem.rendered_text, elem.rendered_text.get_rect(center=(elem.surface.get_width()/2, elem.surface.get_height()/2)))
                self.screen.blit(elem.surface, (elem.rect.x, elem.rect.y))
               
            pg.display.flip()