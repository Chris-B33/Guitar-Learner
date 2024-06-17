import pygame as pg

pg.font.init()
FONT = pg.font.SysFont("Arial", 24)

class Label:
    def __init__(self, _x, _y, _w, _h, _text="") -> None:
        self.surface = pg.Surface((_w, _h))
        self.rect = pg.Rect(_x, _y, _w, _h)
        self.set_text(_text)

    def get_text(self) -> str:
        return self.text

    def set_text(self, new_text) -> None:
        self.text = new_text
        self.rendered_text = FONT.render(self.text, False, (255, 255, 255))

class Image(Label):
    def __init__(self, _x, _y, _w, _h, _image_name) -> None:
        super().__init__(_x, _y, _w, _h)
        self.set_image(_image_name)
    
    def set_image(self, new_image_name):
        self.image_name = new_image_name
        self.image = pg.image.load("imgs/" + self.image_name + ".png").convert()
        self.surface.blit(self.image)

class Button(Label):
    def __init__(self, _x, _y, _w, _h, _text, _callback) -> None:
        super().__init__(_x, _y, _w, _h, _text)
        self.callback = _callback
    
    def on_click(self, event) -> None:
        self.callback()