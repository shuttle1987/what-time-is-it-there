import argparse
from typing import Dict
import arrow

from tzlocal import get_localzone

parser = argparse.ArgumentParser(description='Find the time where other people are.')
parser.add_argument('--locations', action='store_true', help="List all locations")

parser.add_argument('-d', '--delta', help="Find a time delta from now")
parser.add_argument('-n', '--now', help="Current time (plus offset)")

parser.add_argument('-v', '--verbose', action='store_true', help="Enable verbose mode")

def locations() -> Dict[str, str]:
    """Return a dict of the locations of interest along with their time zones"""
    return {
        "Australian Office":"Australia/Melbourne",
        "Canadian Office":"America/Toronto",
        "Chicago":"America/Chicago",
    }


def printer(*, current_utc_time, current_location, locations: dict, format_str: str) -> str:
    """Pretty print the current locations"""
    results = []
    current_zone_name = current_location.zone
    for loc, tz_loc in locations.items():
        if current_zone_name == tz_loc:
            prefix = "--->"
        else:
            prefix = "****"
        localized_time = current_utc_time.to(tz_loc)
        localized_day = localized_time.strftime("%A")
        results.append(f'{prefix} {loc} \t {localized_time.strftime(format_str)} ({localized_day})')
    return '\n'.join(results)

def main() -> None:
    time_format_str: str = "%Y-%m-%d %H:%M:%S"
    args = parser.parse_args()
    locs = locations()
    if args.locations is True:
        print(locs)
        return None
    utc_now = arrow.utcnow()

    if args.verbose is True:
        if "UTC" not in locs:
            locs['UTC'] = 'UTC'

    local_tz = get_localzone()

    formatted_times: str = printer(
        current_utc_time=utc_now,
        current_location=local_tz,
        locations=locs,
        format_str=time_format_str
        )
    print(formatted_times)