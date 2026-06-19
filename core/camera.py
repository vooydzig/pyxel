
class Camera:
    def __init__(self, position, screen_size):
        self._position = position
        self.screen_size = screen_size

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value

    def world_to_screen(self, position):
        return position - self._position
