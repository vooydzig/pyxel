import pygame

from core.renderer import BaseRenderer
from games.ships import conf


class FogOfWarRenderer(BaseRenderer):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.alpha_mask = pygame.Surface(conf.WORLD_SIZE, pygame.SRCALPHA)
        self.mask_position = pygame.Vector2()
        self.alpha_mask.fill((0, 0, 0, 0))
        self.uncharted = None

    def plot_map(self, position, radius=100):
        pygame.draw.circle(self.alpha_mask, (255, 255, 255, 255), (position - self.mask_position), radius)

    def render(self, entities, gui_widgets):
        game = self.screen.copy()
        self._render_background(game)
        self._render_entities(entities, game)
        map = pygame.Surface(self.screen.get_size(), pygame.SRCALPHA)
        map.blit(game, (0, 0))
        map.blit(self.alpha_mask, self.camera.world_to_screen(self.mask_position), special_flags=pygame.BLEND_RGBA_MULT)
        self.screen.blit(self.uncharted, (0, 0))
        self.screen.blit(map, (0, 0))
        self._render_gui(gui_widgets, self.screen)
        self._post_process(self.screen)
