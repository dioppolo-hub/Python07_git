from abc import ABC
from ex2.Creature import Sproutling, Bloomelle, Shiftling, Morphagon
from ex2.Creature import Flameling, Pyrodon, Aquabub, Torragun
from ex2.Creature import Creature


class CreatureFactory(ABC):
    def create_base(self):
        pass

    def create_evolved(self):
        pass


class FlameFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Aquabub()

    def create_evolved(self) -> Creature:
        return Torragun()


class HealingCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Sproutling()

    def create_evolved(self) -> Creature:
        return Bloomelle()


class TransformCreatureFactory(CreatureFactory):
    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
