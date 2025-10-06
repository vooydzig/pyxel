class GUIManager:
    def __init__(self, app):
        self.app = app
        self._widgets = []

    def update(self, dt):
        for widget in self._widgets:
            widget.update(dt)

    @property
    def widgets(self):
        # TODO: overdrawn?
        return sorted(self._widgets, key=lambda w: w.z_index) if self._widgets else []

