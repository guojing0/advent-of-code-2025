with open('day-five.txt') as f:
    lines = f.read().splitlines()

def parse_range(s):
    start, end = s.split('-')
    return range(int(start), int(end) + 1)

ranges = [parse_range(line) for line in lines if '-' in line]
ids = [int(line) for line in lines if line and '-' not in line]

# Part 1

cnt = sum(any(n in r for r in ranges) for n in ids)
print(cnt)

# Part 2

ranges.sort(key=lambda r: r.start)
merged = [ranges[0]]

for r in ranges[1:]:
    last = merged[-1]

    if r.start <= last.stop:
        merged[-1] = range(last.start, max(last.stop, r.stop))
    else:
        merged.append(r)

fresh_cnt = sum(len(r) for r in merged)
print(fresh_cnt)
