# 字符串索引
a = "hello word"
# a[0] = h
print(a[0])
# 直接赋值时，使用的是同一个对象
b = a[:]
print(b)
print(id(a))
print(id(b))
# 字符串切片 a[1:4]  索引左闭右开
print(a[1:4])
print('h' in a) # true
print('h' not in a) # false
print(a,'test','sdfsf') # print 中直接， 字符串之间间隔一个 空格
print(a + 'test') # 使用 + 号时，直接字符串拼接，没有空格
print(a*2) # 字符串拼接没有空格
a = "hello word"
b = "THIS a test py file"
print(len(a))
print(len(b))
# 转义字符 \'  \"  
print("\"")
print("\'")
print("this is a \nhaha") # 换行符
print(r"this is a \n hahah") #原始字符串，不作任何转义
print(f"hahah  {a}") #格式化字符串
print(f"a is '{a}'\nb is '{b}'") # 格式化字符串
# 字符串常用函数
# 1. 判断类，返回布尔函数true or false
# isdigit() 字符串只包含数字
print('wr'.isdigit()) # false
print('1234'.isdigit()) # true
# ispace()  字符串只包含空格
print('   s'.isspace())
# join() 注意join 的用法，分隔符放在前面，字符串放在join 中
print('，'.join(a))
# 大小写切换，lower()  upper()
print(a.upper())
print(b.lower())

# str.split() 用括号中的字符切片分割str,返回一个list
print(a.split(' ')) # ['hell','word']
