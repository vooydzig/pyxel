import random
import string
from typing import Any

import pygame

from engine.entity import Entity


class TextEntity(Entity):
    def __init__(self, text, font, color=pygame.Color(255, 255, 255), position=(0, 0)):
        self.position = pygame.Vector2(position)
        self.color = color
        super().__init__(text, font)

    @property
    def text(self):
        return self.name

    @text.setter
    def text(self, text):
        self.name = text

    @property
    def font(self):
        return self.asset

    def render(self, surface):
        surface.blit(self.font.render(self.text, False, self.color), self.position)


class MatrixCharacter(TextEntity):
    DEFAULT_MOVE_SPEED = 16 * 30
    DEFAULT_CHANGE_SPEED = 16 * 30

    def __init__(self, font, move_speed=16 * 30, change_speed=16 * 30, color=pygame.Color(255, 255, 255),
                 position=(0, 0)):
        self.alphabet = string.ascii_letters + string.digits
        self.move_counter = move_speed
        self.change_counter = change_speed
        self.move_speed = move_speed
        self.change_speed = change_speed
        super().__init__('', font, color, position)
        self.set_random_character()

    def move(self):
        self.move_counter = self.move_speed
        self.position.y += self.font.size(self.text)[1]

    def set_random_character(self):
        self.text = random.choice(self.alphabet)

    def update(self, dt, input_manager=None):
        self.move_counter -= dt
        self.change_counter -= dt
        if self.move_counter < 0:
            self.move()
        if self.change_counter < 0:
            self.change_counter = self.change_speed
            self.set_random_character()
        super().update(dt)


class Stream(Entity):
    WHITE_DENSITY = 0.25

    def __init__(self, font, stream_length=16, color=pygame.Color(0, 255, 70), position=(0, 0)):
        self.move_speed = 16 * random.randint(15, 60)
        self.change_speed = 16 * random.randint(15, 60)
        self.stream_length = stream_length
        self.font = font
        self.color = color
        self._generate_stream(position)

    def _generate_stream(self, position: tuple[int, int] | Any):
        self.characters = []
        delta = 0
        for i in range(self.stream_length):
            r = random.random()
            is_white = (i == 0) or r < self.WHITE_DENSITY
            c = pygame.Color(255, 255, 255) if is_white else self.color
            self.characters.append(MatrixCharacter(
                self.font,
                move_speed=self.move_speed,
                change_speed=self.change_speed,
                color=c,
                position=(position[0], position[1] + delta)
            ))
            delta -= self.font.size(self.characters[-1].text)[1]

    def render(self, surface):
        for character in self.characters:
            character.render(surface)

    def update(self, dt, input_manager=None):
        for character in self.characters:
            character.update(dt, input_manager)
