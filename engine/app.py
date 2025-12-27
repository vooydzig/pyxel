import pygame

from engine.input import InputManager
from game.player import Player
from engine.ui import GUIManager
from engine.ui import widgets


class App:
    def __init__(self, width, height, title, renderer=None, assets=None, fps=60):
        pygame.init()
        self.screen_size = pygame.Vector2(width, height)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = False
        self.input = InputManager()
        self.renderer = renderer
        self.assets = assets
        self.ui = GUIManager()
        self.player = None
        self.entities = []
        self.fps = fps

    def run(self):
        self.initialize()
        while self.running:
            self.loop()
        pygame.quit()

    def initialize(self):
        self.renderer.set_destiation(self.screen)
        if self.assets:
            self.assets.initialize()
        self.running = True

    def loop(self):
        self.clock.tick(self.fps)
        self._process_events()
        self.update()
        self.render()

    def update(self):
        self._update_input()
        self._update_entities()
        self._update_renderer()
        self._update_ui()

    def _update_input(self):
        self.input.update()

    def _update_entities(self):
        for entity in self.entities:
            entity.update(self.clock.get_time(), self.input)

    def _update_renderer(self):
        self.renderer.update(self.clock.get_time())

    def _update_ui(self):
        self.ui.update(self.clock.get_time())

    def render(self):
        self.renderer.render(
            self.entities,
            self.ui.widgets,
        )

    def _process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                self.running = False
            if event.type == pygame.KEYDOWN:
                self.input.on_key_down(event.key)
            if event.type == pygame.KEYUP:
                self.input.on_key_up(event.key)

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
