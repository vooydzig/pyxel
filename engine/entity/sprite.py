import pygame

from engine.entity import Entity


class Sprite(Entity):
    def __init__(self, name, asset, position=(0, 0), size=pygame.Vector2(64, 64)):
        self.size = size
        self.position = pygame.Vector2(position)
        self._widgets = {}
        self._widget_offsets = {}
        super().__init__(name, pygame.transform.scale(asset, self.size))

    def render(self, surface):
        surface.blit(self.asset, self.position)
        for widget in self._widgets.values():
            widget.render(surface)

    def update(self, dt, input_manager=None):
        for name, widget in self._widgets.items():
            widget.set_position(
                self.position.x + self._widget_offsets.get(name).x,
                self.position.y + self._widget_offsets.get(name).y,
            )
            widget.update(dt)

    def attach_widget(self, name, widget, position_offset=(0, 0)):
        if name in self._widgets:
            raise ValueError(f"Widget with name '{name}' already exists.")
        self._widgets[name] = widget
        self._widget_offsets[name] = pygame.Vector2(position_offset)
