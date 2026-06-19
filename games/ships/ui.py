import pygame

from core.ui.widgets import Widget


class Counter(Widget):
    def __init__(self, position, value, font, color, icon, min=0, max=100):
        self._value = 0
        self.font = font
        self.color = color
        self.icon = icon

        self.min = min
        self.max = max
        self.value = 0
        surface_size = self.surface_size()
        self.text_surface = None

        super().__init__(*position.xy, *surface_size.xy, 0)

        self.value = value
        self.text_offset = pygame.Vector2(self.icon.get_width()*2, 0)

    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, value):
        self._value = min(self.max, max(value, self.min))
        self.set_text(f'{value:03d}')

    def surface_size(self):
        text_surface = self.font.render(self.text, True, self.color)
        return pygame.Vector2(
            text_surface.get_width() + self.icon.get_width(),
            text_surface.get_height()
        )

    def set_text(self, new_text):
        self.text = new_text
        self.text_surface = self.font.render(self.text, True, self.color)
        self.size = self.surface_size()

    def render(self, surface, camera=None):
        if self.visible:
            surface.blit(self.icon, self._get_screen_position(camera))
            surface.blit(self.text_surface, self._get_screen_position(camera) + self.text_offset)
