import pygame


class BaseRenderer:
    def __init__(self, *args, **kwargs):
        self.screen = None
        self.screen_size = None

    def set_destiation(self, screen: pygame.Surface):
        self.screen = screen
        self.screen_size = pygame.Vector2(screen.get_size())

    def render(self, entities: list, gui_widgets: list, screen: pygame.Surface):
        self._render_entities(entities, screen)
        self._render_gui(gui_widgets, screen)
        self._post_process(screen)

    def update(self, dt):
        raise NotImplementedError

    def _render_entities(self, entities, frame):
        for entity in entities:
            entity.render(frame)

    def _render_gui(self, gui_widgets, frame):
        for widget in gui_widgets:
            widget.render(frame)

    def _post_process(self, *args, **kwargs):
        pygame.display.flip()


class SingleFrameRenderer(BaseRenderer):
    def render(self, entities: list, gui_widgets: list, screen: pygame.Surface):
        screen.fill(pygame.Color(132, 165, 66))
        pygame.display.flip()

    def update(self, dt):
        pass


class UpscaledRenderer(BaseRenderer):
    def __init__(self, frame_size, *args, **kwargs):
        self.frame_size = frame_size
        super().__init__(*args, **kwargs)

    def render(self, entities: list, gui_widgets: list, screen: pygame.Surface):
        frame = pygame.Surface(self.frame_size)
        screen.fill(pygame.Color(132, 165, 66))
        super().render(entities, gui_widgets, frame)

    def update(self, dt):
        pass

    def _render_entities(self, entities, frame):
        for entity in entities:
            entity.render(frame)

    def _render_gui(self, gui_widgets, frame):
        for widget in gui_widgets:
            widget.render(frame)

    def _post_process(self, frame):
        scaled_frame = pygame.transform.scale(frame, self.screen.get_size())
        self.screen.blit(scaled_frame, (0, 0))
        pygame.display.flip()
        self.frame = None


class PutPixelRenderer(BaseRenderer):
    def __init__(self, frame_size, *args, **kwargs):
        self.frame_size = frame_size
        super().__init__(*args, **kwargs)

    def render(self, entities: list, gui_widgets: list, screen: pygame.Surface):
        frame = pygame.Surface(self.frame_size)
        frame.fill(pygame.Color(132, 165, 66))
        super().render(entities, gui_widgets, frame)
        for x in range(frame.get_width()):
            for y in range(frame.get_height()):
                color = frame.get_at((x, y))
                screen.set_at((x, y), color)
        pygame.display.flip()

    def update(self, dt):
        pass
