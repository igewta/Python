# 列表基础：列表是有序的
a = [1,2,3,4,5,'h','e','word']
# 索引
print(a[0]) #1
print(a[2:6]) # [3,4,5,'h']  左闭右开
b = a[:]
#print(b)

# 新建列表，允许创建空列表,列表的元素可以是数字、字符串、列表
c = [] # 空列表
# 列表添加元素：list.append()
c.append(1)
print(c) # [1]
c.append('hello')
print(c) # [1,'hello']

# 删除列表元素,del list[]
del c[0]
print(c)  # ['hello']

# 列表的 + 和 *
a = ['hello','word']
b = ['this ','is','a','test']
print(a +b ) # ['hello','word','this','is','a','test']
print(a*2) # ['hello','word','hello','word']

# in not in 
print('hello' in a) # true
print('hello' not in a) # false

# for 循环遍历列表
for i in a:
	print(i)

# list(seq) 将元组转换为列表
print(list('hello')) # 将字符串转换为列表
 
# list 方法，list.append(),list.count(),list.extend(),list.insert(index,obj)
# list.reverse() 反向列表中的元素
# list.sort() 对原列表进行排序
# list.pop() 移除列表最后一个元素并返回改值