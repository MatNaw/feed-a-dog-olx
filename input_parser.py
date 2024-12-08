import argparse

DEFAULT_ITERATIONS = 15


def check_positive(value):
    try:
        int_value = int(value)
    except ValueError as ex:
        raise argparse.ArgumentTypeError("'{}' is not a valid number: {}".format(value, ex))

    if int_value <= 0:
        raise argparse.ArgumentTypeError("'{}' is not a valid positive integer value".format(value))

    return int_value


def get_input_arguments():
    parser = argparse.ArgumentParser(formatter_class=argparse.ArgumentDefaultsHelpFormatter)
    parser.add_argument("-i", "--iterations", help="set number of script iterations",
                        nargs="?", const=DEFAULT_ITERATIONS, default=DEFAULT_ITERATIONS, type=check_positive)
    parser.add_argument("-v", "--verbose", help="enable or disable more verbose logging",
                        action=argparse.BooleanOptionalAction)

    args = parser.parse_args()
    return args.iterations, args.verbose
