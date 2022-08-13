# 문자열 -> 정수
def atoi(s):
    i = 0
    for x in s:
        i = i*10 + ord(x)-ord('0')
    return i

s = '130'
print(atoi(s))

# 정수 -> 문자열
def itoa(n):
    str = ''
    while n>0:
        str = chr(n%10 + ord('0')) + str
        n //= 10

    return str

n = 130
print(itoa(n))