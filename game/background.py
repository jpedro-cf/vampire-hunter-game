from game.entity import Entity


class Background(Entity):
    def __init__(
        self, name, position, surface="./assets/backgrounds/PNG/1/terrace.png"
    ):
        super().__init__(name, position, surface)
