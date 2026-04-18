import random

import pygame

from core.app import App
from entity import Star


class WarpspeedApp(App):
    STARS_COUNT = 1000
    TURN_ACCELERATION = 0.1
    TURN_DAMPING = 0.86
    EMITTER_DEPTH = 10
    EMITTER_DRIFT = 1.0

    def initialize(self):
        super().initialize()
        self.turn_velocity = pygame.Vector2()
        self.turn_delta = pygame.Vector2()
        self.emitter_center = pygame.Vector2()
        for i in range(self.STARS_COUNT):
            self.entities.append(Star(f'star_{i}', self.get_random_position()))
        self.input.mouse.position = self.screen_size / 2
        self.last_mouse_position = pygame.Vector2(self.input.mouse.position)

    def _update_input(self):
        super()._update_input()
        mouse_delta = self.input.mouse.position - self.last_mouse_position
        turn_impulse = pygame.Vector2(
            mouse_delta.x * self.TURN_ACCELERATION,
            mouse_delta.y * self.TURN_ACCELERATION
        )
        self.turn_velocity += turn_impulse
        self.turn_velocity *= self.TURN_DAMPING
        self.turn_delta = pygame.Vector2(self.turn_velocity)
        self.emitter_center += self.turn_delta * self.EMITTER_DEPTH * self.EMITTER_DRIFT
        self.last_mouse_position = pygame.Vector2(self.input.mouse.position)

    def _update_entities(self):
        for star in self.entities:
            star.turn_delta = self.turn_delta
        super()._update_entities()
        for star in self.entities:
            if star.position.z < 1:
                star.position = self.get_random_position()
                star.previous_position = pygame.Vector3(star.position)

    def get_random_position(self):
        return pygame.Vector3(
            random.randint(-int(self.renderer.canvas_size.x), int(self.renderer.canvas_size.x)),
            random.randint(-int(self.renderer.canvas_size.y), int(self.renderer.canvas_size.y)),
            random.randint(1, 10)
        )
