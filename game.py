from game.app import GameApp
from engine import conf
from engine.assets import AssetManager
from engine.renderer import UpscaledRenderer

app = GameApp(
    conf.SCREEN_WIDTH,
    conf.SCREEN_HEIGHT,
    "Game",
    renderer=UpscaledRenderer(
        frame_size=(conf.CANVAS_WIDTH, conf.CANVAS_HEIGHT)
    ),
    assets=AssetManager('./assets/'),
    fps=conf.FPS,
)
app.run()
