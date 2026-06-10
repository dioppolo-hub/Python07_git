from abc import ABC, abstractmethod
from typing import Any
from ex2.Abilities import TransformCapability, HealCapability


class Creature(ABC):
    def __init__(self, name: str, type: str):
        super().__init__()
        self.name = name
        self.type = type

    @abstractmethod
    def attack(self, target: Any) -> str:
        pass

    def describe(self) -> str:
        return f"{self.name} is a {self.type} type Creature"


class Flameling(Creature):
    def __init__(self):
        super().__init__("Flameling", "Fire")

    def attack(self, target: Creature) -> str:
        return f"Flameling uses Ember on {target.name}!"


class Aquabub(Creature):
    def __init__(self):
        super().__init__("Aquabub", "Water")

    def attack(self, target: Creature) -> str:
        return f"Aquabub uses Water Gun on {target.name}!"


class Sproutling(Creature, HealCapability):
    def __init__(self):
        super().__init__("Sproutling", "Grass")

    def attack(self, target: Creature) -> str:
        return f"Sproutling uses Vine Whip on {target.name}!"

    def heal(self, target: Creature) -> str:
        return f"Sproutling heal {target.name}"


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self, target: Creature) -> str:
        return f"Bloomelle uses Petal Dance on {target.name}!"

    def heal(self, target: Creature) -> str:
        return f"Bloomelle heal {target.name}"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")

    def transform(self) -> str:
        self.change_form()
        return "Shiftling shifts into a sharper form"

    def revert(self):
        self.change_form()
        return "Shiftling returns to normal"

    def attack(self, target: Creature) -> str:
        form = self.get_form()
        if not form:
            return f"Shiftling uses Normal Attack on {target.name}!"
        else:
            return f"Shiftling uses Boosted Attck on {target.name}!"


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")

    def transform(self) -> str:
        self.change_form()
        return "Morphagon morphs into a Draconic Battle Form!"

    def revert(self):
        self.change_form()
        return "Morphagon stabilizes its form"

    def attack(self, target: Creature) -> str:
        form = self.get_form()
        if not form:
            return f"Morphagon uses Tail Attack on {target.name}!"
        else:
            return f"Morphagon uses Dragon Morph Dive on {target.name}!"
