import pygame
from core.entity.sprite import Sprite
from games.ships.cargo import CargoHold


class Player(Sprite):
    ACTIONS = {
        pygame.K_w: 'speed_up',
        pygame.K_s: 'speed_down',
        pygame.K_a: 'rotate_left',
        pygame.K_d: 'rotate_right',
        pygame.K_i: 'show_cargo',
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
        self.cargo = CargoHold()

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

    def render(self, surface, camera):
        # pygame.draw.circle(surface, pygame.Color(conf.COLORS['green']), self.position, self.collision_radius)
        self.trail.render(surface, camera)
        self._blit_rotated(surface, camera)
        self.gui.render(surface, camera)

    def _blit_rotated(self, surface, camera):
        rotated_image = pygame.transform.rotate(self.asset, self.current_angle)
        position = camera.world_to_screen(self.position)
        new_rect = rotated_image.get_rect(center=rotated_image.get_rect(center=position).center)
        surface.blit(rotated_image, new_rect)

    def full_stop(self):
        self.current_speed = 0

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

    def show_cargo(self, dt):
        for name in ['gold', 'crew', 'goods', 'ammo']:
            cargo = getattr(self.cargo, name)
            print(f'{cargo.name}: {cargo.current}/{cargo.max}')

    def load_cargo(self, cargo_name, value):
        getattr(self.cargo, cargo_name).increment(value)

    def unload_cargo(self, cargo_name, value):
        getattr(self.cargo, cargo_name).decrement(value)
