import pygame


class InputManager:
    last_frame_keys = set()
    current_frame_keys = set()
    mouse_pos = pygame.Vector2(0, 0)
    mouse_delta = pygame.Vector2(0, 0)
    mouse_buttons = (0, 0, 0)
    mouse_wheel = 0

    def update(self):
        self.last_frame_keys = self.current_frame_keys.copy()

    def on_key_down(self, key):
        self.current_frame_keys.add(key)

    def on_key_up(self, key):
        self.current_frame_keys.discard(key)

    def is_key_pressed(self, key):
        return key in self.current_frame_keys and key not in self.last_frame_keys

    def is_key_released(self, key):
        return key not in self.current_frame_keys and key in self.last_frame_keys

    def is_key_held(self, key):
        return key in self.current_frame_keys and key in self.last_frame_keys
