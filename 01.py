# !/usr/bin/env python
# -*- coding:utf-8 -*-


# 字符串翻转
def f(String):
    # 去除前后空格
    String = String.strip(" ")
    # 判断是否存在空格
    if String.find(" ") >= 0:
        # 根据空格分词
        StringList = String.split(" ")
        # 清除里面的字符串
        String = ""
        for i in StringList:
            i = i[::-1]
            String = String + i + " "
        # 去除前后空格
        String = String.strip(" ")
    else:
        String = String[::-1]
    return String


if __name__ == '__main__':
    SS = f("You Are Money")
    print(SS)
