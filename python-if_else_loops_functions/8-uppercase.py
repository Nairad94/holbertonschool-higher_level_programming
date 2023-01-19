#!/usr/bin/python3
def uppercase(str):
    p = ""
    for n in str:
        if ord(n) >= 96 and ord(n) <= 123:
            p += chr(ord(n)-32)
        else:
            p += n
    print("{}".format(p))
