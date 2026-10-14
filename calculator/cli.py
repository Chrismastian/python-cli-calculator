import argparse
from calculator import core


def main() -> None:
    parser = argparse.ArgumentParser(description="Simple CLI calculator")
    parser.add_argument("a", type=float, help="First number")
    parser.add_argument("b", type=float, help="Second number")
    parser.add_argument(
        "--op",
        choices=["add", "sub", "mul", "div"],
        required=True,
        help="Operation: add | sub | mul | div",
    )
    args = parser.parse_args()

    if args.op == "add":
        result = core.add(args.a, args.b)
    elif args.op == "sub":
        result = core.subtract(args.a, args.b)
    elif args.op == "mul":
        result = core.multiply(args.a, args.b)
    elif args.op == "div":
        result = core.divide(args.a, args.b)
    else:
        raise ValueError(f"unknown operation: {args.op}")

    print(f"Result: {result}")


if __name__ == "__main__":
    main()
