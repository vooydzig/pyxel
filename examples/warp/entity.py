import pygame

from core.entity import Entity


class Star(Entity):
    SPEED = 0.1

    def __init__(self, name, position):
        super().__init__(name, None, position)
        self.previous_position = pygame.Vector3(self.position)
        self.size = 4
        self.turn_delta = pygame.Vector2()

    def render(self, surface, camera):
        surface_size = pygame.math.Vector2(surface.get_size())
        coords_2d = self.to_screen_coords(self.position, self.position.z, surface_size)
        prev_coords_2d = self.to_screen_coords(
            self.previous_position,
            self.previous_position.z,
            surface_size
        )
        pygame.draw.line(surface, (255, 255, 255), coords_2d, prev_coords_2d, self.size)

    def update(self, dt, input_manager=None):
        self.previous_position = pygame.Vector3(self.position)
        speed = self.SPEED
        if input_manager.is_mouse_held(pygame.BUTTON_LEFT):
            speed *= 2
        elif input_manager.is_mouse_held(pygame.BUTTON_RIGHT):
            speed /= 2

        self.position.x += self.turn_delta.x * self.position.z
        self.position.y += self.turn_delta.y * self.position.z
        self.position.z -= speed

    def to_screen_coords(self, coords_3d, camera_distance, surface_size):
        return pygame.math.Vector2(
            (coords_3d.x / camera_distance) + surface_size.x / 2,
            (coords_3d.y / camera_distance) + surface_size.y / 2,
        )
