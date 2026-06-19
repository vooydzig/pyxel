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



class BootyCallsApp(App):
    def initialize(self):
        super().initialize()
        self.renderer.background = Background(pygame.Color(conf.COLORS['dark_sea']))
        self.renderer.uncharted = pygame.transform.scale(
            self.asset_manager.get_asset('image', 'map'),
            self.renderer.canvas_size,
        )

        self.map = World(pygame.Vector2(conf.WORLD_SIZE), asset_manager=self.asset_manager)

        self.player = Player('player', self.asset_manager.get_asset('image', 'ship (1)'))
        self.player.position = self.map.center.copy()/2
        self.renderer.camera.position = self.player.position.copy()
        self.renderer.camera.bound_to(self.map.size)
        self.player.trail = Trail(self.asset_manager.get_asset('image', 'wake'), self.player.position)
        self.entities.append(self.player)

        self.entities.extend(self.map.islands)
        self.entities.extend(self.map.bootey)

        self.active_event = None
        self.player_is_docked = False

    def _update_entities(self):
        self.renderer.camera.position = self.player.position - self.renderer.canvas_size / 2
        super()._update_entities()
        self.renderer.plot_map(self.player.position)
        self.handle_collision(self.map.islands, self.handle_event)
        self.handle_collision(self.map.bootey, self.handle_event)
        for entity in self.map.bootey:
            if entity.should_cleanup:
                self.entities.remove(entity)
                self.map.bootey.remove(entity)

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
            self.player_is_docked = False
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
        if self.player_is_docked:
            return
        self.player_is_docked = True
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
