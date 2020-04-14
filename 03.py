# !/usr/bin/env python
# -*- coding:utf-8 -*-

from itertools import permutations
# 使用全排列解决
# 定义字符集
str_list = ["铅笔", "混合笔", "原子笔"]
result_list = permutations(str_list)
for i in result_list:
    for j in i:
        print(j, end=" ")
    print()
