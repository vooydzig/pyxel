class Event:
    def __init__(self, description, outcome=""):
        self.description = description
        self.outcomes = []
        if outcome:
            self.outcomes = outcome.split(',')

    def process_outcome(self, player):
        if not self.outcomes:
            return
        for _outcome in self.outcomes:
            _outcome.strip()
            value, cargo_name = _outcome.split()
            if '+' in value:
                player.load_cargo(cargo_name, int(value.replace('+', '')))
            elif '-' in value:
                player.unload_cargo(cargo_name, int(value.replace('-', '')))

EMPTY_EVENT = Event("Nothing interesting here.", "")

ISLAND_EVENTS = [
    Event("You have found a buried treasure.", "+100 gold"),
    Event("You have discovered an abandoned supply cache.", "+10 goods"),
    Event("You have traded goods with friendly islanders.", "-10 goods, +20 gold"),
    Event("You have mapped an uncharted reef.", ""),
    Event("You have helped repair a stranded merchant ship.", "+10 goods"),
    Event("You have found a message in a bottle.", ""),
    Event("You have uncovered an ancient pirate map.", ""),
    Event("You have discovered a forgotten shrine.", ""),
    Event("You have found a chest washed ashore.", "+20 gold"),
    Event("You have rescued a sailor from a deserted island.", "+1 crew"),
    Event("You have recovered a captain's lost journal.", ""),
    Event("You have encountered a wandering trader.", "-10 gold, +20 goods"),
    Event("You have found fresh water on a remote island.", ""),
    Event("You have earned the gratitude of local fishermen.", "+1 crew, +10 goods"),
    Event("You have followed a flock of seabirds to hidden supplies.", "+10 goods"),
]

SEA_EVENTS = {
    'castaway': [
        Event("You have rescued a castaway drifting at sea.", "+1 crew"),

    ],
    'trash': [
        Event("You have caught a rare fish.", "+10 goods"),
        Event("You have spotted dolphins guiding your ship.", ""),
    ],
    'shipwreck': [
        Event("You have recovered cargo from a shipwreck.", "+20 gold, +10 goods, +10 ammo"),
        Event("You have discovered the remains of a legendary ship.", "+200 gold, +10 goods"),

    ],
    'bottle': [
        Event("You have found a message in a bottle.", ""),
    ]
}
