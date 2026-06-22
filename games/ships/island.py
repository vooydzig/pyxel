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
        self.visited = False

class BooteyType(enum.Enum):
    CASTAWAY = 'castaway'
    SHIPWRECK = 'shipwreck'
    TRASH = 'trash'
    BOTTLE = 'bottle'

    @classmethod
    def from_string(cls, type_str):
        type_str = type_str.upper()
        if type_str in cls.__members__:
            return cls[type_str]
        else:
            raise ValueError(f"Invalid BooteyType string: {type_str}")


class Bootey(Sprite):
    def __init__(self, name, position=pygame.Vector2(), asset=None, type:BooteyType=None):
        super().__init__(name, asset, position, pygame.Vector2(64, 64))
        self.type = type
        self.events = random.sample(SEA_EVENTS[self.type.value], 1)

    @property
    def should_cleanup(self):
        return len(self.events) == 0
