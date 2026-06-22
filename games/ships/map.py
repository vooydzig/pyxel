import random

import pygame
from pygame import Vector2

from core.ui import widgets
from games.ships import conf
from games.ships.island import Island, IslandSize, Bootey, BooteyType

ISLAND_NAMES = [
    "Golden Tooth Island",
    "Island of the Scourge",
    "Full Moon Cave",
    "Blackbeard's Hideout",
    "Isle of the Death Curse",
    "Cavern of Parrots",
    "Cavern of Dry Rum",
    "Island of Old Salt",
    "Cavern of Silver",
    "Isle of Hornswaggle",
    "Shipwreck Atoll",
    "Cavern of the Unnamed",
    "Island of the Unnamed",
]


class World:
    def __init__(self, size, asset_manager=None):
        self.size = size
        self.asset_manager = asset_manager
        self.islands = self._generate_islands()
        self.bootey = self._generate_bootey()
        self.center = self.size / 2

    def _generate_islands(self):
        islands = []
        for name in ISLAND_NAMES:
            position = pygame.Vector2(random.randint(0, int(self.size.x)), random.randint(0, int(self.size.y)))
            size = random.choice(list(IslandSize))
            collision_radius = max(size.value)
            collisions = self._get_collision(position, collision_radius, islands)
            while collisions:
                position = pygame.Vector2(random.randint(0, int(self.size.x)), random.randint(0, int(self.size.y)))
                size = random.choice(list(IslandSize))
                collision_radius = max(size.value)
                collisions = self._get_collision(position, collision_radius, islands)
            i = Island(name, self.asset_manager.get_asset('image', 'island_2'), position, size)
            widget = widgets.Label(pygame.Vector2(), i.name, self.asset_manager.get_asset('font', 'minecraft_18'))
            i.add_widget('name', widget, relative_position=pygame.Vector2(-widget.size.x / 2, i.collision_radius))
            islands.append(i)
        return islands

    def _generate_bootey(self):
        bootey = []
        for i in range(10):
            position = pygame.Vector2(random.randint(0, int(self.size.x)), random.randint(0, int(self.size.y)))
            _type = random.choice(list(BooteyType))
            collision_radius = 64
            collisions = self._get_collision(position, collision_radius, self.islands + bootey)
            while collisions:
                position = pygame.Vector2(random.randint(0, int(self.size.x)), random.randint(0, int(self.size.y)))
                collisions = self._get_collision(position, collision_radius, self.islands + bootey)
            bootey.append(Bootey(
                _type.value.title(),
                position,
                self.asset_manager.get_asset('image', _type.value),
                _type
            ))
        return bootey

    def _get_collision(
            self,
            position: Vector2,
            collision_radius: float,
            entities: list
    ) -> list:
        return [
            e
            for e in entities
            if (e.position - position).length() < collision_radius
        ]

    def draw_full_map(self):
        surface = pygame.Surface((self.size.x, self.size.y))
        surface.fill(pygame.Color(conf.COLORS['dark_sea']))
        for e in self.islands+self.bootey:
            surface.blit(e.asset, e.position - e.size / 2)
        pygame.image.save(surface, '/home/vooydzig/__MOJE/gfx_pixel_lab/assets/booty/map/preview.png')
