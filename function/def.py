#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Created by zyf on 2018/11/27.
#定义默认参数要牢记一点：默认参数必须指向不变对象！注意一下两个函数的区别
#默认参数
def add_end(L=[]):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end())
print(add_end())

def add_end2(L=None):
    if L is None:
        L = []
    L.append('END')
    return L
print(add_end2())
print(add_end2())

#可变参数  这*用的很灵性
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum
print(calc(1,2,3))

nums = [1, 2, 3]
print(calc(*nums))