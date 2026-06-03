from abc import ABC, abstractmethod
from ex2.Abilities import TransformCapability, HealCapability


class Creature(ABC):
    def __init__(self, name: str, type: str):
        super().__init__()
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return "Flameling uses Ember!"


class Pyrodon(Creature):
    def __init__(self):
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return "Pyrodon uses Flamethrower!"


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self) -> str:
        return "Aquabub uses Water Gun!"


class Torragun(Creature):
    def __init__(self):
        super().__init__("Torragun", "Water/Earth")

    def attack(self) -> str:
        return "Torragun uses Hydro Pump!"


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self) -> str:
        return "Sproutling uses Vine Whip!"

    def heal(self, target: str) -> str:
        return f"Sproutling heal {target}"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"

    def heal(self, target: str) -> str:
        return f"Bloomelle heal {target}"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")

    def transform(self) -> str:
        self.change_form()
        return "Shiftling shifts into a sharper form"

    def revert(self):
        self.change_form()
        return "Shiftling returns to normal"

    def attack(self) -> str:
        form = self.get_form()
        if not form:
            return "Shiftling uses Normal Attack!"
        else:
            return "Shiftling uses Boosted Attck!"


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")

    def transform(self) -> str:
        self.change_form()
        return "Morphagon morphs into a Draconic Battle Form!"

    def revert(self):
        self.change_form()
        return "Morphagon stabilizes its form"

    def attack(self) -> str:
        form = self.get_form()
        if not form:
            return "Morphagon uses Tail Attack!"
        else:
            return "Morphagon uses Dragon Morph Dive!"
