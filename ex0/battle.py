from ex0 import FlameFactory, AquaFactory
from typing import Any


def TestFactory(obj: Any) -> None:
    f1 = obj.create_base()
    f2 = obj.create_evolved()

    print("\nTesting Factory:")
    print(f1.describe())
    print(f1.attack())
    print(f2.describe())
    print(f2.attack())


def TestBattle(flame: Any, aqua: Any) -> None:
    f1 = flame.create_base()
    a1 = aqua.create_base()
    print("\nTesting Battle:")
    print(f1.describe(), "vs", a1.describe())
    print("FIGHT!")
    print(f1.attack())
    print(a1.attack())


if __name__ == "__main__":
    flame = FlameFactory()
    TestFactory(flame)
    aqua = AquaFactory()
    TestFactory(aqua)
    TestBattle(flame, aqua)
