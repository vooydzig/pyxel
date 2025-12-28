import pygame

from core.entity import Entity
from core.ui import GUIManager


class Sprite(Entity):
    def __init__(self, name, asset, position=(0, 0), size=pygame.Vector2(64, 64)):
        self.size = size
        self.position = pygame.Vector2(position)
        self.gui = GUIManager(self)
        super().__init__(name, pygame.transform.scale(asset, self.size))

    def render(self, surface):
        surface.blit(self.asset, self.position)
        self.gui.render(surface)

    def update(self, dt, input_manager=None):
        self.gui.update(dt)
        super().update(dt, input_manager)

    def add_widget(self, name, widget, relative_position=pygame.Vector2(0, 0)):
        self.gui.add_widget(name, widget, relative_position)
