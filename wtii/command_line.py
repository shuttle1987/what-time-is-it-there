import argparse
from typing import Dict
import arrow

from tzlocal import get_localzone

parser = argparse.ArgumentParser(description='Find the time where other people are.')
parser.add_argument('--locations', action='store_true', help="List all locations")

parser.add_argument('-d', '--delta', help="Find a time delta from now")
parser.add_argument('-n', '--now', help="Current time (plus offset)")

parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose mode")

local_tz = get_localzone()
current_zone_name = local_tz.zone

def locations() -> Dict[str, str]:
    """Return a dict of the locations of interest along with their time zones"""
    return {
        "Australian Office":"Australia/Melbourne",
        "Canadian Office":"America/Toronto",
        "Chicago":"America/Chicago",
    }

def main() -> None:
    time_format_str: str = "%Y-%m-%d %H:%M:%S"
    args = parser.parse_args()
    if args.locations is True:
        print(locations())
        return None
    utc_now = arrow.utcnow()
    if args.verbose is True:
        print("UTC", utc_now.strftime(time_format_str))
    for loc, tz_loc in locations().items():
        if current_zone_name == tz_loc:
            prefix = "--->"
        else:
            prefix = "****"
        localized_time = utc_now.to(tz_loc)
        localized_day = localized_time.strftime("%A")
        print(f'{prefix} {loc} \t {localized_time.strftime(time_format_str)} ({localized_day})')