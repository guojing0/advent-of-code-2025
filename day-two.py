# My original version

print('My original version')

with open('day-two.txt') as f:
    num_seq = f.read().split(',')

num_seq = [tuple(map(int, num.split('-'))) for num in num_seq]
part_one_invalid_seq = []
part_two_invalid_seq = []

def part_one_is_invalid(n):
    s = str(n)
    mid = len(s) // 2
    return len(s) % 2 == 0 and s[:mid] == s[mid:]

def part_two_is_invalid(n):
    s = str(n)

    for divided in range(2, len(s) + 1):
        if len(s) % divided == 0:
            part = s[: len(s) // divided]
            if part * divided == s:
                return True
    return False

for start_num, end_num in num_seq:
    for num in range(start_num, end_num + 1):
        if part_one_is_invalid(num):
            part_one_invalid_seq.append(num)
        if part_two_is_invalid(num):
            part_two_invalid_seq.append(num)

print(sum(part_one_invalid_seq))
print(sum(part_two_invalid_seq))

# Claude improved version

print('Claude improved version')

def parse_ranges(filename: str) -> list[tuple[int, int]]:
    with open(filename) as f:
        ranges = f.read().split(',')
    return [tuple(map(int, r.split('-'))) for r in ranges]

def is_repeated_twice(n: int) -> bool:
    s = str(n)
    length = len(s)
    
    if length % 2 != 0:
        return False
    
    mid = length // 2
    return s[:mid] == s[mid:]

def is_repeated(n: int) -> bool:
    s = str(n)
    length = len(s)
    
    # Try all possible pattern lengths (from 1 to length/2)
    for pattern_length in range(1, length // 2 + 1):
        if length % pattern_length == 0:
            pattern = s[:pattern_length]
            repeated_times = length // pattern_length
            if pattern * repeated_times == s:
                return True

    return False

def find_invalid_ids(ranges: list[tuple[int, int]], validator) -> list[int]:
    invalid_ids = []
    
    for start, end in ranges:
        for num in range(start, end + 1):
            if validator(num):
                invalid_ids.append(num)
    
    return invalid_ids

def main() -> None:
    ranges = parse_ranges('day-two.txt')
    
    part_one_invalid = find_invalid_ids(ranges, is_repeated_twice)
    part_two_invalid = find_invalid_ids(ranges, is_repeated)
    
    print(sum(part_one_invalid))
    print(sum(part_two_invalid))

if __name__ == '__main__':
    main()
