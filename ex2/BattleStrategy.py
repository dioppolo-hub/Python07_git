from abc import ABC, abstractmethod
from .Creature import Creature


class BattleStrategy(ABC):
    def __init__(self, name: str):
        super().__init__()
        self.name = name

    @abstractmethod
    def act(self, creature: Creature, target: Creature):
        pass

    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        pass


class InvalidStrategyError(Exception):
    def Norm_strategy(self):
        print("coming soon")
