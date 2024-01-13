#!/usr/bin/python3
def uppercase(s):
    result = ""
    for char in s:
        result += "{:c}".format(ord(char - 32) if 'a' <= char <= 'z' else ord(char))
    print(result)

if __name__ == "__main__":
    uppercase("best")
    uppercase("Best School 98 Battery street")

