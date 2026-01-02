from core import conf
from core.assets import AssetManager
from core.renderer import UpscaledRenderer, BaseRenderer

from app import WarpspeedApp


app = WarpspeedApp(
    conf.SCREEN_WIDTH,
    conf.SCREEN_HEIGHT,
    "Warpspeed",
    # renderer=UpscaledRenderer(
    renderer=BaseRenderer(
        frame_size=(800, 600)
    ),
    asset_manager=AssetManager('../assets/'),
    fps=conf.FPS,
)
app.run()
