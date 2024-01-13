#!/usr/bin/python3

def uppercase(s):
    result = ""
    for char in s:
        result += "{:c}".format(ord(char) - 32) if 'a' <= char <= 'z' else "{:c}".format(ord(char))
    print(result)

if __name__ == "__main__":
    uppercase("holberton")
    uppercase("Holberton School")
    uppercase("Holberton School, 98 battery street")
    uppercase("")
    uppercase("98")
    uppercase("z")

