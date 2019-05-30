# 元组基础：不可变序列，小括号表示(1,2,'1','2')
# 空元组  tup = ()  ,tup = (50,),只有一个元素时要加逗号
# 元组索引切片
tup = (1,2,3,4,5)
print(tup[1]) #2
print(tup[1:4]) #(2,3,4) ,元组切片后仍是个元组，列表切片后仍是个列表，字符串切片后仍是个字符串

# 元组的 + 和 * ，创建一个新元组（list str tuple 都可用）
tup2 = (6,7,8)
print(tup+tup2) # (1...8)
print(tup*2) #(1..5,1,2,3,4,5,)

# 元组的删除，单个元素不可删除，只能删除整个元组
#del tup
print(tup)
# in not in 
print(2 in tup) # true
print(9 in tup) # false

# tuple() 将列表转换为元组
print(tuple([1,2,3,4]))  # (1,2,3,4)