class Calculator:
    def __init__(self, a: float, b: float, operation: str):
        self.a = a
        self.b = b
        self.operation = operation.lower()
    
    def calculate(self) -> float:
        if self.operation == 'addition' or self.operation == 'add':
            return self.a + self.b
        elif self.operation == 'subtraction' or self.operation == 'subtract':
            return self.a - self.b
        elif self.operation == 'multiplication' or self.operation == 'multiply':
            return self.a * self.b
        elif self.operation == 'division' or self.operation == 'divide':
            if self.b == 0:
                raise ValueError("Cannot divide by zero")
            return self.a / self.b
        else:
            raise ValueError("Invalid operation. Please use: addition, subtraction, multiplication, or division")

# Example usage
if __name__ == "__main__":
    try:
        a = float(input("Enter first number (a): "))
        b = float(input("Enter second number (b): "))
        op = input("Enter operation (addition/subtraction/multiplication/division): ")
        
        calc = Calculator(a, b, op)
        result = calc.calculate()
        
        print(f"Result of {op}: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
