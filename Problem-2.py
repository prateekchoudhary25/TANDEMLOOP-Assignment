def generate_odd_series(a: int) -> str:
    series = [str(2 * i + 1) for i in range(a)]
    return ', '.join(series)

# Example Usage
if __name__ == "__main__":
    try:
        a = int(input("Enter an integer (a): "))
        if a < 1:
            print("Input must be a positive integer.")
        else:
            result = generate_odd_series(a)
            print(f"Output: {result}")
    except ValueError:
        print("Error: Please enter a valid integer.")
