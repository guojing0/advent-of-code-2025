TRACK_SIZE = 100
START_POSITION = 50


def parse_moves(filename: str) -> list[tuple[str, int]]:
    with open(filename) as f:
        return [(line[0], int(line[1:])) for line in f]

def count_zeros_crossed(position: int, distance: int, going_right: bool) -> int:
    """Count how many times the dial passes through zero during a rotation."""
    if going_right:
        first_zero = TRACK_SIZE - position
    else:
        first_zero = TRACK_SIZE if position == 0 else position

    if distance < first_zero:
        return 0
    return (distance - first_zero) // TRACK_SIZE + 1

def simulate_dial(moves: list[tuple[str, int]], count_all_zeros: bool) -> int:
    """Simulate dial rotations and count zeros."""
    position = START_POSITION
    zero_count = 0

    for direction, distance in moves:
        if count_all_zeros:
            zero_count += count_zeros_crossed(position, distance, direction == 'R')

        if direction == 'R':
            position = (position + distance) % TRACK_SIZE
        else:
            position = (position - distance) % TRACK_SIZE

        if not count_all_zeros and position == 0:
            zero_count += 1

    return zero_count

def main() -> None:
    moves = parse_moves('day-one.txt')
    print(simulate_dial(moves, count_all_zeros=False))  # Part 1
    print(simulate_dial(moves, count_all_zeros=True))   # Part 2

if __name__ == '__main__':
    main()
