from abc import ABC, abstractmethod
from ex1.Abilities import TransformCapability, HealCapability


class Creature(ABC):
    def __init__(self, name: str, type: str):
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


class Bloomelle(Creature, HealCapability):
    def __init__(self):
        super().__init__("Bloomelle", "Grass/Fairy")

    def attack(self) -> str:
        return "Bloomelle uses Petal Dance!"


class Shiftling(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Shiftling", "Normal")

    def transform(self) -> str:
        form = TransformCapability.get_form()
        if form == False:
            TransformCapability.change_form()
            return "Shiftling shifts into a sharper form"
        else:
            TransformCapability.change_form()
            return "Shiftling returns to normal"

    def attack(self) -> str:
        form = TransformCapability.get_form()
        if form == False:
            return "Shiftling uses Normal Attack!"
        else:
            return "Shiftling uses Boosted Attck!"


class Morphagon(Creature, TransformCapability):
    def __init__(self):
        super().__init__("Morphagon", "Normal/Dragon")

    def transform(self) -> str:
        form = TransformCapability.get_form()
        if form == False:
            TransformCapability.change_form()
            return "Morphagon morphs into a Draconic Battle Form!"
        else:
            TransformCapability.change_form()
            return "Morphagon stabilizes its form"

    def attack(self) -> str:
        form = TransformCapability.get_form()
        if form == False:
            return "Morphagon uses Normal Attack!"
        else:
            return "Morphagon uses Devastating Morph Strike!"
