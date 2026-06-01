from abc import ABC


class Creature(ABC):
    def __init__(self, name: str, type: str):
        self.name = name
        self.type = type

    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return f"Aquabub uses Water Gun!"


class Torragun(Creature):
    def __init__(self):
        super().__init__("Torragun", "Water/Earth")

    def attack(self) -> str:
        return f"Torragun uses Hydro Pump!"