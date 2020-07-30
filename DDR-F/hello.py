#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n - 1, a, c, b)
        print(a, '-->', c)
        move(n - 1, b, a, c)

move(4, 'A', 'B', 'C')
print(2 ** 14)
