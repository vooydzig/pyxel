import pygame

from core.ui.widgets import Widget


class Label(Widget):
    def __init__(self, x, y, text, font, color=pygame.Color(255, 255, 255), z_index=0):
        text_surface = font.render(text, True, color)
        super().__init__(x, y, text_surface.get_width(), text_surface.get_height(), z_index)
        self.text = text
        self.font = font
        self.color = color
        self.text_surface = text_surface

    def set_text(self, new_text):
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.color)
        self.size = pygame.Vector2(self.text_surface.get_width(), self.text_surface.get_height())

    def render(self, surface):
        if self.visible:
            surface.blit(self.text_surface, self.position)
