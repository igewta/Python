# for 循环基础:  for i in a:

# list 循环
a = [1,2,3,4]
for i in a:
	print(i,end=' ') # 1 2 3 4 

# tuple  循环
b = (4,3,2,1)
print()  # 换行
for i in b:
	print(i,end=' ') # 4 3 2 1

# str 循环
c = 'hello word'
print()
for i in c:
	print(i,end=' ') # h e l l o  w o r d 

# dict 循环
d  = {'a':1,'b':2,'c':3,'d':4}
print()
for k,v in d.items():
	print(k,v) # a 1 \n b 2 \n c 3

# dict 键循环
for k in d.keys():
	print(k)


# break :终止循环，跳出整个循环
# continue ：终止循环，跳出该次循环 ，执行下次循环
# pass : 空语句
print('test break/continue:')
for i in [1,2,3,4]:
	if i == 2:
		break  
	print(i)   # 1 \n2 ,跳出整个循环，不再输出

print('test break/continue:')
for i in [1,2,3,4,5]:
	if i == 3:
		continue
	print(i)   # 1 2 4 5, i == 3 时跳出此次循环，执行i == 4 的循环

if i in a:
	pass # pass