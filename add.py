import sys


def add_numbers(a, b):
    return a + b


if __name__ == "__main__":
    # Check if the user provided exactly two arguments (plus the script name)
    if len(sys.argv) != 3:
        print("❌ Error: Please provide exactly two numbers.")
        print("Usage: python script.py <number1> <number2>")
        sys.exit(1)

    try:
        # Convert arguments to integers
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])

        result = add_numbers(num1, num2)

        # Print the formatted result
        print("=================================")
        print("Addition Result")
        print("=================================")
        print(f"First Number : {num1}")
        print(f"Second Number: {num2}")
        print(f"Sum          : {result}")

    except ValueError:
        print(
            "❌ Error: Both arguments must be valid integers (e.g., 5, 10)."
        )
        sys.exit(1)
