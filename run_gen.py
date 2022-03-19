import argparse
import os
import sys

cli_parser = argparse.ArgumentParser(prog='run_gen',
                                     usage='%(prog)s [options]',
                                     description='Database generator')

cli_parser.add_argument('-s', '--seed', action="store", type=int, help='set a seed for generator')

args = cli_parser.parse_args()

if not len(sys.argv) > 1:
    print(0)
    sys.exit()
if args.seed:
    print(args.seed)

