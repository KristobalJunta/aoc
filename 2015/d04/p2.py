#!/usr/bin/env python3
import sys
from hashlib import md5

secret = sys.stdin.readline().strip()

i = 0

while True:
    digest = md5(f"{secret}{i}".encode("utf-8")).hexdigest()
    if digest.startswith("000000"):
        print(i)
        break

    i += 1
