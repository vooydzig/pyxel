import pygame

from core.app import App
from core.renderer import Background
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
        self.islands = [
            Island(
                'Cape Vista',
                self.asset_manager.get_asset('image', 'island_2'),
                self.renderer.canvas_size / 8,
                IslandSize.SMALL
            ),
            Island(
                'Bona Ventura',
                self.asset_manager.get_asset('image', 'island_2'),
                pygame.Vector2(self.renderer.canvas_size.x / 8 * 7, self.renderer.canvas_size.y / 8),
                IslandSize.SMALL
            ),
            Island(
                'Tralla Lala',
                self.asset_manager.get_asset('image', 'island_2'),
                pygame.Vector2(self.renderer.canvas_size.x / 8 * 7, self.renderer.canvas_size.y / 8 * 7),
                IslandSize.SMALL
            ),
            Island(
                'Concordia',
                self.asset_manager.get_asset('image', 'island_2'),
                pygame.Vector2(self.renderer.canvas_size.x / 8 , self.renderer.canvas_size.y / 8 * 7),
                IslandSize.SMALL
            ),

        ]
        self.entities.append(self.player)
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
