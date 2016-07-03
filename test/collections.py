#!/usr/bin/env python
# -*-coding:utf-8 -*-
# list
classmates = ["wowo", "lili", "huanhuan", "xiaoxiao"]
print classmates
classmates.append("dada")
print classmates
classmates.pop(3)
print classmates
# tuple(与list的区别在于不可变)
classmates = ("wowo", "lili", "huanhuan", "xiaoxiao")
print classmates
classmates = ("wowo")
print classmates
# dict(与Java中的map类似)
dict = {"wowo": 100, "xiaoxiao": 90}
print dict
print dict["wowo"]
# set(要创建一个set，需要提供一个list作为输入集合)
set = set(["wowo", "lili", "xiaoxiao"])
print set
set.add("dada")
print set
