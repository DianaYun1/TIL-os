import sys
sys.stdin = open("input.txt", "r")

pri = {'+':1, '*':2}
t = 10
for tc in range(1, 1+t):
    n = int(input())
    st = input()
