import argparse
import json
import sys

from .parse_compile import load, loads

parser = argparse.ArgumentParser(description='Runs recognition/rep counting tests.')
parser.add_argument('-o', '--output', nargs=1, default=None)
parser.add_argument('paths', metavar='PATH', type=str, nargs='+',
                    help='paths to files or directories')

EXTENSION = ".jsonk"

if __name__ == '__main__':
    args = parser.parse_args()

    if len(args.paths) > 0 and args.output:
        print("-o cannot be used with multiple input files.")
        sys.exit(1)

    for filepath in args.paths:
        if args.output is None:
            args.output = filepath.replace(EXTENSION, ".json")

        if filepath.endswith(EXTENSION):
            with open(args.output, 'w') as f:
                json.dump(load(open(filepath, 'r')), f)
