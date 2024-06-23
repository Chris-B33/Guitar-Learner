import pygame as pg

pg.font.init()
FONT = pg.font.SysFont("Arial", 24)

class Label:
    def __init__(self, _x, _y, _w, _h, _text="") -> None:
        self.surface = pg.Surface((_w, _h))
        self.rect = pg.Rect(_x, _y, _w, _h)
        self.set_text(_text)

    def draw(self) -> None:
        pg.draw.rect(self.surface, 0, self.rect)
        self.surface.blit(self.rendered_text, self.rendered_text.get_rect(center=(self.surface.get_width()/2, self.surface.get_height()/2)))

    def get_text(self) -> str:
        return self.text

    def set_text(self, new_text) -> None:
        self.text = new_text
        self.rendered_text = FONT.render(self.text, False, (255, 255, 255))

class Image(Label):
    def __init__(self, _x, _y, _w, _h, _image_name) -> None:
        super().__init__(_x, _y, _w, _h)
        self.set_image(_image_name)
    
    def draw(self) -> None:
        super().draw()
        self.surface.blit(self.image, (0, 0))

    def set_image(self, new_image_name) -> None:
        self.image_name = new_image_name
        self.image = pg.image.load("imgs/" + self.image_name + ".png").convert()

class Button(Label):
    def __init__(self, _x, _y, _w, _h, _text, _callback) -> None:
        super().__init__(_x, _y, _w, _h, _text)
        self.callback = _callback
    
    def on_click(self, event) -> None:
        self.callback()