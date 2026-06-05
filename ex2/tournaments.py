from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2 import FlameFactory, AquaFactory, InvalidStrategyError
from ex2 import TransformCreatureFactory, HealingCreatureFactory


def battle(opponents: list):
    RED = "\033[91m"
    GREEN = "\033[92m"
    RESET = "\033[0m"
    creatures = []
    for factory, strategy in opponents:
        creatures.append((factory.create_base(), strategy))
    count: int = 1
    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            print(f"\n------Tournament {count}------")
            creature1, strategy1 = creatures[i]
            creature2, strategy2 = creatures[j]
            print(
                f"[({creature1.name}+{strategy1.name}),"
                f"({creature2.name}+{strategy2.name}]"
                )
            print(f"{creature1.describe()} vs {creature2.describe()}")
            print(f"\n{GREEN}FIGHT!{RESET}")
            try:
                strategy1.act(creature1, creature2)
            except InvalidStrategyError:
                print(f"{RED}Invalid Strategy for {creature1.name}{RESET}")
            try:
                strategy2.act(creature2, creature1)
            except InvalidStrategyError:
                print(f"{RED}Invalid Strategy for {creature2.name}{RESET}")
            count += 1


def main():
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    opponents = [
        (FlameFactory(), normal),
        (AquaFactory(), normal),
        (TransformCreatureFactory(), aggressive),
        (HealingCreatureFactory(), defensive),
        (FlameFactory(), defensive)
    ]
    battle(opponents)


if __name__ == "__main__":
    main()
