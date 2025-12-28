from core.app import App
from core import conf
from core.assets import AssetManager
from core.renderer import UpscaledRenderer

app = App(
    conf.SCREEN_WIDTH,
    conf.SCREEN_HEIGHT,
    "Blank app",
    renderer=UpscaledRenderer(
        frame_size=(conf.CANVAS_WIDTH, conf.CANVAS_HEIGHT)
    ),
    assets=AssetManager('./assets/'),
    fps=conf.FPS,
)
app.run()
