import pygame

from core.entity import Entity
from core.ui.widgets import Widget


class BaseRenderer:
    def __init__(self, *args, **kwargs):
        self.screen = None
        self.screen_size = None

    @property
    def canvas_size(self):
        return pygame.math.Vector2(self.screen.get_size())

    def set_destiation(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_size = pygame.Vector2(screen.get_size())

    def render(self, entities: list[Entity], gui_widgets: list[Widget]):
        self.screen.fill(pygame.Color(0, 0, 0))
        self._render_entities(entities, self.screen)
        self._render_gui(gui_widgets, self.screen)
        self._post_process(self.screen)

    def update(self, dt:float):
        pass

    def _render_entities(self, entities:list[Entity], frame:pygame.Surface):
        for entity in entities:
            entity.render(frame)

    def _render_gui(self, gui_widgets:list[Widget], frame: pygame.Surface):
        for widget in gui_widgets:
            widget.render(frame)

    def _post_process(self, *args, **kwargs):
        pygame.display.flip()


class SingleFrameRenderer(BaseRenderer):
    def render(self, entities: list[Entity], gui_widgets: list[Widget]):
        self.screen.fill(pygame.Color(0, 0, 0))
        pygame.display.flip()

    def update(self, dt:float):
        pass


class UpscaledRenderer(BaseRenderer):
    def __init__(self, frame_size: tuple, *args, **kwargs):
        self.frame_size = frame_size
        super().__init__(*args, **kwargs)

    @property
    def canvas_size(self):
        return pygame.math.Vector2(self.frame_size)

    def render(self, entities: list[Entity], gui_widgets: list[Widget]):
        frame = pygame.Surface(self.frame_size)
        frame.fill(pygame.Color(0, 0, 0))
        self._render_entities(entities, frame)
        scaled_frame = pygame.transform.scale(frame, self.screen.get_size())
        self._render_gui(gui_widgets, scaled_frame)
        self._post_process(scaled_frame)

    def update(self, dt:float):
        pass

    def _render_entities(self, entities:list[Entity], frame: pygame.Surface):
        for entity in entities:
            entity.render(frame)

    def _render_gui(self, gui_widgets:list[Widget], frame: pygame.Surface):
        for widget in gui_widgets:
            widget.render(frame)

    def _post_process(self, frame: pygame.Surface):
        self.screen.blit(frame, (0, 0))
        pygame.display.flip()


class PutPixelRenderer(BaseRenderer):
    def __init__(self, frame_size:tuple, *args, **kwargs):
        self.frame_size = frame_size
        super().__init__(*args, **kwargs)

    def render(self, entities: list[Entity], gui_widgets: list[Widget]):
        frame = pygame.Surface(self.frame_size)
        frame.fill(pygame.Color(0, 0, 0))
        super().render(entities, gui_widgets, frame)
        for x in range(frame.get_width()):
            for y in range(frame.get_height()):
                color = frame.get_at((x, y))
                self.screen.set_at((x, y), color)
        pygame.display.flip()

    def update(self, dt:float):
        pass
