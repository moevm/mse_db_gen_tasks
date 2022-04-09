import argparse
import os
import sys
from main import MainGenerator


def main():
    cli_parser = argparse.ArgumentParser(prog='run_gen',
                                         usage='%(prog)s [options]',
                                         description='Database generator')

    cli_parser.add_argument('-s', '--seed', action="store", type=int, help='set a seed for generator')
    cli_parser.add_argument('-d', '--dump', action="store", type=str, help='dump database', default='dump_file.txt')

    args = cli_parser.parse_args()
    main_gen = MainGenerator()

    if not len(sys.argv) > 1:
        main_gen.generate_tree_with_random_seed()
        sys.exit()
    if args.seed:
        main_gen.generate_tree(args.seed)
        sys.exit()
    if args.dump:
        main_gen.dump_db(args.dump)
        sys.exit()


if __name__ == "__main__":
    main()
