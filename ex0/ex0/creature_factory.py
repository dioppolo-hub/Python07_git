from abc import ABC
from ex0.Creature import Flameling, Pyrodon, Aquabub, Torragun
from ex0.Creature import Creature


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
