import pygame


class GUIManager:
    def __init__(self, parent):
        self.parent = parent
        self._widgets = {}
        self._widget_relative_positions = {}

    def update(self, dt):
        for name, widget in self._widgets.items():
            widget.set_position(
                self.parent.position.x + self._widget_relative_positions[name].x,
                self.parent.position.y + self._widget_relative_positions[name].y
            )
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

    def render(self, surface):
        for widget in self._widgets.values():
            widget.render(surface)
