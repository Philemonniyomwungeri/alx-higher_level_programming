#!/usr/bin/python3
for c in range(ord('z'), ord('a') - 1, -1):
    print("{:c}".format(c - (32 * (c % 2))), end="")

