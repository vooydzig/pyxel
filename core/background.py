import pygame

from core import renderer
from core.entity import Entity


class LayeredBackground(renderer.Background):
    def __init__(self):
        self.layers = []

    def add_layers(self, layers: list):
        self.layers.extend(layers)

    def render(self, screen: pygame.Surface):
        for layer in self.layers:
            layer.render(screen)

    def update(self, dt, input_manager=None):
        for layer in self.layers:
            layer.update(dt, input_manager)


class BackgroundLayer(Entity):
    def __init__(self, name, asset, position=pygame.Vector2(), size=pygame.Vector2(64, 64)):
        self.size = size
        super().__init__(name, pygame.transform.scale(asset, self.size), position)

    def render(self, surface):
        surface.blit(self.asset, self.position)

    @classmethod
    def create_fit_to_screen(cls, name, image, position, screen_size):
        image_size = pygame.Vector2(image.get_size())
        if image_size.x > image_size.y:
            scale_factor = screen_size.x / image_size.x
        else:
            scale_factor = screen_size.y / image_size.y

        return cls(
            name, image, position, size=image_size * scale_factor
        )

class ParallaxLayer(BackgroundLayer):
    ACTIONS = {
        pygame.K_a: 'move_left',
        pygame.K_d: 'move_right',
    }

    def __init__(self, speed, *args, **kwargs):
        self.speed = speed
        self.velocity = pygame.Vector2()
        self.blit_position_x = 0
        super().__init__(*args, **kwargs)


    @classmethod
    def create_fit_to_screen(cls, name, image, position, screen_size, speed):
        image_size = pygame.Vector2(image.get_size())
        if image_size.x > image_size.y:
            scale_factor = screen_size.x / image_size.x
        else:
            scale_factor = screen_size.y / image_size.y

        new_size = image_size * scale_factor
        return cls(speed, name, image, position, new_size)

    def update(self, dt, input_manager=None):
        if input_manager:
            self.velocity.x = 0
            self.velocity.y = 0
            if input_manager.is_key_held(pygame.K_a):
                self.velocity.x += 1

            if input_manager.is_key_held(pygame.K_d):
                self.velocity.x += -1

        if self.velocity.length() > 0:
            self.velocity = self.velocity.normalize()
        self.position += self.velocity * self.speed * dt

    def render(self, surface):
        if self.position.x >= surface.get_size()[0]:
            self.position.x = 0
        elif self.position.x <= -surface.get_size()[0]:
            self.position.x = 0
        offset = pygame.Vector2(self.asset.get_size()[0], 0)
        surface.blit(self.asset, self.position-offset)
        surface.blit(self.asset, self.position)
        surface.blit(self.asset, self.position+offset)

