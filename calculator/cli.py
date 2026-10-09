import argparse
from calculator import core


def main() -> None:
    parser = argparse.ArgumentParser(description="Kalkulator CLI sederhana")
    parser.add_argument("a", type=float, help="Angka pertama")
    parser.add_argument("b", type=float, help="Angka kedua")
    parser.add_argument(
        "--op",
        choices=["add", "sub", "mul", "div"],
        required=True,
        help="Operasi: add | sub | mul | div",
    )
    args = parser.parse_args()

    if args.op == "add":
        hasil = core.tambah(args.a, args.b)
    elif args.op == "sub":
        hasil = core.kurang(args.a, args.b)
    elif args.op == "mul":
        hasil = core.kali(args.a, args.b)
    elif args.op == "div":
        hasil = core.bagi(args.a, args.b)
    else:
        raise ValueError(f"operasi tidak dikenal: {args.op}")

    print(f"Hasil: {hasil}")


if __name__ == "__main__":
    main()
