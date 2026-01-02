from core import conf
from core.assets import AssetManager
from core.renderer import UpscaledRenderer, BaseRenderer

from app import MatrixApp


app = MatrixApp(
    conf.SCREEN_WIDTH,
    conf.SCREEN_HEIGHT,
    "Matrix",
    renderer=BaseRenderer(
        frame_size=(conf.CANVAS_WIDTH, conf.CANVAS_HEIGHT)
    ),
    asset_manager=AssetManager('../assets/'),
    fps=conf.FPS,
)
app.run()
