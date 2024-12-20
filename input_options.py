import argparse

DEFAULT_ITERATIONS = 15
DEFAULT_VERBOSE = False
DEFAULT_HEADLESS = True
DEFAULT_THREADS = 3


def check_positive(value):
    try:
        int_value = int(value)
    except ValueError as ex:
        raise argparse.ArgumentTypeError("'{}' is not a valid number: {}".format(value, ex))

    if int_value <= 0:
        raise argparse.ArgumentTypeError("'{}' is not a valid positive integer value".format(value))

    return int_value


def get_input_options():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--iterations", help="set number of script iterations",
                        nargs="?", const=DEFAULT_ITERATIONS, default=DEFAULT_ITERATIONS, type=check_positive)
    parser.add_argument("-v", "--verbose", help="enable or disable more verbose logging",
                        action=argparse.BooleanOptionalAction, default=DEFAULT_VERBOSE)
    parser.add_argument("-hl", "--headless", help="enable or disable browser's headless mode",
                        action=argparse.BooleanOptionalAction, default=DEFAULT_HEADLESS)
    parser.add_argument("-t", "--threads", help="set number of parallel script threads",
                        nargs="?", const=DEFAULT_THREADS, default=DEFAULT_THREADS, type=check_positive)

    args = parser.parse_args()
    return args.iterations, args.verbose, args.headless, args.threads


class InputOptions:
    iterations = DEFAULT_ITERATIONS
    verbose = DEFAULT_VERBOSE
    headless = DEFAULT_HEADLESS
    threads = DEFAULT_THREADS

    def __init__(self):
        self.iterations, self.verbose, self.headless, self.threads = get_input_options()
