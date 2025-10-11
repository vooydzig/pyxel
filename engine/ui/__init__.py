import pygame


class GUIManager:
    def __init__(self, app):
        self.app = app
        self._widgets = {}

    def update(self, dt):
        for widget in self._widgets.values():
            widget.update(dt)

    @property
    def widgets(self):
        # TODO: overdrawn?
        widgets = self._widgets.values()
        return sorted(widgets, key=lambda w: w.z_index)

    def add_widget(self, name, widget):
        if name in self._widgets:
            raise ValueError(f"Widget with name '{name}' already exists.")
        self._widgets[name] = widget

    def get_widget(self, name):
        return self._widgets.get(name)

class Widget:
    def __init__(self, x, y, width, height, z_index=0):
        self.position = pygame.Vector2(x, y)
        self.size = pygame.Vector2(width, height)
        self.z_index = z_index
        self.visible = True

    def update(self, dt):
        pass

    def render(self, surface):
        if self.visible:
            pygame.draw.rect(surface, pygame.Color(255, 0, 0), (*self.position, *self.size), 2)

    def set_position(self, x, y):
        self.position = pygame.Vector2(x, y)

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