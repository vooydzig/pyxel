import random

from engine.app import App
from entity import Stream


class MatrixApp(App):
    FONT_SIZE = 24
    SPAWN_SPEED = 16 * 60

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.spawn_counter = self.SPAWN_SPEED
        self.streams_count = int(self.screen_size.x / self.FONT_SIZE)

    def initialize(self):
        super().initialize()
        for i in range(self.streams_count):
            y_delta = random.randint(-50 * self.FONT_SIZE, 50 * self.FONT_SIZE)
            self.entities.append(
                Stream(self.assets.get_asset('font', f'minecraft_{self.FONT_SIZE}'), position=(i * self.FONT_SIZE, y_delta)),
            )

    def _update_entities(self):
        super()._update_entities()
        dt = self.clock.get_time()
        self.spawn_counter -= dt
        if self.spawn_counter <= 0:
            self.spawn_counter = self.SPAWN_SPEED
            x_delta = random.randint(0, self.streams_count)
            y_delta = random.randint(-50 * self.FONT_SIZE, 50 * self.FONT_SIZE)
            self.entities.append(
                Stream(self.assets.get_asset('font', f'minecraft_{self.FONT_SIZE}'), position=(x_delta * self.FONT_SIZE, y_delta)),
            )

        for entity in self.entities:
            if entity.characters[-1].position.y > self.screen_size.y:
                y_delta = random.randint(-50 * self.FONT_SIZE, 50 * self.FONT_SIZE)
                for ch in entity.characters:
                    ch.position.y -= (self.screen_size.y + y_delta)
