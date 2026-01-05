import random
import pygame


def random_point_in_rect(rect: pygame.Rect):
    return pygame.Vector2(
        random.random() * rect.width + rect.x,
        random.random() * rect.height + rect.y,
    )
