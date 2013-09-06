import argparse
from sys import stdout
from time import sleep


def fibonacci(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)


def gen_fib():
    yield 0
    yield 1
    a, b = 0, 1
    while True:
        yield a + b
        # Mmmm... Python magic to preserve a when assigning b to a + b.
        a, b = b, a + b


def display(num):
    stdout.write("%s " % num)
    stdout.flush()
    sleep(0.1)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Fibonacci number to the Nth position in the sequence")
    terminal_or_continue = parser.add_mutually_exclusive_group()
    parser.add_argument(
        '--hateful',
        default=False,
        help="Use recursive method to calculate. (Default: False)",
        action="store_true"
    )
    terminal_or_continue.add_argument(
        '-n',
        type=int,
        help="Number of Fibonacci Numbers to show."
    )
    terminal_or_continue.add_argument(
        '--continuous',
        default=False,
        help="Continue calculating until your machine falls apart." +
             " (Default: False)",
        action="store_true"
    )
    args = parser.parse_args()

    # Get a new Fibonacci Number generator.
    fib = gen_fib()
    while args.continuous:
        display(fib.next())
    for num in xrange(args.n):
        if args.hateful:
            display(fibonacci(num))
        else:
            display(fib.next())
