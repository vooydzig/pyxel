import pygame


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
