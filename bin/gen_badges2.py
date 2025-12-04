#!/usr/bin/env python3

"""
Script to generate star count badges for README.md
Fork of https://github.com/alexandru-dinu/programming-challenges/blob/main/advent-of-code/.scripts/gen_badges.py
"""

import argparse
import colorsys
import json
import os
import time

import requests


def rgb2hex(r, g, b):
    f = lambda x: max(0, min(255, round(x * 255)))
    return f"{f(r):02x}{f(g):02x}{f(b):02x}"


def hsv_interp(t):
    # 0 - 60 - 120
    assert 0 <= t <= 1
    return rgb2hex(*colorsys.hsv_to_rgb(h=t * 120 / 360, s=1, v=0.6))


# cookie session (see browser tools)
SID = os.getenv("AOC_SESSION")
assert SID is not None

# personal ID (see in AOC Settings)
UID = os.getenv("AOC_UID")
assert UID is not None

USER_AGENT = "https://github.com/KristobalJunta/aoc/blob/master/bin/gen_badges.py"
AOC_URL = "https://adventofcode.com/{year}/leaderboard/private/view/{uid}.json"
STAR = "⭐"
YEARS = list(range(2025, 2014, -1))
NUM_YEARS = len(YEARS)


def fmt_year_badge(year: int, stars: int, color: str) -> str:
    return f"https://img.shields.io/badge/{year}-{stars}%20{STAR}-{color}?style=flat-square"


def fmt_total_badge(stars: int, color: str) -> str:
    return f"https://img.shields.io/badge/total-{stars}%20{STAR}-{color}?style=for-the-badge"


def get_year_stars(year: int) -> int:
    res = requests.get(
        AOC_URL.format(year=year, uid=UID),
        headers={"User-Agent": USER_AGENT},
        cookies={"session": SID},
    )
    assert res.status_code == 200
    time.sleep(0.1)

    data = json.loads(res.text)

    return data["members"][UID]["stars"]


def get_year_badge_url(year: int, stars: int) -> str:
    total_stars = 50 if year < 2025 else 24
    color = hsv_interp(stars / total_stars)

    badge = f'<img src="{fmt_year_badge(year,stars, color)}"></img>'
    badge = f'<a href="./{year}">{badge}</a>'

    return badge


def get_total_badge_url(stars: int) -> str:
    return f'<a href="./README.md"><img src="{fmt_total_badge(stars, "3e3e3e")}"></img></a>'


def gen_badge_links() -> str:
    links = []
    y2s = {y: get_year_stars(y) for y in YEARS}

    for y, s in y2s.items():
        link = get_year_badge_url(y, s)
        links.append(link)

    return links


if __name__ == "__main__":
    for link in gen_badge_links():
        print(link)
