import random


ACHIEVEMENTS = [
    "First Steps", "Master Explorer", "Boss Slayer", "Treasure Hunter",
    "Speed Runner", "Survivor", "Crafting Genius", "World Savior",
    "Collector Supreme", "Untouchable", "Strategist", "Unstoppable",
    "Hidden Path Finder", "Sharp Mind",
]


def gen_player_achievements() -> set[str]:
    count = random.randint(6, 10)
    return set(random.sample(ACHIEVEMENTS, count))


def main() -> None:
    print("=== Achievement Tracker System ===")
    players = ["Alice", "Bob", "Charlie", "Dylan"]
    collections: list[set[str]] = []
    all_distinct: set[str] = set()
    common = set(ACHIEVEMENTS)
    for player in players:
        achievements = gen_player_achievements()
        collections.append(achievements)
        all_distinct = all_distinct.union(achievements)
        common = common.intersection(achievements)
        print(f"\nPlayer {player}: {achievements}")
    print(f"\nAll distinct achievements: {all_distinct}")
    print(f"Common achievements: {common}")

    index = 0
    for player in players:
        others: set[str] = set()
        other_index = 0
        for achievements in collections:
            if other_index != index:
                others = others.union(achievements)
            other_index += 1
        exclusive = collections[index].difference(others)
        print(f"Only {player} has: {exclusive}")
        index += 1

    index = 0
    for player in players:
        missing = set(ACHIEVEMENTS).difference(collections[index])
        print(f"{player} is missing: {missing}")
        index += 1


if __name__ == "__main__":
    main()
