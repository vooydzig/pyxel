import random

import pygame

from core.app import App
from core.renderer import Background
from core.ui import widgets
from games.ships.events import EMPTY_EVENT
from games.ships.map import World
from games.ships.player import Player
from games.ships.trail import Trail
from games.ships import conf
from games.ships.ui import Counter


class BootyCallsApp(App):
    def initialize(self):
        super().initialize()
        self.active_event = None

        self.renderer.background = Background(pygame.Color(conf.COLORS['dark_sea']))
        self.renderer.uncharted_background = pygame.transform.scale(
            self.asset_manager.get_asset('image', 'map'),
            self.renderer.canvas_size,
        )

        self.map = World(pygame.Vector2(conf.WORLD_SIZE), asset_manager=self.asset_manager)
        self.player = Player('player', self.asset_manager.get_asset('image', 'ship (1)'))
        self.player.position = self.map.center.copy()/2
        self.player.trail = Trail(self.asset_manager.get_asset('image', 'wake'), self.player.position)

        self.renderer.camera.position = self.player.position.copy()
        self.renderer.camera.bound_to(self.map.size)
        self.renderer.plot_map(self.player.position, 400)

        self.entities.append(self.player)
        self.entities.extend(self.map.islands)
        self.entities.extend(self.map.bootey)

        self._setup_hud()

    def _setup_hud(self):
        visited = int(len([i for i in self.map.islands if i.visited])/len(self.map.islands) * 100)
        self.ui.add_widget(f'discovery_conter', Counter(
            pygame.Vector2(),
            visited,
            self.asset_manager.get_asset('font', 'minecraft_18'),
            pygame.Color(conf.COLORS['white']),
            pygame.transform.scale(self.asset_manager.get_asset('image', f'map_icon'), pygame.Vector2(14, 14))
        ), relative_position=pygame.Vector2(50, self.screen_size.y - 350))
        for i, cargo_type in enumerate(['gold','crew','ammo','goods'], start=1):
            self.ui.add_widget(f'{cargo_type}_conter', Counter(
                pygame.Vector2(),
                getattr(self.player.cargo,cargo_type).current,
                self.asset_manager.get_asset('font', 'minecraft_18'),
                pygame.Color(conf.COLORS['white']),
                pygame.transform.scale(self.asset_manager.get_asset('image', f'{cargo_type}_icon'), pygame.Vector2(14, 14)),
                0,
                getattr(self.player.cargo, cargo_type).max,
            ), relative_position=pygame.Vector2(50, self.screen_size.y - 50*i))

    def _update_entities(self):
        self.renderer.camera.position = self.player.position - self.renderer.canvas_size / 2
        super()._update_entities()
        self.renderer.plot_map(self.player.position)
        self.handle_collision(self.map.islands, self.handle_island_event)
        self.handle_collision(self.map.bootey, self.handle_event)
        for entity in self.map.bootey:
            if entity.should_cleanup:
                self.entities.remove(entity)
                self.map.bootey.remove(entity)

    def _update_ui(self):
        super()._update_ui()
        visited = int(len([i for i in self.map.islands if i.visited]) / len(self.map.islands) * 100)
        w = self.ui.get_widget('discovery_conter')
        w.value = visited
        for i, cargo_type in enumerate(['gold','crew','ammo','goods'], start=1):
            w = self.ui.get_widget(f'{cargo_type}_conter')
            w.value = getattr(self.player.cargo,cargo_type).current

    def handle_collision(self, entities, event_handler):
        min_distance = conf.INFINITY
        nearest_entity = None
        for entity in entities:
            d = self.player.position.distance_to(entity.position)
            if d < min_distance:
                min_distance = d
                nearest_entity = entity
            if d < entity.collision_radius + self.player.collision_radius:
                self.player.full_stop()
                self.renderer.plot_map(entity.position, entity.collision_radius*2)
        if nearest_entity is None:
            return
        boarding_distance = nearest_entity.collision_radius + self.player.collision_radius
        if min_distance > boarding_distance:
            self.player.is_docked = False
        if min_distance < boarding_distance and self.input.is_key_held(pygame.K_e):
            event_handler(nearest_entity)

    def update(self):
        self._update_input()
        if self.active_event:
            if self.input.is_key_held(pygame.K_SPACE):
                self.active_event.process_outcome(self.player)
                self.active_event = None
                self.ui.remove_widget('active_event')
        else:
            self._update_entities()
            self._update_renderer()
            self._update_ui()

    def handle_event(self, entity):
        if self.player.is_docked:
            return
        self.player.is_docked = True
        self.player.full_stop()
        if not entity.events:
            self.active_event = EMPTY_EVENT
        else:
            event_id = random.randrange(0, len(entity.events))
            self.active_event = entity.events.pop(event_id)

        self.ui.add_widget('active_event', widgets.Label(
            0, 0 ,
            self.active_event.description + " " + str.join(',', self.active_event.outcomes),
            self.asset_manager.get_asset('font', 'minecraft_18')
        ), relative_position=pygame.Vector2(0, self.screen_size.y-18))

    def handle_island_event(self, island):
        island.visited = True
        return self.handle_event(island)
