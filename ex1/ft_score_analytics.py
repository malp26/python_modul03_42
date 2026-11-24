import sys


def parse_scores(arguments: list[str]) -> list[int]:
    scores: list[int] = []
    for argument in arguments:
        try:
            scores.append(int(argument))
        except ValueError:
            print(f"Invalid parameter: '{argument}'")
    return scores


def main() -> None:
    print("=== Player Score Analytics ===")
    scores = parse_scores(sys.argv[1:])
    if not scores:
        print("No scores provided. Usage: python3 ft_score_analytics.py "
              "<score1> <score2> ...")
        return
    total = sum(scores)
    print(f"Scores processed: {scores}")
    print(f"Total players: {len(scores)}")
    print(f"Total score: {total}")
    try:
        print(f"Average score: {total / len(scores)}")
    except OverflowError:
        print("Average score: too large to represent as a float")
    print(f"High score: {max(scores)}")
    print(f"Low score: {min(scores)}")
    print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    main()
