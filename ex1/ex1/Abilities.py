from abc import ABC, abstractmethod


class HealCapability(ABC):
    def heal(target: str) -> str:
        return f"heals {target} for a small amount"


class TransformCapability(ABC):
    def __init__(self):
        self._transformed = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass

    def get_form(self):
        return self._transformed

    def change_form(self):
        if self._transformed == False:
            self._transformed = True
        else:
            self._transformed = False
