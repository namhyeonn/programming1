numbers = [int input(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)) for _ in range(10)]
remainders = {num % 42 for num in numbers}
unique_remainder_count = len(remainders)
print(unique_remainder_count)
