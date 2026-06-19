from core.assets import AssetManager
from games.ships import conf
from games.ships.app import BootyCallsApp
from games.ships.renderer import FogOfWarRenderer

app = BootyCallsApp(
    conf.SCREEN_WIDTH,
    conf.SCREEN_HEIGHT,
    "Booty Calls",
    renderer=FogOfWarRenderer(
        frame_size=(conf.CANVAS_WIDTH, conf.CANVAS_HEIGHT)
    ),
    asset_manager=AssetManager('../../assets/booty/'),
    fps=conf.FPS,
)
app.run()
