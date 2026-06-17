import enum

import pygame
from core.entity.sprite import Sprite
from games.ships import conf


class IslandSize(enum.Enum):
    SMALL = (200, 200)
    MEDIUM = (400, 400)
    LARGE = (800, 800)

class Island(Sprite):
    def __init__(self, name, asset, position, island_size:IslandSize):
        super().__init__(name, asset, position, pygame.Vector2(island_size.value))
        self.collision_radius = max(self.size.xy) / 2

    def render(self, surface):
        # pygame.draw.circle(surface, pygame.Color(conf.COLORS['white']), self.position, self.collision_radius)
        super().render(surface)
