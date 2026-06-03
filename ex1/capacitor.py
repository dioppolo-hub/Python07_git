from ex1 import HealingCreatureFactory, TransformCreatureFactory
from typing import Any


def TestHealingFactory(creature: Any):
    h1 = creature.create_base()
    h2 = creature.create_evolved()
    print("\nTesting HealingFactory:")
    print("--Base--")
    print(h1.describe())
    print(h1.attack())
    print(h1.heal("itself"))
    print("--Evolved--")
    print(h2.describe())
    print(h2.attack())
    print(h2.heal("itself and others"))


def TestTransformingFactory(creature: Any):
    h1 = creature.create_base()
    h2 = creature.create_evolved()
    print("\nTesting TransformingFactory:")
    print("--Base--")
    print(h1.describe())
    print(h1.attack())
    print(h1.transform())
    print(h1.attack())
    print(h1.revert())
    print("--Evolved--")
    print(h2.describe())
    print(h2.attack())
    print(h2.transform())
    print(h2.attack())
    print(h2.revert())


def main():
    healing = HealingCreatureFactory()
    TestHealingFactory(healing)
    morphing = TransformCreatureFactory()
    TestTransformingFactory(morphing)


if __name__ == "__main__":
    main()
