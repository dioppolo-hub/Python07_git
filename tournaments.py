from ex2 import NormalStrategy, AggressiveStrategy, DefensiveStrategy
from ex2 import FlameFactory, AquaFactory, InvalidStrategyError
from ex2 import TransformCreatureFactory, HealingCreatureFactory


def battle(tournament_id, opponents: list) -> None:
    creatures = []
    for factory, strategy in opponents:
        creatures.append((factory.create_base(), strategy))
    print(f"\nTournament {tournament_id}")
    print("*** Tournament ***")
    print(f"{len(creatures)} opponents involved")
    for i in range(len(creatures)):
        for j in range(i + 1, len(creatures)):
            creature1, strategy1 = creatures[i]
            creature2, strategy2 = creatures[j]
            print("* Battle *")
            print(creature1.describe())
            print("vs.")
            print(creature2.describe())
            print("FIGHT!")
            try:
                strategy1.act(creature1, creature2)
            except InvalidStrategyError:
                print(f"Battle error, Invalid Strategy for {creature1.name}")
            try:
                strategy2.act(creature2, creature1)
            except InvalidStrategyError:
                print(f"Battle error, Invalid Strategy for {creature2.name}")


def main():
    normal = NormalStrategy()
    aggressive = AggressiveStrategy()
    defensive = DefensiveStrategy()
    tournaments = [
        [
            (FlameFactory(), normal),
            (AquaFactory(), normal),
        ],
        [
            (FlameFactory(), aggressive),
            (HealingCreatureFactory(), defensive),
        ],
        [
            (AquaFactory(), normal),
            (HealingCreatureFactory(), defensive),
            (TransformCreatureFactory(), aggressive),
        ]
    ]
    for i, tournament in enumerate(tournaments):
        battle(i, tournament)


if __name__ == "__main__":
    main()
