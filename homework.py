import random


def homework1():
    s = "JanFebMarAprMayJunJulAugSepOctNovDes"
    x = int(input())
    print(s[3 * (x - 1):3 * x])


def homework2():
    s = input()
    a, b, c, d = 0, 0, 0, 0
    for i in s:
        if str.isupper(i):
            a += 1
        elif str.islower(i):
            b += 1
        elif str.isdigit(i):
            c += 1
        else:
            d += 1
    print(a, b, c, d)


def homework3():
    s = "QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm0123456789"
    res = ""
    for i in range(4):
        res += s[random.randint(0, len(s) - 1)]
    print(res)
    if res == input():
        print("success")
    else:
        print("fail")
