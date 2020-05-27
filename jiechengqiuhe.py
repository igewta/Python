def qiuhe():
    sum_ = 0
    a = int(input())
    jie_cheng = 1
    for i in range(1, a+1):
        jie_cheng = jie_cheng * i
        sum_ = sum_ + jie_cheng
    return sum_


if __name__ == '__main__':
    print(qiuhe())
