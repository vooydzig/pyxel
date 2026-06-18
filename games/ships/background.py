import pygame
from core.background import LayeredBackground, BackgroundLayer

class UnchartedMapBackground(LayeredBackground):
    def __init__(self, asset_manager, background_size):
        super().__init__()
        self.add_layers([
            BackgroundLayer(
                f'uncharted',
                asset_manager.get_asset('image', 'map'),
                pygame.Vector2(0, 0),
                background_size,
            )
        ])
