#!/usr/bin/python3
def uppercase(str):
    for char in str:
        if ord('a') <= ord(char) <= ord('z'):
            print("{:c}".format(ord(char) - ord('a') + ord('A')), end="")
        else:
            print("{:c}".format(ord(char)), end="")
    print()

if __name__ == "__main__":
    uppercase = __import__('8-uppercase').uppercase

    uppercase("best")
    uppercase("Best School 98 Battery street")

