import argparse
from sys import stdout

def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fibonacci number to the Nth position in the sequence")
    parser.add_argument('num', type=int, help="Number of digits of PI to show.")
    args = parser.parse_args()

    for num in range(1, args.num):
        stdout.write("%s " % str(fib(num)))
        stdout.flush()
