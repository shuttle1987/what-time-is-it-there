import argparse
from typing import List

parser = argparse.ArgumentParser(description='Find the time where other people are.')
parser.add_argument('--locations', action='store_true', help="List all locations")

def locations() -> List:
    raise NotImplementedError

def main() -> None:
    args = parser.parse_args()
    if args.locations is True:
        print(locations())