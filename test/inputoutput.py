#!/usr/bin/env python
# -*- coding: utf-8 -*-
#标准输入和输出
#由于Python源代码也是一个文本文件，所以，当你的源代码中包含中文的时候，
# 在保存源代码时，就需要务必指定保存为UTF-8编码。当Python解释器读取源代码时，
# 为了让它按UTF-8编码读取，我们通常在文件开头写上开头的两行。
#输入姓名，并打印出来
name = raw_input("input your name please:")
print "hello,",name
print"我是中国人"