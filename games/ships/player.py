import math

import pygame
from core.entity.sprite import Sprite

class Player(Sprite):
    ACTIONS = {
        pygame.K_w: 'speed_up',
        pygame.K_s: 'speed_down',
        pygame.K_a: 'rotate_left',
        pygame.K_d: 'rotate_right',
    }

    def __init__(self, name, asset, position=pygame.Vector2(), speed=.2):
        super().__init__(name, asset, position)
        self.max_speed = speed
        self.acceleration = 0.0005
        self.current_speed = 0
        self.current_angle = 0
        self.turn_speed = 0.1
        self.direction = pygame.Vector2(0, 1)
        self.trail = None

    def update(self, dt, input_manager=None):
        if input_manager:
            for key, action in self.ACTIONS.items():
                if input_manager.is_key_held(key):
                    getattr(self, action)(dt)
        if self.direction.length() > 0:
            self.direction = self.direction.normalize()
        self.position.x -= self.direction.x * self.current_speed * dt
        self.position.y += self.direction.y * self.current_speed * dt

        self.trail.add_point(self.position.copy())

        self.trail.update(dt)
        super().update(dt)

    def render(self, surface):
        self.trail.render(surface)
        self._blit_rotated(surface)
        self.gui.render(surface)

    def _blit_rotated(self, surface):
        rotated_image = pygame.transform.rotate(self.asset, self.current_angle)
        new_rect = rotated_image.get_rect(center=rotated_image.get_rect(center=self.position).center)
        surface.blit(rotated_image, new_rect)

    def speed_up(self, dt):
        self.current_speed = min(self.max_speed, self.current_speed + self.acceleration * dt)

    def speed_down(self, dt):
        self.current_speed = max(0, self.current_speed - self.acceleration * dt)

    def rotate_left(self, dt):
        angle = self.turn_speed * dt
        self.current_angle += angle
        self.direction = self.direction.rotate(angle)

    def rotate_right(self, dt):
        angle = self.turn_speed * dt
        self.current_angle -= angle
        self.direction = self.direction.rotate(-angle)
