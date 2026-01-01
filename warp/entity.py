import pygame

from core.entity import Entity


class Star(Entity):
    SPEED = 0.5

    def __init__(self, name, position):
        super().__init__(name, None)
        self.position = position
        self.pz = self.position.z
        self.size = 4

    def render(self, surface):
        surface_size = pygame.math.Vector2(surface.get_size())
        coords_2d = self.to_screen_coords(self.position, self.position.z, surface_size)
        prev_coords_2d = self.to_screen_coords(self.position, self.pz, surface_size)
        pygame.draw.line(surface, (255, 255, 255), coords_2d, prev_coords_2d, self.size)
        self.pz = self.position.z

    def update(self, dt, input):
        speed = self.SPEED
        if input.is_mouse_held(pygame.BUTTON_LEFT):
            speed *= 2
        elif input.is_mouse_held(pygame.BUTTON_RIGHT):
            speed /= 2
        self.position.z -= speed

    def to_screen_coords(self, coords_3d, camera_distance, surface_size):
        return pygame.math.Vector2(
            (coords_3d.x / camera_distance) + surface_size.x / 2,
            (coords_3d.y / camera_distance) + surface_size.y / 2,
        )
