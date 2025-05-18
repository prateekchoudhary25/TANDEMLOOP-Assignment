def count_multiples(numbers):
    multiples_count = {i: 0 for i in range(1, 10)}
    for num in numbers:
        for divisor in range(1, 10):
            if num % divisor == 0:
                multiples_count[divisor] += 1
    return multiples_count

# Example Usage
if __name__ == "__main__":
    input_numbers = [1, 2, 8, 9, 12, 46, 76, 82, 15, 20, 30]
    result = count_multiples(input_numbers)
    print(result)
