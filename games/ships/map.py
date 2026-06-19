import pygame

from core.ui import widgets
from games.ships import conf
from games.ships.island import Island, IslandSize, Bootey

# # ISLAND_COUNT=3
# # BOOTEY_COUNT=2
# #
# # ISLANDS =[]
# # BOOTEY =[]
# # for i in range(ISLAND_COUNT):
# #     size = random.choice(['tiny', 'small', 'medium'])
# #     position = (
# #         random.randint(-WORLD_SIZE, WORLD_SIZE),
# #         random.randint(-WORLD_SIZE, WORLD_SIZE)
# #     )
# #     ISLANDS.append((f"Island {i+1}", position, size))
# #
# #
# # for i in range(BOOTEY_COUNT):
# #     bootey = random.choice(['shipwreck','castaway','trash','bottle',])
# #     position = (
# #         random.randint(-WORLD_SIZE, WORLD_SIZE),
# #         random.randint(-WORLD_SIZE, WORLD_SIZE)
# #     )
# #     BOOTEY.append((f"Island {i + 1}", position, bootey))

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
            widget = widgets.Label(0, 0, i.name, self.asset_manager.get_asset('font', 'minecraft_18'))
            i.add_widget('name', widget, relative_position=pygame.Vector2(-widget.size.x / 2, i.collision_radius))
            islands.append(i)
        return islands

    def _setup_bootey(self):
        bootey = []
        for _bootey in conf.BOOTEY:
            b = Bootey(
                _bootey[0],
                self.asset_manager.get_asset('image', _bootey[2]),
                pygame.Vector2(_bootey[1]),
            )
            bootey.append(b)
        return bootey
