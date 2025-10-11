import pygame


from engine.input import InputManager
from game.player import Player
from engine.ui import GUIManager, Label


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
        self.ui = GUIManager(self)
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
            # Load default assets if any
            self.assets.initialize()
        self.player = Player('player', self.assets.get_asset('image', 'player'))
        self.player.position = pygame.Vector2(141, 70)
        self.entities.append(
            self.player
        )
        self.running = True

        widget = Label(0, 0, 'Tomek', self.assets.get_asset('font', 'minecraft_12'))
        self.player.attach_widget('name', widget, position_offset=(12, -20))
        self.ui.add_widget('fps_label', Label(10, 10, 'FPS: 0', self.assets.get_asset('font', 'minecraft_12')))

    def loop(self):
        self.clock.tick(self.fps)
        self._process_events()
        self.update()
        self.render()

    def update(self):
        self.input.update()
        for entity in self.entities:
            entity.update(self.clock.get_time(), self.input)
        self.renderer.update(self.clock.get_time())
        self.ui.get_widget('fps_label').set_text(f'FPS: {self.clock.get_fps():.2f}')
        self.ui.get_widget('fps_label').set_position(10, self.screen_size.y - 20)
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