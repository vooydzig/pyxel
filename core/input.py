import pygame


class Device:
    def __init__(self):
        self.last_frame_keys = set()
        self.current_frame_keys = set()

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


class Mouse(Device):
    def __init__(self):
        super().__init__()
        self.last_frame_keys = set()
        self.current_frame_keys = set()
        self.position = pygame.Vector2(0, 0)
        self.delta = pygame.Vector2(0, 0)
        self.wheel = pygame.Vector2(0, 0)


class Keyboard(Device):
    ...


class InputManager:
    def __init__(self):
        self.keyboard = Keyboard()
        self.mouse = Mouse()

    def update(self):
        self.mouse.update()
        self.keyboard.update()
        
    def is_key_pressed(self, key):
        return self.keyboard.is_key_pressed(key)

    def is_key_released(self, key):
        return self.keyboard.is_key_released(key)

    def is_key_held(self, key):
        return self.keyboard.is_key_held(key)

    def is_button_pressed(self, button):
        return self.mouse.is_key_pressed(button)

    def is_button_released(self, button):
        return self.mouse.is_key_released(button)

    def is_mouse_held(self, button):
        return self.mouse.is_key_held(button)
