import argparse
from typing import Dict
import arrow

parser = argparse.ArgumentParser(description='Find the time where other people are.')
parser.add_argument('--locations', action='store_true', help="List all locations")

parser.add_argument('-d', '--delta', help="Find a time delta from now")
parser.add_argument('-n', '--now', help="Current time (plus offset)")


def locations() -> Dict[str, str]:
    """Return a dict of the locations of interest along with their time zones"""
    return {"Australian Office":"Australia/Melbourne",
            "Canadian Office":"America/Toronto"}

def main() -> None:
    args = parser.parse_args()
    if args.locations is True:
        print(locations())
        return None
    utc_now = arrow.utcnow()
    print("UTC", utc_now)
    for loc, tz_loc in locations().items():
        print(loc, utc_now.to(tz_loc))
