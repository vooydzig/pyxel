import pygame

from core.entity.sprite import Sprite


class Player(Sprite):
    ACTIONS = {
        pygame.K_w: 'move_up',
        pygame.K_s: 'move_down',
        pygame.K_a: 'move_left',
        pygame.K_d: 'move_right',
    }

    def __init__(self, name, asset, position=(0, 0), speed=0.2):
        super().__init__(name, asset, position)
        self.speed = speed
        self.velocity = pygame.Vector2(0, 0)

    def update(self, dt, input_manager=None):
        if input_manager:
            self.velocity.x = 0
            self.velocity.y = 0
            for key, action in self.ACTIONS.items():
                if input_manager.is_key_held(key):
                    getattr(self, action)()
        if self.velocity.length() > 0:
            self.velocity = self.velocity.normalize()
        self.position += self.velocity  * self.speed * dt
        super().update(dt)

    def move_up(self):
        self.velocity.y += -1

    def move_down(self):
        self.velocity.y += 1

    def move_left(self):
        self.velocity.x += -1

    def move_right(self):
        self.velocity.x += 1
