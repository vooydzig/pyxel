import pygame

from core.app import App
from background import LayeredBackground, BackgroundLayer, ParallaxLayer


class ParallaxApp(App):

    def initialize(self):
        super().initialize()
        background = LayeredBackground()
        background.add_layers([
            BackgroundLayer.create_fit_to_screen(
                f'layer_1',
                self.asset_manager.get_asset('image', 'Bckg'),
                pygame.Vector2(0, 0),
                self.renderer.canvas_size,
            ),
            ParallaxLayer.create_fit_to_screen(
                f'layer_2',
                self.asset_manager.get_asset('image', 'Cloud'),
                pygame.Vector2(0,0),
                self.renderer.canvas_size,
                0.2
            ),
            ParallaxLayer.create_fit_to_screen(
                f'layer_3',
                self.asset_manager.get_asset('image', 'Mountain_2'),
                pygame.Vector2(0, 0),
                self.renderer.canvas_size,
                0.1
            )
        ])
        self.renderer.background = background

    def _update_entities(self):
        self.renderer.background.update(self.clock.get_time(), self.input)
        for entity in self.entities:
            entity.update(self.clock.get_time(), self.input)
