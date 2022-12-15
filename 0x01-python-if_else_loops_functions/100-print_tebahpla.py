#!/usr/bin/python3
num = 0
for x in range(ord('z'), ord('a') - 1, -1):
    print("{}".format(chr(x - num)), end="")
    num = 32 if num == 0 else 0
