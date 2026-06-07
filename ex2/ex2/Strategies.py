from .Abilities import TransformCapability, HealCapability
from .BattleStrategy import BattleStrategy, InvalidStrategyError
from .Creature import Creature


class NormalStrategy(BattleStrategy):
    def __init__(self):
        super().__init__("NormalStrategy")

    def is_valid(self, creature: Creature):
        return True

    def act(self, creature: Creature, target: Creature):
        print(creature.attack(target))


class AggressiveStrategy(BattleStrategy):
    def __init__(self):
        super().__init__("AggressiveStrategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature, target: Creature):
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                "Creature cannot use AggressiveStrategy"
            )
        print(creature.transform())
        print(creature.attack(target))
        print(creature.revert())


class DefensiveStrategy(BattleStrategy):
    def __init__(self):
        super().__init__("DefensiveStrategy")

    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, HealCapability)

    def act(self, creature: Creature, target: Creature):
        if not isinstance(creature, HealCapability):
            raise InvalidStrategyError(
                "Creature cannot use DefensiveStrategy"
            )
        print(creature.attack(target))
        print(creature.heal(creature))
