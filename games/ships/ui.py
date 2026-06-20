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

        super().__init__(position, surface_size, 0)

        self.value = value
        self.text_offset = pygame.Vector2(self.icon.get_width() + 8, self.icon.get_height()/4)

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


class Icon(Widget):
    def __init__(self, position, icon):
        self.icon = icon
        self.current_angle = 0
        super().__init__(position, icon.get_size(), z_index=99)

    def render(self, surface, camera=None):
        if self.visible:
            self._blit_rotated(surface, camera)
            # surface.blit(self.icon, self._get_screen_position(camera))

    def _blit_rotated(self, surface, camera):
        rotated_image = pygame.transform.rotate(self.icon, self.current_angle)
        position = camera.world_to_screen(self.position)
        new_rect = rotated_image.get_rect(center=rotated_image.get_rect(center=position).center)
        surface.blit(rotated_image, new_rect)
