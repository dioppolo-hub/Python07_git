from abc import ABC, abstractmethod


class BattleStrategy(ABC):
    @abstractmethod
    def act(self):
        pass

    @abstractmethod
    def is_valid(self) -> bool:
        pass


class NormalStrategy(BattleStrategy):
    def Norm_strategy(self):
