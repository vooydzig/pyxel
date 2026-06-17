import pygame

from core.app import App
from core.renderer import Background
from core.ui import widgets
from games.ships.island import Island, IslandSize
from games.ships.player import Player
from games.ships.trail import Trail
from games.ships import conf


class BootyCallsApp(App):
    def initialize(self):
        super().initialize()
        self.renderer.background = Background(pygame.Color(conf.COLORS['dark_sea']))
        self.player = Player('player', self.asset_manager.get_asset('image', 'ship (1)'))
        self.player.position = self.renderer.canvas_size / 2
        self.player.trail = Trail(self.asset_manager.get_asset('image', 'wake'), self.player.position)
        self.entities.append(self.player)

        self.islands = []
        self._setup_islands()
        self.entities.extend(self.islands)

    def _update_entities(self):
        super()._update_entities()
        min_distance = conf.INFINITY
        nearest_island = None
        for island in self.islands:
            d = self.player.position.distance_to(island.position)
            if d < min_distance:
                min_distance = d
                nearest_island = island
            if d < island.collision_radius + self.player.collision_radius:
                self.player.full_stop()
        boarding_distance = nearest_island.collision_radius + self.player.collision_radius
        if min_distance < boarding_distance and self.input.is_key_held(pygame.K_e):
            print(f'Docking {nearest_island.name}')

    def _setup_islands(self):
        for i_conf in conf.ISLANDS:
            i = Island(
                i_conf[0],
                self.asset_manager.get_asset('image', 'island_2'),
                i_conf[1],
                IslandSize.from_string(i_conf[2]),
            )
            widget = widgets.Label(0, 0, i.name, self.asset_manager.get_asset('font', 'minecraft_18'))
            i.add_widget('name', widget, relative_position=pygame.Vector2(-widget.size.x / 2, i.collision_radius))
            self.islands.append(i)
