from core import conf
from core.assets import AssetManager
from core.renderer import UpscaledRenderer, BaseRenderer

from app import ParticlesApp


app = ParticlesApp(
    conf.SCREEN_WIDTH,
    conf.SCREEN_HEIGHT,
    "Particles",
    renderer=UpscaledRenderer(
    # renderer=BaseRenderer(
        frame_size=(800, 600)
    ),
    asset_manager=AssetManager('../assets/'),
    fps=conf.FPS,
)
app.run()
