import random

import pygame

from core.app import App
from core.renderer import Background
from core.ui import widgets
from games.ships.island import Island, IslandSize, Bootey
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
        self.islands = self._setup_islands()
        self.bootey = self._setup_bootey()
        self.entities.extend(self.islands)
        self.entities.extend(self.bootey)

        self.active_event = None
        self.player_is_docked = False

    def _update_entities(self):
        super()._update_entities()
        self.handle_collision(self.islands, self.handle_event)
        self.handle_collision(self.bootey, self.handle_event)

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
        boarding_distance = nearest_entity.collision_radius + self.player.collision_radius
        if min_distance > boarding_distance:
            self.player_is_docked = False
        if min_distance < boarding_distance and self.input.is_key_held(pygame.K_e):
            event_handler(nearest_entity)

    def update(self):
        self._update_input()
        if self.active_event:
            if self.input.is_key_held(pygame.K_SPACE):
                self.active_event = None
                self.ui.remove_widget('active_event')
        else:
            self._update_entities()
            self._update_renderer()
            self._update_ui()

    def _setup_islands(self):
        islands = []
        for _island in conf.ISLANDS:
            i = Island(
                _island[0],
                self.asset_manager.get_asset('image', 'island_2'),
                _island[1],
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
                _bootey[1],
            )
            bootey.append(b)
        return bootey

    def handle_event(self, entity):
        if self.player_is_docked:
            return
        self.player_is_docked = True
        self.player.full_stop()
        if not entity.events:
            self.active_event = "Nothing interesting here."
        else:
            event_id = random.randrange(0, len(entity.events))
            self.active_event = entity.events.pop(event_id)
        self.ui.add_widget('active_event', widgets.Label(
            0, 0 , self.active_event, self.asset_manager.get_asset('font', 'minecraft_18')
        ), relative_position=pygame.Vector2(0, self.screen_size.y-18))
