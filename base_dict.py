# 字典基础：键值对的形式，无序    ，key:value,key 必须是不可变的，如str ,数字，tuple

dict = {'a':1,'b':2,'c':3}

# 查询，以键做索引
print(dict['b']) #2

# 修改键值对
dict['b'] = 22
print(dict) # {'a':1,'b':22,'c':3}

# 删除键值对
del dict['b']
print(dict) # {'a':1,'c':3}

# dict.clear()  清空字典所有茨木
# del dict  删除字典

# len(dict) 字典元素个数，即键的总数
# str(dict) 输出字典可打印的字符串表示
print('字符串表示:',str(dict))
print(type(str(dict)))  # str

# 用for 循环表里dict 
for k,v in dict.items():
	print(k,v)

# dict.get() 无此键时不会报错，无输出
#print(dict['hah']) # 报错
print(dict.get('hah')) # 无输出，None

