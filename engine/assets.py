import os
import pygame
from pygame import image


class AssetManager:
    IMAGES = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']
    FONTS = ['.ttf', '.otf']
    FONT_SIZES = [4, 6, 8, 12, 18, 24, 32, 48, 64]

    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.assets = {
            'image': {},
            'sound': {},
            'font': {},
        }

    def initialize(self):
        self.assets['font']['default'] = pygame.font.SysFont('Arial', 18)
        assert os.path.exists(self.root_dir)
        for dirpath, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                name, ext = os.path.splitext(filename)
                if ext.lower() in self.IMAGES:
                    self._load_image(name, filepath)
                if ext.lower() in self.FONTS:
                    for size in self.FONT_SIZES:
                        font_key = f"{name}_{size}"
                        self._load_font(font_key, filepath, size)
                    self._load_font(name, filepath, 18)  # Default size

    def _load_image(self, name, path):
        self.assets['image'][name] = image.load(path)

    def _load_font(self, name, font_name, font_size):
        self.assets['font'][name] = pygame.font.Font(font_name, font_size)

    def get_asset(self, asset_type, name):
        return self.assets.get(asset_type, {}).get(name)

    def list_assets(self):
        return [
            (asset_type, list(assets.keys()))
            for asset_type, assets in self.assets.items()
        ]
