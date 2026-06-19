import pygame


class Entity:
    def __init__(self, name, asset, position=pygame.Vector2(0,0)):
        self.name = name
        self.asset = asset
        self.position = position

    def update(self, dt, input_manager=None):
        pass

    def render(self, surface, camera=None):
        pass
