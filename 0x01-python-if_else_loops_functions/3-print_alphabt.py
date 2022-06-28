#!/usr/bin/python3
i = ord('a')
while i < ord('z') + 1:
    if i != 101 and i != 113:
        print("{:c}".format(i), end='')
    i += 1
