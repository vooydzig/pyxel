import pygame

from engine.app import App
from engine.ui import widgets
from game.player import Player


class GameApp(App):
    def initialize(self):
        super().initialize()
        self.player = Player('player', self.assets.get_asset('image', 'player'))
        self.player.position = pygame.Vector2(141, 70)
        self.entities.append(
            self.player
        )
        widget = widgets.Label(0, 0, 'Tomek', self.assets.get_asset('font', 'minecraft_12'))
        self.player.add_widget('name', widget, relative_position=pygame.Vector2(12, -20))
        self.ui.add_widget('fps_label', widgets.Label(10, 10, 'FPS: 0', self.assets.get_asset('font', 'minecraft_12')))
        self.ui.move_widget('fps_label', pygame.Vector2(10, self.screen_size.y - 20))

    def _update_ui(self):
        self.ui.get_widget('fps_label').set_text(f'FPS: {self.clock.get_fps():.2f}')
        super()._update_ui()
