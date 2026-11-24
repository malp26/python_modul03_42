import math


def get_player_pos() -> tuple[float, float, float]:
    while True:
        text = input("Enter new coordinates as floats in format 'x,y,z': ")
        try:
            x_text, y_text, z_text = text.split(",")
        except ValueError:
            print("Invalid syntax")
            continue
        values: list[float] = []
        for parameter in (x_text, y_text, z_text):
            try:
                value = float(parameter)
                if not -float("inf") < value < float("inf"):
                    raise ValueError("coordinate must be a finite number")
                values.append(value)
            except ValueError as error:
                print(f"Error on parameter '{parameter.strip()}': {error}")
                break
        else:
            x, y, z = values
            return (x, y, z)


def distance(first: tuple[float, float, float],
             second: tuple[float, float, float]) -> float:
    x1, y1, z1 = first
    x2, y2, z2 = second
    result = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    if result == float("inf"):
        raise OverflowError("distance is too large")
    return result


def main() -> None:
    print("=== Game Coordinate System ===")
    try:
        print("\nGet a first set of coordinates")
        first = get_player_pos()
        print(f"Got a first tuple: {first}")
        x, y, z = first
        print(f"It includes: X={x}, Y={y}, Z={z}")
        print(f"Distance to center: {round(distance(first, (0, 0, 0)), 4)}")
        print("\nGet a second set of coordinates")
        second = get_player_pos()
        print("Distance between the 2 sets of coordinates: "
              f"{round(distance(first, second), 4)}")
    except (EOFError, KeyboardInterrupt):
        print("\nCoordinate input cancelled.")
    except OverflowError:
        print("Coordinates are too large to calculate the distance.")


if __name__ == "__main__":
    main()
