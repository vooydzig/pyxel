import pygame

from core.assets import AssetManager
from core.input import InputManager
from core.renderer import BaseRenderer
from core.ui import GUIManager


class App:
    def __init__(self, width: float, height: float, title: str, renderer:BaseRenderer=None, asset_manager:AssetManager=None, fps:int=60):
        pygame.init()
        self.screen_size = pygame.Vector2(width, height)
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption(title)
        self.clock = pygame.time.Clock()
        self.running = False
        self.input = InputManager()
        self.renderer = renderer
        self.asset_manager = asset_manager
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
        if self.asset_manager:
            self.asset_manager.initialize()
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
                self.input.keyboard.on_key_down(event.key)
            if event.type == pygame.KEYUP:
                self.input.keyboard.on_key_up(event.key)
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.input.mouse.on_key_down(event.button)
            if event.type == pygame.MOUSEBUTTONUP:
                self.input.mouse.on_key_up(event.button)
