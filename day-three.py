with open('day-three.txt') as f:
    lines = f.read().splitlines()

line_length = len(lines[0])
joltage_list = []

for line in lines:
    curr_max_num = 0
    curr_max_lead_digit = 0

    for i in range(line_length - 1):
        curr_lead_digit = int(line[i])

        if curr_lead_digit > curr_max_lead_digit:
            curr_max_lead_digit = curr_lead_digit

            for j in range(i + 1, line_length):
                curr_digit = int(line[j])

                curr_num = curr_lead_digit * 10 + curr_digit

                if curr_num > curr_max_num:
                    curr_max_num = curr_num

    joltage_list.append(curr_max_num)

print(sum(joltage_list))


### Claude improved version

def max_k_digit_number(line, k):
    """Find the max k-digit number from any k digits in order."""
    n = len(line)
    digits = []
    cursor = 0

    for i in range(k):
        # Valid range: [cursor, n - (k - 1 - i))
        # Need to leave room for (k - 1 - i) more digits after this pick
        end = n - (k - 1 - i)

        # Find leftmost maximum in line[cursor:end]
        best_pos = cursor
        for j in range(cursor + 1, end):
            if line[j] > line[best_pos]:
                best_pos = j

        digits.append(line[best_pos])
        cursor = best_pos + 1

    return int(''.join(digits))

print(sum(max_k_digit_number(line, 2) for line in lines))   # Part 1
print(sum(max_k_digit_number(line, 12) for line in lines))  # Part 2
