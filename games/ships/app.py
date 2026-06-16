import pygame

from core.app import App
from core.renderer import Background
from games.ships.player import Player
from games.ships.trail import Trail
from games.ships import conf


class BootyCallsApp(App):
    def initialize(self):
        super().initialize()
        self.renderer.background = Background(pygame.Color(conf.COLORS['dark_sea']))
        self.player = Player('player', self.asset_manager.get_asset('image', 'ship (1)'))
        self.player.position = self.renderer.canvas_size / 2
        self.player.trail = Trail(self.asset_manager.get_asset('image', 'wake'), self.player.position)
        self.entities.append(
            self.player
        )
