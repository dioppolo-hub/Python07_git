from abc import ABC
from Creature import Flameling, Pyrodon, Aquabub, Torragun
import Creature


class CreatureFactory(ABC):
    def create_base():
        pass

    def create_evolved():
        pass


class FlameFactory(CreatureFactory):
    def create_base() -> Creature:
        return Flameling()

    def create_evolved() -> Creature:
        return Pyrodon()


class AquaFactory(CreatureFactory):
    def create_base() -> Creature:
        return Aquabub()

    def create_evolved() -> Creature:
        return Torragun()
