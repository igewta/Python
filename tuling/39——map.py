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
print("L:", L)

print(type(list(range(100))))
'''
lambda 匿名函数
'''
l = lambda x: x*2, [1, 2, 3]
print(l)

'''
按照权重排序，函数式编程，权重是100，价格占得权重40%，销量占的权重17%，评级占得权重13%，评论占得权重30%
'''

goods = [{"name": "good1", "price": 200, "sales": 100, "stars": 5, "comment": 400},
         {"name": "good2", "price": 300, "sales": 300, "stars": 3, "comment": 400},
            {"name": "good3", "price": 2800, "sales": 1500, "stars": 5, "comment": 3200}]

def my_sorted(arg):#  关于函数的参数问题，*，** 和arg 之类的
    price = arg['price']
    sales = arg['sales']
    stars = arg['stars']
    comment = arg['comment']
    data = price * 0.4 + sales * 0.17 + stars * 0.13 + comment * 0.3
    return data


print(sorted(goods, key=my_sorted))
print(sorted(goods, key=lambda x:x['price'] * 0.4 +x['sales']*0.17+x['stars']*0.13+x['comment']*0.3, reversed=True) )