import sys

def main() -> None:
    match sys.argv[1:]:
        case [arg1, arg2]:
            try:
                num1, num2 = int(arg1), int(arg2)

                print(
                    "=================================\n"
                    "Addition Result\n"
                    "=================================\n"
                    f"First Number : {num1}\n"
                    f"Second Number: {num2}\n"
                    f"Sum          : {num1 + num2}"
                )

            except ValueError:
                print("Error: Inputs must be integers.", file=sys.stderr)
                sys.exit(1)

        case _:
            print("Usage: python addition.py <num1> <num2>", file=sys.stderr)
            sys.exit(1)

if __name__ == "__main__":
    main()