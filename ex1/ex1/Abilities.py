from abc import ABC, abstractmethod


class HealCapability(ABC):
    @abstractmethod
    def heal(self, target: str) -> str:
        pass


class TransformCapability(ABC):
    def __init__(self):
        self._transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

    def get_form(self) -> bool:
        return self._transformed

    def change_form(self) -> None:
        if not self._transformed:
            self._transformed = True
        else:
            self._transformed = False
