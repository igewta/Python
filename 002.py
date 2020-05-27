import copy
a = [[1,2],[3,4],5,6]
b = copy.copy(a)
a[0][0] = '00'
print(a)
print(b)
