#!/usr/bin/python3
for letter in range(90, 64, -1):
    if (not (letter % 2)):
        letter += 32
    print('{}'.format(chr(letter)), end='')
