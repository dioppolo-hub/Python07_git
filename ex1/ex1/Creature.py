from abc import ABC, abstractmethod
from ex1.Abilities import TransformCapability, HealCapability


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
        if form == False:
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
        if form == False:
            return "Morphagon uses Tail Attack!"
        else:
            return "Morphagon uses Dragon Morph Dive!"
