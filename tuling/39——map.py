# -*- coding:utf-8 -*-

"""
文件说明：
利用map()函数 把list 列表中的英文名称变成标准的首字母大写,['JACK', 'ALIbaba', 'baidu']

"""
def starderd(s):
    t = s.lower()
    t = t.capitalize()
    return  t

new_list = list(map(starderd, ['JACK', 'ALIbaba', 'baidu']))
print(new_list)


'''
打印回数，从左向右读和从右向左读都是一样的数，比如12321,999，利用filter()函数
'''
def equal(a, b):
    return a == b

def is_palindrome(n):
    s = str(n)
    for i in range(len(s)-1):
        if equal(s[i], s[len(s)-i-1]):
            continue
        else:
            return False
    return True


output = filter(is_palindrome, range(1, 1000))
print("1-1000:", list(output))

'''
假设，我们用一组tuple 来表示学生的名称和成绩，L  = [('Bob', 75), ('ADAM', 92), ('HAHA', 66), ('lISA', 89)],利用sorted 对上述列表进行名称排序

'''
L = [('Bob', 75), ('ADAM', 92), ('HAHA', 66), ('lISA', 89)]

def by_name(t):
    t = sorted(t[0], key=str.lower)# 这是什么鬼？
    return t

l2 = sorted(L, key=by_name)
print(l2)

# 根据成绩排序
def by_score(t):
    t =  sorted(range(t[1]), key=abs)
    return t

l3 = sorted(L, key=by_score)
print(l3)