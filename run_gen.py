import argparse
import os
import sys
from main import MainGenerator

cli_parser = argparse.ArgumentParser(prog='run_gen',
                                     usage='%(prog)s [options]',
                                     description='Database generator')

cli_parser.add_argument('-s', '--seed', action="store", type=int, help='set a seed for generator')

args = cli_parser.parse_args()
main_gen = MainGenerator()

if not len(sys.argv) > 1:
    main_gen.generate_tree_with_random_seed()
    sys.exit()
if args.seed:
    main_gen.generate_tree(args.seed)
    sys.exit()

