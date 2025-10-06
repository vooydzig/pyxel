import pygame


from engine.input import InputManager
from game.player import Player
from engine.ui import GUIManager


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
        self.renderer.set_destiation(self.screen)
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
        if self.assets:
            # Load default assets if any
            self.assets.initialize()
        self.player = Player('player', self.assets.get_asset('image', 'player'))
        self.entities.append(
            self.player
        )
        self.running = True

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
        # self.ui.update(self.clock.get_time())

    def render(self):
        self.renderer.render(
            self.entities,
            self.ui.widgets,
            self.screen
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