# -*- coding:utf-8 -*-
# author:
#
"""
生成菲波那切数列
"""


def fei_bo(n):
    """
    限定菲波那切数列的最大值
    :param n:
    :return:
    """
    a = 1
    b = 1
    arr_list = [1, 1]
    print(a, end=" ")
    while b < n:
        print(b, end=" ")
        a, b = b, a+b
        arr_list.append(b)
    return arr_list


def fei_bo2(n):
    """
    返回固定项数的斐波那契数列
    :param n:
    :return:
    """
    a = 1
    b = 1
    arr_list = [1, 1]
    print(a, b, end=" ")
    for i in range(1, n-1):
        a, b = b, a+b
        print(b, end=" ")
        arr_list.append(b)
    return arr_list


if __name__ == '__main__':
    arr = fei_bo(1000)
    print()
    print(type(arr))
    arr = fei_bo2(10)
    print()
    print(arr)
