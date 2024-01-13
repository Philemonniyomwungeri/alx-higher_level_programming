#!/usr/bin/python3
def uppercase(s):
    for char in s:
        print("{:c}".format(ord(char - 32) if 'a' <= char <= 'z' else ord(char)), end="")
    print()

if __name__ == "__main__":
    uppercase = __import__('8-uppercase').uppercase

    uppercase("best")
    uppercase("Best School 98 Battery street")

