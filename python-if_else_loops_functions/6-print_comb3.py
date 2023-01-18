#!/usr/bin/python3
for n in range(10):
    for i in range(10):
        if i == n:
            continue
        if i < n:
            continue
        if n < 9 and i != 1:
            print(", ", end="")
            if n == 8 and i == 9:
                print("89\n")
        print("{}{}".format(n, i), end="")
