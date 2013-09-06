import argparse
from sys import stdout
from time import sleep


def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)


def gen_fib():
    yield 0
    yield 1
    a, b = 0, 1
    while True:
        yield a + b
        a, b = b, a + b


def display(num):
    stdout.write("%s " % num)
    stdout.flush()
    sleep(0.1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fibonacci number to the Nth position in the sequence")
    parser.add_argument(
        'num',
        type=int,
        help="Number of digits of PI to show."
    )
    parser.add_argument(
        '--efficient',
        default=False,
        help="Use generator method to calculate. Default: False",
        action="store_true"
    )
    args = parser.parse_args()

    gen = gen_fib()
    for num in xrange(args.num):
        if args.efficient:
            display(gen.next())
        else:
            display(fib(num))