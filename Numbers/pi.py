import argparse
from sympy.mpmath import mp

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="PI to the Nth digit")
    parser.add_argument('num', type=int, help="Number of digits of PI to show.")
    args = parser.parse_args()

    mp.dps = args.num
    print mp.pi
