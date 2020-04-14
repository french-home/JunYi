# !/usr/bin/env python
# -*- coding:utf-8 -*-

def cipher(Digital):
    Count = 0
    for i in range(1, Digital + 1):
        # 判断如果i是3和5的倍数则保留
        if i % 3 == 0 and i % 5 == 0:
            Count = Count + 1
        elif i % 3 == 0 or i % 5 == 0:
            pass
        else:
            Count = Count + 1
    return Count


if __name__ == '__main__':
    # 等待用户输入数据
    Number = int(input("Input:"))
    result = cipher(Number)
    print("OutPut:", result)
