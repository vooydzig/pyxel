from core.app import App
from examples.parallax.background import MountainRange


class ParallaxApp(App):

    def initialize(self):
        super().initialize()
        self.renderer.background = MountainRange(self.asset_manager, self.renderer.canvas_size)

    def _update_entities(self):
        self.renderer.background.update(self.clock.get_time(), self.input)
        for entity in self.entities:
            entity.update(self.clock.get_time(), self.input)
