#
# Kaili Takara
# September 30, 2026

def get_even_nums(limit):
    even_nums = []

    num = 2
    while num <= limit:
        even_nums.append(num)
        num += 2

    return even_nums


test_cases = [
    (50, list(range(2, 51, 2))),
    (5, [2, 4]),
    (2, [2]),
    (1, []),
]

for limit, expected in test_cases:
    assert get_even_nums(limit) == expected, f"Failed for limit {limit}"

print("All test cases passed.")
print(get_even_nums(50))