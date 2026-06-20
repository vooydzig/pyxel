import pygame

from core.ui import widgets
from games.ships import conf
from games.ships.island import Island, IslandSize, Bootey

class World:
    def __init__(self, size, asset_manager=None):
        self.size = size
        self.asset_manager = asset_manager
        self.islands = self._setup_islands()
        self.bootey = self._setup_bootey()
        self.center = self.size / 2

    def _setup_islands(self):
        islands = []
        for _island in conf.ISLANDS:
            i = Island(
                _island[0],
                self.asset_manager.get_asset('image', 'island_2'),
                pygame.Vector2(_island[1]),
                IslandSize.from_string(_island[2]),
            )
            widget = widgets.Label(pygame.Vector2(), i.name, self.asset_manager.get_asset('font', 'minecraft_18'))
            i.add_widget('name', widget, relative_position=pygame.Vector2(-widget.size.x / 2, i.collision_radius))
            islands.append(i)
        return islands

    def _setup_bootey(self):
        bootey = []
        for _bootey in conf.BOOTEY:
            b = Bootey(
                _bootey[0],
                pygame.Vector2(_bootey[1]),
                self.asset_manager.get_asset('image', _bootey[2]),
                _bootey[2]
            )
            bootey.append(b)
        return bootey
