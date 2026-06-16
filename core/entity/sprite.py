import pygame

from core.entity import Entity
from core.ui import GUIManager


class Sprite(Entity):
    def __init__(self, name, asset=None, position=pygame.Vector2(), size=None):
        self.gui = GUIManager(self)
        if asset:
            self.size = pygame.Vector2(asset.get_size())
        if asset and size:
            self.size = size
            super().__init__(name, pygame.transform.scale(asset, self.size), position)
        else:
            super().__init__(name, asset, position)


    def render(self, surface):
        surface.blit(self.asset, self.position)
        self.gui.render(surface)

    def update(self, dt, input_manager=None):
        self.gui.update(dt)
        super().update(dt, input_manager)

    def add_widget(self, name, widget, relative_position=pygame.Vector2(0, 0)):
        self.gui.add_widget(name, widget, relative_position)
