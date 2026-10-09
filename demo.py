import argparse

parser = argparse.ArgumentParser()
parser.add_argument("nama")
args = parser.parse_args()

print("Halo", args.nama, "!")
