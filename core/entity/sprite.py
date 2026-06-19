import pygame

from core.camera import Camera
from core.entity import Entity
from core.ui import GUIManager


class Sprite(Entity):
    def __init__(self, name, asset=None, position=pygame.Vector2(), size=None):
        self.gui = GUIManager(self)
        self.collision_radius = 0
        self.screen_position = position.copy()
        if asset:
            self.size = pygame.Vector2(asset.get_size())
        if asset and size:
            self.size = size
            super().__init__(name, pygame.transform.scale(asset, self.size), position)
        else:
            super().__init__(name, asset, position)
        if self.size:
            self.collision_radius = max(self.size.xy) / 2


    def render(self, surface: pygame.Surface, camera: Camera):
        super().render(surface)
        surface.blit(self.asset, camera.world_to_screen(self.position) - self.size / 2)
        self.gui.render(surface, camera)

    def update(self, dt, input_manager=None):
        self.gui.update(dt)
        super().update(dt, input_manager)

    def add_widget(self, name, widget, relative_position=pygame.Vector2(0, 0)):
        self.gui.add_widget(name, widget, relative_position)
