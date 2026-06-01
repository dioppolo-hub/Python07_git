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
    def __init__(self, name, type):
        super().__init__(name, type)
        self.name = name
        self.type = type

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.name = name
        self.type = type

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.name = name
        self.type = type

    def attack(self) -> str:
        return f"{self.name} uses Water Gun!"


class Torragun(Creature):
    def __init__(self, name, type):
        super().__init__(name, type)
        self.name = name
        self.type = type

    def attack(self) -> str:
        return f"{self.name} uses Hydro Pump!"