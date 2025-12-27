from engine import conf
from engine.assets import AssetManager
from engine.renderer import UpscaledRenderer, BaseRenderer

from app import MatrixApp


app = MatrixApp(
    conf.SCREEN_WIDTH,
    conf.SCREEN_HEIGHT,
    "Matrix",
    renderer=BaseRenderer(
        frame_size=(conf.CANVAS_WIDTH, conf.CANVAS_HEIGHT)
    ),
    assets=AssetManager('../assets/'),
    fps=conf.FPS,
)
app.run()
