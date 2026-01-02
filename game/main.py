from game.app import GameApp
from core import conf
from core.assets import AssetManager
from core.renderer import UpscaledRenderer

app = GameApp(
    conf.SCREEN_WIDTH,
    conf.SCREEN_HEIGHT,
    "Game",
    renderer=UpscaledRenderer(
        frame_size=(conf.CANVAS_WIDTH, conf.CANVAS_HEIGHT)
    ),
    asset_manager=AssetManager('../assets/'),
    fps=conf.FPS,
)
app.run()
