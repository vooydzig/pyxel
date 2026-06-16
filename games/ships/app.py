import math

import pygame

from core.app import App
from core.entity.sprite import Sprite
from core.renderer import Background
from games.ships.player import Player
from games.ships import conf


class Trail(Sprite):
    def __init__(self, asset, position):
        super().__init__('trail', asset, position)
        self.points = []
        self.max_points = 10
        self.color = pygame.Color(255, 255, 255, 30)
        self.sea_color = pygame.Color(66, 194, 245)
        self.thickness = 40
        self.add_threshold = 10
        self.ttl = 10
        self.timer = 0

    def render(self, surface):
        num_points = len(self.points)
        if num_points < 2:
            return

        # Loop through pairs of points to build segments
        for i in range(num_points - 1):
            # Calculate "age factor" from 0.0 (oldest/tail) to 1.0 (newest/boat)
            age_factor = (i + 1) / (num_points - 1)

            # Apply age factor to thickness and transparency for a tapering effect
            current_thickness = max(2, int(self.thickness * age_factor))
            current_alpha = int(255 * age_factor)

            # Math for distance and angle
            diff = pygame.Vector2(self.points[i + 1] - self.points[i])
            distance = diff.length()

            if distance < 1:
                continue

            angle = -diff.as_polar()[1]+90

            scaled_texture = pygame.transform.scale(self.asset, (8 * int(distance), 8 * current_thickness))
            scaled_texture.set_alpha(current_alpha)
            rotated_texture = pygame.transform.rotate(scaled_texture, angle)
            rect = rotated_texture.get_rect()
            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]
            rect.center = ((x1 + x2) // 2, (y1 + y2) // 2)
            surface.blit(rotated_texture, rect.topleft)

    def update(self, dt):
        if len(self.points) > self.max_points:
            self.pop_point()
        elif self.timer > self.ttl:
            self.pop_point()

    def add_point(self, point):
        if self.points:
            last_point = self.points[-1]
            d = last_point.distance_to(point)
            if d < self.add_threshold:
                self.timer += 1
                return

        self.points.append(point)

    def pop_point(self):
        self.points.pop(0)
        self.timer = 0



class BootyCallsApp(App):
    def initialize(self):
        super().initialize()
        sea = Background()
        # sea.color = pygame.Color(66, 194, 245)
        sea.color = pygame.Color(20, 40, 65)
        self.renderer.background = sea
        self.player = Player('player', self.asset_manager.get_asset('image', 'ship (1)'))
        self.player.position = self.renderer.canvas_size / 2
        self.player.trail = Trail(self.asset_manager.get_asset('image', 'wake'), self.player.position)
        self.entities.append(
            self.player
        )
