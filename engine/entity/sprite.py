import pygame

from engine.entity import Entity


class Sprite(Entity):
    def __init__(self, name, asset, position=(0, 0)):
        super().__init__(name, asset)
        self.position = pygame.Vector2(position)

    def render(self, surface):
        surface.blit(self.asset, self.position)

    def update(self, dt, input_manager=None):
        pass
