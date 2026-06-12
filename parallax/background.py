import pygame

from core.background import LayeredBackground, BackgroundLayer, ParallaxLayer


class MountainRange(LayeredBackground):
    def __init__(self, asset_manager, background_size):
        super().__init__()
        self.add_layers([
            BackgroundLayer.create_fit_to_screen(
                f'layer_1',
                asset_manager.get_asset('image', 'sky'),
                pygame.Vector2(0, 0),
                background_size,
            ),
            ParallaxLayer.create_fit_to_screen(
                f'layer_2',
                asset_manager.get_asset('image', 'clouds_bg'),
                pygame.Vector2(0, 0),
                background_size,
                0.1
            ),
            ParallaxLayer.create_fit_to_screen(
                f'layer_5',
                asset_manager.get_asset('image', 'glacial_mountains'),
                pygame.Vector2(0, 0),
                background_size,
                0.2
            ),
            ParallaxLayer.create_fit_to_screen(
                f'layer_3',
                asset_manager.get_asset('image', 'cloud_lonely'),
                pygame.Vector2(0, 0),
                background_size,
                0.5
            ),
            ParallaxLayer.create_fit_to_screen(
                f'layer_6',
                asset_manager.get_asset('image', 'clouds_mg_1'),
                pygame.Vector2(0, 0),
                background_size,
                0.3
            ),
            ParallaxLayer.create_fit_to_screen(
                f'layer_7',
                asset_manager.get_asset('image', 'clouds_mg_2'),
                pygame.Vector2(0, 0),
                background_size,
                0.25
            ),
        ])
