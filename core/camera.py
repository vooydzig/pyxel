
class Camera:
    def __init__(self, position, screen_size):
        self._position = position
        self.screen_size = screen_size
        self.bounds = None

    @property
    def position(self):
        return self._position

    @position.setter
    def position(self, value):
        self._position = value
        if self.bounds:
            self._position.x = max(0, min(self._position.x, self.bounds.x - self.screen_size.x))
            self._position.y = max(0, min(self._position.y, self.bounds.y - self.screen_size.y))


    def world_to_screen(self, position):
        return position - self._position

    def bound_to(self, bounds):
        self.bounds = bounds
