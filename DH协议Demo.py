import math
import random


def prime_judgment(n):
    if n <= 1:
        print("%d不是素数,请重新输入" % n)
        return False
    i = 2
    while i*i <= n:
        if n%i ==0:
            print("%d不是素数,请重新输入" % n)
            return False
        i += 1
    print("%d是素数" % n)
    return True


def get_original(n):
    a = 1
    o_list = []
    while a < n:
        flag = 1
        while flag !=n:
            if (a**flag)%n == 1:
                break
            flag += 1
        if flag == (n-1):
            o_list.append(a)
        a += 1
    return o_list


def get_y(n, a, x):
    y = (a ** x) % n
    return y


def get_key(x, y, n):
    k = (y ** x) % n
    return k


if __name__ == '__main__':
    print("请输入一个素数：")
    flag = False
    while flag == False:
        n = int(input())
        flag = prime_judgment(n)
    a = get_original(n)
    print("%d的最大原根是：" % n)
    print(a[-1])
    Xa = random.randint(0, n - 1)
    print("Alice生成随机数：%d" % Xa)
    Xb = random.randint(0, n - 1)
    print("Bob生成随机数：%d" % Xb)
    Ya = get_y(n, a[-1], Xa)
    print("Alice的计算结果为：%d" % Ya)
    Yb = get_y(n, a[-1], Xb)
    print("Bob的计算结果为：%d" % Yb)
    Ka = get_key(Xa, Yb, n)
    print("Alice的密钥结果为：%d" % Ka)
    Kb = get_key(Xb, Ya, n)
    print("Bob的密钥结果为：%d" % Kb)
    if Kb == Ka:
        print("Alice和Bob两人的密钥为%d"% Ka)
    else:
        print("Unknown Error")