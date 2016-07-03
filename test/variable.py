#!/usr/bin/env python
# -*-coding:utf-8-*-
# 类型和变量
# 整数
n = 1
print isinstance(n, int)
# 浮点数
n = 1.23e9
print isinstance(n, float)
# 字符串
data = "wowo is a beautiful girl"
print isinstance(data, str)
# 不转义字符
print r"wowo \n  is "
# 转义字符
print "wowo \n is "
# 布尔
s = True
m = False
print isinstance(s, bool)
# 布尔值可以用and、or和not运算
print s and m
print s or m
print not m
# 空值
print None
# 变量(python是动态语言，变量类型不固定，Java是静态语言，变量类型固定)
a = "wowo"
print a
#常量
PI =3.1415926
print PI
