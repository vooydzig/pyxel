import random

import pygame

from core.entity import Entity
from core.math import random_point_in_rect


class Particle(Entity):
    def __init__(self, name, color=pygame.Color(255, 255, 255), position=pygame.Vector2(0, 0), size=2):
        super().__init__(name, None, position)
        self.pp = self.position
        self.color = color
        self.size = size
        self.velocity = pygame.Vector2(0, 0.2)
        self.acceleration = pygame.Vector2(0, 0)
        self.ttl = random.randint(1, 20)

    def render(self, surface):
        pygame.draw.circle(surface, self.color, self.position, self.size)
        # pygame.draw.line(surface, self.color, self.pp, self.position, self.size)


    def update(self, dt, input=None):
        self.pp = self.position
        self.velocity += self.acceleration * dt
        self.position += self.velocity * dt
        self.ttl -= 1

    @property
    def is_alive(self):
        return self.ttl > 0

class Rain(Entity):
    def __init__(self, color: pygame.Color, particles_count: int, bounding_box: pygame.Rect, asset=None):
        super().__init__('rain', asset, pygame.Vector2(bounding_box.topleft))
        self.color = color
        self.bounding_box = bounding_box
        self.particles_count = particles_count
        self.particles = [
            Particle(f'rain_{i}', self.color, random_point_in_rect(self.bounding_box)+pygame.Vector2(0, self.bounding_box.h/2), size=1)
            for i in range(self.particles_count)
        ]

    def render(self, surface:pygame.Surface):
        if self.asset:
            surface.blit(self.asset, self.position)
        for particle in self.particles:
            particle.render(surface)

    def update(self, dt, input_manager=None):
        for particle in self.particles:
            particle.update(dt, input_manager)
            if not particle.is_alive:
                particle.position = random_point_in_rect(self.bounding_box)+pygame.Vector2(0, self.bounding_box.h/2)
                particle.ttl = 20
                particle.pp = particle.position
