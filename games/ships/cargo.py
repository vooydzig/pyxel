class Cargo:
    def __init__(self, name, current, max):
        self.name = name
        self.current = current
        self.max = max

    def increment(self, value):
        self.current = min(self.current + value, self.max)

    def decrement(self, value):
        self.current = max(self.current - value, 0)


class CargoHold:
    def __init__(self):
        self.gold = Cargo('gold', 0, 100)
        self.crew = Cargo('crew', 0, 100)
        self.ammo = Cargo('ammo', 0, 100)
        self.goods = Cargo('goods', 0, 100)
