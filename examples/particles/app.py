import random

import pygame

from core.app import App
from core.entity.particles import Rain

class ParticlesApp(App):

    def initialize(self):
        super().initialize()
        cloud = self.asset_manager.get_asset('image', 'cloud')
        cloud = pygame.transform.scale(cloud, (100, 100))
        x_pos = pygame.math.lerp(0, self.renderer.canvas_size.x,
                                 self.input.mouse.position.x / self.screen_size.x)
        self.rain = Rain(pygame.Color(255,255,255), particles_count=100, bounding_box=pygame.Rect(x_pos, 0, 100, 100), asset=cloud)
        self.entities.append(self.rain)

    def update(self):
        super().update()
        x_pos = pygame.math.lerp(0, self.renderer.canvas_size.x, self.input.mouse.position.x/self.screen_size.x) - self.rain.bounding_box.width/2
        self.rain.position.x = x_pos
        self.rain.bounding_box.x = x_pos
