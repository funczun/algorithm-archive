# https://www.acmicpc.net/problem/10952

import sys

A, B = True, True

while A and B:
    A, B = map(int, sys.stdin.readline().split())
    if A != 0 and B != 0:
        print(A + B)