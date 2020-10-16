#!/usr/bin/env python3
import os
import sys
from configparser import ConfigParser
from datetime import date
from inspect import cleandoc
from typing import List, Tuple

import requests


usage = """
get_input.py [year day]

If year and day are provided - gets input for that particular day.
Else tries to get input for current date (works only in December).
"""

input_url = "https://adventofcode.com/{}/day/{}/input"

config = ConfigParser()
assert os.path.isfile("config.ini"), "Create and fill config.ini file"
config.read("config.ini")


def get_year_day(args: List[str]) -> Tuple[str, str]:
    if len(args) not in [0, 2]:
        print(cleandoc(usage))
        sys.exit(1)

    if args:
        year, day = args
    else:
        today = date.today()
        if today.month != 12:
            print("The magic only works in December!")
            sys.exit(1)

        year, day = str(today.year), str(today.day)

    return year, day


def get_input(year: str, day: str, *, force: bool = False) -> str:
    print(f"Gettng input for {year} day {day}")
    dir_path = os.path.join(year, f"d{day.rjust(2, '0')}")
    if not os.path.isdir(dir_path):
        os.makedirs(dir_path)
    infile_path = os.path.join(dir_path, "input.txt")
    if os.path.isfile(infile_path) and not force:
        print("Using cached input file")
        with open(infile_path) as f:
            return f.read()
    else:
        try:
            session_cookie = config["aoc"]["session_cookie"]
            assert session_cookie
        except (AssertionError, KeyError):
            print("set session cookie in config")
            sys.exit(1)

        r = requests.get(input_url.format(year, day), cookies={"session": session_cookie})
        assert r.status_code == 200, "Failed to get input from website"
        with open(infile_path, "w") as f:
            f.write(r.text)
        return r.text


def main():
    args = sys.argv[1:]
    year, day = get_year_day(args)
    get_input(year, day)


if __name__ == "__main__":
    main()
