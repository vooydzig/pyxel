import pygame

from core.entity.sprite import Sprite


class Trail(Sprite):
    def __init__(self, asset, position):
        super().__init__('trail', asset, position)
        self.points = []
        self.max_points = 10
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

            angle = -diff.as_polar()[1] + 90

            scaled_texture = pygame.transform.scale(self.asset, (8 * int(distance), 8 * current_thickness))
            scaled_texture.set_alpha(current_alpha)
            rotated_texture = pygame.transform.rotate(scaled_texture, angle)
            rect = rotated_texture.get_rect()
            x1, y1 = self.points[i]
            x2, y2 = self.points[i + 1]
            rect.center = ((x1 + x2) // 2, (y1 + y2) // 2)
            surface.blit(rotated_texture, rect.topleft)

    def update(self, dt, input_manager=None):
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
