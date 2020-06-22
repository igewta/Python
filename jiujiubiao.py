"""
九九乘法表
"""
for i in range(1, 10):
    for j in range(1, i+1):
        print(f"{j} * {i} = {i*j: >4.1f}", end="    ")
        # 对齐方式 f"{x:*>4}",* 填充符， ><^ 对齐方式，4 保留位数,.2f 浮点数小数点后的位数保留
    print(end="\n")

