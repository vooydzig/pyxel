import enum
import random

import pygame
from core.entity.sprite import Sprite
from games.ships.events import ISLAND_EVENTS, SEA_EVENTS


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
        self.events = random.sample(ISLAND_EVENTS, 2)

class BooteyType(enum.Enum):
    CASTAWAY = 'castaway'
    SHIPWRECK = 'shipwreck'
    TRASH = 'trash'
    BOTTLE = 'bottle'

    @classmethod
    def from_string(cls, size_str):
        size_str = size_str.upper()
        if size_str in cls.__members__:
            return cls[size_str]
        else:
            raise ValueError(f"Invalid IslandSize string: {size_str}")


class Bootey(Sprite):
    def __init__(self, name, asset=None, position=pygame.Vector2()):
        super().__init__(name, asset, position, pygame.Vector2(64, 64))
        self.events = random.sample(SEA_EVENTS, 1)
