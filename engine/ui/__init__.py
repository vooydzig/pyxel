import pygame


class GUIManager:
    def __init__(self, parent=None):
        self.parent = parent
        self._widgets = {}
        self._widget_relative_positions = {}

    def update(self, dt):
        for name, widget in self._widgets.items():
            widget.position = self.get_widget_relative_position(name)
            widget.update(dt)

    def add_widget(self, name, widget, relative_position=pygame.Vector2(0, 0)):
        if name in self._widgets:
            raise ValueError(f"Widget with name '{name}' already exists.")
        self._widget_relative_positions[name] = relative_position
        self._widgets[name] = widget

    def get_widget(self, name):
        return self._widgets.get(name)

    def move_widget(self, name, relative_position):
        if name not in self._widgets:
            raise ValueError(f"Widget with name '{name}' does not exist.")
        self._widget_relative_positions[name] = relative_position

    @property
    def widgets(self):
        widgets = self._widgets.values()
        return sorted(widgets, key=lambda w: w.z_index)

    def get_widget_relative_position(self, widget_name):
        parent_position = pygame.Vector2()
        if self.parent:
            parent_position = self.parent.position
        return  parent_position + self._widget_relative_positions[widget_name]

    def render(self, surface):
        for widget in self._widgets.values():
            widget.render(surface)
