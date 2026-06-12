import pygame

from core.background import LayeredBackground, BackgroundLayer, ParallaxLayer


class MountainRange(LayeredBackground):
    def __init__(self, asset_manager, background_size):
        super().__init__()
        self.add_layers([
            BackgroundLayer.create_fit_to_screen(
                f'layer_1',
                asset_manager.get_asset('image', 'Bckg'),
                pygame.Vector2(0, 0),
                background_size,
            ),
            ParallaxLayer.create_fit_to_screen(
                f'layer_2',
                asset_manager.get_asset('image', 'Cloud'),
                pygame.Vector2(0, 0),
                background_size,
                0.2
            ),
            ParallaxLayer.create_fit_to_screen(
                f'layer_3',
                asset_manager.get_asset('image', 'Mountain_2'),
                pygame.Vector2(0, 0),
                background_size,
                0.1
            )
        ])
