import os

from pygame import image


class AssetManager:
    IMAGES = ['.png', '.jpg', '.jpeg', '.bmp', '.gif']

    def __init__(self, root_dir):
        self.root_dir = root_dir
        self.assets = {
            'image': {},
            'sound': {},
            'font': {},
        }

    def initialize(self):
        for dirpath, _, filenames in os.walk(self.root_dir):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                name, ext = os.path.splitext(filename)
                if ext.lower() in self.IMAGES:
                    self.load_asset(name, 'image', filepath)

    def load_asset(self, name, asset_type, path):
        self.assets[asset_type][name] = image.load(path)

    def get_asset(self, asset_type, name):
        return self.assets.get(asset_type, {}).get(name)

    def list_assets(self):
        return [
            (asset_type, list(assets.keys()))
            for asset_type, assets in self.assets.items()
        ]
