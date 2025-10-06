from engine.app import App
from engine import conf
from engine.assets import AssetManager
from engine.renderer import UpscaledRenderer

app = App(
    conf.SCREEN_WIDTH,
    conf.SCREEN_HEIGHT,
    "My Application",
    renderer=UpscaledRenderer(
        frame_size=(conf.CANVAS_WIDTH, conf.CANVAS_HEIGHT)
    ),
    assets=AssetManager('./assets/'),
    fps=conf.FPS,
)
app.run()