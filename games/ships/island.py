import enum

import pygame
from core.entity.sprite import Sprite


class IslandSize(enum.Enum):
    TINY = (100, 100)
    SMALL = (200, 200)
    MEDIUM = (400, 400)
    LARGE = (800, 800)

    @classmethod
    def from_string(cls, size_str):
        size_str = size_str.upper()
        if size_str in cls.__members__:
            return cls[size_str]
        else:
            raise ValueError(f"Invalid IslandSize string: {size_str}")


class Island(Sprite):
    def __init__(self, name, asset, position, island_size: IslandSize):
        super().__init__(name, asset, position, pygame.Vector2(island_size.value))
        self.collision_radius = max(self.size.xy) / 2

    def render(self, surface):
        # pygame.draw.circle(surface, pygame.Color(conf.COLORS['white']), self.position, self.collision_radius)
        super().render(surface)
