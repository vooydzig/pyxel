from games.ships.app import BootyCallsApp
from games.ships import conf
from core.assets import AssetManager
from core.renderer import BaseRenderer

app = BootyCallsApp(
    conf.SCREEN_WIDTH,
    conf.SCREEN_HEIGHT,
    "Booty Calls",
    renderer=BaseRenderer(
        frame_size=(conf.CANVAS_WIDTH, conf.CANVAS_HEIGHT)
    ),
    asset_manager=AssetManager('../../assets/booty/'),
    fps=conf.FPS,
)
app.run()
