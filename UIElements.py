import pygame as pg

pg.font.init()
FONT = pg.font.SysFont("Arial", 24)

class Label:
    def __init__(self, _x, _y, _w, _h, _text) -> None:
        self.surface = pg.Surface((_w, _h))
        self.rect = pg.Rect(_x, _y, _w, _h)
        self.text = FONT.render(_text, False, (255, 255, 255))
    
    def on_click(self) -> None:
        pass

class Button(Label):
    def __init__(self, _x, _y, _w, _h, _text, _callback) -> None:
        super().__init__(_x, _y, _w, _h, _text)
        self.callback = _callback
    
    def on_click(self, event) -> None:
        if self.rect.collidepoint(event.pos):
            self.callback()