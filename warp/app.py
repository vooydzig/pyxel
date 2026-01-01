import random

import pygame

from core.app import App
from entity import Star


class WarpspeedApp(App):
    STARS_COUNT = 1000

    def initialize(self):
        super().initialize()
        for i in range(self.STARS_COUNT):
            self.entities.append(Star(f'star_{i}', self.get_random_position()))

    def _update_entities(self):
        super()._update_entities()
        for star in self.entities:
            if star.position.z < 1:
                star.position = self.get_random_position()
                star.pz = star.position.z

    def get_random_position(self):
        return pygame.Vector3(
            random.randint(-int(self.renderer.canvas_size.x), int(self.renderer.canvas_size.x)),
            random.randint(-int(self.renderer.canvas_size.y), int(self.renderer.canvas_size.y)),
            random.randint(1, 10)
        )
