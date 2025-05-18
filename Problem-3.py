def generate_odd_series(a: int) -> str:
    if a < 1:
        return "Input must be a positive integer."
    last_number = a if a % 2 != 0 else a - 1
    series = [str(num) for num in range(1, last_number + 1, 2)]
    return ', '.join(series)

# Example Usage
if __name__ == "__main__":
    try:
        a = int(input("Enter an integer (a): "))
        result = generate_odd_series(a)
        print(f"Output: {result}")
    except ValueError:
        print("Error: Please enter a valid integer.")
