import random


def main() -> None:
    print("=== Game Data Alchemist ===")
    players = ["Alice", "bob", "Charlie", "dylan", "Emma", "Gregory",
               "john", "kevin", "Liam"]
    capitalized = [name.capitalize() for name in players]
    already_capitalized = [n for n in players if n == n.capitalize()]
    print(f"\nInitial list of players: {players}")
    print(f"New list with all names capitalized: {capitalized}")
    print(f"New list of capitalized names only: {already_capitalized}")

    scores = {name: random.randint(0, 1000) for name in capitalized}
    average = sum(scores.values()) / len(scores) if scores else 0.0
    high_scores = {n: s for n, s in scores.items() if s > average}
    print(f"\nScore dict: {scores}")
    print(f"Score average is {round(average, 2)}")
    print(f"High scores: {high_scores}")


if __name__ == "__main__":
    main()
