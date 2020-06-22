"""
阶乘，以及阶乘求和
"""
# def qiuhe():
#     sum_ = 0
#     a = int(input())
#     jie_cheng = 1
#     for i in range(1, a+1):
#         jie_cheng = jie_cheng * i
#         sum_ = sum_ + jie_cheng
#     return sum_
#
#
# if __name__ == '__main__':
#     print(qiuhe())


# 重写一遍，阶乘求和
def qiu_he():

    n = int(input())
    s = 0
    tmp = 1
    for i in range(1, n+1):
        tmp = tmp * i
        s = s + tmp
    return s


def jie():
    n = int(input())
    s = 1
    for i in range(1, n+1):
        s = s * i
    return s


if __name__ == '__main__':
    print(qiu_he())
    print(jie())
