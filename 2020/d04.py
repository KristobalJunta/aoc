import fileinput
from os import stat
from typing import List
from functools import reduce
import operator
from copy import copy
from pprint import pprint
import re
import string


required_fields = {
    'byr',  # (Birth Year)
    'iyr',  # (Issue Year)
    'eyr',  # (Expiration Year)
    'hgt',  # (Height)
    'hcl',  # (Hair Color)
    'ecl',  # (Eye Color)
    'pid',  # (Passport ID)
    # 'cid',  # (Country ID)
}


class DocValidator:
    def validate(self, doc):
        for k, v in doc.items():
            f = getattr(self, f'validate_{k}', self._nop)
            if not f(v):
                return False
        return True

    @staticmethod
    def _nop(_):
        return True

    @staticmethod
    def _validate_int(val, low, high):
        try:
            assert low <= int(val) <= high
        except:
            return False
        else:
            return True

    # byr (Birth Year) - four digits; at least 1920 and at most 2002.
    def validate_byr(self, val):
        return self._validate_int(val, 1920, 2002)

    # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
    def validate_iyr(self, val):
        return self._validate_int(val, 2010, 2020)

    # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
    def validate_eyr(self, val):
        return self._validate_int(val, 2020, 2030)

    # hgt (Height) - a number followed by either cm or in:
    # If cm, the number must be at least 150 and at most 193.
    # If in, the number must be at least 59 and at most 76.
    def validate_hgt(self, val):
        match = re.match(r"^(\d+)(cm|in)$", val)
        if not match:
            return False
        hgt, unit = match.groups()

        if unit not in ['cm', 'in']:
            return False
        elif unit == 'cm':
            return self._validate_int(hgt, 150, 193)
        else:
            return self._validate_int(hgt, 59, 76)

    # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
    @staticmethod
    def validate_hcl(val):
        return bool(re.match(r'^#[0-9,a-f]{6}$', val))

    # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
    @staticmethod
    def validate_ecl(val):
        return val in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

    # pid (Passport ID) - a nine-digit number, including leading zeroes.
    @staticmethod
    def validate_pid(val):
        return bool(re.match(r'^\d{9}$', val))


def get_input():
    data = [l.strip() for l in fileinput.input()]
    return data


def parse_line(line):
    return {
        k: v for k, v in [
            s.split(':') for s in line.split()
        ]
    }


def convert_data(data):
    res = []
    cur_item = {}
    for line in data:
        if not line:
            res.append(copy(cur_item))
            cur_item = {}

        cur_item.update(parse_line(line))
    if cur_item:
        res.append(cur_item)
    return res


def has_valid_fields(doc):
    return required_fields <= set(doc.keys())


def has_valid_values(doc):
    valid = DocValidator().validate(doc)
    return valid


def part1(docs):
    return len([doc for doc in docs if has_valid_fields(doc)])


def part2(docs):
    # 186 too high
    return len([
        doc for doc in docs
        if has_valid_fields(doc) and has_valid_values(doc)
    ])


if __name__ == '__main__':
    indata = get_input()
    docs = convert_data(indata)

    res1 = part1(docs)
    res2 = part2(docs)

    print(res1)
    print(res2)
