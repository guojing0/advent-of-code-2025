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
