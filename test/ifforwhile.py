#!/usr/bin/env python
# -*-coding:utf-8-*-
# if语句
# 注意用int()强制转换为int类型
birth = int(raw_input('birth: '))
if birth < 2000:
    print '00前'
else:
    print '00后'

# for循环(range(101)就可以生成0-100的整数序列)
sum = 0
for x in range(101):
    sum = x + sum
print sum
# while循环
n = 100
sum = 0
while n > 0:
    sum = n + sum
    n = n - 1
print sum
